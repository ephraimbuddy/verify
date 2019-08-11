from django.db import models
from django.conf import settings

class TimestampedModel(models.Model):
    # A timestamp representing when this object was created.
    created_at = models.DateTimeField(auto_now_add=True)

    # A timestamp reprensenting when this object was last updated.
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

        ordering = ['-created_at', '-updated_at']


class PhoneNumber(TimestampedModel):
    
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )
    number = models.CharField(max_length=17, blank=True) 
    verified = models.BooleanField(default=False)
    
    def __str__(self):
        return self.user.email


