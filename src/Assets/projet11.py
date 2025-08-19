# coding: UTF-8
"""
Script: SAE15/projet11
Création: pingetm, le 12/11/2021
"""


# Imports

# Fonctions

# Programme principal
import numpy as np

import tools_constantes
import tools_date
import tools_sae
import matplotlib.pyplot as plt
import os

def extract_events(n):
    d1 = n.find("BEGIN:VEVENT") #search for the first "BEGIN:VEVENT
    f1 = n.find("END:VEVENT")#search for the first "END:VEVENT
    l1 = []
    while d1 != -1: #loop that checks if there is still a "BEGIN:VEVENT"
        l1.append(n[(d1+13):(f1-1)] + "\n") #add lines from d1 without "BEGIN:VEVENT" to f1 without "END:VEVENT" with a line break
        d1 = (n.find("BEGIN:VEVENT",d1 + 1)) #find out where the next "BEGIN:VEVENT" is by adding +1
        f1 = (n.find("END:VEVENT",f1 + 1)) #find out where the next "END:VEVENT" is by adding +1
    return l1

def conversion_date(d):
    jour = ''
    mois = ''
    annee = ''
    for i in range(4):
        annee += d[i] #add to the string "year" the first 4 characters of "d"
    for i in range(4,6):
        mois += d[i] #add to the string str "month" the characters from 4 to 6 of "d"
    for i in range(6,8):
        jour += d[i] #add to the string str "day" the characters from 6 to 8 of "d"
    conversion = (f'{jour}-{mois}-{annee}')
    return conversion

def conversion_heure(d):
    heure = ''
    minute = ''
    for i in range(2):
        heure += d[i]  #add to the string str "time" the first 2 characters of "d"
    for i in range(3,5):
        minute += d[i] #add to the string str "minute" the characters 3 to 5 of "d"
    conversion = (f'{heure}:{minute}')
    return conversion

def calcul_duree(debut,fin):
    heured = ''
    heuref = ''
    minuted = ''
    minutef = ''
    for i in range(2):
        heured += debut[i] #add to the string str "heured" the first 2 characters of "debut"
        heuref += fin[i] #add to the string str "hourf" the first 2 characters of "end"
    for i in range(3,5):
        minuted += debut[i] #add to the string "minuted" the characters 3 to 5 of "debut"
        minutef += fin[i] #add to the string str "minutef" the characters 3 to 5 of "end"
    converminute1 = (int(heured)*60)+int(minuted) #multiply "hourd" by 60 to get it in minutes and add it to "minuted" to put them in the same unit
    converminute2 = (int(heuref)*60)+int(minutef)  #multiply "hourf" by 60 to get it in minutes and add it to "minutef" to put them in the same unit
    dureemin = converminute2 - converminute1 #subtract "converminute2" by "converminute1" to get the time in minutes it separates them
    dh = dureemin//60 #euclidean division of "dureemin" by 60 to retrieve the time
    dm = dureemin%60 #modulo of 'dureemin' by 60 to get the rest in minutes
    if dh <= 10 and dm == 0: #check that dh is less than or equal to 10 and that dm is equal to 0
        return (f'0{dh}:{dm}0') #return a str string with the requested format 09:00
    elif dh <= 10: #verification that dh is less than or equal to 10
        return (f'0{dh}:{dm}') #return a str string with the requested format 09:01
    elif dm == 0:#verify that dm is equal to 0
        return (f'{dh}:{dm}0') #return a string str with the requested format 10:00
    else:
        return (f'{dh}:{dm}') #return a string str with the requested format 10:01

def parse_event(event):
    liste = event.split("\n") #separates event from each "\n"
    uid = tools_sae.get_event_by_id(liste, "UID").split(":")[1] #Search for UID and take the occurrence after the ':'
    date_debut = tools_sae.get_event_by_id(liste, "DTSTART").split(":")[1] #Search for DTSTART and take the occurrence after the ':'
    date_fin = tools_sae.get_event_by_id(liste, "DTEND").split(":")[1] #Search for DTEND and take the occurrence after the ':'
    groupe = tools_sae.get_event_by_id(liste, "CATEGORIES").split(":")[1] #Search for CATEGORIES and take the occurrence after the ':'
    matiere = tools_sae.get_event_by_id(liste, "SUMMARY").split(":")[1] #Search for SUMMARY and take the occurrence after the ':'
    salle = tools_sae.get_event_by_id(liste, "LOCATION").split(":")[1] #Search for LOCATION and take the occurrence after the ':'
    date3 = conversion_date(date_debut)
    heure_debut = conversion_heure(date_debut.split("T")[1]) #converts the time taken in date_debut after the "T"
    heure_fin = conversion_heure(date_fin.split("T")[1]) #converts the time taken in date_fin after the "T"
    duree = calcul_duree(heure_debut, heure_fin)
    modalite1 = matiere.split("-")[0] #take the modality in matiere before the "-"
    nb_modalite = matiere.count("-")
    prof = tools_sae.get_event_by_id(liste, "DESCRIPTION")
    if prof is not None: # if the prof variable is not empty
        prof = (prof.split(":")[1]).replace(",", "|") # take the occurrence after ":" and replace the "," with "|"
    if salle.find(",") != -1: # if there is a ',' in salle
        salle = salle.replace(",", "|")
    if groupe.find(",") != -1:  # if there is a ',' in groupe
        groupe = groupe.replace(",", "|")

    if prof is None and nb_modalite > 1:
        modalite2 = matiere.split("-")[1] # takes the occurrence after "-" in matiere
        return (f'{uid};{date3};{heure_debut};{duree};{modalite1};{modalite2};{matiere};{salle};;{groupe}')
    if nb_modalite > 1 and prof is not None:
        modalite2 = matiere.split("-")[1]
        return (f'{uid};{date3};{heure_debut};{duree};{modalite1};{modalite2};{matiere};{salle};{prof};{groupe}')
    if prof is None:
        return (f'{uid};{date3};{heure_debut};{duree};Autre;;{modalite1};{matiere};{salle};{groupe}')
    if nb_modalite > 1:
        modalite2 = matiere.split("-")[1]
        return (f'{uid};{date3};{heure_debut};{duree};{modalite1};{modalite2};{matiere};{salle};{groupe}')
    else:
        return (f'{uid};{date3};{heure_debut};{duree};Autre;;{matiere};{salle};{prof};{groupe}')

def parse_fichier_ics(fichier_ics):
    fichier_rtn = []
    fichier_c = tools_sae.lecture_fichier(fichier_ics) # conversion of fichier_ics to string
    fichier_e = extract_events(fichier_c) # extract events from file_c
    for i in range(len(fichier_e)):
        fichier_rtn.append(parse_event(fichier_e[i])) # add the information in a good format line by line in the list fichier_rtn
    return fichier_rtn

def nombre_minutes(temps):
    heure = ''
    minute = ''
    for i in range(2):
        heure += temps[i]  # add to the string heure the first 2 characters of temps
    for i in range(3,5):
        minute += temps[i] # add to the minute string the characters from 3 to 5 of temps
    h_en_m = int(heure)*60 # conversion from hour to minute
    nb_min_t = h_en_m + int(minute) # addition of minutes
    return nb_min_t

def compare_dates(date1,date2):
    jour1 = ''
    mois1 = ''
    annee1 = ''
    jour2 = ''
    mois2 = ''
    annee2 = ''
    for i in range(6,10):
        annee1 += date1[i] # add to the string "annee1" the characters from 6 to 10 of "d1"
        annee2 += date2[i]
    for i in range(3,5):
        mois1 += date1[i] # add to the string "mois1" the characters from 3 to 5 of "d1"
        mois2 += date2[i]
    for i in range(2):
        jour1 += date1[i] # add to the string "jour1" the first 2 characters of "d1"
        jour2 += date2[i]
    r1 = {f'{jour1}-{mois1}-{annee1}'}
    r2 = {f'{jour2}-{mois2}-{annee2}'}
    if r1 == r2: # comparison of the 2 strings of characters
        return 0
    if annee1 < annee2: # "annee1" and "annee2" comparisons
        return -1
    if annee2 < annee1:
        return 1
    if mois1 < mois2:# "mois1" and "mois2" comparisons
        return -1
    if mois2 < mois1:
        return 1
    if jour1 < jour2:# "jour1" and "jour2" comparisons
        return -1
    if jour2 < jour1:
        return 1

def calcul_heure_fin(hd,duree):
    heure_debut = ''
    minute_debut = ''
    heure_duree = ''
    minute_duree = ''
    for i in range(2):
        heure_debut += hd[i] #  add to the string "heure_debut" the first 2 characters of "hd"
        heure_duree += duree[i]
    for i in range(3, 5):  # browse the characters from 3 to 5
        minute_debut += hd[i] # add to the string "minute_debut" the characters from 3 to 5 of "hd"
        minute_duree += duree[i]
    conver_hd = ((int(heure_debut))*60)+ int(minute_debut) #conversion from "heure_debut" to minute and addition to "minute_debut"
    conver_duree = ((int(heure_duree))*60)+int(minute_duree)
    add_conver = conver_duree+conver_hd
    hf = add_conver//60 #euclidean division to recover hours
    mf = add_conver%60 #modulo to retrieve minutes
    if hf <= 10 and mf == 0:  # check that "dh" is less than or equal to 10 and that "dm" is equal to 0
        return (f'0{hf}:{mf}0')  # return a str string with the requested format 09:10
    elif hf <= 10:  # verification that "dh" is less than or equal to 10
        return (f'0{hf}:{mf}')  # returns a string str with the requested format 01:11
    elif mf == 0:  # verify that dm is equal to 0
        return (f'{hf}:{mf}0')  # return a string str with the requested format 11:10
    else:  # if none of the above arguments fit
        return (f'{hf}:{mf}')

def date_dans_intervalle(d,dd,df):
    a = compare_dates(d, dd) #comparison of the given date with the start date
    b = compare_dates(d, df) #comparison of the given date with the end date
    if a == -1: # comparison with the return values of compare_dates
        return False
    if b == -1:
        return True
    if b == 1:
        return False
    if a == 0 or b == 0:
        return True

def nb_heures_module(events,code_module):
    CM = 0
    TP = 0
    TD = 0
    Projet = 0
    type = tools_constantes.MODALITES
    for event in events: #course of events to transform it into a str
        parsed_event = event.split(';') #separation of the different information of the envenment separated by a ';'
        for a in range(len(type)): #course of the number of different modalities
            is_type = tools_sae.get_event_by_id(parsed_event, type[a]) #verification of the presence of a modality
            is_code_module = tools_sae.get_event_by_id(parsed_event, code_module) #verification of the presence of a module
            if is_type and is_code_module:
                is_cm = tools_sae.get_event_by_id(parsed_event, "CM")#Search for CM in parsed_event
                is_tp = tools_sae.get_event_by_id(parsed_event, "TP")
                is_td = tools_sae.get_event_by_id(parsed_event, "TD")
                is_projet = tools_sae.get_event_by_id(parsed_event, "Proj")
                if is_cm:
                    CM1 = int(parsed_event[3].split(":")[0])*60 #takes the third occurrence of parsed-event and takes the int before the ":" and multiplies it by 60
                    CM2 = int(parsed_event[3].split(":")[1]) #takes the third occurrence of parsed-event and takes the int after the ":"
                    CM += (CM1+CM2)/60
                elif is_tp:
                    TP1 = int(parsed_event[3].split(":")[0])*60
                    TP2 = int(parsed_event[3].split(":")[1])
                    TP += (TP1+TP2)/60
                elif is_td:
                    TD1 = int(parsed_event[3].split(":")[0])*60
                    TD2 = int(parsed_event[3].split(":")[1])
                    TD += (TD1+TD2)/60
                elif is_projet:
                    Projet1 = int(parsed_event[3].split(":")[0])*60
                    Projet2 = int(parsed_event[3].split(":")[1])
                    Projet += (Projet1+Projet2)/60
    return [float(CM), float(TD), float(TP), float(Projet)]

def nb_heures_ue(events,liste_module):
    CM = 0.0
    TD = 0.0
    TP = 0.0
    Proj = 0.0
    for i in range(len(liste_module)): #module number path
        res = nb_heures_module(events,liste_module[i]) # calls the function nb_hours_module with the parameter events and the module in relation to the occurrence of the loop
        CM += res[0] #add occurrence 0 of the return of res in CM
        TD += res[1]
        TP += res[2]
        Proj += res[3]

    return '{};{};{};{}'.format(CM,TD,TP,Proj)

def traitement(events):
    UE1 = tools_constantes.UE1_RT1_Administrer
    UE2 = tools_constantes.UE2_RT2_Connecter
    UE3 = tools_constantes.UE3_RT3_Programmer
    nb_h_ue1 = nb_heures_ue(events,UE1).split(';') #call of the function nb_hours_ue with the parameter events and the different modules of the UE1
    nb_h_ue2 = nb_heures_ue(events, UE2).split(';')
    nb_h_ue3 = nb_heures_ue(events, UE3).split(';')
    resUE1 = 'UE1-RT1-Administrer;{};{};{};{}'.format(nb_h_ue1[0],nb_h_ue1[1],nb_h_ue1[2],nb_h_ue1[3]) #setting up the correct formant using the occurrences of the return value of nb-h-ue1
    resUE2 = 'UE2-RT2-Connecter;{};{};{};{}'.format(nb_h_ue2[0],nb_h_ue2[1],nb_h_ue2[2],nb_h_ue2[3])
    resUE3 = 'UE3-RT3-Programmer;{};{};{};{}'.format(nb_h_ue3[0],nb_h_ue3[1],nb_h_ue3[2],nb_h_ue3[3])
    return [resUE1,resUE2,resUE3]

def export_markdown(res_traitement):
    file = open("Resultat_markdown.md", "w") #creating a markdown file
    data = []
    res1 =''
    for i in range(len(res_traitement)):
        sepUEs = res_traitement[i] #separation of the different UEs
        sepInterne = sepUEs.split(';') #separation of the internal elements of the UE which are separated by a ';'
        data.append(sepInterne)
    res1 += ("| UEs | Heures CM | Heures TD | Heures TP | Heures Projet |") #add string to res1
    res1 += ("\n")
    res1 += ("| :-------------- | :-------------------| :-------------------| :-------------------| :-------------------|")
    res1 += ("\n")
    res1 += (f"|{(data[0])[0]} | {(data[0])[1]} | {(data[0])[2]} |{(data[0])[3]}|{(data[0])[4]}|") # addition of data in relation to their UEs and internal UE occurrence
    res1 += ("\n")
    res1 += (f"|{(data[1])[0]} | {(data[1])[1]} | {(data[1])[2]} |{(data[1])[3]}|{(data[1])[4]}|")
    res1 += ("\n")
    res1 += (f"|{(data[2])[0]} | {(data[2])[1]} | {(data[2])[2]} |{(data[2])[3]}|{(data[2])[4]}|")
    file.write(res1) # add all the strings in the file created beforehand
    return res1

def export_png(res_traitement):
    data = []
    for i in range(len(res_traitement)):
        sepUEs = res_traitement[i] #separation of the different UEs
        sepInterne = sepUEs.split(';') #separation of the internal elements of the UE which are separated by a ';'
        data.append(sepInterne)
    res1 = float((data[0])[1])+float((data[0])[2])+float((data[0])[3])+float((data[0])[4]) # addition of the totality of the UE modalities
    res2 = float((data[1])[1]) + float((data[1])[2]) + float((data[1])[3]) + float((data[1])[4])
    res3 = float((data[2])[1]) + float((data[2])[2]) + float((data[2])[3]) + float((data[2])[4])
    rest = res1 + res2 + res3
    resp1 = (res1/rest) * 100 # creation of a percentage of the totality of each Ue
    resp2 = (res2/rest) * 100
    resp3 = (res3/rest) * 100
    fig, axs = plt.subplots(1, 4, figsize=(10, 10), sharey=True ) # setting the page size and number of graphics on the same window
    fig.suptitle('Graphiques des UEs')
    labels = 'UE1-RT1-Administrer', 'UE2-RT2-Connecter', 'UE3-RT3-Programmer'
    sizes = [resp1,resp2,resp3] #distribution of the different percentages
    colors = ['yellowgreen', 'gold', 'lightskyblue']
    axs[0].pie(sizes, labels=labels, autopct='%1.1f%%',colors=colors,
            shadow=True, startangle=90)
    axs[0].axis('equal')
    labels = 'UE1-CM', 'UE1-TD', 'UE1-TP','UE1-Proj'
    sizes = [((float((data[0])[1])/res1)*100), ((float((data[0])[2])/res1)*100), ((float((data[0])[3])/res1)*100),((float((data[0])[4])/res1)*100)] #distribution of each percentage but according to UE only
    colors = ['yellowgreen', 'gold', 'lightskyblue','red']
    axs[1].pie(sizes, labels=labels, autopct='%1.1f%%', colors=colors,
            shadow=True, startangle=90)
    axs[1].axis('equal')
    labels = 'UE2-CM', 'UE2-TD', 'UE2-TP','UE2-Proj'
    sizes = [((float((data[1])[1])/res2)*100), ((float((data[1])[2])/res2)*100), ((float((data[1])[3])/res2)*100),((float((data[1])[4])/res2)*100)]
    colors = ['yellowgreen', 'gold', 'lightskyblue','red']
    axs[2].pie(sizes, labels=labels, autopct='%1.1f%%', colors=colors,
            shadow=True, startangle=90)
    axs[2].axis('equal')
    labels = 'UE3-CM', 'UE3-TD', 'UE3-TP','UE3-Proj'
    sizes = [((float((data[2])[1])/res3)*100), ((float((data[2])[2])/res3)*100), ((float((data[2])[3])/res3)*100),((float((data[2])[4])/res3)*100)]
    colors = ['yellowgreen', 'gold', 'lightskyblue','silver']
    axs[3].pie(sizes, labels=labels, autopct='%1.1f%%', colors=colors,
            shadow=True, startangle=90)
    axs[3].axis('equal')

    plt.savefig('GrpahiqueUEs.png') # save the graphic as a png file
    plt.show() # open the graph window

def main():
    file = tools_sae.lecture_fichier("tests/data/data.csv").split('\n')
    file = [i for i in file if len(i) > 1]
    res = (traitement(file))
    export_markdown(res)
    export_png(res)
if __name__ == '__main__':
    main()
# Fin
