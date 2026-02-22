from django.shortcuts import render

# Create your views here.
def first_view(request):
    obj={
        'name':'girish',
        'college':'MITE Mangalore'
    }
    return render(request,'context.html',obj)
