#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

with open('./Input/Names/invited_names.txt') as invited_names:
    lista_invitados = invited_names.read().split("\n")

with open('./Input/Letters/starting_letter.txt') as carta_inicial:
    bosquejo = carta_inicial.read()

def generar_letra():
    for invitado in lista_invitados:
        contenido = bosquejo.replace('[name]', invitado)
        ruta = f'Output/ReadyToSend/letter_for_{invitado}.txt'
        with open(ruta, mode='w') as carta:
            carta.write(contenido)

generar_letra()
