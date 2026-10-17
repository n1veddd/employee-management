from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from .forms import EmployeeForm
from .models import Employee


def home(request):
    search = request.GET.get("search", "").strip()
    employees = Employee.objects.all().order_by("name")

    if search:
        employees = employees.filter(
            Q(name__icontains=search) |
            Q(department__icontains=search)
        )

    return render(request, "app/home.html", {
        "employees": employees,
        "total": employees.count(),
        "search": search,
    })


def add_employee(request):
    form = EmployeeForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("home")

    return render(request, "app/add_emp.html", {"form": form})


def edit_employee(request, id):
    employee = get_object_or_404(Employee, id=id)
    form = EmployeeForm(request.POST or None, instance=employee)

    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("home")

    return render(request, "app/edit.html", {"form": form, "employee": employee})


def delete_employee(request, id):
    employee = get_object_or_404(Employee, id=id)

    if request.method == "POST":
        employee.delete()

    return redirect("home")
