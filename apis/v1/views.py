from django.shortcuts import render

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import authentication, permissions


from notices.models import Notice
from jobs.models import Job
from events.models import Event
from users.models import User, PushNotificationToken

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
    queryset = Notice.objects.all().order_by('updated_on', 'posted_on')
    serializer_class = NoticeSerializer

class JobListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Job.objects.all().order_by('updated_on', 'posted_on')
    serializer_class = JobSerializer

class EventsListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Event.objects.all().order_by('updated_on', 'posted_on')
    serializer_class = EventSerializer

class PushNotificationView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request, format=None):
        user = request.user
        token = request.data.get('token')
        try:
            PushNotificationToken.objects.get(token=token)
        except:
            # create a new token entry
            if(token):
                PushNotificationToken.objects.create(
                    user = user,
                    token = token
                )
            
            
        return Response("DONE")
        
class Profile(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request, format=None):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

    def patch(self, request, format=None):
        return Response("patched success")