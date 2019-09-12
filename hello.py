# hello = "hello"
# print(hello)

# for i in range(4):
#     if i > 0:
#         print(i)

# print("===============================")

# input_peso = input("Peso em Pounds: ")
# peso = int(input_peso)
# resultado = peso / 2.2046
# print(f"[-> o peso em Kilogramas é de {str(round(resultado,2))}]")

# print(10 + 3 * 2 ** 2)

# equacao = ""

# operadores = "+ - * / **"
# while 1 > 0:
#         num = input("Número: ")
#         op = "null"
#         print(operadores.find(op))
#         if operadores.find(op) == -1:
#                 op = input("Operador ")

#         equacao += f"{num} {op} "
#         print(equacao)


import requests


r = requests.get("https://coreyms.com")
print(r.status_code)
print(r.ok)
