from django.db import models

class Doctor(models.Model):
    name = models.TextField()
    

class Patient(models.Model):
    name = models.TextField()
    doctors = models.ManyToManyField(Doctor, related_name='patients')#, through='Reservation')
    
# Doctor:Reservation = 1:N -> Reservation = N*Doctor
# Patient:Reservation = 1:M -> Reservation = M*Patient
# N*Doctor = M*Patient -> M:N = Doctor:Patient
# Doctor:Patient = M:N
# class Reservation(models.Model):
#     doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
#     patient = models.ForeignKey(Patient, on_delete=models.CASCADE)