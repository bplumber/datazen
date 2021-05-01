from django.shortcuts import render
from .models import Register, Backend, Frontend, DataScience

def home(request):
    return render(request, "home.html")

def register(request):
    name = request.POST['name']
    phone = request.POST['phone']
    email = request.POST['email']
    github = request.POST['github']
    first = request.POST['first']
    second = request.POST['second']
    third = request.POST['third']
    b2 = Register(name=name, phone=phone, email=email, github=github, first=first, second=second, third=third)
    b2.save()
    if first=='Frontend':
        fronts = Frontend.objects.all()
        return render(request, 'front.html',{'fronts':fronts})
    elif first=='Backend':
        backs = Backend.objects.all()
        return render(request, 'back.html',{'backs':backs})
    else:
        datas = DataScience.objects.all()
        return render(request, 'data.html',{'datas':datas})

def backend(request):
    backs=Backend.objects.all() 
    responses = []
    answers = []
    finalscore = Backend.objects.all().count()
    for key in request.POST:
        value = request.POST[key]
        responses.append(value)
    responses = responses[1:len(responses)-1]
    for back in backs:
        answer = back.answer
        answers.append(answer)
    score = 0
    for i in range(len(responses)):
        if answers[i]==responses[i]:
            score += 1
    grade = ''
    if score < int(finalscore/2):
        grade='Below Average'
    elif score == int(finalscore/2):
        grade= 'Average'
    elif score > int(finalscore/2) :
        grade= 'Average'
    elif score == int(finalscore):
        grade='Good'
    return render(request, 'score.html', {'finalscore':finalscore,'score':score, 'grade':grade})

def frontend(request):
    fronts=Frontend.objects.all() 
    responses = []
    answers = []
    finalscore = Frontend.objects.all().count()
    for key in request.POST:
        value = request.POST[key]
        responses.append(value)
    responses = responses[1:len(responses)-1]
    for front in fronts:
        answer = front.answer
        answers.append(answer)
    score = 0
    for i in range(len(responses)):
        if answers[i]==responses[i]:
            score += 1
    grade = ''
    if score < int(finalscore/2):
        grade='Below Average'
    elif score == int(finalscore/2):
        grade= 'Average'
    elif score > int(finalscore/2) :
        grade= 'Average'
    elif score == int(finalscore):
        grade='Good'
    return render(request, 'score.html', {'finalscore':finalscore,'score':score, 'grade':grade})

def datascience(request):
    datas=DataScience.objects.all() 
    responses = []
    answers = []
    finalscore = DataScience.objects.all().count()
    for key in request.POST:
        value = request.POST[key]
        responses.append(value)
    responses = responses[1:len(responses)-1]
    for data in datas:
        answer = data.answer
        answers.append(answer)
    score = 0
    for i in range(len(responses)):
        if answers[i]==responses[i]:
            score += 1
    grade = ''
    if score < int(finalscore/2):
        grade='Below Average'
    elif score == int(finalscore/2):
        grade= 'Average'
    elif score > int(finalscore/2) :
        grade= 'Average'
    elif score == int(finalscore):
        grade='Good'
    return render(request, 'score.html', {'finalscore':finalscore,'score':score, 'grade':grade})

def datasciencequiz(request):
    datas = DataScience.objects.all()
    return render(request, "data.html",{'datas':datas})

def frontendquiz(request):
    fronts = Frontend.objects.all()
    return render(request, 'front.html',{'fronts':fronts})

def backendquiz(request):
    backs = Backend.objects.all()
    return render(request, "back.html", {'backs':backs})
    
