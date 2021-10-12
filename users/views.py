from django.views import View
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
import json


# Create your views here.
class UserView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self,request,id=0):
        if (id>0):
            products=list(User.objects.filter(id=id).values())
            if len(products) > 0:
                product=products[0]
                data = {'message': "Success", 'users': product}
            else:
                data = {'message': "User not found"}
            return JsonResponse(data)
        else:    
            products=list(User.objects.values())
            if len(products) > 0:
                data = {'message': "Success", 'users': products}
            else:
                data = {'message': "User not found"}
            return JsonResponse(data)