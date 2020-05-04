from django.db import models
from django.contrib.auth.models import User

'''this is for the extra field that will appear in regsiter field.
Default User model is imported.So no need to define the model of it'''

class Extra(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    extra_field = models.CharField(max_length=500)

    def __str__(self):
     return f'{self.user.username} profile'

