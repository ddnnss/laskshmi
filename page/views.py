from django.shortcuts import render
from .models import Banner
from item.models import *
from pytils.translit import slugify
import os
from PIL import Image

import csv
from django.core.files.storage import FileSystemStorage


# Create your views here.
def index(request):
    banners = Banner.objects.filter(is_active=True).order_by('-order')
    collections = Collection.objects.filter(show_at_homepage=True)
    main_category = Category.objects.all()









    # ItemImage.objects.create(item_id=1,image='items/1/1201.jpg')
    return render(request, 'page/index.html', locals())


def category(request, cat_slug):

    cat = Category.objects.get(name_slug=cat_slug)
    subcats = SubCategory.objects.filter(category=cat)
    return render(request, 'page/category.html', locals())

def subcategory(request, subcat_slug):

    subcat = SubCategory.objects.get(name_slug=subcat_slug)
    items = Item.objects.filter(subcategory_id=subcat.id)
    return render(request, 'page/subcategory.html', locals())