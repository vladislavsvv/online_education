from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework import viewsets

from education.models import Course, Lesson, Subscription
from education.paginations import LessonPaginator
from education.permissions import IsAutor, IsManager
from education.serializers import CourseSerializer, LessonSerializer, CourseCreateSerializer, SubscriptionSerializer


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    pagination_class = LessonPaginator
    permission_classes = [IsManager | IsAutor]

    def create(self, request, *args, **kwargs):
        self.serializer_class = CourseCreateSerializer
        new_course = super().create(request, *args, **kwargs)
        new_course.author = self.request.user
        return new_course


    def perform_create(self, serializer):
        # привязка создателя к курсу
        serializer.save()
        self.request.user.course_set.add(serializer.instance)

    def get_queryset(self):
        if not self.request.user.is_staff:
            return Course.objects.filter(author=self.request.user)
        elif self.request.user.is_staff:
            return Course.objects.all()


class LessonListAPIView(ListAPIView):

    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAutor]
    pagination_class = LessonPaginator


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


class SubscriptionCreateAPIView(CreateAPIView):

    serializer_class = SubscriptionSerializer
    queryset = Subscription.objects.all()
    permission_classes = [IsManager | IsAutor]

    def perform_create(self, serializer):
        serializer.save()
        self.request.user.subscription_set.add(serializer.instance)


class SubscriptionDestroyAPIView(DestroyAPIView):

    queryset = Subscription.objects.all()
    permission_classes = [IsManager | IsAutor]
