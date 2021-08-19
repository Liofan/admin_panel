from django.db import models
from django.utils.html import format_html
from django.urls import reverse_lazy



class Contract(models.Model):
    contract_number = models.CharField('Номер Договора', max_length=100)
    day = models.DateField(verbose_name='Дата Договора',auto_now_add=True,null=False)
    fio = models.CharField('Ф.И.О', max_length=100)
    name_course = models.CharField('Название курса', max_length=100)
    data_start_course = models.DateField(verbose_name='Дата начала курса', auto_now_add=False, null=False)
    time_course = models.IntegerField('Продолжительность курса', max_length=100)
    amount_person = models.IntegerField('Количество людей', max_length=100)
    price_course = models.IntegerField('Цена', max_length=100)

    passport = models.CharField('Номер Паспорта', max_length=100)
    address = models.CharField('Адрес', max_length=100)
    tel = models.CharField('Номер Телефона', max_length=100)
    created_at = models.DateTimeField(verbose_name='Дата создания',auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.contract_number

    def activate_button(self):
        return format_html('<a href="{}" download class="link">Скачать Договор</a>',
                           reverse_lazy("admin:admin_activate_scenario", args=[self.pk])
                           )

    class Meta:
        verbose_name = 'Договор' # в одном числе
        verbose_name_plural = 'Договора'  # в многочисл
        ordering = ['-created_at']
