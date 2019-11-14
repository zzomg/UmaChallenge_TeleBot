# UmaChallenge_TeleBot

Этот проект представляет собой Telegram бота для классификации изображений футболистов из предоставленного датасета, в основе которого лежит нейросеть, написанная на FastAI.

**Нейросеть** можно найти здесь: https://colab.research.google.com/drive/1QH6_NsRfRYN3F_ygFpWr9nfbVRK8hYHi.
С помощью этой модели на тестовых данных удалось достигнуть **accuracy 95%** (модель с этим результатом была экспортирована в файл **export.pkl**):

![Image alt](https://github.com/zzomg/UmaChallenge_TeleBot/blob/master/res.png)

Для запуска бота необходимо:

1. Обучить [модель](https://colab.research.google.com/drive/1QH6_NsRfRYN3F_ygFpWr9nfbVRK8hYHi) и получить файл .pkl. **Либо** воспользоваться уже готовым вариантом (файл export.pkl).

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
