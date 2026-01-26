#!/usr/bin/env python3
"""
Автоматический импортер документов из Google Drive в структуру VK-offee B.COFFEE

Этот скрипт:
1. Читает ВСЕ файлы из папки Google Drive
2. Конвертирует Google Docs → Markdown, Sheets → CSV/Markdown
3. Автоматически распределяет по структуре SRT 3×3
4. Добавляет YAML frontmatter к каждому документу
5. Создает коммит с импортированными файлами

Использование:
    python3 auto-import-gdrive.py [--dry-run] [--priority 1]

Параметры:
    --dry-run       Показать что будет импортировано, но не создавать файлы
    --priority N    Импортировать только Priority N документы (1, 2, 3)
    --all           Импортировать ВСЕ документы (по умолчанию)
"""

import os
import sys
import json
import re
import argparse
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Optional, Tuple

# Отключаем SSL предупреждения (только для локального использования!)
import urllib3
urllib3.disable_warnings()
os.environ['PYTHONHTTPSVERIFY'] = '0'
os.environ['CURL_CA_BUNDLE'] = ''
os.environ['REQUESTS_CA_BUNDLE'] = ''

try:
    from google.oauth2.credentials import Credentials
    from googleapiclient.discovery import build
    from googleapiclient.http import MediaIoBaseDownload
    import httplib2
    import google_auth_httplib2
    import io
except ImportError:
    print("❌ Ошибка: Не установлены Google API библиотеки!")
    print("\nУстановите:")
    print("pip install google-auth-oauthlib google-auth-httplib2 google-api-python-client")
    sys.exit(1)


# ============================================================================
# КОНФИГУРАЦИЯ МАППИНГА: Google Drive папки → SRT структура
# ============================================================================

FOLDER_MAPPING = {
    # Папка БАР → F5 (Архитектура) + F6 (Операции)
    'БАР': {
        'recipes': {
            'path': 'B.COFFEE/content/2.VkusnyCoffeeNetwork/2.2.Architecture/bar',
            'family': 'F5',
            'category': 'Продуктовая архитектура',
            'tags': ['рецепты', 'бар', 'напитки']
        },
        'operations': {
            'path': 'B.COFFEE/content/2.VkusnyCoffeeNetwork/2.3.Operations/bar',
            'family': 'F6',
            'category': 'Операционные процессы',
            'tags': ['инструкции', 'бар', 'оборудование']
        }
    },

    # Папка КУХНЯ → F5 (Рецепты) + F6 (Операции)
    'КУХНЯ': {
        'recipes': {
            'path': 'B.COFFEE/content/2.VkusnyCoffeeNetwork/2.2.Architecture/recipes',
            'family': 'F5',
            'category': 'Продуктовая архитектура',
            'tags': ['рецепты', 'кухня', 'еда']
        },
        'operations': {
            'path': 'B.COFFEE/content/2.VkusnyCoffeeNetwork/2.3.Operations',
            'family': 'F6',
            'category': 'Операционные процессы',
            'tags': ['кухня', 'процессы']
        },
        'meetings': {
            'path': 'B.COFFEE/content/2.VkusnyCoffeeNetwork/2.3.Operations/meetings',
            'family': 'F6',
            'category': 'Управление операциями',
            'tags': ['планерки', 'протоколы', 'встречи']
        }
    },

    # Папка ПЕРСОНАЛ → F9 (Команда)
    'ПЕРСОНАЛ': {
        'path': 'B.COFFEE/content/3.ManagementTeam/3.3.Operations/roles/job-descriptions',
        'family': 'F9',
        'category': 'Роли и обязанности',
        'tags': ['должностные-инструкции', 'персонал', 'роли']
    },

    # Папка ФИНАНСЫ → F7 (Бизнес-модель)
    'ФИНАНСЫ': {
        'path': 'B.COFFEE/content/3.ManagementTeam/3.1.Meaning/finance',
        'family': 'F7',
        'category': 'Финансы и бизнес-модель',
        'tags': ['финансы', 'калькуляция', 'бюджет']
    },

    # Папка ПОСТАВЩИКИ → F8 (Инструменты)
    'ПОСТАВЩИКИ': {
        'path': 'B.COFFEE/content/3.ManagementTeam/3.2.Architecture/vendors/suppliers',
        'family': 'F8',
        'category': 'Поставщики и партнеры',
        'tags': ['поставщики', 'прайс-листы', 'контракты']
    },

    # Папка ДОКУМЕНТЫ → F0 (Управление)
    'ДОКУМЕНТЫ': {
        'path': 'B.COFFEE/content/0.Management',
        'family': 'F0',
        'category': 'Управление хранилищем',
        'tags': ['документы', 'реквизиты', 'юридическое']
    },

    # Папка ОБУЧЕНИЕ → F9 (Команда)
    'ОБУЧЕНИЕ': {
        'path': 'B.COFFEE/content/3.ManagementTeam/3.3.Operations/training',
        'family': 'F9',
        'category': 'Обучение и развитие',
        'tags': ['обучение', 'тренинги', 'программы']
    },

    # Папка ОПЕРАЦИОННЫЙ МЕНЕДЖЕР → F6 (Операции)
    'ОПЕРАЦИОННЫЙ МЕНЕДЖЕР': {
        'path': 'B.COFFEE/content/3.ManagementTeam/3.3.Operations/roles',
        'family': 'F9',
        'category': 'Роли и обязанности',
        'tags': ['операционный-менеджер', 'управление', 'роли']
    },

    # Папка МАРКЕТИНГ → F1-F3 (Надсистема)
    'МАРКЕТИНГ': {
        'path': 'B.COFFEE/content/1.HoReCaMarket/1.3.Operations',
        'family': 'F3',
        'category': 'Маркетинг и продвижение',
        'tags': ['маркетинг', 'реклама', 'стратегия']
    },

    # Папка ДИЗАЙН И БРЕНД → F5 (Архитектура)
    'ДИЗАЙН': {
        'path': 'B.COFFEE/content/2.VkusnyCoffeeNetwork/2.2.Architecture/branding',
        'family': 'F5',
        'category': 'Брендинг и дизайн',
        'tags': ['дизайн', 'брендбук', 'визуал']
    }
}


# Ключевые слова для определения типа документа
KEYWORDS_MAPPING = {
    'рецепт': 'recipes',
    'технологическ': 'recipes',
    'меню': 'recipes',
    'инструкция': 'operations',
    'протокол': 'meetings',
    'планерка': 'meetings',
    'должностн': 'job-descriptions',
    'вакансия': 'job-descriptions',
    'прайс': 'suppliers',
    'поставщик': 'suppliers',
    'калькуляция': 'finance',
    'себестоимость': 'finance',
    'бюджет': 'finance'
}


# Priority mapping
PRIORITY_MAPPING = {
    1: [  # Критически важные
        'технологическ', 'рецепт', 'протокол', 'планерка',
        'должностная инструкция повар', 'должностная инструкция ом',
        'инструкция.*кофемашин'
    ],
    2: [  # Важные
        'финанс', 'бюджет', 'поставщик', 'контракт',
        'обучение', 'программа', 'kpi'
    ],
    3: [  # Желательные
        'маркетинг', 'дизайн', 'видео', 'фото'
    ]
}


class GoogleDriveImporter:
    """Автоматический импортер из Google Drive"""

    def __init__(self, token_file='token.json', dry_run=False, priority=None):
        self.dry_run = dry_run
        self.priority_filter = priority
        self.stats = {
            'total_files': 0,
            'imported': 0,
            'skipped': 0,
            'errors': 0
        }

        # Инициализация Google Drive API
        self.service = self._init_drive_service(token_file)

        print(f"{'🔍 DRY RUN MODE' if dry_run else '🚀 IMPORT MODE'}")
        if priority:
            print(f"📊 Фильтр: Priority {priority} документы")
        print("=" * 70)

    def _init_drive_service(self, token_file):
        """Инициализация Google Drive API"""
        if not Path(token_file).exists():
            print(f"❌ Ошибка: Файл {token_file} не найден!")
            print("Запустите сначала: python3 get-gdrive-token-manual.py")
            sys.exit(1)

        with open(token_file, 'r') as f:
            token_data = json.load(f)

        creds = Credentials(
            token=token_data['token'],
            refresh_token=token_data['refresh_token'],
            token_uri=token_data['token_uri'],
            client_id=token_data['client_id'],
            client_secret=token_data['client_secret'],
            scopes=token_data['scopes']
        )

        # Создаем HTTP клиент с отключенной SSL верификацией
        # (необходимо для окружений с self-signed сертификатами)
        http = httplib2.Http(disable_ssl_certificate_validation=True)
        authorized_http = google_auth_httplib2.AuthorizedHttp(creds, http=http)

        return build('drive', 'v3', http=authorized_http)

    def get_folder_name(self, file_obj):
        """Получить имя родительской папки"""
        if 'parents' not in file_obj or not file_obj['parents']:
            return None

        parent_id = file_obj['parents'][0]
        try:
            parent = self.service.files().get(
                fileId=parent_id,
                fields='name'
            ).execute()
            return parent.get('name')
        except:
            return None

    def determine_priority(self, filename, folder_name=''):
        """Определить priority документа"""
        text = (filename + ' ' + folder_name).lower()

        for priority, keywords in PRIORITY_MAPPING.items():
            for keyword in keywords:
                if re.search(keyword, text, re.IGNORECASE):
                    return priority

        return 3  # По умолчанию Priority 3

    def map_file_to_path(self, file_obj) -> Optional[Dict]:
        """Определить путь для файла в структуре B.COFFEE"""
        filename = file_obj['name']
        folder_name = self.get_folder_name(file_obj)

        if not folder_name:
            return None

        # Ищем маппинг по имени папки
        mapping = None
        for key, value in FOLDER_MAPPING.items():
            if key in folder_name.upper():
                if isinstance(value, dict) and 'path' in value:
                    # Простой маппинг
                    mapping = value
                else:
                    # Сложный маппинг - определяем подкатегорию
                    for keyword, submap in KEYWORDS_MAPPING.items():
                        if keyword in filename.lower():
                            if submap in value:
                                mapping = value[submap]
                                break

                    # Если не нашли - используем первый доступный
                    if not mapping:
                        mapping = list(value.values())[0] if value else None

                break

        if not mapping:
            return None

        # Определяем имя файла
        safe_filename = self._sanitize_filename(filename)

        # Определяем priority
        priority = self.determine_priority(filename, folder_name)

        return {
            'path': mapping['path'],
            'filename': safe_filename,
            'family': mapping['family'],
            'category': mapping['category'],
            'tags': mapping['tags'],
            'priority': priority,
            'source_folder': folder_name
        }

    def _sanitize_filename(self, filename):
        """Очистить имя файла"""
        # Убираем расширение
        name = Path(filename).stem

        # Транслитерация кириллицы
        translit_map = {
            'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'yo',
            'ж': 'zh', 'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm',
            'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u',
            'ф': 'f', 'х': 'h', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'sch',
            'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya',
            ' ': '-', '_': '-'
        }

        name = name.lower()
        result = ''
        for char in name:
            result += translit_map.get(char, char if char.isalnum() or char == '-' else '-')

        # Убираем множественные дефисы
        result = re.sub(r'-+', '-', result).strip('-')

        return result + '.md'

    def download_and_convert(self, file_obj) -> Optional[str]:
        """Скачать и конвертировать файл в Markdown"""
        file_id = file_obj['id']
        mime_type = file_obj['mimeType']

        try:
            if mime_type == 'application/vnd.google-apps.document':
                # Google Docs → Markdown (через plain text)
                request = self.service.files().export_media(
                    fileId=file_id,
                    mimeType='text/plain'
                )
                content = self._download_content(request)
                return content.decode('utf-8')

            elif mime_type == 'application/vnd.google-apps.spreadsheet':
                # Google Sheets → CSV → Markdown table
                request = self.service.files().export_media(
                    fileId=file_id,
                    mimeType='text/csv'
                )
                content = self._download_content(request)
                return self._csv_to_markdown(content.decode('utf-8'))

            elif mime_type.startswith('image/'):
                # Изображения - просто ссылка
                return f"![{file_obj['name']}](https://drive.google.com/file/d/{file_id}/view)\n\n> Изображение из Google Drive"

            else:
                # Другие файлы - ссылка на скачивание
                return f"[📎 {file_obj['name']}](https://drive.google.com/file/d/{file_id}/view)\n\n> Файл из Google Drive"

        except Exception as e:
            print(f"    ⚠️  Ошибка при скачивании: {e}")
            return None

    def _download_content(self, request):
        """Скачать контент"""
        fh = io.BytesIO()
        downloader = MediaIoBaseDownload(fh, request)
        done = False
        while not done:
            status, done = downloader.next_chunk()
        return fh.getvalue()

    def _csv_to_markdown(self, csv_content):
        """Конвертировать CSV в Markdown таблицу"""
        lines = csv_content.strip().split('\n')
        if not lines:
            return csv_content

        # Первая строка - заголовок
        header = lines[0].split(',')
        separator = ['---'] * len(header)

        md = '| ' + ' | '.join(header) + ' |\n'
        md += '| ' + ' | '.join(separator) + ' |\n'

        for line in lines[1:]:
            cells = line.split(',')
            md += '| ' + ' | '.join(cells) + ' |\n'

        return md

    def generate_frontmatter(self, file_obj, mapping):
        """Генерация YAML frontmatter"""
        frontmatter = f"""---
title: {file_obj['name']}
family: {mapping['family']}
category: {mapping['category']}
type: Импортирован из Google Drive
status: IMPORTED
priority: {mapping['priority']}
source: Google Drive / {mapping['source_folder']}
import_date: {datetime.now().strftime('%Y-%m-%d')}
drive_id: {file_obj['id']}
modified: {file_obj.get('modifiedTime', 'unknown')}
tags:
{chr(10).join(f'  - {tag}' for tag in mapping['tags'])}
---

"""
        return frontmatter

    def import_file(self, file_obj):
        """Импортировать один файл"""
        self.stats['total_files'] += 1

        # Пропускаем папки
        if file_obj['mimeType'] == 'application/vnd.google-apps.folder':
            return

        # Определяем маппинг
        mapping = self.map_file_to_path(file_obj)
        if not mapping:
            print(f"  ⚠️  Пропущен (нет маппинга): {file_obj['name']}")
            self.stats['skipped'] += 1
            return

        # Фильтр по priority
        if self.priority_filter and mapping['priority'] != self.priority_filter:
            self.stats['skipped'] += 1
            return

        # Полный путь к файлу
        full_path = Path(mapping['path']) / mapping['filename']

        print(f"  📄 {file_obj['name']}")
        print(f"     → {full_path}")
        print(f"     Priority: {mapping['priority']} | Family: {mapping['family']}")

        if self.dry_run:
            self.stats['imported'] += 1
            return

        # Скачиваем и конвертируем
        content = self.download_and_convert(file_obj)
        if not content:
            print(f"     ❌ Ошибка конвертации")
            self.stats['errors'] += 1
            return

        # Создаем директорию
        full_path.parent.mkdir(parents=True, exist_ok=True)

        # Генерируем frontmatter
        frontmatter = self.generate_frontmatter(file_obj, mapping)

        # Сохраняем файл
        with open(full_path, 'w', encoding='utf-8') as f:
            f.write(frontmatter)
            f.write(content)

        print(f"     ✅ Импортирован")
        self.stats['imported'] += 1

    def import_all(self, folder_id='120x7kqYeV0Vb4TLbdCC0esv0WkF5JROC'):
        """Импортировать все файлы из папки"""
        print(f"\n🔍 Сканирование Google Drive папки...")
        print(f"📁 Folder ID: {folder_id}\n")

        # Получаем все файлы
        all_files = []
        page_token = None

        while True:
            try:
                results = self.service.files().list(
                    q=f"'{folder_id}' in parents and trashed=false",
                    pageSize=100,
                    fields="nextPageToken, files(id, name, mimeType, modifiedTime, parents)",
                    pageToken=page_token
                ).execute()

                files = results.get('files', [])
                all_files.extend(files)

                page_token = results.get('nextPageToken')
                if not page_token:
                    break
            except Exception as e:
                print(f"❌ Ошибка при получении списка файлов: {e}")
                return

        print(f"✅ Найдено файлов: {len(all_files)}\n")

        # Импортируем каждый файл
        for file_obj in all_files:
            try:
                self.import_file(file_obj)
            except Exception as e:
                print(f"  ❌ Ошибка при импорте {file_obj['name']}: {e}")
                self.stats['errors'] += 1

        # Статистика
        self.print_stats()

    def print_stats(self):
        """Вывести статистику"""
        print("\n" + "=" * 70)
        print("📊 СТАТИСТИКА ИМПОРТА")
        print("=" * 70)
        print(f"Всего файлов:        {self.stats['total_files']}")
        print(f"✅ Импортировано:    {self.stats['imported']}")
        print(f"⚠️  Пропущено:        {self.stats['skipped']}")
        print(f"❌ Ошибок:           {self.stats['errors']}")
        print("=" * 70)


def main():
    parser = argparse.ArgumentParser(description='Автоматический импорт из Google Drive')
    parser.add_argument('--dry-run', action='store_true',
                        help='Показать что будет импортировано, не создавая файлы')
    parser.add_argument('--priority', type=int, choices=[1, 2, 3],
                        help='Импортировать только Priority N документы')
    parser.add_argument('--folder-id', type=str,
                        default='120x7kqYeV0Vb4TLbdCC0esv0WkF5JROC',
                        help='ID папки Google Drive')

    args = parser.parse_args()

    print("🚀 Автоматический импортер VK-offee из Google Drive")
    print("=" * 70)

    # Создаем импортер
    importer = GoogleDriveImporter(
        dry_run=args.dry_run,
        priority=args.priority
    )

    # Запускаем импорт
    importer.import_all(args.folder_id)

    if not args.dry_run:
        print("\n✅ Импорт завершен!")
        print("\n📝 Следующие шаги:")
        print("1. Проверьте импортированные файлы")
        print("2. Создайте коммит: git add -A && git commit -m 'feat: auto-import from Google Drive'")
        print("3. Push: git push")


if __name__ == '__main__':
    main()
