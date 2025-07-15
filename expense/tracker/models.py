from django.db import models
import uuid

class BaseModel(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        abstract = True
    


class Transaction(BaseModel):
    description = models.CharField(max_length=100)
    amount = models.FloatField()
    class Meta:
        ordering = ('description',)
    def isNegative(self):
        return self.amount < 0
    
