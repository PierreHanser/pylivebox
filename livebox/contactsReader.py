#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
fabrique des objects "contacts" au sens de la livebox,
en lisant un fichier avec des lignes de la forme

# commentaire
nom prenom telephone # commmentaire
nom telephone

le '#' debute un commentaire

"""
from pprint import pprint as pp

def do1line(lIn):

    lIn = lIn.strip()
    # supprime les commentaires
    if "#" in lIn:
        l = lIn.split("#")[0]
    else:
        l = lIn
    l = l.strip()
    if not l:
        # trace les erreurs du fichier d'entrée, mais pas les lignes vides
        if lIn:
            print("line ignorée: %s" % lIn)
        return None

    items = l.split()
    if len(items) < 2:
        print("line incorrecte: %s" % lIn)
        return None
    elif len(items) == 2:
        name = "N:%s;;" % items[0]
        formattedName = name
        tel = items[1]
    else:
        name = "N:%s;%s;" % (items[0], " ".join(items[1:-1]))
        formattedName = " ".join(items[0:-1])
        tel = items[-1]

    contact = {}
    contact['name'] = name
    contact['formattedName'] = formattedName
    contact['ringtone'] = "1"
    # le type de telephone est HOME CELL ou WORK
    if tel.startswith("06") or tel.startswith("07"):
        contact['telephoneNumbers'] = [{u'preferred': False, u'type': u'CELL', u'name': tel, u'key': u'2'}]
    elif "boulot" in items or "" in items:
        contact['telephoneNumbers'] = [{u'preferred': False, u'type': u'WORK', u'name': tel, u'key': u'3'}]
    else:
        contact['telephoneNumbers'] = [{u'preferred': False, u'type': u'HOME', u'name': tel, u'key': u'1'}]

    return contact


def read1file(fileName):

    allContacts = []
    try:
        f = open(fileName, "r")
    except:
        print("file not found: %s" % fileName)
        return
    for line in f.readlines():
        res = do1line(line)
        if res:
            allContacts.append(res)
    return allContacts

def readMainFile():

    return read1file("./contacts-fixe.txt") 

if __name__ == "__main__":

    pp(readMainFile())

