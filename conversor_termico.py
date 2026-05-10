# definindo a função
def converter_celsius_para_fahrenheit(celsius):
    # formula
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit # retorna o valor calculado
# usando a função
tempC =  float(input('Digite a temperatura em Celsius: '))
# Chamamos a função e guardamos o que ela 'retornou' em uma variável
resultado = converter_celsius_para_fahrenheit(tempC)
print(f"{tempC}°C equivalem a {resultado}°C fahrenheit")
