from django.db import models


class Status(models.Choices):
        NEW = 'New'
        MOD = 'Moderation'
        CONFIRMED = 'Confirmed'
        CANCELED = 'Canceled'


class Sponsor_type(models.Choices):
        PHYICAL_PERSON = 'Physical_person'
        LEGAL_ENTITY = 'Legal_entity'