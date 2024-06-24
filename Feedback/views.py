from django.shortcuts import render, redirect
from .models import Student, Faculty, Feedback
from .forms import FeedbackForm

def index(request):
    return render(request, 'index.html')

def feedback_form(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thank_you')
    else:
        form = FeedbackForm()
    return render(request, 'feedback_form.html', {'form': form})

def thank_you(request):
    return render(request, 'thank_you.html')
