## Le Résumé Automatique, La Maximisation de Caracarestiques

### L'installation



Pour faire tourner le code, il faut installer Python, numpy et scipy, NLTK :
http://www.scipy.org/install.html


    sudo apt-get install python-numpy python-scipy
    
mais également nltk (présuppose d'avoir installé pip) :

http://www.nltk.org/install.html

    sudo pip install -U nltk


et de plus, il faut installer le pyenchant et editdistance 0.3.1
http://pythonhosted.org/pyenchant/tutorial.html
https://pypi.python.org/pypi/editdistance

    sudo pip install editdistance

    pip install pyenchant

### La structure

*   TextSummarizer: cette classe est dans le fichier summarizer et elle est responsible de provoquer toutes les foctions principales du résumé.
    elle enveloppe les documents de corpus dans une structure bien organisée et composée des classes suivantes:

    *   Paper
    *   Section
    *   Sentence
    *   Word

    - toutes ces classes se trouvent dans le fichier coprpus.py, elles sont toutes composées de quelque attribues avec leur getter et setter et une fonction pour l'initiation.
    -l'iinitiation est la plus importante fonction pour comprendre la façon dans la quelle je crée cette structure.
    -l'initiateur de la classe Word contient la plupart des operations comme le traitement linguistique de NLTK.
    -la classe Word contient deux listes, les indices et les phrases. les deux listes sont associées et alignées. par exemple, le premier index représente la position du mot dans la premiere phrase.

*   la classe MatricesBuilder, située dans le fichier matrices.py est responsable de créer les matrices demandées pour la maximisation de caractaristiques
    bref, elle fait les donées d'éntrée pour la classe :

*   FeatureMaximization: située dans le fichier fm.py est responsable de calculer les matrices de FR, FP, FF. ces matrices sont calculées lors de l'initialisation. les autres matrices sont calculées quand on provoque getRelevantFeatures pour calculer les caracarestiques pertinentes

    - le resultat du prgramme est enregistré dans le console: les mots pertinents, les phrases gagnates avec des méta données: le poids, le nombre de mots gagnats, le nombre de mots ayant un poids non-zero ..

> le fichier test_isko.py ne fonctionne plus, il a besoin d'adaption avec la nouvelle forme de la classe de FM

> vieux commentaire de Nicolas :

*   /exemple_isko contient les fichiers qui représentent l'exemple utilisé dans nos articles pour expliquer la feature f-mesure (homme/femme avec tailles pieds, cheveux, nez)

*   /pyfmax est un package qui contient le module "fmax.py" qui introduit la classe qui nous servira à calculer la feature f-mesure

*   /test_isko.py utilise pyfmax/fmax.py pour charger le contenu de /exemple_isko dans une matrice

*   /pycorpus est un package qui contient le module loader qui permet de charger des fichiers du corpus

*   /test_load_file utilise pycorpus pour charger un fichier





