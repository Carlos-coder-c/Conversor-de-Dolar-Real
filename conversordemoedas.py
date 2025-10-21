def dolar_para_real(dolar, cotacao):
    return dolar * cotacao

def real_para_dolar(real, cotacao):
    return real / cotacao

cotacao = float(input("Informe a cotação do dólar (ex: 5.25): "))
opcao = input("Converter para (1) Real ou (2) Dólar? ")

if opcao == "1":
    valor_dolar = float(input("Informe o valor em dólar: "))
    convertido = dolar_para_real(valor_dolar, cotacao)
    print(f"US$ {valor_dolar:.2f} = R$ {convertido:.2f}")
elif opcao == "2":
    valor_real = float(input("Informe o valor em real: "))
    convertido = real_para_dolar(valor_real, cotacao)
    print(f"R$ {valor_real:.2f} = US$ {convertido:.2f}")
else:
    print("Opção inválida.")