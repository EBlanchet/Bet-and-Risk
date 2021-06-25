# Bet-and-Risk #

## Introduction ##

### Objectifs ###

Des ingénieurs ont perdu le code d’un jeu nommé Bet & Risk, l’objectif est de réécrire celui-ci afin d’obtenir un rendu similaire à celui retrouvé par les ingénieurs et que le jeu corresponde à leurs souvenirs.

### Démarche Logique et Mathématiques ###

La première approche du projet fut très factuelle, nous avons commencé par une tentative d’écriture complète d’un code permettant de retrouver un rendu égal à celui retrouvé par les ingénieurs. Lorsque ceci fut effectué, nous avons vérifié que le jeu proposé par notre code permettait de répondre aux attentes des ingénieurs (leurs souvenirs). La réflexion globale du groupe fut plus technique qu’abstraite.

## Documentation Technique ##

### Démarche Programmation ###

Le programme débute par un zone d’initialisation où on importe randint et seed du module random et où on affecte quelques variables qui nous seront utile ensuite.

La boucle principale du jeu démarre ensuite. C’est une boucle while faisant fonctionner le jeu qui reste active jusqu’à ce que le joueur perde ou décide d’arrêter. Cette boucle contient notamment le code des différentes commandes qui se trouvent dans les manuels d’utilisation.

Dans ces diverses commandes se trouve lancer. C’est lorsque l’utilisateur entre cette commande qu’une partie de Bet & Risk démarre : Les dés sont lancés et le joueur mise (avec un système de saisie contrôlée).
Il fallait ensuite calculer la somme des deux dés les plus élevés du joueur et de la banque. Ayant réfléchit au préalable à propos du quitte ou double et voulant utiliser le même système ici en créant peu de variable, nous avons réalisé un petit algorithme permettant au programme de « trier » les dés pour ne garder que les deux plus élevés. Cela nous a donc permis en peu de ligne de créer un système simple et efficace ne nécessitant que 3 variables pour le joueur et 3 pour la banque pour calculer la somme des deux meilleurs dés. Cet algorithme est présent ligne 71 pour les 3 premiers dés de la banque et ligne 111 pour le quitte ou double.

Après cela, on détecte qui du joueur ou de la banque gagne. Si le joueur perd et que le programme est en version 2, on entre dans la boucle while du quitte ou double qui permet à chaque itération de choisir de quitter ou doubler. Lorsque l’on double, les dés sont lancés, l’algorithme de « tri » sélectionne les deux dés les plus élevés parmi les deux anciens et le nouveau puis on calcule la somme. Le temps que le joueur perd, a suffisamment d’argent et ne quitte pas, on reste dans la boucle. Sinon on peut recommencer une nouvelle partie.

## Manuels d'Utilisation ##

### Manuel Utilisateur ###

Pour jouer, vous avez accès à différentes commandes :

    lancer (Lancer les dés et commencer à jouer)
    consulter (Vérifier l'argent que vous avez)
    terminer (Quitter le jeu)
    
Lorsque le programme vous le demande, vous devez entrer une mise (nombre entier positif inférieur ou égal à votre argent)

Enfin, en cas de défaite ou d'égalité, vous pouvez faire un quitte ou double:

    quitte (Met fin au pari)
    double (Double la mise, le joueur et la banque retirent un dé)
    
La saisie d'une commande se fait à l'affichage d'un $ et la saisie de la mise à l'affichage d'un €

### Manuel Développeur ###

Commandes supplémentaires pour les développeurs :

    version (Vérifie la version actuelle du jeu)
    v1 (Passe le jeu en version 1 (sans quitte ou double)
    v2 (Passe le jeu en version 2 (avec quitte ou double)
    graine (Permet d'entrer un nombre entier pour fixer la graine du générateur aléatoire)

## Conclusion ##

### Conclusion ###

Nous avons donc réussis à reproduire le jeu Bet & Risk des ingénieurs et avoir un rendu similaire sans trop de difficultés. Nous trouvons notre programme satisfaisant bien que nous pensons qu’on pourrait l’améliorer et l’optimiser notamment avec des fonctions.
Quant à notre groupe, le travail et la réflexion y a été plutôt efficace. Et nous avons bien réussis à communiquer ensemble principalement avec Discord.
