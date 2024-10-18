data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

def calculate_structure_sum(a):
    sum=0
    if type(a)==str:
        sum += len(a)
    elif type(a)==int:
        sum += a
    elif type(a)==dict:
        for sk, value in (a.items()):
            sum += len(sk)
            sum += value
    else:
        for i in (a):
            if type(i)==int:
                sum+=i
            elif type(i)==str:
                sum+=len(i)
            else:
                sum+=calculate_structure_sum(i)
               # print(b)
    return sum

result=calculate_structure_sum(data_structure)
print(result)
