from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import redirect
from django.utils import timezone
from django.views.decorators.csrf import csrf_protect

from books.models import Grade, Student, Major, Books
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


@login_required(login_url='/login')
@check_staff
@csrf_protect
def grade_all(request, page):
    grades = Grade.objects.all()
    for i in range(len(grades)):
        grades[i].nums = len(Student.objects.filter(grade=grades[i]))

    paginator = Paginator(grades, 10)
    l = page - 1 if page - 1 > 0 else 1
    r = page + 1 if page + 1 <= paginator.num_pages else paginator.num_pages
    return managerRender(request, 'grade_all.html', {"grades": paginator.get_page(page),
                                                     'l': l,
                                                     'r': r})


@login_required(login_url='/login')
@check_staff
@csrf_protect
def grade_about(request, id):
    students = Student.objects.filter(grade_id=id)
    return managerRender(request, 'grade_about.html', {'students': students})


@login_required(login_url='/login')
@check_staff
@csrf_protect
def students_all(request, page):
    try:
        search_type = request.GET.get('search_type')
        search = request.GET.get('search')
        if search_type == 'name':
            students = Student.objects.filter(name__contains=search)
        elif search_type == 'id':
            students = Student.objects.filter(student_id__contains=search)
        else:
            students = Student.objects.all()
        if search == '':
            students = Student.objects.all()
    except:
        students = Student.objects.all()
    paginator = Paginator(students, 10)
    l = page - 1 if page - 1 > 0 else 1
    r = page + 1 if page + 1 <= paginator.num_pages else paginator.num_pages
    return managerRender(request, 'students_all.html', {'students': paginator.get_page(page),
                                                        'l': l,
                                                        'r': r})


@login_required(login_url='/login')
@check_staff
@csrf_protect
def add_student(request):
    if request.method == 'POST':
        student = Student()
        student.name = request.POST.get('name')
        student.student_id = request.POST.get('student_id')
        student.grade_id = request.POST.get('grade')
        student.notice = request.POST.get('notice')
        student.save()
        return redirect('/manager/students_all/1')
    grade_list = Grade.objects.all()
    return managerRender(request, 'add_student.html', {'grade_list': grade_list})


@login_required(login_url='/login')
@check_staff
@csrf_protect
def add_grade(request):
    if request.method == 'POST':
        grade = Grade()
        grade.name = request.POST.get('name')
        grade.major_id = request.POST.get('major')
        grade.save()
        return redirect('/manager/grade_all/1')
    major_list = Major.objects.all()
    return managerRender(request, 'add_grade.html', {'major_list': major_list})


@login_required(login_url='/login')
@check_staff
@csrf_protect
def edit_student(request, id):
    if request.method == 'POST':
        student = Student.objects.get(id=id)
        student.name = request.POST.get('name')
        student.student_id = request.POST.get('student_id')
        student.grade_id = request.POST.get('grade')
        student.notice = request.POST.get('notice')
        student.save()
        return redirect('/manager/students_all/1')
    student = Student.objects.get(id=id)
    grade_list = Grade.objects.all()
    return managerRender(request, 'edit_student.html', {'student': student,
                                                        'grade_list': grade_list})

@login_required(login_url='/login')
@check_staff
@csrf_protect
def book_all(request, page):
    books = Books.objects.all()
    paginator = Paginator(books, 10)
    l = page - 1 if page - 1 > 0 else 1
    r = page + 1 if page + 1 <= paginator.num_pages else paginator.num_pages
    return managerRender(request, 'book_all.html', {"books": paginator.get_page(page),
                                                     'l': l,
                                                     'r': r})

@login_required(login_url='/login')
@check_staff
@csrf_protect
def add_book(request):
    if request.method == 'POST':
        book = Books()
        book.name = request.POST.get('name')
        book.publish = request.POST.get('publish')
        book.author = request.POST.get('author')
        book.price = request.POST.get('price')
        book.ISBN = request.POST.get('isbn')
        book.notice = request.POST.get('notice')
        book.save()
        return redirect('/manager/book_all/1')
    return managerRender(request, 'add_book.html')
