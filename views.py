from wavy import render
from wavy import Application


def main_view(request):
    key = request.get('key', None)
    return '200 OK', render('index.html', key=key)


def about_view(request):
    return '200 OK', "About"


def contact_view(request):
    if request['method'] == 'POST':
        data = request['data']
        title = data['title']
        text = data['text']
        email = data['email']
        print(f'Вы получили сообщение от {Application.decode_value(email)} на тему '
              f'"{Application.decode_value(title)}", текст сообщения: {Application.decode_value(text)}')
        return '200 OK', render('contact.html')
    else:
        return '200 OK', render('contact.html')
