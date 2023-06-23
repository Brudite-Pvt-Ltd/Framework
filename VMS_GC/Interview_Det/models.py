from django.db import models


class Interview(models.Model):
    username = models.CharField(max_length=100)
    candidate_email = models.EmailField()
    interviewer_email = models.EmailField()
    additional_people_email = models.EmailField(blank=True)
    google_meet_link = models.URLField(blank=True)
    interview_time = models.DateTimeField()
    remarks = models.TextField(blank=True)

    def __str__(self):
        return self.username
