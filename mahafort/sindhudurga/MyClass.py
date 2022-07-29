from django.db import models
 
class MyClass(models.Model):
    class Meta:
        db_table = 'my_class'
        
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    roll_number = models.IntegerField()
    password = models.CharField(max_length=50)

