# -*- coding:utf-8 -*-
from datetime import datetime
# from DjangoUeditor.models import UEditorField


from django.db import models
from organization.models import CourseOrg, Teacher


class Course(models.Model):
    course_org = models.ForeignKey(CourseOrg, verbose_name="课程机构", null=True, blank=True)
    name = models.CharField(max_length=50, verbose_name="课程名称")
    desc = models.CharField(max_length=300, verbose_name="课程描述")
    detail = models.TextField(verbose_name="课程详情")

    # Python 3 中无法使用 Ueditor
    # detail = UEditorField(verbose_name="课程详情", width=600, height=300, imagePath="course/ueditor/",
    #                         filePath="course/ueditor/", default="")

    is_banner = models.BooleanField(default=False, verbose_name="是否轮播")
    degree = models.CharField(verbose_name="课程难度", choices=(("cj", "初级"), ("zj", "中级"), ("gj", "高级")), max_length=2)
    learn_times = models.IntegerField(default=0, verbose_name="学习时长(分钟数)")
    teacher = models.ForeignKey(Teacher, verbose_name="讲师", null=True, blank=True)
    students = models.IntegerField(default=0, verbose_name="学习人数")
    fav_nums = models.IntegerField(default=0, verbose_name="收藏人数")
    image = models.ImageField(upload_to="course/%Y/%m", verbose_name="封面图片", max_length=100)
    click_nums = models.IntegerField(default=0, verbose_name="点击数")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")
    tag = models.CharField(default='', verbose_name="课程标签", max_length=10)
    category = models.CharField(max_length=20, verbose_name="课程类别", default="后端开发")
    you_need_know = models.CharField(max_length=300, verbose_name="课程须知", default='')
    teacher_tell = models.CharField(max_length=300, verbose_name="老师告诉你", default='')

    class Meta:
        verbose_name = "课程"
        verbose_name_plural = verbose_name

    # 获取课程章节数
    def get_zj_nums(self):
        return self.lesson_set.all().count()
    # 修改后台列名的显示，否则该列显示为 get_zj_nums
    get_zj_nums.short_description = "章节数"


    # def go_to(self):
    #     from django.utils.safestring import mark_safe
    #     return mark_safe("<a href='http://www.baidu.com'>跳转</a>")
    # go_to.short_description = "跳转"

    def get_learn_users(self):
        return self.usercourse_set.all()[:5]

    # 获取课程所有章节
    def get_course_lesson(self):
        return self.lesson_set.all()

    def __str__(self):
        return self.name


# 只是为了在 admin 中注册不同的数据，不要再生成一张新表，但具有 model 的功能
class BannerCourse(Course):
    class Meta:
        verbose_name = "轮播课程"
        verbose_name_plural = verbose_name
        proxy = True


class Lesson(models.Model):
    course = models.ForeignKey(Course, verbose_name="课程")
    name = models.CharField(max_length=100, verbose_name="章节名")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "章节"
        verbose_name_plural = verbose_name

    # 获取章节视频
    def get_lesson_video(self):
        return self.video_set.all()

    def __str__(self):
        return self.name


class Video(models.Model):
    lesson = models.ForeignKey(Lesson, verbose_name="章节")
    name = models.CharField(max_length=100, verbose_name="视频名")
    url = models.CharField(max_length=200, verbose_name="访问地址", default='')
    learn_times = models.IntegerField(default=0, verbose_name="学习时长(分钟数)")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "视频"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class CourseResource(models.Model):
    course = models.ForeignKey(Course, verbose_name="课程")
    name = models.CharField(max_length=100, verbose_name="名称")
    download = models.FileField(upload_to="course/resource/%Y/%m", verbose_name="资源文件", max_length=100)
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "课程资源"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

