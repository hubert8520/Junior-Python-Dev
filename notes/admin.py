from django.contrib import admin
from .models import Notes

# Register your models here.
"""Tworzysz klase o nazwie NotesAdmin oraz wskazujesz jej wlasciwosci, ktorymi mozesz zarzadzac, 
np. to co ma byc wyswietlane w widoku admina (za pomoca funkcji list_display). Wszystkie te funkcje dostepne 
sa po kliknieciu CTRL + 'click'ModelAdmin"""

@admin.register(Notes)
class NotesAdmin(admin.ModelAdmin):
    list_display = ("title",)


"""To co robisz ponizej to:
- na stronie admin (admin.site) rejestrujesz swoj model (models.Notes) i wskazujesz klase tego modelu (NotesAdmin);
- wskazujesz, ze ten model powinien byc wyswietlany w panelu admina"""
#admin.site.register(models.Notes, NotesAdmin)

"""Powyzsza komende wykonalem z uzyciem dekoratora - skorzystalem z modulu admin, funkcji register, przesyłam model Notes,
aby zarejestrowac widok modelu Notes w panelu admin"""
