#Francisco Rosales Huey
#Programa que lee un autómata finito determinista a partir de un archivo txt
class AFD:
    def __init__(self):
        """Inicializa el autómata finito determinista (AFD)"""
        self.estados = None
        self.alfabeto = None
        self.transiciones = None
        self.estado_inicial = None
        self.estados_aceptacion = []
        self.estado_actual = None

    def cargar_desde_archivo(self, archivo):
        """Carga el autómata desde un archivo de texto"""
        with open(archivo, 'r') as archivo_txt:
            lineas = archivo_txt.readlines()

        self.alfabeto = lineas[0].strip().split(',')[1:]
        self.estados = []
        self.transiciones = {}
        self.estado_inicial = None
        self.estados_aceptacion = []

        for linea in lineas[1:]:
            partes = linea.strip().split(',')
            estado = partes[0]

            if estado.startswith('+*'):
                estado = estado[2:]
                self.estado_inicial = estado
                self.estados_aceptacion.append(estado)
            elif estado.startswith('+'):
                estado = estado[1:]
                self.estado_inicial = estado
            elif estado.startswith('*'):
                estado = estado[1:]
                self.estados_aceptacion.append(estado)

            self.estados.append(estado)
            self.transiciones[estado] = {self.alfabeto[i]: partes[i + 1] for i in range(len(self.alfabeto))}

    def mostrar(self):
        """Muestra el autómata en un formato legible"""
        if not self.estados or not self.alfabeto or not self.transiciones:
            print("El autómata no ha sido cargado.")
            return

        print("," + ",".join(self.alfabeto) + ",")
        for estado in self.estados:
            estado_formato = ""
            if estado == self.estado_inicial and estado in self.estados_aceptacion:
                estado_formato = "->*" + estado
            elif estado == self.estado_inicial:
                estado_formato = "->" + estado
            elif estado in self.estados_aceptacion:
                estado_formato = "*" + estado
            else:
                estado_formato = estado

            transiciones_estado = [self.transiciones[estado][simbolo] for simbolo in self.alfabeto]
            print(estado_formato + "," + ",".join(transiciones_estado) + ",")

    def procesar_simbolo(self, simbolo):
        """Actualiza el estado actual basado en el símbolo de entrada"""
        self.estado_actual = self.transiciones[self.estado_actual][simbolo]
        return self.estado_actual

    def es_estado_aceptacion(self):
        """Verifica si el estado actual es de aceptación"""
        return self.estado_actual in self.estados_aceptacion

    def validar_cadena(self, cadena):
        """Valida la cadena de entrada"""
        self.estado_actual = self.estado_inicial
        for simbolo in cadena:
            self.procesar_simbolo(simbolo)
            if self.estado_actual == 'NM':  # Estado no válido
                return False
        return self.es_estado_aceptacion()


def menu():
    afd = AFD()
    while True:
        print("\n===== Menú =====")
        print("1. Cargar autómata desde archivo")
        print("2. Verificar cadena")
        print("3. Mostrar autómata")
        print("4. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            archivo = input("Introduce el nombre del archivo (incluyendo la extensión .txt): ")
            try:
                afd.cargar_desde_archivo(archivo)
                print("Autómata cargado correctamente.")
            except FileNotFoundError:
                print("Archivo no encontrado. Verifica que el archivo esté en la ruta correcta.")
        elif opcion == "2":
            if afd.estados is None:
                print("Primero debes cargar un autómata (opción 1).")
            else:
                cadena = list(input("Introduce la cadena a validar (solo caracteres '0' y '1'): "))
                print("ACCEPTED" if afd.validar_cadena(cadena) else "REJECTED")
        elif opcion == "3":
            afd.mostrar()
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, elige una opción correcta.")


if __name__ == "__main__":
    menu()
