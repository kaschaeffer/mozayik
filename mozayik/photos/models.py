from django.db import models

from core.models import TimeStampedModel

class User(TimeStampedModel):
    email = models.EmailField()
    password = models.CharField(max_length=255)

    # FilePathField seems useful
    # PositiveIntegerField also seems useful
    # how does ImageField work?
    # autoincrementing ids?

class Photo(models.Model):
    # TODO do I need an id?
    user_id = models.IntegerField() #TODO this should be a foreign key
    path = models.DateTimeField(max_length=200)

class PhotoDivision(models.Model):
    pass

class PhotoPiece(models.Model):
    x_position = models.IntegerField() # should be within range of photo division
    y_position = models.IntegerField()
    path = models.DateTimeField(max_length=200)

# TODO better name?
class PhotoMatch(models.Model):
    original_photo_piece_id = models.IntegerField()
    path = models.DateTimeField(max_length=200)
    match_score = models.IntegerField() # this should be between 0 and 100, TODO enforce

