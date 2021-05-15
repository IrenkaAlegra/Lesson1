def get_summ(one, two, delimiter='&'):
    my_string = str(one) + delimiter + str(two)
    print(my_string) 


get_summ(1, 0.5)
get_summ("Привет", "Ира")
get_summ('Ира', "привет", delimiter=' ')
