from wavy import render


def main_view(request):
    key = request.get('key', None)
    return '200 OK', render('index.html', key=key)


def about_view(request):
    return '200 OK', "About"

