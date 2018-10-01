from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.generic.base import View
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, FormView
from braces.views import CsrfExemptMixin, JsonRequestResponseMixin
from courses.models import Course
from .models import ModuleContinue
from .forms import CourseEnrollForm, UserCreationForm


class StudentRegistrationView(CreateView):
	template_name = 'students/student/registration.html'
	form_class = UserCreationForm
	success_url = reverse_lazy('course_list')
	
	def form_valid(self, form):
		result = super(StudentRegistrationView, self).form_valid(form)
		cd = form.cleaned_data
		user = authenticate(username=cd['username'], password=cd['password1'])
		login(self.request, user)
		return result

# To enroll in a course
class StudentEnrollCourseView(LoginRequiredMixin, FormView):
	course = None
	form_class = CourseEnrollForm
	
	def form_valid(self, form):
		self.course = form.cleaned_data['course']
		self.course.students.add(self.request.user)
		ModuleContinue.objects.get_or_create(student=self.request.user, course=self.course.id)
		return super(StudentEnrollCourseView, self).form_valid(form)

	def get_success_url(self):
		return reverse_lazy('students:student_course_detail', args=[self.course.id])

# To unroll from a course
class DeleteEnrollCourseView(CsrfExemptMixin, JsonRequestResponseMixin, LoginRequiredMixin, View):

	def post(self, request):
		for key, id in self.request_json.items():
			course = get_object_or_404(Course, id=id)
			course.students.remove(self.request.user)
			module_continue = get_object_or_404(ModuleContinue, student=request.user, course=id)
			module_continue.delete()
		data = {'saved': True, 'id': id}
		return self.render_json_response(data)


class StudentCourseListView(LoginRequiredMixin, ListView):
	model = Course
	template_name = 'students/course/list.html'

	def get_queryset(self):
		qs = super(StudentCourseListView, self).get_queryset()
		return qs.filter(students__in=[self.request.user])



@login_required
def course_content_list(request, pk):
	course = get_object_or_404(Course, pk=pk, students__in=[request.user])
	module_id = request.GET.get('module')
	module = None
	try:
		module = course.modules.get(id=module_id)
		# saving module id for continue that course later
		obj = request.user.courses_countinue.get(course=course.id)
		obj.module = module_id
		obj.save()
	except:
		# if there is a module id for this user and this course we continue this module
		module_id = request.user.courses_countinue.get(course=course.id).module
		if module_id!=None:
			module = course.modules.get(id=module_id)
		else:
			module = course.modules.all()[0]

	if request.is_ajax():
		return render(request, 'students/course/list_ajax.html',
				{'object': course,'module': module})
	return render(request, 'students/course/detail.html',
				{'object': course,'module': module})



# For get the module contents by Ajax in StudentCourseDetailView
class ModuleContentRetreiveView(CsrfExemptMixin, JsonRequestResponseMixin, LoginRequiredMixin, View):

	def post(self, request):
		data = dict(self.request_json.items())
		course_id = data['course_id']
		module_id = data['module_id']
		course = get_object_or_404(Course, id=course_id)
		module = course.modules.get(id=module_id)

		return render(request, 'students/course/list_ajax.html', {'module': module})
		