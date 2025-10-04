# Cahier de laboratoire du projet 1

Ce cahier suit le progrès realisé par les membres du groupe.


## 19/09/2025

**Chloe** : Creation du cahier.

**Rose** : Creation de Github repository : https://github.com/RoseCollot/Projet1
**Rose** : Création .girignore

**Ikram** : Recherche bibliographique: fichier Word (ciblée sur la problématique de la contamination génomique).

**Chloe** : Création d'un environnement conda 
`conda create -n projet_env`
**Chloe** : Installation de NCBI dataset dans l'environnement
`conda install -c conda-forge ncbi_dataset-cli`
**Chloe** : Téléchargement des génomes
`dataset download genome accession <genome_id> --filename <genome_name>`

Téléchargés sur:
* Nephilia pilipes https://www.ncbi.nlm.nih.gov/datasets/genome/GCA_019974015.1/

* Oedothorax gibbosus  https://www.ncbi.nlm.nih.gov/datasets/genome/GCA_019343175.1/ 

* Trichonephila clavata  https://www.ncbi.nlm.nih.gov/datasets/genome/GCA_019973975.1/ 

* Oppiella nova  https://www.ncbi.nlm.nih.gov/datasets/genome/GCA_905397405.1/ 

* Tropilaelaps mercedesae https://www.ncbi.nlm.nih.gov/datasets/genome/GCA_002081605.1/

**Chloe** : Installation de 'unzip' dans l'environnement virtuel.
`conda install -c conda-forge unzip`

**Ikram** : Dézippage (placés dans genome) + contrôle qualité pour l’ensemble des génomes.
- Ajout de channel bioconda 
- Téléchargement d'outils seqkit, QUAST, BUSCO.
- Téléchargement de Kraken2 et OMArk (analyse de contamination). 