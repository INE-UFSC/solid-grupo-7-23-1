"""
Interface Segregation Principle
Crie interfaces que são específicas. Clientes não devem depender de interfaces que eles não usarão
"""
from abc import ABC

class IJanela(ABC):
    def fechar(self):
        raise NotImplementedError
    
class IJanelaFixo(IJanela,ABC):  
    def mostrar_menu(self):
        raise NotImplementedError

class IJanelaSemMenu(IJanela,ABC):
    def maximizar(self):
        raise NotImplementedError
    def minimizar(self):
        raise NotImplementedError

class JanelaTamanhoFixo(IJanelaFixo):
    
    def mostrar_menu(self):
        pass
    
    def fechar(self):
        pass

class JanelaSemMenu(IJanelaSemMenu):
    def maximizar(self):
        pass

    def minimizar(self):
        pass
    
    def fechar(self):
        pass


