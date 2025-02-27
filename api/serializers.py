# api/serializers.py
from rest_framework import serializers
from .models import  Profile, Announcement, Task, Client, Project, Member, Team, Course, Event, Support,Timelog, LeaveRequest

# profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'firstname', 'lastname', 'email', 'phone', 'position', 'country', 'state', 'postalcode', 'taxid', 'facebook', 'twitter', 'instagram', 'linkedin']
        read_only_fields = ['id']

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ['id', 'name', 'role', 'department', 'email', 'status']
        read_only_fields = ['id']


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project        
        fields = ['id', 'name', 'client', 'deadline', 'teamsize', 'description']
        read_only_fields = ['id']


class TeamSerializer(serializers.ModelSerializer):
    # Use project name directly
    project = serializers.SlugRelatedField(
        queryset=Project.objects.all(),
        slug_field='name',  # Use the 'name' field of the Project model
    )

    # Use team member names directly
    teammembers = serializers.SlugRelatedField(
        queryset=Member.objects.all(),
        slug_field='name',  # Use the 'name' field of the Member model
        many=True,
    )

    class Meta:
        model = Team
        fields = ['id', 'name', 'leader', 'teammembers', 'project']
        read_only_fields = ['id']


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course    
        fields = ['id', 'name', 'instructor', 'duration', 'level', 'enrolledstudents', 'description']
        read_only_fields = ['id']



class ClientSerializer(serializers.ModelSerializer):
    project = serializers.SlugRelatedField(
        queryset=Project.objects.all(),
        slug_field='name',  # Use the 'name' field of the Project model
    )

    class Meta:
        model = Client
        fields = ['id', 'name', 'project', 'email', 'contactinfo', 'status']
        read_only_fields = ['id']


class AnnouncementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        fields = ['id', 'title', 'content', 'date']
        read_only_fields = ['id']

class TaskSerializer(serializers.ModelSerializer):
    # Use SlugRelatedField to represent the team by its name
    assignedto = serializers.SlugRelatedField(
        queryset=Team.objects.all(),
        slug_field='name',  # Use the 'name' field of the Team model
    )

    class Meta:
        model = Task
        fields = ['id', 'title', 'duedate', 'status', 'assignedto', 'description','priority']
        read_only_fields = ['id']

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'title', 'startdate', 'enddate','time', 'category', 'description']
        read_only_fields = ['id']

class SupportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Support
        fields = ['id', 'title', 'category', 'priority', 'description', 'contactinfo', 'file', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']


class TimelogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timelog
        fields = ['id', 'date', 'start_time', 'end_time', 'break_time', 'task_description']

class LeaveRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeaveRequest
        fields = ['id', 'type', 'start_date', 'end_date', 'status', 'created_at']

class TotalsSerializer(serializers.Serializer):
    totalMembers = serializers.IntegerField()
    totalClients = serializers.IntegerField()
    totalProjects = serializers.IntegerField()
    totalCourses = serializers.IntegerField()
    totalTeams = serializers.IntegerField()
    totalVacancies = serializers.IntegerField()