from django.shortcuts import render
from django.views.generic import View


class CourseListView(View):
    def get(self, request):
        return render(request, 'course-list.html', {})
