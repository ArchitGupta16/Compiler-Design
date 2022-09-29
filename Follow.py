import random
import string


def Left_Recursive(G, V):
    for i in V:
        for j in G[i]:
            # print(j)
            if j[0] == i:
                x = j[1:]  # comparing to check the variable availability for left recursion
                a = random.choice(string.ascii_uppercase)
                while a in V:
                    a = random.choice(string.ascii_uppercase)  # the random allotment of a new variable
                G[a] = [x + a]  # appending new variable to the remaining part of the production
                V.append(a)  # adding the new symbol
                G[i].remove(j)  # removing the original symbol
                ly = G[i].copy()  # making a copy of remaining productions
                for k in ly:
                    if k[0] != j[0]:  # if it is not the variable that is in the iteration for checking of left
                        # recursion ,
                        # add it with the new symbol
                        G[i].extend([k + a])
                        G[i].remove(k)  # remove  the production after adding the new symbol
                    else:
                        x = k[1:]  # if it is the variable that is in the iteration for checking of left recursion,
                        # add the remaining of it with the new symbol
                        G[a].extend([x + a])  # creation of new production rule
                        G[i].remove(k)  # remove the production after adding the new symbol
                G[a].append('\u03B5')

    return G, V


def Left_Factoring():
    for i in V:
        for j in G[i]:
            x = []
            y = []
            z = []
            for k in range(len(G[i])):  # repeats until all the productions are parsed
                print(G[i][k][0])
                if j[0] == G[i][k][0]:  # matching the first letter with other production letters
                    x.append(k)  # storing the iteration value for loop inside the productions of a particular variable
                    y.extend([G[i][k][1:]])  # removing the first letter
                    z.extend([G[i][k]])  # copying the production as it is
            if len(x) > 1:
                a = random.choice(string.ascii_uppercase)
                while a in G:
                    a = random.choice(string.ascii_uppercase)  # allotment of the new variable randomly
                G[a] = y  # creating a new production rule derived from new variable and having the elements of list y
                w = []
                for k in G[i]:
                    if k not in z:  # if any production is remaining , add it to list w
                        w.extend([k])
                G[i] = w  # replacing the current value at the i'th key
                G[i].extend([j[0] + a])  # adding the new variable along with the first letter to the previous
                # value list of i'th key
                V.append(a)  # add the new variable


h = []
n = int(input("Enter the number of production rules:"))
for i in range(n):
    G = {}
    p = input(f"Enter the Production {i+1}:\n")
    l = p.split('=')
    l1 = l[1].split('/')
    G[l[0]] = l1
    V = list(G.keys())
    print(G)
    print(V)
    ch = input("Enter 1 to remove Left Recursion from a Production \n                   OR                   \n    "
               "Enter 2 "
               "to Left Factor a Production\n")
    while True:
        if ch == '1':
            for i in range(n):
                G, V = Left_Recursive(G, V)
                for i in V:
                    x = i + '='
                    for j in G[i]:
                        x = x + j + '/'
                    print(x[:(len(x) - 1)])
                    x = ''
            h.append(G)
            break
        elif ch == '2':
            Left_Factoring()
            for i in V:
                x = i + '='
                for j in G[i]:
                    x = x + j + '/'
                print(x[:(len(x) - 1)])
                x = ''
            break
        else:
            print("WRONG INPUT")
            ch = input(
                "Enter 1 to remove Left Recursion from a Production \n                   OR                   \n     "
                "Enter 2 to Left Factor a Production")


def Merge(dict1, dict2):
    res = dict1 | dict2
    return res


f = {}
for i in h:
    print(i)
    f = Merge(i, f)
print("Left Recursion free grammar:")
print(f)

# --------------------------------------------------------------------------
# First and Follow
# dic = {'S': ['Bb', 'bCd'], 'B': ['aB', 'ε'], 'C': ['cC', 'ε']}
dic = {}
word = input("Enter variables of the grammar(separated with commas):")
var = word.split(",")
start_symbol = input("Enter the start symbol").upper()
terminals = ['(', ')']

for i in range(len(var)):
    gram_rules = input(f"Enter rules of variable {var[i]} separated with /:")
    dic[var[i]] = gram_rules.split("/")
print(dic)
p = [dic[i] for i in dic]

temp = []
global fir
fir = []
global foll
foll = []


def help_me(x):
    a = []
    l = []
    prod = dic[x]
    for j in prod:
        if j == "ε":
            a.append('\u03B5')
        if j[0] in terminals:
            a.append(j[0])
        if j[0] in var:
            l.append(help_me(j[0]))
            for i in l:
                if i == "ε" and len(j)>2 and j[2] in terminals:
                    fir.append(j[2])
                if i in terminals:
                    fir.append(i)
    return a


def first(x):
    prod = dic[x]
    t = []
    global fir
    for j in prod:
        if j == "ε":
            fir.append('\u03B5')
        if j[0] in terminals:
            fir.append(j[0])
        if j[0] in var:
            t.append(help_me(j[0]))
            for j in t:
                for i in j:
                    if i == "ε" and len(j)>2 and j[2] in terminals:
                        fir.append(j[2])
                    if i in terminals:
                        fir.append(i)
                    if i == "ε" and len(j) > 2 and j[2] in var:
                        help_me(j[2])
    print("First", fir)
    fir = []


def get_key(val):
    for key, value in dic.items():
        if val == value:
            return key


def follow(x):
    global foll
    if x == start_symbol:
        foll.append("$")
    z = []
    for i in range(len(p)):
        for j in range(len(p[i])):
            if x in p[i][j]:
                if p[i] not in z:
                    z.append(p[i])
    for i in z:
        prod = i

        index = 0
        for i in range(len(prod)):
            for j in range(len(prod[i])):
                if x == prod[i][j]:
                    index = j

        for i in range(len(prod)):
            if x in prod[i]:
                if index != len(prod[i]) - 1 and len(prod[i])!=1:
                    if prod[i][index + 1] in terminals:
                        foll.append(prod[i][index + 1])

                    if prod[i][index + 1] in var:
                        temp.append(help_me(prod[i][index + 1]))
                        for k in temp:
                            for j in k:
                                if j in terminals:
                                    foll.append(j)
                                elif j == '\u03B5' and len(prod[i]) > index+2 and prod[i][index+2] in terminals:
                                    foll.append(prod[i][index+2])
                                else:
                                    follow(get_key(prod))
    print("Follow ", foll)
    foll = []


for i in var:
    print(i)
    first(i)
    follow(i)
