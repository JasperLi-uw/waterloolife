from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ThreadType(models.Model):
	type_name = models.CharField(max_length=15)

	def __str__(self):
		return self.type_name

class Thread(models.Model):
	title = models.CharField(max_length=50)
	thread_type = models.ForeignKey(ThreadType, on_delete=models.CASCADE)
	content = models.TextField()
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	created_time = models.DateTimeField(auto_now_add=True)
	last_update_time = models.DateTimeField(auto_now=True)

	def __str__(self):
		return "<Thread: %s>" % self.title

	class Meta:
		ordering = ['-created_time']
