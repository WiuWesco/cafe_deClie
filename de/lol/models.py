from django.db import models
class for_main(models.Model):
    image = models.ImageField(upload_to="for_main")
    color_background = models.CharField(max_length=20)
    color_text = models.CharField(max_length=20)
    heading = models.CharField(max_length=20)
    text = models.TextField()
class vacance(models.Model):
    title = models.CharField(max_length=20)
    text = models.TextField()
    image = models.ImageField(upload_to="vacance")
    def __str__(self):
        return f"{self.title}"
    class Meta:
        verbose_name = "Вакансия"
        verbose_name_plural = "Вакансии"  # Установить отображение множественного числа
class MP(models.Model):
    image = models.ImageField(upload_to="MP")
    date = models.DateField()
    title = models.CharField(max_length=20)
    text = models.TextField()
    yandexloc = models.TextField()
    def __str__(self):
        return f"{self.title}"
    class Meta:
        verbose_name = "Мероприятие"
        verbose_name_plural = "Мероприятия"  # Установить отображение множественного числа
class galary(models.Model):
    image = models.ImageField(upload_to="galary")
    date = models.DateField()
    title = models.CharField(max_length=20,null = True,blank = True)
    def __str__(self):
        return f"{self.title}"
    class Meta:
        verbose_name = "Фото"
        verbose_name_plural = "Галерея"  # Установить отображение множественного числа
class store(models.Model):
    title = models.CharField(max_length=20)
    text = models.TextField(null = True,blank=True)
    image = models.ImageField(upload_to="store")
    def __str__(self):
        return f"{self.title}"
    class Meta:
        verbose_name = "Раздел еды"
        verbose_name_plural = "Разделы еды"  # Установить отображение множественного числа
class store_chapter(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField(null = True,blank = True)
    cost = models.IntegerField()
    image = models.ImageField(upload_to="forstore")
    category = models.CharField(max_length=20)
    def __str__(self):
        return f"{self.title}"
    class Meta:
        verbose_name = "Блюдо"
        verbose_name_plural = "Блюда"  # Установить отображение множественного числа
class RegMP(models.Model):
    name = models.CharField(max_length=20)
    sername = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    MP = models.CharField(max_length=30)
    class Meta:
        verbose_name = "Зарегистрирувшийся на мероприятие"
        verbose_name_plural = "Зарегистрирувшиеся на мероприятие"  # Установить отображение множественного числа
class feedback(models.Model):
    name = models.CharField(max_length=20)
    sername = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    text = models.TextField()
    def __str__(self):
        return f"{self.name},{self.sername},{self.email}"
    class Meta:
        verbose_name = "Пожелание"
        verbose_name_plural = "Пожелания"  # Установить отображение множественного числа
class reservation(models.Model):
    date = models.DateTimeField()
    name = models.CharField(max_length=20)
    sername = models.CharField(max_length=20)
    number = models.CharField(max_length=20)
    place = models.CharField(max_length=30)
    class Meta:
        verbose_name = "Забронированный столик"
        verbose_name_plural = "Забронированные столики"  # Установить отображение множественного числа
