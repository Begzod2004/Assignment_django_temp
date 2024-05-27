
from django.db import models
from django.contrib.auth.models import User


from django.utils.text import slugify
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.db.models.functions import Now


class CompanyInfo(models.Model):
    name = models.CharField(max_length=100)
    about = models.CharField(max_length=1900)
    address = models.CharField(max_length=100)
    gmail = models.CharField(max_length=70)
    phone = models.CharField(max_length=50)
    logo = models.ImageField(upload_to='static/img/logo')

    def __str__(self):
        return f"{self.name} {self.address} {self.gmail}"


class Facts(models.Model):
    number = models.CharField(max_length=20)
    title = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.number} {self.title}"


class Service(models.Model):
    name = models.CharField(max_length=75)
    title = models.CharField(max_length=100)
    i_class = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} {self.title}"


class Testimonial(models.Model):
    title = models.CharField(max_length=500)
    author = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.author}"


class Employee(models.Model):
    full_name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    image = models.ImageField(upload_to='static/img/employee_images')

    def __str__(self):
        return f"{self.full_name} {self.position}"


class News(models.Model):
    comments = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=70)
    about = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.title} {self.about}"


# Create your models here.


class Profile(models.Model):
	user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
	first_name = models.CharField(max_length=200, blank=True, null=True)
	last_name = models.CharField(max_length=200, blank=True, null=True)
	email = models.CharField(max_length=200)
	profile_pic = models.ImageField(null=True, blank=True, upload_to="images", default="/user.png")
	bio = models.TextField(null=True, blank=True)
	twitter = models.CharField(max_length=200,null=True, blank=True)

	def __str__(self):
		name = str(self.first_name)
		if self.last_name:
			name += ' ' + str(self.last_name)
		return name

class Tag(models.Model):
	name = models.CharField(max_length=200)

	def __str__(self):
		return self.name


class Post(models.Model):
	headline = models.CharField(max_length=200)
	sub_headline = models.CharField(max_length=200, null=True, blank=True)
	thumbnail = models.ImageField(null=True, blank=True, upload_to="images", default="/images/placeholder.png")
	body = RichTextUploadingField(null=True, blank=True)
	created = models.DateTimeField(auto_now_add=True)
	active = models.BooleanField(default=False)
	featured = models.BooleanField(default=False)
	tags = models.ManyToManyField(Tag, null=True, blank=True)
	slug = models.SlugField(null=True, blank=True)

	def __str__(self):
		return self.headline

	def save(self, *args, **kwargs):

		if self.slug == None:
			slug = slugify(self.headline)

			has_slug = Post.objects.filter(slug=slug).exists()
			count = 1
			while has_slug:
				count += 1
				slug = slugify(self.headline) + '-' + str(count) 
				has_slug = Post.objects.filter(slug=slug).exists()

			self.slug = slug

		super().save(*args, **kwargs)


class PostComment(models.Model):
	author = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
	post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True)
	body = models.TextField(null=True, blank=True)
	created = models.DateTimeField(auto_now_add=True, null=True, blank=True)

	def __str__(self):
		return self.body

	# @property
	# def created_dynamic(self):
	# 	now = timezone.now()
	# 	return now
	