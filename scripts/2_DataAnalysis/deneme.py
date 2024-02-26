import matplotlib.pyplot as plt
import seaborn as sns

# Seaborn'dan "Set2" renk paletini kullan
#sns.cubehelix_palette(start=.5, rot=-.75, as_cmap=True)
#sns.set_palette("rocket")
#sns.set_palette('set2')
#sns.color_palette("light:b", as_cmap=True)
#sns.color_palette("Paired")

#sns.color_palette("ch:start=.2,rot=-.3", as_cmap=True)

# Verilen yüzdelikler
genomes = ['Bacillus_subtilis_aa', 'Deinococcus_radiodurans_aa', 'Rhodococcus_erythropolis_aa']
species_specific_percentages = [13.5, 8.3, 27.7]
genes_in_orthogroups_percentages = [58.4, 59.2, 64.8]

# Conserved yüzdelikleri hesapla
conserved_percentages = [orthogroups - species_specific for orthogroups, species_specific in zip(genes_in_orthogroups_percentages, species_specific_percentages)]

# Bar plot oluşturma
plt.figure(figsize=(10, 6))
bar1 = plt.bar(genomes, species_specific_percentages, label='Species-specific')
bar2 = plt.bar(genomes, conserved_percentages, bottom=species_specific_percentages, label='Conserved')

# Barların üzerine yüzde değerlerini yazma
for bars in [bar1, bar2]:
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval, f"{yval:.2f}%", color='black', ha='center', va='bottom')

# Eksen ve başlık ayarları
plt.xlabel('Genomlar')
plt.ylabel('Yüzde (%)')
plt.title('Species-Specific ve Conserved Ortogrupların Yüzdesi')
sns.color_palette("ch:start=.2,rot=-.3", as_cmap=True)
# Legend
plt.legend()

# Plotu gösterme
plt.show()

###########
#
import matplotlib.pyplot as plt
import numpy as np

# Verilen yüzdelikler
genomes = ['Bacillus_subtilis_aa', 'Deinococcus_radiodurans_aa', 'Rhodococcus_erythropolis_aa']
species_specific_percentages = [13.5, 8.3, 27.7]
genes_in_orthogroups_percentages = [58.4, 59.2, 64.8]

# Conserved yüzdelikleri hesapla
conserved_percentages = [orthogroups - species_specific for orthogroups, species_specific in zip(genes_in_orthogroups_percentages, species_specific_percentages)]

# Renk paleti
colors = ['#1f77b4', '#ff7f0e']

# Bar plot oluşturma
plt.figure(figsize=(10, 6))

bar1 = plt.bar(genomes, species_specific_percentages, color=colors[0], label='Species-specific')
bar2 = plt.bar(genomes, conserved_percentages, bottom=species_specific_percentages, color=colors[1], label='Conserved')

# Barların üzerine yüzde değerlerini yazma
for bars in [bar1, bar2]:
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval, f"{yval:.2f}%", color='black', ha='center', va='bottom')

# Eksen ve başlık ayarları
plt.xlabel('Genomlar', fontsize=12)
plt.ylabel('Yüzde (%)', fontsize=12)
plt.title('Species-Specific ve Conserved Ortogrupların Yüzdesi', fontsize=14)

# Legend
plt.legend()

# Grid ekleme
#plt.grid(axis='y', linestyle='--', alpha=0.7)

# Plotu gösterme
plt.show()

######
import matplotlib.pyplot as plt
import seaborn as sns

# Seaborn'un "deep" renk paletini kullan
#sns.cubehelix_palette(start=.5, rot=-.5, as_cmap=True)
#sns.dark_palette("#69d", reverse=True, as_cmap=True)
sns.color_palette("light:b", as_cmap=True)

# Verilen yüzdelikler
genomes = ['Bacillus_subtilis', 'Deinococcus_radiodurans', 'Rhodococcus_erythropolis']
species_specific_percentages = [13.5, 8.3, 27.7]
genes_in_orthogroups_percentages = [58.4, 59.2, 64.8]

# Conserved yüzdelikleri hesapla
conserved_percentages = [orthogroups - species_specific for orthogroups, species_specific in zip(genes_in_orthogroups_percentages, species_specific_percentages)]

# Bar plot oluşturma
plt.figure(figsize=(10, 6))

bar1 = plt.bar(genomes, species_specific_percentages, label='Species-specific')
bar2 = plt.bar(genomes, conserved_percentages, bottom=species_specific_percentages, label='Conserved')

# Barların üzerine yüzde değerlerini yazma
for bars in [bar1, bar2]:
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval, f"{yval:.2f}%", color='black', ha='center', va='bottom')

# Eksen ve başlık ayarları
plt.xlabel('Genomlar', fontsize=12)
plt.ylabel('Yüzde (%)', fontsize=12)
plt.title('Species-Specific ve Conserved Ortogrupların Yüzdesi', fontsize=14)

# Legend
plt.legend()

# Grid ekleme
#plt.grid(axis='y', linestyle='--', alpha=0.7)

# Plotu gösterme
plt.show()
