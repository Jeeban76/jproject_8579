from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import TextFile, Ontology, GeneratedQuestion
from .utils import process_text, create_ontology, generate_questions
from .utils.text_processing import process_text

def upload_file(request):
    if request.method == 'POST' and request.FILES['file']:
        text_file = TextFile.objects.create(name=request.FILES['file'].name, file=request.FILES['file'])
        return redirect('process_file', file_id=text_file.id)
    return render(request, 'question_gen/upload.html')

def process_file(request, file_id):
    text_file = TextFile.objects.get(id=file_id)
    entities, relations = process_text(text_file.file.path)
    ontology = create_ontology(entities, relations)
    ontology_obj = Ontology.objects.create(name=f"Ontology for {text_file.name}")
    questions = generate_questions(ontology, entities, relations)
    for question in questions:
        GeneratedQuestion.objects.create(ontology=ontology_obj, question=question)
    return JsonResponse({"status": "success", "questions": questions})
