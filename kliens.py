kliensek=[]
with open('kliensek.txt','r', encoding='utf-8') as forras,\
    open ('kliensek_adat.txt','w',encoding='utf-8') as cel:
    fejletc=forras. readline()
    for sor in forras:
        adat=sor.strip().split(',')
        kliens={'allomas': adat [0] ,'ip':adat[1], 'halozat':adat[2],}
        kliensek.append(kliens)
        print(kliensek,file=cel)
print(f'{kliensek}')