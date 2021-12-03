# Modèle de diffusion d'une maladie dans une population d'agents mobiles

Création d'un modèle d'une population d'agents mobiles se transmettant une maladie.

Les agents qui constituent la population (taille paramétrable) sont dans l'un des (au moins) trois états :

S : sain
I : infecté
R : rétabli (le R est pour recovered)
En cas de contact (à définir/paramétrable) avec un agent I, un agent S peut devenir I avec une certaine probabilité (paramétrable). Un agent I peut, soit mourir, avec une certaine probabilité (paramétrable), soit guérir, avec une certaine probabilité (paramétrable).

Les agents se déplacent suivant un modèle de déplacement (à définir/paramétrable).

Vous pourrez étudier l'influence des paramètres sur :

le taux de contaminés après un nombre d’itération
le nombre de morts
le nombre de contaminés en fonction du temps
Vous pourrez également mesurer l'incidence de l’introduction d'un vaccin (passage I -> R), ou des tests (deux états infectieux : U et K, pour respectivement malade ne connaissant pas son état, et malade connaissant son état), avec traitement différencié
