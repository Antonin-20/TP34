import operator
class Noeud :

    def __init__(self,name,children = None) :
        """
        Args:
            name (str|int|float): nom du noeud considéré
            enfants (list): liste des noeuds enfants
            val (float|int) : la valeur associée au nom des variables (x,y,...)
        """ 
        self.name = name
        self.children = []

    def add_child(self, child):
        """ajout d'un enfant à la liste des noeuds enfants
            n'est pas utilisé dans l'implémentation 'plus = n.Noeud('exp',[deux,y])' de l'arbre"""
        self.children += [child]
        return None
    
    def affichage(self):
        print(str(self.name)+" ", end="")
        #self.aff =  str(self.name) + self.aff
        for child in self.children:
            child.affichage()

    def evaluer(self,dict):
        if self.name in dict :
            self.val = dict[self.name]
        if self.name == "+":
            print(sum([c.evaluer(dict) for c in self.children]))    
        
        
    


