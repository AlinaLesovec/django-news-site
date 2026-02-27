# Django News Site

Практическая работа 23.  
Создано веб-приложение для публикации новостей с использованием Django и SQLite.

## 📌 Описание проекта

- Сайт новостей с главной страницей и страницей отдельной новости  
- Фильтрация новостей по заголовку  
- Административная панель для управления статьями  
- Использованы Class-Based Views (CBV)  
- Простое оформление через встроенный CSS  

## 🧱 Структура проекта

```text
news_site/
├── manage.py
├── pyproject.toml
├── .env
├── news_site/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── news/
    ├── models.py
    ├── views.py
    ├── admin.py
    └── templates/news/
        ├── base.html
        ├── article_list.html
        └── article_detail.html
