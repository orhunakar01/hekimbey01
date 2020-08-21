import mimetypes

from django.contrib.auth import authenticate
from django.contrib.auth.decorators import permission_required , login_required
from django.contrib.auth.models import User
from django.shortcuts import render , redirect , get_object_or_404 , HttpResponseRedirect , HttpResponse

from giris.views import login_view
from .models import Form1
from .forms import Form1Form
from django.db.models import Q
from form2.models import Form2
from form3.models import Form3
from datetime import datetime , timedelta , time
from django.contrib.auth.models import Group,GroupManager,Permission

@login_required(login_url=login_view)
def form1_view(request):
    if request.user.is_staff or request.user.is_superuser:
        listele=Form1.objects.all().order_by('pk')
    else:
        listele=Form1.objects.all().order_by('pk').filter(Olusturan=request.user)
    #query = request.GET.get('q')
    # Item.objects.filter(created__startswith='2015-10-01')  -Item.objects.filter(created__contains=date(2015, 10, 1))
    """if query:

        listele = listele.filter(
             Q(ilgili_birim__icontains=query) |
             Q(isin_kategorisi__icontains=query) |
             Q(konusu__icontains=query) |
             Q(dosya__icontains=query) |
             Q(sorumlu_kisi__icontains=query) |
             Q(Olusturan__username__icontains=query)
        ).distinct()"""

    return render(request , 'Form1/Form1.html' , {'listele': listele,'islemdekiler':[islemdekiler.Form22
                                                                                     for islemdekiler in Form2.objects.all()
                                                                                     if islemdekiler.Form22]
                                                  })

@login_required(login_url=login_view)
def form1_detail(request , pk):
    liste = get_object_or_404(Form1 , id=pk)
    context = {'liste': liste}
    return render(request , 'Form1/detail.html' , context)

@login_required(login_url=login_view)
def create(request):
    form = Form1Form(request.POST or None , request.FILES or None)
    context = {'form': form}
    if request.method == "POST":
        if form.is_valid():
            a = form.save(commit=False)
            a.Olusturan = request.user
            a.save()
            return redirect('form1_view')
    return render(request , 'Form1/form.html' , context)


@login_required(login_url=login_view)
@permission_required('form_1.change_form1',login_url=form1_view)
def update(request , pk):
    liste = get_object_or_404(Form1 , id=pk)
    form = Form1Form(request.POST or None,request.FILES or None, instance=liste)
    if form.is_valid():
        form.save()
        return redirect('form1_view')
    context = {'form': form}
    return render(request , 'Form1/form.html' , context)


@login_required(login_url=login_view)
@permission_required('form_1.delete_form1',login_url=form1_view)
def delete(request , pk):
    liste = Form1.objects.get(id=pk)
    #   if User.groups.name('Yetkili'):
    liste.delete()
    context = {'liste': liste}
    return redirect('form1_view')




@login_required(login_url=login_view)
def download(request , pk):
    liste = get_object_or_404(Form1 , id=pk)
    file_path = liste.dosya.path
    file_name = str(liste.dosya)

    fh = open(file_path , 'rb')
    mime_type , _ = mimetypes.guess_type(file_path)
    response = HttpResponse(fh , content_type=mime_type)
    response['Content-Disposition'] = f"attachment; filename={file_name}"
    return response
