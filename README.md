# PT_START.INT-3
## Установка

1. Клонирование репозитория 

```git clone https://github.com/DanVilcka/PT_START.INT-3.git```

2. Переход в директорию INT-3

```cd INT-3```

3. Создание виртуального окружения

```python3 -m venv venv```

4. Активация виртуального окружения

```source venv/bin/activate```

5. Установка зависимостей

```pip3 install -r requirements.txt```

6. Запуск скрипта старта сервера. Не забудьте указать количество открытых портов!

```python3 server/server.py```

7. Запуск скрипта старта клиента. Введите название функции, в качестве параметров:
- для CheckLocalFile - сначала абсолютный путь к файлу, после сигнатуру в виде байтов через проблелы.
- для QuarantineLocal - сначала абсолютный путь к файлу, потом полный путь к необходимой папке.

```python3 client/client.py```


<video src='https://youtu.be/gi8hmI9l5TE' width=180/> 
[![Watch the video]](https://youtu.be/gi8hmI9l5TE)