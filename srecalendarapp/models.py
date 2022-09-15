from django.db import models

# Create your models here.

class sre(models.Model):
    sre_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    ggs_level = models.IntegerField()
    username = models.CharField(max_length=30)

    def __str__(self):
        return self.first_name + " " + self.last_name





class offset(models.Model):
    offset_id = models.IntegerField(primary_key=True)
    offset_start = models.DateTimeField(blank=True, null=True)
    offset_end = models.DateTimeField(blank=True, null=True)
    offset_total = models.FloatField(blank=True, null=True)
    offset_used = models.FloatField(blank=True, null=True,default=0)
    offset_expiring = models.FloatField(blank=True, null=True)
    offset_bal = models.FloatField(blank=True, null=True)
    sre = models.ForeignKey(sre,on_delete=models.CASCADE,blank=True,null=True)

    
class list_type(models.Model):
        type_id= models.IntegerField(primary_key=True)
        name = models.CharField(max_length=30)

        def __str__(self):
             return self.name

class calendar_list(models.Model):
    calendar_id = models.AutoField(primary_key=True)
    type = models.ForeignKey(list_type, on_delete=models.CASCADE , null=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    description = models.CharField(max_length=200)
    sre = models.ForeignKey(sre, on_delete=models.CASCADE ,null=True)


