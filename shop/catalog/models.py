from django.db import models



class Thinners(models.Model):
    name = models.CharField(max_length=30, help_text='Здесь пишем наименование растворителя',
                            verbose_name='Наименование')
    purpose = models.CharField(max_length=50, help_text='Здесь пишем назначение растворителя',
                               verbose_name='Назначение')
    price = models.CharField(max_length=20, help_text='Здесь пишем цену растворителя', verbose_name='Цена')
    currency = models.CharField(max_length=20, help_text='Здесь пишем валюту растворителя', verbose_name='Валюта')
    description = models.TextField(help_text='Здесь пишем комментарий', verbose_name='Комментарий')
    country = models.CharField(max_length=50, help_text='Здесь пишем страну производства растворителя',
                               verbose_name='Страна')
    photo = models.ForeignKey('Im', on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return self.name


class Ukr_thinners(models.Model):
    name = models.CharField(max_length=30, help_text='Здесь пишем наименование растворителя',
                            verbose_name='Наименование')
    purpose = models.CharField(max_length=50, help_text='Здесь пишем назначение растворителя',
                               verbose_name='Назначение')
    price = models.CharField(max_length=20, help_text='Здесь пишем цену растворителя', verbose_name='Цена')
    currency = models.CharField(max_length=20, help_text='Здесь пишем валюту растворителя', verbose_name='Валюта')
    description = models.TextField(help_text='Здесь пишем комментарий', verbose_name='Комментарий')
    country = models.CharField(max_length=50, help_text='Здесь пишем страну производства растворителя',
                               verbose_name='Страна')
    photo = models.ForeignKey('Im', on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return self.name


class Im(models.Model):
    img = models.ImageField(upload_to='static/photo/', db_index=True, verbose_name='Фото', blank=True)


class News(models.Model):
    head = models.CharField(max_length=50, help_text='Здесь пишем заголовок новости', verbose_name='Заголовок')
    text = models.TextField(help_text='Здесь пишем новость', verbose_name='Текст новости')
    picture = models.ImageField(upload_to='static/photo/%Y/%m/%d/', db_index=True,
                                verbose_name='Фото к новости', blank=True)
    date = models.DateTimeField(auto_now_add=True, help_text='Здесь у нас дата опубликования новости',
                                verbose_name='Дата опубликования')

    # def get_absolute_url(self):
    #     return reverse_lazy('news',kwargs={'news_pk':self.pk})
    def __str__(self):
        return self.head


class Order(models.Model):
    name = models.CharField(max_length=30,
                            verbose_name='Растворитель иностранный', null=True, blank=True)
    ukr_name = models.CharField(max_length=30,
                                verbose_name='Растворитель украинский', null=True, blank=True)
    purpose = models.CharField(max_length=50,
                               verbose_name='Количество', null=True, blank=True)
    description = models.TextField(verbose_name='Дополнительная информация', null=True, blank=True)

    def __str__(self):
        return f'{self.name}({self.ukr_name})'


class Feedback(models.Model):
    fio = models.CharField(max_length=50, verbose_name='Напишите Ваше имя, фамилию, и название организации')
    mail = models.EmailField(verbose_name='Электронная почта', null=True, blank=True)
    phone = models.CharField(max_length=13, verbose_name='Номер телефона, пожалуйста', null=True, blank=True)
    text = models.TextField(verbose_name='Текст обращения', null=True, blank=True)

    def __str__(self):
        return self.fio
