from django.shortcuts import render


from django.shortcuts import render
from django.core.mail import send_mail

from sendmail.settings import EMAIL_HOST_USER
from . import forms


# Create your views here.
def index(request):
    sub = forms.Subscribe()
    return render(request, 'subscribe/index.html', {'form': sub})


def subscribe(request):
    sub = forms.Subscribe()

    if request.method == 'POST':
        sub = forms.Subscribe(request.POST)
        subject = 'Test auto send mail'
        message = 'Hello world!!!'
        recipient = str(sub['Email'].value())
        send_mail(subject=subject, message=message, from_email=EMAIL_HOST_USER,
                  recipient_list=[recipient], fail_silently=False)
        return render(request, 'subscribe/success.html', {'recipient': recipient})

    return render(request, 'subscribe/index.html', {'form': sub})
