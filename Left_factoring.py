dic = {}
word = input("Enter variables of the grammar(separated with commas):")
var = word.split(",")
for i in range(len(var)):
    gram_rules = input(f"Enter rules of variable {var[i]} separated with /:")
    dic[var[i]] = gram_rules.split("/")


def left_factoring():
    gram_rules = []
    for key, value in dic.items():
        for i in range(len(value)):
            x = value[i]
            index = i
            for k in range(0, index):
                if x[0] == value[k][0]:
                    if x in value[k]:
                        gram_rules.append([key, value[k], x])

            for k in range(index + 1, len(value)):
                if x[0] == value[k][0]:
                    if x in value[k]:
                        gram_rules.append([key, value[k], x])

    grammar = []
    s = ""
    for i in range(len(gram_rules)):
        for j in range(len(gram_rules[i])):
            s = gram_rules[i][0] + " -> " + gram_rules[i][2] + gram_rules[i][0] + "'"
        grammar.append(s)
        s = ""

        for j in range(len(gram_rules[i])):
            s = gram_rules[i][0] + "' -> " + gram_rules[i][1][len(gram_rules[i][2]):] + "|" + '\u03B5'
        grammar.append(s)
        s = ""

    print("Grammar is", dic)
    print("Updated grammar gram_rules are:")
    for i in grammar:
        print(i)
