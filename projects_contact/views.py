

from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm

def contact(request):
    form = ContactForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Thank you for your message. I’m Banze Billy, a  software engineer. I appreciate your interest and will review your inquiry carefully. You can expect a response from me shortly."
            )

          
          
            return redirect('contact')
        else:
            messages.error(
                request,
                "There was a problem submitting your message. Please correct the errors below."
            )

    context = {
        'form': form
    }
    return render(request, 'pages/contact.html', context)




