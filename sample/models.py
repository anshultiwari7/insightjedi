from django.db import models

# Create your models here.
from django.contrib.postgres.fields import JSONField
from django.contrib.auth import get_user_model

User = get_user_model()

class Document(models.Model):
	"""
	Model created with following assumptions -
	1. 3 source choices as mentioned below.
	2. Source ID can be any string.
	3. input_meta_data can store any key value pairs in dictionary.
	"""

	SOURCE_CHOICE_1 = 1
	SOURCE_CHOICE_2 = 2
	SOURCE_CHOICE_3 = 3

	SOURCE_CHOICES = (
			(SOURCE_CHOICE_1, 'source-choice-1'),
			(SOURCE_CHOICE_2, 'source-choice-2'),
			(SOURCE_CHOICE_3, 'source-choice-3')
		)

	owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='exports')
	created_time = models.DateTimeField(auto_now_add=True)
	type = models.CharField(max_length=100)
	source_type = models.CharField(
		choices=SOURCE_CHOICES, blank=True, null=True, max_length=20)
	source_id = models.CharField(blank=True, null=True, max_length=50)
	input_meta_data = JSONField(default=dict, null=True, blank=True)
