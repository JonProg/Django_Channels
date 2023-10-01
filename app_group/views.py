from django.shortcuts import render
from app_group.models import Groups

def index(request):
    groups = Groups.objects.order_by('-id')

    context = {
        'groups':groups,
    }
    return render(
        request,
        "app_group/index.html",
        context
    )

