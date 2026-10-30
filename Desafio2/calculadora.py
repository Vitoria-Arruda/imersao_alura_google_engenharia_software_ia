"""
Calculadora Completa em Python
Realiza operações aritméticas básicas e compostas:
- Adição (+)
- Subtração (-)
- Multiplicação (*)
- Divisão (/)
- Porcentagem (%)
- Avaliação de expressões matemáticas (ex: 2 + 3 * 8, 200 * 15%, 100 + 10%)
"""

import ast
import operator
import re


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


def porcentagem(valor: float, percentual: float) -> float:
    """
    Calcula o valor percentual correspondente.
    Exemplo: porcentagem(200, 15) -> 30.0 (15% de 200).
    """
    return (valor * percentual) / 100


# Mapeamento de nós da AST para funções existentes e operadores seguros
OPERADORES_BINARIOS = {
    ast.Add: somar,
    ast.Sub: subtrair,
    ast.Mult: multiplicar,
    ast.Div: dividir,
}

OPERADORES_UNARIOS = {
    ast.USub: operator.neg,
    ast.UAdd: operator.pos,
}


def _avaliar_no(no: ast.AST) -> float:
    """
    Avalia recursivamente nós da AST (Abstract Syntax Tree) de forma segura.
    Garante respeito à precedência de operadores e reutiliza as funções existentes.
    """
    if isinstance(no, ast.Constant):
        if isinstance(no.value, (int, float)):
            return float(no.value)
        raise ValueError("Valores não numéricos não são permitidos.")
    elif isinstance(no, ast.BinOp):
        tipo_op = type(no.op)
        if tipo_op not in OPERADORES_BINARIOS:
            raise ValueError(f"Operador binário não suportado: {tipo_op.__name__}")
        esquerda = _avaliar_no(no.left)
        direita = _avaliar_no(no.right)
        return OPERADORES_BINARIOS[tipo_op](esquerda, direita)
    elif isinstance(no, ast.UnaryOp):
        tipo_op = type(no.op)
        if tipo_op not in OPERADORES_UNARIOS:
            raise ValueError(f"Operador unário não suportado: {tipo_op.__name__}")
        operando = _avaliar_no(no.operand)
        return OPERADORES_UNARIOS[tipo_op](operando)
    else:
        raise ValueError("Estrutura de expressão não permitida ou inválida.")


def avaliar_expressao(expressao: str) -> float:
    """
    Avalia uma expressão matemática com múltiplos operadores e operandos.
    Respeita a ordem matemática (multiplicação e divisão antes de soma e subtração),
    suporta parênteses e porcentagem (%).

    Exemplos:
        avaliar_expressao("2 + 3 * 8")   -> 26.0
        avaliar_expressao("(2 + 3) * 8") -> 40.0
        avaliar_expressao("200 * 15%")   -> 30.0
        avaliar_expressao("100 + 10%")   -> 110.0
        avaliar_expressao("100 - 15%")   -> 85.0
    """
    if not expressao or not expressao.strip():
        raise ValueError("A expressão não pode estar vazia.")

    # Normalização de símbolos comuns
    expr = expressao.strip().replace(",", ".")
    expr = expr.replace("÷", "/").replace("×", "*").replace("x", "*")

    # Suporte a acréscimo e desconto percentual: ex: 100 + 10% -> (100 + (100 * 10 / 100))
    expr = re.sub(
        r"(\d+(?:\.\d+)?)\s*([\+\-])\s*(\d+(?:\.\d+)?)\s*%",
        r"(\1 \2 (\1 * \3 / 100))",
        expr,
    )

    # Suporte a porcentagem multiplicativa ou direta: ex: 15% -> (15 / 100)
    expr = re.sub(r"(\d+(?:\.\d+)?)\s*%", r"(\1 / 100)", expr)

    try:
        arvore = ast.parse(expr, mode="eval")
    except SyntaxError:
        raise ValueError("Expressão matemática inválida. Verifique a sintaxe digitada.")

    return _avaliar_no(arvore.body)


def exibir_menu() -> None:
    """Exibe o menu de opções disponíveis para o usuário."""
    print("\n" + "=" * 44)
    print("            CALCULADORA PYTHON              ")
    print("=" * 44)
    print("1 - Adição (+)")
    print("2 - Subtração (-)")
    print("3 - Multiplicação (*)")
    print("4 - Divisão (/)")
    print("5 - Porcentagem (%)")
    print("6 - Expressão completa (ex: 2 + 3 * 8 ou 50 + 10%)")
    print("0 - Sair")
    print("=" * 44)


def obter_numero(mensagem: str) -> float:
    """
    Solicita um número ao usuário e garante que seja válido.
    Evita que o programa trave caso o usuário digite texto inválido.
    """
    while True:
        try:
            return float(input(mensagem).replace(",", "."))
        except ValueError:
            print("❌ Entrada inválida! Por favor, digite um número válido.")


def calculadora() -> None:
    """Função principal que orquestra a execução da calculadora."""
    print("Bem-vindo(a) à Calculadora em Python!")

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção (0 a 6) ou digite a expressão diretamente: ").strip()

        # Opção para sair do programa
        if opcao == "0":
            print("\n👋 Encerrando a calculadora. Até mais!")
            break

        # Operações básicas tradicionais (opções 1 a 4)
        if opcao in ("1", "2", "3", "4"):
            num1 = obter_numero("Digite o primeiro número: ")
            num2 = obter_numero("Digite o segundo número: ")

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

        # Nova opção: Cálculo direto de porcentagem
        elif opcao == "5":
            base = obter_numero("Digite o valor base (ex: 200): ")
            taxa = obter_numero("Digite a porcentagem (%) (ex: 15): ")
            valor_perc = porcentagem(base, taxa)

            print(f"\n✅ {taxa}% de {base} = {valor_perc}")
            print(f"   Com acréscimo (+{taxa}%): {base + valor_perc}")
            print(f"   Com desconto (-{taxa}%): {base - valor_perc}")

        # Nova opção: Expressão completa pelo submenu
        elif opcao == "6":
            expressao = input("Digite a expressão matemática (ex: 2+3*8 ou 200*15%): ").strip()
            try:
                resultado = avaliar_expressao(expressao)
                print(f"\n✅ Resultado: {expressao} = {resultado}")
            except ValueError as erro:
                print(f"\n❌ Erro: {erro}")

        # Caso o usuário tenha digitado diretamente a expressão no menu principal
        else:
            try:
                resultado = avaliar_expressao(opcao)
                print(f"\n✅ Resultado: {opcao} = {resultado}")
            except ValueError:
                print("⚠️ Opção inválida! Escolha um número de 0 a 6 ou digite uma expressão válida.")


# Ponto de entrada padrão para scripts Python
if __name__ == "__main__":
    calculadora()
