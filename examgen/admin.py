from django.contrib import admin
from examgen.models import Course, Exam

# Register your models here. 
class CourseAdmin(admin.ModelAdmin):
    pass


class ExamAdmin(admin.ModelAdmin):
    pass

admin.site.register(Course, CourseAdmin)
admin.site.register(Exam, ExamAdmin)