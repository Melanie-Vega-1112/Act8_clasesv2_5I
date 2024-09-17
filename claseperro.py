print("clases version 2 el constructor")

class Perro:
    # función constructor
    def __init__(self, color, edad):
        self.color = color
        self.edad = edad

    # funciones creadas por el usuario
    def muerde(self):
        print("Chale, el perro me mordió")

    def Chatperro(self, mensaje):
        print(f"chat perro: {mensaje}")

    def Chatperra(self, mensajepe):
        print(f"chat perra: {mensajepe}")

    def datos(self):
        print(f"color: {self.color}, edad: {self.edad}")

# crear el objeto
chihuas = Perro("Negro" , 2)

# llamada a funciones
chihuas.datos()
chihuas.muerde()
chihuas.Chatperro("hola canina")
chihuas.Chatperra("hola boby")
chihuas.Chatperro("quieres ser mi gugguu?")
chihuas.Chatperra("grrru.....")
