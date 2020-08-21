
from django.shortcuts import render , redirect , get_object_or_404 , HttpResponseRedirect , HttpResponse
from .forms import FirmalarForm
from .models import Firmalar




def form6_firmalar(request):
    if request.user.is_staff or request.user.is_superuser:
        listele = Firmalar.objects.all().order_by('pk')
    return render(request,'Firmalar/Firmalar.html',{'listele':listele})

def form6_create(request):
    firma=FirmalarForm(request.POST or None)

    context = {'firma': firma}
    if request.method == "POST":
        if firma.is_valid():
            a=firma.save(commit=False)
            a.Olusturan=request.user
            a.save()
            return redirect('Firmalar6')
    return render(request, 'Firmalar/create.html', context)




def form6_update(request , pk):
    listele = get_object_or_404(Firmalar , id=pk)
    firma = FirmalarForm(request.POST or None, instance=listele)
    if firma.is_valid():
        firma.save()
        return redirect('Firmalar6')
    context = {'firma': firma}
    return render(request , 'Firmalar/create.html' , context)

def form6_delete(request , pk):
    listele = Firmalar.objects.get(id=pk)
    listele.delete()
    context = {'listele': listele}
    return redirect('Firmalar6')