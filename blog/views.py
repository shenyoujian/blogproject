from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post, Category
import markdown
from comments.forms import CommentForm
# Create your views here.

# web服务器的作用就是接受来自用户的http请求，根据请求内容做出相应的处理，并把处理结果包装成http响应返回给用户。
# 这个函数体现了这个过程，request参数是django为我们封装好的http请求，它是HttpRequest的一个实例。
# 然后我们返回一个也是django帮我们封装好的HttpResonse实例。
# 使用render函数来构造HttpRespone，第一个参数是http请求，第二个参数是模板，第三个参数是掺入模板变量的字典。
# -表示倒序。
def index(request):
	post_list = Post.objects.all()
	return render(request, 'blog/index.html', context={
						'post_list':post_list,
				})

# 当用户点击继续阅读和文章标题的时候调用的视图函数
# 根据我们从url获取的pk获取数据库里中文章，然后传递给模板。
def detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	# 把数据库里的原始Markdown文本渲染成html,codehilite是语法高亮，toc则允许我们自动生成目录。
	post.body = markdown.markdown(post.body, extensions=[
                                     'markdown.extensions.extra',
                                     'markdown.extensions.codehilite',
                                     'markdown.extensions.toc',
                                  ])
	form = CommentForm()
	# 获取这篇post下的全部评论
	comment_list = post.comment_set.all()

	# 将文章，表单，以及文章下的评论列表作为模板变量传给detail.html模板
	context = {'post':post,
				'form':form,
				'comment_list':comment_list
				}
	return render(request, 'blog/detail.html', context=context)


# 归档视图函数，当有人点击归档下的链接时候，调用这个函数
# 传入年和月，post的create_time属性是一个date对象，里面包含了create_time.year和create_time.month
# 然后把传入的跟他们比较就行了，但是这里作为函数的参数列表，django要求把点换成下划线。
# 归档下的文章列表跟首页差不多，所以我们渲染的是首页，也就是说当点击归档下的链接我们返回的还是首页。
def archives(request, year, month):
	post_list = Post.objects.filter(created_time__year=year,
									created_time__month=month)
	return render(request, 'blog/index.html', context={'post_list':post_list})


# 分类视图函数
def category(request, pk):
	cate = get_object_or_404(Category, pk=pk)
	post_list = Post.objects.filter(category=cate)
	return render(request, 'blog/index.html', context={'post_list':post_list})