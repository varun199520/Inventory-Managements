from django.shortcuts import render


def index(request):
    from student_management.models import Student
    context = {'student_count': Student.objects.count()}
    return render(request, 'main/index.html', context)


def profile(request):
    """User profile page (for sidebar Profile link)."""
    return render(request, 'main/profile.html')