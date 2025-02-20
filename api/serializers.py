# api/serializers.py
from rest_framework import serializers
from .models import  Profile, Announcement, Task, Client, Project, Member, Team, Course

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
    teamleader = MemberSerializer(read_only=True)  # Full leader details
    teammembers = MemberSerializer(many=True, read_only=True)  # Full members details
    project = ProjectSerializer(read_only=True)

    class Meta:
        model = Team
        fields = ['id', 'teamname', 'teamleader', 'teammembers', 'project']
        read_only_fields = ['id']


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course    
        fields = ['id', 'name', 'instructor', 'duration', 'level', 'enrolledstudents', 'description']
        read_only_fields = ['id']



class ClientSerializer(serializers.ModelSerializer):
    project = ProjectSerializer(read_only=True)
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
    assignedto = MemberSerializer(read_only=True)  # Returns full Member details
    class Meta:
        model = Task        
        fields = ['id', 'title', 'duedate', 'status', 'assignedto', 'description']
        read_only_fields = ['id']

