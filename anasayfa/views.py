from django.contrib.auth.decorators import permission_required , login_required
from django.shortcuts import render , redirect , get_object_or_404 , HttpResponseRedirect , HttpResponse
from form_1.models import Form1
from form_1.forms import Form1Form
from giris.views import login_view

from .models import Anasayfa
from form5.models import Form5

@login_required(login_url=login_view)
@permission_required('anasayfa.view_anasayfa',login_url=Anasayfa)
def anasayfa(request):
    if request.user.is_staff or request.user.is_superuser:
        listeler = Form5.objects.all().filter(onay=True)
    return render(request,'Anasayfa/Anasayfa.html',{'listeler':listeler})
