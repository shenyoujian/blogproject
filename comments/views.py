from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Post

from .models import Comment
from .forms import CommentForm
# Create your views here.
def post_comment(request, post_pk):
	# 先获取被评论的文章，因为后面需要把评论和被评论的文章关联起来。
	post = get_object_or_404(Post, pk=post_pk)

	# http请求有get和post，提交表单时通过post，只有当用户的请求为post才需要处理表单数据
	if request.method == 'POST':
		# 用户提交的数据存在request.Post中，这是一个类字典对象。
		# 我们利用这些数据构造了CommentsForm的实例，这样django的表单就生成了
		form = CommentForm(request.POST)

		# 当调用form.is_valid()方法时，django自动帮我们检查表单的数据是否符合格式要求。
		if form.is_valid():
			# 检查到数据是合法的，调用表单的save方法保存数据到数据库
			# commit = False的作用是仅仅利用表单的数据生成Comment模型类的实例，但还不保存评论数据到数据库
			comment = form.save(commit=False)

			# 将评论和被评论的文章关联起来
			comment.post = post

			# 最终将评论数据保存到数据库
			comment.save()

			# 然后重定向post的详情页，实际上当redirect函数接受一个模型的实例时，它会调用这个模型实例的get_absolute__url方法
			# 然后重定向到get_absolute_url方法返回的url
			return redirect(post)
		else:
			# 当检查到数据不合法，重新渲染详情页，并且渲染表单的错误
			# 因此我们传了三个模板变量给detail.html
			# 一个是文章(post),一个是评论列表，一个是表单form
			# 注意我们这里用到了post.comment_set.add()
			# 其作用是获取该文章下的所有评论
			# 跟Comment.objects.filter(post=post)是一样的
			# 因为post和comment是foreignkey关联我们就可以
			# 使用post.comment_set.all()反向查询全部评论
			comment_list = post.comment_set.all()
			context = {'post':post,
						'form':form,
						'comment_list':comment_list
						}
			return render(request, 'blog/detail.html', context=context)
	return redirect(post)