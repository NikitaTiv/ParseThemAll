from django.http import HttpRequest, HttpResponse


def upload_image(request: HttpRequest) -> HttpResponse:
    return HttpResponse('Upload image page')
