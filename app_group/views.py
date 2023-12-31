from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from app_group.models import GroupChat, Message
from django.http import JsonResponse

def index(request):
    groups = GroupChat.objects.order_by('-id')

    context = {
        'groups':groups,
    }
    return render(
        request,
        "app_group/index.html",
        context
    )


def save_message(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        group_slug = request.POST.get('group')
        group = get_object_or_404(GroupChat, slug=group_slug)

        user = request.user
        Message.objects.create(sender=user, content=message, group=group)
        
        return JsonResponse({'success': True})

@login_required
def group(request, group_slug):    
    group = get_object_or_404(
        GroupChat, slug=group_slug
    )
    messages = Message.objects.filter(group=group)

    title = f'Group | {group_slug}'

    context = {
        'group':group,
        'title':title,
        'messages':messages,
    }

    return render(
        request,
        "app_group/group.html",
        context
    )

