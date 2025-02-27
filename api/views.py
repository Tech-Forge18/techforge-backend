from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import generics
from .models import  Profile, Announcement, Task, Client, Project, Member, Team, Course, Event, Support,Timelog, LeaveRequest
from .serializers import  ProfileSerializer, AnnouncementSerializer, TaskSerializer, ClientSerializer, ProjectSerializer, MemberSerializer, TeamSerializer, CourseSerializer, EventSerializer, SupportSerializer, TimelogSerializer, LeaveRequestSerializer, TotalsSerializer

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

class EventListCreateView(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class EventDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class SupportListCreateView(generics.ListCreateAPIView):
    queryset = Support.objects.all()
    serializer_class = SupportSerializer

class SupportDetailView(generics.RetrieveUpdateDestroyAPIView): 
    queryset = Support.objects.all()
    serializer_class = SupportSerializer

class TimelogListCreateView(generics.ListCreateAPIView):
   queryset = Timelog.objects.all()
   serializer_class = TimelogSerializer

class TimelogDetailView(generics.RetrieveDestroyAPIView):
    queryset = Timelog.objects.all()
    serializer_class = TimelogSerializer

class LeaveRequestListCreate(generics.ListCreateAPIView):
    queryset = LeaveRequest.objects.all()
    serializer_class = LeaveRequestSerializer

class LeaveRequestDetail(generics.RetrieveUpdateAPIView):
    queryset = LeaveRequest.objects.all()
    serializer_class = LeaveRequestSerializer

class DashboardTotalsView(APIView):
    def get(self, request):
        totals = {
            "totalMembers": Member.objects.count(),
            "totalClients": Client.objects.count(),
            "totalProjects": Project.objects.count(),
            "totalCourses": Course.objects.count(),
            "totalTeams": Team.objects.count(),
            # Assuming "Vacancies" could be open tasks or support tickets; adjust as needed
            "totalVacancies": Task.objects.filter(status="Pending").count(),  # Example derivation
        }
        serializer = TotalsSerializer(totals)
        return Response(serializer.data)