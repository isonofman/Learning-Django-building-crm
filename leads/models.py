from django.db import models

# Create your models here.
class Agent(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)

class Lead(models.Model):


    SOURCE_CHOICES = (
        ('Youtube', 'Youtube'),
        ('Google', 'Google'),
        ('Newsletter', 'Newsletter'),
    )
    first_name =models.CharField(max_length=20)
    last_name =models.CharField(max_length=20)
    age =models.IntegerField(default=12)

    phoned = models.BooleanField(default=False)
    source = models.CharField(choices=SOURCE_CHOICES, max_length=100)


    profile_picture = models.ImageField(blank=True, nul=True)
    special_files = models.FileField(blank=True, null= True)
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)



