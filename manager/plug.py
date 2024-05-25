from django.shortcuts import render

from books.models import FeedBack, Order


def getBooks(semesterOrder):
    return Order.objects.filter(semester=semesterOrder)


def getFeedbackOrder(feedback_id):
    semesterOrder = FeedBack.objects.get(id=feedback_id).tabel
    return getBooks(semesterOrder)


def getFeedbackList():
    feedbacks = FeedBack.objects.all().order_by('msg', 'time')
    return feedbacks


def getFeedbackById(id):
    return FeedBack.objects.get(id=id)


def managerRender(request, template_name, context=None):
    if context is None:
        context = {}
    context['user'] = request.user
    return render(request, template_name, context)
