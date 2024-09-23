#Hecho por: 
# Hector Alejandro Ortega Garcia
# Registro: 21310248
# Grupo: 7F
import json  # Importa la librería JSON para poder trabajar con archivos en formato JSON.

# Base de datos de conocimiento
database_file = "knowledge.json"  # Nombre del archivo que almacenará el conocimiento adquirido.

# Función para cargar el conocimiento almacenado
def load_knowledge():
    try:
        # Abre el archivo de base de datos en modo lectura.
        with open(database_file, "r") as file:
            # Carga el contenido del archivo JSON como un diccionario y lo devuelve.
            return json.load(file)
    except FileNotFoundError:
        # Si el archivo no existe, devuelve un diccionario vacío.
        # Esto previene errores si el archivo aún no ha sido creado.
        return {}

# Función para guardar el conocimiento en la base de datos
def save_knowledge(knowledge):
    # Abre el archivo en modo escritura para guardar el nuevo conocimiento.
    with open(database_file, "w") as file:
        # Convierte el diccionario en formato JSON y lo guarda en el archivo.
        json.dump(knowledge, file)

# Función principal del chat
def chat():
    # Carga el conocimiento almacenado previamente desde el archivo JSON.
    knowledge = load_knowledge()

    # Respuestas precargadas
    # Diccionario que contiene respuestas predefinidas a algunas preguntas comunes.
    predefined_responses = {
        "hola": "¡Hola! ¿Cómo estás?",
        "bien y tu como estas": "Estoy bien, gracias por preguntar. ¿De qué te gustaría hablar?",
        "de que te gustaria hablar": "Podemos hablar de lo que quieras. ¿Qué te interesa?"
    }

    # Bucle infinito para mantener la conversación en el chat.
    while True:
        # Solicita al usuario una entrada y la convierte a minúsculas para facilitar la comparación.
        user_input = input("Tú: ").lower()

        # Verifica si la entrada del usuario está en las respuestas predefinidas.
        if user_input in predefined_responses:
            # Si la encuentra, imprime la respuesta correspondiente.
            print("Chatbot:", predefined_responses[user_input])

        # Si no está en las respuestas predefinidas, busca en la base de conocimiento almacenada.
        elif user_input in knowledge:
            # Si se encuentra una coincidencia en el conocimiento previamente almacenado, responde con esa respuesta.
            print("Chatbot:", knowledge[user_input])

        # Si no se encuentra la pregunta en las respuestas predefinidas ni en el conocimiento almacenado:
        else:
            # El chatbot indica que no tiene una respuesta para la pregunta actual.
            print("Chatbot: No tengo una respuesta para eso. ¿Cuál debería ser la respuesta?")
            # Solicita al usuario que introduzca una respuesta para esa pregunta.
            new_response = input("Tú: ")

            # Añade la nueva pregunta y su respuesta al diccionario de conocimiento.
            knowledge[user_input] = new_response
            # Guarda el nuevo conocimiento en el archivo JSON para uso futuro.
            save_knowledge(knowledge)

            # Agradece al usuario por aportar nueva información.
            print("Chatbot: ¡Gracias! Ahora sé cómo responder esa pregunta.")

# Iniciar el chat
# Si este archivo se ejecuta directamente (no es importado como módulo), inicia el chat.
if __name__ == "__main__":
    chat()
