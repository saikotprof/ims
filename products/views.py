from django.shortcuts import render
from .models import Device, Apple, Samsung, Xiaomi
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def index(request):
    items = Device.objects.all()
    paginator = Paginator(items, 8)
    page = request.GET.get('page')

    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        items = paginator.page(1)
    except EmptyPage:
        items = paginator.page(paginator.num_pages)

    context = {
        'items': items,
        'header': 'Home Page',
    }
    return render(request, 'index.html', context)


def product(request):
    items = Device.objects.all()
    paginator = Paginator(items, 8)
    page = request.GET.get('page')

    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        items = paginator.page(1)
    except EmptyPage:
        items = paginator.page(paginator.num_pages)
    context = {
        'items': items,
        'header': 'Products Page',
    }
    return render(request, 'products/products_details.html', context)


def apple(request):
    items = Apple.objects.all()
    paginator = Paginator(items, 8)
    page = request.GET.get('page')

    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        items = paginator.page(1)
    except EmptyPage:
        items = paginator.page(paginator.num_pages)
    context = {
        'items': items,
        'header': 'Apple',
    }

    return render(request, 'products/products.html', context)


def samsung(request):
    items = Samsung.objects.all()
    paginator = Paginator(items, 8)
    page = request.GET.get('page')

    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        items = paginator.page(1)
    except EmptyPage:
        items = paginator.page(paginator.num_pages)
    context = {
        'items': items,
        'header': 'Samsung',
    }

    return render(request, 'products/products.html', context)


def xiaomi(request):
    items = Xiaomi.objects.all()
    paginator = Paginator(items, 8)
    page = request.GET.get('page')

    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        items = paginator.page(1)
    except EmptyPage:
        items = paginator.page(paginator.num_pages)
    context = {
        'items': items,
        'header': 'Xiaomi',
    }

    return render(request, 'products/products.html', context)


class AppleCreateView(CreateView):
    model = Apple
    fields = ['name', 'brand', 'price', 'status', 'remarks']
    template_name = 'products/add/apple_form.html'
    success_url = reverse_lazy('product-details')


class SamsungCreateView(CreateView):
    model = Samsung
    fields = ['name', 'brand', 'price', 'status', 'remarks']
    template_name = 'products/add/samsung_form.html'
    success_url = reverse_lazy('product-details')


class XiaomiCreateView(CreateView):
    model = Xiaomi
    fields = ['name', 'brand', 'price', 'status', 'remarks']
    template_name = 'products/add/xiaomi_form.html'
    success_url = reverse_lazy('product-details')


class AppleUpdateView(UpdateView):
    model = Apple
    fields = ['name', 'brand', 'price', 'status', 'remarks']
    template_name = 'products/edit/apple_edit.html'
    success_url = reverse_lazy('product-details')


class SamsungUpdateView(UpdateView):
    model = Samsung
    fields = ['name', 'brand', 'price', 'status', 'remarks']
    template_name = 'products/edit/samsung_edit.html'
    success_url = reverse_lazy('product-details')


class XiaomiUpdateView(UpdateView):
    model = Xiaomi
    fields = ['name', 'brand', 'price', 'status', 'remarks']
    template_name = 'products/edit/xiaomi_edit.html'
    success_url = reverse_lazy('product-details')


class AppleDeleteView(DeleteView):
    model = Apple
    template_name = 'products/delete/apple_confirm_delete.html'
    success_url = reverse_lazy('apple')

class SamsungDeleteView(DeleteView):
    model = Samsung
    template_name = 'products/delete/samsung_confirm_delete.html'
    success_url = reverse_lazy('samsung')


class XiaomiDeleteView(DeleteView):
    model = Xiaomi
    template_name = 'products/delete/xiaomi_confirm_delete.html'
    success_url = reverse_lazy('xiaomi')
