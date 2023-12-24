from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework import viewsets

from education.models import Course, Lesson
from education.permissions import IsAutor, IsManager
from education.serializers import CourseSerializer, LessonSerializer, CourseCreateSerializer


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()

    def create(self, request, *args, **kwargs):
        self.serializer_class = CourseCreateSerializer
        new_course = super().create(request, *args, **kwargs)
        new_course.author = self.request.user
        new_course.save()
        return new_course

    def get_queryset(self):
        if not self.request.user.is_staff:
            return Course.objects.filter(autor=self.request.user)
        elif self.request.user.is_staff:
            return Course.objects.all()


class LessonListAPIView(ListAPIView):

    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAutor]


class LessonRetrieveAPIView(RetrieveAPIView):

    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsManager | IsAutor]


class LessonCreateAPIView(CreateAPIView):

    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsManager]

    def perform_create(self, serializer):
        new_lesson = serializer.save()
        new_lesson.author = self.request.user
        new_lesson.save()


class LessonUpdateAPIView(UpdateAPIView):

    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAutor]


class LessonDestroyAPIView(DestroyAPIView):

    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsManager]
