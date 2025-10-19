# Cahier de laboratoire du projet 1

Ce cahier suit le progrès realisé par les membres du groupe.


## 19/09/2025

**Chloe** : Creation du cahier.

**Rose** : Creation de Github repository : https://github.com/RoseCollot/Projet1
**Rose** : Création .girignore

**Ikram** : Recherche bibliographique: fichier Word (ciblée sur la problématique de la contamination génomique):
* Étude l’impact des séquences contaminantes sur la qualité des assemblages génomiques.
* Identification de méthodes et outils de détection et de quantification des contaminations.
* Analyse de certaines stratégies pour isoler ou corriger les séquences.
* Publications et références scientifiques pertinents pour debuter.


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

## 22/09/2025

**Chloe** : Installation de 'unzip' dans l'environnement virtuel.
`conda install -c conda-forge unzip`

**Ikram** 
* Dézippage (placés dans genome) + creation de nouveaux environnements conda pour chacun des outils (contrôle qualité de l’ensemble des génomes):

* Ajout de channel bioconda, conda forage.
`conda config --env --add channels bioconda` 
`conda config --env --add channels conda-forge`
`conda config --env --set channel_priority strict`
Commande utilisé pour chacun des outils.

* Création de l’environnement Conda avec bonne version Python 

* Installation de BUSCO (v6.0) dans l'environnement busco_env
`conda create -n busco_env python -y`
-> `conda install bioconda::busco`

* Installation de OMARK (v0.3.1) dans environnement omark_env:
`conda create -n omark_env python -y` 
-> `conda install bioconda::omark`

* Installation de QUAST (v5.3.0) dans l'environnement quast_env 
`conda create -n quast_env python`
-> `conda install bioconda::quast`

* Installation de KRAKEN (v2.1.6) (identifier la taxonomie et détecter les contaminations) dans l'environnement kraken_env
`onda create -n kraken_env python -y`
-> `conda install bioconda::kraken`

## 04/10/2025

**Chloe** : Clonage du repositoire projet1 de git et test de add, commit et push.


## 09/10

**Rose** : 
Telechargement de la base de donnée pour kraken : Standard 16
`wget https://genome-idx.s3.amazonaws.com/kraken/k2_standard_16_GB_20250714.tar.gz`
Decompression de la database 
`tar -xvzf ./k2_standard_16_GB_20250714.tar.gz` 

**Chloe**
Suppression de repositoire cloné de git.

Création de fichier omark_db dans databases:
`mkdir databases/omark_db/LUCA.h5`

Téléchargement de la base de données LUCA pour OMARK
`wget https://omamer-database-link/LUCA.h5`  *(chemin local : /data/projet1/databases/omark_db/LUCA.h5)*

## 14/10 

**Rose** 
Suppression de la abse de données Standard 16 par manque de mémoire RAM disponible 
Telechargement de la base de donnée Kraken : Standard 8 (8Gb)
`wget https://genome-idx.s3.amazonaws.com/kraken/k2_standard_08_GB_20250714.tar.gz`
Décompression de la database 
`tar -xvzf /data/projet1/databases/kraken_db_8/k2_standard_08_GB_20250714.tar.gz`

## 15/10
**Rose**
Lancement de la classification des reads 
Pour Nephila Pilipes:
`kraken2 --db ./databases/kraken_db_8/ --output ./kraken_outputs/nephila.txt --report ./kraken_outputs/nephila.kreport ./data/genome/nephila_pilipes/ncbi_dataset/data/GCA_019974015.1/GCA_019974015.1_Npil_1.0_genomic.fna `
Pour Oedothorax Giggosus:
`kraken2 --db ./databases/kraken_db_8/ --output ./kraken_outputs/oedothorax.txt --report ./kraken_outputs/oedothorax.kreport /data/projet1/data/genome/oedothorax_gibbosus/ncbi_dataset/data/GCA_019343175.1/GCA_019343175.1_Ogib_1.0_genomic.fna`
Pour Oppiela Nova : 
`kraken2 --db ./databases/kraken_db_8/ --output ./kraken_outputs/oppiela.txt --report ./kraken_outputs/oppiela.kreport /data/projet1/data/genome/oppiella_nova/ncbi_dataset/data/GCA_905397405.1/GCA_905397405.1_1_On_b1v03.max_arth_b2g_droso_b2g_emblv2_genomic.fna`
Pour Trichonephila Clavata : 
`kraken2 --db ./databases/kraken_db_8/ --output ./kraken_outputs/trichonephila.txt --report ./kraken_outputs/trichonephila.kreport /data/projet1/data/genome/trichonephila_clavata/ncbi_dataset/data/GCA_019973975.1/GCA_019973975.1_Tnct_1.0_genomic.fna `
Pour Tropilaelaps Mercedesae :
`kraken2 --db ./databases/kraken_db_8/ --output ./kraken_outputs/tropilaelaps.txt --report ./kraken_outputs/tropilaelaps.kreport /data/projet1/data/genome/tropilaelaps_mercedesae/ncbi_dataset/data/GCA_002081605.1/GCA_002081605.1_T._mercedesae_v01_genomic.fna `

Installation de Bracken (v3.1) dans l'environnement kraken_env : 
`conda install bioconda::bracken`
Analayse de l'abondance de chaque espèce à partir des resultsts de kraken pour Nephila Pilipes: 
`bracken -d ./databases/kraken_db_8/ -i ./kraken_outputs/nephila.kreport -o ./kraken_outputs/nephila.bracken`

**Ikram**
* Diagrammes des contaminants:
Creation de script diagrammes_contaminants.py pour représenter graphiquement et sous forme de tableaux excel les résultats de Bracken pour chacun des 5 génomes:

* Creation d'environnement pour l'analyse des contaminants: contaminants_env
`conda create -n contaminants_env python=3.11`

* Intallation de packages pythons necessaires:
* Installation de pandas:
`conda install -c conda-forge pandas`

* Installation de matplotlib:
`conda install -c conda-forge matplotlib`

* Installation de seaborn:
`conda install -c conda-forge seaborn`


**Chloe**

Création de fichier pour les sequences proteiques des genomes:
`mkdir data/genome_protein`

Creation de fichiers pour chaque espèce dans results:
`mkdir data/genome_protein/<nom_espèce>`

Téléchargement des genomes avec sequences protéiques fasta (.faa) de ncbi dans le fichier de l'espèce:

Trichonephila_clavata:
`datasets download genome accession GCA_019973975.1 --include protein`

Tropilaelaps mercedesae:
`datasets download genome accession GCA_002081605.1 --include protein`

Oppiella nova:
`datasets download genome accession GCA_905397405.1 --include protein`

Nephila pilipes:
`datasets download genome accession GCA_019974015.1 --include protein`

Oedothorax gibbosus:
`datasets download genome accession GCA_019343175.1 --include protein`

Dezippage des fichiers avec `unzip`


## 16/10

**Rose**
Bibliographie : https://pmc.ncbi.nlm.nih.gov/articles/PMC9997750/

Analayse de l'abondance de chaque espèce à partir des resultsts de kraken : 
Oedothorax Gibbosus: 
`bracken -d ./databases/kraken_db_8/ -i ./kraken_outputs/oedothorax.kreport -o ./kraken_outputs/oedothorax.bracken`
Pour Oppiela Nova : 
`bracken -d ./databases/kraken_db_8/ -i ./kraken_outputs/oppiela.kreport -o ./kraken_outputs/oppiela.bracken`
Pour Trichonephila Clavata : 
`bracken -d ./databases/kraken_db_8/ -i ./kraken_outputs/trichonephila.kreport -o ./kraken_outputs/trichonephila.bracken`
Pour Tropilaelaps Mercedesae :
`bracken -d ./databases/kraken_db_8/ -i ./kraken_outputs/tropilaelaps.kreport -o ./kraken_outputs/tropilaelaps.bracken`

**Chloe**
Creation de fichier omark dans results:
`mkdir results/omark`

Creation de fichiers pour chaque espèce dans results:
`mkdir results/omark/<nom_espèce>`

Utilisation de OMAmer pour créer des fichiers .omamer pour utiliser Omark.

Tentatives OMAmer multi-thread échouée – manque de RAM
Pour Tropilaelaps mercedesae:
`omamer search --db /data/projet1/databases/omark_db/LUCA.h5 --query /data/projet1/data/genome_protein/Tropilaelaps_mercedesae/ncbi_dataset/data/GCA_002081605.1/protein.faa --out /data/projet1/results/Tropilaelaps_mercedesae.omamer --nthreads 1`
Pour Oppiella nova:
`omamer search --db /data/projet1/databases/omark_db/LUCA.h5 --query /data/projet1/data/genome_protein/Oppiella_nova/ncbi_dataset/data/GCA_905397405.1/protein.faa --out /data/projet1/results/Oppiella_nova.omamer --nthreads 1`
Pour Trichonephila clavata:
`omamer search --db /data/projet1/databases/omark_db/LUCA.h5 --query /data/projet1/data/genome_protein/Trichonephila_clavata/ncbi_dataset/data/GCA_019973975.1/protein.faa --out /data/projet1/results/Trichonephila_clavata.omamer --nthreads 1`
Pour Oedothorax gibbosus:
`omamer search --db /data/projet1/databases/omark_db/LUCA.h5 --query /data/projet1/data/genome_protein/Oedothorax_gibbosus/ncbi_dataset/data/GCA_019343175.1/protein.faa --out /data/projet1/results/Oedothorax_gibbosus.omamer --threads 1`
* `--nthreads 1` pas assez de RAM pour plus de threads

***

Utilisation de Omark:
input: fichier.omamer crée avec Omamer
Pour Tropilaelaps mercedesae:
`omark --file /data/projet1/results/omark/Tropilaelaps_mercedesae/Tropilaelaps_mercedesae.omamer --database /data/projet1/databases/omark_db/LUCA.h5 --outputFolder /data/projet1/results/omark/Tropilaelaps_mercedesae` 
Pour Oppiella nova:
`omark --file /data/projet1/results/omark/Oppiella_nova/Oppiella_nova.omamer --database /data/projet1/databases/omark_db/LUCA.h5 --outputFolder /data/projet1/results/omark/Oppiella_nova`
Pour Trichonephila clavata:
`omark --file /data/projet1/results/omark/Trichonephila_clavata/Trichonephila_clavata.omamer --database /data/projet1/databases/omark_db/LUCA.h5 --outputFolder /data/projet1/results/omark/Trichonephila_clavata`


**Ikram**
* Representation graphique et sous forme de tableaux excel des résultats de l'outil Omark pour chacun des 5 génomes, placés dans Resultats.

* Utilisation de l'outil Centrifuge pour l'analyse taxonomique des contaminants:
* Création de l’environnement Conda et intallation de l'outil:
`conda create -n centrifuge_env python=3.11 -y`
`conda install bioconda::centrifuge`
`conda install -c bioconda blast`

Telechargement database:
`wget https://genome-idx.s3.amazonaws.com/centrifuge/k2_standard_08_GB_20250714.tar.gz`

Nephila_pilipes:
``centrifuge -x /data/projet1/databases/centrifuge_db/library/k2_standard \ -U /data/projet1/data/genome/nephila_pilipes/ncbi_dataset/data/GCA_019974015.1/GCA_019974015.1_Npil_1 0_genomic.fna \ -S /data/projet1/results/centrifuge/nephila_pilipes.out \ --report-file /data/projet1/results/centrifuge/nephila_pilipes.report`

Oedothorax_gibbosus:
`centrifuge -x /data/projet1/databases/centrifuge_db/library/k2_standard -U /data/projet1/data/genome/oedothorax_gibbosus/ncbi_dataset/data/GCA_019343175.1/GCA_019343175.1_OGibb_1.0_genomic.fna -S /data/projet1/results/centrifuge/oedothorax_gibbosus.out --report-file /data/projet1/results/centrifuge/oedothorax_gibbosus.report`

Oppiella_nova:
`centrifuge -x /data/projet1/databases/centrifuge_db/library/k2_standard -U /data/projet1/data/genome/oppiella_nova/ncbi_dataset/data/GCA_905397405.1/GCA_905397405.1_ONova_1.0_genomic.fna -S /data/projet1/results/centrifuge/oppiella_nova.out --report-file /data/projet1/results/centrifuge/oppiella_nova.report`

Trichonephila_clavata:
`centrifuge -x /data/projet1/databases/centrifuge_db/library/k2_standard -U /data/projet1/data/genome/trichonephila_clavata/ncbi_dataset/data/GCA_019973975.1/GCA_019973975.1_Tclav_1.0_genomic.fna -S /data/projet1/results/centrifuge/trichonephila_clavata.out --report-file /data/projet1/results/centrifuge/trichonephila_clavata.report`

Tropilaelaps_mercedesae:
`centrifuge -x /data/projet1/databases/centrifuge_db/library/k2_standard -U /data/projet1/data/genome/tropilaelaps_mercedesae/ncbi_dataset/data/GCA_002081605.1/GCA_002081605.1_TMercedes_1.0_genomic.fna -S /data/projet1/results/centrifuge/tropilaelaps_mercedesae.out --report-file /data/projet1/results/centrifuge/tropilaelaps_mercedesae.report`


##17/10/2025 - 19/10/2025

**Chloe**

Plusieurs tentatives OMAmer pour Nephila pilipes échouées
