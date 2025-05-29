from django.db import models

class City(models.Model):  # 建议名称更简洁
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class ComputerRoom(models.Model):  # 建议更明确
    name = models.CharField(max_length=50)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='computer_rooms')

    def __str__(self):
        return f"{self.city.name} - {self.name}"


class Host(models.Model):
    hostname = models.CharField(max_length=100, unique=True)
    ip_address = models.GenericIPAddressField(protocol='both')
    computer_room = models.ForeignKey(ComputerRoom, on_delete=models.CASCADE, related_name='hosts')
    root_password = models.CharField(max_length=128)
    last_password_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.hostname


class HostPasswordHistory(models.Model):
    host = models.ForeignKey(Host, on_delete=models.CASCADE, related_name='password_history')
    password = models.CharField(max_length=128)
    changed_at = models.DateTimeField(auto_now_add=True)


class HostStats(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    computer_room = models.ForeignKey(ComputerRoom, on_delete=models.CASCADE)
    count = models.IntegerField()
    date = models.DateField(auto_now_add=True)
