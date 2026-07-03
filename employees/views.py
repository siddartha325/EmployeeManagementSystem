from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee
from .forms import EmployeeForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required, user_passes_test
def admin_required(view_func):
    return user_passes_test(lambda u: u.is_superuser)(view_func)


def home(request):
    return render(request, 'home.html')


def dashboard(request):

    employees = Employee.objects.all().order_by('-id')

    context = {
        'employees': employees,
        'total_employees': Employee.objects.count(),
        'male_count': Employee.objects.filter(gender='Male').count(),
        'female_count': Employee.objects.filter(gender='Female').count(),
        'department_count': Employee.objects.values('department').distinct().count(),
    }

    return render(request, 'dashboard.html', context)


@login_required
@admin_required
def employee_list(request):
    employees = Employee.objects.all()

    search = request.GET.get('search')
    if search:
        employees = employees.filter(name__icontains=search)

    paginator = Paginator(employees, 10)  # 10 employees per page
    page_number = request.GET.get('page')
    employees = paginator.get_page(page_number)

    return render(request, 'employee_list.html', {
        'employees': employees
    })


@login_required
@admin_required
def add_employee(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm()

    return render(request, 'employee_form.html', {'form': form})


@login_required
@admin_required
def edit_employee(request, id):
    employee = get_object_or_404(Employee, id=id)

    if request.method == "POST":
        form = EmployeeForm(request.POST, request.FILES, instance=employee)

        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm(instance=employee)

    return render(request, 'employee_form.html', {'form': form})

@login_required
@admin_required
def delete_employee(request, id):
    employee = get_object_or_404(Employee, id=id)

    if request.method == "POST":
        employee.delete()
        return redirect('employee_list')

    return render(request, 'confirm_delete.html', {'employee': employee})


def employee_detail(request, id):
    employee = get_object_or_404(Employee, id=id)

    return render(request, 'employee_detail.html', {'employee': employee})