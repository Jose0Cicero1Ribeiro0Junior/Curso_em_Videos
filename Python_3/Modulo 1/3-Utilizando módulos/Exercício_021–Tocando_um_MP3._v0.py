#Exercício Python 21: Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3
import playsound
tru_false = str(input('Quer reproduzir a musica? ')).title()
if tru_false == 'Sim':
    playsound.playsound('/home/joseciceroribeirojunior/Música/Ghost.mp3')
else:
    print('Fim')
