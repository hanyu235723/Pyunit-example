

class A:
    class B:
        class C:
            def me(self):
                print(self.__module__)
                print(type(self).__name__)
                print(type(self).__qualname__)
                print(repr(self))

c=A.B.C()
c.me()