from wavy import Application
import views

urlpatterns = {
    '/': views.main_view,
    '/about/': views.about_view,
    '/contact/': views.contact_view,
}


def secret_controller(request):
    # Пример Front controller
    request['key'] = '123123123'


front_controllers = [
    secret_controller
]

application = Application(urlpatterns, front_controllers)

