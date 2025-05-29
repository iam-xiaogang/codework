# author xiaogang

from celery import shared_task
from .models import Host, HostPasswordHistory, HostStats, ComputerRoom
import random
import string
from datetime import date

import logging
logger = logging.getLogger(__name__)

def generate_password(length=12):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))



@shared_task
def rotate_host_passwords():
    logger.info('rotating host passwords')
    for host in Host.objects.all():
        new_password = generate_password()
        HostPasswordHistory.objects.create(
            host=host,
            password=host.root_password
        )

        host.root_password = new_password
        host.save()



@shared_task
def daily_host_statistics():
    logger.info('Daily host statistics')
    for room in ComputerRoom.objects.select_related("city"):
        count = room.hosts.count()
        HostStats.objects.create(
            city=room.city,
            computer_room=room,
            count=count,
            date=date.today()
        )
