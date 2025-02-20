from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import generics
from .models import  Profile, Announcement, Task, Client, Project, Member, Team, Course
from .serializers import  ProfileSerializer, AnnouncementSerializer, TaskSerializer, ClientSerializer, ProjectSerializer, MemberSerializer, TeamSerializer, CourseSerializer

 #List & Create Profiles
class ProfileListCreateView(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

# Retrieve, Update, Delete a Profile
class ProfileDetailView(generics.RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class MemberListCreateView(generics.ListCreateAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

class MemberDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

class ProjectListCreateView(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class ProjectDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class CourseListCreateView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CourseDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class TaskListCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer   

class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class ClientListCreateView(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class ClientDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class AnnouncementListCreateView(generics.ListCreateAPIView):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer

class AnnouncementDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer

class TeamListCreateView(generics.ListCreateAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class TeamDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
