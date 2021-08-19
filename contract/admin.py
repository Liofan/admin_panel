import os
import datetime
import sys
import locale

from django.contrib import admin
from django.http import HttpResponse
from django.utils.safestring import mark_safe
from .models import Contract
from django.urls import path

from docxtpl import DocxTemplate
import jinja2
from .num2t4ru import num2text
from django.contrib.staticfiles import finders



if sys.platform == 'win32':
    locale.setlocale(locale.LC_ALL, 'rus_rus')
else:
    locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')

class ContractAdmin(admin.ModelAdmin):
    list_display = ('contract_number', 'fio', 'name_course', 'data_start_course', 'tel', 'activate_button')
    list_display_links = ('contract_number','fio',)
    search_fields = ('contract_number', 'fio')

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('activate-scenario/<int:pk>/', self.button, name="admin_activate_scenario"),
        ]
        return my_urls + urls

    def button(self, request, pk):
        dogovor = Contract.objects.get(id=pk)

        result = finders.find('template.docx')
        doc = DocxTemplate(result)
        price_string = num2text(dogovor.price_course)


        day = dogovor.data_start_course
        d = datetime.datetime.strptime(str(day), '%Y-%m-%d')
        day = d.strftime('%d')  # %I:%M if you want 12 hour format
        month = datetime.date.today().strftime("%B")
        data = d.strftime('%d.%m.%Y')  # %I:%M if you want 12 hour format




        context = {'contract_number': dogovor.contract_number,
                   'day': day,
                   'month': month,
                   'fio': dogovor.fio,
                   'name_course': dogovor.name_course,
                   'data_start_course': data,
                   'time_course': dogovor.time_course,
                   'amount_person': dogovor.amount_person,
                   'price_course': dogovor.price_course,
                   'price_course_string': price_string,
                   'passport': dogovor.passport,
                   'address': dogovor.address,
                   'tel': dogovor.tel,

                   }  # Where the magic happens


        name_file =   'attachment; filename='+ dogovor.contract_number +'.docx'

        doc.render(context)
        doc.save("generated_doc.docx")
        filename = 'generated_doc.docx'
        data = open(filename, "rb").read()
        response = HttpResponse(data, content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
        response['Content-Disposition'] = name_file
        response['Content-Length'] = os.path.getsize(filename)

        return response

admin.site.register(Contract, ContractAdmin)