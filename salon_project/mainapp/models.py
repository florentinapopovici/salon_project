from django.db import models
from django.contrib.auth.models import User

class Services(models.Model):
    """
    Model care definește serviciile oferite de salon.
    Include numele serviciului, durata și prețul.
    """
    services = models.CharField(max_length=225)
    duration = models.TextField()
    price = models.IntegerField()

    class Meta:
        db_table ="services"
        ordering = ['services']

    def __str__(self):
        return self.services
    

class Appointment(models.Model):
    """
    Model pentru programările clienților.
    Leagă utilizatorul de serviciul ales și stochează data, ora și statusul.
    """
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    service = models.ForeignKey('Services' , on_delete=models.CASCADE)
    date = models.DateField()
    hour = models.TimeField()

    class Meta:
        db_table ="appointment"

    def __str__(self):
        return f"{self.service.services} - {self.user.username}"
    
    status_choices = [
        ('pending' , 'Pending'),
        ('confirmed' , 'Confirmed'),
        ('cancelled' , 'Cancelled'),
    ]

    status = models.CharField(max_length=20 , choices=status_choices , default='pending')

class Review(models.Model):
    """
    Model pentru recenziile serviciilor.
    Fiecare recenzie aparține unui utilizator și unui serviciu.
    """
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    service = models.ForeignKey(Services , on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table ="review"

    def __str__(self):
        return f"{self.service.services} ({self.rating})"