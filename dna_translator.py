# --- PART 1: UNIVERSAL GENETIC CODE DICTIONARY (64 CODONES) ---
# This dictionary includes all amino acids, including Histidine (H) and Glutamine (Q)
genetic_code = {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M', 'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K', 'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L', 'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A', 'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G', 'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L', 'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_', 
    'TGA':'_', 'GTC':'V', 'GTT':'V', 'GTA':'V', 'GTG':'V', 'TGC':'C', 'TGT':'C', 'TGG':'W',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R', 
    'CAT':'H', 'CAC':'H', 'CAA':'Q', 'CAG':'Q' 
}

# --- PART 2: CORE BIOINFORMATICS FUNCTION ---
def analyze_genomic_sequence(raw_sequence):
    """
    Cleans raw DNA sequences and translates them into protein sequences.
    Filters out non-genomic noise (whitespaces, newlines, and non-ATGC characters).
    """
    # DATA CLEANING: Remove hidden characters and white spaces
    dna_input = "".join(raw_sequence.split()).upper()
    clean_dna = "".join([base for base in dna_input if base in "ATGC"])
    
    if len(clean_dna) == 0:
        print("Error: No valid DNA sequence found.")
        return

    # GC CONTENT CALCULATION
    gc_percentage = (clean_dna.count("G") + clean_dna.count("C")) / len(clean_dna) * 100
    
    # TRANSLATION PROCESS (Reading in 3-base triplets)
    protein_sequence = ""
    for i in range(0, (len(clean_dna) // 3) * 3, 3):
        codon = clean_dna[i:i+3]
        # Fetch amino acid from dictionary, defaults to '?' if codon is unknown
        amino_acid = genetic_code.get(codon, "?")
        protein_sequence += amino_acid
            
    # FINAL LABORATORY REPORT
    print("-" * 50)
    print("      BIOTECHNOLOGY ANALYSIS REPORT")
    print("-" * 50)
    print(f"Sequence Length: {len(clean_dna)} bases")
    print(f"GC Content:      {gc_percentage:.2f}%")
    print(f"Protein Output:  {protein_sequence}")
    print("-" * 50)

# --- PART 3: HUMAN INSULIN GENE SAMPLE ---
insulin_sample = """
ATGGCCCTGTGGATGCGCCTCCTGCCCCTGCTGGCCCTGCTGGCCCTCTGGGGACCTGACCCAGCCGCAGCCTTTGTGAACCA
ACACCTGTGCGGCTCACACCTGGTGGAAGCTCTCTACCTAGTGTGCGGGGAACGAGGCTTCTTCTACACACCCAAGACCCGCC
GGGAGGCAGAGGACCTGCAGGTGGGGCAGGTGGAGCTGGGCGGCGGCCCTGGTGCAGGCAGCCTGCAGCCCTTGGCCCTGGAG
GGGTCCCTGCAGAAGCGTGGCATTGTGGAACAATGCTGTACCAGCATCTGCTCCCTCTACCAGCTGGAGAACTACTGCAACTAG
"""

# Run analysis
analyze_genomic_sequence(insulin_sample)
