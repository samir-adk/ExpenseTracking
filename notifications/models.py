from django.db import models
from authentication.models import CustomUser
# Create your models here.
class Message(models.Model):
	message=models.CharField(max_length=200)
	created_at=models.DateTimeField()
	important=models.BooleanField(default=True)
	created_user=models.ForeignKey(CustomUser,on_delete=models.CASCADE,null=True,blank=True)

	def __str__(self):
		return self.message