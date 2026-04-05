# --- PART 1: GENETIC MAPPING ---
genetic_code = {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M', 'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K', 'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L', 'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A', 'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G', 'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L', 'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_', 
    'TGA':'_', 'GTC':'V', 'GTT':'V', 'GTA':'V', 'GTG':'V', 'TGC':'C', 'TGT':'C', 'TGG':'W',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R', 'CAT':'H', 'CAC':'H', 'CAA':'Q', 'CAG':'Q'
}

# --- PART 2: PROCESSING ENGINE ---

def clean_sequence(raw_data):
    """Filters non-genomic noise and standardizes sequence to uppercase."""
    dna_input = "".join(raw_data.split()).upper()
    return "".join([base for base in dna_input if base in "ATGC"])

def translate_dna(dna_seq):
    """Translates DNA triplets into primary protein amino acid structure."""
    protein = ""
    for i in range(0, (len(dna_seq) // 3) * 3, 3):
        codon = dna_seq[i:i+3]
        protein += genetic_code.get(codon, "?")
    return protein

# --- PART 3: MOLECULAR DIAGNOSTIC ENGINE ---

def run_hbb_diagnostic(protein_seq):
    """Specific biomarker detection for Sickle Cell Anemia (HbS)."""
    if len(protein_seq) >= 6:
        target_aa = protein_seq[5] # Index 5 is Position 6
        print("\n" + "*"*50)
        print(" [MOLECULAR DIAGNOSTIC REPORT: HBB GENE] ")
        print("*"*50)
        
        if target_aa == 'V':
            print("FINAL STATUS: POSITIVE (Pathogenic)")
            print("FINDINGS: HbS mutation (Valine) detected at Position 6.")
        elif target_aa == 'E':
            print("FINAL STATUS: NEGATIVE (Normal)")
            print("FINDINGS: Glutamic Acid (Wild Type) detected at Position 6.")
        else:
            print(f"FINAL STATUS: ATYPICAL VARIANT ('{target_aa}')")
            print("WARNING: Non-standard amino acid detected. Clinical review required.")
        print("*"*50)
    else:
        print("\nCRITICAL ERROR: DNA sequence length is insufficient for HBB analysis.")

# --- PART 4: INTERACTIVE INTERFACE ---

def main_console():
    print("\n" + "="*55)
    print("      GENOMIC ANALYSIS SUITE - V3.1 PROFESSIONAL")
    print("="*55)
    print("1. PROTEIN TRANSLATION (General)")
    print("2. SICKLE CELL ANEMIA DETECTION (HBB Gene)")
    print("3. SEQUENCE METRICS (GC Content & Length)")
    print("4. TERMINATE PROTOCOL")
    
    user_choice = input("\nSelect system option (1-4): ")

    if user_choice == '1':
        # Default Human Insulin Fragment
        insulin_dna = "ATGGCCCTGTGGATGCGCCTCCTGCCCCTGCTGGCCCTGCTGGCCCTCTGGGGACCTGACCCAGCC"
        clean_dna = clean_sequence(insulin_dna)
        print(f"\nPRIMARY STRUCTURE OUTPUT: {translate_dna(clean_dna)}")
        
    elif user_choice == '2':
        print("\n--- INITIATING HBB SCANNER ---")
        print("Input DNA sequence for HBB analysis:")
        # Test positive: ATGGTGCACCTGACTGTG
        dna_input = input("DNA SEQUENCE > ")
        clean_dna = clean_sequence(dna_input)
        prot_output = translate_dna(clean_dna)
        print(f"\nTRANSLATION RESULT: {prot_output}")
        run_hbb_diagnostic(prot_output)
        
    elif user_choice == '3':
        dna_input = input("\nEnter sequence for metric calculation: ")
        clean_dna = clean_sequence(dna_input)
        if clean_dna:
            gc_val = (clean_dna.count("G") + clean_dna.count("C")) / len(clean_dna) * 100
            print(f"\n--- DATA METRICS ---")
            print(f"GC CONTENT: {gc_val:.2f}%")
            print(f"TOTAL BASES: {len(clean_dna)} bp")
        else:
            print("\nERROR: No valid genomic input detected.")

    elif user_choice == '4':
        print("\nSystem offline. Session ended.")
        return

    # Keep the console running
    main_console()

if __name__ == "__main__":
    main_console()
