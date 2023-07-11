from django.db import models

# Create your models here.
class Message(models.Model):
	message=models.CharField(max_length=200)
	created_at=models.DateTimeField()
	important=models.BooleanField(default=True)

	def __str__(self):
		return self.message