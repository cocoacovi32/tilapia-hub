from django.http import HttpResponse

def test_notifications(request):
    return HttpResponse("Notifications app working!")
