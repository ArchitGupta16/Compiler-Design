dic = {}
word = input("Enter variables of the grammar(separated with commas):")
var = word.split(",")
rule = [] * len(var)

terminals = ['a', 'b', 'c', 'd', 'e']

for i in range(len(var)):
    rules = input(f"Enter rules of variable {var[i]} separated with /:")
    dic[var[i]] = rules.split("/")

print(dic)


def first(prod, f):
    if prod == "Epsilon":
        f.append("\u03B5")
    if prod[0] in terminals:
        f.append(prod[0])
    if prod[0] in var:
        if len(dic[prod[0]]) > 1:
            r = dic[prod[0]]
            for x in r:
                if x in terminals:
                    f.append(x)
                if x == "Epsilon":
                    if len(prod) == 1:
                        f.append("\u03B5")
                    else:
                        if prod[1] in var:
                            first(dic[prod[1]], f)
                        else:
                            f.append(prod[1])

                if x in var:
                    first(dic[x], f)
        else:
            z = dic[prod[0]][0]
            print(z[0])
            if z == "Epsilon":
                f.append("\u03B5")
            if z[0] in terminals:
                f.append(z[0])
            else:
                first(dic[prod[0]], f)

    return f


arr = []
temp = []

for i in var:
    x = []
    for j in dic[i]:
        temp.append(first(j, x))
    if temp not in arr:
        arr.append(temp)
    temp = []
arr[1].pop()

print("First:")
for i in arr:
    print(i)
