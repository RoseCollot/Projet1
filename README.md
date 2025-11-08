# Projet 1 (PTU) 
## Détection, caractérisation et assemblage de génomes contaminants dans des données génomiques d’arachnides

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

- Kraken2 version 2.1.6 
- Bracken version 3.1 
- OMAmer version 2.1.0 
- OMArk version 0.3.1 
- BLASTn NCBI (en ligne) 
- Minimap2 
- Python, Pandas et Matplotlib 
- SRA-Tools
- Conda

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
* Sélection des espèces contaminantes pour utiliser comme référence dnas le mapping
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



