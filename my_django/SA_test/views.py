from django.shortcuts import render
from django.http import HttpResponse
from dwebsocket.decorators import accept_websocket,require_websocket
from SA_test.models import computer_info,computer
import time

# Create your views here.


def index(request):
#     list_s = client_info.objects.all()
#     print(list_s)
    return render(request,'index.html')

# def add(request):
#     a = request.GET['a']
#     b = request.GET['b']
#     c = int(a)+int(b)
#     return HttpResponse(str(c))

def add2(request):
    # test1 = client_info(client_id = 11,cpu_info=0.23)
    # test1.save()
    return render(request,'add2.html')

@accept_websocket
def echo(request):
    if not request.is_websocket():#判断是不是websocket连接
        try:#如果是普通的http方法
            message = request.GET['message']
            return HttpResponse(message)
        except:
            return render(request,'index.html')
    else:
        while True:
                list_s_1 = computer_info.objects.filter(computer_id_id = 1).last()
                list_s_2 = computer_info.objects.filter(computer_id_id = 2).last()
                list_s_3 = computer_info.objects.filter(computer_id_id = 3).last()
                # print(list_s)
                request.websocket.send(str(list_s_1.cpu_info)+' '+ str(list_s_1.computer_id_id)+' '+
                str(list_s_2.cpu_info)+' '+ str(list_s_2.computer_id_id)+' '+
                str(list_s_3.cpu_info)+' '+ str(list_s_3.computer_id_id)
                )#发送消息到客户端
                time.sleep(1)