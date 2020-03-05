from django import forms
from django.core import validators
class Feedbackform(forms.Form):
    name=forms.CharField(max_length=100)
    rollno=forms.IntegerField()
    email=forms.EmailField()
    feedback=forms.CharField(widget=forms.Textarea,validators=[validators.MaxLengthValidator(40),validators.MinLengthValidator(5)])
    def clean_name(self):
        print("validating name")
        inputname=self.cleaned_data['name']
        if len(inputname)<4:
            raise forms.ValidationError("The minimum no of chacters in the name field is shoule be 4 and first character should be c")
        return inputname
    def clean_rollno(self):
        print("validating rollno")
        inputrollno=self.cleaned_data['rollno']
        if inputrollno <1994 :
            raise forms.ValidationError("the rollno should be above 1994")
        return inputrollno
    """def clean_feedback(self):
        print("validating feedback")
        inputfeedback=self.cleaned_data['feedback']
        if len(inputfeedback)<8:
            raise forms.ValidationError("the feedback length must be eight characters")"""