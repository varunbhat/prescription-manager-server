from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class Prescription(models.Model):
    # user for whom the med is priscribed
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # medicine that needs to be prescribed
    drug = models.ForeignKey("PrescriptionMedicine", on_delete=models.CASCADE)

    # Schedule array at which the medicine that needs to be taken
    schedules = models.ManyToManyField("PillSchedule")

    prescription_date = models.DateField()
    def __str__(self):
        return str(self.drug)


class PrescriptionMedicine(models.Model):
    # Medicine Name
    drug_name = models.CharField(max_length=100, unique=True)
    composition = models.ManyToManyField("Composition", default=None, blank=True)

    def __str__(self):
        return self.drug_name


class Composition(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class DrugInteraction(models.Model):
    composition_array = models.ManyToManyField("Composition")
    severity = models.CharField(max_length=50, choices=(("LO", "Low"), ("HI", "High"), ("MI", "Medium")))


class PillSchedule(models.Model):
    ch=(("AF", "After Food"), ("AT", "Anytime"), ('ES', "Empty Stomach"))

    # Tablet that needs to be taken
    medicine_count = models.IntegerField()

    # timestamp at which the medicine has to be taken
    timestamp = models.TimeField()

    # After food or other conditions as choices
    condition = models.CharField(max_length=50, choices=ch)

    def __str__(self):
        return "%d pills at %s %s" % (int(self.medicine_count), str(self.timestamp), dict(self.ch)[self.condition])


class Despensor(models.Model):
    patient = models.ForeignKey(User, on_delete=models.CASCADE)

    # unique id of the despensor
    despensor_uid = models.IntegerField()
    medicine_prescription_validation = models.ManyToManyField("PrescriptionMedicine")


class DrugDispensorList(models.Model):
    despensor = models.ForeignKey("Despensor", on_delete=models.CASCADE)
    drug = models.ForeignKey("PrescriptionMedicine", on_delete=models.CASCADE)
    drug_count = models.IntegerField()


class DespenseLog(models.Model):
    despensor = models.ForeignKey("Despensor", on_delete=models.CASCADE)
    timestamp = models.DateTimeField()
    count = models.IntegerField()
