from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import User, WellnessScore
from .utils import generate_wellness_plan, send_sms

import markdown

def index(request):
    return render(request, 'index.html')

def submit_scores(request):
    categories = ['physical', 'intellectual', 'mental', 'social', 'spiritual',
                'occupational', 'emotional', 'financial', 'environmental']
    if request.method == 'POST':
        name = request.POST['name']
        phone_number = request.POST['phone_number']
        scores = {aspect: int(request.POST[aspect]) for aspect in categories}
        
        user, created = User.objects.get_or_create(name=name, phone_number=phone_number)
        WellnessScore.objects.create(user=user, **scores)
        
        return HttpResponseRedirect(reverse("generate_plan", args=(request.POST['phone_number'],)))

    context = {
        'aspects': categories
    }
    return render(request, 'submit_scores.html', context)

def generate_plan(request, phone_number):
    user = User.objects.get(phone_number=phone_number)
    latest_score = WellnessScore.objects.filter(user=user).latest('created_at')

    wellness_plan = generate_wellness_plan(latest_score)
    # send_sms(phone_number, wellness_plan['summary'])

    temp_html = markdown.markdown(wellness_plan['full']) 

    return render(request, 'generate_plan.html', {'wellness_plan': temp_html})
