import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#sütun başlıkları belirtilir
columns = ["seqid", "source", "type", "start", "end", "score", "strand", "phase", "attributes"]

#columns = ["Genom_Adı", "Kaynak", "Öznitelik", "Başlangıç_Pozisyonu", "Bitiş_Pozisyonu", "E_Değeri", "Yön", "Phred_Skoru", "Öznitelikler"]

# GFF dosyasını DataFrame olarak yükle
barrnap_bacillus = pd.read_csv('/Users/macvbookpro/PycharmProjects/my_bioinformatics_project/output/barrnap/Bacillus_subtilis_rrna.gff3', sep="\t", comment="#", header=None, names=columns)
barrnap_bacillus['score'] = barrnap_bacillus['score'].astype(complex)
#pd.options.display._format = '{:.8f}'.format
# barrnap_bacillusu görüntüle
print(barrnap_bacillus)

import pandas as pd

# Veri çerçevesinin sütunları
columns = ["seqid", "source", "type", "start", "end", "score", "strand", "phase", "attributes"]

# GFF dosyasını DataFrame olarak yükle
barrnap_bacillus = pd.read_csv('/Users/macvbookpro/PycharmProjects/my_bioinformatics_project/output/barrnap/Bacillus_subtilis_rrna.gff3', sep="\t", comment="#", header=None, names=columns)

# attributes sütununu ayrıştırma ve yeni sütunlar oluşturma
attributes_split = barrnap_bacillus["attributes"].str.split(";", expand=True)
attributes_dict = {}
for col in attributes_split.columns:
    key_values = attributes_split[col].str.split("=", expand=True)
    attributes_dict[col] = key_values[1]

# Yeni sütunları DataFrame'e ekleme
barrnap_bacillus = pd.concat([barrnap_bacillus, pd.DataFrame(attributes_dict)], axis=1)
barrnap_bacillus.to_csv("output.csv", index=False)

# İlk 5 satırı görüntüleme
print(barrnap_bacillus.head())
print(barrnap_bacillus)

out = pd.read_csv('/Users/macvbookpro/PycharmProjects/my_bioinformatics_project/output.csv', sep=",", comment="#", header=None, names=columns1)
sns.scatterplot(x='features', y='score', hue='features', data=out, palette='viridis')  #sns.histplot(data=barrnap_bacillus, x='0')
sns.scatterplot(x='features', y='start', hue='features', data=out, palette='viridis')  #bbacillus
sns.histplot(data=out, x='features')  #barrnap_bacillus_rRNA_sayımı_plotu

columns1 = ["seqid", "source", "type", "start", "end", "score", "strand", "phase", "attributes", 'features', 'attributes2', 'attributes3']

#columns = ["Genom_Adı", "Kaynak", "Öznitelik", "Başlangıç_Pozisyonu", "Bitiş_Pozisyonu", "E_Değeri", "Yön", "Phred_Skoru", "Öznitelikler"]

# GFF dosyasını DataFrame olarak yükle
barrnap_deinococcus = pd.read_csv('/Users/macvbookpro/PycharmProjects/my_bioinformatics_project/output/barrnap/Deinococcus_radiodurans_rrna.gff3', sep="\t", comment="#", header=None, names=columns)
barrnap_deinococcus['score'] = barrnap_deinococcus['score'].astype(complex)

barrnap_rhodococcus = pd.read_csv('/Users/macvbookpro/PycharmProjects/my_bioinformatics_project/data/Genome/Rhodococcus_erythropolis.fasta', sep="\t", comment="#", header=None, names=columns)

sns.histplot(data=barrnap_bacillus, x='0')
sns.scatterplot(x='start', y='end', hue='seqid', data=barrnap_bacillus, palette='viridis')
sns.scatterplot(x='start', y='end', hue='seqid', data=barrnap_rhodococcus, palette='husl')
sns.scatterplot(x='start', y='end', hue='seqid', data=barrnap_deinococcus, palette='flare')
sns.scatterplot(x='index', y='bitscore', data=barrnap_bacillus, palette='end')
sns.scatterplot(x='start', y='end', data=barrnap_deinococcus, palette='viridis')
sns.scatterplot(x='start', y='end', data=barrnap_bacillus, palette='viridis')

# Gösterme
plt.show()

#sns.histplot(data=barrnap_bacillus, x='')

#sns.scatterplot(data=blast_G_muris.reset_index(), x='index', y='bitscore', hue='pident')

#sns.scatterplot(data=blast_G_muris.reset_index(), x='index', y='length', hue='pident')

pivot_table = pd.pivot_table(out, values='start', index='end', columns='seqid')
sns.heatmap(pivot_table)

plt.show()

import pandas as pd
import matplotlib.pyplot as plt

# Barrnap çıktısını yükle
barrnap_data = pd.read_csv('/Users/macvbookpro/PycharmProjects/my_bioinformatics_project/output/barrnap/Bacillus_subtilis_rrna.gff3', sep="\t",comment="#", header=None, names=columns)
columns = ["seqid", "source", "type", "start", "end", "score", "strand", "phase", "attributes"]
# rRNA türlerini belirle
barrnap_data['rrna_type'] = barrnap_data['attributes'].str.extract('(18S_rRNA|5S_rRNA|28S_rRNA)')

# Scatter plot oluştur
plt.figure(figsize=(10, 6))
for rrna_type, color in zip(['18S_rRNA', '5S_rRNA','28S_rRNA'], ['blue', 'red', 'orange']):
    rrna_type_data = barrnap_data[barrnap_data['rrna_type'] == rrna_type]
    plt.scatter(rrna_type_data['start'], rrna_type_data['start'], label=rrna_type, color=color)

plt.xlabel('Start Position')
plt.ylabel('End Position')
plt.title('rRNA Type Scatter Plot')
plt.legend()
plt.grid(True)
plt.show()

import pandas as pd
import matplotlib.pyplot as plt

# Barrnap çıktısını yükle
barrnap_data = pd.read_csv('/Users/macvbookpro/PycharmProjects/my_bioinformatics_project/output/barrnap/Bacillus_subtilis_rrna.gff3', sep="\t",comment="#", header=None, names=columns)
columns = ["seqid", "source", "type", "start", "end", "score", "strand", "phase", "attributes"]
# rRNA türlerini belirle
barrnap_data['rrna_type'] = barrnap_data['attributes'].str.extract('(18S_rRNA')

# Scatter plot oluştur
plt.figure(figsize=(10, 6))
for rrna_type, color in zip(['18S_rRNA', '5S_rRNA'], ['blue', 'red']):
    rrna_type_data = barrnap_data[barrnap_data['rrna_type'] == rrna_type]
    plt.scatter(rrna_type_data['start'], rrna_type_data['start'], label=rrna_type, color=color)

plt.xlabel('Start Position')
plt.ylabel('End Position')
plt.title('rRNA Type Scatter Plot')
plt.legend()
plt.grid(True)
plt.show()



import pandas as pd
import matplotlib.pyplot as plt

# Barrnap çıktılarını yükle
columns = ["seqid", "source", "type", "start", "end", "score", "strand", "phase", "attributes"]
barrnap1_data = pd.read_csv('/Users/macvbookpro/PycharmProjects/my_bioinformatics_project/output/barrnap/Bacillus_subtilis_rrna.gff3', sep="\t", comment="#", header=None, names=columns)
barrnap2_data = pd.read_csv('/Users/macvbookpro/PycharmProjects/my_bioinformatics_project/output/barrnap/Deinococcus_radiodurans_rrna.gff3', sep="\t", comment="#", header=None, names=columns)
barrnap3_data = pd.read_csv('/Users/macvbookpro/PycharmProjects/my_bioinformatics_project/output/barrnap/Rhodococcus_erythropolis_rrna.gff3', sep="\t", comment="#", header=None, names=columns)

# rRNA türlerini belirle
barrnap1_data['rrna_type'] = barrnap1_data['attributes'].str.extract('(18S_rRNA|5S_rRNA|28S_rRNA)')
barrnap2_data['rrna_type'] = barrnap2_data['attributes'].str.extract('(18S_rRNA|5S_rRNA|28S_rRNA)')
barrnap3_data['rrna_type'] = barrnap3_data['attributes'].str.extract('(18S_rRNA|5S_rRNA|28S_rRNA)')

# Scatter plotu oluştur
plt.figure(figsize=(10, 6))

# Her bir barrnap çıktısı için scatter plot oluştur
for barrnap_data, label in zip([barrnap1_data, barrnap2_data, barrnap3_data], ['Barrnap 1', 'Barrnap 2', 'Barrnap 3']):
    for rrna_type, color in zip(['18S_rRNA', '5S_rRNA', '28S_rRNA'], ['blue', 'red', 'orange']):
        rrna_type_data = barrnap_data[barrnap_data['rrna_type'] == rrna_type]
        plt.scatter(rrna_type_data['start'], rrna_type_data['end'], label=f"{label} {rrna_type}", color=color)

plt.xlabel('Start Position')
plt.ylabel('End Position')
plt.title('rRNA Type Scatter Plot')
plt.legend()
plt.grid(True)
plt.show()

# Renk paleti
colors = ['blue', 'red', 'orange']

# Her bir barrnap çıktısı için scatter plot oluştur
for barrnap_data, label, color in zip([barrnap1_data, barrnap2_data, barrnap3_data], ['Barrnap 1', 'Barrnap 2', 'Barrnap 3'], colors):
    for rrna_type in ['18S_rRNA', '5S_rRNA', '28S_rRNA']:
        rrna_type_data = barrnap_data[barrnap_data['rrna_type'] == rrna_type]
        plt.scatter(rrna_type_data['start'], rrna_type_data['end'], label=f"{label} {rrna_type}", color=color)

plt.xlabel('Start Position')
plt.ylabel('End Position')
plt.title('rRNA Type Scatter Plot')
plt.legend()
plt.grid(True)
plt.show()



#############
#renkler ile 3 genom için scatterplot
import pandas as pd
import matplotlib.pyplot as plt

# Veri çerçevesinin sütunları
columns = ["seqid", "source", "type", "start", "end", "score", "strand", "phase", "attributes"]

# Bakteri genomlarının barrnap çıktılarını yükle
bacillus_barrnap = pd.read_csv('/Users/macvbookpro/PycharmProjects/repeatmodeler/output/barrnap/Bacillus_subtilis_rrna.gff3', sep="\t", comment="#", header=None, names=columns)
deinococcus_barrnap = pd.read_csv('/Users/macvbookpro/PycharmProjects/repeatmodeler/output/barrnap/Deinococcus_radiodurans_rrna.gff3', sep="\t", comment="#", header=None, names=columns)
rhodococcus_barrnap = pd.read_csv('/Users/macvbookpro/PycharmProjects/repeatmodeler/output/barrnap/Rhodococcus_erythropolis_rrna.gff3', sep="\t", comment="#", header=None, names=columns)

# Scatter plotu oluştur
plt.figure(figsize=(10, 6))

# Her bir bakteri genomu için scatter plot oluştur
plt.scatter(bacillus_barrnap['start'], bacillus_barrnap['end'], color='blue', label='Bacillus subtilis')
plt.scatter(deinococcus_barrnap['start'], deinococcus_barrnap['end'], color='red', label='Deinococcus radiodurans')
plt.scatter(rhodococcus_barrnap['start'], rhodococcus_barrnap['end'], color='green', label='Rhodococcus erythropolis')

plt.xlabel('Start Position')
plt.ylabel('End Position')
plt.title('rRNA Locations of Different Bacteria')
plt.legend(title='Bacteria')  # Bilgi kutucuğuna başlık ekleme
#plt.grid(True)
plt.show()
