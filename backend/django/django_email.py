from django.core.mail import send_mail

def send_welcome_email(request):
    send_mail(
        'Welcome',
        'Thanks for joining us!',
        'from@example.com',
        ['to@example.com'],
        fail_silently=False,
    )
    return HttpResponse('Email sent.')
