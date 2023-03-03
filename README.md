# Quelques exemples de génération d'images Docker

  - [x] projet 1 : Conteneur le plus basique. Image source : `FROM python:3.10.0a2-slim-buster`
  - [x] projet 2 : Un exemple à peine plus évolué.
  - [ ] projet 3 : On complexifie à peine : Gestion des args du programme via la commande `docker run`.
  - [ ] projet 4 : Construction d'un env. miniconda à partir d'un slim-buster Python.
  - [x] projet 5 : Image utilitaire avec quelques lib. python orientées Sig et Data (scipy, numpy, osmnx, ...)
  - [x] projet 7 : Exécution d'un container basé sur igո/geopythoո lançant un programme Python simple. Test de `docker pull` sur le registry IGո.
  - [x] projet 8 : Identique à précédent, mais le script Python teste les `import` en vue de préparer le lancement de bdf-mesh.
  - [x] projet 9 : Un fix pour l'import de fiona : Ajout de la ligne `ENV PROJ_LIB = ...` dans le Dockerfile.
  - [x] projet 11 : Un docker run (à affiner) pour l'appli bdf-mesh
  - [x] projet 14 : Dockerfile générant l'envioronnement conda à partir d'un Yaml. Activation de l'env pour exécution du script. 
