# api/urls.py
from django.urls import path
from .views import ProfileListCreateView, ProfileDetailView, TaskListCreateView, TaskDetailView, ClientListCreateView, ClientDetailView, ProjectListCreateView, ProjectDetailView, MemberListCreateView, MemberDetailView,CourseListCreateView, CourseDetailView,  TeamListCreateView, TeamDetailView,AnnouncementListCreateView, AnnouncementDetailView, EventListCreateView, EventDetailView, SupportListCreateView, SupportDetailView, TimelogListCreateView, TimelogDetailView, LeaveRequestListCreate, LeaveRequestDetail,DashboardTotalsView


urlpatterns = [
   
    path('profiles/', ProfileListCreateView.as_view(), name='profile-list'),
    path('profiles/<int:pk>/', ProfileDetailView.as_view(), name='profile-detail'),

    path('tasks/', TaskListCreateView.as_view(), name='task-list'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),

    path('clients/', ClientListCreateView.as_view(), name='client-list'),
    path('clients/<int:pk>/', ClientDetailView.as_view(), name='client-detail'),

    path('projects/', ProjectListCreateView.as_view(), name='project-list'),
    path('projects/<int:pk>/', ProjectDetailView.as_view(), name='project-detail'),

    path('members/', MemberListCreateView.as_view(), name='member-list'),   
    path('members/<int:pk>/', MemberDetailView.as_view(), name='member-detail'),

    path('teams/', TeamListCreateView.as_view(), name='team-list'),
    path('teams/<int:pk>/', TeamDetailView.as_view(), name='team-detail'),

    path('courses/', CourseListCreateView.as_view(), name='course-list'),
    path('courses/<int:pk>/', CourseDetailView.as_view(), name='course-detail'),

    path('announcements/', AnnouncementListCreateView.as_view(), name='announcement-list'),
    path('announcements/<int:pk>/', AnnouncementDetailView.as_view(), name='announcement-detail'),

    path('events/', EventListCreateView.as_view(), name='event-list'),
    path('events/<int:pk>/', EventDetailView.as_view(), name='event-detail'),

    path('supports/', SupportListCreateView.as_view(), name='support-list'),
    path('supports/<int:pk>/', SupportDetailView.as_view(), name='support-detail'),

    path('timelogs/', TimelogListCreateView.as_view(), name='timelog-list'),
    path('timelogs/<int:pk>/', TimelogDetailView.as_view(), name='timelog-detail'),

    path('leave-requests/', LeaveRequestListCreate.as_view(), name='leave-request-list-create'),
    path('leave-requests/<int:pk>/', LeaveRequestDetail.as_view(), name='leave-request-detail'),

    path("dashboard/totals/", DashboardTotalsView.as_view(), name="dashboard-totals"),
   

]
