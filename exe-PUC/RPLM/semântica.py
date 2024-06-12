import ttg as t
# exer a)
# p = caminhar q = reprovar r = Jogar futebol s = correr
resultado = t.Truths(['p', 'q', 'r', 's'], ['(p => ~q) and (~r => s) and (q => s)'],  ints=False )
print(resultado)
print(resultado.valuation())

#p = atraso do professor q= aula começa na hora certa r = atraso aluno
resultado = t.Truths(['p', 'q', 'r'], ['(~p => q) and (~r and ~p )=> q'],  ints=False )

print(resultado.valuation())

#exer c)
#p = Pedro esteve aqui q = João esteve aqui r = quadro com poesias

resultado = t.Truths(['p', 'q', 'r'], ['(q or p) and (q => r) and (~r =>p)'],  ints=False )

print(resultado.valuation())

#exer d)
# p = trabalho q = brincar r = passar em matemática 

resultado = t.Truths(['p', 'q', 'r'], ['(p => ~q) and (p or r) and (r and ~q) => ~p'],  ints=False )

print(resultado.valuation())

#exer e)
# p = marido rico q = esposa pobre r =  ser honesta s = casamento bom  t = filhos u = probelmas familiáres v = brigam 

resultado = t.Truths(['p', 'q', 'r', 's', 't', 'u'], ['(p  and q and r) and ((q and p) => (s or ~t or u )) and (~s and ~v and ~u) => ~t'],  ints=False )

print(resultado.valuation())

resultado = t.Truths(['p', 'q'], ['p => p or q '],  ints=False )

print(resultado.valuation())

resultado = t.Truths(['p', 'q', 'r'], ['(p or q) and (p =>r) and (~r) => q '],  ints=False )
print(resultado)
print(resultado.valuation())





