from django.shortcuts import render
from .models import Contract



def word_file(request, id):
    dogovor = Contract.objects.filter(slug=id)
    print(dogovor)
    doc = DocxTemplate("template.docx")

    price = 9878
    price_string = num2text(price)

    context = {'contract_number': 777,
               'day': 13,
               'month': 'Август',
               'fio': 'Иванов Иван Иваныч',
               'name_course': 'Бариста',
               'data_start_course': '13.08.2021',
               'time_course': 40,
               'amount_person': 1,
               'price_course': price,
               'price_course_string': price_string,
               'passport': 123123123,
               'address': 'Сулейменого 18',
               'tel': '87771234455',

               }  # Where the magic happens

    doc.render(context)
    return doc.save("generated_doc.docx")