from django.contrib import admin

from .models import Question, Osoba

class OsobaAdmin(admin.ModelAdmin):
    list_display = ('imie', 'nazwisko', 'miesiac_urodzenia', 'data_dodania')

admin.site.register(Question)
admin.site.register(Osoba, OsobaAdmin)
