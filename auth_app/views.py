from django.http import HttpResponse

def test_auth(request):
    return HttpResponse("Auth app working!")
