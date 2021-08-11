import functools


def bold(func):
    @functools.wraps(func)
    def wrapper(text):
        return f'<b>{func(text)}</b>'

    return wrapper


def italic(func):
    @functools.wraps(func)
    def wrapper(text):
        return f'<i>{func(text)}</i>'

    return wrapper


@bold
@italic
def text_with_exclamation(text):
    '''
    This is a cool docstring
    '''
    return text + '!'


def transform_args_to_positive_number(func):
    def wrapper(*args):
        return func(*[abs(x) for x in args])

    return wrapper


@transform_args_to_positive_number
def i_can_sum_n_arguments(a, b, c, d, e):
    return sum([a, b, c, d, e])


print(text_with_exclamation('hi'))
print(text_with_exclamation.__name__)
print(text_with_exclamation.__doc__)
print('-------------')
print(i_can_sum_n_arguments(1, 2, 3, 3, 3))
print(i_can_sum_n_arguments(1, -2, 3, 3, 3))
