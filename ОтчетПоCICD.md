# Отчет по лабораторной работе: Настройка CI/CD с GitHub Actions

## Цель работы
Настроить автоматическое выполнение unit-тестов с помощью GitHub Actions после каждой операции push и pull_request в репозиторий.

## Задачи
1. Разработать workflow файл для GitHub Actions
2. Реализовать запуск unit-тестов на двух операционных системах: ubuntu-latest и windows-latest
3. Протестировать работу workflow файла
4. Составить документацию по результатам работы

# Выполнение работы

## 1. Создание workflow файла

Был создан файл `main.yml`:

```yaml

name: Unit Tests Runner
on:
  push:
    branches: [ "main" ]
  pull_request:
    branches: [ "main" ]

jobs:
  linux_test:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Setup python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'

      - name: Test rectangle.py
        run: python unit_tests.py

  windows_test:
    runs-on: windows-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Setup python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'
      - name: Test rectangle.py
        run: python unit_tests.py

```

## 2. Описание workflow файла

### Структура workflow:

* Триггеры: запуск при push и pull request в ветки main и master

* Задачи: две параллельные задачи - test-linux и test-windows

* Runner'ы: ubuntu-latest и windows-latest

### Шаги:

1. Checkout code - клонирование репозитория

2. Setup Python - установка Python последней версии

3. Test rectangle.py - выполнение тестов для прямоугольника

## 3. Тестирование workflow

После создания yml файла и выполнения push, Workflow успешно запустился на GitHub:
![alt text](<photo.png>)