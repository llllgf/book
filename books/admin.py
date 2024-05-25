from django.contrib import admin

# Register your models here.
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import Books, College, Major, Grade, Student, Order, SemesterOrder, FeedBack
from .resources import StudentResource, BookResource


class OrderInline(admin.TabularInline):
    model = Order
    extra = 1
    fieldsets = (
        ['Main', {
            'fields': ('book',),
        }],
        ['Advance', {
            'classes': ('collapse',),
            'fields': ('notice',),
        }]
    )




@admin.register(Books)
class BooksAdmin(ImportExportModelAdmin):
    list_display = ('name', 'publish', 'author', 'price', 'ISBN', 'notice')
    search_fields = ('name', 'publish', 'author', 'ISBN')
    list_filter = ('publish', 'author')
    resource_class=BookResource


@admin.register(College)
class CollegeAdmin(admin.ModelAdmin):
    list_display = ('name', 'notice')
    search_fields = ('name',)


@admin.register(Major)
class MajorAdmin(admin.ModelAdmin):
    list_display = ('name', 'college', 'notice')
    search_fields = ('name', 'college__name')
    list_filter = ('college',)


@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'major', 'notice')
    search_fields = ('name', 'major__name')
    list_filter = ('major',)


@admin.register(Student)
class StudentAdmin(ImportExportModelAdmin):
    list_display = ('name', 'grade', 'account', 'notice')
    search_fields = ('name', 'grade__name', 'account__username')
    list_filter = ('grade__major__college', 'grade__major')
    resource_class = StudentResource

# admin.site.register(Student, StudentAdmin)

@admin.register(SemesterOrder)
class SemesterOrderAdmin(admin.ModelAdmin):
    list_display = ('name', 'grade', 'notice')
    search_fields = ('grade__name',)
    list_filter = ('grade',)
    inlines = [OrderInline]


@admin.register(FeedBack)
class FeedBackAdmin(admin.ModelAdmin):
    list_display = ('tabel', 'student', 'content', 'time', 'msg_account')
    search_fields = ('tabel__name__icontains', 'student__name__icontains', 'msg_account__username__icontains')


from django.contrib import admin

admin.site.site_header = '书本费管理后台'  # 设置header
admin.site.site_title = '书本费管理后台'  # 设置title
admin.site.index_title = '书本费管理后台'
