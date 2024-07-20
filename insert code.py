import requests
from bs4 import BeautifulSoup
import os

def scrap_web(url):
    
    # Start a session
    session = requests.Session()
    
    # Get the page content
    response = session.get(url)
    response.raise_for_status()  # Ensure we notice bad responses
    
    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Extract question name
    question_name = soup.select_one("div#__next h1.chakra-heading.css-1o1jsbj").text
    
    # Extract question difficulty
    question_difficulty = soup.select_one("div#__next span[class*='chakra-badge css-']").text
    
    question_id = url.split('/')[-1]
    
    return [question_name, question_difficulty, 0, question_id]



def insert_code(info, script):
    
    a = {'ساده':'easy', 'متوسط':'mid', 'سخت':'hard',}
    
    if not os.path.exists(f'Codes/{a[info[1]]}/{info[3]}/'):
        os.makedirs(f'Codes/{a[info[1]]}/{info[3]}/')
    
    
    files_in_folder = os.listdir(f'Codes/{a[info[1]]}/{info[3]}/')
    if len(files_in_folder) >= 1:
        for i in files_in_folder:
            
            with open(f'Codes/{a[info[1]]}/{info[3]}/{i}', 'r', encoding='utf-8') as f:
                t = f.readlines()
                
            if script == t:
                return
        
    text = ''.join(script)
    with open(f'Codes/{a[info[1]]}/{info[3]}/{info[3]}_{len(files_in_folder)+1}.py', 'w', encoding='utf-8') as f:
        f.write(text)
    
    # text = 'id,name(link to question),difficulty,score(link to answer)'
    text = f'-1 | {info[3]} | [{info[0]}](https://quera.org/problemset/{info[3]}) | {info[1]} | [جواب](Codes/{a[info[1]]}/{info[3]}/) | |\n'
    
    update_csv(text)



def update_csv(text):
    
    info = text.split(' | ')
    
    with open('question.txt', 'r', encoding='utf-8') as f:
        read_in_file = f.readlines()
        read_in_file = [[j for j in i.split(' | ')] for i in read_in_file]
    
    if info not in read_in_file:
        read_in_file.append(info)
    read_in_file.sort(key=lambda x:int(x[1]))
    
    for i in range(1, len(read_in_file)+1):
        read_in_file[i-1][0] = '| ' + str(i)
    
    
    read_in_file = [' | '.join(i) for i in read_in_file]
    
    with open('question.txt', 'w', encoding='utf-8') as f:
        for item in read_in_file:
            f.write(item)
        


def update_table():
    
    with open('question.txt', 'r', encoding='utf-8') as f:
        read_in_file = f.read()

    with open('README.md', 'r', encoding='utf-8') as f:
        text = f.read()
        text = text.split('***\n')
    
    table = text[len(text)-2].split('| 1 |')
    table[1] = read_in_file
    
    text[len(text)-2] = table[0]+table[1]+'\n[بازگشت به ابتدا :back:](#حل-سوالات-Quera)\n'
    
    text = '***\n'.join(text)
    
    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(text)
    
    

    
if __name__ == '__main__':
    
    
    path_to_answer = input('Please enter path to your directory that all of your complete codes is there: ')

    files_in_folder = os.listdir(path_to_answer)
    with open('question.txt', 'r', encoding='utf-8') as f:
        read_in_file = f.readlines()
        read_in_file = [(i.split(' | ')[1]+'.py') for i in read_in_file]
        
    for i in files_in_folder:
        if i not in read_in_file:
            
            with open(path_to_answer+'/'+i, 'r', encoding='utf-8') as f:
                script = f.readlines()
            
                
            url = 'https://quera.org/problemset/'+i[:len(i)-3]
            info = scrap_web(url)
            
            if script[0] != '# '+url+'\n':
                script.insert(0, f"# {url}\n")
                
            insert_code(info, script)
        
    
    update_table()
    
    
    
    