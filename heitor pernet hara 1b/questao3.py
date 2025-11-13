nome="admin"
senha="1234"
input_nome=input("digite seu nome do login :")
if input_nome==nome :  
    input_senha=(input("digite sua senha :"))
    if input_senha==senha:
        print("login realizado com sucesso!")
    else:
        print("senha incorreta!")
else:
    print("nome do login incorreto!")