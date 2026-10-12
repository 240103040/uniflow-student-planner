from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST
from .forms import AssignmentForm
from .models import Assignment

def dashboard(request):
    if request.method == "POST":
        form = AssignmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("dashboard")
    else:
        form = AssignmentForm()

    status = request.GET.get("status", "all")
    assignments = Assignment.objects.all()
    if status == "pending":
        assignments = assignments.filter(is_completed=False)
    elif status == "completed":
        assignments = assignments.filter(is_completed=True)
    else:
        status = "all"

    sort = request.GET.get("sort", "due_date")
    if sort == "due_date":
        assignments = assignments.order_by("due_date", "created_at")
    else:
        sort = "due_date"

    return render(request, "planner/dashboard.html", {
        "form": form,
        "assignments": assignments,
        "status": status,
        "sort": sort,
        "total_count": Assignment.objects.count(),
    })

@require_POST
def toggle_assignment(request, assignment_id):
    assignment = get_object_or_404(Assignment, pk=assignment_id)
    assignment.is_completed = not assignment.is_completed
    assignment.save(update_fields=["is_completed"])
    return redirect("dashboard")
