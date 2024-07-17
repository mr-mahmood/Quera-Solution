# https://quera.org/problemset/66862

s = input()


def count(t, number, sum): # it will make all possible len(X).len(X).len(X).len(X) IP which sum of all X`s lenght is equal to length of string s
    num = ['1','2','3']
        
    if t < 3:
        for i in num:
            number.append(i)
            sum += int(i)
            count(t+1, number, sum)
            sum -= int(number[len(number)-1]) # add number to sum to check if length of this possible X.X.X.X matching s       
            number.pop(len(number)-1)
    else:
        for i in num:
            if sum+int(i) == len(s): # check for length match
                number.append(i)
                
                temp = number.copy()
                
                x = [0,0,0,0] # from here to line 40 we make every X of X.X.X.X IP, base on number that we havr been making. which hold length of every X
                # for example if number is ['2','3','1','2'] it mean that IP is something like that: xx.xxx.x.xx
                
                start = 0
                end = int(temp[0])
                x[0] = s[start : end]
                
                start = end
                end = int(temp[0]) + int(temp[1])
                x[1] = s[start : end]
                
                start = end
                end = int(temp[0]) + int(temp[1]) + int(temp[2])
                x[2] = s[start : end]
                
                start = end
                end = int(temp[0]) + int(temp[1]) + int(temp[2]) + int(temp[3])
                x[3] = s[start : end]
                
                flag = True
                for i in x:
                    if i[0] == '0' and len(i) > 1:
                        flag = False
                    if int(i) > 255:
                        flag = False
                        
                if flag == True:
                    print(x[0] + '.' + x[1] + '.' + x[2] + '.' + x[3])
                    
                number.pop(len(number)-1)
                    
count(0, [], 0)
                    

            
            

# Code wirter mr-mahmood
# Github: https://github.com/mr-mahmood