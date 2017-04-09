# coding=utf-8
from django.shortcuts import render,HttpResponse
from .models import UserMessage
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt,csrf_protect #Add this

@csrf_exempt
def getform(request):
    # # objects 是数据表管理器
    # # .all() 方法返回指定 model 在数据库中所对应的表中的所有数据
    # all_messages = UserMessage.objects.all()
    #
    # # 该方法删除多条记录
    # all_messages.delete()
    #
    message = None
    # .filter() 方法，设置字段的过滤条件
    all_messages = UserMessage.objects. filter(name='张校长')
    if all_messages:
        message = all_messages[0]

    return render(request, 'message_form.html', {
        "my_message": message,
    })

        # for message in all_messages:
    #
    #     # 删除单单条记录
    #     message.delete()
    #     print(message.name)

    # if request.method == 'POST':
    #     # 当取不到 name 的时候，默认为 ''
    #     name = request.POST.get('name', '')
    #     message = request.POST.get('message', '')
    #     address = request.POST.get('address', '')
    #     email = request.POST.get('email', '')
    #     user_message = UserMessage()
    #     user_message.name = name
    #     user_message.message = message
    #     user_message.address = address
    #     user_message.email = email
    #     user_message.object_id = "hello3"
    #     user_message.save()



