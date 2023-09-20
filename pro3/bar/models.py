from django.db import models

class Station(models.Model):
    name = models.CharField(max_length=64)
    code = models.CharField(max_length=3)
    def __str__(self):
        return f"{self.name} ({self.code})"
    
class Job(models.Model):
    post = models.CharField(max_length=64)
    def __str__(self):
        return f"{self.post}"
    
class Clerk(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    location = models.ForeignKey(Station, on_delete=models.CASCADE, related_name="location")
    position = models.ForeignKey(Job, on_delete=models.CASCADE, related_name="position")
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"