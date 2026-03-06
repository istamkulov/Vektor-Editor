CLI Vector Editor

CLI Vector Editor — это консольное приложение на Python для создания и управления простыми векторными фигурами через интерфейс командной строки.

Проект демонстрирует базовую архитектуру Python-приложения с разделением на модели данных, бизнес-логику и CLI интерфейс, а также использование ООП и unit-тестирования.

Возможности

Поддерживаемые фигуры:

Point

Segment

Circle

Square

Основной функционал:

создание фигур

просмотр списка фигур

удаление фигур

валидация входных данных

unit-тесты

Структура проекта
vector-editor
│
├── app
│   ├── shapes.py
│   ├── editor.py
│   └── cli.py
│
├── tests
│   └── test_editor.py
│
├── main.py
├── requirements.txt
└── README.md
Архитектура
User → main.py → cli.py → editor.py → shapes.py

main.py — точка входа приложения

cli.py — обработка CLI команд

editor.py — бизнес-логика редактора

shapes.py — модели геометрических фигур

Установка и запуск
git clone https://github.com/your-username/vector-editor.git
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
