import openai
import pyfiglet
import typer
from rich import print
from rich.table import Table




def main():

    openai.api_key = "INTRODUCIR VUESTRA API KEY"


    print("[bold red]-[/bold red]" * 75)
    title = pyfiglet.figlet_format("CHAT-GPT API EN PYTHON", font="slant")
    print (title)
    print("[bold red]-[/bold red]" * 75)

    table = Table("Comando", "Descripción")
    table.add_row("exit --->", "Salir de la aplicación") # Para salir del programa
    table.add_row("new --->", "Crear una nueva conversación") #Elimina el historial de busqueda para "empezar de nuevo"
    print(table)



    context = {"role": "system", "content": "Eres un asistente muy útil"} #Definimos lo que es el asistente para que cuando conteste este sea más preciso combinando IA
    messages = [context]
    while True:

        contenido = __prompt()

        if contenido == "new":
            print("[bold yellow]Nueva conversación creada!![/bold yellow]")
            print("\n Se ha borrado el historial de conversaciones anteriores")
            messages = [context]
            contenido = __prompt()

        messages.append({"role": "user", "content": contenido}) #Vamos guardando cada uno de los mensajes que introduce el usuario concatenandolos

        respuesta = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages) #Contexto de las respuestas que se vinculan a preguntas anteriores

        contenido_respuesta = respuesta.choices[0].message.content #Filtramos exclusivamente el contenido de la respuesta

        messages.append({"role": "assistant", "content": contenido_respuesta}) #AHora es capaz de guardar información de todas las preguntas hechas por el usuario

        print(f"[bold green][+][/bold green] [green]{contenido_respuesta}[/green]")

def __prompt() -> str:
    prompt = typer.prompt("\n ¿Que me quieres preguntar?")

    if prompt == "exit":
        exit = typer.confirm("[+]¿Estas seguro que quieres salir?")
        if exit:
            print("Nos vemos pronto!!!")
            raise typer.Abort()
        
        return __prompt()
    
    return prompt
    


if __name__ == "__main__":
    typer.run(main)
