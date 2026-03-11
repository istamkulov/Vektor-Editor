# CLI Vektor Editor

CLI Vektor Editor — это консольное приложение на Python для создания и управления векторными фигурами через интерфейс командной строки (CLI).

Проект демонстрирует базовую архитектуру Python-приложения с разделением на **модели данных, бизнес-логику и CLI интерфейс**, а также использование **ООП, работы с файлами и unit-тестирования**.

---

## Возможности

### Поддерживаемые фигуры

- Point
- Segment
- Circle
- Square
- Oval
- Rectangle

### Основной функционал

- создание фигур
- просмотр списка фигур
- удаление фигур
- сохранение фигур в файл
- загрузка фигур из файла
- валидация входных данных
- unit-тесты

---

## Структура проекта


vektor-editor/

app/                   # Основной код приложения
    shapes.py          # Классы геометрических фигур
    editor.py          # Бизнес-логика редактора
    cli.py             # CLI интерфейс

tests/                 # Unit-тесты
    test_editor.py     # Тестирование логики editor.py

main.py                # Точка входа приложения
requirements.txt       # Зависимости проекта
README.md              # Документация проекта

---

## Архитектура


User → main.py → cli.py → editor.py → shapes.py


**main.py**  
Точка входа приложения. Запускает CLI интерфейс.

**cli.py**  
Обрабатывает команды пользователя и передаёт их в редактор.

**editor.py**  
Реализует бизнес-логику управления фигурами:
- создание
- удаление
- хранение
- сохранение и загрузка из файла

**shapes.py**  
Содержит классы геометрических фигур.

---

## Установка и запуск

Клонировать репозиторий:

```bash
git clone https://github.com/istamkulov/vektor-editor.git
cd vektor-editor

или через SSH:

git clone git@github.com:istamkulov/vektor-editor.git
cd vektor-editor

Установить зависимости:

pip install -r requirements.txt

Запустить приложение:

python main.py
Примеры CLI команд

Создание фигур

create point 2 3
create segment 0 0 5 5
create circle 4 4 10
create square 1 1 5
create oval 3 3 6 4
create rectangle 2 2 8 5

Просмотр списка фигур

list

Удаление фигуры

delete 1

Сохранение фигур в файл

save shapes.json

Загрузка фигур из файла

load shapes.json

Выход из программы

exit
Тестирование

Проект содержит unit-тесты для проверки бизнес-логики редактора.

Запуск тестов:

python -m unittest discover tests
Технологии

Python 3

Object-Oriented Programming (OOP)

CLI интерфейс

Работа с файлами (JSON)

Unit testing (unittest)

Цель проекта

Проект создан как тестовое задание и демонстрирует:

навыки Python разработки

применение ООП

архитектуру CLI приложений

работу с файловым хранением данных

написание тестируемого кода

работу с Git и GitHub
