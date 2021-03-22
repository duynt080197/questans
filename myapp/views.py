from django.shortcuts import render
from .models import Question
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import QuestionSerializer
# Create your views here.

def home(request):
    list_question = Question.objects.all()
    context = {"dsquest":list_question}
    return render(request, "home.html", context) 

def detail(request, question_id):
    q = Question.objects.get(pk=question_id)
    tags = q.tags.split(",")
    return render(request, "detail.html", {"q":q, "tags":tags})

def up(request,question_id):
    q = Question.objects.get(pk=question_id)
    dulieu = request.POST["up"]
    q.up = q.up + 1
    q.save()
    return HttpResponse(q.up)

def down(request,question_id):
    q = Question.objects.get(pk=question_id)
    dulieu = request.POST["down"]
    q.down = q.down + 1
    q.save()
    return HttpResponse(q.down)


class GetQuestionsAPI(APIView):
    def get(self, request):
        list_questions = Question.objects.all()
        mydata = QuestionSerializer(list_questions, many=True)
        return Response(data=mydata.data, status=status.HTTP_200_OK)
