from django.db import models


# MODELS
# Defining post details in Post model
class Post(models.Model):
    """Class model for blog post with title, body, signature and date.
    :param models.Model: Inheritance of the django class model.
    """
    title = models.CharField(max_length=140)
    body = models.TextField()
    signature = models.CharField(max_length=140, default="SVS")
    date = models.DateTimeField()

    # Return post title
    def __str__(self):
        """
        :return: post title
        :rtype: Str
        """
        return self.title
