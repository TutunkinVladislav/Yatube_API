# api_final_yatube

### Описание

Этот api сервис предназначачен для просмотра постов от разных людей, так же возможно стать автором для создания своих собственных постов. Имеется возсможность подписаться на аатора постов, которые понравились. Под каждым постом можно оставить комментарий и посмотреть на комментарии других

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/TutunkinVladislav/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python -m venv venv
```

```
source venv/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

### Примеры

1. api/v1/posts/
   - GET: Просмотр всех постов
   - POST: Создание поста

2. api/v1/posts/{id}/
   - GET: Просмотр поста по его id
   - UPDATE, : Редактирование поста
   - DELETE: Удаление поста
   
3. api/v1/groups/
   - GET: Просмотр групп
   - POST: Создание группы
   
4. api/v1/groups/{id}/
   - GET: Просмотр группы по её id
   - UPDATE, : Редактирование группы
   - DELETE: Удаление группы
   
5. api/v1/posts/{post_id}/comments/
   - GET: Просмотр комментариев поста по его id
   - POST: Создание нового комментария
   
6. api/v1/posts/{post_id}/comments/{id}/
   - GET: Просмотр комментария по его id
   - UPDATE, : Редактирование комментария
   - DELETE: Удаление комментария
   
7. api/v1/follow/
   - GET: Просмотр подписок пользователя
   - POST: Создание подписки
