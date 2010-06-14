from django.contrib.auth.models import User
import csv

def gen(path='usernames'):
    freader = csv.reader(open(path))
    for record in freader:
        u = User.objects.create_user(record[4], record[3], record[4])
        u.first_name=record[2]
        u.last_name=record[1]
        u.save()
