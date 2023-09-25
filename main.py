from tkinter import *
from math import pi

def f_calc():
    try:
        rpm = float(entrada_rpm.get())
        p_motor = float(entrada_polia_motor.get())
        p_maior = float(entrada_polia_maior.get())
        p_menor = float(entrada_polia_menor.get())
        p_roda = float(entrada_polia_roda.get())
        circ_pneu = float(entrada_pneu.get())

        # calculando rpm final da roda
        rpm_f = (((rpm * p_motor) / p_maior) * p_menor) / p_roda

        # calculando a velocidade final do patinete com base no rpm da roda
        diametro = circ_pneu / 100
        circunferencia = pi * diametro
        distancia_percorrida = circunferencia
        mpm = distancia_percorrida * rpm_f
        kmh = (mpm * 60) / 1000
        
        label_resultado.config(text=f"RPM FINAL DA RODA: {rpm_f:.2f} rpm")
        label_resultado2.config(text=f'VELOCIDADE FINAL: {kmh:.2f} km/h')
    except ValueError:
        label_resultado.config(text="Erro: Insira valores numéricos")


janela = Tk()
janela.title("WALKMACHINE CUSTOM")

largura_tela = janela.winfo_screenwidth()
altura_tela = janela.winfo_screenheight()
posicao_x = (largura_tela - 600) // 2
posicao_y = (altura_tela - 400) // 2
janela.geometry(f"350x200+{posicao_x}+{posicao_y}")
janela.resizable(False, False)

label_rpm_motor = Label(janela, text=f'{"RPM DO MOTOR:":>40}')
label_polia_motor = Label(janela, text=f'{"POLIA DO MOTOR(mm):":>34}')
label_polia_maior = Label(janela, text=f'{"POLIA MAIOR(mm):":>40}')
label_polia_menor = Label(janela, text=f'{"POLIA MENOR(mm):":>39}')
label_polia_roda = Label(janela, text=f'{"POLIA DA RODA(mm):":>39}')
label_pneu = Label(janela, text=f'{"CIRCUNFERÊNCIA DO PNEU(cm):":>30}')

entrada_rpm = Entry(janela)
entrada_polia_motor = Entry(janela)
entrada_polia_maior = Entry(janela)
entrada_polia_menor = Entry(janela)
entrada_polia_roda = Entry(janela)
entrada_pneu = Entry(janela)

botao_somar = Button(janela, text="CALCULAR", command=f_calc)

label_resultado = Label(janela, text=f'{"RPM FINAL DA RODA:":<30}')
label_resultado2 = Label(janela, text=f'{"VELOCIDADE FINAL:":<30}')

label_rpm_motor.grid(row=0, column=0)
entrada_rpm.grid(row=0, column=1)

label_polia_motor.grid(row=1, column=0)
entrada_polia_motor.grid(row=1, column=1)

label_polia_maior.grid(row=2, column=0)
entrada_polia_maior.grid(row=2, column=1)

label_polia_menor.grid(row=3, column=0)
entrada_polia_menor.grid(row=3, column=1)

label_polia_roda.grid(row=4, column=0)
entrada_polia_roda.grid(row=4, column=1)

label_pneu.grid(row=5, column=0)
entrada_pneu.grid(row=5, column=1)

botao_somar.grid(row=7, columnspan=2)
label_resultado.grid(row=8, columnspan=3)
label_resultado2.grid(row=9, columnspan=3)

janela.mainloop()
