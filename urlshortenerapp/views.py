from django.shortcuts import render, HttpResponse

topics = [
    {'id':1, 'title':'Shorten', 'body': 'This is URL Shortener'},
    {'id':2, 'title':'Shorten URL List', 'body': 'Shorten URL List'},
    {'id':3, 'title':'Analysis', 'body': 'Analysis'},
    
]

def HTMLTemplate(articleTag):
    global topics
    ol =''
    for topic in topics:
        ol += f'<li><a href="/read/{topic["id"]}">{topic["title"]}</a></li>'
    return f'''
    <html>
    <body>
        <h1><a href="/">URLShortener</a></h1>
        <ol>
            {ol}
        </ol>
        {articleTag}
        
    </body>
    </html>
    '''

# Create your views here.
def index(request):
    article = '''
    <h2>Welcome</h2>
    Hello!
    '''
    return HttpResponse(HTMLTemplate(article))



def read(request, id):
    global topics
    article = ''
    for topic in topics:
        if topic['id'] == int(id) :
            article = f'<h2>{topic["title"]}</h2>{topic["body"]}'
    return HttpResponse(HTMLTemplate(article))
    
def create(request):
    return HttpResponse('Create')