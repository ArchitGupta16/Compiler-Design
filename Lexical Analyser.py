variables = []
operator = []
constants = []
keywords = []
special_symbols = []

string = ""
data = []
with open("test.txt", 'r') as data_file:
    for line in data_file:
        data.append(line.split())

for line in data:
    for word in line:
        for char in word:
            string += char

string = ""
bool = False
index1 = 0
count = 0
index2 = 0
chars = []
for line in data:
    for word in line:
        for char in word:
            chars.append(char)

s = ""
for i in range(len(chars)):
    s += chars[i]
    if chars[i] == "=":
        index1 = i
        bool = True
    if bool == True and chars[i] == "(":
        x = ""
        index1 = 0
        index2 = 0
        bool = False

    if bool == True:
        if chars[i] == ";":
            index2 = i
            bool = False
            x = ""
            for i in range(index1 + 1, index2):
                x += s[i]
            if x not in constants:
                constants.append(x)

for line in data:
    for word in line:

        if (word == "int" or word == "endif" or word == "else" or word == "if" or word == "then") and (
                word not in keywords):
            keywords.append(word)

        if word == "int" or word == "float" or word == "double" or word == "bool":
            variables.append(line[1])

        for char in word:

            if (char == "+" or char == "-" or char == "*" or char == "/" or char == ">") and (char not in operator):
                operator.append(char)

            if (char == "," or char == ";" or char == "(" or char == "{" or char == ")" or char == "}") \
                    and char not in special_symbols:
                special_symbols.append(char)

            if (char == "6" or char == "5") and (char not in constants):
                constants.append(char)

print("Variables:", variables)
print("Keywords", keywords)
print("Operator", operator)
print("Special_Symbols", special_symbols)
print("Constants", constants)
