"""
Calculadora Simples em Python
Realiza as quatro operações aritméticas básicas:
- Adição (+)
- Subtração (-)
- Multiplicação (*)
- Divisão (/)
"""

def somar(a: float, b: float) -> float:
    """Retorna a soma de dois números."""
    return a + b

def subtrair(a: float, b: float) -> float:
    """Retorna a subtração do primeiro número pelo segundo."""
    return a - b

def multiplicar(a: float, b: float) -> float:
    """Retorna a multiplicação de dois números."""
    return a * b

def dividir(a: float, b: float) -> float:
    """
    Retorna a divisão do primeiro número pelo segundo.
    Lança ValueError se houver tentativa de divisão por zero.
    """
    if b == 0:
        raise ValueError("Não é possível dividir por zero!")
    return a / b

def exibir_menu() -> None:
    """Exibe o menu de opções disponíveis para o usuário."""
    print("\n" + "=" * 32)
    print("      CALCULADORA PYTHON        ")
    print("=" * 32)
    print("1 - Adição (+)")
    print("2 - Subtração (-)")
    print("3 - Multiplicação (*)")
    print("4 - Divisão (/)")
    print("0 - Sair")
    print("=" * 32)

def obter_numero(mensagem: str) -> float:
    """
    Solicita um número ao usuário e garante que seja válido.
    Evita que o programa trave caso o usuário digite texto inválido.
    """
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("❌ Entrada inválida! Por favor, digite um número válido.")

def calculadora() -> None:
    """Função principal que orquestra a execução da calculadora."""
    print("Bem-vindo(a) à Calculadora em Python!")
    
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção (0 a 4): ").strip()
        
        # Opção para sair do programa
        if opcao == "0":
            print("\n👋 Encerrando a calculadora. Até mais!")
            break
            
        # Validação da opção escolhida
        if opcao not in ("1", "2", "3", "4"):
            print("⚠️ Opção inválida! Escolha um número entre 0 e 4.")
            continue
            
        # Coleta dos dois números
        num1 = obter_numero("Digite o primeiro número: ")
        num2 = obter_numero("Digite o segundo número: ")
        
        # Execução e exibição do cálculo
        try:
            if opcao == "1":
                resultado = somar(num1, num2)
                operador = "+"
            elif opcao == "2":
                resultado = subtrair(num1, num2)
                operador = "-"
            elif opcao == "3":
                resultado = multiplicar(num1, num2)
                operador = "*"
            elif opcao == "4":
                resultado = dividir(num1, num2)
                operador = "/"
                
            print(f"\n✅ Resultado: {num1} {operador} {num2} = {resultado}")
            
        except ValueError as erro:
            print(f"\n❌ Erro: {erro}")

# Ponto de entrada padrão para scripts Python
if __name__ == "__main__":
    calculadora()
