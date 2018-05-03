from django import forms
from .models import Comment

# 表单必须继承forms.Form类或者forms.ModelForm类，如果表单对应有一个数据库模型
# 那么使用ModelForm类会简单很多。
# 表单内部类Meta里指定一些和表单相关的东西。model=Comment表明这个表单对应数据库模型是Comment类。
# field指定表单需要显示的字段。
class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ['name', 'email', 'url', 'text']