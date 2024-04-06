from django.db import models


class Student_type(models.Choices):
    BACHELOR = 'Bachelor'
    MASTER = 'Master'
