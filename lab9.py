def negate_literal(lit):
    return lit[1:] if lit.startswith("~") else "~" + lit

def resolve(ci, cj):
    ci = set(ci)
    cj = set(cj)
    resolvents = []

    for di in ci:
        ndi = negate_literal(di)
        if ndi in cj:
            new_clause = (ci - {di}) | (cj - {ndi})
            if len(new_clause) == 0:
                resolvents.append({"res": set(), "pair": (ci, cj)})
            else:
                resolvents.append({"res": new_clause, "pair": (ci, cj)})
    return resolvents


# CLAUSES (CNF)
clauses = [
    {"~Food(x)", "Likes(John,x)"},
    {"~Eats(x,y)", "~Killed(y)", "Food(y)"},
    {"Eats(Anil,Peanut)"},
    {"Alive(Anil)"},
    {"~Alive(z)", "~Killed(z)"},
    {"~Likes(John,Peanut)"}   # Negated Query
]

# Resolution Steps Storage
steps = []

changed = True
while changed:
    changed = False
    new = []

    for i in range(len(clauses)):
        for j in range(i+1, len(clauses)):
            ci = clauses[i]
            cj = clauses[j]
            resolvents = resolve(ci, cj)

            for r in resolvents:
                res = r["res"]
                if res == set(): # NIL Found
                    steps.append((ci, cj, set()))
                    print("\n✅ NIL (Contradiction Found)")
                    print("=> Query Proven TRUE")
                    changed = False
                    break

                if res not in clauses and res not in new:
                    new.append(res)
                    steps.append((ci, cj, res))
                    changed = True
        if changed is False and resolvents and res == set():
            break

    for c in new:
        clauses.append(c)


print("      RESOLUTION STEPS")

for (a, b, c) in steps:
    if c == set():
        print(f"{a}  +  {b}  =>  NIL")
    else:
        print(f"{a}  +  {b}  =>  {c}")

# PRINT CLAUSES AFTER DERIVATION
print("\nRemaining Clauses:")
for c in clauses:
    print(c)
