from django.db import models , utils
from django.contrib.auth.models import User



class Anasayfa(models.Model):
    #form1=models.OneToOneField(Form1,on_delete=models.CASCADE)
    #form2=models.OneToOneField(Form2,on_delete=models.CASCADE)
    #form3=models.OneToOneField(Form3,on_delete=models.CASCADE)
    #form4=models.OneToOneField(Form4,on_delete=models.CASCADE)
    #form5=models.OneToOneField(Form5,on_delete=models.CASCADE)
    Olusturan = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.Olusturan
