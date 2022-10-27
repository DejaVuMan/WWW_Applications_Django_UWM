from django.contrib import admin

from .models import Question, Osoba, Druzyna

class OsobaAdmin(admin.ModelAdmin):
    list_display = ('imie', 'nazwisko', 'miesiac_urodzenia', 'data_dodania', 'druzyna')
    list_filter = ('miesiac_urodzenia', 'druzyna', 'data_dodania')

class DruzynaAdmin(admin.ModelAdmin):
    list_display = ('nazwa', 'kraj')
    list_filter = ['kraj']

admin.site.register(Question)
admin.site.register(Osoba, OsobaAdmin)
admin.site.register(Druzyna, DruzynaAdmin)
