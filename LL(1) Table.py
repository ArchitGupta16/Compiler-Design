import re
import pandas as pd


def fir(s, productions):
    first = set()

    for i in range(len(productions[s])):

        for j in range(len(productions[s][i])):

            c = productions[s][i][j]

            if c.isupper():
                f = fir(c, productions)
                if '&' not in f:
                    for k in f:
                        first.add(k)
                    break
                else:
                    if j == len(productions[s][i]) - 1:
                        for k in f:
                            first.add(k)
                    else:
                        f.remove('&')
                        for k in f:
                            first.add(k)
            else:
                first.add(c)
                break

    return first


def foll(s, productions, first):
    follow = set()
    if len(s) != 1:
        return {}
    if s == list(productions.keys())[0]:
        follow.add('$')

    for i in productions:
        for j in range(len(productions[i])):
            if s in productions[i][j]:
                idx = productions[i][j].index(s)

                if idx == len(productions[i][j]) - 1:
                    if productions[i][j][idx] == i:
                        break
                    else:
                        f = foll(i, productions, first)
                        for x in f:
                            follow.add(x)
                else:
                    while idx != len(productions[i][j]) - 1:
                        idx += 1
                        if not productions[i][j][idx].isupper():
                            follow.add(productions[i][j][idx])
                            break
                        else:
                            f = fir(productions[i][j][idx], productions)

                            if '&' not in f:
                                for x in f:
                                    follow.add(x)
                                break
                            elif '&' in f and idx != len(productions[i][j]) - 1:
                                f.remove('&')
                                for k in f:
                                    follow.add(k)

                            elif '&' in f and idx == len(productions[i][j]) - 1:
                                f.remove('&')
                                for k in f:
                                    follow.add(k)

                                f = foll(i, productions, first)
                                for x in f:
                                    follow.add(x)

    return follow


def parsing_table(productions, first, follow):
    table = {}
    for key in productions:
        for value in productions[key]:
            val = ''.join(value)
            if val != '&':
                for element in first[key]:
                    if element != '&':
                        if not val[0].isupper():
                            if element in val:
                                table[key, element] = val
                            else:
                                pass
                        else:
                            table[key, element] = val
            else:
                for element in follow[key]:
                    table[key, element] = val

    new_table = {}
    for pair in table:
        new_table[pair[1]] = {}

    for pair in table:
        new_table[pair[1]][pair[0]] = table[pair]
    print("\nParsing Table \n")
    print(pd.DataFrame(new_table).fillna('-'))

    return table


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

first = {}
follow = {}
table = {}

start = ""
print("Grammar")
productions = {'S': [['A', 'B'], ['a', 'S']], 'A': [['e', 'A', 'c'], ['d'], ['&']], 'B': [['c', 'B'], ['b'], ['&']]}
for s in productions.keys():
    first[s] = fir(s, productions)

print("First")
for lhs, rhs in first.items():
    print(lhs, ":", rhs)

for lhs in productions:
    follow[lhs] = set()

for s in productions.keys():
    follow[s] = foll(s, productions, first)

print("Follow")
for lhs, rhs in follow.items():
    print(lhs, ":", rhs)

table = parsing_table(productions, first, follow)
