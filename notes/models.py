from django.db import models

# Create your models here.


class Notes(models.Model):

    # Title with a limitation of 200 characters
    title = models.CharField(max_length=200)

    # Note without any character limitation
    text = models.TextField()

    # When it was created?
    created_at = models.DateTimeField(auto_now_add=True)
