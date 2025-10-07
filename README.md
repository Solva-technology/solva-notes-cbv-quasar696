# Note App: Переписывание на CBV

## Цель
Проект был полностью рефакторен: все существующие view-функции заменены на class-based views (CBV). Это делает код более структурированным, гибким для расширения и удобным для поддержки.

## Описание проекта
**Note App** — учебное Django-приложение для работы с заметками.  
На текущем этапе проект включает:

- Админку и локализацию.
- Список заметок (главная), страницу отдельной заметки, страницы редактирования и удаления заметок.
- CRUD для модели `Note` через Django Forms.
- Систему пользователей: регистрация, авторизация, восстановление пароля.
- Разграничение прав доступа (редактировать и удалять заметки может только автор или администратор).
- Базовый шаблон `base.html`.
- Запуск приложения через Docker с PostgreSQL.

## Реализованные CBV

### Заметки
| Действие | CBV |
|-----------|-----|
| Список заметок | `ListView` |
| Просмотр заметки | `DetailView` |
| Создание заметки | `CreateView` |
| Редактирование заметки | `UpdateView` |
| Удаление заметки | `DeleteView` |

Формы настроены через `form_class` или `fields` в CBV. Шаблоны `note_form.html` и `note_confirm_delete.html` привязаны к CBV.

### Аутентификация и регистрация
| Действие | CBV |
|-----------|-----|
| Вход | `LoginView` |
| Выход | `LogoutView` |
| Регистрация | `CreateView` с кастомной формой |
| Сброс пароля | `PasswordResetView`, `PasswordResetDoneView`, `PasswordResetConfirmView`, `PasswordResetCompleteView` |

### Ограничение прав
- Использован `LoginRequiredMixin` для защиты всех приватных маршрутов.
- Для проверки прав на редактирование и удаление заметок использованы `UserPassesTestMixin` и `PermissionRequiredMixin`.
- Авторизация и проверка на автора/администратора полностью работают на уровне CBV.

## Требования и особенности
- Все функции во `views.py` переписаны на CBV.
- Используются стандартные Django CBV (`ListView`, `DetailView`, `CreateView`, `UpdateView`, `DeleteView`, `FormView` и др.).
- Сохраняется существующая структура URL'ов.
- Шаблоны работают без изменений или с минимальными правками.
- Проект готов к запуску через Docker + PostgreSQL.

---

## Стек технологий
- Python 
- Django 
- PostgreSQL
- Docker
- HTML, CSS (шаблоны Django)
- Django Forms, CBV

## Автор
**Aibar**  
Контакт: [GitHub](https://github.com/quasar696) 


---

## Запуск проекта

1. Склонировать репозиторий:
   ```bash
   git clone git@github.com:Solva-technology/solva-notes-cbv-quasar696.git
   cd notes_service
   ```

2. Запустить приложение в Docker:

   ```bash
   docker-compose up --build
   ```

3. Приложение будет доступно по адресу:
   [http://localhost:8000](http://localhost:8000)