from django.db import models

# Create your models here.


class BasicInfo(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=200)
    roll_no = models.IntegerField(default=0)

    def __str__(self):
        return self.first_name

class Marks(models.Model):
    name = models.ForeignKey(BasicInfo, on_delete='do_nothing')
    address = models.CharField(max_length=500, default='')
    english_marks = models.IntegerField(default=0)
    math_marks = models.IntegerField(default=0)
    science_marks = models.IntegerField(default=0)

    def __str__(self):
        return str(self.name)
