from django.conf.urls import url
from . import views

# 视图函数命名空间，就是我们调用视图函数的时候，是调用别名，如果有很多别名一样就必须设置这个
app_name = 'blog'
# 把网址和处理函数的关系写在了urlpatterns列表里
# 绑定关系的写法是把网址和对应的处理函数作为参数传给url函数
# 第一个参数是网址，第二参数是处理函数，第三个参数是name，这个参数的值将作为处理函数的别名。
# 网址参数是用正则表达式写的，该正则表达式的要匹配的是以空字符串开头且以空字符串结尾。
# 对于输入http://127.0.0.1:8000后，django首先会把协议http，域名127.0.0.1和端口号去掉，此时只剩下一个空字符串。匹配后就会调用views.index函数
# 但是django匹配url模式是在blogproject目录下的urls.py,所以最后一步是把blog的urls写进blogproject的urls里
urlpatterns = [
	url(r'^$', views.index, name='index'),
	# 以post开头，后跟一个至少一位的数字，并且以/结尾。(?<pk>[0-9]+)表示命名捕获组，作用是从用户访问的url里把括号
	# 内匹配的字符串捕获并作为关键字参数传给detail函数，例如用户访问post/255，匹配的就是255，detail(request,pk=255)
	url(r'^post/(?P<pk>[0-9]+)/$', views.detail, name='detail'),
	# 两个括号起来的地方就是两个命名组参数，django会从用户访问的url中自动提取这两个参数的值，然后传递给视图函数。
	# 例如如果用户想查看2017年3月下的全部文章，他访问/archives/2017/3，那么archives视图函数实际调用为
	# archives(request, year=2017, month=3)
	url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.archives, name='archives'),
	url(r'^category/(?P<pk>[0-9]+)/$', views.category, name='category'),
]