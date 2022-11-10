from musicplatform.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from artists.models import Artist
from django.utils import timezone
from django.db.models import Max
from datetime import timedelta
from celery import shared_task

@shared_task
def congratulation_mail(id, name, release_date, cost):
    artist = Artist.objects.get(user_id = id)
    message = 'We would like to congratulate you on the addition of your new album. We wish you luck.'
    message = message + name + "released:" + release_date 
    message = message + " " + " the cost: " + str(cost)
    send_mail('Congrats ', message, EMAIL_HOST_USER,[artist.user.email], fail_silently=False)

@shared_task
def album_checking():
    for artist in Artist.objects.prefetch_related('album').all():
        latest = artist.album_set.aggregate(Max('release_date'))
        if(timezone.now() - timedelta(days=30) > latest["release_date__max"]):
            message = 'Artist: '
            message += artist.stageName + " "
            message += + "Because you haven't uploaded a new album in a while, your popularity on our platform is dwindling."
            send_mail('Important Note',message,'',[artist.user.email],fail_silently=False)
