from django.urls import path
from django.views.decorators.cache import cache_page
from .views import (StudentRegistrationView, StudentEnrollCourseView,
					StudentCourseListView, StudentCourseDetailView,
					DeleteEnrollCourseView, ModuleContentRetreiveView,course_content_list)

app_name = 'students'
 
urlpatterns = [
	path('register/', StudentRegistrationView.as_view(), name='student_registration'),
	path('enroll-course/', StudentEnrollCourseView.as_view(), name='student_enroll_course'),
	path('unroll-course/', DeleteEnrollCourseView.as_view(), name='student_unroll_course'),
	path('module-content/', ModuleContentRetreiveView.as_view(), name='module_content_ajax'),
	path('courses/', StudentCourseListView.as_view(), name='student_course_list'),
	# path('course/<int:pk>/', StudentCourseDetailView.as_view(),
			# name='student_course_detail'),
	path('course/<int:pk>/', course_content_list, name='student_course_detail'),
	# path('course/<int:pk>/<int:module_id>/', StudentCourseDetailView.as_view(),
			# name='student_course_detail_module'),
]