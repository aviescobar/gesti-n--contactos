class Contacto:
    def __init__(self, nombre, telefono, email):
        self.nombre = nombre
        self.telefono = telefono
        self.email = email

def __str__(self):
    return f"Nombre: {self.nombre}, Telefono: {self.telefono}, Email: {self.email}"

class GestorContactos:
    def __init__(self):
        self.contactos = []

    def agregar_contacto(self, contacto):
        self.contactos.append(self, contacto):
        print(f"Contacto '{contacto.nombre}' agregado.")

    def listar_contacto(self):
        if not self.contactos:
            print("No hay contactos en la lista.")
        else:
            print("Lista de Contactos:")
            for contacto in self.contactos:
                print(contacto)

    def buscar_contato(self, nombre):
        for contactos in self.contactos:
            if contacto.nombre.lower() == nombre.lower():
                return contacto
        return None

def menu():
    print("/nMenu:")
    print("1. Agregar contacto")
    print("2. Listar contacto")
    print("3. Buscar contacto")
    print("4. Salir")

def main():
    gestor = GestorContactos()

while True():
    menu()
    opcion = input("Seleccionar una opcion: ")


    if opcion == '1':
        nombre = input("Nombre: ")
        telefono = input("Telefono: ")
        email = input("Email: ")
        nuevo_contacto = Contacto(nombre, telefono, email)
        gestor.agregar_contacto(nuevo_contacto)

    elif opcion == '2':
        gestor.listar_contactos()

    elif opcion == '3':
        nombre = input("Ingresa el nombe del contacto a buscar: ")
        conctacto = gestor.byuscar_contacto(nombre)
        if contacto:
            print("Contacto entrotado: ")
        else:
            print("Contacto no encontrado.")
    


    


    


        
        
    
