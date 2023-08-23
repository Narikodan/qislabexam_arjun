from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    USER_TYPES = (
        ('participant', 'Participant'),
        ('captain', 'House Captain'),
        ('coordinator', 'Event Coordinator'),
    )
    
    user_type = models.CharField(max_length=20, choices=USER_TYPES)

class House(models.Model):
    name = models.CharField(max_length=50)
    event = models.ForeignKey('Event', on_delete=models.CASCADE, related_name='houses')
    captain = models.OneToOneField(CustomUser, on_delete=models.SET_NULL, null=True, blank=True, related_name='captain_of')

class Event(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
class Participant(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    house = models.ForeignKey(House, on_delete=models.CASCADE)

    
    
    class Meta:
        unique_together = ('user', 'event')
