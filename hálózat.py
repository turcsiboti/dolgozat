halozat=[]
with open('halozat.txt','r', encoding='utf-8') as forras,\
    open ('halozat_adat.txt','w',encoding='utf-8') as cel:
    fejletc=forras. readline()
    for sor in forras:
        adat=sor.strip().split(',')
        halo={'szerzo': adat [0] ,'cm':adat[1], 'kiads':adat[2], 'ISBN':adat[3], 'alapot':adat[4],}
        halozat.append(halo)
        print(halozat,file=cel)
print(f'{halozat}')