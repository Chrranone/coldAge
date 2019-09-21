from django.db import models

class ProduceType(models.Model):
    type_name = models.CharField(max_length=20)
    type_image = models.ImageField(upload_to='produce',verbose_name='分类图片',null=True)

    def __str__(self):
        return self.type_name

class ProduceTypeTwo(models.Model):
    type_name = models.CharField(max_length=20)
    type_image = models.ImageField(upload_to='produce',verbose_name='分类图片',null=True)

    def __str__(self):
        return self.type_name


class ProgrameType(models.Model):
    type_name = models.CharField(max_length=20)
    type_info = models.CharField(max_length=20,null=True)
    type_image = models.ImageField(upload_to='produce',verbose_name='分类图片',null=True)

    def __str__(self):
        return self.type_name

class Produce(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField(max_length=50)
    content = models.CharField(max_length=100)
    image = models.ImageField(upload_to='produce',verbose_name='产品图片')
    produce_type = models.ForeignKey(ProduceType,on_delete=models.CASCADE)
    produce_type_two = models.ForeignKey(ProduceTypeTwo,on_delete=models.CASCADE,null=True)
    programe_type = models.ForeignKey(ProgrameType,on_delete=models.CASCADE,null=True)
    information_image = models.ImageField(upload_to='produce',verbose_name='产品介绍图片')
    information = models.CharField(max_length=100)

    def __str__(self):
        return "<produce: %s>" % self.name
