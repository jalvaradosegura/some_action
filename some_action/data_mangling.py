class Test:
    def __init__(self):
        self.foo = 'hi'
        self._bar = 'hey'
        self.__baz = 'hello'


class Test2(Test):
    def __init__(self):
        super().__init__()
        self.foo = 'hi'
        self._bar = 'hey'
        self.__baz = 'hello 2'


test = Test()
print(dir(test))
test = Test2()
print(dir(test))
print(test._Test__baz)
print(test._Test2__baz)
