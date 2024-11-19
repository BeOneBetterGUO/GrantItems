from Tools.scripts.make_ctype import method
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.decorators.http import require_http_methods, require_POST, require_GET

from items.models import ItemCategory, ItemStatus, Item


# Create your views here.
def index(request):
    return render(request, 'index.html')


def login_index(request):
    return render(request, 'login_index.html')


def search(request):
    return render(request, 'search.html')


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


def show_all(request):
    items = Item.objects.filter(status_id__in=[1,2,3]).order_by('status_id')
    context = {
        'items': items
    }
    return render(request, 'show_all.html', context=context)


def show_type(request, type_id):
    items = Item.objects.filter(type_id=type_id, status_id__in=[1,2,3]).order_by('status_id')
    context = {
        'items': items
    }
    return render(request, 'show_all.html', context=context)


def show_status(request, status_id):
    items = Item.objects.filter(status_id=status_id).order_by('type_id')
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
