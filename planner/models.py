from django.db import models

class Assignment(models.Model):
    title = models.CharField(max_length=160)
    subject = models.CharField(max_length=100)
    due_date = models.DateField()
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["due_date", "created_at"]

    def __str__(self):
        return f"{self.title} ({self.subject})"
