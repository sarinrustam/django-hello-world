from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from shop.models import Category, Course
from .auth import CustomAuth


class CategoryResource(ModelResource):
    class Meta:
        queryset = Category.objects.all()
        resource_name = 'categories'
        allowed_methods = ['get']


class CourseResource(ModelResource):
    class Meta:
        queryset = Course.objects.all()
        resource_name = 'courses'
        allowed_methods = ['post', 'delete', 'get']
        authentication = CustomAuth()
        authorization = Authorization()