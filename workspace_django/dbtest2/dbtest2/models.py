from django.db import models


class MyBoard(models.Model):
    myname = models.CharField(max_length=100)
    mytitle = models.CharField(max_length=300)
    mycontent = models.CharField(max_length=2000)
    mydate = models.DateTimeField()

# 상속받아서 재정의 __str__
    def __str__(self):
        return str({"myname": self.myname, "mytitle": self.mytitle,"mycontent": self.mycontent,"mydate": self.mydate})



