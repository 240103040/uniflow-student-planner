import datetime
import pytest
from django.urls import reverse
from planner.models import Assignment

pytestmark = pytest.mark.django_db

def test_home_page_loads(client):
    response = client.get(reverse("dashboard"))
    assert response.status_code == 200
    assert b"UniFlow" in response.content

def test_create_assignment(client):
    response = client.post(reverse("dashboard"), {
        "title": "Database project",
        "subject": "DBMS",
        "due_date": "2026-11-20",
    })
    assert response.status_code == 302
    item = Assignment.objects.get()
    assert item.title == "Database project"
    assert item.subject == "DBMS"
    assert item.is_completed is False

def test_empty_title_is_rejected(client):
    response = client.post(reverse("dashboard"), {
        "title": "",
        "subject": "DBMS",
        "due_date": "2026-11-20",
    })
    assert response.status_code == 200
    assert Assignment.objects.count() == 0
    assert "This field is required" in response.content.decode()

def test_filter_pending_and_completed(client):
    pending = Assignment.objects.create(title="Pending task", subject="Math", due_date=datetime.date(2026, 11, 20))
    completed = Assignment.objects.create(title="Done task", subject="Java", due_date=datetime.date(2026, 11, 21), is_completed=True)
    response = client.get(reverse("dashboard") + "?status=pending")
    assert b"Pending task" in response.content
    assert b"Done task" not in response.content
    response = client.get(reverse("dashboard") + "?status=completed")
    assert b"Done task" in response.content
    assert b"Pending task" not in response.content

def test_toggle_completion(client):
    item = Assignment.objects.create(title="Quiz", subject="Networks", due_date=datetime.date(2026, 11, 22))
    response = client.post(reverse("toggle_assignment", args=[item.id]))
    assert response.status_code == 302
    item.refresh_from_db()
    assert item.is_completed is True

def test_assignments_sorted_by_due_date(client):
    later = Assignment.objects.create(title="Later", subject="Math", due_date=datetime.date(2026, 12, 1))
    earlier = Assignment.objects.create(title="Earlier", subject="DBMS", due_date=datetime.date(2026, 11, 1))
    response = client.get(reverse("dashboard"))
    content = response.content.decode()
    assert content.index("Earlier") < content.index("Later")
