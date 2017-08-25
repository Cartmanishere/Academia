from django.shortcuts import render
from .models import Subject, Practical
from django.http import HttpResponse
from django.template import loader
from django.http import Http404

def index(request):
    subjects = Subject.objects.all()
    return render(request, "Practicals/subjects.html", { 'subjects': subjects })

def practicals(request, subject_name):
    try:
        practicals = Practical.objects.filter(subject=Subject.objects.get(subject_name=subject_name))
    except Exception as e:
        practicals = []

    list = []
    for i in practicals:
        list.append({ 'name': i.name, 'id': i.id })
    print(list)
    return render(request, "Practicals/practicals.html", { 'practicals': list, 'subject_name': subject_name })

def details(request, subject_name, practical_id):
    try:
        practical = Practical.objects.get(id=practical_id)
        objectives = practical.objectives.split("\n")
        return render(request, "Practicals/details.html",
                      {'objectives': objectives, 'practical': practical, 'subject_name': subject_name})
    except Exception as e:
        raise Http404("This practical does not exist.")


