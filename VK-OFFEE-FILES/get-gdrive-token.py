#!/usr/bin/env python3
"""
Автоматическое получение Google Drive refresh token для Claude Code
Используйте credentials.json из Google Cloud Console

Установка:
    pip install google-auth-oauthlib google-auth-httplib2 google-api-python-client

Использование:
    python3 get-gdrive-token.py
"""

import json
import os
import sys
from pathlib import Path

try:
    from google_auth_oauthlib.flow import InstalledAppFlow
    from google.auth.transport.requests import Request
    from google.oauth2.credentials import Credentials
except ImportError:
    print("❌ Ошибка: Не установлены необходимые библиотеки!")
    print("\nУстановите их командой:")
    print("pip install google-auth-oauthlib google-auth-httplib2 google-api-python-client")
    sys.exit(1)

# Scopes для полного доступа к Google Drive
SCOPES = [
    'https://www.googleapis.com/auth/drive',
    'https://www.googleapis.com/auth/drive.file',
    'https://www.googleapis.com/auth/documents'
]

def main():
    print("🔐 Получение Google Drive Refresh Token")
    print("=" * 50)

    # Проверяем наличие credentials.json
    credentials_file = Path('credentials.json')
    if not credentials_file.exists():
        print("❌ Ошибка: Файл credentials.json не найден!")
        print("\nШаги:")
        print("1. Перейдите в Google Cloud Console")
        print("2. APIs & Services → Credentials")
        print("3. Скачайте JSON файл OAuth credentials")
        print("4. Сохраните его как 'credentials.json' в эту папку")
        sys.exit(1)

    print("✅ Найден файл credentials.json")

    # Читаем credentials
    try:
        with open('credentials.json', 'r') as f:
            creds_data = json.load(f)

        # Проверяем тип credentials
        if 'installed' in creds_data:
            client_type = 'installed'
            client_id = creds_data['installed']['client_id']
            client_secret = creds_data['installed']['client_secret']
        elif 'web' in creds_data:
            client_type = 'web'
            client_id = creds_data['web']['client_id']
            client_secret = creds_data['web']['client_secret']
        else:
            print("❌ Неизвестный формат credentials.json")
            sys.exit(1)

        print(f"✅ Тип клиента: {client_type}")
        print(f"✅ Client ID: {client_id[:30]}...")

    except Exception as e:
        print(f"❌ Ошибка чтения credentials.json: {e}")
        sys.exit(1)

    print("\n🌐 Запускаем OAuth flow...")
    print("📌 Сейчас откроется браузер - нажмите 'Разрешить' (Allow)")
    print()

    try:
        # Запускаем OAuth flow
        flow = InstalledAppFlow.from_client_secrets_file(
            'credentials.json',
            SCOPES
        )

        # Запускает локальный сервер и открывает браузер
        creds = flow.run_local_server(port=0)

        print("\n✅ Авторизация успешна!")

        # Сохраняем токены
        token_data = {
            'refresh_token': creds.refresh_token,
            'token': creds.token,
            'client_id': creds.client_id,
            'client_secret': creds.client_secret,
            'token_uri': creds.token_uri,
            'scopes': creds.scopes
        }

        # Сохраняем в token.json
        with open('token.json', 'w') as token_file:
            json.dump(token_data, token_file, indent=2)

        print("✅ Токены сохранены в token.json")

        # Сохраняем в .env
        env_content = f"""# Google Drive API Credentials
GOOGLE_CLIENT_ID={client_id}
GOOGLE_CLIENT_SECRET={client_secret}
GOOGLE_REFRESH_TOKEN={creds.refresh_token}
GOOGLE_FOLDER_ID=120x7kqYeV0Vb4TLbdCC0esv0WkF5JROC
"""

        with open('.env', 'w') as env_file:
            env_file.write(env_content)

        print("✅ Переменные окружения сохранены в .env")

        # Выводим важную информацию
        print("\n" + "=" * 50)
        print("🎉 ГОТОВО! Используйте эти данные:")
        print("=" * 50)
        print(f"\nGOOGLE_CLIENT_ID={client_id}")
        print(f"GOOGLE_CLIENT_SECRET={client_secret}")
        print(f"GOOGLE_REFRESH_TOKEN={creds.refresh_token}")
        print(f"GOOGLE_FOLDER_ID=120x7kqYeV0Vb4TLbdCC0esv0WkF5JROC")

        print("\n📝 Следующие шаги:")
        print("1. Скопируйте .mcp.json.example → .mcp.json")
        print("2. Замените значения на реальные из .env файла")
        print("3. Перезапустите Claude Code")
        print("4. Готово! Claude Code сможет читать Google Drive")

        print("\n⚠️  ВАЖНО: Не коммитьте файлы:")
        print("   - credentials.json")
        print("   - token.json")
        print("   - .env")
        print("   - .mcp.json")
        print("\n(Они уже в .gitignore)")

    except Exception as e:
        print(f"\n❌ Ошибка при авторизации: {e}")
        print("\nВозможные причины:")
        print("1. Не добавлен test user в OAuth consent screen")
        print("2. Не включен Google Drive API")
        print("3. Проблемы с сетью")
        sys.exit(1)

if __name__ == '__main__':
    main()
