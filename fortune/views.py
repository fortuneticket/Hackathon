from django.shortcuts import get_object_or_404, render, redirect
from .models import Fortune, User
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string


def lottery(request):
    fortune = Fortune.objects
    return render(request, 'lottery.html', {'fortune': fortune})


def enroll(request):
    email = request.GET.get('email')
    user = User(fortune_id=1, email=email)
    user.save()

    return redirect('lottery')


def sendEmail(request):

    msg_plain = render_to_string('email.txt')
    success_html = render_to_string('email.html')
    fail_html = render_to_string('failemail.html')

    id = request.GET.get('id')

    fortune = Fortune.objects.get(pk=id)
    print(fortune.seat)

    send_mail(
        '🥠포춘 티켓 응모 결과',
        msg_plain,
        settings.EMAIL_HOST_USER,
        ['minjony1014@gmail.com'],
        html_message=success_html,
        fail_silently=False
    )

    send_mail(
        '🥠포춘 티켓 응모 결과',
        msg_plain,
        settings.EMAIL_HOST_USER,
        ['jmtkdsh@gmail.com'],
        html_message=fail_html,
        fail_silently=False
    )

    return redirect('lottery')
