print('Spurthi Reddy P  1BM23CS338')
def unify(x, y, subst=None):
    if subst is None:
        subst = {}

    # If x or y is a variable or constant
    if is_variable(x) or is_constant(x):
        if x == y:
            return subst
        elif is_variable(x):
            return unify_var(x, y, subst)
        elif is_variable(y):
            return unify_var(y, x, subst)
        else:
            return None

    # If both x and y are compound expressions
    if is_compound(x) and is_compound(y):
        if x[0] != y[0] or len(x[1]) != len(y[1]):
            return None
        for xi, yi in zip(x[1], y[1]):
            subst = unify(xi, yi, subst)
            if subst is None:
                return None
        return subst
    return None


def is_variable(x):
    return isinstance(x, str) and x.islower() and x.isalpha()


def is_constant(x):
    return isinstance(x, str) and x.isupper() and x.isalpha()


def is_compound(x):
    return isinstance(x, tuple) and len(x) == 2 and isinstance(x[0], str) and isinstance(x[1], list)


def unify_var(var, x, subst):
    if var in subst:
        return unify(subst[var], x, subst)
    elif x in subst:
        return unify(var, subst[x], subst)
    elif occurs_check(var, x, subst):
        return None
    else:
        subst[var] = x
        return subst


def occurs_check(var, x, subst):
    if var == x:
        return True
    elif is_variable(x) and x in subst:
        return occurs_check(var, subst[x], subst)
    elif is_compound(x):
        return any(occurs_check(var, arg, subst) for arg in x[1])
    else:
        return False


# Example usage:
# Let's say we want to unify P(x, A) and P(B, y)
x = ("P", ["x", "A"])
y = ("P", ["B", "y"])

result = unify(x, y)
if result is not None:
    print("Unification succeeded with substitution:", result)
else:
    print("Unification failed.")
