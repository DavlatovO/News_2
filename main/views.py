from django.shortcuts import render
from .models import News, Category
from django.forms import model_to_dict
from rest_framework.generics import ListAPIView, RetrieveAPIView, ListCreateAPIView
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response

from .serializers import NewsSerializer


class NewsAPIView(APIView):
    def get(self, request: Request) -> Response:
        newses = News.objects.values()
        return Response(newses)
    


    def post(self, request:Request):
        title = request.data['title']
        content = request.data['content']
        category_id = request.data['category_id']

        news = News.objects.create(
            title=title,
            content = content,
            category_id = category_id
        )

        return Response({'news':model_to_dict(news), 'message':"Maqola qo'shildi!!!"})

