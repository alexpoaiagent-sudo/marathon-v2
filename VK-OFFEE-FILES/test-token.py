#!/usr/bin/env python3
"""Тестовый скрипт для проверки токена Google Drive"""

import json
import httplib2
import google_auth_httplib2
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

# Загружаем токен
with open('token.json', 'r') as f:
    token_data = json.load(f)

# Создаем credentials
creds = Credentials(
    token=token_data.get('token'),
    refresh_token=token_data['refresh_token'],
    token_uri=token_data['token_uri'],
    client_id=token_data['client_id'],
    client_secret=token_data['client_secret'],
    scopes=token_data['scopes']
)

print("🔑 Токен загружен")
print(f"📋 Scopes: {creds.scopes}")
print(f"🔄 Refresh token: {creds.refresh_token[:20]}...")

# Создаем HTTP с отключенным SSL
http = httplib2.Http(disable_ssl_certificate_validation=True)
authorized_http = google_auth_httplib2.AuthorizedHttp(creds, http=http)

# Пробуем создать service
print("\n🔧 Создание Google Drive service...")
service = build('drive', 'v3', http=authorized_http)

# Пробуем получить информацию о пользователе
print("🧪 Тест 1: Получение информации о пользователе...")
try:
    about = service.about().get(fields='user').execute()
    user = about.get('user', {})
    print(f"✅ Успех! Пользователь: {user.get('emailAddress', 'N/A')}")
except Exception as e:
    print(f"❌ Ошибка: {e}")

# Пробуем получить список файлов из корня
print("\n🧪 Тест 2: Получение списка файлов из My Drive...")
try:
    results = service.files().list(
        pageSize=10,
        fields="files(id, name, mimeType)"
    ).execute()
    files = results.get('files', [])
    print(f"✅ Успех! Найдено файлов: {len(files)}")
    for f in files[:5]:
        print(f"  📄 {f['name']} ({f['mimeType']})")
except Exception as e:
    print(f"❌ Ошибка: {e}")

# Пробуем получить файлы из конкретной папки
print("\n🧪 Тест 3: Получение файлов из папки VK Coffee...")
folder_id = '120x7kqYeV0Vb4TLbdCC0esv0WkF5JROC'
try:
    results = service.files().list(
        q=f"'{folder_id}' in parents and trashed=false",
        pageSize=10,
        fields="files(id, name, mimeType)"
    ).execute()
    files = results.get('files', [])
    print(f"✅ Успех! Найдено файлов в папке: {len(files)}")
    for f in files[:5]:
        print(f"  📄 {f['name']} ({f['mimeType']})")
except Exception as e:
    print(f"❌ Ошибка: {e}")

print("\n✅ Тестирование завершено!")
