### Simulated Dataset 
20k synthetic proteins, including protein sequences, physical properties, and functional classification for ML targeting. More information on the dataset [here](https://www.kaggle.com/code/devraai/bioinformatics-protein-dataset-analysis/input)\
**Columns:**
- ID_protein: Unique identifier for each protein.
- sequence: String of amino acids.
- molecular_mass: Molecular weight calculated from the sequence.
- isoelectric_point: Estimated isoelectric point based on the sequence composition.
- hydrophobicity: Average hydrophobicity calculated from the sequence.
- total_charge: Sum of the charges of the amino acids in the sequence.
- polar_proportion: Percentage of polar amino acids in the sequence.
- nonpolar_proportion: Percentage of nonpolar amino acids in the sequence.
- sequence_length: Total number of amino acids in the sequence.
- class: The functional class of the protein, one of five categories: Enzyme, Transport, Structural, Receptor, Other.