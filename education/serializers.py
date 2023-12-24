from rest_framework import serializers

from education.models import Course, Lesson


class LessonCourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = ('pk', 'title_course',)


class CourseCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = ('title_course', 'description_course',)


class CourseSerializer(serializers.ModelSerializer):

    lesson_count = serializers.SerializerMethodField()  # поле вывода количества уроков
    lessons = LessonCourseSerializer(source='lesson_set', many=True)  # поле вывода уроков

    def get_lesson_count(self, instance):
        return instance.lesson_set.count()

    class Meta:
        model = Course
        fields = ('pk', 'title_course', 'image_course', 'description_course', 'lesson_count', 'lessons')


class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = '__all__'  # Выводить все поля
