import Stack as s
class thuchanhStack:
    print('===========Demo Stack============')
    s = s.ArrayStack()

    s.push(5)
    s.push(3)
    print('Stack length: ',s.len())
    print('s: ',s)

    print('Pop: ',s.pop())
    print('Is stack empty?: ',s.is_empty())
    print('Pop: ',s.pop())
    print('Is stack empty?: ',s.is_empty())
    print('s: ',s)
    s.push(7)
    s.push(9)
    print('Top element in stack: ',s.top())
    s.push(4)
    s.push(6)
    print('s: ',s)