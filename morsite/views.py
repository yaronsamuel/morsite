from django.http import HttpResponse
from django.template import RequestContext, loader
from zinnia.models.entry import Entry

FEATURED_NUMBER = 3

def homepage(request):
    
    template = loader.get_template('zinnia/my_entry_list.html')
    context = RequestContext(request, {
        'object_list': Entry.published.filter(featured=True)[:FEATURED_NUMBER],
        'homepage' : True , 
    })
    return HttpResponse(template.render(context))
    

def kissesPage(request):
    
    template = loader.get_template('morsite/kisses.html')
    context = RequestContext(request, {

    })
    return HttpResponse(template.render(context))
     

     
def coursePage(request):
    
    template = loader.get_template('morsite/course.html')
    context = RequestContext(request, {

    })
    return HttpResponse(template.render(context))

def aboutPage(request):
    
    template = loader.get_template('morsite/about.html')
    context = RequestContext(request, {

    })
    return HttpResponse(template.render(context))
    

def Page500(request):
    
    template = loader.get_template('morsite/500.shtml')
    # lst = ['%s %s' %(k,v) for k,v in request.items()]
    
    context = RequestContext(request, {
    'content_list' :[str(request)] ,

    })
    return HttpResponse(template.render(context))