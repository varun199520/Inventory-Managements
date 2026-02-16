from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import StudentForm
from .models import Student


def student_list(request):
    students = Student.objects.all().order_by('-created_at')
    return render(request, 'list.html', {'students': students})


@login_required
def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES, request=request)
        if form.is_valid():
            student = form.save()
            messages.success(request, f'Student "{student.first_name} {student.last_name}" was created successfully.')
            return redirect('students:student_profile', pk=student.pk)
    else:
        form = StudentForm(request=request)
    context = {
        'form': form,
        'title': 'Add New Student',
    }
    return render(request, 'form.html', context)


@login_required
def student_edit(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES, request=request, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, f'Student "{student.first_name} {student.last_name}" was updated successfully.')
            return redirect('students:student_profile', pk=student.pk)
    else:
        form = StudentForm(request=request, instance=student)
    context = {
        'form': form,
        'title': 'Edit Student',
        'student': student,
    }
    return render(request, 'form.html', context)


@login_required
def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    name = f"{student.first_name} {student.last_name}"
    if request.method == 'POST':
        student.delete()
        messages.success(request, f'Student "{name}" was deleted successfully.')
        return redirect('students:student_list')
    return redirect('students:student_list')


def student_profile(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request, 'profile.html', {'student': student})