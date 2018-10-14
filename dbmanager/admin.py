from django.contrib import admin
from django.contrib.admin import AdminSite
from django.utils.translation import ugettext_lazy

# Register your models here.
from dbmanager.models import Prescription, PrescriptionMedicine, Composition, DrugInteraction, PillSchedule, \
    Despensor, DespenseLog

admin.site.register(Prescription)
admin.site.register(PrescriptionMedicine)
# admin.site.register(Composition)
# admin.site.register(DrugInteraction)
# admin.site.register(PillSchedule)
admin.site.register(Despensor)
admin.site.register(DespenseLog)


admin.site.site_header = "Priscription Management"
admin.site.site_title = "DocPill"
admin.site.index_title = "Manage Patient Priscription"