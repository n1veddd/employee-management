from datetime import date
from django.test import TestCase
from django.urls import reverse

from .models import Employee


class EmployeeViewsTests(TestCase):
    def setUp(self):
        Employee.objects.create(
            name="Asha", email="asha@example.com", department="IT",
            salary=35000, joining_date=date(2025, 1, 10)
        )
        Employee.objects.create(
            name="Rahul", email="rahul@example.com", department="HR",
            salary=30000, joining_date=date(2025, 2, 15)
        )

    def test_home_shows_employees_and_count(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Asha")
        self.assertEqual(response.context["total"], 2)

    def test_search_by_department(self):
        response = self.client.get(reverse("home"), {"search": "it"})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Asha")
        self.assertNotContains(response, "Rahul")
        self.assertEqual(response.context["total"], 1)

    def test_delete_requires_post(self):
        employee = Employee.objects.get(email="asha@example.com")
        self.client.get(reverse("delete", args=[employee.id]))
        self.assertTrue(Employee.objects.filter(id=employee.id).exists())
        self.client.post(reverse("delete", args=[employee.id]))
        self.assertFalse(Employee.objects.filter(id=employee.id).exists())
