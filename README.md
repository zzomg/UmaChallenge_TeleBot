# UmaChallenge_TeleBot

Этот проект представляет собой Telegram бота для классификации изображений футболистов из предоставленного датасета. Классификатор написан на FastAI.

**UPD**: Проект занял 3-е место на Uma.Challenge https://challenge.uma.tech/ 🎉

**Бот в telegram**: @umatechbot (в данный момент отключен)

**Ссылка на ноутбук**: https://colab.research.google.com/drive/1QH6_NsRfRYN3F_ygFpWr9nfbVRK8hYHi.
Метрики: **accuracy 95%** (модель: **[export.pkl](https://drive.google.com/open?id=1eZ0GUVUKWkVGuhbBem4h0ujZvrhsbSZ4)**):

![Image alt](https://github.com/zzomg/UmaChallenge_TeleBot/blob/master/res.png)

Для запуска бота необходимо:

1. Обучить [модель](https://colab.research.google.com/drive/1QH6_NsRfRYN3F_ygFpWr9nfbVRK8hYHi) и получить файл .pkl. Либо воспользоваться уже готовым вариантом (файл export.pkl).

2. Файлы из папки telebot загрузить на сервер (в моем случае бот хостится на Amazon Lightsail). 

3. Создать виртуальное окружение, активировать его и установить нужные библиотеки из файла requirements.txt. 
```
$ pip3 install --upgrade virtualenv
$ virtualenv -p python3 envname
$ source envname/bin/activate
(envname) $ pip3 install -r requirements.txt
```

4. Создать бота. В Telegram найти @BotFather - бота для создания ботов. Команда /newbot позволяет создать бота. Следовать инструкциям от @BotFather и дать боту имя. Получить токен.

5. Модифицировать config.py (вставить свой личный токен, прописать пути до папок для хранения получаемых картинок и папки с экспортированной моделью в формате .pkl).

6. Запустить бота.
```
$ nohup python3 app.py &
```

7. При возникновении ошибок см. файл loginfo. 

---
