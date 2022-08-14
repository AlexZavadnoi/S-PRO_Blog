from django.db import models


# class Account(AbstractUser):
#     birth_date = models.DateField(null=True, blank=True)
#     country = models.ForeignKey('Country', on_delete=models.SET_NULL, null=True)
#     city = models.ForeignKey('City', on_delete=models.SET_NULL, null=True)
#     subscribers = models.ManyToManyField('self', related_name='subscriptions')
#
#     def __str__(self):
#         return self.get_full_name()
