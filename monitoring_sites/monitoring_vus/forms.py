import re
from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator, URLValidator
from .models import Sites, Comments, Notifications
    
class UrlForm(forms.Form):
    url = forms.URLField(label='Введите URL')
    
    def clean_url(self):
       url = self.cleaned_data['url']

       root_slashes_index = url.index('//')+1

       if url[root_slashes_index+1:].find('/') != -1:
           slash_index = root_slashes_index + url[root_slashes_index+1:].index('/') ++ 1
           url = url[:slash_index+1]
           
       return url


class CommentsForm(forms.ModelForm):
    review = forms.CharField(max_length=6000, required=False, label='Напишите отзыв (не более 6000 символов)', widget=forms.Textarea)
    
    class Meta:
        model = Comments
        fields = ('evaluation',)
        labels = {'evaluation': 'Поставьте оценку от 1 до 5',}


    def clean_evaluation(self):
        if not 1 <= self.cleaned_data['evaluation'] <= 5:
            raise ValidationError('Оценка должна быть от 1 до 5')

        return self.cleaned_data['evaluation']


class NotificationsForm(forms.ModelForm):
    class Meta:
        model = Notifications
        fields = ('email',)
        labels = {'email': "Введите ваш email"}