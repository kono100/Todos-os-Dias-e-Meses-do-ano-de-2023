# Definir uma lista com os nomes dos meses
meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 
         'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

# Definir um loop for para percorrer todos os meses
for mes in meses:
    # Definir um loop for para percorrer todos os dias de cada mês
    for dia in range(1, 32):
        # Verificar se o dia é válido para o mês atual
        if ((mes == 'Fevereiro' and dia > 28) or 
            ((mes == 'Abril' or mes == 'Junho' or mes == 'Setembro' or mes == 'Novembro') and dia > 30)):
            break  # Se o dia não for válido, saia do loop interno

        # Imprimir a data no formato "dia/mês/ano"
        print(f"{dia:02d}/{mes}/2023")
