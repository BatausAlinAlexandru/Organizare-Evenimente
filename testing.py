def space(lenght):
    vec = []
    for i in range(50):
        vec += " "
    for i in range(lenght):
        vec.pop()

    string = ""
    for i in vec:
        string += i
    return string


print("ID: 12", space(2), "NAME: Bataus Alin-Alexandru", space(21), "DESC: Nu stiu ce naiba sa pun aici dar merge" )
print("ID: 234232", space(6), "NAME: PAVEN Andrei", space(12), "DESC: Nu stiu ce naiba sa pun aici dar merge" )