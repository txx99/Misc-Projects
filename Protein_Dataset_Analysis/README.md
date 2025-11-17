## Simulated Dataset 
This notebook will analyse a synthetic dataset of 20k proteins and build a Random Forest Classifier. The data includes protein sequences, physical properties, and functional classification of the proteins for ML targeting.  \
This dataset was uploaded by Rafael Gallo; find more information on the dataset [here](https://www.kaggle.com/datasets/gallo33henrique/bioinformatics-protein-dataset-simulated).

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

### Data files
archive.zip = all three data files in zip folder \
proteinas_20000_enriquecido.csv = combined dataset of 20k proteins \
proteinas_train.csv = training split of protein data, 16k x 10 \
proteinas_test.csv = testing split of protein data, 4k x 10 