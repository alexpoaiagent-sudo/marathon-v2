# Карта импорта из Google Drive в multi-kernel архитектуру

> **Источник:** https://drive.google.com/drive/folders/120x7kqYeV0Vb4TLbdCC0esv0WkF5JROC
> **Дата составления:** 2026-01-20
> **Архитектура:** C.FPF → A.SRT → B.COFFEE

---

## Принципы распределения

### Иерархия ядер

```
C.FPF (философия)
  └─→ Ничего не импортируется (источник правды для FPF)

A.SRT (методология)
  └─→ Шаблоны и процессы (если есть общие, применимые к любому проекту)

B.COFFEE (данные кофейни)
  └─→ ВСЕ операционные документы кофейни
```

### SRT 3×3 структура в B.COFFEE

```
F0: Management          — Управление хранилищем
F1-F3: Suprasystem      — Рынок HoReCa, окружение
F4-F6: System (Coffee)  — Целевая система (сеть кофеен)
F7-F9: Constructor      — Команда управления
```

---

## Mapping: Google Drive → B.COFFEE

### Папка: ПЕРСОНАЛ → F9 (3.3.Operations/roles)

**Семейство:** F9 — Команда (Roles & Operations)
**Путь:** `B.COFFEE/content/3.ManagementTeam/3.3.Operations/roles/job-descriptions/`

| Документ в Drive | Тип | Целевой файл | Статус |
|------------------|-----|--------------|--------|
| Должностная инструкция Бариста | Google Docs | `waiter-job-description.md` | ✅ Есть |
| Должностная инструкция Раннера | Google Docs | `runner-job-description.md` | ✅ Есть |
| Вопросы для собеседования официанта | Google Docs | `questions-waiter-job-description.md` | ✅ Есть |
| Адаптационный план стажёра | Google Sheets | `waiter-trainee-adaptation-plan.md` | ✅ Есть |
| Список чатов кафе | Google Sheets | `cafe-chat-list.md` | ✅ Есть |
| Инструкция по кассе | Google Docs | `cash-register-guidelines.md` | ✅ Есть |
| **Вакансии (Бариста, Помощник, Раннер)** | Google Docs | `vacancies.md` | ⚠️ Обновить |

**Что нужно добавить:**
- Вакансии (обновлённая версия)
- Контракты с сотрудниками (если есть)
- Графики работы (если есть)

---

### Папка: КУХНЯ → F5 + F6 (2.2.Architecture + 2.3.Operations)

#### Подраздел: Рецепты и меню → F5 (2.2.Architecture)

**Семейство:** F5 — Архитектура продукта
**Путь:** `B.COFFEE/content/2.VkusnyCoffeeNetwork/2.2.Architecture/`

| Документ в Drive | Тип | Целевой файл | Статус |
|------------------|-----|--------------|--------|
| Меню Холодных напитков (Самокиша) | Image | `menus/menu-cold-drinks-samokisha.md` | ✅ Есть |
| Меню Холодных напитков (Тургенева) | Image | `menus/menu-cold-drinks-turgeneva.md` | ✅ Есть |
| Меню Еда | Image | `menus/menu-food.md` | ✅ Есть |
| Меню Смузи | Image | `menus/menu-smoothies.md` | ✅ Есть |
| **Технологические карты** | Google Docs | `recipes/tech-cards.md` | ❌ НЕТ |
| Состав продуктов | Google Sheets | `product-compositions.md` | ✅ Есть |
| Сроки годности продуктов | Google Sheets | `product-shelf-life.md` | ✅ Есть |

#### Подраздел: Операции на кухне → F6 (2.3.Operations)

**Семейство:** F6 — Реализация процессов
**Путь:** `B.COFFEE/content/2.VkusnyCoffeeNetwork/2.3.Operations/`

| Документ в Drive | Тип | Целевой файл | Статус |
|------------------|-----|--------------|--------|
| **Должностная инструкция Повара** | Google Docs | `roles/job-descriptions/cook-job-description.md` | ⚠️ Обновить |
| Чек-лист открытия (Луговая) | Google Sheets | `checklists/location-checklist-lugovaya.md` | ✅ Есть |
| Чек-лист открытия (Самокиша) | Google Sheets | `checklists/location-checklist-samokisha.md` | ✅ Есть |
| Чек-лист открытия (Тургенева) | Google Sheets | `checklists/location-checklist-turgeneva.md` | ✅ Есть |
| Чек-лист раннера (все локации) | Google Sheets | `checklists/runner-checklist-*.md` | ✅ Есть |
| **Протоколы планерок** | Google Docs | `meetings/meeting-protocols.md` | ❌ НЕТ |

**Что нужно добавить:**
- Технологические карты (если удастся загрузить)
- Протоколы планерок (если удастся загрузить)
- Инструкции по оборудованию

---

### Папка: БАР → F5 + F6 (2.2.Architecture + 2.3.Operations)

**Статус:** ⚠️ Папка была пропущена в предыдущем экспорте

**Семейство:** F5-F6 — Архитектура и операции бара
**Путь:** `B.COFFEE/content/2.VkusnyCoffeeNetwork/`

| Документ в Drive | Тип | Целевой файл | Статус |
|------------------|-----|--------------|--------|
| Рецепты напитков | Google Docs | `2.2.Architecture/bar/drink-recipes.md` | ❌ НЕТ |
| Инструкция по кофемашине | Google Docs | `2.3.Operations/bar/coffee-machine-guide.md` | ❌ НЕТ |
| Стандарты подачи | Google Docs | `2.3.Operations/bar/serving-standards.md` | ❌ НЕТ |

**Что нужно добавить:**
- Полное содержимое папки БАР

---

### Папка: ФИНАНСЫ → F7 (3.1.Meaning/finance)

**Семейство:** F7 — Принципы бизнеса (бизнес-модель, финансы)
**Путь:** `B.COFFEE/content/3.ManagementTeam/3.1.Meaning/finance/`

| Документ в Drive | Тип | Целевой файл | Статус |
|------------------|-----|--------------|--------|
| Калькуляция напитков | Google Sheets | `drink-calculations.md` | ✅ Есть |
| Себестоимость напитков | Google Sheets | `drink-costing.md` | ✅ Есть |
| **Бизнес-модель** | Google Docs | `business-model.md` | ⚠️ Обновить |
| **P&L отчёт** | Google Sheets | `pnl-report.md` | ❌ НЕТ |
| **Бюджет** | Google Sheets | `budget.md` | ❌ НЕТ |

**Что нужно добавить:**
- P&L отчёт (если есть)
- Бюджет (если есть)
- Финансовые прогнозы

---

### Папка: ПОСТАВЩИКИ → F8 (3.2.Architecture/vendors)

**Семейство:** F8 — Инструменты и поставщики
**Путь:** `B.COFFEE/content/3.ManagementTeam/3.2.Architecture/vendors/suppliers/`

| Документ в Drive | Тип | Целевой файл | Статус |
|------------------|-----|--------------|--------|
| Прайс-лист «Горячие слоечки» | Excel | `goryachie-sloechki-price-*.md` | ✅ Есть |
| Прайс-лист «Мельница» | PDF | `melnitsa-price-*.md` | ✅ Есть |
| Прайс-лист «Северные слойки» | PDF | `sev-sloyki-price-*.md` | ✅ Есть |
| Каталог «Мельница» | PDF | `melnitsa-catalog.md` | ✅ Есть |
| Информация о поставщиках | Google Sheets | `suppliers-info.md` | ✅ Есть |
| Список поставщиков для печати | Google Sheets | `supplier-print-list.md` | ✅ Есть |
| **Контракты с поставщиками** | PDF | `contracts/*.md` | ❌ НЕТ |

**Что нужно добавить:**
- Контракты с поставщиками (если есть)
- Обновлённые прайс-листы (если изменились)

---

### Папка: ДОКУМЕНТЫ → F0 (0.Management)

**Семейство:** F0 — Управление (метаинформация)
**Путь:** `B.COFFEE/content/0.Management/`

| Документ в Drive | Тип | Целевой файл | Статус |
|------------------|-----|--------------|--------|
| Карточка ИП (реквизиты) | Google Docs | `company-details.md` | ✅ Есть |
| **ОГРН, ИНН** | Google Docs | `company-details.md` | ✅ Включено |
| **Лицензии и разрешения** | PDF | `licenses/licenses.md` | ❌ НЕТ |
| **Договора аренды** | PDF | `contracts/rent-agreements.md` | ❌ НЕТ |

**Что нужно добавить:**
- Лицензии (если есть)
- Договора аренды точек

---

### Папка: ОБУЧЕНИЕ → F9 (3.3.Operations/training)

**Семейство:** F9 — Команда (обучение и развитие)
**Путь:** `B.COFFEE/content/3.ManagementTeam/3.3.Operations/training/`

| Документ в Drive | Тип | Целевой файл | Статус |
|------------------|-----|--------------|--------|
| Описание системы Бариста | Google Docs | `barista-system-description.md` | ✅ Есть |
| **Программа обучения бариста** | Google Docs | `barista-training-program.md` | ❌ НЕТ |
| **Экзамен для бариста** | Google Forms | `barista-exam.md` | ❌ НЕТ |
| **Видео-инструкции** | Google Drive Videos | `videos/README.md` + links | ❌ НЕТ |

**Что нужно добавить:**
- Полная программа обучения
- Материалы для экзамена
- Ссылки на видео (если есть)

---

### Папка: ОПЕРАЦИОННЫЙ МЕНЕДЖЕР → F6 (2.3.Operations)

**Семейство:** F6 — Реализация процессов (управление операциями)
**Путь:** `B.COFFEE/content/2.VkusnyCoffeeNetwork/2.3.Operations/`

| Документ в Drive | Тип | Целевой файл | Статус |
|------------------|-----|--------------|--------|
| Дорожная карта ОМ | Google Docs | `operations-manager-roadmap.md` | ✅ Есть |
| **Должностная инструкция ОМ** | Google Docs | `roles/operations-manager-job-description.md` | ❌ НЕТ |
| **KPI менеджера** | Google Sheets | `management/manager-kpi.md` | ❌ НЕТ |

**Что нужно добавить:**
- Должностная инструкция операционного менеджера
- KPI и метрики

---

### Папка: МАРКЕТИНГ → F1-F3 (1.HoReCaMarket)

**Семейство:** F1-F3 — Надсистема (рынок, маркетинг, взаимодействие с клиентами)
**Путь:** `B.COFFEE/content/1.HoReCaMarket/`

| Документ в Drive | Тип | Целевой файл | Статус |
|------------------|-----|--------------|--------|
| **Маркетинговая стратегия** | Google Docs | `1.1.Meaning/marketing-strategy.md` | ❌ НЕТ |
| **Презентация для франшизы** | Google Slides | `1.3.Operations/franchise/presentation.md` | ✅ Есть |
| **Анализ конкурентов** | Google Sheets | `1.2.Architecture/competitors-analysis.md` | ❌ НЕТ |
| **Программа лояльности** | Google Docs | `1.3.Operations/loyalty-program.md` | ❌ НЕТ |

**Что нужно добавить:**
- Маркетинговая стратегия
- Анализ конкурентов
- Программа лояльности

---

### Папка: ДИЗАЙН И БРЕНД → F5 (2.2.Architecture)

**Семейство:** F5 — Архитектура продукта (брендинг, дизайн)
**Путь:** `B.COFFEE/content/2.VkusnyCoffeeNetwork/2.2.Architecture/branding/`

| Документ в Drive | Тип | Целевой файл | Статус |
|------------------|-----|--------------|--------|
| **Брендбук** | PDF | `brand-book.md` | ❌ НЕТ |
| **Логотипы** | Images | `assets/branding/logos/` | ❌ НЕТ |
| **Фирменный стиль** | PDF | `brand-style-guide.md` | ❌ НЕТ |
| Фото тары | Images | `assets/job-aids/packaging-photos/` | ❌ НЕТ |
| Ценники-наклейки | Images | `assets/branding/price-tags/` | ❌ НЕТ |

**Что нужно добавить:**
- Все визуальные материалы
- Брендбук
- Фото тары и этикеток

---

## Статистика импорта

### Текущее состояние (на 20.01.2026)

| Категория | Всего документов | Импортировано | Осталось |
|-----------|------------------|---------------|----------|
| Должностные инструкции | ~10 | 6 | 4 |
| Регламенты и процессы | ~20 | 12 | 8 |
| Меню и рецепты | ~8 | 4 | 4 |
| Финансовые документы | ~5 | 2 | 3 |
| Поставщики | ~10 | 8 | 2 |
| Обучение | ~5 | 1 | 4 |
| Маркетинг | ~5 | 1 | 4 |
| Дизайн и бренд | ~10 | 0 | 10 |
| **ИТОГО** | **~73** | **34** | **39** |

**Процент завершённости:** 47%

---

## Приоритеты импорта

### Критически важно (Priority 1)

1. **Папка БАР** — полностью пропущена
2. **Технологические карты** — ключевые рецепты
3. **Протоколы планерок** — история решений
4. **Должностные инструкции** — недостающие роли
5. **Финансовые отчёты** — P&L, бюджет

### Важно (Priority 2)

6. **Программа обучения бариста** — стандартизация
7. **Брендбук и логотипы** — визуальная идентичность
8. **Маркетинговая стратегия** — позиционирование
9. **Контракты** — юридические документы
10. **KPI и метрики** — управление эффективностью

### Желательно (Priority 3)

11. **Видео-инструкции** — ссылки на обучающие материалы
12. **Фото тары и этикеток** — визуальные референсы
13. **Анализ конкурентов** — исследование рынка
14. **Программа лояльности** — маркетинговые инструменты

---

## Процесс импорта

### Вариант 1: Через Google Drive API (рекомендуется)

1. **Настройка доступа:**
   ```bash
   # Установить Google Drive MCP Server
   npm install -g @modelcontextprotocol/server-gdrive

   # Добавить в .mcp.json
   {
     "mcpServers": {
       "gdrive": {
         "command": "mcp-server-gdrive",
         "args": [],
         "env": {
           "GOOGLE_CLIENT_ID": "your-client-id",
           "GOOGLE_CLIENT_SECRET": "your-client-secret",
           "GOOGLE_REFRESH_TOKEN": "your-refresh-token"
         }
       }
     }
   }
   ```

2. **Получение токена:**
   - Перейти на https://console.cloud.google.com/
   - Создать OAuth 2.0 credentials
   - Получить refresh token

3. **Автоматический импорт:**
   - Claude Code подключится к Google Drive через MCP
   - Скачает все документы из папки
   - Конвертирует в Markdown
   - Распределит по структуре B.COFFEE
   - Создаст коммит

### Вариант 2: Ручной экспорт (быстрее для начала)

1. **Экспорт из Google Drive:**
   - Открыть папку: https://drive.google.com/drive/folders/120x7kqYeV0Vb4TLbdCC0esv0WkF5JROC
   - Выбрать все файлы → Скачать
   - Google автоматически конвертирует Docs → DOCX, Sheets → XLSX

2. **Конвертация в Markdown:**
   ```bash
   # Использовать pandoc для конвертации
   for file in *.docx; do
     pandoc "$file" -o "${file%.docx}.md"
   done
   ```

3. **Ручное распределение:**
   - Следовать mapping из этого документа
   - Переместить файлы в нужные папки B.COFFEE
   - Claude Code поможет с форматированием frontmatter

### Вариант 3: Публичный доступ + WebFetch

1. **Открыть доступ:**
   - В Google Drive: правый клик на папку → Открыть доступ
   - Выбрать "Доступен всем, у кого есть ссылка"

2. **Использовать WebFetch:**
   - Claude Code будет использовать WebFetch для доступа к документам
   - Ограничение: может не работать для всех типов файлов

---

## Следующие шаги

1. ✅ Создан mapping документов
2. ⏳ **Выбрать способ импорта** (API / Ручной / WebFetch)
3. ⏳ Импортировать Priority 1 документы
4. ⏳ Распределить по структуре B.COFFEE
5. ⏳ Добавить frontmatter к каждому документу
6. ⏳ Создать индексы (README.md в каждой папке)
7. ⏳ Закоммитить и запушить

---

**Версия:** 1.0
**Дата:** 2026-01-20
**Автор:** Claude Code + alexpoaiagent-sudo
