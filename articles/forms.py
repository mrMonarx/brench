from django import forms

from .models import Article
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title','content']
    def clean(self):
        cleaned_data = self.cleaned_data
        title = cleaned_data.get('title')
        content = cleaned_data.get('content')
        qr_t = Article.objects.filter(title__icontains=title)
        qr_c = Article.objects.filter(content__icontains=content)
        if qr_t.exists():
            self.add_error('title', f'"{title}" is already taken')
        if qr_c.exists():
            self.add_error('content', f'"{content}" is already taken')
        return cleaned_data




class ArticleForm_old(forms.Form):
    title = forms.CharField()
    content = forms.CharField()

    def clean(self):
        cleaned_data = self.cleaned_data
        print('cleaned_data: ', cleaned_data)
        title = cleaned_data.get('title')
        content = cleaned_data.get('content')
        if title.lower().strip() == 'the office':
            self.add_error('title', 'this title is taken')


        if 'content' in content:
            self.add_error('content', 'this content is taken')
            raise forms.ValidationError('Not allowed.')
        return cleaned_data



