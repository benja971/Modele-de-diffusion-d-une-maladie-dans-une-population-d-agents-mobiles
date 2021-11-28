<h1 style="text-align: center; ">Modèle de diffusion d'une maladie dans une population d'agents mobiles</h1>

<h2 style="text-align: center; ">Sommaire</h2>

-   Introduction
-   Présentation du modèle
    -   Les variables
    -   Les agents
        -   Leurs interactions
-   Exprériences, résultats et limites

-   Conclusion

<div style="page-break-after: always;"></div>

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

## Exprériences et résultats

Dans toutes nos simulations nous utilisons un nombre d'agents fixé à 1000, un nombre d'agents contaminés au temps zéro fixé à 1 et un degré de contamination à 3.5%.

Avant de commencer à endiguer la maladie, nous avons simuler l'évolution de celle-ci sans mesures de restrictions. Voici le résultat obtenu:

![Natural immunity only](./Courbes/1000_agents_1_contaminé_5_ans/Natural_immunity_only.png)

On observe des vagues de guérisons et de contaminations qui s'étendent jusqu'à la fin de la simulation. Ces vagues sont dues au fait que nos agents obtinnent une immunité naturelle temporaire après chaque guérison.

### Exprériences, résultats et limites

Nous avons mit en place plusieurs expériences pour tenter de ralentir ou d'éradiquer la maladie. Pour chaque expérience, nous avons conserver les mêmes paramètres pour la simulation et répéter les simulations 5 fois pour réduire les incertitudes dues à l'aléatoire.

Comme première expérience nous avons décidé de confiner la population. Pour ce faire nous divisons les valeurs de vx et vy par deux, puis par trois et enfin par cinq. Ce qui nous ramène à trois tests que nous appellons "confinement leger", "confinement moyen" et "confinement strict". Ceci entraine une réduction des interactions entre les agents. On cherche à connaître quel niveau de confinement permettrait d'éradiquer la maladie et sur quelle durée il faudrai le mettre en place.

Dans un deuxieme temps, nous avons décidé de mettre en place un respect des gestes barrières suivant. Cette méthode cherche à réduire la probabilité qu'un agent contaminé transmette la maladie à un autre agent lors de leur rencontre. Pour ce faire, nous avons mit en place trois intensités: "Basics barrier gestures", "Mediums barrier gestures" et "Heavys barrier gestures" qui réduisent par deux, trois et cinq la probabilité d'infection. Dans ce cas, on veut savoir jusqu'à quel niveau les gestes barrières peuvent ralentir la maladie.

Nous avons ensuite instauré un cycle de vaccination. En effet, dans la simulation, chaque jour, nous vaccinons un nombre d'agents définits au préalable.Le vaccin donne une imunité plus longue que celle obtenue naturellement. Au seins même de cette expérience nous avons pu tester plusieurs choses. Dans un premier temps, les agents n'effectuent qu'une seule vaccination qui les imunisent un certain temps mais finissent par attraper la maladie à la fin de leur prériode de vaccination.

Par la suite, nous avons implémenté les rappels de vaccins. Nous revaccinons les agents dès lors que leur vaccin ne fait plus effet. On regarde donc le seuil minimal de personnes à vacciner par jour pour que la maladie soit éradiquée.
