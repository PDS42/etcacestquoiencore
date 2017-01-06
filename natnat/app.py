import json
import sys


# entries = [
#     "ET CA DANS MON FIL D’ACTUALITE",
#     "ET CA C EST QUOI A DROITE DE MON FB",
#     "ET C EST QUOI A DROITE DE FIL D’ACTUALITE",
#     "VOUS VOUS FOUTEZ DE MA GUEULE ENCORE DEBILES MENTALES",
# ]


# body = [
#     "ET TOUTES LES MAGOUILLES ORDURIERES",
#     "ET POUR ME POURRIR MA VIE EN TOUT POINT DE VU",
#     "ET PAR LE BIAIS DE N IMPORTE QUOI",
#     "ET MOI ET MON FILS ET LES ANIMAUX",
#     "ET POUR ME POURRIR MA VIE EN TOUT POINT DE VU",
#     "ET VOUS ET LES AUTRES DEBILES MENTAUX",
#     "ET JE MANGEAIS DU JAMBON DE DINDE ET DU PAIN",
#     "ET SALADE ET ON ETAIT AU TELEPHONE ET JE FAISAIS DU MENAGE ETC",
#     "ET TOUTES LES MAGOUILLES ORDURIERES",
#     "ET DE TOUT ORDRE ET DEPUIS DES ANNEES",
#     "ET POUR ME FOUTRE MA VIE EN L AIR ET CELLE DE MON FILS ET DES ANIMAUX ET D AUTRES AUSSI",
#     "TOUTES ET TOUS CES DEBILES DE PARTOUT",
# ]



# end = [
#     "ET DEPUIS DES ANNEES",
#     "ET TOUT CE QUI S’EN SUIT"
# ]


try:
    while 1:
        with open('../data.json') as data_file:
            data = json.load(data_file)
        entries = data['entries']
        body = data['body']
        end = data['end']
        for line in sys.stdin:
            line = line.split(',')
            if line[1] == "1\n":
                if line[0].strip() not in entries:
                    entries.append(line[0].strip()) 
                else:
                    print("already in")
            elif line[1] == "2\n":
                if line[0].strip() not in body:
                    body.append(line[0].strip()) 
                else:
                    print("already in")
            elif line[1] == "3\n":
                if line[0].strip() not in end:
                    end.append(line[0].strip()) 
                else:
                    print("already in")
except KeyboardInterrupt:
    dict = {
        'entries' : entries, 
        'body' : body,
        'end' : end
    }
    with open('../data.json', 'w', encoding='utf8') as outfile:
        json.dump(dict, outfile, indent=4)
    outfile.close()
    with open('data.txt', 'w', encoding='utf8') as outfile:
        json.dump(dict, outfile, indent=4)
    outfile.close()