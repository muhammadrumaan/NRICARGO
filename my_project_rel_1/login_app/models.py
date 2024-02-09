from django.contrib.auth.models import AbstractUser
from django.db import models

class UserTable(AbstractUser):
    # You can add custom fields or methods here if needed

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'UserTable'



# from django.contrib.auth.models import AbstractUser
# from django.db import models
#
# class UserTable(AbstractUser):
#     username = models.CharField(max_length=30, unique=True)
#     password = models.CharField(max_length=120)
#
#     def __str__(self):
#         return self.username
#
#     class Meta:
#         db_table = 'UserTable'


# class UserTable(models.Model):
#     username = models.CharField(max_length=30, unique=True)
#     password = models.CharField(max_length=120)
#
#     def __str__(self):
#         return self.username
#
#     class Meta:
#         db_table = 'UserTable'


