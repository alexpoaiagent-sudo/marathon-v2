# C.FPF — Ядро First Principles Framework

> **Источник правды для фундаментальных принципов мышления**

## О ядре

**C.FPF** — это ядро проекта VK-offee, содержащее полную спецификацию **First Principles Framework (FPF)** — операционной системы для мышления.

### Роль в multi-kernel архитектуре

C.FPF выступает **фундаментом** для других ядер:

```
C.FPF (Фундаментальные принципы)
  ↓ предоставляет философию и паттерны
A.SRT (Методология SRT)
  ↓ предоставляет структуру и процессы
B.COFFEE (Данные кофейни)
```

---

## Что внутри

### FPF-Spec.md (4.2 MB, ~50K строк)

Полная спецификация First Principles Framework, включающая:

**Part A: Kernel Architecture Cluster**
- Онтология: Holons, Systems, Epistemes, Bounded Contexts
- Трансформация: Agent, Method, Description, Work
- Пространство состояний: Characteristics, Scales, Dynamics

**Part B: Trans-disciplinary Reasoning Cluster**
- Γ Algebra: Композиция систем, знаний, ресурсов
- Assurance: F-G-R calculus и графы доказательств
- TGA: Transduction Graph Architecture
- Evolution: Циклы наблюдения, уточнения, развертывания

**Part C: Architheory Specifications**
- Sys-CAL: Физика и законы сохранения
- KD-CAL: Динамика знаний
- NQD-CAL: Novelty, Quality, Diversity поиск
- Kind-CAL: Типизированное рассуждение

**Part D: Ethics & Conflict-Optimisation**
- Многоуровневая этика
- Аудит предвзятости
- Медиация на основе доверия

**Part E: People & Projects (PPKA)**
- Роли, команды, проекты
- Управление знаниями

**Part F: Records & Tables**
- Концептуальные артефакты
- Таблицы, карточки, записи

**Part G: SoTA-Packs**
- Пакеты современных практик

### Readme.md (15K)

Обзор FPF, ключевые концепции, примеры использования.

---

## Ключевые принципы FPF

### 1. Holonic Foundation (A.1)
Всё — холон: одновременно целое и часть.
- Строгое разделение между физическими акторами (**Systems**) и артефактами знаний (**Epistemes**)

### 2. Contextual Meaning (A.1.1)
Значение локально в пределах Bounded Context.
- Межконтекстная коммуникация через явные **Bridges** с декларируемой потерей

### 3. Strict Distinction (A.7)
Никогда не путаем карту с территорией:
- **Role** ≠ **Method** ≠ **Work**
- Документы не "действуют"; только Systems выполняют Work

### 4. Trust & Assurance Calculus (B.3)
Доверие — это вычисляемый кортеж **⟨F, G, R⟩**:
- **F (Formality)**: Насколько строго выражено?
- **G (Claim Scope)**: Где применимо?
- **R (Reliability)**: Насколько подкреплено доказательствами?

### 5. Evolution & Creativity (B.4, C.18)
Системы должны эволюционировать через:
- **NQD**: Novelty-Quality-Diversity
- Явные политики Explore-Exploit

### 6. Universal Aggregation (Γ)
Единая алгебра композиции, сохраняющая инварианты (например, "слабое звено" для надёжности).

---

## Как использовать C.FPF

### Для AI-агентов

**ВАЖНО:** FPF предназначен для загрузки как файл в RAG, **НЕ** в контекст LLM!

```python
# Неправильно: загружать FPF-Spec.md в контекст (слишком большой)
# Правильно: использовать через RAG

# Промпт для работы с FPF через RAG:
"You have FPF in a file. Use it but answer with no FPF-specific
terminology. Answer as to engineer-manager."
```

### Для людей

**Не пытайтесь прочитать FPF-Spec.md целиком!**
- Это не книга, а спецификация (как исходный код ОС)
- Используйте как атлас: ищите нужные паттерны через LLM
- Читайте `Readme.md` для понимания общей концепции

### Для других ядер

**A.SRT применяет паттерны FPF:**
- Holonic Foundation → Структура SRT 3×3
- Bounded Context → Семейства документов F0-F9
- Strict Distinction → Разделение систем, ролей, методов

**B.COFFEE применяет через A.SRT:**
- Транзитивно использует принципы FPF
- Организация знаний по холоническому принципу

---

## Связи с другими ядрами

| От ядра | К ядру | Тип связи | Описание |
|---------|--------|-----------|----------|
| C.FPF | A.SRT | Philosophy Provider | Предоставляет фундаментальные принципы мышления |
| C.FPF | B.COFFEE | Philosophy Provider (транзитивно) | Через A.SRT |
| A.SRT | C.FPF | Philosophy Consumer | Применяет паттерны FPF к SRT-методу |
| B.COFFEE | C.FPF | Philosophy Consumer (транзитивно) | Через A.SRT |

---

## Кто автор?

**Primary Author:** Anatoly Levenchuk (with LLM assistance)
**Version:** January 2026
**Status:** Normative kernel, "eternal alpha"

**Upstream репозиторий:** https://github.com/TserenTserenov/FPF (original)
**Fork:** https://github.com/alexpoaiagent-sudo/FPF

---

## Для кого FPF?

- **Инженеры** — строят надежные физические или кибер-физические системы
- **Исследователи** — конструируют достоверные знания и теории
- **Менеджеры** — оркеструют коллективный интеллект, бюджеты, эволюционные циклы

---

## Метафора: FPF как ОС

Используя метафору операционной системы:

- **Запускает "приложения мышления"**: Канонический цикл рассуждения (abduction–deduction–induction)
- **Изолирует процессы**: Bounded Context как "адресное пространство значений"
- **Создаёт и завершает процессы**: Цепочка holon → role → method → work
- **Управляет памятью**: Evidence Graphs и контекстные паспорта
- **Готовит управление ресурсами**: Γ_work оператор композиции
- **Предоставляет "файловую систему"**: Карточки, таблицы, записи (RSR/RSCR, F-cluster)
- **Расширяемая архитектура**: Минимальное ядро + подключаемые CAL, LOG, CHR, SoTA-packs

---

## Разумные ожидания

✅ **SoTA-смещённый со-мыслитель**: При загрузке в LLM через RAG, FPF действует как bias-assistant
✅ **DDD-backbone для дисциплин**: Моделируй дисциплину с явными контекстами, ролями, исчислениями
✅ **Долгосрочный атлас**: Исследуй, запрашивай, извлекай паттерны через LLM
✅ **Ядро для программ развития**: Уже питает программы развития инженеров-менеджеров

## Неразумные ожидания

❌ **"Прочитаю за раз и составлю мнение"**: Это код, а не популярная книга
❌ **"Plug-and-play инструмент"**: Требуется адаптация к вашей дисциплине
❌ **"Работает без 'заклинаний'"**: LLM+FPF не думает за вас
❌ **"Игнорирую принципы, FPF всё исправит"**: FPF усиливает ваш стиль мышления

---

## Навигация

**Для изучения FPF:**
- Читай [Readme.md](Readme.md) — обзор и концепции
- Изучай [FPF-Spec.md](FPF-Spec.md) через LLM — конкретные паттерны

**Для понимания роли в проекте:**
- [0.KERNELS/kernel-map.md](../0.KERNELS/kernel-map.md) — карта ядер
- [0.KERNELS/connections.md](../0.KERNELS/connections.md) — связи между ядрами

**Для применения в других ядрах:**
- [A.SRT/README.md](../A.SRT/README.md) — как SRT применяет FPF
- [B.COFFEE/README.md](../B.COFFEE/README.md) — как кофейня использует методологию

---

**Версия:** 1.0 (интеграция в VK-offee)
**Дата:** 2026-01-20
**Интегрировано:** Claude Code + alexpoaiagent-sudo
