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

## 22/09/2025

**Chloe** : Installation de 'unzip' dans l'environnement virtuel.
`conda install -c conda-forge unzip`

**Ikram** : Dézippage (placés dans genome) + creation de nouveaux environnements conda pour chacun des outils (contrôle qualité de l’ensemble des génomes):
* Ajout de channel bioconda, conda forage.
* Création de l’environnement Conda avec bonne version Python 
* Installation de BUSCO dans l'environnement busco_env
`conda create -n busco_env python -y`
-> conda install bioconda::busco
* Installation de OMARK dans environnement omark_env:
`conda create -n omark_env python -y` 
-> conda install bioconda::omark
* Installation de QUAST dans l'environnement quast_env 
`conda create -n quast_env python`
-> conda install bioconda::quast
* Installation de KRAKEN (v2.1.6) (identifier la taxonomie et détecter les contaminations) dans l'environnement kraken_env
`onda create -n kraken_env python -y`
-> conda install bioconda::kraken

## 04/10/2025

**Chloe** : Clonage du repositoire projet1 de git et test de add, commit et push.


## 09/10

**Rose** : 
Telechargement de la base de donnée pour kraken : Standard 16
`wget https://genome-idx.s3.amazonaws.com/kraken/k2_standard_16_GB_20250714.tar.gz`
Decompression de la database 
`tar -xvzf ./k2_standard_16_GB_20250714.tar.gz` 

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
Pour nephilia philipes:
`kraken2 --db ./databases/kraken_db_8/ --output ./kraken_outputs/nephilia_out.txt --report ./kraken_outputs/nephilia.kreport ./data/genome/nephila_pilipes/ncbi_dataset/data/GCA_019974015.1/GCA_019974015.1_Npil_1.0_genomic.fna `
Pour oedothorax giggosus:
`kraken2 --db ./databases/kraken_db_8/ --output ./kraken_outputs/oedothorax.txt --report ./kraken_outputs/oedothorax.kreport /data/projet1/data/genome/oedothorax_gibbosus/ncbi_dataset/data/GCA_019343175.1/GCA_019343175.1_Ogib_1.0_genomic.fna`
Pour oppiela nova : 
`kraken2 --db ./databases/kraken_db_8/ --output ./kraken_outputs/oppiela.txt --report ./kraken_outputs/oppiela.kreport /data/projet1/data/genome/oppiella_nova/ncbi_dataset/data/GCA_905397405.1/GCA_905397405.1_1_On_b1v03.max_arth_b2g_droso_b2g_emblv2_genomic.fna`
Pour trichonephila clavata : 
`kraken2 --db ./databases/kraken_db_8/ --output ./kraken_outputs/trichonephila.txt --report ./kraken_outputs/trichonephila.kreport /data/projet1/data/genome/trichonephila_clavata/ncbi_dataset/data/GCA_019973975.1/GCA_019973975.1_Tnct_1.0_genomic.fna `
Pour tropilaelaps mercedesae :
`kraken2 --db ./databases/kraken_db_8/ --output ./kraken_outputs/tropilaelaps.txt --report ./kraken_outputs/tropilaelaps.kreport /data/projet1/data/genome/tropilaelaps_mercedesae/ncbi_dataset/data/GCA_002081605.1/GCA_002081605.1_T._mercedesae_v01_genomic.fna `

Installation de Bracken (v3.1) dans l'environnement kraken_env : 
`conda install bioconda::bracken`
Analayse de l'abondance de chaque espèce à partir des resultsts de kraken : 
`bracken -d ./databases/kraken_db_8/ -i ./kraken_outputs/nephilia.kreport -o ./kraken_outputs/nephilia.bracken`





