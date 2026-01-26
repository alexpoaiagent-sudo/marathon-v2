---
type: spec
status: active
created: 2026-01-07
updated: 2026-01-07
system: "Management"
role: "ValidationSpecs"
layer: methodology
scope: local-edge
target_audience: [ai-agents]
related:
  - README.md
fpf_principles:
  - metadata-first
  - continuous-validation
fpf_patterns:
  - B.3
---

# ТЗ: Проверка YAML Frontmatter

## Цель проверки

Убедиться, что все документы в `content/` имеют корректный YAML frontmatter с обязательными полями.

## Входные данные

Все файлы `*.md` в директории `content/`

## Правила валидации

### Правило 1: Наличие frontmatter

- **Условие:** Любой `.md` файл в `content/`
- **Ожидание:** Файл начинается с `---` и содержит YAML-блок
- **Ошибка:** `FRONTMATTER_MISSING: Файл не содержит YAML frontmatter`
- **Критичность:** critical

### Правило 2: Обязательное поле `type`

- **Условие:** Файл имеет frontmatter
- **Ожидание:** Поле `type` присутствует и имеет значение из списка: `doc`, `spec`, `process`, `report`, `template`
- **Ошибка:** `TYPE_INVALID: Поле type отсутствует или имеет недопустимое значение`
- **Критичность:** critical

### Правило 3: Обязательное поле `status`

- **Условие:** Файл имеет frontmatter
- **Ожидание:** Поле `status` присутствует и имеет значение из списка: `stub`, `draft`, `active`, `archived`
- **Ошибка:** `STATUS_INVALID: Поле status отсутствует или имеет недопустимое значение`
- **Критичность:** critical

### Правило 4: Обязательное поле `system`

- **Условие:** Файл имеет frontmatter
- **Ожидание:** Поле `system` присутствует и имеет значение из списка: `Management`, `Suprasystem`, `System-of-Interest`, `Constructor`
- **Ошибка:** `SYSTEM_INVALID: Поле system отсутствует или имеет недопустимое значение`
- **Критичность:** critical

### Правило 5: Обязательное поле `role`

- **Условие:** Файл имеет frontmatter
- **Ожидание:** Поле `role` присутствует
- **Ошибка:** `ROLE_MISSING: Поле role отсутствует`
- **Критичность:** high

### Правило 6: Поля дат

- **Условие:** Файл имеет frontmatter
- **Ожидание:** Поля `created` и `updated` присутствуют в формате `YYYY-MM-DD`
- **Ошибка:** `DATE_INVALID: Поля created/updated отсутствуют или имеют неверный формат`
- **Критичность:** medium

### Правило 7: Соответствие пути и system

- **Условие:** Файл находится в `content/N.{System}/`
- **Ожидание:** Значение `system` в frontmatter соответствует папке
- **Ошибка:** `PATH_MISMATCH: system в frontmatter не соответствует пути файла`
- **Критичность:** high

## Выходные данные

```json
{
  "total_files": 15,
  "passed": 12,
  "failed": 3,
  "errors": [
    {
      "file": "content/2.System-of-Interest/2.1.Meaning/doc.md",
      "rule": "TYPE_INVALID",
      "message": "Поле type отсутствует",
      "criticality": "critical"
    }
  ]
}
```

## Команда запуска

```
Проверь все документы в content/ по ТЗ frontmatter-spec.md
и сгенерируй отчёт в 0.4.AutoReports/
```
