from django.db import models

class Tafzily(models.Model):
    tafzilycode = models.DecimalField(db_column='TafzilyCode', max_digits=6, decimal_places=0, primary_key=True)
    moencode = models.CharField(db_column='MoenCode', max_length=255, blank=True, null=True)
    allcode = models.CharField(db_column='AllCode', max_length=255, blank=True, null=True)
    tafzilysharh = models.CharField(db_column='TafzilySharh', max_length=255, blank=True, null=True)
    tafzilyadd = models.CharField(db_column='TafzilyAdd', max_length=255, blank=True, null=True)
    bad = models.BooleanField(db_column='Bad', blank=True, null=True)
    change = models.BooleanField(db_column='Change', blank=True, null=True)
    mandeh = models.CharField(db_column='Mandeh', max_length=255, blank=True, null=True)
    moenname = models.CharField(db_column='MoenName', max_length=255, blank=True, null=True)
    tel = models.CharField(db_column='Tel', max_length=255, blank=True, null=True)
    atbar = models.DecimalField(db_column='Atbar', max_digits=19, decimal_places=4, blank=True, null=True)
    city = models.CharField(db_column='City', max_length=255, blank=True, null=True)
    fname = models.CharField(db_column='Fname', max_length=255, blank=True, null=True)
    lastname = models.CharField(max_length=255, blank=True, null=True)
    daftar = models.CharField(max_length=10, blank=True, null=True)
    moarref = models.CharField(max_length=255, blank=True, null=True)
    sms = models.CharField(db_column='SMS', max_length=50, blank=True, null=True)
    ozv = models.DecimalField(db_column='Ozv', max_digits=18, decimal_places=0, blank=True, null=True)
    atabarok = models.BooleanField(blank=True, null=True)
    ashxas = models.CharField(db_column='Ashxas', max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Tafzily'
        
