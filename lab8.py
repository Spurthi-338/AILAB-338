facts = {
    'American(West)': True,         
    'Hostile(Nono)': True,           
    'Missiles(Nono)': True,          
}
def rule1(facts):
    if facts.get('American(West)', False) and facts.get('Hostile(Nono)', False):
        return 'Criminal(West)'  
    return None

def rule2(facts):
    if facts.get('Missiles(Nono)', False) and facts.get('Hostile(Nono)', False):
        return 'SoldWeapons(West, Nono)'  


def forward_chaining(facts, rules):
    new_facts = facts.copy()
    inferred = True
    while inferred:
        inferred = False
        for rule in rules:
            result = rule(new_facts)
            if result and result not in new_facts:-
                new_facts[result] = True
                inferred = True
                print(f"New fact inferred: {result}")
    return new_facts
rules = [rule1, rule2]

inferred_facts = forward_chaining(facts, rules)

print("\nFinal facts:")
for fact in inferred_facts:
    print(fact)
