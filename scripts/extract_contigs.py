import pandas as pd
import sys

def write_contig_csv(path_to_txt, path_to_csv):
    with open(path_to_txt) as species_table : 
        contigs = []
        for line in species_table :
            parsed_line = line.strip().split('\t')
            if parsed_line[2] != '0' : 
                contigs.append([parsed_line[1], parsed_line[2]])
        df = pd.DataFrame(contigs)
        df.to_csv(path_to_csv)

if __name__ == '__main__':
    path_to_txt = sys.argv[1]
    path_to_csv = sys.argv[2]
    write_contig_csv(path_to_txt, path_to_csv)