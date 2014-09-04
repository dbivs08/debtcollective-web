from django.db import models
from django.contrib import admin

class UserData(models.Model):
  user_id_secret = models.CharField(max_length=200)
  created_at = models.DateTimeField()
  location = models.CharField(max_length=200)

  @staticmethod
  def user_id_secret(user_id):
    """TODO: encrypt the given user id
    to create the user_id_secret"""
    pass

class Debt(models.Model):
  AUTO = 1
  HOME = 2
  STUDENT = 3
  CREDIT = 4
  DEBT_CHOICES = (
    (AUTO, 'Auto'),
    (HOME, 'Home'),
    (STUDENT, 'Student'),
    (CREDIT, 'Credit')
  )

  userdata = models.ForeignKey(UserData)
  amount = models.IntegerField()
  kind = models.IntegerField(max_length=1, choices=DEBT_CHOICES)
  last_payment = models.DateTimeField()
