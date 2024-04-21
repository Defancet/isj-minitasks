# minitask 4

mcase = {'a': 10, 'b': 34, 'A': 7, 'Z': 3}
# wanted = {'a': 17, 'b': 34, 'z': 3}

wanted = {x.lower(): mcase.get(x.lower(), 0) + mcase.get(x.upper(), 0) for x in mcase}

print(wanted)
