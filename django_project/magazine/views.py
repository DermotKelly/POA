# magazine/views.py
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Magazine
from .forms import MagazineForm

@login_required
def magazine_list(request):
    magazines = Magazine.objects.all()
    return render(request, 'magazine/magazine_list.html', {'magazines': magazines})

@login_required
def magazine_detail(request, magazine_id):
    magazine = Magazine.objects.get(id=magazine_id)
    return render(request, 'magazine/magazine_detail.html', {'magazine': magazine})

@login_required
def add_magazine(request):
    if request.method == 'POST':
        form = MagazineForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('magazine_list')
    else:
        form = MagazineForm()
    return render(request, 'magazine/add_magazine.html', {'form': form})

