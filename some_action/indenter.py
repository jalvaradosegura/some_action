class Indenter:
    def __init__(self):
        self.level = 0

    def __enter__(self):
        self.level += 1
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        self.level -= 1

    def print(self, text):
        print(' ' * self.level + text)


with Indenter() as indenter:
    indenter.print('hello')
    with indenter:
        indenter.print('Im deeper')
        with indenter:
            indenter.print("I'm even deeper")
        indenter.print('go back by 1')
