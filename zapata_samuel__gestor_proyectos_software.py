from dataclasses import dataclass, field

@dataclass
class Colaborador:
    username: str
    email: str

    
@dataclass
class Proyecto:
    nombre:str
    lenguaje:str
    colaboradores: list[Colaborador] = field(default_factory=list)

    def agregar_colaborador(self, colaborador: Colaborador) -> None:
        if colaborador not in self.colaboradores:
            self.colaboradores.append(colaborador)
        else:
            print("aviso: ya existe")

    def __str__(self) -> str:
        return f"Proyecto: {self.nombre} [{self.lenguaje}] - {len(self.colaboradores)} colaborador(es)"
     
    def tiene_colaborador(self, username: str) -> bool:
        for colaborador in self.colaboradores:
            if colaborador.username == username:
                return True
        return False
    

class GestorProyectos:
    def __init__(self):
        self.proyectos: list[Proyecto] = []
         

    def registrar_proyecto(self, proyecto: Proyecto) -> None:
        if proyecto not in self.proyectos:
            self.proyectos.append(proyecto)
        else:
            print("aviso: ya existe")

    def buscar_proyecto(self, nombre_proyecto: str) -> Proyecto | None:
        for proyecto in self.proyectos:
            if proyecto.nombre == nombre_proyecto:
                return proyecto
        return None



    def listar_proyectos(self) -> list[Proyecto]:
        return self.proyectos
     
         


# Colaboradores
ana   = Colaborador(username="ana_dev", email="ana@mail.com")
luis  = Colaborador(username="luis99",  email="luis@mail.com")
sofia = Colaborador(username="sofiaml", email="sofia@mail.com")

# Proyectos
p1 = Proyecto(nombre="InventarioApp", lenguaje="Python")
p1.agregar_colaborador(ana)
p1.agregar_colaborador(luis)
p1.agregar_colaborador(ana)   # aviso: ya existe

p2 = Proyecto(nombre="WebStore", lenguaje="JavaScript")
p2.agregar_colaborador(sofia)

# __str__
print(p1)  # Proyecto: InventarioApp [Python] — 2 colaborador(es)
print(p2)  # Proyecto: WebStore [JavaScript] — 1 colaborador(es)

# tiene_colaborador
print(p1.tiene_colaborador("ana_dev"))  # True
print(p1.tiene_colaborador("sofiaml"))  # False
#print(p1.tiene_colaborador("luis99"))  # True solo para ver
# Gestor
gestor = GestorProyectos()
gestor.registrar_proyecto(p1)
gestor.registrar_proyecto(p2)
gestor.registrar_proyecto(p1)  # aviso: ya existe

encontrado = gestor.buscar_proyecto("WebStore")
print(encontrado)  # Proyecto: WebStore [JavaScript] — 1 colaborador(es)

no_existe = gestor.buscar_proyecto("OtroProyecto")
print(no_existe)   # None

#para mirar si esta bien
#encontrado1 = gestor.buscar_proyecto("InventarioApp")
#print(encontrado1)  # Proyecto: InventarioApp [Python] — 2 colaborador(es)

print(len(gestor.listar_proyectos()))  # 2