<h1 style="text-align: center; ">Modèle de diffusion d'une maladie dans une population d'agents mobiles</h1>

<h2 style="text-align: center; ">Sommaire</h2>

-   Introduction
-   Présentation du modèle
    -   Les variables
    -   Les agents
        -   Leurs interactions
-   Exprériences et résultats
-   Conclusion

Le but de cette étude est de mettre en place une simulation de diffusion d'une maladie dans une population d'agents mobiles et d'étudier les différents moyens d'endiguer la maladie. Dans nos expériences, nous ferons varier différents paramètres de la simulation, comme le nombre d'agents, le temps, le nombre d'agents contaminés au temps zéro, etc. Nous présenterons ici les différentes méthodes d'endiguage de la maladie ainsi que les résultats obtenus.

## Présentation du modèle

### Définition des variables

La première étape consiste à définir les différents paramètres de la simulation. Nous aurons donc:

-   une durée de simulation
-   un nombre d'agents
-   un nombre d'agents contaminés au temps zéro
-   un degrés de confinement de la population
-   un degrés de de respect des gestes barrières

### Présentation des agents

Nos agents sont représentés par des cercles de coordonnées (x, y) et de rayon (r). Ils possèdent un état de contamination booléen, une probabilité de contamination (p), un état de guérison booléen et un état d'imunité boolean. Ces états sont modifiés par les interactions entre les agents et des durées définies qui cherchent à être les plus proches de la réalité. Les agents évoluent dans un monde carré de dimension (w, h) et sont placés aléatoirement dans ce monde avec une vitesse (vx, vy), elle aussi aléatoire.

### Définition des intéractions

Il n'existe qu'un seul type d'interaction entre nos agents. C'est l'interaction de contagion. Lorsqu'un agent est contaminé, il peut infecter d'autres agents mais ne peut plus être contaminé. Pour qu'un agent sain se fasse contaminé, il doit respecter certaines conditions. Il doit être un rayon de contamination (ir) défini. Il doit être sain, ne pas être immunisé et ne pas être vacciné.
