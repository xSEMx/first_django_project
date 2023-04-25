import requests
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UrlForm, CommentsForm, NotificationsForm
from .models import Sites, Comments, Notifications
from django.contrib.auth.models import User

def index(request):
    if request.method == 'POST':
        form = UrlForm(request.POST)

        if form.is_valid():
            try:
                true_status = True if requests.get(form.cleaned_data['url']).status_code == 200 else False
            except requests.exceptions.RequestException:
                true_status = False
                
            res = Sites.objects.filter(url=form.cleaned_data['url'])

            if len(res) == 0:
                res = Sites(url=form.cleaned_data['url'], status=true_status)
            else:
                res = res[0]
                res.status = true_status
                
            res.save()
        else:
            res = None
    else:
        form  = UrlForm()
        res = None
    
    context = {
            'form': form,
            'res': res,
            'sites': Sites.objects.filter(famous=True)
    }
        
    return render(request, 'monitoring_vus/index.html', context)


def evaluations(request):
    if not request.POST:
        return redirect('/monitoring_vus/')

    if request.POST.get('id') == 'notification':
        form = CommentsForm()
        form_notification = NotificationsForm(request.POST)

        if form_notification.is_valid():
            email = form_notification.cleaned_data.get('email')
            site_id = Sites.objects.filter(url=request.POST.get('url'))[0].id

            Notifications(email=email, site_id=site_id).save()

    elif request.POST.get('id') == 'comment-delete':
        comment = Comments.objects.get(id=request.POST.get('comment_id'))
        comment.delete()

        form = CommentsForm()
            
    elif request.POST.get('id') == 'comment-edit':
        form = CommentsForm(request.POST)

        if form.is_valid():
            site_id = Sites.objects.filter(url=request.POST.get('url'))[0].id
            comment = Comments.objects.filter(user_id=request.user.id, site_id=site_id)[0]
        
            comment.evaluation = form.cleaned_data.get('evaluation')
            comment.review = form.cleaned_data.get('review') if form.cleaned_data.get('review') else ''
            comment.save()
            
    elif request.POST.get('id') == 'comment-new':
        form = CommentsForm(request.POST)

        if form.is_valid():
            user_id = User.objects.filter(id=request.user.id)[0].id
            site_id = Sites.objects.filter(url=request.POST.get('url'))[0].id
            evaluation = form.cleaned_data['evaluation']
            review = form.cleaned_data['review']
            
            Comments(user_id=user_id, site_id=site_id, evaluation=evaluation, review=review).save()
    else:
        form = CommentsForm()
    
    site = Sites.objects.filter(url=request.POST.get('url'))[0]
    comments_for_site = Comments.objects.filter(site_id=site.id)
    
    if request.user.is_authenticated:
        comments_for_site = comments_for_site.exclude(user_id=request.user.id)
    
    if request.POST.get('id') == 'more':
        more = False
    else:
        more = True if len(comments_for_site) > 4 else False
        comments_for_site = comments_for_site[:4] if more else comments_for_site
    
    if request.POST.get('user_id') != 'None':
        site_id = Sites.objects.filter(url=request.POST.get('url'))[0].id
        has_comment = Comments.objects.filter(user_id=request.user.id, site_id=site_id).exists()
        
        if has_comment:
            user_comment = Comments.objects.filter(user_id=request.user.id, site_id=site_id)[0]
        else:
            user_comment = None
    else:
        has_comment = False

    context = {
        'more': more,
        'has_comment': has_comment,
        'user_comment': user_comment,
        'comments' : comments_for_site,
        'site': site,
        'form': form,
        'form_notification': form_notification if request.POST.get('id') == 'notification' else NotificationsForm(),
        'url_site': request.POST.get('url'),
        'errors': 'true' if form.errors else 'false'
    }
    
    return render(request, 'monitoring_vus/evaluations.html', context)    