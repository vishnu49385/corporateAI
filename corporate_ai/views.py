from django.shortcuts import render


def index(request):
    context = {
        "page":"index",
    }
    return render(request, 'index.html', context)

def products(request):
    context = {
        "page":"products",
    }
    return render(request, 'products.html',context)

def cad_detail(request):
    context = {
        "page":"services",
    }
    return render(request, 'cad.html',context)

def cce_detail(request):
    context = {
        "page":"products",
    }
    return render(request, 'cce.html',context)

def graphic_detail(request):
    context = {
        "page":"services",
    }
    return render(request, 'graphic-design.html',context)

def uiux_detail(request):
    context = {
        "page":"services",
    }
    return render(request, 'ui-ux.html',context)

def qee_detail(request):
    context = {
        "page":"products",
    }
    return render(request, 'qee.html',context)

def incinerator_detail(request):
    context = {
        "page":"products",
    }
    return render(request, 'incinerator.html',context)

def product_detail(request):
    context = {
        "page":"services",
    }
    return render(request, 'product-detail.html',context)

def services(request):
    context = {
        "page":"services",
    }
    return render(request, 'services.html',context)

def contact(request):
    context = {
        "page":"contact",
    }
    return render(request, 'contact.html',context)

def about(request):
    context = {
        "page":"about",
    }
    return render(request, 'about.html',context)
