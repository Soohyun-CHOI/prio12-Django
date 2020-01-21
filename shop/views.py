from django.shortcuts import render, get_object_or_404, redirect

from shop.forms import ItemForm
from shop.models import Item


def item_list(request):
    qs = Item.objects.all()

    q = request.GET.get("q", "")
    if q:
        qs = qs.filter(name__icontains=q)

    ctx = {
        "item_list": qs,
        "q": q
    }
    return render(request, "shop/item_list.html", ctx)


def item_detail(request, pk):
    item = get_object_or_404(Item, pk=pk)

    ctx = {
        "item": item,
    }
    return render(request, "shop/item_detail.html", ctx)


def item_new(request, item=None):
    if request.method == "POST":
        form = ItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            item = form.save()
            return redirect(item)

    else:
        form = ItemForm(instance=item)

    ctx = {"form": form}
    return render(request, "shop/item_form.html", ctx)
