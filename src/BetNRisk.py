###############################################################################
#                          Problème : Bet & Risk                            #
###############################################################################

#Importation des modules necessaires
from random import randint,seed

#Initialisation
argent = 10
argentObjectif = argent * 2
jeu = True
version2 = True

#Boucle principale du jeu
while jeu:
    commande = input("$ ")
    
    #Gestion versions
    if commande == "version":
        if version2:
            print("v2")
        else :
            print("v1")
    elif commande == "v1":
            version2 = False
    elif commande == "v2":
            version2 = True    
    
    #Commande pour fixer la graine
    elif commande == "graine":
        seed(int(input("$ ")))
        
    #Commande pour terminer le jeu
    elif commande == "terminer":
        if argent >= argentObjectif:
            print("Bravo, vous avez doublé votre mise initiale !")
        else:
            print("Désolé vous n'avez pas doublé votre mise initiale !")
        jeu = False
        
    #Commande pour vérifier son argent
    elif commande == "consulter":
        print(f"Vous avez {argent}€")
        
    #Commande pour commencer la partie
    elif commande == "lancer":
        
        #Premier tir joueur et banque
        joueurD1 = randint(1,6)
        banqueD1 = randint(1,6)
        print(f"Vous avez tiré un {joueurD1}\nLa banque a tiré un {banqueD1}")
        
        #Mise du joueur
        attenteMise = True
        while attenteMise:
            mise = int(input("Votre mise ?\n€ "))
            if mise <= 0 or mise > argent:
                print(f"Pas possible !\nPour info, vous avez {argent}€")
            else:
                attenteMise = False
                
        #Second tir joueur et banque
        joueurD2 = randint(1,6)
        banqueD2 = randint(1,6)
        banqueDBonus = randint(1,6)
        print(f"Vous avez maintenant tiré un {joueurD2}")
        print(f"La banque a aussi tiré un {banqueD2} et un {banqueDBonus}")
        
        #Enregistrement des 2 dés les plus grands
        if banqueDBonus > banqueD1:
            banqueDBonus,banqueD1 = banqueD1,banqueDBonus
        elif banqueDBonus > banqueD2:
            banqueDBonus,banqueD2 = banqueD2,banqueDBonus
            
        #Calcul somme des dés
        joueurDSomme = joueurD1 + joueurD2
        banqueDSomme = banqueD1 + banqueD2
        print(f"Votre somme : {joueurDSomme}")
        print(f"Celle de la banque : {banqueDSomme}")
        
        #Verification gain
        if joueurDSomme > banqueDSomme:
            print("Gagné !")
            argent += mise
        else:
            if joueurDSomme == banqueDSomme:
                print("Egalité !")
            else:
                print("Perdu !")
             
            #Quitte ou double
            quitteOuDouble = True
            while quitteOuDouble:
                if argent >= mise*2 and version2:
                    print("Quitte ou double ?")
                    commande = input("$ ")
                    if commande == "quitte":
                        argent -= mise
                        quitteOuDouble = False
                    elif commande == "double":
                        mise *= 2
                        
                        #Tir bonus joueur et banque
                        joueurDBonus = randint(1,6)
                        banqueDBonus = randint(1,6)
                        print(f"Vous avez maintenant tiré un {joueurDBonus}")
                        print(f"La banque a aussi tiré un {banqueDBonus}")
                        
                        #Enregistrement des 2 dés les plus grands
                        if joueurDBonus > joueurD1:
                            joueurDBonus,joueurD1 = joueurD1,joueurDBonus
                        elif joueurDBonus > joueurD2:
                            joueurDBonus,joueurD2 = joueurD2,joueurDBonus
                        if banqueDBonus > banqueD1:
                            banqueDBonus,banqueD1 = banqueD1,banqueDBonus
                        elif banqueDBonus > banqueD2:
                            banqueDBonus,banqueD2 = banqueD2,banqueDBonus
                            
                        #Calcul somme des dés
                        joueurDSomme = joueurD1 + joueurD2
                        banqueDSomme = banqueD1 + banqueD2
                        print(f"Votre somme : {joueurDSomme}")
                        print(f"Celle de la banque : {banqueDSomme}")
                        
                        #Verifiction gain
                        if joueurDSomme > banqueDSomme:
                            print("Gagné !")
                            argent += mise
                            quitteOuDouble = False
                        elif joueurDSomme == banqueDSomme:
                            print("Egalité !")
                        else:
                            print("Perdu !")
                                
                    else:
                        print("Commande Inconnue")
                else:
                    argent -= mise
                    quitteOuDouble = False
                    
        #Plus d'argent
        if argent <= 0:
            print("Vous n'avez plus d'argent...")
            jeu = False
        
    else:
        print("Commande Inconnue")