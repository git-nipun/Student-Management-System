from django.db import models
# Create your models here.
class studentdetail(models.Model):
    roll_number=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=25)
    mobile=models.IntegerField()
    mail=models.EmailField()
    course=models.CharField(max_length=30)
    sem=models.IntegerField()
    dob=models.DateField()
    #photo=models.ImageField()

    def __str__(self):
        return str(self.roll_number)+"  "+self.name


class facultydetail(models.Model):
    f_name=models.CharField(max_length=30)
    f_department=models.CharField(max_length=30)
    f_mobile=models.IntegerField()

    def __str__(self):
        return str(self.f_name)








        