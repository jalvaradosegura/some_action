class NameTooShort(ValueError):
    pass


def validate(text):
    if len(text) < 3:
        raise NameTooShort('name is too short')


validate('hi')
