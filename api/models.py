from django.db import models

class Member(models.Model):
    name = models.CharField(max_length=20)
    role = models.CharField(max_length=20)
    department = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    status = models.CharField( max_length=50)

    def __str__(self):
        return self.name

#Projects
class Project(models.Model):
    name = models.CharField(max_length=20)
    client = models.CharField(max_length=20)
    deadline = models.DateField()
    teamsize = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.name
    
#course
class Course(models.Model):
    name = models.CharField(max_length=20)
    instructor = models.CharField(max_length=20)
    duration = models.IntegerField()
    level = models.CharField(max_length=20)
    enrolledstudents = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.name
    

    
#team
class Team(models.Model):
    name = models.CharField(max_length=100)
    leader = models.CharField(max_length=20)
    teammembers = models.ManyToManyField(Member, related_name='teams')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='teams')

    def __str__(self):
        return self.name

#tasks
class Task(models.Model):
    title = models.CharField(max_length=50)
    duedate = models.DateField()
    status = models.CharField(max_length=20)
    assignedto = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="tasks")
    description = models.TextField()
    priority = models. CharField(max_length=20, default="Normal")

    def __str__(self):
        
        return self.title
    
#announcement
class Announcement(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.title
    
#client
class Client(models.Model):
    name = models.CharField(max_length=20)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="clients")
    email = models.EmailField(unique=True)
    contactinfo = models.TextField()
    status = models.CharField(max_length=20)

    def __str__(self):
        return self.name


# Profile
class Profile(models.Model):
    # Personal
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    phone = models.IntegerField()  # Fixed
    position = models.CharField(max_length=20)

    # Address
    country = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    postalcode = models.CharField(max_length=20)
    taxid = models.CharField(max_length=20)

    # Social media
    facebook = models.CharField(max_length=100, blank=True, null=True)
    twitter = models.CharField(max_length=100, blank=True, null=True)
    instagram = models.CharField(max_length=100, blank=True, null=True)
    linkedin = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.firstname


class Event(models.Model):
    title = models.CharField(max_length=100)
    startdate = models.DateField()
    enddate = models.DateField()
    time = models.TimeField(null=True, blank=True)  # Use datetime.time object
    category = models.CharField(max_length=20)
    description = models.TextField()

    def __str__(self):
        return self.title
    
class Support(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=20)
    priority = models.CharField(max_length=20)
    description = models.TextField()
    contactinfo = models.IntegerField()
    file = models.FileField(upload_to='support/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically stores the date and time when created
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title


class Timelog(models.Model):
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    break_time = models.PositiveIntegerField(help_text="Break time in minutes")
    task_description = models.TextField()

    def __str__(self):
        return f"Time log for {self.date} - {self.start_time} to {self.end_time}"

class LeaveRequest(models.Model):
    LEAVE_TYPES = (
        ('vacation', 'Vacation'),
        ('sick', 'Sick Leave'),
        ('personal', 'Personal Leave'),
    )
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('denied', 'Denied'),
    )

    type = models.CharField(max_length=20, choices=LEAVE_TYPES)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.type} request from {self.start_date} to {self.end_date}"