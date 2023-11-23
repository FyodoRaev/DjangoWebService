# DjangoWebService
Вы говорили, что можно выбрать себе проект, который не будет использовать те же инструменты, но реализует себе схожий функционал. Так как я не очень хочу заниматься Java и Rest API я решил изучать Django.

<img title="a title" alt="Alt text" src="basic-django.png">


ДЗ по информатике:
* Я реализваол простейший веб сервис с Django, он отвечает на запрос message выводя сообщение на HTML страницу, показывает число книг в библиотеке (сами книги и их описание хранится SQLite базе данных, позже я добавлю функционал просморта описаний книг и авторов). Реализовал ответ на запрос с пустой URL строкой - просто home страница без message
* Вообще говоря конкретно этот веб-сервис - локальная библиотека, в которой впоследствии должны быть реализованы хранение книг, их описание, хранение информации о жанре /жанрах и авторе книги, поэтому в моделях Genre, Book и BookInstance и описаны соовтествующие поля.
    * Для BookInstance мы дополнительно объявляем несколько новых типов полей:
        * UUIDField используется для поля id, чтобы установить его как primary_key для этой модели. Этот тип поля выделяет глобальное уникальное значение для каждого экземпляра (по одному для каждой книги, которую вы можете             найти в библиотеке).
        * DateField используется для данных due_back (при которых ожидается, что книга появится после заимствования или обслуживания). Это значение может быть blank или null (необходимо, когда книга доступна). Метаданные               модели (Class Meta) используют это поле для упорядочивания записей, когда они возвращаются в запросе.
        * status - это CharField, который определяет список choice/selection. Как вы можете видеть, мы определяем кортеж, содержащий кортежи пар ключ-значение и передаём его аргументу выбора. Значение в key/value паре - это             отображаемое значение, которое пользователь может выбрать, а ключи - это значения, которые фактически сохраняются, если выбрана опция. Мы также установили значение по умолчанию «m» (техническое обслуживание),                 поскольку книги изначально будут созданы недоступными до того, как они будут храниться на полках.

