from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from courses.models import Course
from .models import Profile
from .forms import UserEditForm, ProfileEditForm


@method_decorator(login_required, name='dispatch')
class ProfileDetailView(DetailView):
	model = Profile
	login_url = '/accounts/login/'

	def get_template_names(self):
		if self.is_instructor:
			template_name = 'profiles/detail.html'
		else:
			template_name = 'profiles/detail_students.html'
		return template_name

	def dispatch(self, request, slug):
		if slug!=request.user.profile.slug:
			return redirect('profiles:profile_detail', slug=request.user.profile.slug)

		profile = Profile.objects.filter(slug=slug)[0]
		self.is_instructor = False
		if profile.is_instructor:
			self.is_instructor = True
		return super(ProfileDetailView, self).dispatch(request, slug)

	def get_context_data(self, *args, **kwargs):
		context = super(ProfileDetailView, self).get_context_data(*args, **kwargs)
		context['is_instructor'] = self.is_instructor
		if self.is_instructor :
			courses_made = Course.objects.filter(owner=self.request.user)
			context['courses_made'] = courses_made

		courses_enrolled = Course.objects.filter(students__in=[self.request.user])
		context['courses_enrolled'] = courses_enrolled
		return context


@login_required
def edit(request, slug):
	if request.method == 'POST':
		user_form = UserEditForm(instance=request.user, data=request.POST)
		profile_form = ProfileEditForm(instance=request.user.profile, 
			data=request.POST, files=request.FILES)
		if user_form.is_valid() and profile_form.is_valid():
			user_form.save()
			profile_form.save()
			# messages.success(request, 'Profile updated successfully')
		else:
			pass
			# messages.error(request, 'Error updating your profile')
	else:
		user_form = UserEditForm(instance=request.user)
		profile_form = ProfileEditForm(instance=request.user.profile)
		
	return render(request,'profiles/update.html',
			{'user_form': user_form, 'profile_form': profile_form})