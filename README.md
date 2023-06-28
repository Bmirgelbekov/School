# О проекте
Техническое задание 

## Настройка проекта

### Создайте виртуальное окружение

```bash
python3 -m venv venv
```

### Активируйте виртуальное окружение

```bash
source venv/bin/activate
```

### Используйте pip для установки библиотек

```bash
pip install -r requirements.txt
```

### Создайте базу данных в PostgreSQL

```bash
createdb <db_name>
```

### Создайте файл .env и заполните данные как в .env.template

```bash
cat .env.template > .env
```
### Для удобства добавлен Makerile

```bash
make migrate:
	python3 manage.py makemigrations
	python3 manage.py migrate

make run:
	python3 manage.py runserver
```

### Проведите миграции

```bash
python3 manage.py makemigrations
python3 manage.py migrate
```

### Создайте супер-пользователя

```bash
python3 manage.py createsuperuser
```

### Запустите сервер

```bash
python3 manage.py runserver
```


