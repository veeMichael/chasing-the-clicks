from django.http import JsonResponse
from django.shortcuts import render
from .models import ClickCount
from django.shortcuts import redirect


def home(request):
    click_count = ClickCount.objects.first() or ClickCount.objects.create(count=0)
    context = {'click_count': click_count.count}
    return render(request, 'base/home.html', context)


def update_click_count(request):
    click_count = ClickCount.objects.first()
    if click_count:
        click_count.count += 1
        click_count.save()
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False})
