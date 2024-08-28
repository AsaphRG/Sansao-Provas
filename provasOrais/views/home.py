from django.shortcuts import render

# Create your views here.
def home(request):
    full_url = f"{request.scheme}://{request.get_host()}{request.get_full_path()}"
    context={}
    return render(request, 'provasOrais/templates/home.html', context=context)
