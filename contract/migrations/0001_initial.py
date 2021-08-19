# Generated by Django 3.2.6 on 2021-08-18 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contract_number', models.CharField(max_length=100, verbose_name='Номер Договора')),
                ('day', models.DateField(auto_now_add=True, verbose_name='Дата Договора')),
                ('fio', models.CharField(max_length=100, verbose_name='Ф.И.О')),
                ('name_course', models.CharField(max_length=100, verbose_name='Название курса')),
                ('data_start_course', models.DateField(verbose_name='Дата начала курса')),
                ('time_course', models.IntegerField(max_length=100, verbose_name='Продолжительность курса')),
                ('amount_person', models.IntegerField(max_length=100, verbose_name='Количество людей')),
                ('price_course', models.IntegerField(max_length=100, verbose_name='Цена')),
                ('price_course_string', models.IntegerField(max_length=100, null=True, verbose_name='Цена пропьсью')),
                ('passport', models.CharField(max_length=100, verbose_name='Номер Паспорта')),
                ('address', models.CharField(max_length=100, verbose_name='Адрес')),
                ('tel', models.CharField(max_length=100, verbose_name='Номер Телефона')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Договор',
                'verbose_name_plural': 'Договора',
                'ordering': ['-created_at'],
            },
        ),
    ]
