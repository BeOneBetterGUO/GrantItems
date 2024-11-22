from Tools.scripts.make_ctype import method
from django.db.models import Q
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.decorators.http import require_http_methods, require_POST, require_GET
from django.db.models import Count
from datetime import timedelta
from django.utils import timezone

from items.models import ItemCategory, ItemStatus, Item


# Create your views here.
def index(request):
    return render(request, 'index.html')


@login_required(login_url=reverse_lazy('grant_auth:login'))
def login_index(request):
    today = timezone.now().date()
    one_month_later = today + timedelta(days=30)

    expired_items = Item.objects.filter(owner=request.user, overdue__lt=today, status_id__in=[1, 3]).order_by(
        'overdue')[:5]
    expiring_soon_items = Item.objects.filter(owner=request.user, overdue__range=(today, one_month_later),
                                              status_id__in=[1, 3]).order_by(
        'overdue')[:5]
    pre_purchase_items = Item.objects.filter(owner=request.user, status_id=2).order_by('overdue')[
                         :5]  # Assuming status_id=2 represents pre-purchase items
    category_counts = Item.objects.filter(owner=request.user).values('type__name').annotate(count=Count('id')).order_by(
        'type__name')
    status_counts = Item.objects.filter(owner=request.user).values('status__name').annotate(count=Count('id')).order_by(
        'status__name')

    context = {
        'expired_items': expired_items,
        'expiring_soon_items': expiring_soon_items,
        'pre_purchase_items': pre_purchase_items,
        'today': today,
        'category_counts': list(category_counts),
        'status_counts': list(status_counts)
    }
    return render(request, 'login_index.html', context=context)


@require_http_methods(['GET', 'POST'])
@login_required(login_url=reverse_lazy('grant_auth:login'))
def item_add(request):
    if request.method == 'GET':
        categories = ItemCategory.objects.all()
        status = ItemStatus.objects.all()
        context = {
            'categories': categories,
            'status': status
        }
        return render(request, 'item_add.html', context=context)
    else:
        name = request.POST.get('name')
        description = request.POST.get('description')
        type = request.POST.get('type')
        status = request.POST.get('status')
        is_consumable = request.POST.get('is_consumable') == 'true'
        price = request.POST.get('price')
        count = request.POST.get('count')
        image = request.FILES.get('image')
        overdue = request.POST.get('overdue') or None
        link = request.POST.get('link')
        owner = request.user

        image_path = None
        if image:
            image_path = 'media/items/' + image.name
            with open(image_path, 'wb') as dest:
                for chunk in image.chunks():
                    dest.write(chunk)
        Item.objects.create(name=name, description=description,
                            type_id=type, status_id=status, is_consumable=is_consumable,
                            image=image_path, price=price,
                            count=count, overdue=overdue, link=link, owner=owner)
        return JsonResponse({'code': 200, 'msg': '发布成功'})


@require_http_methods(['GET', 'POST'])
@login_required(login_url=reverse_lazy('grant_auth:login'))
def show_all(request):
    items = Item.objects.filter(owner=request.user, status_id__in=[1, 2, 3]).order_by('type_id').order_by('status_id')
    context = {
        'items': items
    }
    return render(request, 'show_all.html', context=context)


@require_http_methods(['GET', 'POST'])
@login_required(login_url=reverse_lazy('grant_auth:login'))
def show_type(request, type_id):
    items = Item.objects.filter(owner=request.user, type_id=type_id, status_id__in=[1, 2, 3]).order_by('status_id')
    context = {
        'items': items
    }
    return render(request, 'show_all.html', context=context)


@require_http_methods(['GET', 'POST'])
@login_required(login_url=reverse_lazy('grant_auth:login'))
def show_status(request, status_id):
    items = Item.objects.filter(owner=request.user, status_id=status_id).order_by('type_id')
    context = {
        'items': items
    }
    return render(request, 'show_all.html', context=context)


def show_detail(request, item_id):
    item = Item.objects.get(id=item_id)
    context = {
        'item': item
    }
    return render(request, 'show_detail.html', context=context)


@require_http_methods(['GET', 'POST'])
@login_required(login_url=reverse_lazy('grant_auth:login'))
def item_modify(request, item_id):
    if request.method == 'GET':
        categories = ItemCategory.objects.all()
        status = ItemStatus.objects.all()
        context = {
            'categories': categories,
            'status': status,
            'item': Item.objects.get(id=item_id)
        }
        return render(request, 'item_modify.html', context=context)
    else:
        print(request.POST)
        name = request.POST.get('name')
        description = request.POST.get('description')
        type = request.POST.get('type')
        status = request.POST.get('status')
        is_consumable = request.POST.get('is_consumable') == 'true'
        price = request.POST.get('price')
        count = request.POST.get('count')
        image = request.FILES.get('image')
        overdue = request.POST.get('overdue') or None
        link = request.POST.get('link')
        owner = request.user

        if image:
            image_path = 'media/items/' + image.name
            with open(image_path, 'wb') as dest:
                for chunk in image.chunks():
                    dest.write(chunk)
            Item.objects.filter(id=item_id).update(name=name, description=description,
                                                   type_id=type, status_id=status, is_consumable=is_consumable,
                                                   image=image_path, price=price,
                                                   count=count, overdue=overdue, link=link, owner=owner)
        else:
            Item.objects.filter(id=item_id).update(name=name, description=description,
                                                   type_id=type, status_id=status, is_consumable=is_consumable,
                                                   price=price, count=count, overdue=overdue, link=link, owner=owner)
        return JsonResponse({'code': 200, 'msg': '修改成功！', 'item_id': item_id})


def item_remove(request, item_id):
    Item.objects.filter(id=item_id).update(status_id=4)
    return redirect('items:show_all')


def item_delete(request, item_id):
    Item.objects.filter(id=item_id).delete()
    return redirect('items:show_all')


@require_http_methods(['GET', 'POST'])
@login_required(login_url=reverse_lazy('grant_auth:login'))
def item_timeline(request):
    items = Item.objects.filter(owner=request.user, overdue__isnull=False, status_id__in=[1, 3]).order_by('overdue')
    context = {
        'items': items,
        'today': timezone.now().date()
    }
    return render(request, 'item_timeline.html', context=context)


@require_http_methods(['GET', 'POST'])
@login_required(login_url=reverse_lazy('grant_auth:login'))
def item_expired(request):
    items = Item.objects.filter(owner=request.user, overdue__lt=timezone.now().date(), status_id__in=[1, 3]).order_by(
        'overdue')
    context = {
        'items': items,
        'today': timezone.now().date()
    }
    return render(request, 'show_all.html', context=context)


@require_http_methods(['GET', 'POST'])
@login_required(login_url=reverse_lazy('grant_auth:login'))
@require_GET
def search(request):
    q = request.GET.get('q')
    items = Item.objects.filter(Q(name__icontains=q) | Q(description__icontains=q), owner=request.user)
    return render(request, 'show_all.html', context={'items': items})
