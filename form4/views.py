from django.contrib.auth.decorators import login_required , permission_required
from django.shortcuts import render
from django.shortcuts import render , redirect , get_object_or_404,HttpResponseRedirect , HttpResponse

from giris.views import login_view
from .models import Form3 as Form3Model
from .forms import Form3
from django.db.models import Q
import mimetypes
from form_1.models import Form1
from form2.models import Form2
from .models import Form4
from .forms import Form4Form
from form5.models import Form5

# Create your views here.
@login_required(login_url=login_view)
def form4_view(request):
    if request.user.is_staff or request.user.is_superuser:
        listem = Form4.objects.all().order_by('Form44')
    else:
        listem=Form4.objects.all().order_by('Form44').filter(Olusturan=request.user)

    """query = request.GET.get('q')
    if query:
        listem = listem.filter(
            Q(id=int(query)) |
            Q(Olusturan__username__icontains=query) |
            Q(isin_kategorisi__icontains=query) |
            Q(Aciklama__icontains=query)
        ).distinct()"""
    return render(request , 'Form4/Form4.html' , {'listem': listem,'islem':
                                                  [islem.Form55 for islem in Form5.objects.all() if islem.Form55]})

@login_required(login_url=login_view)
def create(request,form1):
    form4=Form4Form(request.POST or None)

    context = {'form4': form4}
    if request.method == "POST":
        if form4.is_valid():
            a=form4.save(commit=False)
            a.Form44 = Form3.objects.get(Form33=form1)
            a.Olusturan = request.user
            a.save()
            return redirect('form4_view')
    return render(request, 'Form4/create.html', context)

@login_required(login_url=login_view)
def detail(request,pk):
    listem = get_object_or_404(Form4, id=pk)
    context = {'listem': listem}
    return render(request , 'Form4/detail.html', context)

@login_required(login_url=login_view)
@permission_required('form4.delete_form4',login_url=form4_view)
def delete(request , pk):
    listem = Form4.objects.get(id=pk)
    listem.delete()
    context = {'listem': listem}
    return redirect('form4_view')

@login_required(login_url=login_view)
@permission_required('form4.change_form4',login_url=form4_view)
def update(request,pk):
    listem = get_object_or_404(Form4 , id=pk)
    form4 = Form4Form(request.POST or None , instance=listem)
    if form4.is_valid():
        form4.save()
        return redirect('form4_view')
    context = {'form4': form4}
    return render(request, 'Form4/create.html', context)