# https://quera.org/problemset/110015

walk_path = '.......'
wall = '########'
ghorfe = 'ghorfe'
end = '#######################'

num = int(input())
num_temp = 1
temp = ''

for _ in range(4):
    if num_temp <= num:
        
        if num_temp + 1 <= num:
            temp += wall + walk_path + wall + '\n#' + ghorfe + str(num_temp) + walk_path + ghorfe + str(num_temp + 1) + '#\n'
            num_temp += 2
            
        else:
            temp += wall + walk_path + wall + '\n#' + ghorfe + str(num_temp) + walk_path + walk_path + '#\n'
            num_temp += 1
            
    
    else:
        temp += wall + walk_path + wall + '\n#' + walk_path + walk_path + walk_path + '#\n'

temp += end
print(temp)
        
# Code wirter Github: https://github.com/mr-mahmood