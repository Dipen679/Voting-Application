from django import forms
from .models import Question

class QuesForm(forms.ModelForm):
	class Meta:
		model=Question
		fields=["ques" , "op1" , "op2" , "op3" ]
	
		widgets = {'ques': forms.Textarea(attrs={'rows':5,
                                            'cols':27,
                                            'style':'resize:none;'}),
    }
	
