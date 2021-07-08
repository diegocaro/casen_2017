import pandas as pd

# requires pyreadstat package
# conda install -c conda-forge pyreadstat
df = pd.read_spss('Casen 2017.sav')
df = df.astype({'folio':'int','id_vivienda':'int'})
df['folio'] = df['folio'].str[:-2]
df.to_csv('Casen2017.csv.gz', compression='gzip')