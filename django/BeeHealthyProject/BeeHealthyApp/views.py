from django.shortcuts import render
from django.http import HttpResponse


def myview(request):
    context = {
        'message': 'Hello World!'
    }
    return render(request, 'base.html', context)
    
    
    # def HomeRegister(request):

    # # example of password requirements
    # if len(request.POST['password']) < 8:
    #     return redirect('posts:home')

    # if request.POST['password2'] == request.POST['password']:
    #     # print('password', request.POST['password'])
    #     # print('hashed password', make_password(request.POST['password']))

    #     user_model = CustomUser(username=request.POST['name'], password=make_password(request.POST['password']))
    #     user_model.save()
    # else:
    #     print("not match")

    # return redirect('posts:home')