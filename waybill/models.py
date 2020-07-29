from django.db import models


class Customer(models.Model):
    """
    客户,三一重工\沃尔沃等.
    """
    name = models.CharField("顾客名称",max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '客户'
        verbose_name_plural = verbose_name

class Department(models.Model):
    """
    客户的部门
    """
    name = models.CharField("部门名称",max_length=20)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE,
                                 related_name="departments")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '部门'
        verbose_name_plural = verbose_name

class Logistics(models.Model):
    """
    物流公司,平成\鹏泽等.
    """
    name = models.CharField("公司名称",max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '物流公司'
        verbose_name_plural = verbose_name


class Vehicle(models.Model):
    """
    车辆
    """
    license = models.CharField("车牌号",max_length=20)

    def __str__(self):
        return self.license

    class Meta:
        verbose_name = '车辆'
        verbose_name_plural = verbose_name

class Checklist(models.Model):
    """
    运货清单
    """
    logistics = models.ForeignKey(Logistics,on_delete=models.CASCADE,
                                  related_name="log_checklists")
    department = models.ForeignKey(Department,on_delete=models.CASCADE,
                                   related_name="dep_checklists")
    delivery = models.CharField("发货地",max_length=50)
    receipt = models.CharField("收货地",max_length=50)
    items = models.CharField("运货清单",max_length=20)
    number = models.CharField("运单号",max_length=20)

    def __str__(self):
        return self.number

    class Meta:
        verbose_name = '运单'
        verbose_name_plural = verbose_name
