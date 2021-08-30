from django.db import models

# Create your models here.

class Interface(models.Model):
    if_id = models.AutoField(primary_key=True, null=False)
    if_name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    request_body_param = models.TextField()
    response_body_param = models.TextField()

    def __str__(self):
        return self.if_name

