# Настройка Google Drive API для интеграции с Claude Code

> **Цель:** Настроить прямой доступ Claude Code к Google Drive для чтения и редактирования документов

---

## Преимущества интеграции

С Google Drive API Claude Code сможет:
- ✅ **Читать документы** напрямую из Google Drive
- ✅ **Редактировать документы** на Drive (синхронизация)
- ✅ **Автоматически импортировать** новые файлы
- ✅ **Конвертировать** Google Docs → Markdown автоматически
- ✅ **Отслеживать изменения** (версионирование)
- ✅ **Двусторонняя синхронизация**: GitHub ↔ Google Drive

---

## Шаг 1: Создание проекта в Google Cloud Console

### 1.1 Перейдите в Google Cloud Console

Откройте: https://console.cloud.google.com/

### 1.2 Создайте новый проект

1. Нажмите на выпадающий список проектов (вверху слева)
2. Нажмите **"Создать проект"** (New Project)
3. Введите название: `VK-Coffee-Integration`
4. Нажмите **"Создать"** (Create)

### 1.3 Выберите проект

После создания убедитесь, что выбран новый проект `VK-Coffee-Integration`.

---

## Шаг 2: Включение Google Drive API

### 2.1 Перейдите в API & Services

1. В боковом меню → **APIs & Services** → **Enabled APIs & services**
2. Или перейдите: https://console.cloud.google.com/apis/dashboard

### 2.2 Включите Google Drive API

1. Нажмите **"+ ENABLE APIS AND SERVICES"**
2. Найдите **"Google Drive API"**
3. Нажмите на неё
4. Нажмите **"ENABLE"**

### 2.3 (Опционально) Включите Google Docs API

Если нужно редактировать Google Docs напрямую:
1. Повторите процесс для **"Google Docs API"**
2. Нажмите **"ENABLE"**

---

## Шаг 3: Создание OAuth 2.0 Credentials

### 3.1 Перейдите в Credentials

1. **APIs & Services** → **Credentials**
2. Или: https://console.cloud.google.com/apis/credentials

### 3.2 Настройте OAuth consent screen

**ВАЖНО:** Сначала нужно настроить consent screen!

1. Нажмите **"OAuth consent screen"** (в левом меню)
2. Выберите **"External"** (для тестирования)
3. Нажмите **"CREATE"**

**Заполните форму:**
- **App name:** `VK-Coffee Claude Integration`
- **User support email:** ваш email
- **Developer contact email:** ваш email
- Нажмите **"SAVE AND CONTINUE"**

**Scopes:**
1. Нажмите **"ADD OR REMOVE SCOPES"**
2. Найдите и выберите:
   - `https://www.googleapis.com/auth/drive` (полный доступ)
   - `https://www.googleapis.com/auth/drive.file` (доступ к созданным файлам)
   - `https://www.googleapis.com/auth/documents` (если нужен Google Docs)
3. Нажмите **"UPDATE"**
4. Нажмите **"SAVE AND CONTINUE"**

**Test users:**
1. Нажмите **"ADD USERS"**
2. Добавьте свой email (тот, под которым авторизованы в Google Drive)
3. Нажмите **"SAVE AND CONTINUE"**

4. Нажмите **"BACK TO DASHBOARD"**

### 3.3 Создайте OAuth 2.0 Client ID

1. Вернитесь в **Credentials**
2. Нажмите **"+ CREATE CREDENTIALS"**
3. Выберите **"OAuth client ID"**

**Настройте:**
- **Application type:** `Desktop app` (для CLI)
- **Name:** `Claude Code Desktop`
- Нажмите **"CREATE"**

### 3.4 Скачайте credentials

1. После создания появится окно с Client ID и Client Secret
2. Нажмите **"DOWNLOAD JSON"**
3. Сохраните файл как `credentials.json`

**НЕ ДЕЛИТЕСЬ ЭТИМ ФАЙЛОМ!** Он содержит секретные данные.

---

## Шаг 4: Получение Refresh Token

Теперь нужно получить refresh token для длительного доступа.

### Вариант A: Использовать OAuth2 Playground

1. Перейдите: https://developers.google.com/oauthplayground/
2. Нажмите на **⚙️ (шестерёнка)** справа вверху
3. Отметьте **"Use your own OAuth credentials"**
4. Введите:
   - **OAuth Client ID:** (из скачанного JSON)
   - **OAuth Client secret:** (из скачанного JSON)
5. Закройте настройки

**Select & authorize APIs:**
1. В левой панели найдите **"Drive API v3"**
2. Выберите:
   - `https://www.googleapis.com/auth/drive`
   - `https://www.googleapis.com/auth/drive.file`
3. Нажмите **"Authorize APIs"**
4. Войдите под своим Google аккаунтом
5. Разрешите доступ

**Exchange authorization code for tokens:**
1. После авторизации нажмите **"Exchange authorization code for tokens"**
2. Скопируйте **Refresh token** (сохраните его!)

### Вариант B: Использовать Python скрипт

Если предпочитаете программный подход:

```python
from google_auth_oauthlib.flow import InstalledAppFlow
import json

SCOPES = [
    'https://www.googleapis.com/auth/drive',
    'https://www.googleapis.com/auth/documents'
]

flow = InstalledAppFlow.from_client_secrets_file(
    'credentials.json', SCOPES)
creds = flow.run_local_server(port=0)

print("Refresh Token:", creds.refresh_token)
print("Access Token:", creds.token)

# Сохраните refresh token в безопасное место!
with open('token.json', 'w') as token:
    token.write(json.dumps({
        'refresh_token': creds.refresh_token,
        'token': creds.token,
        'client_id': creds.client_id,
        'client_secret': creds.client_secret
    }))
```

Запустите:
```bash
pip install google-auth-oauthlib
python get_token.py
```

---

## Шаг 5: Настройка MCP Server (для Claude Code)

### 5.1 Установка Google Drive MCP Server

```bash
# Установить через npm (если доступен)
npm install -g @modelcontextprotocol/server-gdrive

# Или использовать официальный MCP сервер
# https://github.com/modelcontextprotocol/servers
```

### 5.2 Обновление .mcp.json

Добавьте конфигурацию Google Drive в `.mcp.json`:

```json
{
  "mcpServers": {
    "quint-code": {
      "command": "/usr/local/bin/quint-code",
      "args": ["serve"],
      "cwd": "/home/user/VK-offee",
      "env": {
        "QUINT_PROJECT_ROOT": "/home/user/VK-offee"
      }
    },
    "gdrive": {
      "command": "mcp-server-gdrive",
      "args": [],
      "env": {
        "GOOGLE_CLIENT_ID": "ваш-client-id-из-credentials.json",
        "GOOGLE_CLIENT_SECRET": "ваш-client-secret-из-credentials.json",
        "GOOGLE_REFRESH_TOKEN": "ваш-refresh-token-из-шага-4",
        "GOOGLE_FOLDER_ID": "120x7kqYeV0Vb4TLbdCC0esv0WkF5JROC"
      }
    }
  }
}
```

**Где найти значения:**
- `GOOGLE_CLIENT_ID`: в файле `credentials.json` → `"client_id"`
- `GOOGLE_CLIENT_SECRET`: в файле `credentials.json` → `"client_secret"`
- `GOOGLE_REFRESH_TOKEN`: из Шага 4
- `GOOGLE_FOLDER_ID`: из URL папки Drive (последняя часть)

### 5.3 Безопасное хранение токенов

**ВАЖНО:** Не коммитьте `.mcp.json` с токенами в Git!

Добавьте в `.gitignore`:
```bash
echo ".mcp.json" >> .gitignore
echo "credentials.json" >> .gitignore
echo "token.json" >> .gitignore
```

**Лучше использовать переменные окружения:**

1. Создайте файл `.env` (НЕ коммитьте в Git!):
```bash
GOOGLE_CLIENT_ID=ваш-client-id
GOOGLE_CLIENT_SECRET=ваш-secret
GOOGLE_REFRESH_TOKEN=ваш-refresh-token
```

2. Обновите `.mcp.json`:
```json
{
  "mcpServers": {
    "gdrive": {
      "command": "mcp-server-gdrive",
      "args": [],
      "env": {
        "GOOGLE_CLIENT_ID": "${GOOGLE_CLIENT_ID}",
        "GOOGLE_CLIENT_SECRET": "${GOOGLE_CLIENT_SECRET}",
        "GOOGLE_REFRESH_TOKEN": "${GOOGLE_REFRESH_TOKEN}",
        "GOOGLE_FOLDER_ID": "120x7kqYeV0Vb4TLbdCC0esv0WkF5JROC"
      }
    }
  }
}
```

---

## Шаг 6: Проверка подключения

После настройки, перезапустите Claude Code и проверьте:

```bash
# Я смогу использовать команды типа:
# - gdrive.list_files (список файлов)
# - gdrive.read_file (чтение файла)
# - gdrive.write_file (запись файла)
# - gdrive.create_file (создание файла)
```

Попросите меня:
```
"Claude, прочитай список файлов из Google Drive папки VK-Coffee"
```

Если MCP настроен правильно, я смогу получить доступ!

---

## Шаг 7: Автоматизация импорта

После настройки API, я смогу:

### Автоматический импорт всех документов

```
"Claude, импортируй все документы из Google Drive в B.COFFEE,
распредели их по структуре SRT 3×3, добавь frontmatter"
```

**Что я сделаю:**
1. ✅ Получу список всех файлов из папки
2. ✅ Определю тип каждого файла (Docs, Sheets, PDF)
3. ✅ Конвертирую Google Docs → Markdown
4. ✅ Распределю по семействам F0-F9
5. ✅ Добавлю YAML frontmatter
6. ✅ Создам README.md в каждой папке
7. ✅ Закоммичу изменения

### Двусторонняя синхронизация

```
"Claude, синхронизируй изменения из GitHub обратно в Google Drive"
```

**Workflow:**
```
1. Редактируешь документ на GitHub
2. Коммитишь изменения
3. Claude автоматически обновляет Google Drive
```

Или наоборот:
```
1. Редактируешь документ в Google Drive
2. Claude детектит изменения
3. Автоматически создаёт коммит в GitHub
```

---

## Альтернатива: Упрощённый доступ (read-only)

Если полный OAuth сложен, можно использовать **Service Account** для read-only доступа:

### Создание Service Account

1. В Google Cloud Console → **IAM & Admin** → **Service Accounts**
2. Нажмите **"+ CREATE SERVICE ACCOUNT"**
3. Введите имя: `vk-coffee-reader`
4. Нажмите **"CREATE AND CONTINUE"**
5. Роль: **"Viewer"**
6. Нажмите **"DONE"**

### Получение JSON ключа

1. Найдите созданный Service Account
2. Нажмите на него → **Keys** → **Add Key** → **Create new key**
3. Тип: **JSON**
4. Скачайте файл

### Предоставление доступа к папке

1. Откройте папку в Google Drive
2. Нажмите **"Открыть доступ"**
3. Добавьте email Service Account (например: `vk-coffee-reader@...`)
4. Права: **"Читатель"**

**Плюсы:** Проще настроить, не нужен OAuth
**Минусы:** Только чтение, нет редактирования

---

## Troubleshooting

### Ошибка 403: Access Denied

**Причина:** Недостаточно прав или не добавлен test user
**Решение:**
1. Проверьте OAuth consent screen → Test users
2. Убедитесь, что добавили свой email
3. Проверьте scopes (должны быть drive и documents)

### Ошибка 401: Invalid Credentials

**Причина:** Неверный refresh token или истёк access token
**Решение:**
1. Получите новый refresh token (Шаг 4)
2. Обновите `.mcp.json`

### MCP Server не запускается

**Причина:** Не установлен или неправильный путь
**Решение:**
```bash
# Проверьте, установлен ли mcp-server-gdrive
which mcp-server-gdrive

# Установите заново
npm install -g @modelcontextprotocol/server-gdrive
```

---

## Что дальше?

После настройки API:

1. ✅ Сообщите мне, что API настроен
2. ✅ Я проверю подключение
3. ✅ Запущу автоматический импорт всех документов
4. ✅ Распределю по структуре B.COFFEE
5. ✅ Создам коммит с импортированными файлами

**Готовы начать настройку?** Следуйте инструкциям выше и дайте знать, когда будете готовы! 🚀

---

**Версия:** 1.0
**Дата:** 2026-01-20
**Автор:** Claude Code + alexpoaiagent-sudo
**Ссылки:**
- Google Cloud Console: https://console.cloud.google.com/
- OAuth2 Playground: https://developers.google.com/oauthplayground/
- MCP Servers: https://github.com/modelcontextprotocol/servers
