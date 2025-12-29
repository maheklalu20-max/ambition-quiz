from django.shortcuts import render,get_object_or_404
from django.contrib.auth.decorators import login_required
# Create your views here.
from .models import Quiz, Question, Result
from django.db import models
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from django.contrib.auth.models import User
from django.contrib import messages


def home(request):
    return render(request, 'quiz/home.html')


def quiz_list(request):
    quizzes = Quiz.objects.all()
    return render(request, 'quiz/quiz_list.html', {'quizzes': quizzes})

@login_required
def quiz_detail(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    questions = Question.objects.filter(quiz=quiz)
    total_questions = questions.count()

    if request.method == "POST":
        score = 0

        for question in questions:
            selected_answer = request.POST.get(f"question_{question.id}")
            if selected_answer == question.correct_option:
                score += 1

        percentage = (score / total_questions) * 100

        # Save result
        Result.objects.create(
            user=request.user,
            quiz=quiz,
            score=score
        )

        # Pass condition
        passed = percentage >= 50

        return render(request, 'quiz/result.html', {
            'quiz': quiz,
            'score': score,
            'total': total_questions,
            'percentage': percentage,
            'passed': passed
        })

    return render(request, 'quiz/quiz_detail.html', {
        'quiz': quiz,
        'questions': questions
    })
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('quiz_list')

    return render(request, 'quiz/login.html')
def signup_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        if password1 != password2:
            messages.error(request, "Passwords do not match")
            return redirect("signup")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect("signup")

        User.objects.create_user(
            username=username,
            password=password1
        )

        messages.success(request, "Account created successfully. Please login.")
        return redirect("login")

    return render(request, "quiz/signup.html")

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def dashboard(request):
    results = Result.objects.filter(user=request.user).order_by('-id')

    total_quizzes = results.count()

    return render(request, 'quiz/dashboard.html', {
        'results': results,
        'total_quizzes': total_quizzes
    })
@login_required
def leaderboard(request):
    leaderboard = (
        Result.objects
        .values('user__username')
        .annotate(total_score=models.Sum('score'))
        .order_by('-total_score')
    )

    return render(request, 'quiz/leaderboard.html', {
        'leaderboard': leaderboard
    })
@login_required
def generate_certificate(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    result = Result.objects.filter(user=request.user, quiz=quiz).last()

    if not result:
        return HttpResponse("No result found")

    total_questions = Question.objects.filter(quiz=quiz).count()
    percentage = (result.score / total_questions) * 100

    if percentage < 50:
        return HttpResponse("You did not pass the quiz")

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="certificate.pdf"'

    pdf = canvas.Canvas(response, pagesize=A4)
    width, height = A4

    pdf.setFont("Helvetica-Bold", 24)
    pdf.drawCentredString(width / 2, height - 100, "Certificate of Completion")

    pdf.setFont("Helvetica", 16)
    pdf.drawCentredString(
        width / 2, height - 180,
        f"This certifies that {request.user.username}"
    )

    pdf.drawCentredString(
        width / 2, height - 220,
        "has successfully passed the quiz"
    )

    pdf.setFont("Helvetica-Bold", 18)
    pdf.drawCentredString(width / 2, height - 260, quiz.title)

    pdf.setFont("Helvetica", 14)
    pdf.drawCentredString(
        width / 2, height - 320,
        f"Score: {result.score} / {total_questions}"
    )

    pdf.drawCentredString(width / 2, height - 360, "Congratulations!")

    pdf.showPage()
    pdf.save()

    return response