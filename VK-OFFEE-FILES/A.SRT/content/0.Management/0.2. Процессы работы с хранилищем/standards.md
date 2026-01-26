---
type: doc
status: active
created: 2026-01-07
updated: 2026-01-07
system: "Management"
role: "Инженер"
layer: architecture
scope: local-edge
target_audience: [ai-agents, contributors]
related:
  - structure.md
  - roles.md
  - "../0.1. Логика хранилища и знаний/taxonomy.md"
fpf_principles:
  - clarity
  - metadata-first
fpf_patterns:
  - E.8      # Pattern Authoring
---

# Стандарты оформления документов

## Назначение документа

Правила форматирования и оформления документов в хранилище.

## Формат документа

### Общая структура

```markdown
---
[YAML frontmatter]
---

# Заголовок документа

## Назначение документа

[1-2 предложения о цели документа]

## Основное содержание

[Контент документа]

## Changelog

[Таблица изменений]

## Связанные документы

[Список ссылок]
```

## YAML Frontmatter

### Обязательные поля

```yaml
---
type: doc                    # doc, spec, process, report, template
status: active               # stub, draft, active, archived
created: 2026-01-07          # Дата создания ISO 8601
updated: 2026-01-07          # Дата обновления ISO 8601
system: "Management"         # Management, Suprasystem, System-of-Interest, Constructor
role: "Предприниматель"      # Предприниматель, Инженер, Менеджер
---
```

### Рекомендуемые поля

```yaml
---
layer: methodology           # methodology, architecture, operations, data
scope: local-edge            # local-edge, project, ecosystem, universal
target_audience: [developers, managers]
related:
  - path/to/doc.md
fpf_principles:
  - minimalism
  - practicality
fpf_patterns:
  - A.1
  - B.3
tags:
  - api
  - design
---
```

### Полный пример

```yaml
---
type: spec
status: active
created: 2026-01-07
updated: 2026-01-07
system: "System-of-Interest"
role: "Инженер"
layer: architecture
scope: project
target_audience: [developers, architects]
related:
  - ../2.1.Meaning/requirements.md
  - ../2.3.Operations/implementation.md
fpf_principles:
  - clarity
  - idempotency
fpf_patterns:
  - A.1
  - A.7
tags:
  - api
  - rest
  - schema
---
```

## Markdown-форматирование

### Заголовки

```markdown
# H1 — только для названия документа (один на файл)
## H2 — основные разделы
### H3 — подразделы
#### H4 — детали (редко)
```

### Списки

```markdown
Маркированный список:
- Пункт 1
- Пункт 2
  - Вложенный пункт

Нумерованный список:
1. Первый шаг
2. Второй шаг
3. Третий шаг
```

### Таблицы

```markdown
| Заголовок 1 | Заголовок 2 | Заголовок 3 |
|-------------|-------------|-------------|
| Данные 1    | Данные 2    | Данные 3    |
| Данные 4    | Данные 5    | Данные 6    |
```

### Код

Inline: `` `code` ``

Блок:
````markdown
```language
code block
```
````

### Ссылки

```markdown
[Текст ссылки](path/to/file.md)
[Внешняя ссылка](https://example.com)
```

### Выделение

```markdown
**Жирный** — важное
*Курсив* — акцент
~~Зачёркнутый~~ — устаревшее
```

## Правила оформления

### Именование файлов

| Правило | Хорошо | Плохо |
|---------|--------|-------|
| Нижний регистр | `api-design.md` | `API-Design.md` |
| Дефис | `user-auth.md` | `user_auth.md` |
| Описательное имя | `database-schema.md` | `db.md` |
| Английский | `requirements.md` | `требования.md` |

### Язык документа

- **Русский** — для описаний, документации
- **Английский** — для кода, тегов, технических терминов

### Длина строки

- Рекомендуется: до 100 символов
- Максимум: 120 символов
- Таблицы: исключение

### Структура разделов

1. **Назначение** — всегда первый раздел после заголовка
2. **Основное содержание** — суть документа
3. **Changelog** — история изменений
4. **Связанные документы** — ссылки

## Шаблоны

### Шаблон документа (doc)

```markdown
---
type: doc
status: draft
created: YYYY-MM-DD
updated: YYYY-MM-DD
system: "SystemName"
role: "Предприниматель/Инженер/Менеджер"
related: []
fpf_principles: []
---

# Название документа

## Назначение документа

[Краткое описание цели]

## [Основной раздел]

[Содержание]

## Changelog

| Дата | Изменение | Автор |
|------|-----------|-------|
| YYYY-MM-DD | Создание | Name |

## Связанные документы

- [Документ 1](path/to/doc1.md)
```

### Шаблон спецификации (spec)

```markdown
---
type: spec
status: draft
created: YYYY-MM-DD
updated: YYYY-MM-DD
system: "System-of-Interest"
role: "Инженер"
---

# Спецификация: [Название]

## Назначение

[Что специфицируется]

## Требования

[Входные требования]

## Спецификация

[Детальное описание]

## Примеры

[Примеры использования]
```

## Changelog

| Дата | Изменение | Автор |
|------|-----------|-------|
| 2026-01-07 | Создание документа | Claude |

## Связанные документы

- [Структура хранилища](structure.md)
- [Классификация и теги](../0.1.%20Логика%20хранилища%20и%20знаний/taxonomy.md)
- [Создание документов](document-creation.md)
