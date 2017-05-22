from django.shortcuts import render, HttpResponse, redirect

def index(request):
    context= {'languages' : ['Javascript', 'Python', 'Ruby', 'C#']}
    return render (request, 'survey_app/index.html', context)

def process(request):
    print request.method
    if request.method != "POST":
        return redirect('/')

    if 'count' in request.session:
        request.session['count'] += 1
    else:
        request.session['count']= 1

    context = {
        'survey': { 'name': request.POST['name'],\
                    'language': request.POST['language'],\
                    'location':request.POST['location'],\
                    'comment':request.POST['comment']}
                    }


    return render (request, 'survey_app/done.html',context)





# Create your views here
