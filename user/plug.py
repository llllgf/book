from django.contrib.auth.models import User
from django.shortcuts import render

from books.models import Student, SemesterOrder, Order, FeedBack


def getSemesters(user: User):
    student = Student.objects.get(account=user)
    return SemesterOrder.objects.filter(grade=student.grade)


def getBooks(user: User, semesterName: str):
    student = Student.objects.get(account=user)
    semester = SemesterOrder.objects.get(name=semesterName, grade=student.grade)
    return Order.objects.filter(semester=semester)


def getFeedback(user: User, semesterName: str):
    student = Student.objects.get(account=user)
    semester = SemesterOrder.objects.get(name=semesterName, grade=student.grade)
    return FeedBack.objects.filter(tabel=semester, student=student).order_by('-time')


def newFeedback(user: User, semesterName: str, content: str):
    student = Student.objects.get(account=user)
    semester = SemesterOrder.objects.get(name=semesterName, grade=student.grade)
    FeedBack.objects.create(tabel=semester, student=student, content=content)


def userRender(request, template_name, context=None):
    if context is None:
        context = {}
    context['user'] = request.user
    context['semesters'] = getSemesters(request.user)
    return render(request, template_name, context)
