from django.db import models

class TimeStampedModel(models.Model):
    """
    An abstract class model that provides self-updating
    ``create_at`` and ``updated_at`` fields.
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
