from django.db import models
from django.utils import timezone


class Dormitory(models.Model):
    KU_CHOICES = (
        ('伏見区', '伏見区'),
        ('東山区', '東山区'),
        ('上京区', '上京区'),
        ('北区', '北区'),
        ('南区', '南区'),
        ('中京区', '中京区'),
        ('西京区', '西京区'),
        ('左京区', '左京区'),
        ('下京区', '下京区'),
        ('右京区', '右京区'),
        ('山科区', '山科区'),
    )
    d_name = models.CharField(max_length=20, unique=True)
    ku = models.CharField(max_length=10, choices=KU_CHOICES)
    chou = models.CharField(max_length=10)
    banchi = models.CharField(max_length=10)

    def __str__(self):
        return '%s' % (self.d_name)


class School(models.Model):
    KU_CHOICES = (
        ('伏見区', '伏見区'),
        ('東山区', '東山区'),
        ('上京区', '上京区'),
        ('北区', '北区'),
        ('南区', '南区'),
        ('中京区', '中京区'),
        ('西京区', '西京区'),
        ('左京区', '左京区'),
        ('下京区', '下京区'),
        ('右京区', '右京区'),
        ('山科区', '山科区'),
    )
    s_name = models.CharField(max_length=20, unique=True)
    ku = models.CharField(max_length=10, choices=KU_CHOICES)
    chou = models.CharField(max_length=10)
    banchi = models.CharField(max_length=10)

    def __str__(self):
        return '%s' % (self.s_name)


class tamashii(models.Model):
    SEX_CHOICES = (
        ('男', '男'),
        ('女', '女'),
    )
    name = models.CharField(max_length=40)
    country = models.CharField(max_length=15)
    sex = models.CharField(max_length=1, choices=SEX_CHOICES)
    dormitory = models.ForeignKey(Dormitory, on_delete=models.CASCADE, to_field="d_name")
    room = models.IntegerField()
    evangelist = models.CharField(max_length=40)
    date = models.DateField(default=timezone.now)
    visit = models.DateField(auto_now=True)
    school = models.ForeignKey(School, on_delete=models.CASCADE, to_field="s_name")
    status = models.TextField(blank=True)

    def __str__(self):
        return '%s' % (self.name)
