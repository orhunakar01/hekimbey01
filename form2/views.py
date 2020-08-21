from django.contrib.auth.decorators import permission_required , login_required
from django.shortcuts import render , redirect , get_object_or_404 , HttpResponseRedirect , HttpResponse
from form_1.models import Form1
from giris.views import login_view
from .forms import Form2Form
from form_1.forms import Form1Form
from .models import Form2 as Form2Model
from form_1.models import Form1
from django.db.models import Q
from django.urls import reverse
from form2.models import Form2
from form3.models import Form3

@login_required(login_url=login_view)
def form2_view(request):
    if request.user.is_staff or request.user.is_superuser:
        listeler = Form2Model.objects.all().order_by('Form22')
    else:
        listeler=Form2Model.objects.all().order_by('Form22').filter(Olusturan=request.user)


    """query = request.GET.get('q')
    if query:
        listeler = listeler.filter(
            Q(id=int(query)) |
            Q(Sorumlusu__icontains=query) |
            Q(Olusturan__username__icontains=query)
        ).distinct()"""
    return render(request , 'Form2/Form2.html' , {'listeler': listeler,'islemdeki':
                                                  [islemdeki.Form33 for islemdeki in Form3.objects.all() if islemdeki.Form33]
 })

@login_required(login_url=login_view)
def create_view(request,form1):
    form2=Form2Form(request.POST or None)

    context = {'form2': form2}
    if request.method == "POST":
        if form2.is_valid():
            a=form2.save(commit=False)
            a.Form22 = Form1.objects.get(pk=form1)
            a.Olusturan = request.user
            a.save()
            return redirect('form2_view')
    return render(request, 'Form2/create.html', context)


@login_required(login_url=login_view)
def detail(request,pk):
    liste = get_object_or_404(Form2Model , id=pk)
    context = {'liste': liste}
    return render(request , 'Form2/detail.html', context)


@login_required(login_url=login_view)
@permission_required('form2.delete_form2',login_url=form2_view)
def delete(request,pk):
    liste = Form2Model.objects.get(id=pk)
    liste.delete()
    context = {'liste': liste}
    return redirect('form2_view')

@login_required(login_url=login_view)
@permission_required('form2.change_form2',login_url=form2_view)
def update(request,pk):
    liste = get_object_or_404(Form2Model , id=pk)
    form2 = Form2Form(request.POST or None , instance=liste)
    if form2.is_valid():
        form2.save()
        return redirect('form2_view')
    context = {'form2': form2}
    return render(request, 'Form2/create.html', context)




"""def create_view(request):
    temlate_name="Form2/create.html"
    form_class=Form2Form
    if request.method == 'POST':
        form1 = Form1Form(request.POST or None)
        form2 = Form2Form(request.POST or None)
        if form1.is_valid() and form2.is_valid() and request.method=='POST':
            model1 = form1.save()
            model2 = form2.save(commit=False)
            model2.model1_one_to_one_field = model1
            form2.save()
            return redirect('form2_view')
    else:
            form1 = Form1Form()
            form2 = Form2Form()
    return render(request, 'Form2/create.html', {'form1':form1,'form2':form2})"""