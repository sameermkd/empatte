from django.db import models
from datetime import datetime    

class EmpModel(models.Model):
    emp_id=models.CharField(unique=True, auto_created=True, max_length=5)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    phone=models.CharField(max_length=12)
    email=models.EmailField(null=True)
    def __str__(self):
        return self.first_name
class JobModel(models.Model):
    job_id=models.CharField(unique=True, auto_created=True, max_length=5)
    job_title=models.CharField(max_length=200)
    job_desc=models.TextField(max_length=500)
    job_starting=models.DateTimeField(default=None)
    job_ending=models.DateTimeField(default=None)
    job_status=models.TextField(max_length=200)
    def __str__(self):
        return self.job_title
class JobStarting(models.Model):
    s_date=models.DateField(default=datetime.now)
    s_name=models.TextField(max_length=100)
    s_jobs=models.TextField(max_length=100)
    s_start=models.TimeField(default=datetime.now)
    s_end=models.TimeField(default=datetime.now)
    s_status=models.TextField(max_length=200)
    s_lunch=models.CharField(max_length=3)
    s_holyday=models.CharField(max_length=3)
    def __str__(self):
        return self.s_name
    def workhour(self):
        s1 = str(self.s_start)
        s2 = str(self.s_end)
        start_dt = datetime.strptime(s1, '%H:%M:%S')
        end_dt = datetime.strptime(s2, '%H:%M:%S')
        diff = (end_dt - start_dt)
        days = diff.days
        days_to_hours = days * 24
        diff_btw_two_times = (diff.seconds) / 3600
        overall_hours = days_to_hours + diff_btw_two_times
        if self.s_lunch=='Yes':
            overall_hours=overall_hours-1
        return overall_hours
    def overtime(self):
        overtime=0
        s1 = str(self.s_start)
        s2 = str(self.s_end)
        start_dt = datetime.strptime(s1, '%H:%M:%S')
        end_dt = datetime.strptime(s2, '%H:%M:%S')
        diff = (end_dt - start_dt)
        days = diff.days
        days_to_hours = days * 24
        diff_btw_two_times = (diff.seconds) / 3600
        overall_hours = days_to_hours + diff_btw_two_times
        if self.s_lunch=='Yes' and self.s_holyday=='No':
            overall_hours=overall_hours-1
        if self.s_lunch=='Yes' and self.s_holyday=='No' and overall_hours>7:
            overtime=overall_hours-7
        if self.s_lunch=='No' and self.s_holyday=='Yes':
            overtime=overall_hours
        if self.s_lunch=='No' and self.s_holyday=='No':
            overtime=overall_hours
        if self.s_lunch=='Yes' and self.s_holyday=='Yes':
            overall_hours=overall_hours-1
            overtime=overall_hours
        return overtime
    