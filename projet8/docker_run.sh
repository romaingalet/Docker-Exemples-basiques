## Consulter la dernière version de l'image sur nexus.
## Puis lancer :
#docker pull <docker-registry-url>/<nom_image_geopython>

## Récupérer l identifiant de l image (IMAGE ID) grâce à la commande `docker images`
## Ici, mettons que l'id vaut : 526de.
## Lancer la commande docker run:
#docker run -v $(pwd):/data --entrypoint '/bin/bash' 526de -c 'python /data/test.py'

## Quelques explications:
##  > -v $(pwd):/data : récupère le contenu courant et le met dans le répertoire /data du container
##  > --entrypoint '/bin/bash' : pour la souce du shell
##  > -c 'python /data/test.py' : pour exécution du script python.
