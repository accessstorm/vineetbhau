from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User



# Create your models here.




class Post(models.Model):
    Subject = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    Marks = models.CharField(max_length=50, default="N/A")
    post_date = models.DateTimeField(auto_now_add=True)
    Semester = models.CharField(max_length=255, default="Semester-1")

    def __str__(self):
        return self.Subject + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse("vineet")