from django.shortcuts import render, get_object_or_404
from app_group.models import GroupChat

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


def group(request, group_slug):
    group = get_object_or_404(
        GroupChat, slug=group_slug
    )

    title = f'Group | {group_slug}'

    context = {
        'group':group,
        'title':title,
    }

    return render(
        request,
        "app_group/group.html",
        context
    )

