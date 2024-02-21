from django.db import models
import uuid

class BaseModel(models.Model):
	guid=models.UUIDField(unique=True,default=uuid.uuid4,editable=False)
	createdAt=models.DateTimeField(auto_now_add=True)
	updatedAt=models.DateTimeField(auto_now=True)

	class Meta:
		abstract=True