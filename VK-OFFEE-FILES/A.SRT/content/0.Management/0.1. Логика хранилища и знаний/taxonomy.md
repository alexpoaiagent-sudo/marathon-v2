---
type: doc
status: active
created: 2026-01-07
updated: 2026-01-07
system: "Management"
role: "Предприниматель"
layer: methodology
scope: local-edge
target_audience: [ai-agents, administrators, contributors]
related:
  - principles.md
  - glossary.md
fpf_principles:
  - systemic-thinking
  - metadata-first
fpf_patterns:
  - A.2      # Role Taxonomy
---

# Классификация и теги

## Назначение документа

Система классификации документов и правила использования тегов для организации и поиска информации.

## Системы классификации

### 1. По системе (SRT)

| Код | Система | Описание |
|-----|---------|----------|
| 0 | Management | Метасистема, управление хранилищем |
| 1 | Supersystem | Внешняя среда, контекст |
| 2 | TargetSystem | Целевой продукт |
| 3 | CreationSystem | Процесс создания |

### 2. По роли (SRT)

| Код | Роль | Вопрос | Описание |
|-----|------|--------|----------|
| 1 | Предприниматель | Зачем? | Цели, ценности, требования |
| 2 | Инженер | Как устроено? | Структура, компоненты |
| 3 | Менеджер | Как работает? | Процессы, действия |

### 3. По типу документа

| Тип | Описание | Примеры |
|-----|----------|---------|
| `doc` | Концептуальный | Принципы, описания, обзоры |
| `spec` | Спецификация | API, схемы, модели |
| `process` | Процессный | Workflows, инструкции |
| `report` | Отчёт | Аналитика, статусы |
| `template` | Шаблон | Образцы документов |

### 4. По статусу

| Статус | Описание | Использование |
|--------|----------|---------------|
| `stub` | Заглушка | Идея, placeholder |
| `draft` | Черновик | В работе |
| `active` | Актуальный | Готов к использованию |
| `archived` | Архив | Устарел, для истории |

### 5. По слою (layer)

| Слой | Описание |
|------|----------|
| `methodology` | Методологические документы |
| `architecture` | Архитектурные решения |
| `operations` | Операционные процессы |
| `data` | Данные и модели |

### 6. По области применения (scope)

| Область | Описание |
|---------|----------|
| `local-edge` | Локальный, специфичный |
| `project` | Уровень проекта |
| `ecosystem` | Уровень экосистемы |
| `universal` | Универсальный |

## Система тегов

### Правила тегирования

1. **Нижний регистр:** `api`, не `API`
2. **Дефис для составных:** `api-design`, не `api_design`
3. **Единственное число:** `requirement`, не `requirements`
4. **Английский язык:** для совместимости

### Категории тегов

#### Технические теги
```
api, database, frontend, backend, infrastructure,
security, performance, testing, deployment
```

#### Процессные теги
```
planning, review, retrospective, meeting,
workflow, automation, monitoring
```

#### Предметные теги
```
user, customer, product, feature, requirement,
architecture, design, implementation
```

#### FPF-теги
```
fpf, holon, context, bridge, trust,
evidence, evolution, assurance
```

### Таблица соответствия

| Система | Типичные теги |
|---------|---------------|
| Management | management, process, workflow, planning |
| Supersystem | market, stakeholder, context, environment |
| TargetSystem | product, feature, requirement, architecture |
| CreationSystem | development, tool, methodology, practice |

| Роль | Типичные теги |
|------|---------------|
| Предприниматель | goal, value, requirement, vision, mission |
| Инженер | structure, component, interface, schema |
| Менеджер | process, workflow, action, monitoring |

## Использование в frontmatter

```yaml
---
type: doc
status: active
system: "TargetSystem"
role: "Инженер"
layer: architecture
scope: project
tags:
  - api
  - design
  - rest
fpf_principles:
  - clarity
  - practicality
fpf_patterns:
  - A.1
  - A.7
---
```

## Поиск по классификации

### Примеры запросов

**Найти все активные документы по архитектуре:**
```
status: active AND role: Architecture
```

**Найти документы с тегом api в TargetSystem:**
```
system: TargetSystem AND tags: api
```

**Найти черновики для review:**
```
status: draft
```

## Changelog

| Дата | Изменение | Автор |
|------|-----------|-------|
| 2026-01-07 | Создание документа | Claude |

## Связанные документы

- [Принципы организации](principles.md)
- [Глоссарий](glossary.md)
- [Стандарты оформления](../0.2.%20Процессы%20работы%20с%20хранилищем/standards.md)
