# Решение Sql задач

1. Решение
```sql   
UPDATE full_names
SET status = (
  SELECT status   
  FROM short_names 
  WHERE name = SUBSTRING(full_names.name, 1, LENGTH(full_names.name) - 4) 
);
```

2. Решение
   
```sql
UPDATE full_names
SET status = short_names.status
FROM short_names
WHERE fn.name LIKE sn.name;
```


# **Документация к API**

# Технологии
- Python 3.11+
- FastAPI
- FastAPI-Cache
- Redis (для кэширования)

## Как развернуть
### 1. Разворачивание с помощью Docker

- Клонируем репозиторий
```
git clone https://github.com/ded2322/api_phone_cach.git
```
- Переходим в директорию
```
cd api_phone_cach
```
- Прописываем в консоле команду
```
docker-compose up --build
```
- Документация к api находятся по адресу: http://localhost:8000/docs
### Нюансы с docker
<p align="center">
   <img src="img.png" width="250" height="200">
</p>
Обновление адреса работает, 
но только после остановки контейнеров и пересборки контейнеров:

``` docker-compose up --build```

Что я пытался сделать для решения этой проблемы:
- Я пытался сделать очистку по ключу, но инструмент просто не чистит ключ, а как фиксить хз

Предположительно решение проблемы:
- Скорее всего проблема, что docker-compose не отслеживает обновления в redis и нужно сделать выгрузку на диск. 

Я бы такое провернул, но у меня не хватило свободного времени(.

НО

Если это api запускать не в докере, то все работает прекрасно.


### 2. Разворачиваем без docker
1. Иметь установленный python 3.11+

2. Установка зависимостей  
```bash
    pip install -r requirements.txt
```
3. Запускаем сервер
```
uvicorn core.main:app --port 8000 --reload
```
- Теперь документация к api находятся по адресу: http://localhost:8000/docs

#### Кто-то вообще это читает?. Если да, то держи анек, чтобы было не так скучно
Снёс конь яйцо… Да не простое, а деду копытом.