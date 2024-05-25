from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.utils import timezone
from django.views.decorators.csrf import csrf_protect

from manager.plug import getFeedbackList, managerRender, getFeedbackOrder, getFeedbackById
from util.check_staff import check_staff


# Create your views here.


@login_required(login_url='/login')
@check_staff
def home(request):
    return managerRender(request, 'manager_index.html')


@login_required(login_url='/login')
@check_staff
def add_book(request):
    return managerRender(request, 'add_book.html')


@login_required(login_url='/login')
@check_staff
def feedback(request):
    feedbacks = getFeedbackList()
    return managerRender(request, 'feedback.html', {"feedbacks": feedbacks})


@login_required(login_url='/login')
@check_staff
@csrf_protect
def reply(request):
    if request.method == "POST":
        msg = request.POST.get('msg')
        feedback_id = request.GET.get('id')
        feedback = getFeedbackById(feedback_id)
        feedback.msg = msg
        feedback.msg_account = request.user
        feedback.msg_time = timezone.now()
        feedback.save()
        return redirect(f"/manager/reply?id={feedback_id}")
    books = getFeedbackOrder(request.GET.get('id'))
    price = f"{sum([book.book.price for book in books]) / 100}元"
    return managerRender(request,
                         'reply.html',
                         {
                             'books': books,
                             'price': price,
                             'feedback': getFeedbackById(request.GET.get('id'))
                         }
                         )
