from django.db import models
from django.conf import settings
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class Profile(models.Model):
	user 			= models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	date_of_birth 	= models.DateField(blank=True, null=True)
	photo 			= models.ImageField(upload_to='users/%Y/%m/%d',blank=True)
	slug			= models.SlugField()
	is_instructor	= models.BooleanField(default=False)
	

	def __str__(self):
		return 'Profile for user {}'.format(self.user.username)

	def get_absolute_url(self):
		return reverse('profiles:profile_detail', args=[self.slug])

	def get_absolute_url_edit(self):
		return reverse('profiles:profile_update', args=[self.slug])

def post_save_user_receiver(sender, instance, created, *args, **kwargs):
    if created:
        profile, is_created = Profile.objects.get_or_create(user=instance, slug=instance.username)


post_save.connect(post_save_user_receiver, sender=User)
