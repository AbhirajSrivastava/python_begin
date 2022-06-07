from re import X


def square():
    print("taking input of first function")
    x=int(input("enter a number to square"))
    gevent.sleep(0)
    xy=x*x
    print("square is",xy)

    def cube():
    print("taking input of first function")
    x=int(input("enter a number to cube"))
    gevent.sleep(0)
    yx=y*y*y
    print("cube is",yx)

    gevent.joinall([
        gevent.spwan(square),
        gevent.spwan(cube),
    ])