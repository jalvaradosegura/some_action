# Emulating switch


def handle_a():
    pass


def handle_b():
    pass


def handle_default():
    pass


# We can turn this:
def check_cond(cond):
    if cond == 'cond_a':
        handle_a()
    elif cond == 'cond_b':
        handle_b()
    else:
        handle_default()


# Into this
def check_cond_with_dict(cond):
    some_dict = {
        'cond_a': handle_a,
        'cond_b': handle_b,
    }
    return some_dict.get(cond)


check_cond_with_dict('cond_a')()


# Cool case
def dispatch_dict(operator, x, y):
    return {
        'add': lambda: x + y,
        'sub': lambda: x + y,
        'mul': lambda: x * y,
        'div': lambda: x / y,
    }.get(operator, lambda: None)()


print(dispatch_dict('mul', 3, 4))
print(dispatch_dict('div', 100, 3))


# Learn Python with this weird awesome case
# print({True: 'yes', 1: 'no', 1.0: 'maybe'})
# print(True == 1 == 1.0)
# prints: {True: 'maybe'}
# Dictionaries treat keys to be equal if their __eq__ results say they are
# equal and if their hash value is equal
