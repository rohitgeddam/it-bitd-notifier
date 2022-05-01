from rest_framework import serializers
from django.contrib.auth import get_user_model
from notices.models import Notice
from jobs.models import Job
from events.models import Event
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        exclude = ('password',)

class NoticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notice
        fields = '__all__'

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'
        
        
class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'