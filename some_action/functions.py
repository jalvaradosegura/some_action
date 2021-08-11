def yell(text):
    return text.upper() + '!'


print(yell('Im yelling'))
bark = yell
print(bark('Woof'))
del yell
print(bark('Woof'))
print(bark.__name__)
print(yell('Im yelling'))
