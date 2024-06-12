from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    id = models.OneToOneField(User, models.DO_NOTHING, db_column='id', primary_key=True)
    appid = models.CharField(db_column='AppID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    devid = models.CharField(db_column='DevID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    certid = models.CharField(db_column='CertID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    runame = models.CharField(db_column='RuName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    locale = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    oauth_token = models.TextField(blank=True, null=True)
    refresh_token = models.TextField(blank=True, null=True)
    authnauth = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'profile'