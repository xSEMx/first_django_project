# Generated by Django 4.1.5 on 2023-03-22 22:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Sites',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(unique=True, verbose_name='URL')),
                ('status', models.BooleanField()),
                ('famous', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Сайт',
                'verbose_name_plural': 'Сайты',
            },
        ),
        migrations.CreateModel(
            name='TelegramLatestMessageIds',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chat_id', models.IntegerField(unique=True, verbose_name='Чат')),
                ('message_id', models.IntegerField(verbose_name='Сообщение')),
            ],
            options={
                'verbose_name': 'Последнее сообщение',
                'verbose_name_plural': 'Последние сообщения',
            },
        ),
        migrations.CreateModel(
            name='Notifications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monitoring_vus.sites', verbose_name='Cайт')),
            ],
            options={
                'verbose_name': 'Заявка',
                'verbose_name_plural': 'Заявки',
            },
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('evaluation', models.IntegerField(verbose_name='Оценка')),
                ('review', models.CharField(max_length=6000, null=True, verbose_name='Отзыв')),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monitoring_vus.sites', verbose_name='Сайт')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарии',
                'unique_together': {('user', 'site')},
            },
        ),
    ]