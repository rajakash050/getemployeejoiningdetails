# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

# -*- coding: utf-8 -*-


from django.db import models

class Member(models.Model):
    member_name = models.CharField(max_length=100)
    member_desc = models.CharField(max_length=100)
    memberid = models.IntegerField(max_length=11)
    # end_date = models.DateTimeField
    # start_date = models.DateTimeField

    def __str__(self):
        return self.member_name
