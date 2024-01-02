from rest_framework import serializers

from education.models import Course, Lesson, Subscription
from education.validators import UrlValidator

class LessonCourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = ('pk', 'title_course',)


class CourseCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = ('title_course', 'description_course',)


class CourseSerializer(serializers.ModelSerializer):

    lesson_count = serializers.IntegerField(source='lesson_set.all.count', read_only=True)  # поле вывода количества уроков
    lessons = LessonCourseSerializer(source='lesson_set', read_only=True, many=True)  # поле вывода уроков
    course_subscription = serializers.SerializerMethodField()

    def get_lesson_count(self, instance):
        return instance.lesson_set.count()

    def get_course_subscription(self, obj):
        """ Метод вывода подписан ли пользователь на курс """
        return Subscription.objects.filter(course_subscription=obj, user=self.context['request'].user).exists()

    class Meta:
        model = Course
        fields = ('pk', 'title_course', 'image_course', 'description_course', 'lesson_count', 'lessons', 'course_subscription',)


class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = '__all__'  # Выводить все поля
        validators = [UrlValidator(field='url_lesson')]


class SubscriptionSerializer(serializers.ModelSerializer):
    """ Сериализатор модели подписки"""

    class Meta:
        model = Subscription
        fields = '__all__'

