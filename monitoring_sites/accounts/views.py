from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from monitoring_vus.models import Comments, Sites
from monitoring_vus.forms import CommentsForm

from .forms import RegistrationForm

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            
            return redirect(f"/account/login?next={request.POST.get('next')}")
    else:
        form = RegistrationForm()

    return render(request, 'accounts/register.html', {'form': form, 'next': request.GET.get('name')})


@login_required
def profile(request):
    if not request.POST:
        return redirect('monitoring_vus')

    if request.POST.get('id') == 'comment-delete':
            comment = Comments.objects.get(id=request.POST.get('comment_id'))
            comment.delete()

            form = CommentsForm()
            
    elif request.POST.get('id') == 'comment-edit':  
        form = CommentsForm(request.POST)

        if form.is_valid():
            site_id = Sites.objects.filter(url=request.POST.get('url_site'))[0].id
            comment = Comments.objects.filter(user_id=request.user.id, site_id=site_id)[0]
        
            comment.evaluation = form.cleaned_data.get('evaluation')
            comment.review = form.cleaned_data.get('review') if form.cleaned_data.get('review') else ''
            
            comment.save()
    else:
        form = CommentsForm()
            
    user_comments = Comments.objects.filter(user_id=request.user.id)

    context = {
        'form': form,
        'user_comments': user_comments,
        'errors': 'true' if form.errors else 'false',
        'comments': 'true' if request.POST.get('id') != 'start' else 'false',
        'com_id': request.POST.get('com_id') if request.POST.get('com_id') else None
    }
    
    return render(request, 'accounts/profile.html', context)
    
