"""
Работа с шаблонами, паттерн INTERFACE
Используем шаблонизатор jinja2
"""
from jinja2 import FileSystemLoader
from jinja2.environment import Environment


def render(template_name, folder='templates', **kwargs):
    env = Environment()
    env.loader = FileSystemLoader(folder)
    tmpl = env.get_template(template_name)
    return tmpl.render(**kwargs)

