from tastypie.resources import ModelResource
from core.models import FSUser
from tastypie.authorization import Authorization


class UserResource(ModelResource):

    class Meta:
        queryset = FSUser.objects.all()
        resource_name = 'user'
        authorization = Authorization()
        excludes = ['password']
