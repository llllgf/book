from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect

from books.models import Student
from user.plug import getSemesters, userRender, getBooks, getFeedback, newFeedback


# Create your views here.

@login_required(login_url='/login')
def home(request):
    print(request.user)
    student = Student.objects.get(account=request.user)
    return userRender(request, 'user_index.html',{"student":student})



@login_required(login_url='/login')
@csrf_protect
def bookTable(request):
    semester = request.GET.get('semester', None)
    if semester is None:
        return redirect('user_index')
    if request.method == 'POST':
        content = request.POST.get('content', None)
        if content is not None:
            newFeedback(request.user, semester, content)
            return redirect(f"/user/book_table?semester={semester}")
    books = getBooks(request.user, semester)
    price = f"{sum([book.book.price for book in books])/100}元"
    feedback = getFeedback(request.user, semester)
    return userRender(request, 'book_table.html', {'books': books,
                                                   'price': price,
                                                   'feedback': feedback,
                                                   'semester': semester})
