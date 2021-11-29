<h1 align = "center" >Modèle de diffusion d'une maladie dans une population d'agents mobiles</h1>

<h2 align = "center">Sommaire</h2>

-   Introduction
-   Présentation du modèle
    -   Les variables
    -   Les agents
        -   Leurs interactions
-   Exprériences, résultats et limites

-   Conclusion

<div style="page-break-after: always;"></div>

<u>

## Présentation du modèle

</u>

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

<div style="page-break-after: always;"></div>

<u>

## Exprériences, résultats et limites

</u>

Dans toutes nos simulations nous utilisons un nombre d'agents fixé à 1000, un nombre d'agents contaminés au temps zéro fixé à 1 et un degré de contamination à 3.5%.

Avant de commencer les tests pour endiguer la maladie, nous avons simuler l'évolution de celle-ci sans mesures de restrictions. Voici le résultat obtenu:

<p align="center">
<image src = "./Courbes/1000_agents_1_contaminé_5_ans/Natural_immunity_only.png" style = "width: 420px; padding-top: 30px; padding-bottom: 30px">
</p>
On observe des vagues de guérisons et de contaminations qui s'étendent jusqu'à la fin de la simulation. Ces vagues sont dues au fait que nos agents obtiennent une immunité naturelle temporaire après chaque guérison.

<div style="page-break-after: always;"></div>

Nous avons mit en place plusieurs expériences pour tenter de ralentir ou d'éradiquer la maladie. Pour chaque expérience, nous avons conserver les mêmes paramètres pour la simulation et réitéré 5 fois. Nous utilisons la moyenne de ces simulations pour réduire les incertitudes dues à l'aléatoire.

1. Confinement

Comme première expérience nous avons décidé de confiner la population. Pour ce faire nous divisons les valeurs de vx et vy par deux, puis par trois et enfin par cinq. Ce qui nous ramène à trois tests que nous appelons respectivement "confinement léger", "confinement moyen" et "confinement strict" par rapport à leur taux de limitation. Ce taux fera baisser la possibilité de déplacement des agents jusqu'à la quasi-immobilité lorsque ce dernier vaut cinq. Ceci entraine donc une réduction des interactions entre les agents qui devrait limiter la dispersion de la maladie. On veut savoir si cette réduction est suffisante pour éradiquer la maladie. Et si oui, quel taux faut-il mettre en place et sûr combien de temps. Nous avons donc réalisé les simulations suivantes:

<div style="display: flex; padding-top: 30px; padding-bottom: 30px;">

<image src="./Courbes/1000_agents_1_contaminé_5_ans/Light_confinement.png"   style="width: 320px; padding-right: 10px" >

<image src = "./Courbes/1000_agents_1_contaminé_5_ans/Partial_confinement.png" style = "width: 320px;">

</div>

<p align="center"> 
<image src = "./Courbes/1000_agents_1_contaminé_5_ans/Strict_confinement.png" style = "width: 320px; padding-bottom: 20px;">
</p>

<div style="page-break-after: always;"></div>

Les graphiques ci-dessus représentent l'évolution de l'état des agents au cours de la simulation (temps en jour)en fonction du taux de confinement. <br>
On observe que la méthode de confinement est une facon très efficace de ralentir le déplacement de la maladie au sein de la population. On le constate clairement sur les graphiques du confinement léger et moyen. En effet, le pic de contamination initial est beaucoup moins important que celui de la simulation sans restrictions. Enfin, en se basant sur la courbe du confinement stricte, on confirme que cette méthode, malgré un degré très important de limitations, n'est pas suffisante pour éradiquer la maladie. On peut donc envisager de combiner cette dernière avec une autre méthode. Mais avant cela, nous avons testé si mettre en place un confinement de la population alors que la s'est déja bien propagé. Nous obtenons donc le résultat suivant:

<div style="display: flex; padding-top: 30px; padding-bottom: 30px;">

<image src="./Courbes/1000_agents_100_contaminé_5_ans/Light_confinement.png"   style="width: 320px; padding-right: 10px" >

<image src = "./Courbes/1000_agents_100_contaminé_5_ans/Partial_confinement.png" style = "width: 320px;">

</div>

<p align="center"> 
<image src = "./Courbes/1000_agents_100_contaminé_5_ans/Strict_confinement.png" style = "width: 320px; padding-bottom: 20px;">
</p>
2. Respect des gestes barrières

Dans un deuxième temps, nous avons décidé de mettre en place un respect des gestes barrières. Cette méthode cherche à réduire la probabilité qu'un agent contaminé transmette la maladie à un autre agent lors de leur rencontre. Pour ce faire, nous avons mit en place trois intensités: "Basics barrier gestures", "Mediums barrier gestures" et "Heavys barrier gestures" qui réduisent par deux, trois et cinq la probabilité d'infection. Dans ce cas, on veut savoir jusqu'à quel niveau les gestes barrières peuvent ralentir la maladie.

<div style="display: flex; padding-top: 30px; padding-bottom: 30px;">

<image src="./Courbes/1000_agents_1_contaminé_5_ans/Basics_barrier_gestures.png"   style="width: 320px; padding-right: 10px" >

<image src = "./Courbes/1000_agents_1_contaminé_5_ans/Mediums_barrier_gestures.png" style = "width: 320px;">

</div>

<p align="center"> 
<image src = "./Courbes/1000_agents_1_contaminé_5_ans/Heavys_barrier_gestures.png" style = "width: 320px; padding-bottom: 20px;">
</p>

<div style="page-break-after: always;"></div>

Ici, nous représentons l'évolution de l'état des agents au fil du temps (en jour) en fonction du degrés de respect de la population pour les gestes barrières. <br>
On voit clairement que les gestes barrières sont très efficaces pour réduire la transmission de la maladie même si les agents ne les suivent pas de manière stricte comme le montre le graphique "gestes barrières basiques". Encore une fois, cette méthode est efficace pour ralentir la transmission de la maladie. Grace au courbes, il est clair que les gestes barrières sont une très bonne pratique pour réduire la transmission de la maladie. De plus, comme le montre le graphique "gestes barrières strictes", si respectés sérieusement et dès les premiers jours, une épidémie peut facilement être évitée. Mais on peut aussi se demander si cette méthode serait aussi utile, si mise en place alors que l'épidémie est déjà en cours. Voici donc les résultats obtenus pour ce cas:

<div style="display: flex; padding-top: 30px; padding-bottom: 30px;">

<image src="./Courbes/1000_agents_100_contaminé_5_ans/Basics_barrier_gestures.png"   style="width: 320px; padding-right: 10px" >

<image src = "./Courbes/1000_agents_100_contaminé_5_ans/Mediums_barrier_gestures.png" style = "width: 320px;">

</div>

<p align="center"> 
<image src = "./Courbes/1000_agents_100_contaminé_5_ans/Heavys_barrier_gestures.png" style = "width: 320px; padding-bottom: 20px;">
</p>

3. Vaccination

Nous avons ensuite instauré un cycle de vaccination. En effet, dans la simulation, chaque jour, nous vaccinons un nombre d'agents définits au préalable.Le vaccin donne une imunité plus longue que celle obtenue naturellement. Au seins même de cette expérience nous avons pu tester plusieurs choses. Dans un premier temps, les agents n'effectuent qu'une seule vaccination qui les imunisent un certain temps mais finissent par attraper la maladie à la fin de leur prériode de vaccination.

<div style="display: flex; padding-top: 30px; padding-bottom: 30px;">

<image src="./Courbes/1000_agents_1_contaminé_5_ans/Vaccin01.png"   style="width: 320px; padding-right: 10px" >

<image src = "./Courbes/1000_agents_1_contaminé_5_ans/Vaccin03.png" style = "width: 320px;">

</div>
<div style="display: flex; padding-top: 30px; padding-bottom: 30px;">

<image src="./Courbes/1000_agents_1_contaminé_5_ans/Vaccin04.png"   style="width: 320px; padding-right: 10px" >

<image src = "./Courbes/1000_agents_1_contaminé_5_ans/Vaccin05.png" style = "width: 320px;">

</div>

C'est graphiques représentent l'évolution de l'état de la population en fonction du temps (en jours) pour un nombre de personnes qui se font vacciner chaque jour. <br>
On observe que le fait d'avoir une partie de la population vaccinée est une bonne pratique pour réduire la transmission de la maladie. En effet, le pic de vaccination permet de fortement retardé le pic de contamination initial. De plus, on peut voir que nombre de personnes qui se vaccinent chaque jour est un facteur important pour retarder le début de l'épidémie.

Par la suite, nous avons implémenté les rappels de vaccins. Nous revaccinons les agents dès lors que leur vaccin ne fait plus effet. On regarde donc le seuil minimal de personnes à vacciner par jour pour que la maladie soit éradiquée.

<div style="display: flex; padding-top: 30px; padding-bottom: 30px;">

<image src="./Courbes/1000_agents_1_contaminé_5_ans/Vaccin01_repeat.png"   style="width: 320px; padding-right: 10px" >

<image src = "./Courbes/1000_agents_1_contaminé_5_ans/Vaccin03_repeat.png" style = "width: 320px;">

</div>
<div style="display: flex; padding-top: 30px; padding-bottom: 30px;">

<image src="./Courbes/1000_agents_1_contaminé_5_ans/Vaccin04_repeat.png"   style="width: 320px; padding-right: 10px" >

<image src = "./Courbes/1000_agents_1_contaminé_5_ans/Vaccin05_repeat.png" style = "width: 320px;">

</div>

Ces graphiques montrant l'évolution de l'état de la population en fonction du temps (en jours) pour un nombre de personnes qui se font vacciner chaque jour démontrent bien que se faire vacciner régulièrement permet de très facilement éradiquer la maladie. En effet, on observe que dès trois personnes vaccinées suplémentaires par jour, la maladie ne dépasse pas les 15% d'infectés. Et qu'il suffit de vacciner quatres personnes par jour pour éradiquer la maladie au bout de deux ans.
