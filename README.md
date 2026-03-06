# CLI Vector Editor

CLI Vector Editor — это консольное приложение на Python для создания и управления простыми векторными фигурами через интерфейс командной строки.

Проект демонстрирует базовую архитектуру Python-приложения с разделением на **модели данных, бизнес-логику и CLI интерфейс**, а также использование ООП и unit-тестирования.

---

## Возможности

**Поддерживаемые фигуры:**

- Point
- Segment
- Circle
- Square

**Основной функционал:**

- создание фигур
- просмотр списка фигур
- удаление фигур
- валидация входных данных
- unit-тесты

---

## Структура проекта

vector-editor/

    app/                   # Основной код приложения
        shapes.py          # Классы геометрических фигур (Point, Segment, Circle, Square)
        editor.py          # Бизнес-логика для создания, удаления и управления фигурами
        cli.py             # CLI интерфейс: обработка команд пользователя
        
    tests/                 # Unit-тесты
        test_editor.py     # Тестирование логики editor.py

    main.py                # Точка входа приложения
    requirements.txt       # Зависимости проекта
    README.md              # Документация проекта
---

## Архитектура


User → main.py → cli.py → editor.py → shapes.py


- **main.py** — точка входа приложения  
- **cli.py** — обработка CLI команд  
- **editor.py** — бизнес-логика редактора  
- **shapes.py** — модели геометрических фигур  

---

## Установка и запуск

```bash
git clone https://github.com/istamkulov/vector-editor.git
git clone git@github.com:istamkulov/vector-editor.git
cd vector-editor
pip install -r requirements.txt
python main.py
Тестирование
python -m unittest discover tests
Технологии

Python 3

OOP

CLI

unittest

Цель проекта

Демонстрация навыков:

Python разработки

объектно-ориентированного программирования

проектирования архитектуры приложений

написания тестируемого кода

работы с Git и GitHub
