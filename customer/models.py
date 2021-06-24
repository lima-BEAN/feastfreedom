from django.db import models
from django.contrib.auth.models import User

# Customer Class0
class Customer(User):
# class Customer(models.Model):
    # first_name = models.CharField(max_length=50, null=False)
    # last_name = models.CharField(max_length=50, null=False)
    # email = models.EmailField()
    # password = models.CharField(max_length=10, null=False)
    question_1 = models.CharField(max_length=50, null=False)
    answer_1 = models.CharField(max_length=50, null=False)
    question_2 = models.CharField(max_length=50, null=False)
    answer_2 = models.CharField(max_length=50, null=False)
    is_provider = models.BooleanField(null=False)
