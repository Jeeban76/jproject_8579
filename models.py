from django.db import models

class TextFile(models.Model):
    name = models.CharField(max_length=255)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to="uploads/")

class Ontology(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

class GeneratedQuestion(models.Model):
    ontology = models.ForeignKey(Ontology, on_delete=models.CASCADE, related_name="questions")
    question = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
