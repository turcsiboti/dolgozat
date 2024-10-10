hálózat=[]
with open('hálózat.txt', 'r', encoding='utf-8') as forras, \
     open('hálózat_adat.txt', 'w', encoding='utf-8') as cel:
    fejlec = forras.readline()
    
    
    for sor in forras:
        adat = sor.strip().split(',')

    for elem in hálózat:
        if len(adat) >=5:
            háló = {
                'szerzo': adat[0],
                'cim': adat[1],
                'kiadas': adat[2],
                'ISBN': adat[3],
                'alapot': adat[4]
            }
            hálózat.append(háló)
        
    
            print(elem, file=cel)
print(f'{hálózat}')