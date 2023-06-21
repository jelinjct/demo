from shop.models import category

def menu_links(request):
    links=category.objects.all()
    return{'links':links}
# normal view ne otta html page lreke connect cheyavu
# but from here globaly ethu file lekium connect akam