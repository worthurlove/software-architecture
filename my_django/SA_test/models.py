from django.db import models

# Create your models here.
#监控机器的表
class computer(models.Model):
    #计算机ID，作为主键
    computer_id = models.IntegerField(primary_key=True)

    #该机器的监控状态，默认值为on表示处于被监控状态，为off时表示暂不监控
    computer_status = models.CharField(default = 'on',max_length = 3)

    def __str__(self):
        return self.computer_id


class computer_info(models.Model):
    
    #cpu负载率
    cpu_info = models.FloatField()

    #cpu负载率信息的报告时间
    info_time = models.DateTimeField()

    #外键，对应机器的id
    computer_id = models.ForeignKey(computer,on_delete = True)


    def __str__(self):
        return self.cpu_info

    objects = models.Manager()


