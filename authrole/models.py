from django.db import models
from django.contrib.auth.models import User as AuthUser
from django.contrib.auth.models import Group as AuthGroup

# Create your models here.
class AuthUserGroupsManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().annotate(user_count=models.Count('AuthUser'),
                                               group_count=models.Count('AuthGroup'))
class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)