from django.db import models
from django.contrib.auth.models import User


class Books(models.Model):
    name = models.CharField(max_length=100, verbose_name='书名')
    publish = models.CharField(max_length=100, verbose_name='出版社', null=True, blank=True)
    author = models.CharField(max_length=100, verbose_name='作者', null=True, blank=True)
    price = models.IntegerField(default=0, verbose_name='价格')
    ISBN = models.CharField(max_length=100, verbose_name='ISBN', null=True, blank=True)
    notice = models.TextField(verbose_name='备注', null=True, blank=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = '书籍'
        verbose_name_plural = '书籍'


class College(models.Model):
    name = models.CharField(max_length=100, verbose_name='学院名称')
    notice = models.TextField(verbose_name='备注', null=True, blank=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = '学院'
        verbose_name_plural = '学院'


class Major(models.Model):
    name = models.CharField(max_length=100, verbose_name='专业名称')
    college = models.ForeignKey(College, on_delete=models.CASCADE, verbose_name='所属学院')
    notice = models.TextField(verbose_name='备注', null=True, blank=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = '专业'
        verbose_name_plural = '专业'


class Grade(models.Model):
    name = models.CharField(max_length=100, verbose_name='班级名称')
    major = models.ForeignKey(Major, on_delete=models.CASCADE, verbose_name='所属专业')
    notice = models.TextField(verbose_name='备注', null=True, blank=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = '班级'
        verbose_name_plural = '班级'


class Student(models.Model):
    name = models.CharField(max_length=100, verbose_name='学生姓名')
    student_id = models.CharField(max_length=100, verbose_name='学号')
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE, verbose_name='所属班级')
    account = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='账号', null=True, blank=True)
    notice = models.TextField(verbose_name='备注', null=True, blank=True)

    def __str__(self):
        return f"{self.name}——{self.student_id}"

    class Meta:
        verbose_name = '学生'
        verbose_name_plural = '学生'


class SemesterOrder(models.Model):
    name = models.CharField(max_length=100, verbose_name='学期名称')
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE, verbose_name='所属班级')
    notice = models.TextField(verbose_name='备注', null=True, blank=True)

    def __str__(self):
        return f"{self.grade} {self.name}"

    class Meta:
        verbose_name = '学期订单'
        verbose_name_plural = '学期订单'


class Order(models.Model):
    book = models.ForeignKey(Books, on_delete=models.CASCADE, verbose_name='书籍')
    semester = models.ForeignKey(SemesterOrder, on_delete=models.CASCADE, verbose_name='学期')
    notice = models.TextField(verbose_name='备注', null=True, blank=True)

    def __str__(self):
        return f"{self.book}"

    class Meta:
        verbose_name = '订单'
        verbose_name_plural = '订单'


class FeedBack(models.Model):
    tabel = models.ForeignKey(SemesterOrder, on_delete=models.CASCADE, verbose_name='学期')
    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name='学生')
    content = models.TextField(verbose_name='反馈内容',max_length=100)
    time = models.DateTimeField(auto_now_add=True, verbose_name='反馈时间')
    msg_account = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='回复账号', null=True, blank=True)
    msg = models.TextField(verbose_name='回复',max_length=100, null=True, blank=True)
    msg_time = models.DateTimeField(verbose_name='回复时间', null=True, blank=True)

    def __str__(self):
        return f"{self.student}"

    class Meta:
        verbose_name = '反馈'
        verbose_name_plural = '反馈'
