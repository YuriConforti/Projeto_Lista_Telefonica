#Funcao para adicionar contatos
def adicionar_contato (agenda):
    nome = input("Digite o nome do contato: ")
    numero = input("Digite o numero do contato: ")
    pessoa = {"nome" : nome, "numero": numero}
    agenda.append(pessoa)
    print("Contato salvo com sucesso!")

# #Funcao para buscar pelo nome do contato
    
def buscar_contato (agenda, nome_buscado):
    for pessoa in agenda:
        if pessoa["nome"] == nome_buscado:
                return pessoa ["numero"]
    return "Contato inexistente"
        
#Agenda para armazenar os contatos
agenda = []     

# Menu para usuario
def main():
    while True:
        print("\nMenu: ")
        print("1. Adicionar Contato")
        print("2. Buscar Contato")
        print("3. Sair")
        escolha = input("Escolha uma opcao: ")
 
        if escolha == "1":
            adicionar_contato(agenda)
        elif escolha == "2":
            nome_buscado = input("Digite o nome do contato que deseja buscar: ")
            resultado = buscar_contato(agenda, nome_buscado)
            print("Numero do contato:", resultado)
        elif escolha == "3":
            print("Saindo da Agenda...")
            break
        else:
            print("Opcao invalida. Por favor tente novamente.")

# Executa funcao principal
if __name__ == "__main__":
    main()