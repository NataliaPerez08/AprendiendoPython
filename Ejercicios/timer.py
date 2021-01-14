from threading import Timer


def hello():
       print("hello, world")

tiempo = int(input("Tiempo: "))
t = Timer(tiempo, hello)
t.start() # after 30 seconds, "hello, world" will be printed
