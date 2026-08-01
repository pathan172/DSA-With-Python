# recursion topic #head and tail recursion are two different approaches to implementing recursive functions in programming
#print anzar 4 times using head recursion
def func(count):
    if count == 4:
        return

    func(count + 1)   # Pehle recursive call
    print("anzar")     # Baad me print

func(0)