# https://quera.org/problemset/1365

def Shiftr(n, text):
    temp = text[len(text)-n::]
    text = temp +  text[:len(text)-n:]
    
    return text

def Shiftl(n, text):
    temp = text[:len(text)-n:]
    text = text[len(text)-n::] + temp
    
    return text

def Extend(n, text):
    return text + '*' * n

def Shrink(n, text):
    if len(text) < n:
        return ''
    else:
        return text[:len(text)-n:]
    
def Reverse(text):
    return text[::-1]

def Put(i, c, text):
    temp = list(text)
    temp[i-1] = c
    
    return ''.join(temp)

def Print(text):
    print(text)


if __name__ == '__main__':
    text = input()
    while True:
        
        user_input = input()
        if user_input == 'EXIT':
            break
        
        try:
            user_input = user_input.split(' ')
        except:
            user_input = [user_input]
        
        if user_input[0] == 'SHIFT-R':
            text = Shiftr(int(user_input[1]), text)

        elif user_input[0] == 'SHIFT-L':
            text = Shiftl(int(user_input[1]), text)

        elif user_input[0] == 'EXTEND':
            text = Extend(int(user_input[1]), text)

        elif user_input[0] == 'SHRINK':
            text = Shrink(int(user_input[1]), text)

        elif user_input[0] == 'REVERSE':
            text = Reverse(text)

        elif user_input[0] == 'PUT':
            text = Put(int(user_input[1]), user_input[2], text)

        elif user_input[0] == 'PRINT':
            Print(text)

