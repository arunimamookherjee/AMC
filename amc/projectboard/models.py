
# Create your models here.

from django.db import models


# Create your models here.

class qp(models.Model):
    title=models.CharField(max_length=500)
    paper=models.CharField(max_length=500000000000000000000)
    latex=models.BooleanField(blank=True)
    amcText=models.BooleanField(blank=True)
    ques=models.IntegerField(default=0)


    def _str_(self):
        return "List: {}".format(self.name)
