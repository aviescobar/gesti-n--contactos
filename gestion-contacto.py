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
    


        
        
    
