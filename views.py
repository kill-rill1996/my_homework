from wavy import render


def decode_value(val):
    val_b = bytes(val.replace('%', '=').replace("+", " "), 'UTF-8')
    val_decode_str = quopri.decodestring(val_b)
    return val_decode_str.decode('UTF-8')


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
        print(f'Вы получили сообщение от {email} на тему "{title}", текст сообщения: {text}')
        return '200 OK', render('contact.html')
    else:
        return '200 OK', render('contact.html')


"""
def decode_value(val):
    val_b = bytes(val.replace('%', '=').replace("+", " "), 'UTF-8')
    val_decode_str = quopri.decodestring(val_b)
    return val_decode_str.decode('UTF-8')
"""