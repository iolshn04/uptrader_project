from django import template

register = template.Library()


@register.simple_tag
def draw_menu(menu):
    if menu:
        if menu.parent:
            parent_menu = menu.parent
            parent_menu.is_expanded = True

        menu_items = menu.menu_set.all().order_by('id')
        return render_menu(menu_items)


def render_menu(menu_items):
    result = ''
    for menu_item in menu_items:
        result += f'<li><a href="{menu_item.url}">{menu_item.name}</a>'

        if hasattr(menu_item, 'is_expanded'):
            result += '<ul>'
            sub_menu_items = menu_item.menu_set.all().order_by('id')
            result += render_menu(sub_menu_items)
            result += '</ul>'

        result += '</li>'
    return result