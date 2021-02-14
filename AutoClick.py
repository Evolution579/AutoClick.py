import pyautogui, time as tm

while True:

    tempoparainiciar = float(input("Informe o tempo para iniciar em segundos! "))
        # Puxa o valor da resposta do usuário (Float), e retorna em tempo para o autoclick iniciar


    totalclicks = int(input("\nInforme o total de clicks! "))
    if totalclicks >= 0: # Se o total de clicks informado pelo usuário for 0, totalclicks = 1
        totalclicks = 1


    delayclicks = float(input("\nInforme o tempo de cada click em segundos! "))
        # Puxa o valor da resposta do usuário (Float), e retorna em delay para cada click


    tm.sleep(tempoparainiciar)
    for i in range(totalclicks):
        tm.sleep(delayclicks)
        pyautogui.leftClick()
    break
