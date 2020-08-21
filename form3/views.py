from django.contrib.auth.decorators import permission_required , login_required
from django.shortcuts import render , redirect , get_object_or_404,HttpResponseRedirect , HttpResponse

from form_1.forms import Form1Form
from form_1.models import Form1
from giris.views import login_view
from .models import Form3 as Form3Model , Form3 , Malzeme
from .forms import Form3Form , MalzemeForm
from django.db.models import Q
import mimetypes
from form2.models import Form2
from form4.models import Form4

@login_required(login_url=login_view)
# Create your views here.
def form3_view(request):
    if request.user.is_staff or request.user.is_superuser:
        listem = Form3Model.objects.all().order_by('Form33__id')
    else:
        listem = Form3Model.objects.all().order_by('Form33__id').filter(Olusturan=request.user)

    """query = request.GET.get('q')
    if query:
        listem = listem.filter(
            Q(id=int(query)) |
            Q(Olusturan__username__icontains=query) |
            Q(isin_kategorisi__icontains=query) |
            Q(Aciklama__icontains=query)
        ).distinct()"""
    return render(request , 'Form3/Form3.html' , {'listem': listem,'islemde':
                                                  [islemde.Form44 for islemde in Form4.objects.all() if islemde.Form44]

                                                 ,'malzeme':malzeme })


@login_required(login_url=login_view)
def create(request,form1):
    form3=Form3Form(request.POST or None, request.FILES or None)

    context = {'form3': form3}
    if request.method == "POST":
        if form3.is_valid():
            a=form3.save(commit=False)
            a.Form33 = Form2.objects.get(Form22=form1)
            a.Olusturan = request.user
            a.save()
            if a.isin_kategorisi=='Malz.Tedariği':
                return redirect('create_malzeme',form3=a.id)
        return redirect(form3_view)
    return render(request, 'Form3/create.html', context)

@login_required(login_url=login_view)
def detail(request,pk):
    listem = get_object_or_404(Form3Model, id=pk)
    context = {'listem': listem}
    return render(request , 'Form3/detail.html', context)


@login_required(login_url=login_view)
@permission_required('form3.delete_form3',login_url=form3_view)
def delete(request , pk):
    listem = Form3Model.objects.get(id=pk)
    listem.delete()
    context = {'listem': listem}
    return redirect('form3_view')


@login_required(login_url=login_view)
@permission_required('form3.change_form3',login_url=form3_view)
def update(request,pk):
    listem = get_object_or_404(Form3Model , id=pk)
    form3 = Form3Form(request.POST or None ,request.FILES or None, instance=listem)
    if form3.is_valid():
        form3.save()
        return redirect('form3_view')
    context = {'form3': form3}
    return render(request, 'Form3/create.html', context)


@login_required(login_url=login_view)
def download(request , pk):
    listem = get_object_or_404(Form3Model , id=pk)
    file_path = listem.dosya.path
    file_name = str(listem.dosya)

    fh = open(file_path , 'rb')
    mime_type , _ = mimetypes.guess_type(file_path)
    response = HttpResponse(fh , content_type=mime_type)
    response['Content-Disposition'] = f"attachment; filename={file_name}"
    return response

@login_required(login_url=login_view)
def create_malzeme(request,form3):
    malzeme_tedarik=MalzemeForm(request.POST or None)
    context={'malzeme_tedarik':malzeme_tedarik}
    if request.method=='POST' and malzeme_tedarik.is_valid():
        b=malzeme_tedarik.save(commit=False)
        b.Form333=Form3.objects.get(id=form3)
        b.save()
    return render(request,'Form3/MalzemeTedarik.html',context)

@login_required(login_url=login_view)
def malzeme(request,form3):
    malzemeler=Malzeme.objects.filter(Form333=form3)
    context={'malzemeler':malzemeler}
    return render(request,'Form3/malzemeview.html',context)


