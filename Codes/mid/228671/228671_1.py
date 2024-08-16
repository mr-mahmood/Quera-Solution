# https://quera.org/problemset/228671

t = int(input())
result = []

for i in range(t):
    
    n, M, T = (int(i) for i in input().split(' '))
    t_list = list((int(i) for i in input().split(' ')))
    t_list.append(T)
    
    if M in t_list:
        index = t_list.index(M)
        t_list = t_list[index::]
        
    '''some times we need to find how many minute sand is still in upper part so we need to change M 
    but we have to store original M as well because when upper part compltly empties then it have original M minute in lower part
    '''
    M_temp = M 
    start = 0
    for i in range(len(t_list)):
        
        time_next = t_list[i]
        
        # because in last iteration when i+1 happend it raise an error
        try:
            
            time_next_next = t_list[i+1]
            if time_next_next - start <= M_temp : # we check if we still have sand in upper part then we dont do anything and go to next t in t_list
                continue
            
        except:
            pass
        
        if time_next - start <= M_temp:
            sand_in_lower_part = time_next-start
            sand_in_upper_part = max(0, M_temp-(sand_in_lower_part))
            start = time_next
            
            if (time_next-sand_in_lower_part) % M_temp == 0 and (time_next-sand_in_lower_part) != 0: # when excauly M minute pass all sand are gone in one place
                M_temp = M
                
            else: # in this part some sand are in upper part ans some of them in lower part
                M_temp = M_temp - sand_in_upper_part
                
                if M_temp == 0 : # mean all sands are in lower part so we have original M minute sant in upper part in next round
                    M_temp = M
        
    if start == T:
        result.append("YES")
    else:
        result.append("NO")
    
print(*result, sep='\n')