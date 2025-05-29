# author xiaogang

from celery import shared_task
from .models import Host, HostPasswordHistory, HostStats, ComputerRoom
import random
import string
from django.db.models import Count
import logging
logger = logging.getLogger(__name__)

def generate_password(length=12):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))


@shared_task
def rotate_host_passwords():
    logger.info('rotating host passwords')
    hosts = Host.objects.only('id', 'root_password')
    updated_hosts = []
    histories = []
    for host in hosts:
        new_password = generate_password()
        histories.append(
            HostPasswordHistory(
                host=host,
                password=host.root_password
            )
        )
        host.root_password = new_password
        updated_hosts.append(host)
    HostPasswordHistory.objects.bulk_create(histories)
    Host.objects.bulk_update(updated_hosts, ['root_password'])

@shared_task
def daily_host_statistics():
    logger.info('Daily host statistics')
    stats = []
    rooms = ComputerRoom.objects.select_related("city").annotate(host_count=Count("hosts"))
    logger.info('Room count: {}'.format(len(rooms)))
    for room in rooms:
        stats.append(HostStats(
            city=room.city,
            computer_room=room,
            count=room.host_count
        ))
    HostStats.objects.bulk_create(stats)
