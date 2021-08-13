from abc import ABCMeta, abstractmethod


class Base(metaclass=ABCMeta):
    @abstractmethod
    def foo(self):
        pass

    @abstractmethod
    def bar(self):
        pass


class Concrete(Base):
    def foo(self):
        pass


class Concrete2(Base):
    def foo(self):
        pass

    def bar(self):
        pass


# This one will fail
concrete = Concrete()
# This one will not
concrete2 = Concrete2()
