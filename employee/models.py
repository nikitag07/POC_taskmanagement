from django.db import models
# Department
class Department(models.Model):
    name=models.CharField(max_length=50,default=None)

    def __str__(self):
        return self.name

# Employee
class Employee(models.Model):
    department=models.ForeignKey(Department,on_delete=models.CASCADE)
    full_name=models.CharField(max_length=50,default=None)
    contact=models.CharField(max_length=50,default=None)
    email=models.EmailField(max_length=100,unique=True,default=None)
    emp_password=models.CharField(max_length=50,default=None)
    add_time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name

# Assign Work
class AssignWork(models.Model):
    employee=models.ForeignKey(Employee,on_delete=models.SET_NULL,null=True)
    work_detail=models.TextField(max_length=200,default=None)
    assign_time=models.DateTimeField(auto_now_add=True)
    work_status=models.BooleanField(default=False)

    def __str__(self):
        return self.work_detail

# Replies
class Reply(models.Model):
    work=models.ForeignKey(AssignWork,on_delete=models.CASCADE)
    reply_txt=models.TextField()
    reply_time=models.DateTimeField(auto_now_add=True)
    reply_status=models.BooleanField(default=False)

    class Meta:
        verbose_name='Reply' 
        verbose_name_plural='Replies'        

    def __str__(self):
        return '{0}'.format(self.reply_txt)
	
