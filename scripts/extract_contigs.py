import pandas as pd
import sys
import csv
from Bio import SeqIO
import os

def write_contig_csv(path_to_txt, path_to_csv):
    with open(path_to_txt) as species_table : 
        contigs = []
        for line in species_table :
            parsed_line = line.strip().split('\t')
            if parsed_line[2] != '0' : 
                contigs.append([parsed_line[1], int(parsed_line[2])])
        df = pd.DataFrame(contigs)
        df.to_csv(path_to_csv, index=False)

def write_fasta_per_species(path_to_csv, path_to_genome, path_to_output_dir, bracken_file):
    species = os.path.basename(path_to_csv).replace('.csv', '')
    genome_sequences = SeqIO.to_dict(SeqIO.parse(path_to_genome, 'fasta'))
    bracken_df = pd.read_csv(bracken_file, sep='\t')
    #species to keep based on the bracken analysis
    bracken_species= bracken_df[bracken_df['new_est_reads'] >= 10]['taxonomy_id'].tolist()

    with open(path_to_csv) as species_table :
        csv_reader = csv.reader(species_table)
        contig_dict = {}
        for row in csv_reader:
            contig_id = row[0]
            taxid = int(row[1])
            contig_dict.setdefault(taxid, []).append(contig_id)
    
    for conta_species, contig_list  in contig_dict.items():
        if conta_species in bracken_species : 
            species_sequences = []
            for contig_id in contig_list : 
                if contig_id in genome_sequences : 
                    species_sequences.append(genome_sequences[contig_id])         

            fasta_file = f'{path_to_output_dir}/{species}/{conta_species}.fasta'
            SeqIO.write(species_sequences, fasta_file, 'fasta')

    


if __name__ == '__main__':
    path_to_txt = sys.argv[1]   #path to the kraken output for one species
    path_to_csv = sys.argv[2]   #path to the empty csv file where the contig id with be stored 
    path_to_output_dir = sys.argv[3]    #directory containing a sub_directory for each species 
    path_to_genome = sys.argv[4]    #path to the fasta file of the species' genome
    bracken_file = sys.argv[5]
    write_contig_csv(path_to_txt, path_to_csv)
    write_fasta_per_species(path_to_csv, path_to_genome,  path_to_output_dir, bracken_file)