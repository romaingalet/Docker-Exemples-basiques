# Quelques exemples de génération d'images Docker

  - [x] projet 1 : Conteneur basique lançant un programme Python affichant 'hello'.
              Image source : `FROM python:3.10.0a2-slim-buster`
  - [x] projet 2 : Un exemple à peine plus évolué 
  - [ ] projet 3 : Lancement du programme Python suivi d'arguments dans le `docker run`.
  - [ ] projet 4 : Construction d'un miniconda à partir d'un slim-buster Python (non achevé)
  - [x] projet 5 : Construction d'une image avec quelques lib. python orientées Gis et Data (scipy, numpy, osmnx, ...)
  - [x] projet 7 : Exécution d'un container basé sur ign/geopython lançant un programme Python simple (affichage d'un hello). Image récupérée via `docker pull` sur le registry IGN.
  - [x] projet 8 : Identique à précédent, mais le script Python teste les `import` en vue de préparer le lancement de bdf-mesh.
  - [x] projet 9 : Un fix pour l'import de fiona : Ajout la ligne `ENV PROJ_LIB = ...` dans le Dockerfile.
  - [x] projet 11 : Un docker run (à affiner) pour l'appli bdf-mesh
