def branch(size, t):
    t.forward(size)
    for i in range(3):
        t.left(45)
        t.forward(size)
        t.backward(size)
        t.right(90)
        t.forward(size)
        t.backward(size)
        t.left(45)
        t.forward(size)
    t.backward(size * 4)


def snowflake(size, t):
    for i in range(8):
        branch(size, t)
        t.left(45)
