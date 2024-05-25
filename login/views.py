from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from books.models import Student


def userLogin(request):
    if request.method == "GET":
        return render(request, 'login.html')

    else:
        account = request.POST.get('account')
        password = request.POST.get('password')
        user = auth.authenticate(request, username=account, password=password)
        if user is not None:
            auth.login(request, user)
            request.session['account'] = account
            request.session['password'] = password
            return redirect('index')  # 跳转到登录成功后的页面
            # return render(request, 'index.html')
        else:
            return render(request, 'login.html', {'error_message': '用户名或密码错误'})


def activateAccount(request):
    if request.method == "POST":
        password = request.POST.get("password")
        password2 = request.POST.get("password2")
        name = request.POST.get("name")
        student_id = request.POST.get("student_id")
        if password is None or password2 is None  or name is None or student_id is None:
            return render(request, 'activate.html', {'error_message': '填写不完整'})
        if password != password2:
            return render(request, 'activate.html', {'error_message': '两次密码不同'})
        try:
            stu = Student.objects.get(name=name, student_id=student_id)
        except:
            return render(request, 'activate.html', {'error_message': '学生不存在'})
        try:
            acc = User.objects.create_user(username=student_id, password=password)
            stu.account = acc
            stu.save()
            auth.login(request, acc )
            request.session['account'] = student_id
            request.session['password'] = password
            return redirect('index')
        except:
            return render(request, 'activate.html', {'error_message': '激活失败'})
    return render(request, 'activate.html')


@login_required(login_url='/login')
def userLogout(request):
    auth.logout(request)
    return redirect('login')


@login_required(login_url='/login')
def home(request):
    if request.user.is_staff:
        return redirect('manager_index')
    else:
        return redirect('user_index')
