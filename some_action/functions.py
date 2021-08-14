def yell(text):
    return text.upper() + '!'


print(yell('Im yelling'))
bark = yell
print(bark('Woof'))
del yell
print(bark('Woof'))
print(bark.__name__)
# will fail because the fx got deleted
# print(yell('Im yelling'))
