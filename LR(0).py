# --------------------------------------------------------------------------------
# Closure
# Closure of the augmented production first and then the closure after finding goto
# --------------------------------------------------------------------------------

def Closure(a, var):
    dfa_states = a
    for pr in dfa_states:
        loc = pr[1].index(".")
        # To check cases like E->.E using below condition
        if loc < len(pr[1]) - 1 and pr[1][loc + 1] in var:
            for rules in var[pr[1][loc + 1]]:
                if [pr[1][loc + 1], str(".") + str(rules)] not in dfa_states:
                    dfa_states.append([pr[1][loc + 1], str(".") + str(rules)])

    return dfa_states


# --------------------------------------------------------------------------------
# Creating of LR0 item
# -----------------------------------------------------------------------------------
dfa = []
dfa_states = []


def LR0_item(start_sym, var, terminal):
    augmented = start_sym + "'"

    dfa_states.append(Closure([[augmented, '.' + start_sym]], var))
    print(dfa_states)
    terminal += list(var.keys())

    for i in dfa_states:
        for gram in terminal:
            if gram == ".":
                continue
            goto = False
            shift = False
            cl = []
            for items in i:
                if items[1].index(".") < len(items[1]) - 1 and items[1][items[1].index(".") + 1] is gram:
                    cl.append(
                        [items[0], items[1][:items[1].index(".")] + gram + "." + items[1][items[1].index(".") + 2:]])

            closure = Closure(cl, var)
            if len(closure) == 0:
                continue
            # print("Closure", closure)

            if gram in var.keys():
                goto = True
            else:
                shift = True

            if closure not in dfa_states:
                if goto:
                    dfa.append([dfa_states.index(i) + 1, gram, len(dfa_states) + 1])
                elif shift:
                    dfa.append([dfa_states.index(i) + 1, gram, len(dfa_states) + 1])
                dfa_states.append(closure)
            else:
                if goto:
                    dfa.append([dfa_states.index(i) + 1, gram, dfa_states.index(closure) + 1])
                else:
                    dfa.append([dfa_states.index(i) + 1, gram, dfa_states.index(closure) + 1])


# --------------------------------------------------------------------------------
# Input of Grammar
# --------------------------------------------------------------------------------
x = input("Enter variables separated by /:")
variables = x.split("/")
y = input("Enter the terminals separated by /:")
terminals = y.split("/")

prod = {}
for i in range(len(variables)):
    rule = input(f"Enter productions for {variables[i]} separated with /:")
    prod[variables[i]] = rule.split("/")
print("Grammar:", prod)

start_symbol = input("Enter start symbol:")
terminals.append("$")

# --------------------------------------------------------------------------------
# Execution of Code
# --------------------------------------------------------------------------------
LR0_item(start_symbol, prod, terminals)
print("Canonical Collection of LR(0) items:")
count = 1
for states in dfa_states:
    states.insert(0, count)
    print(states)
    count += 1

print("DFA")
for i in dfa:
    print(i)

r = []
for i in prod.keys():
    for j in prod[i]:
        r.append([i, j + str(".")])

print("Reduce States: ", r)

# --------------------------------------------------------------------------------
# Construction of DFA objects in required format and visualizing using graphviz
# --------------------------------------------------------------------------------
t = []
x = []
flat_list = []
for sublist in dfa_states:
    new = []
    for i in range(1, len(sublist), 1):
        new.append(sublist[i])
    flat_list = [item for sublist in new for item in sublist]
    t.append(flat_list)
print(t)

final_states = {}
count = 1
for i in t:
    for j in range(0, len(i), 2):
        x.append(f"{i[j]}" + "->" + f"{i[j + 1]}")
    final_states[count] = x
    x = []
    count += 1

states = set()
list_of_states = []
for i in final_states.values():
    s = " ".join(i)
    list_of_states.append(s)
    states.update({s})

terminals.remove("$")

vt = variables + terminals
sigma = set(vt)
delta = {}
counter = 1

initial_state = ""
for i in range(len(list_of_states)):

    delta.update({list_of_states[i]: dict({})})
    xx = delta.get(list_of_states[i])
    if i == 0:
        initial_state = list_of_states[i]
    if i + 1 == counter:

        for k in dfa:
            if k[0] == counter:
                xx.update({k[1]: list_of_states[k[2] - 1]})
    delta.update({list_of_states[i]: xx})
    counter += 1

# --------------------------------------------------------------------------------
# DFA and its parameters
# --------------------------------------------------------------------------------

initialState = initial_state
print("DFA Elements\n")
print("States:\n", states)
print("\nSigma:\n", sigma)

print("\nDelta:\n", delta)

from visual_automata.fa.dfa import VisualDFA
from automathon import DFA

new_dfa = DFA(Q=states, sigma=sigma, delta=delta, initialState=initialState, F=set())
new_dfa.view("DFA")
"""
The above line generates a DFA.gv named file which has to be run in online simulator if one does not have the system for 
running graphviz files
However if a system has the required settings a png file with the dfa will be created
"""
diag1 = VisualDFA(new_dfa)
