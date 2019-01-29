# Памятка для Front-End разработчика
## Я немного изменил пути
```
@app.route('/tablet/<ekran>/<lang>/') # Для планшетов
@app.route('/click/<ekran>/<lang>/<id>') # Для кликов
@app.route('/disp/<ekran>/<lang>') # Для экранов
```

## Пути внутри js файлов

Пути внутри js файлов надо писать вот так:
```
img.setAttribute('src', "http://" + window.location.hostname + ':8888/static/image/logo-white.png');
```

А не так:

```
leftSidebar.innerHTML = `<img src="static/image/logo-white2.png" alt="logo">
```

Суть в добавлении *HOSTNAME*

## Отмена кэширования JSON файлов

Для отмены кэширования json пакетов, надо засунуть в нее временную переменную, вот так:

```
xhr.open('GET', "http://" + window.location.hostname + ':8888/static/json/data.json?' + new Date().getTime(), true);
```

То есть добавляем timestamp:

```
+ new Date().getTime()
```

## Загрузка MonoDB

Загружаешь его с помощью утилиты mongorestore в папке main:
```
mongorestore ./mongodump/NOtest
```
