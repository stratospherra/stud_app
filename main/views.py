from django.shortcuts import render
from main.models import DayOfWeek, Language
from rest_framework import viewsets
from .models import (Student, Faculty, StudentOfFaculty, Speciality, Teacher, Subject, Language, 
                     StudentStatus, News, Notification, Application, ApplicationStatus, 
                     StudentOfLanguage, StudentOfSpeciality, TypeOfGrades, Grade, 
                     DayOfWeek, ScheduleVersion, Schedule)
from .serializers import (FacultySerializer, SpecialitySerializer, TeacherSerializer, SubjectSerializer, 
                          LanguageSerializer, StudentStatusSerializer, NewsSerializer, NotificationSerializer, 
                          ApplicationSerializer, ApplicationStatusSerializer, TypeOfGradesSerializer, 
                          StudentSerializer, GradeSerializer, StudentOfFacultySerializer, 
                          StudentOfSpecialitySerializer, StudentOfLanguageSerializer, DayOfWeekSerializer, 
                          ScheduleVersionSerializer, ScheduleSerializer)


def index(request):
    return render(request, 'index.html')

class FacultyViewSet(viewsets.ModelViewSet):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer

class SpecialityViewSet(viewsets.ModelViewSet):
    queryset = Speciality.objects.all()
    serializer_class = SpecialitySerializer

class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

class LanguageViewSet(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer

class StudentStatusViewSet(viewsets.ModelViewSet):
    queryset = StudentStatus.objects.all()
    serializer_class = StudentStatusSerializer

class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer

class ApplicationStatusViewSet(viewsets.ModelViewSet):
    queryset = ApplicationStatus.objects.all()
    serializer_class = ApplicationStatusSerializer

class TypeOfGradesViewSet(viewsets.ModelViewSet):
    queryset = TypeOfGrades.objects.all()
    serializer_class = TypeOfGradesSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class GradeViewSet(viewsets.ModelViewSet):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer

class StudentOfFacultyViewSet(viewsets.ModelViewSet):
    queryset = StudentOfFaculty.objects.all()
    serializer_class = StudentOfFacultySerializer

class StudentOfSpecialityViewSet(viewsets.ModelViewSet):
    queryset = StudentOfSpeciality.objects.all()
    serializer_class = StudentOfSpecialitySerializer

class StudentOfLanguageViewSet(viewsets.ModelViewSet):
    queryset = StudentOfLanguage.objects.all()
    serializer_class = StudentOfLanguageSerializer

class DayOfWeekViewSet(viewsets.ModelViewSet):
    queryset = DayOfWeek.objects.all()
    serializer_class = DayOfWeekSerializer

class ScheduleVersionViewSet(viewsets.ModelViewSet):
    queryset = ScheduleVersion.objects.all()
    serializer_class = ScheduleVersionSerializer

class ScheduleViewSet(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer

