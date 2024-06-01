from tkinter import *
from PIL import Image,ImageTk
import os

#Definindo a janela
root = Tk()

#Definindo o tamanho da janela
root.geometry('600x600')
root.minsize(600,600)

#Definindo o título da página
root.title('Banco Matuto')

#Definindo o ícone da página
root.iconbitmap('img/icone_cacto.ico')

#Definindo a cor inicial da página
root.config(bg='black')

#timer1=4000
#timer2=4000
#timer3=5500
#timer4=12000
#timer5=13000

#Timers para os fake loads
timer1 = 0
timer2 = 0
timer3 = 0
timer4 = 0
timer5 = 0

#Lista com o nome de todas as imagens
banco_de_imagens = ['logo_banco_matuto.png','logo_matuto.png','logo_nome_matuto.png']

#Define informações dos usuarios 
dados_usuário = {'1000':'123','2000':'321'}
informações_usuário = {'1000':'Silvio Santos da Cunha','2000':'Rodrigo Faro da Silva'}
saldo_dos_usuários = {'1000':0,'2000':0}

#Dicionario com os imagens carregadas
imagens_carregadas = {}

#Função para abrir as imagens e transformar em objetos que podem ser usados pelas labels
def carregar_imagens(imagem):
    for imgs in banco_de_imagens:
        if imgs is imagem:
            caminho_para_imagem = os.path.join('img/',imgs)
            objeto_imagem = ImageTk.PhotoImage(Image.open(caminho_para_imagem))
            imagens_carregadas[imgs] = objeto_imagem
            break
    return objeto_imagem

#Função para criar as labels
def criar_label_imagem(indice_imagem):
    label_criada = Label(image=carregar_imagens(banco_de_imagens[indice_imagem]),borderwidth=0,highlightthickness=0)
    return label_criada

#Função para posicionar as labels
def posicionar_label(label,posx,posy):
    label.place(relx=posx,rely=posy,anchor=CENTER)

#Função para deletar as labels
def deletar_label(label):
    label.destroy()

#Função para mandar os avisos na tela de login
def mensagem_usuário_login(texto,cor):
    mensagem_pro_usuário = Label(root,font=('Arial',10),text=texto,background='white',fg=cor)
    posicionar_label(mensagem_pro_usuário,0.5,0.35)
    return mensagem_pro_usuário

#Função para retornar ao menu pelo página deposito
def retornar_ao_menu_deposito(l1,l2,l3,l4):
    deletar_label(l1)
    deletar_label(l2)
    deletar_label(l3)
    deletar_label(l4)
    menu()

#Função para deletar todos os itens do menu quando entrar em alguma página
def deletar_itens_menu(b1,b2,b3,b4,b5,b6):
    deletar_label(b1)
    deletar_label(b2)
    deletar_label(b3)
    deletar_label(b4)
    deletar_label(b5)
    deletar_label(b6)

#Função para verificar os valores colocados na caixa de depósito
def verificar_valor_deposito(valor,caixa_deposito):
    try:
        valor = int(valor)
        if valor <= 0:
            mensagem_error_deposito = Label(text='Valor inserido inválido',fg='red',bg='white',font=('Arial',12))
            posicionar_label(mensagem_error_deposito,0.5,0.3)
            root.after(1500,lambda:deletar_label(mensagem_error_deposito))
        else:
            saldo_dos_usuários[cpf_usuário]+=valor
            mensagem_valido_deposito = Label(text='Depósito concluido',fg='green',bg='white',font=('Arial',12))
            posicionar_label(mensagem_valido_deposito,0.5,0.3)
            root.after(1500,lambda:deletar_label(mensagem_valido_deposito))
            caixa_deposito.delete(0,END)
    except:
        mensagem_error_deposito = Label(text='Valor inserido inválido',fg='red',bg='white',font=('Arial',12))
        posicionar_label(mensagem_error_deposito,0.5,0.3)
        root.after(1500,lambda:deletar_label(mensagem_error_deposito))
        
#Função para verificar os valores colocados na caixa de saque 
def verificar_valor_saque(valor,caixa_deposito):
    try:
        valor = int(valor)
        if valor > saldo_dos_usuários[cpf_usuário] or valor == 0:
            mensagem_error_saque = Label(text='Saldo insuficiente',fg='red',bg='white',font=('Arial',12))
            posicionar_label(mensagem_error_saque,0.5,0.3)
            root.after(1500,lambda:deletar_label(mensagem_error_saque))
        else:
            saldo_dos_usuários[cpf_usuário]-=valor
            mensagem_valido_saque = Label(text='Saque concluido',fg='green',bg='white',font=('Arial',12))
            posicionar_label(mensagem_valido_saque,0.5,0.3)
            root.after(1500,lambda:deletar_label(mensagem_valido_saque))
            caixa_deposito.delete(0,END)
    except:
        mensagem_error_saque = Label(text='Valor inserido inválido',fg='red',bg='white',font=('Arial',12))
        posicionar_label(mensagem_error_saque,0.5,0.3)
        root.after(1500,lambda:deletar_label(mensagem_error_saque))

        
#Função para inicialização
def boot():
    root.config(bg='#1b1b1b')
    root.after(timer2,lambda: root.config(bg='white'))
    label_logo_boot = criar_label_imagem(0)
    label_logo_boot
    root.after(timer3,lambda: posicionar_label(label_logo_boot,0.5,0.5))
    root.after(timer4,lambda: deletar_label(label_logo_boot))
    root.after(timer5,login)

#Página de login
def login():
    global login_logo
    login_logo = criar_label_imagem(1)
    login_logo
    posicionar_label(login_logo,0.5,0.2)
    
    global cpf_formulario
    global titulo_cpf
    global senha_formulario
    global titulo_senha
    global botão_entrar

    cpf_formulario = Entry(root,width=30,borderwidth=5)
    posicionar_label(cpf_formulario,0.5,0.45)
    
    titulo_cpf = Label(root,font=('Arial',10),text='CPF',background='white')
    posicionar_label(titulo_cpf,0.5,0.4)
    
    senha_formulario = Entry(root,width=30,borderwidth=5,show='*')
    posicionar_label(senha_formulario,0.5,0.55)
    
    titulo_senha = Label(root,font=('Arial',10),text='SENHA',background='white')
    posicionar_label(titulo_senha,0.5,0.5)
    
    botão_entrar = Button(root,text='Entrar',background='#38A37F',font=('Arial',14),fg='white',command=lambda: obter_dados_formulário(cpf_formulario,senha_formulario))
    posicionar_label(botão_entrar,0.5,0.65)

#Função que obtem os dados do formulário
def obter_dados_formulário(cpf,senha):
    global cpf_usuário
    cpf_usuário = str(cpf.get())
    senha_usuário = str(senha.get())
    if cpf_usuário and senha_usuário != None:
        if cpf_usuário in dados_usuário and dados_usuário[cpf_usuário] == senha_usuário:
            cpf.delete(0,END)
            senha.delete(0,END)
            mensagem_liberado = mensagem_usuário_login('Acesso liberado!','green')
            deletar_label(login_logo)
            deletar_label(titulo_cpf)
            deletar_label(cpf_formulario)
            deletar_label(titulo_senha)
            deletar_label(senha_formulario)
            deletar_label(botão_entrar)
            root.after(1500,lambda:deletar_label(mensagem_liberado))
            root.after(2000,menu)
        else:
            cpf.delete(0,END)
            senha.delete(0,END)
            mensagem_inválida = mensagem_usuário_login('Cpf ou senha inválidos','red')
            root.after(2000,lambda: deletar_label(mensagem_inválida))
    else:
        mensagem_preencha_dados = mensagem_usuário_login('Preencha os campos com seus dados','red')
        root.after(2000,lambda: deletar_label(mensagem_preencha_dados))
        if senha != None:
            senha.delete(0,END)    
            
#Página do menu
def menu():
    capturar_nome_usuário = informações_usuário[cpf_usuário]
    capturar_saldo_usuário = saldo_dos_usuários[cpf_usuário]
    nome_usuário = Label(root,text=f'Bem vindo, {capturar_nome_usuário}',bg='white',font=('Arial',12))
    posicionar_label(nome_usuário,0.5,0.1)
    saldo_usuário = Label(root,text=f'Seu saldo é R$ {capturar_saldo_usuário}',bg='white',font=('Arial',12))
    posicionar_label(saldo_usuário,0.5,0.135)
    botão_deposito = Button(root,text='Depósito',width=20,height=3,bg='#38A37F',fg='white',font=('Arial',16),command=lambda:página_deposito(botão_deposito,botão_saque,botão_extrato,botão_encerrar,nome_usuário,saldo_usuário))
    posicionar_label(botão_deposito,0.25,0.3)
    botão_saque = Button(text='Saque',width=20,height=3,bg='#38A37F',fg='white',font=('Arial',16),command=lambda:página_saque(botão_deposito,botão_saque,botão_extrato,botão_encerrar,nome_usuário,saldo_usuário))
    posicionar_label(botão_saque,0.75,0.3)
    botão_extrato = Button(root,text='Meus dados',width=20,height=3,bg='#38A37F',fg='white',font=('Arial',16),command=lambda:página_meusdados(botão_deposito,botão_saque,botão_extrato,botão_encerrar,nome_usuário,saldo_usuário))
    posicionar_label(botão_extrato,0.25,0.7)
    botão_encerrar = Button(root,text='Encerrar operação',width=20,height=3,bg='red',fg='white',font=('Arial',16),command=lambda:encerrar_operação(botão_deposito,botão_saque,botão_extrato,botão_encerrar,nome_usuário,saldo_usuário))
    posicionar_label(botão_encerrar,0.75,0.7)

#Função para o botão deposito   
def página_deposito(b1,b2,b3,b4,b5,b6):
    deletar_itens_menu(b1,b2,b3,b4,b5,b6)
    entrada_valor_depósito = Entry(root,width=20,font=('Arial',20),borderwidth=5)
    entrada_valor_depósito.place(height=60,relx=0.5,rely=0.45,anchor=CENTER)
    mensagem_depósito_valor = Label(root,text='Qual valor deseja depositar?',font=('Arial',12),bg='white')
    posicionar_label(mensagem_depósito_valor,0.5,0.36)
    botão_confirmar_depósito = Button(root,text='Confirmar',width=20,height=3,bg='#38A37F',fg='white',command=lambda:verificar_valor_deposito(entrada_valor_depósito.get(),entrada_valor_depósito))
    posicionar_label(botão_confirmar_depósito,0.35,0.6)
    botão_retornar_depósito = Button(root,text='Retornar',width=20,height=3,bg='red',fg='white',command=lambda:root.after(1500,retornar_ao_menu_deposito(entrada_valor_depósito,mensagem_depósito_valor,botão_confirmar_depósito,botão_retornar_depósito)))
    posicionar_label(botão_retornar_depósito,0.65,0.6)
    
#Função para o botão saque
def página_saque(b1,b2,b3,b4,b5,b6):
    deletar_itens_menu(b1,b2,b3,b4,b5,b6)
    entrada_valor_saque = Entry(root,width=20,font=('Arial',20),borderwidth=5)
    entrada_valor_saque.place(height=60,relx=0.5,rely=0.45,anchor=CENTER)
    mensagem_saque_valor = Label(root,text='Qual valor deseja sacar?',font=('Arial',12),bg='white')
    posicionar_label(mensagem_saque_valor,0.5,0.36)
    botão_confirmar_saque = Button(root,text='Confirmar',width=20,height=3,bg='#38A37F',fg='white',command=lambda:verificar_valor_saque(entrada_valor_saque.get(),entrada_valor_saque))
    posicionar_label(botão_confirmar_saque,0.35,0.6)
    botão_retornar_saque = Button(root,text='Retornar',width=20,height=3,bg='red',fg='white',command=lambda:root.after(1500,retornar_ao_menu_deposito(entrada_valor_saque,mensagem_saque_valor,botão_confirmar_saque,botão_retornar_saque)))
    posicionar_label(botão_retornar_saque,0.65,0.6)

#Função para o botão extrato
def página_meusdados(b1,b2,b3,b4,b5,b6):
    deletar_itens_menu(b1,b2,b3,b4,b5,b6)

#Função para o botão encerrar operação
def encerrar_operação(b1,b2,b3,b4,b5,b6):
    deletar_itens_menu(b1,b2,b3,b4,b5,b6)
    mensagem_encerramento = Label(text='Até mais :)',font=('Arial',24),fg='red',bg='white')
    posicionar_label(mensagem_encerramento,0.5,0.45)
    root.after(2000,lambda: root.quit())
    
#Delay de 1 segundo para executar a função boot() - Inicio
root.after(timer1,boot)

#Loop principal da janela
root.mainloop()