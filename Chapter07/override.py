class A:
    def hello(self):
        print('class A says Hello')

class B(A):
    def hello(self):
        print('class B says Hello')

b = B()
b.hello()
