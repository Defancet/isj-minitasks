# minitask 5
default_qentry = ('How do you feel today?', ['sad','happy','angry'])

funcqpool = [('If return statement is not used inside the function, the function will return:',
          ['0',
           'None object',
           'an arbitrary integer',
           'Error! Functions in Python must have a return statement.'
          ]),
         ('Which of the following function calls can be used to invoke function definition:\n def test(a, b, c, d):?',
          ['test(1, 2, 3, 4)',
           'test(a = 1, 2, 3, 4)',
           'test(a = 1, b = 2, c = 3, 4)',
           'test(a = 1, b = 2, c = 3, d = 4)',
           'test(1, 2, 3, d = 4)])'])
        ]
funcquiz1 = [('Which of the following keywords marks the beginning of the function block?',
         ['func',
          'define',
          'def',
          'func',
         ])]

def add_question(x, pool, *quiz):
    if not quiz:
        return [default_qentry, pool[x]]
    else:
        try:
            quiz[0].append(pool[x])
        except:
            return quiz[0]
        else:
            return quiz[0]

print(add_question(0, funcqpool, funcquiz1))
print(funcquiz1)
print(add_question(0, funcqpool))
