from django.db import models

# Create your models here.


class GoValidator(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(postData['ht_lat']) == 0:
            errors["mylat"] = "Latitude needs to be +90 to -90"
        if len(postData['ht_long']) == 0:
            errors["mylon"] = "Longitude needs to be -180 to +180"
        if int(postData['ht_lat']) < -90 or int(postData['ht_lat']) > 90:
            errors["mylat"] = "Latitude needs to be +90 to -90"
        if int(postData['ht_long']) < -180 or int(postData['ht_long']) > 180 :
            errors["mylon"] = "Longitude needs to be -180 to +180"
        return errors

class Go(models.Model):
    mylat = models.TextField(max_length=255)
    mylong = models.TextField(max_length=255)
    objects = GoValidator()