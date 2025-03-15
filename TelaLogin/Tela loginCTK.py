import customtkinter as ctk

janela = ctk.CTk()

janela.title('MINHA JANELA')
janela.geometry("300x300")
janela._set_appearance_mode('system')

janela.resizable(width = False, height = False)

label_usuario = ctk.CTkLabel(janela, text = 'usuario')
label_usuario.pack(pady = 10)

campo_usuario = ctk.CTkEntry(janela, placeholder_text = 'Digite o seu nome...')
campo_usuario.pack()

label_senha = ctk.CTkLabel(janela, text = 'Senha')
label_senha.pack(pady = 10)

campo_senha = ctk.CTkEntry(janela, placeholder_text = 'Digite a sua senha...')
campo_senha.pack()

botao_login = ctk.CTkButton(janela, text = 'Entrar')
botao_login.pack(pady = 20)

janela.mainloop()

