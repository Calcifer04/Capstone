from django.db import models


# MODELS
# Defining post details in Post model
class Post(models.Model):
    title = models.CharField(max_length=140)
    body = models.TextField()
    signature = models.CharField(max_length=140, default="SVS")
    date = models.DateTimeField()

    # Return post title
    def __str__(self):
        return self.title
