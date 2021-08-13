class BaseValidationError(ValueError):
    pass


class NameTooShort(BaseValidationError):
    pass


class NameTooLong(BaseValidationError):
    pass


class NameTooCute(BaseValidationError):
    pass


def validate(text):
    if len(text) < 3:
        raise NameTooShort('name is too short')
    elif len(text) > 10:
        raise NameTooLong('name is too long')
    elif text == 'puppy':
        raise NameTooCute('name is too cute')


try:
    text = 'hi'
    validate(text)
except BaseValidationError as err:
    print(f'There was some error when calling: validate("{text}") -> {err}')

try:
    text = 'This is a long text'
    validate(text)
except BaseValidationError as err:
    print(f'There was some error when calling: validate("{text}") -> {err}')

try:
    text = 'puppy'
    validate(text)
except BaseValidationError as err:
    print(f'There was some error when calling: validate("{text}") -> {err}')
