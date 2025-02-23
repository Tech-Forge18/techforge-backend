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
    # Display names for team members and project
    teammembers = serializers.StringRelatedField(many=True, read_only=True)
    project = serializers.StringRelatedField(read_only=True)

    # Accept member IDs and project ID for creation
    teammember_ids = serializers.PrimaryKeyRelatedField(queryset=Member.objects.all(), many=True, source='teammembers', write_only=True)
    project_id = serializers.PrimaryKeyRelatedField(queryset=Project.objects.all(), source='project', write_only=True)

    class Meta:
        model = Team
        fields = ['id', 'name', 'leader', 'teammembers', 'teammember_ids', 'project', 'project_id']
        read_only_fields = ['id', 'teammembers', 'project']

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

