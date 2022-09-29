dic = {}
word = input("Enter variables of the grammar(separated with commas):")
var = word.split(",")
for i in range(len(var)):
    rules = input(f"Enter rules of variable var{i + 1} separated with /:")
    dic[var[i]] = rules.split("/")
print(dic)


def left_recursion():
    boolean = False
    ini = []
    beta = []
    without_left = []
    for key, value in dic.items():
        for j in range(len(value)):
            if key == value[j][0]:
                ini.append([key, value[j]])
                boolean = True
            else:
                if boolean:
                    beta.append([key, value[j]])
                    boolean = False
                else:
                    without_left.append([key, value[j]])

    alpha = []
    for i in range(len(ini)):
        if ini[i][0] == ini[i][1][0]:
            s = ini[i][1]
            alpha.append([ini[i][0], s[1:]])

    rules = []
    for i in range(len(alpha)):
        a = alpha[i][0] + "'" + " -> " + alpha[i][1] + alpha[i][0] + "'" + "|" + '\u03B5'
        rules.append([alpha[i][0], a])

    for i in range(len(beta)):
        b = beta[i][0] + " -> " + beta[i][1] + beta[i][0] + "'"
        rules.append([beta[i][0], b])

    rules.sort()
    for i in range(len(rules)):
        print(rules[i][1])

    for i in range(len(without_left)):
        print(without_left[i][0], "->", without_left[i][1])


left_recursion()