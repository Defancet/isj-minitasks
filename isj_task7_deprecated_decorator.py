#minitask 7

def deprecated(func):
    def some_new_function(x, y):
        print("Call to deprecated function: " + func.__name__)
        print(func(x, y))
        return
    return some_new_function


@deprecated
def some_old_function(x, y):
    return x + y

some_old_function(1,2)

# should write:
# Call to deprecated function: some_old_function
# 3
