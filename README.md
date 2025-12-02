# pytest_ui_api_template
## Шаблон для автоматизации тестирования на python
### Стек:
- pytest
- selenium
- requests
- _sqlalchemy_
- allure
- config
### Структура:
- ./test - тесты
- ./pages - описание страниц
- ./api - хелперы для работы с API
- ./db - хелперы для работы с БД
### Полезные ссылки
- [Подсказка по markdown](https://www.markdownguide.org/basic-syntax/)
### Шаги
1. Склонировать проект 'git clone https://github.com/enje8/final_project.git'
2. Установить зависимости
3. Запустить api тесты `python3 -m pytest test/test_api.py -s -v`
4. Запустить ui тесты `python3 -m pytest test/test_ui.py -s -v`
5. Сгенерировать отчет 'allure generate allure-files -o allure-report'
6. Открыть отчет 'allure open allure-report'
### Библиотеки (!)
- pyp install pytest
- pip install selenium
- pip install webdriver-manager
- pip install allure-pytest
- pip install requests
