# https://quera.org/problemset/604

def winner(person_list):
    flag = False
    while True:
        for i in range(len(person_list)):
            
            if person_list[i] != '' and flag == False:
                flag = True
                continue
            
            if flag == True:
                person_list[i] = ''
                flag = False
                continue
                
        person_list = [i for i in person_list if i != '']
        if len(person_list) == 1:
            return person_list[0]

num = int(input())

person_list = [i for i in range(1, num+1)]

a = winner(person_list)
print(a)