from django.shortcuts import render
from .forms import Feedbackform
# Create your views here.
def feedbackview(request):
    form=Feedbackform()
    if request.method=="POST":
        form=Feedbackform(request.POST)
        if form.is_valid():
            print('Form validating success and printing information')
            print("Name:",form.cleaned_data['name'])
            print("rollno:",form.cleaned_data['rollno'])
            print("email:",form.cleaned_data['email'])
            print("feedback:",form.cleaned_data['feedback'])
    return render(request,'feedbackform.html',{'form':form})
