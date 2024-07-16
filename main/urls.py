from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (FacultyViewSet, SpecialityViewSet, TeacherViewSet, SubjectViewSet, LanguageViewSet, 
                    StudentStatusViewSet, NewsViewSet, NotificationViewSet, ApplicationViewSet, 
                    ApplicationStatusViewSet, TypeOfGradesViewSet, StudentViewSet, GradeViewSet, 
                    StudentOfFacultyViewSet, StudentOfSpecialityViewSet, StudentOfLanguageViewSet, 
                    DayOfWeekViewSet, ScheduleVersionViewSet, ScheduleViewSet)

# Создаем роутер для автоматического определения URL.
router = DefaultRouter()
router.register(r'faculties', FacultyViewSet)
router.register(r'specialities', SpecialityViewSet)
router.register(r'teachers', TeacherViewSet)
router.register(r'subjects', SubjectViewSet)
router.register(r'languages', LanguageViewSet)
router.register(r'student-statuses', StudentStatusViewSet)
router.register(r'news', NewsViewSet)
router.register(r'notifications', NotificationViewSet)
router.register(r'applications', ApplicationViewSet)
router.register(r'application-statuses', ApplicationStatusViewSet)
router.register(r'type-of-grades', TypeOfGradesViewSet)
router.register(r'students', StudentViewSet)
router.register(r'grades', GradeViewSet)
router.register(r'student-of-faculties', StudentOfFacultyViewSet)
router.register(r'student-of-specialities', StudentOfSpecialityViewSet)
router.register(r'student-of-languages', StudentOfLanguageViewSet)
router.register(r'day-of-weeks', DayOfWeekViewSet)
router.register(r'schedule-versions', ScheduleVersionViewSet)
router.register(r'schedules', ScheduleViewSet)

# URL-паттерны Django, включающие все роутеры для автоматической маршрутизации.
urlpatterns = [
    path('', include(router.urls)),
]
