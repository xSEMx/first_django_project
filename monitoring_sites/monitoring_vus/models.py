from django.db import models
from django.contrib.auth.models import User

class Sites(models.Model):
  url = models.URLField(unique=True, verbose_name='URL')
  status = models.BooleanField()
  famous = models.BooleanField(default=False)

  
  def __str__(self):
    return self.url


  class Meta:
    verbose_name = 'Сайт'
    verbose_name_plural = 'Сайты'


class Comments(models.Model):
  evaluation = models.IntegerField(verbose_name='Оценка')
  review = models.CharField(max_length=6000, null=True, verbose_name='Отзыв')
  site = models.ForeignKey(Sites, on_delete=models.CASCADE, verbose_name='Сайт')
  user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name='Пользователь')


  def get_username(self):
    return User.objects.filter(id=self.user_id)[0].username

  
  def __str__(self):
    return f'{self.user.username}: {self.site.url}'

  
  class Meta:
    verbose_name = 'Комментарий'
    verbose_name_plural = 'Комментарии'
    unique_together = ('user', 'site')


class Notifications(models.Model):
  email = models.EmailField()
  site = models.ForeignKey(Sites, on_delete=models.CASCADE, verbose_name='Cайт')


  def __str__(self):
    return f'{self.email} {self.site.url}'

  
  class Meta:
    verbose_name = 'Заявка'
    verbose_name_plural = 'Заявки'


class TelegramLatestMessageIds(models.Model):
  chat_id = models.IntegerField(unique=True, verbose_name='Чат')
  message_id = models.IntegerField(verbose_name='Сообщение')


  def __str__(self):
    return f'{self.chat_id}: {self.message_id}'


  class Meta:
    verbose_name = 'Последнее сообщение'
    verbose_name_plural = 'Последние сообщения'
