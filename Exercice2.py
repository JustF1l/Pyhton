import time

ma_variable_globale = "ma_variable_globale"
ma_variable_argument = "ma_variable_argument"

def ma_fonction(ma_variable_argument):
    
    ma_variable_locale = "ma_variable_locale"
    print(ma_variable_locale)

i = 0

for i in range(3):
    print(ma_variable_argument)
    print(ma_variable_globale)
    ma_fonction(ma_variable_argument)
    time.sleep(1)

ma_fonction("ma_variable_argument")