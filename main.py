print("Hello world" , 15) # pokud chci více datových typů si je oddělit ","

# vytvoření proměnnné (deklarace/inicilizace)
cislo= 1 # Do proměnné cislo je uložná hodnota 1

print("druhý způsob s proměnou" , cislo)

#vytvoření proměnné s názvem text
text = "Zde je v proměnné uložený text" # Datový typ string

#Do konzole vypisujeme obě, oddělujeme čárkou
print(text, cislo)

# text - proměnná text vypíše co je v ní uložené
# cislo - proměnná vypíše číslo, který je proměnné uložen

# vytvoření vstupní hodnoty - uživatel musí zadat hodnotu do terminálu
# následně se hodnota zadána do terminálu uloží do proměnné
vstupni_promenna = input() # input() - příkaz pro vstupní data

# input() - do závorek zapisujeme zprávu pro uživatele který se vypíše v terminálu

druha_vstupni_promenna = input("Zadejte číslo")

# print() nám do konzole, co uživatel zadal do inputu
print(vstupni_promenna, druha_vstupni_promenna)