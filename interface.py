from tkinter import *


def Interface(groups):

    ws = Tk()
    ws.title("Sistema de Recomendacao de Smartphones")
    ws.geometry('1000x800')


    frame1 = LabelFrame(ws, text='Selecione o sistema operacional desejado')
    frame1.grid(row=1, column=1, padx=10)

    frame2 = LabelFrame(ws, text='Qual faixa de preco voce prefere?')
    frame2.grid(row=2, column=1, padx=10)

    frame3 = LabelFrame(ws, text='Selecione o armazenamento interno desejado')
    frame3.grid(row=3, column=1, padx=10)

    frame4 = LabelFrame(ws, text='Selecione o tamanho da RAM desejado')
    frame4.grid(row=4, column=1, padx=10)

    frame5 = LabelFrame(ws, text='Selecione o numero de chips desejado')
    frame5.grid(row=5, column=1, padx=10)

    frame6 = LabelFrame(ws, text='Qual resolucao da camera traseira voce prefere?')
    frame6.grid(row=1, column=2, padx=10)

    frame7 = LabelFrame(ws, text='Qual resolucao da camera frontal voce prefere?')
    frame7.grid(row=2, column=2, padx=10)

    frame8 = LabelFrame(ws, text='Qual resolucao de filmagem voce prefere?')
    frame8.grid(row=3, column=2, padx=10)

    frame9 = LabelFrame(ws, text='Qual tamanho de tela voce prefere?')
    frame9.grid(row=4, column=2, padx=10)

    frame10 = LabelFrame(ws, text='Qual capacidade da basteria do smartphone que voce procura?')
    frame10.grid(row=5, column=2, padx=10)

    frame11 = LabelFrame(ws, text='Qual conexao voce deseja? ')
    frame11.grid(row=1, column=3, padx=10)

    frame12 = LabelFrame(ws, text='O smartphone que voce procura possui NFC?')
    frame12.grid(row=2, column=3, padx=10)

    frame13 = LabelFrame(ws, text='O smartphone que voce procura possui leitor biometrico?')
    frame13.grid(row=3, column=3, padx=10)

    frame14 = LabelFrame(ws, text='O smartphone que voce procura possui resistencia a agua?')
    frame14.grid(row=4, column=3, padx=10)

    frame15 = LabelFrame(ws, text='O smartphone que voce procura possui carregamento sem fio?')
    frame15.grid(row=5, column=3, padx=10,pady = 1)

    frame16 = Frame(ws, relief=SOLID, padx=10, pady=1)
    frame16.grid(row = 6, column = 3, padx = 10, pady = 1)
    #groups = []
    for i in range(16):
        groups.append(IntVar())

    Radiobutton(frame1, text='Android', variable=groups[1], value=1).pack()
    Radiobutton(frame1, text='iOS', variable=groups[1], value=2).pack()

    Radiobutton(frame2, text='Entre R$ 220,00 e R$ 800,00', variable=groups[2], value=1).pack()
    Radiobutton(frame2, text='Entre R$ 1100,00 e R$ 1800,00', variable=groups[2], value=2).pack()
    Radiobutton(frame2, text='Entre R$ 2000,00 e R$ 2700,00', variable=groups[2], value=3).pack()
    Radiobutton(frame2, text='Entre R$ 3900,00 e R$ 4500,00', variable=groups[2], value=4).pack()
    Radiobutton(frame2, text='Acima de R$ 5500,00', variable=groups[2], value=5).pack()

    Radiobutton(frame3, text='512MB', variable=groups[3], value=1).pack()
    Radiobutton(frame3, text='16GB', variable=groups[3], value=2).pack()
    Radiobutton(frame3, text='32GB', variable=groups[3], value=3).pack()
    Radiobutton(frame3, text='64GB', variable=groups[3], value=4).pack()
    Radiobutton(frame3, text='128GB', variable=groups[3], value=5).pack()
    Radiobutton(frame3, text='256GB', variable=groups[3], value=6).pack()
    Radiobutton(frame3, text='512GB', variable=groups[3], value=7).pack()

    Radiobutton(frame4, text='Ate 1GB', variable=groups[4], value=1).pack()
    Radiobutton(frame4, text='2GB', variable=groups[4], value=2).pack()
    Radiobutton(frame4, text='3GB', variable=groups[4], value=3).pack()
    Radiobutton(frame4, text='4GB', variable=groups[4], value=4).pack()
    Radiobutton(frame4, text='6GB', variable=groups[4], value=5).pack()
    Radiobutton(frame4, text='8GB', variable=groups[4], value=6).pack()
    Radiobutton(frame4, text='16GB', variable=groups[4], value=7).pack()

    Radiobutton(frame5, text='Single chip', variable=groups[5], value=1).pack()
    Radiobutton(frame5, text='Dual chip', variable=groups[5], value=2).pack()

    Radiobutton(frame6, text='0.3 a 10 MP', variable=groups[6], value=1).pack()
    Radiobutton(frame6, text='12 a 20 MP', variable=groups[6], value=2).pack()
    Radiobutton(frame6, text='Acima de 20 MP', variable=groups[6], value=3).pack()

    Radiobutton(frame7, text='Sem cam frontal', variable=groups[7], value=1).pack()
    Radiobutton(frame7, text='5 a 10 MP', variable=groups[7], value=2).pack()
    Radiobutton(frame7, text='12 a 16MP', variable=groups[7], value=3).pack()
    Radiobutton(frame7, text='20 MP ou mais', variable=groups[7], value=4).pack()

    Radiobutton(frame8, text='HD', variable=groups[8], value=1).pack()
    Radiobutton(frame8, text='FULL HD', variable=groups[8], value=2).pack()
    Radiobutton(frame8, text='4K', variable=groups[8], value=3).pack()
    Radiobutton(frame8, text='8K', variable=groups[8], value=4).pack()
    Radiobutton(frame8, text='Sem Filmadora', variable=groups[8], value=5).pack()

    Radiobutton(frame9, text='2.4 polegadas', variable=groups[9], value=1).pack()
    Radiobutton(frame9, text='4 polegadas', variable=groups[9], value=2).pack()
    Radiobutton(frame9, text='4.5 a 4.9 polegadas', variable=groups[9], value=3).pack()
    Radiobutton(frame9, text='5 a 6 polegadas', variable=groups[9], value=4).pack()
    Radiobutton(frame9, text='Acima de 6 polegadas', variable=groups[9], value=5).pack()

    Radiobutton(frame10, text='Ate 1500 mAh', variable=groups[10], value=1).pack()
    Radiobutton(frame10, text='1821 mAh ate 3000 mAh', variable=groups[10], value=2).pack()
    Radiobutton(frame10, text='3100 mAh ate 4000 mAh', variable=groups[10], value=3).pack()
    Radiobutton(frame10, text='4300 mAh ate 4900 mAh', variable=groups[10], value=4).pack()
    Radiobutton(frame10, text='5000 mAh ate 6000 mAh', variable=groups[10], value=5).pack()

    Radiobutton(frame11, text='3G', variable=groups[11], value=1).pack()
    Radiobutton(frame11, text='4G', variable=groups[11], value=2).pack()
    Radiobutton(frame11, text='5G', variable=groups[11], value=3).pack()

    Radiobutton(frame12, text='Sim', variable=groups[12], value=1).pack()
    Radiobutton(frame12, text='Nao', variable=groups[12], value=2).pack()

    Radiobutton(frame13, text='Sim', variable=groups[13], value=1).pack()
    Radiobutton(frame13, text='Nao', variable=groups[13], value=2).pack()

    Radiobutton(frame14, text='Sim', variable=groups[14], value=1).pack()
    Radiobutton(frame14, text='Nao', variable=groups[14], value=2).pack()

    Radiobutton(frame15, text='Sim', variable=groups[15], value=1).pack()
    Radiobutton(frame15, text='Nao', variable=groups[15], value=2).pack()

    Button(
        frame16, 
        text="Confirmar",
        command = ws.destroy
    ).pack(fill=X, expand=TRUE, side=LEFT)

    ws.mainloop()
