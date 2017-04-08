from django.shortcuts import render,redirect

# Create your views here.
def index(request):
    return render(request, 'vinmyMVC/index.html')

def show(request):
    print(request.method)
    return render(request, 'vinmyMVC/show_users.html')

def create(request):
    print(request.method)
    if request.method == "POST": #here we have to choose POST OR GET
        print ('*'*50)
        print (request.POST) #case sensitive
        print ('*'*50)
        request.session['name'] = request.POST['first_name']
        return redirect('/')
    else:
        return redirect('/')
