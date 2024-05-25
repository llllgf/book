from django.shortcuts import render


def check_staff(func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_staff:
            return func(request, *args, **kwargs)
        else:
            return render(request, 'permissions_error.html')

    return wrapper
