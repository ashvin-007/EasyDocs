from django.db import models
# from django.contrib.auth.models import User

# Create your models here.

class DocUpload(models.Model):
    title=models.CharField(max_length=200)
    # user=models.ForeignKey(User,on_delete=models.CASCADE)
    doc=models.FileField(upload_to='doc/')
    description=models.TextField()
    
    
