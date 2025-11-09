# Projet 1 (PTU) 
## Détection, caractérisation et assemblage de génomes contaminants dans des données génomiques d’arachnides

<img src="https://srs.britishspiders.org.uk/cache/fe4dc530.jpg" width="130" height="130">
<img src="https://indiabiodiversity.org/files-api/api/get/crop/observations//7e82c75b-3d21-4f42-869f-925118e84594/1a9764ac700e4a96865df3ed0544479e.jpg?h=500" width="130" height="130">
<img src="https://singapore.biodiversity.online/taxo4254/mainSpace/files/Np.%20pilipes%20%28female%29.jpg" width="130" height="130">
<img src="https://beeaware.org.au/wp-content/uploads/2014/04/Tropilaelaps-7.jpg" width="130" height="130">
<img src="https://happymag.tv/wp-content/uploads/2021/09/Oppiella-nova-beetle-mite-1.jpg" width="130" height="130">

Images: Tylan Berry (https://srs.britishspiders.org.uk)
Devin (https://indiabiodiversity.org)
Starmer, F. (https://singapore.biodiversity.online)
Ken Walker Museum Victoria, PADIL (https://beeaware.org.au/archive-pest/tropilaelaps-2)
Nature World News (https://www.natureworldnews.com)


### Description

Ce projet vise à détecter, quantifier et confirmer la présence de séquences de contamination dans cinq génomes d’araignées disponibles sur NCBI.  
Plusieurs approches complémentaires ont été utilisées, incluant la classification taxonomique (Kraken2/Bracken, Centrifuge), la détection basée sur l’orthologie protéique (OMAmer/OMArk) ainsi que une validation par BLAST et mapping des lectures sur les génomes de contaminants identifiés.

### Jeu de données

5 génomes d'arachnides (séquences génomiques et protéiques) :
* Nephila pilipes
* Oppiella nova
* Trichonephila clavata
* Oedothorax gibbosus
* Tropilaelaps mercedesae
Disponibles sur le site du NCBI

Bases de données utilisées :
- Kraken2 Standard 8 GB
- OMArk LUCA
- Base NCBI nt/nr (pour BLAST)

Lectures SRA associées aux génomes pour le mapping final.

### Outils et logiciels

Nous avons créé plusiers environnements virtuels avec conda pour installer les outils et logiciels nécessaires. Ces environnements se trouvent dans le dossier 'conda'.

Dans l'environnement 'projet_env' :
- ncbi-datasets-cli version 18.7.0
- sra-tools version 3.2.1
- unzip version 6.0
- python version 3.13.9

Dans l'environnement 'kraken_env' :
- kraken2 version 2.1.6 
- bracken version 3.1 
- blast version 2.17.0
- python version 3.13.7

Kraken2 : https://github.com/DerrickWood/kraken2

Dans l'environnement 'omark_env' :
- omamer version 2.1.0 
- omark version 0.3.1 
- python version 3.10.19

OMArk : https://github.com/DessimozLab/OMArk

Dans l'environnement 'mapping_env' :
- minimap2 version 2.30
- miniprot version 0.18
- muscle version 3.8.1551
- samtools version 1.22.1
- python version 3.11.14

Dans l'environnement 'contaminants_env' :
- seaborn version 0.13.2
- python version 3.11.14

Dans l'ensemble du projet :
- pandas version 2.3.3
- matplotlib version 3.10.6
- seaborn version
- ncbi-vdb version 3.2.1

- BLASTn NCBI (en ligne) lien du site: https://blast.ncbi.nlm.nih.gov/Blast.cgi?PROGRAM=blastn&PAGE_TYPE=BlastSearch&LINK_LOC=blasthome


### Méthodes 

1. Téléchargement des génomes NCBI (.fna + .faa)
2. Classification taxonomique des séquences (Kraken2 et Bracken)
3. Détection de protéines contaminantes (OMArk)
4. BLAST de contigs pour confirmer les résultats
5. Téléchargement des génomes des espèces contaminantes 
6. Mapping des reads contaminants

Détails des commandes dans ***cahier_labo.md***
Scripts utilisés dans le dossier ***scripts***

### Résumé des principaux résultats

- Le genome de *Tropilaelaps mercedesae* ne possède pas de contaminants.
- Les autres genomes possèdent un niveau de contamination variable.
- Des séquences provenant de *Wolbachia* et *Candidatus Rhabdochlamydia* ont été identifiées dans *Oedothorax gibbosus*.
- 

### Status du projet

<u>Terminé pour les 5 genomes :</u>

* Analyse Kraken2, Braken, OMAmer/OMArk
* Extraction des contigs contaminants
* Sélection des espèces contaminantes les plus probables

<u>Terminé pour *Oedothorax gibbosus* :</u>

* BLAST des contigs contaminants
* Sélection des espèces contaminantes pour utiliser comme référence dans le mapping
* Mapping des reads sur les génomes de contaminants
* Assemblage 

<u> À poursuivre :</u>

* Mapping et assemblage des genomes contaminants dans les 3 espèces d'arachnide restants avec contaminants dans leur genome

En raison de contraintes de temps et de ressources informatiques certaines analyses (Centrifuge, OMArk sur Nephila pilipes…) n’ont pas pu être finalisées. Nous aurions souhaité comparer davantage d’outils.

### Auteurs

**Rose Collot**
**Ikram Hejjaj**
**Chloë Bateman**

Master 2 Bioinformatique et Bioimagerie Structurale

Université de Strasbourg

Cours: Projet Tutoré en BBS

Tuteur: Yannis Nevers

### Remerciements

Nous tenons à remercier notre tuteur Yannis Nevers pour son accompagnement, sa disponibilité et ses idées qui ont permis de réaliser ce projet. 

Nous tenons également à remercier l'université de Strasbourg de nous avoir donné accès au serveur sur lesquel nous avons travaillé.