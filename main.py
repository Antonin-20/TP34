import noeud as n
import operator

#exp = n.Noeud("exp")
plus = n.Noeud("+")
deux = n.Noeud(2)
y = n.Noeud("y")

#exp.add_child(plus)
#plus.add_child(deux)
#plus.add_child(y)

#exp = n.Noeud('exp',[deux,y])  #autre o

#exp.affichage()
a = 5
b = 6
print(operator.add(a,b))
somme = sum([1,2,3,4,5])
#[e.evaluer(d) for e in enfants]

plus.add_child(deux)
plus.add_child(y)

d = {"y":5}

plus.evaluer(d)