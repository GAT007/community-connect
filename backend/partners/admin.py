from django.contrib import admin
from .models import Partners
from .forms import PartnersForm


# Register your models here.
class PartnersAdmin(admin.ModelAdmin):
    form = PartnersForm


admin.site.register(Partners, PartnersAdmin)
