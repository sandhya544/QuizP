from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Question, Result, Profile
import random
import string

def home(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            print(request.user)
            return redirect('profile')
        else:
            messages.info(request, 'Username or password is incorrect')
            return render(request, 'home.html')

    return render(request, 'home.html')


topic = "General"


def generate_random_question_id(topic):
    random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=5))
    first_3_letters = topic[:3]
    question_id = f'{first_3_letters}{random_string}'
    return question_id


@login_required(login_url='home')
def profile(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            question = request.POST['question']
            option1 = request.POST['option1']
            option2 = request.POST['option2']
            option3 = request.POST['option3']
            option4 = request.POST['option4']
            answer = request.POST['cAnswer']
            toughness = request.POST['toughness']
            topic = request.POST['topic']
            qid = generate_random_question_id(topic)
            while Question.objects.filter(qid=qid).exists():
                qid = generate_random_question_id(topic)
            print(question, option1, option2, option3, option4, answer, toughness, topic)
            q = Question(qid=qid,question=question, option1=option1, option2=option2, option3=option3, option4=option4,
                         answer=answer, toughness=toughness, topic=topic)
            q.save()
            messages.info(request, 'Question added successfully')
            return render(request, 'admin.html')

        return render(request, 'admin.html')
    else:
        profile_info = Profile.objects.filter(mail=request.user.email)
        context = {'profile_info': profile_info}

        if request.method == 'POST':
            if "taketest" in request.POST:
                topic = request.POST['topic']
                toughness = Profile.objects.get(mail=request.user.email).exp_level
                questions = Question.objects.filter(topic=topic, toughness__lte=toughness)
                return redirect('test', topic=topic)
            elif "update" in request.POST:
                aim = request.POST['aim']
                p = Profile.objects.get(mail=request.user.email)
                p.aim = aim
                p.save()
                messages.info(request, 'Profile updated successfully')
                return redirect('profile')
        return render(request, 'profile.html', context)


def logoutUser(request):
    logout(request)
    messages.info(request, 'Logged out successfully')
    return redirect('home')


def test(request, topic):
    toughness = Profile.objects.get(mail=request.user.email).exp_level
    counter = list(range(1, 11))
    questions = random.sample(list(Question.objects.filter(topic=topic,toughness__lte=toughness)), 10)
    if request.method == 'POST':
        score = 0
        total = 10
        for i in range(1, 11):
            qid = request.POST["q"+str(i)]
            answer = request.POST["a"+str(i)]
            print(qid, answer)
            if Question.objects.get(qid=qid).answer == answer:
                score += 1
        print(score)
        r = Result(email=request.user.email, topic=topic, score=score, total=total, percentage=(score / total) * 100,
                   name=request.user.username, exp_at_test=toughness)
        r.save()
        p = Profile.objects.get(mail=request.user.email)
        p.exp_level += score / total
        p.save()
        messages.info(request, f'You scored {score} out of {total}')
        return render(request, 'result.html', {'score': score, 'total': total,'percent':(score/total)*100})
    question_count_pairs = zip(questions, counter)
    return render(request, 'test.html', {'question_count_pairs': question_count_pairs, 'topic': topic})
