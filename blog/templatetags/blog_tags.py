from ..models import Post, Category
from django import template
# 自定义模板标签
# 博客右边有四项内容最新文章，归档等
# 如果要让他们显示内容，就得从index视图函数里从数据库获取数据
# 然后再传给index.html模板，太麻烦，而且不止index模板，每个页面都有
# 又不能传给base模板，base又没有视图函数对应
# 这时候就可以使用自定义模板标签，例如定义一个get_recent_posts
# 我们只要在模板中写入{% get_recent_posts as recent_post_list %}
# 那么模板中就会有从数据库获取最新文章的列表，并且通过as语句保存到recent_post_list模板变量中。
# 这样我们就不用每个视图函数传递这个模板参数，直接在base模板中让模板自己去数据库里找并保存为模板变量。


# 最近文章模板标签
# 获取前num篇文章
# 定义函数还不够，django不知道如何使用
# 还得注册这个函数为模板标签
register = template.Library()

@register.simple_tag
def get_recent_posts(num=5):
	return Post.objects.all().order_by('-created_time')[:num]


# 归档模板标签
# date会返回一个列表，列表中的元素为每一篇Post的创建时间，精确到月份，降序排列
@register.simple_tag
def archives():
	return Post.objects.dates('created_time', 'month', order='DESC')


# 分类模板标签
@register.simple_tag
def get_categories():
	return Category.objects.all()


