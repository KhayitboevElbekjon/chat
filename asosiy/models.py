from django.db import models
from django.contrib.auth.models import User
class Talaba(models.Model):
    login=models.CharField(max_length=30)
    parol=models.CharField(max_length=30)
    user_fk=models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    def __str__(self):
        return f"{self.login} {self.parol}"
class Xabar(models.Model):
    xabar=models.TextField()
    user_fk=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    def __str__(self):
        return f"{self.user_fk} | {self.xabar}"