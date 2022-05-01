from django.shortcuts import render

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import authentication, permissions


from notices.models import Notice
from jobs.models import Job
from events.models import Event
from users.models import User

from .serializers import NoticeSerializer, JobSerializer, EventSerializer, UserSerializer

# class ExampleView(APIView):
#     permission_classes = [IsAuthenticated]

#     def get(self, request, format=None):
#         content = {
#             'status': 'request was permitted'
#         }
#         return Response(content)
    
class NoticeListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Notice.objects.all()
    serializer_class = NoticeSerializer

class JobListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Job.objects.all()
    serializer_class = JobSerializer

class EventsListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class Profile(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request, format=None):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

    def patch(self, request, format=None):
        return Response("patched success")