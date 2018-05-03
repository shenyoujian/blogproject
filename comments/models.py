from django.db import models

# Create your models here.
# created_time我们当然是希望自动生成，而不是用户去填写，所以设置auto_noe_add=True
# blank=True是允许为空
class Comment(models.Model):
	name = models.CharField(max_length=100)
	email = models.EmailField(max_length=255)
	url = models.URLField(blank=True)
	text = models.TextField()
	created_time = models.DateTimeField(auto_now_add=True)

	# post = models.Foreignkey('blog.Post')
	post = models.ForeignKey('blog.Post')

	def __str__(self):
		return self.text[:20]