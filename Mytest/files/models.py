from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Folder(models.Model):
    folder_name = models.CharField(max_length=30, primary_key=True)
    create_time = models.DateField(auto_now_add=True)


class FilesModel(models.Model):
    file_name = models.CharField('文件名', max_length=100)
    folder_name = models.ForeignKey(Folder, on_delete=models.DO_NOTHING)

    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    is_show = models.BooleanField('展示', default=True)
    create_time = models.DateField('上传时间', auto_now_add=True)
    change_time = models.DateField('修改时间', auto_now=True)
    # Browse_user = models.ManyToManyField(User, on_delete=models.DO_NOTHING)
    # change_user = models.ManyToManyField
