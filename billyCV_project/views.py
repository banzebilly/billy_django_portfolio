
from pagesApp.models import Work
from django.shortcuts import render, get_object_or_404

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'pages/about.html')
def contact(request):
    return render(request, 'pages/contact.html')


def work(request):
    works = Work.objects.all()

    context = {
        'works': works
    }

    return render(request, 'pages/projects.html', context)




def work_detail(request, pk):
    work = get_object_or_404(Work, pk=pk)
    context = {
        'work': work
    }
    return render(request, 'pages/work_detail.html', context)  
