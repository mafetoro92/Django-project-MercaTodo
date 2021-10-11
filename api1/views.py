from django.views import View
from django.utils.decorators import method_decorator
from .models import Products
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
import json


# Create your views here.
class ProductView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self,request,id=0):
        if (id>0):
            products=list(Products.objects.filter(id=id).values())
            if len(products) > 0:
                product=products[0]
                data = {'message': "Success", 'products': product}
            else:
                data = {'message': "Products not found"}
            return JsonResponse(data)
        else:    
            products=list(Products.objects.values())
            if len(products) > 0:
                data = {'message': "Success", 'products': products}
            else:
                data = {'message': "Products not found"}
            return JsonResponse(data)
    
    def post(self,request):
        # print(request.body)
        jd=json.loads(request.body)
        # print(jd)
        Products.objects.create(pro_name=jd['pro_name'], pro_provider=jd['pro_provider'], pro_existences=jd['pro_existences'], pro_date=jd['pro_date'], pro_description=jd['pro_description'],pro_category=jd['pro_category'])
        data = {'message': "Success"}
        return JsonResponse(data)

    def put(self,request,id):
        jd=json.loads(request.body)
        products=list(Products.objects.filter(id=id).values())
        if len(products) > 0:
            product=Products.objects.get(id=id)
            product.pro_name=jd['pro_name']
            product.pro_provider=jd['pro_provider']
            product.pro_existences=jd['pro_existences']
            product.pro_date=jd['pro_date']
            product.pro_description=jd['pro_description']
            product.pro_category=jd['pro_category']
            product.save()
            data = {'message': "Success"}
        else:
            data = {'message': "Products not found"}
        return JsonResponse(data)
    
    def delete(self,request,id):
        products=list(Products.objects.filter(id=id).values())
        if len(products) > 0:
            Products.objects.filter(id=id).delete()
            data = {'message': "Success"}
        else:
            data = {'message': "Products not found"}
        return JsonResponse(data)
