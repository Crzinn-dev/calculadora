import customtkinter as ctk
from functools import partial

trava = False
janela = ctk.CTk()
janela.title('Calculadora')
janela.geometry('400x500')

# Funções Botões

def enviar(valor):
    global trava
    meu_label = label.cget('text')

    if valor == '(':
        p_aberto = meu_label.count('(')
        p_fechado = meu_label.count(')')
        if p_aberto > p_fechado:
            valor = ')'
        elif p_aberto == p_fechado:
            valor = '('
    if len(meu_label) > 0:
        if valor in '+-x/.':
            if valor != '.':
                trava = False
            if meu_label[-1] in '+-x/.':
                valor = ''
        if valor == '.' and trava == False:
            trava = True
        elif valor == '.' and trava == True:
            valor = ''
    else:
        if valor in '+-x/.':
            valor = ''

    meu_label += valor
    label.configure(text=meu_label)

def apagar_ultimo_caractere():
    global trava
    meu_label = label.cget('text')
    if meu_label[-1] in '+-x/':
        trava = True
    meu_label = meu_label[:-1]
    label.configure(text=meu_label)

def apagar_tudo():
    global trava
    trava = False
    label.configure(text='')

def calcular():
    meu_label = label.cget('text')
    meu_label = meu_label.replace('x', '*')
    resultado = str(eval(meu_label))
    label.configure(text=resultado)


# Box 1
box1 = ctk.CTkFrame(janela)
box1.pack()
label = ctk.CTkLabel(box1, text='', width=400, height=40, font=('bold', 30))
label.pack()
# caixa_calculo = ctk.CTkEntry(box1, width=400, height=40, font=('bold', 30))
# caixa_calculo.pack()

# Box 2
box2 = ctk.CTkFrame(janela, fg_color='transparent')
box2.pack(pady=10)

botao7 = ctk.CTkButton(box2, text='7', width=80, height=50, command=partial(enviar, valor= '7'))
botao7.pack(side='left')

botao8 = ctk.CTkButton(box2, text='8', width=80, height=50, command=partial(enviar, valor= '8'))
botao8.pack(padx=10, side='left')

botao9 = ctk.CTkButton(box2, text='9', width=80, height=50, command=partial(enviar, valor= '9'))
botao9.pack(side='left')

dividir = ctk.CTkButton(box2, text='/', width=80, height=50, command=partial(enviar, valor= '/'))
dividir.pack(padx=10)

# Box 3
box3 = ctk.CTkFrame(janela, fg_color='transparent')
box3.pack(pady=10)

botao4 = ctk.CTkButton(box3, text='4', width=80, height=50, command=partial(enviar, valor= '4'))
botao4.pack(side='left')

botao5 = ctk.CTkButton(box3, text='5', width=80, height=50, command=partial(enviar, valor= '5'))
botao5.pack(padx=10, side='left')

botao6 = ctk.CTkButton(box3, text='6', width=80, height=50, command=partial(enviar, valor= '6'))
botao6.pack( side='left')

multiplicar = ctk.CTkButton(box3, text='x', width=80, height=50, command=partial(enviar, valor= 'x'))
multiplicar.pack(padx=10)

# Box 4
box4 = ctk.CTkFrame(janela, fg_color='transparent')
box4.pack(pady=10)

botao1 = ctk.CTkButton(box4, text='1', width=80, height=50, command=partial(enviar, valor= '1'))
botao1.pack(side='left')

botao2 = ctk.CTkButton(box4, text='2', width=80, height=50, command=partial(enviar, valor= '2'))
botao2.pack(padx=10, side='left')

botao3 = ctk.CTkButton(box4, text='3', width=80, height=50, command=partial(enviar, valor= '3'))
botao3.pack(side='left')

subtraçao = ctk.CTkButton(box4, text='-', width=80, height=50, command=partial(enviar, valor= '-'))
subtraçao.pack(side='left', padx=10)

# Box 5
box5 = ctk.CTkFrame(janela, fg_color='transparent')
box5.pack(pady=10)

botao0 = ctk.CTkButton(box5, text='0', width=80, height=50, command=partial(enviar, valor= '0'))
botao0.pack(side='left')

ponto = ctk.CTkButton(box5, text='.', width=80, height=50, command=partial(enviar, valor= '.'))
ponto.pack(padx=10, side='left')

clearall = ctk.CTkButton(box5, text='c', width=80, height=50, command=apagar_tudo)
clearall.pack(side='left')

adiçao = ctk.CTkButton(box5, text='+', width=80, height=50, command=partial(enviar, valor= '+'))
adiçao.pack(padx=10)

# Box 6
box6 = ctk.CTkFrame(janela, fg_color='transparent')
box6.pack(pady=10)

igual = ctk.CTkButton(box6, text='=', width=((80*2)), height=50, command=calcular)
igual.pack(side='left')

parenteses = ctk.CTkButton(box6, text='()', width=80, height=50, command=partial(enviar, valor= '('))
parenteses.pack(side='left', padx=10)

clearpop = ctk.CTkButton(box6, text='<', width=80, height=50, command=apagar_ultimo_caractere)
clearpop.pack(padx=10)


janela.mainloop()