import ttg

#Operador Termo no Ambiente
# Conjunção (e) ‘and’
# Disjunção (ou) ‘or’
# Negação (não) ‘not’ / ‘~’ / ‘ - ’
# Implicação ‘=>’ / ‘implies’
# Bi-Implicação ‘=’

print ( ttg.Truths(['p'], ['(~p)'], ints= False))

print ( ttg.Truths(['p','q'], ['p and q'], ints= False))

print ( ttg.Truths(['p','q'], ['p or q'], ints= False))

print ( ttg.Truths(['p','q'], ['p = q'], ints= False))

print ( ttg.Truths(['p','q'], ['p => (~q)'], ints= False))

print ( ttg.Truths(['p','q'], ['p or (~q)'], ints= False))

print ( ttg.Truths(['p','q'], ['(~p) and (~q)'], ints= False))

print ( ttg.Truths(['p','q'], ['p = (~q)'], ints= False))

print ( ttg.Truths(['p','q'], ['(p and (~q)) => p'], ints= False))

print ( ttg.Truths(['p','q'], ['~p and q'], ints= False))

print ( ttg.Truths(['p','q'], ['(~p) and (~q)'], ints= False))
print ( ttg.Truths(['p','q'], ['(~p or p) and q'], ints= False))

print ( ttg.Truths(['p','q'], ['q => p'], ints= False))

print ( ttg.Truths(['p'], ['~(~p)'], ints= False))

print ( ttg.Truths(['p','q'], ['~((~p) and (~q))'], ints= False))

print ( ttg.Truths(['p','q', 'r'], ['(p or q) and ~q'], ints= False))

print ( ttg.Truths(['p','q', 'r'], ['(p and q) or (~p and ~r)'], ints= False))

print ( ttg.Truths(['p','r'], ['~(p) and ~(~r)'], ints= False))

print ( ttg.Truths(['p','q', 'r'], ['~(q or r) and ~(~p)'], ints= False))

print ( ttg.Truths(['p','q', 'r'], ['~(p and r) or (~q)'], ints= False))

print ( ttg.Truths(['p','q', 'r'], ['(~p or ~q) and r'], ints= False))

print ( ttg.Truths(['p','q', 'r'], ['~(r) => p and ~q'], ints= False))

print ( ttg.Truths(['p','q', 'r'], ['~(~p and ~q) and (r and p)'], ints= False))

print ( ttg.Truths(['p','q'],['p => q'], ints=False))

print ( ttg.Truths(['p','q'],['p=q'], ints=False))

print ( ttg.Truths(['p'],['~p'], ints=False))

print ( ttg.Truths(['p','q'],['~(p and q)'], ints=False))

print ( ttg.Truths(['a','b'],['(~a) and b'], ints=False))

print ( ttg.Truths(['a','b'],['(~b) => (a or b)'], ints=False))

print ( ttg.Truths(['a','c'],['(c or a) = (~(~c))'], ints=False))

print ( ttg.Truths(['a','c'],['a or (a => b)'], ints=False))

print ( ttg.Truths(['a','c','d'],['(d or (~a)) => (~c)'], ints=False))

print ( ttg.Truths(['a','c','b'],['(~(a and b))=> (~(c and b))'], ints=False))

print ( ttg.Truths(['p','q'],['~(p => ~q)'], ints=False))

print ( ttg.Truths(['p','q','r'],['p = ~q and r'], ints=False))

print ( ttg.Truths(['p','q'],['p => ~q and p or q = p or ~q'], ints=False))

print ( ttg.Truths(['t','d', 'l'],['t and d and l'], ints=False))

print ( ttg.Truths(['m','a'],['m and ~a'], ints=False))

print ( ttg.Truths(['m','a'],['m and ~a'], ints=False))

print ( ttg.Truths(['a','b', 'r'],['a and (b or r)'], ints=False))

print ( ttg.Truths(['r','m', 'c'],['(r and m) and ~c'], ints=False))

print ( ttg.Truths(['a','h', 't'],['(a and h) or (t and ~h)'], ints=False))
