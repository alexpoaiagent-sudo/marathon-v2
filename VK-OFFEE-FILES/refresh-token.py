#!/usr/bin/env python3
"""Скрипт для обновления access token используя refresh token"""

import json
import httplib2
import urllib3
urllib3.disable_warnings()

# Загружаем токен
with open('token.json', 'r') as f:
    token_data = json.load(f)

print("🔄 Обновление access token...")
print(f"📋 Refresh token: {token_data['refresh_token'][:20]}...")

# Подготавливаем данные для запроса refresh
http = httplib2.Http(disable_ssl_certificate_validation=True)
refresh_data = {
    'grant_type': 'refresh_token',
    'client_id': token_data['client_id'],
    'client_secret': token_data['client_secret'],
    'refresh_token': token_data['refresh_token']
}

# Формируем body для POST запроса
body = '&'.join([f'{k}={v}' for k, v in refresh_data.items()])

try:
    # Делаем POST запрос для обновления токена
    response, content = http.request(
        token_data['token_uri'],
        method='POST',
        headers={'Content-Type': 'application/x-www-form-urlencoded'},
        body=body
    )

    if response.status == 200:
        new_token_data = json.loads(content)

        # Обновляем token.json
        token_data['token'] = new_token_data['access_token']
        if 'refresh_token' in new_token_data:
            token_data['refresh_token'] = new_token_data['refresh_token']

        # Сохраняем обновленный токен
        with open('token.json', 'w') as f:
            json.dump(token_data, f, indent=2)

        print("✅ Токен успешно обновлен!")
        print(f"🔑 Новый access token: {new_token_data['access_token'][:30]}...")
        print(f"⏱️  Истекает через: {new_token_data.get('expires_in', 'N/A')} секунд")
    else:
        print(f"❌ Ошибка при обновлении токена:")
        print(f"   Status: {response.status}")
        print(f"   Content: {content.decode('utf-8')}")

except Exception as e:
    print(f"❌ Ошибка: {e}")
