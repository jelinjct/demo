from django.shortcuts import render
from django.http import HttpResponse
from shop.models import product
from django.db.models import Q
# Create your views here.
def searchresult(request):
    products=None
    query=None
    if request.method=="POST":
                query=request.POST.get('q')
                if query:
                    products=product.objects.filter(Q(name__icontains=query)| Q(description__icontains=query))
    return render(request,'search.html',{'query':query,'products':products})


# products=None   #searchil pretyakich keyword koduthilel products none kanikan
# if query:  # query il aanu ipo searxhing keyword ullath so query nthelum undel matarm below step
#product table name
# Q(name__icontains=query) means kodukunna keyword ipo ullath queryil ath product table aanu db
#athil kure details inde athinath etinodelum ee query = anonu nokunnu or descriptionil