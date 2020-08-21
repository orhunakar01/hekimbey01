from django.contrib.auth.decorators import permission_required , login_required
from django.shortcuts import render , redirect , get_object_or_404,HttpResponseRedirect , HttpResponse
from form3.models import Form3
from form3.forms import Form3Form
from django.db.models import Q
import mimetypes
from form_1.models import Form1
from form2.models import Form2
from form4.models import Form4
from giris.views import login_view
from .models import Form5
from .forms import Form5Form
from datetime import date , datetime




@login_required(login_url=login_view)
def form5_view(request):
    if request.user.is_superuser or request.user.is_staff:
        listem = Form5.objects.all()
    else:
        listem = Form5.objects.all().filter(Olusturan=request.user)

    return render(request , 'Form5/Form5.html', {'listem': listem})


@login_required(login_url=login_view)
def create(request,form1):
    form5=Form5Form(request.POST or None, request.FILES)

    context = {'form5': form5}
    if request.method == "POST":
        if form5.is_valid():
            a=form5.save(commit=False)
            a.Form55 = Form4.objects.get(Form44=form1)
            a.Olusturan = request.user
            form5.save()
            return redirect('form5_view')
    return render(request, 'Form5/create.html', context)


@login_required(login_url=login_view)
@permission_required('form5.delete_form5',login_url=form5_view)
def delete(request , pk):
    listem = Form5.objects.get(id=pk)
    listem.delete()
    context = {'listem': listem}
    return redirect('form5_view')

@login_required(login_url=login_view)
def detail(request,pk):
    listem = get_object_or_404(Form5, id=pk)
    context = {'listem': listem}
    return render(request , 'Form5/detail.html', context)


@login_required(login_url=login_view)
@permission_required('form5.change_form5',login_url=form5_view)
def update(request,pk):
    listem = get_object_or_404(Form5 , id=pk)
    form5 = Form5Form(request.POST or None ,request.FILES or None, instance=listem)
    if form5.is_valid():
        form5.save()
        return redirect('form5_view')
    context = {'form5': form5}
    return render(request, 'Form5/create.html', context)

@login_required(login_url=login_view)
def download(request , pk):
    listem = get_object_or_404(Form5, id=pk)
    file_path = listem.dosya.path
    file_name = str(listem.dosya)
    fh = open(file_path, 'rb')
    mime_type, _ = mimetypes.guess_type(file_path)
    response = HttpResponse(fh , content_type=mime_type)
    response['Content-Disposition'] = f"attachment; filename={file_name}"
    return response


