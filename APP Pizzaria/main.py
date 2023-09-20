import pyodbc


def main():
    print('-------Tela Principal------\n')
    print('Escolha a sua ação')
    acao = input('\n[1]Logar\n[2]Cadastrar\n')

    if acao == '1':
        nome_login = input('\nNome de login:')
        senha_login = input('Senha de login:')
        login(nome_login, senha_login)
        # Lógica de autenticação pode ser adicionada aqui
    elif acao == '2':
        print('-------------Tela Cadastro--------------')
        botao = input('[1] aperte 1 para cadastrar\n[2] para voltar\n')

        if botao == '1':
            cadastrar()
            print('Funcionário cadastrado')
        else:
            acao = input('\n[1]Logar\n[2]Cadastrar\n')

def login(nome_login, senha_login):
    server = 'DESKTOP-04O4S90'
    database = 'APP_PIZZARIA'
    trusted_connection = 'yes'  # Indica o uso da autenticação do Windows

    # Conectar ao banco de dados
    conn = pyodbc.connect(f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection={trusted_connection}')
    cursor = conn.cursor()

    # Verificar se as credenciais estão corretas
    query = "SELECT * FROM CADASTRO_FUNCIONARIO WHERE NOME = ? AND SENHA = ?"
    cursor.execute(query, (nome_login, senha_login))

    if cursor.fetchone():
        print('Login bem-sucedido!')
    else:
        print('Credenciais inválidas.')

    # Fechar a conexão
    conn.close()



def cadastrar():
    nome = input('Nome a cadastrar:')
    cargo = input('Cargo do funcionário:')
    senha = input('Senha do Funcionário:')
    salario = input('Salário do funcionário:')
    horario = input('Horário do funcionário:')
    email = input('E-mail do funcionário:')
    
    server = 'DESKTOP-04O4S90'
    database = 'APP_PIZZARIA'
    trusted_connection = 'yes'  # Indica o uso da autenticação do Windows

    # Conectar ao banco de dados
    conn = pyodbc.connect(f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection={trusted_connection}')
    cursor = conn.cursor()

    # Inserir novo registro na tabela "Usuarios"
    query = "INSERT INTO CADASTRO_FUNCIONARIO (NOME, CARGO, SENHA, SALARIO, HORARIO , EMAIL) VALUES (?, ?, ?, ?, ?, ?)"
    cursor.execute(query, (nome, cargo, senha, salario, horario, email))

    # Confirmar a transação e fechar a conexão
    conn.commit()
    conn.close()

main()