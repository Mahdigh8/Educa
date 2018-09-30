from django.db import models
from django.contrib.auth.models import User

# This class store the module id of every course that student enrolled in and
# remember where the student left the course
class ModuleContinue(models.Model):
	student 	= models.ForeignKey(User ,related_name='courses_countinue' ,on_delete=models.CASCADE)
	course 		= models.PositiveIntegerField()
	module 		= models.PositiveIntegerField(blank=True, null=True)

	def __str__(self):
		return "{}-{}-{}".format(self.student.username, self.course, self.module)