# https://quera.org/problemset/244102

class city:
    def __init__(self, **kwargs):
        self.city_name = city_name
        self.city_neighbour = city_neighbour
        

if __name__ == '__main__':
    
    # make city layout with a dict that key is city name and value is city neighbours
    city = {}
    city[1] = [2,3,4]
    city[2] = [1,3,4,5,6]
    city[3] = [1,2,4,6,7]
    city[4] = [1,2,3,5,6,7]
    city[5] = [2,4,6]
    city[6] = [2,3,4,5,7]
    city[7] = [3,4,6]
    
    c = int(input())
    r = int(input())
    
    count = 0
    while c != r:
        
        if r in city[c]:
            count += 1
            print(count)
            break
        
        else:
            # best place for c is 4 because it have acces to all other places
            c = 4
            
            # now try to move r to a place far from c
            for i in city[r]:
                if c not in city[i] and i != c:
                    r = i
                    break

        count += 1
        
    
    