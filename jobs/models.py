from django.db import models

class Employer(models.Model):
    name = models.CharField(max_length=100)
    # Add more fields as needed

    class Meta:
        app_label = 'jobs'  # Add the app_label attribute

    def __str__(self):
        return self.name

class Job(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    company = models.ForeignKey(Employer, on_delete=models.CASCADE)
    location = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    # Add more fields as needed

    def __str__(self):
        return self.title
