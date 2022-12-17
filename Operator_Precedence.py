d=[]
dic = {}
word = input("Enter variables of the grammar(separated with commas):")
var = word.split(",")
terminals = ["+","-","$","id"]
for i in range(len(var)):
    gram_rules = input(f"Enter rules of variable {var[i]} separated with /:")
    dic[var[i]] = gram_rules.split("/")
print(dic)
# dic = {'E': ['S+E','S'] , 'S':['S-E','id']}
p = [dic[i] for i in dic]

boolean = False
print(p)
for i in p:
    for j in i:
        if j == "\u03B5":
            boolean = True
            print("hi")
        if len(j)>=2:
            if j[0].isupper() and j[1].isupper():
                boolean = True

if boolean == False:
    x = []
    y = {}
    op = []
    op.append("id")
    for key,value in dic.items():
        for j in range(len(value)):
            if key == value[j][0]:
                y[value[j][1]] = "l"
                x.append("l")
                op.append(value[j][1])
            if key == value[j][-1]:
                y[value[j][1]] = "r"
                x.append("r")
                op.append(value[j][1])

    print("Associativity:",x)
    op.append("$")
    print("Operator precedence",op)

    arr = [["" for i in range(len(terminals))] for j in range(len(terminals))]
    data ={}
    keys = terminals
    values = arr
    data = dict(zip(keys, values))
    print(data)

    def compare(a,b):
        if a==b=="id" or a==b=="$":
            return None
        if a!=b:
            if op.index(a)<op.index(b):
                return "<"
            else:
                return ">"
        if a==b:
            if y[a] == "r":
                return "<"
            else:
                return ">"

    g = []
    for key,value in data.items():
        x = key
        l = []
        l.append(x)
        for i in terminals:
            
            l.append(compare(x,i))
        data[x] = l
        g.append(l)
    print(g)

    terminals.insert(0,"")
    g.insert(0,terminals)
    from tabulate import tabulate
    print(tabulate(g,tablefmt="grid"))

else:
    print("Not operator Grammar!")
