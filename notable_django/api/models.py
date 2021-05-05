from django.db import models

# Create your models here.


class Note(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    # auto_now_add : sets the value of the field to current datetime when the object is created.
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s : %s' % (self.title, self.body)
