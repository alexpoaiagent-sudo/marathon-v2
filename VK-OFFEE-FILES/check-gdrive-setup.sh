#!/bin/bash
# Проверка готовности к настройке Google Drive API

echo "🔍 Проверка готовности Google Drive API"
echo "========================================"
echo

# Проверка 1: credentials.json
echo -n "1. credentials.json... "
if [ -f "credentials.json" ]; then
    echo "✅ Найден"
else
    echo "❌ Не найден!"
    echo "   Скачайте credentials.json из Google Cloud Console"
    echo "   и сохраните в $(pwd)/"
    MISSING=true
fi

# Проверка 2: Python
echo -n "2. Python 3... "
if command -v python3 &> /dev/null; then
    PYTHON_VERSION=$(python3 --version)
    echo "✅ $PYTHON_VERSION"
else
    echo "❌ Не установлен!"
    MISSING=true
fi

# Проверка 3: pip
echo -n "3. pip... "
if command -v pip &> /dev/null || command -v pip3 &> /dev/null; then
    echo "✅ Установлен"
else
    echo "❌ Не установлен!"
    MISSING=true
fi

# Проверка 4: Google библиотеки
echo -n "4. google-auth-oauthlib... "
if python3 -c "import google_auth_oauthlib" 2>/dev/null; then
    echo "✅ Установлена"
else
    echo "❌ Не установлена"
    echo "   Выполните: pip install google-auth-oauthlib google-auth-httplib2 google-api-python-client"
    NEEDS_INSTALL=true
fi

# Проверка 5: Скрипт get-gdrive-token.py
echo -n "5. get-gdrive-token.py... "
if [ -f "get-gdrive-token.py" ]; then
    echo "✅ Найден"
else
    echo "❌ Не найден!"
    MISSING=true
fi

# Проверка 6: .gitignore
echo -n "6. .gitignore (защита credentials)... "
if grep -q "credentials.json" .gitignore 2>/dev/null; then
    echo "✅ Настроен"
else
    echo "⚠️  Нужно добавить"
    echo "   credentials.json, token.json, .env и .mcp.json"
fi

echo
echo "========================================"

if [ "$MISSING" = true ]; then
    echo "❌ Есть проблемы! Исправьте ошибки выше"
    echo
    echo "📖 Инструкция:"
    echo "   cat GDRIVE-SETUP-QUICK.md"
    exit 1
fi

if [ "$NEEDS_INSTALL" = true ]; then
    echo "⚠️  Нужно установить библиотеки"
    echo
    echo "Выполните:"
    echo "  pip install google-auth-oauthlib google-auth-httplib2 google-api-python-client"
    echo
    echo "Затем запустите:"
    echo "  python3 get-gdrive-token.py"
    exit 1
fi

echo "✅ Всё готово! Запустите:"
echo
echo "  python3 get-gdrive-token.py"
echo
echo "📖 Полная инструкция: GDRIVE-SETUP-QUICK.md"
