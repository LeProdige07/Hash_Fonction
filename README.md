# Fonction de hachage
## Structure de la fonction de hachage
Cette fonction de hachage reçoit en entrée une valeur de longueur arbitraire et donne en sortie une valeur de hachage de longueur *-20-*.
La valeur de hachage est composée de *20 caractères*.
Notre fonction de hachage est composée des certaines opérations dont : 

    - une opération de permutation;
    - une opération de rotation;
    - une opération de compression des valeurs ascii de chaque caractère avec addition et soustraction;
    - une opération de conversion en héxadécimal;
    - une opération de substitution non-linéaire.
Toutes ces opérations nous permettent de mettre en place une fonction de hachage qui respecte les caractéristiques suivantes : 

    - déterministe;
    - fonction à sens unique;
    - sécurité entre les collisions(Fonction de hachage cryptographique);
    - rapidité;
    - resistance.

## Utilisation de la fonction de hachage
Nous y avons joint un exemple d'utilisation. Il suffit d'exécuter le fichier.
