class Noeud :
    def __init__(self,val,childs : list) :
        """
        Args:
            val (str|int|float): valeur du noeud considéré
            enfants (list): liste des noeuds enfants
        """
        self.val = val
        self.child = childs

    def add_child(self,child):
        """ajout d'un enfant à la liste des noeuds enfants"""
        self.child += [child]
        return None
    
