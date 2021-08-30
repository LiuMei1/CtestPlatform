from django.shortcuts import render
from ctest.models import Interface
from django.http import HttpResponseRedirect,HttpResponse
import os
# Create your views here.

#用例的增删改差
def case_index(request):
    return render(request, 'base/case/index.html')

def case_add(request):
    if request.method == 'GET':
        return render(request,'base/case/add.html')


#ctest接口的增删改查
def interface_index(request):
    if request.method == 'GET':
        if_list = Interface.objects.all()
        return render(request,'base/interface/index_new.html',{"if_list":if_list})

def interface_add(request):
    if request.method == 'GET':
        return render(request,'base/interface/add_new.html')

    if request.method == 'POST':
        if_id = request.POST.get('if_id', False)
        if_name = request.POST['if_name']
        description = request.POST['description']
        request_body_data = request.POST['request_body_data']
        response_body_data = request.POST['response_body_data']

        if if_id:
            Interface.objects.filter(if_id=if_id).update(if_name=if_name, description=description,
                                                         request_body_param=request_body_data,
                                                         response_body_param=response_body_data)
        else:
            interface = Interface(if_name=if_name, description=description, request_body_param=request_body_data,
                                  response_body_param=response_body_data)
            interface.save()
        return HttpResponseRedirect("/ctest/interface")


def interface_del(request):
    if request.method == 'POST':
        if_id = request.POST['if_id']
        Interface.objects.get(if_id=if_id).delete()
        return HttpResponseRedirect("/ctest/interface")

def interface_exe(request):
    if request.method == 'POST':
        if_id = request.POST['if_id']
        request_body_datas = Interface.objects.values('request_body_param').filter(if_id=if_id)
        for obj in request_body_datas:
            request_body_data = obj['request_body_param']
            tmp = tmp = os.popen(request_body_data).readlines()
            Interface.objects.filter(if_id=if_id).update(response_body_param=tmp)
        return HttpResponseRedirect("/ctest/interface")


