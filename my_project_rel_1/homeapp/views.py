from django.shortcuts import render, HttpResponse

# Create your views here.
# def my_index_page(request):
#     return HttpResponse("Welcome")

# Create your views here.
def my_index_page(request):
    return render(request, 'newindex.html', {})
