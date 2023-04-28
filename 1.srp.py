"""
Single Responsibility Principle

Uma classe deve ter somente uma responsabilidade
ou
Uma classe deve ter somente um motivo para mudar
"""

class Save(ABC):
    @abstractmethod
    def save(self, animal: Animal):
        pass

class DBSave:
    # salva no DB
    def save(self, animal: Animal):
        pass

class Animal:
    def __init__(self, name: str):
        self.name = name
    
    def get_name(self) -> str:
        pass

    def save(self, animal: Animal):
        DBSave().save(self)
