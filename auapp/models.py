from django.db import models
from django.core.validators import MinLengthValidator


class Question(models.Model):
	ques=models.TextField(validators=[
            MinLengthValidator(2, 'the field must contain at least 2 characters')
            ])
	op1=models.CharField(max_length=300,validators=[
            MinLengthValidator(2, 'the field must contain at least 2 characters')
            ])
	op2=models.CharField(max_length=300,validators=[
            MinLengthValidator(2, 'the field must contain at least 2 characters')
            ])
	op3=models.CharField(max_length=300,validators=[
            MinLengthValidator(2, 'the field must contain at least 2 characters')
            ])
	option_one_count = models.IntegerField(default=0)
	option_two_count = models.IntegerField(default=0)
	option_three_count = models.IntegerField(default=0)
	

	
	def total(self):
		return self.option_one_count + self.option_two_count + self.option_three_count


	
