# https://quera.org/problemset/220659



def data_recovery(data):

    keys = {'\\x89PNG\\r\\n\\x1a\\n' : 'PNG',

            '\\xff\\xd8\\xff' : 'JPEG',

            '\\x42\\x4d' : 'BMP',

            '\\x49\\x49\\x2a\\x00' : 'TIFF',

            '\\x47\\x49\\x46\\x38' : 'GIF',

            '\\x50\\x4b\\x03\\x04' : 'ZIP',

            '\\x7fELF' : 'ELF',

            '\\x25\\x50\\x44\\x46' : 'PDF',

            '\\x49\\x44\\x33' : 'MP3',

            '\\xff\\xfb' : 'MPEG',

            '\\x00\\x00\\x01\\x00' : 'PDDF',

            '\\x00\\x01\\x00\\x00' : 'ICO'

            }

    result = []

    for i,j in keys.items():

        if i in data:

            result.append(j) 

    return result  

n = input()

print(data_recovery(n[2:len(n)-1]))