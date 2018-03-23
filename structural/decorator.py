from functools import wraps


def make_blink(func):
    """Defines the decorator"""

    # This makes the decorator transparent in terms of name and docstring
    @wraps(func)
    def wrap_with_blink_tag():
        text = func()
        return f'<blink>{text}</blink>'

    return wrap_with_blink_tag


@make_blink
def hello_world():
    """Returns Hello World!"""
    return 'Hello World!'


print(hello_world())
print(hello_world.__name__)
print(hello_world.__doc__)
