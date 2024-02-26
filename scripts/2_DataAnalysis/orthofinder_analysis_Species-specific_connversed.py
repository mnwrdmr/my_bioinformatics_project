import matplotlib.pyplot as plt

# Verileri tanımlama
veri = """
Bacillus_subtilis_aa;Deinococcus_radiodurans_aa;Rhodococcus_erythropolis_aa
Number of genes;4237;3091;6130
Number of genes in orthogroups;2476;1830;3973
Number of unassigned genes;1761;1261;2157
Percentage of genes in orthogroups;58.4;59.2;64.8
Percentage of unassigned genes;41.6;40.8;35.2
Number of orthogroups containing species;1612;1457;2031
Percentage of orthogroups containing species;63.7;57.6;80.3
Number of species-specific orthogroups;218;91;509
Number of genes in species-specific orthogroups;571;258;1699
Percentage of genes in species-specific orthogroups;13.5;8.3;27.7
"""

# ';' ile ayrılmış verileri parçalama
satirlar = veri.strip().split("\n")
basliklar = satirlar[0].split(";")
degerler = [satir.split(";") for satir in satirlar[1:]]

# Verileri al
species_specific = [float(s[degerler("Percentage of genes in species-specific orthogroups")]) for s in degerler]
conserved = [100 - s for s in species_specific]  # Species-specific'in dışında kalanlar conserved olacak

# Bar plot oluşturma
plt.figure(figsize=(10, 6))
plt.barh(["Bacillus_subtilis_aa", "Deinococcus_radiodurans_aa", "Rhodococcus_erythropolis_aa"], species_specific, color='blue', label='Species-specific')
plt.barh(["Bacillus_subtilis_aa", "Deinococcus_radiodurans_aa", "Rhodococcus_erythropolis_aa"], conserved, left=species_specific, color='green', label='Conserved')

# Eksen ve başlık ayarları
plt.xlabel('Yüzde (%)')
plt.title('Species-Specific vs. Conserved')

# Legend
plt.legend()

# Plotu gösterme
plt.show()

import matplotlib.pyplot as plt

# Verilen yüzdelikler
genomes = ['Bacillus_subtilis', 'Deinococcus_radiodurans', 'Rhodococcus_erythropolis']
percentages = [13.5, 8.3, 27.7]

# Bar plot oluşturma
plt.figure(figsize=(8, 6))
plt.bar(genomes, percentages, color='skyblue')

# Eksen ve başlık ayarları
plt.xlabel('Genomlar')
plt.ylabel('Yüzde (%)')
plt.title('Species-Specific Ortogruplarının Yüzdesi')

# Barların üzerine yüzde değerlerini yazma
for i in range(len(genomes)):
    plt.text(i, percentages[i] + 0.5, str(percentages[i]) + '%', ha='center')

# Plotu gösterme
plt.show()

###########
import matplotlib.pyplot as plt

# Verilen yüzdelikler
genomes = ['Bacillus_subtilis_aa', 'Deinococcus_radiodurans_aa', 'Rhodococcus_erythropolis_aa']
species_specific_percentages = [13.5, 8.3, 27.7]
total_percentages = [58.4, 59.2, 64.8]

# Conserved yüzdelikleri hesapla
conserved_percentages = [total - species_specific for total, species_specific in zip(total_percentages, species_specific_percentages)]

# Bar plot oluşturma
plt.figure(figsize=(10, 6))
plt.bar(genomes, species_specific_percentages, color='blue', label='Species-specific')
plt.bar(genomes, conserved_percentages, bottom=species_specific_percentages, color='green', label='Conserved')

# Eksen ve başlık ayarları
plt.xlabel('Genomlar')
plt.ylabel('Yüzde (%)')
plt.title('Species-Specific ve Conserved Ortogrupların Yüzdesi')

# Barların üzerine yüzde değerlerini yazma
for i in range(len(genomes)):
    plt.text(i, species_specific_percentages[i] + conserved_percentages[i] + 0.5, str(total_percentages[i]) + '%', ha='center')

# Legend
plt.legend()

# Plotu gösterme
plt.show()

##########
import matplotlib.pyplot as plt

# Verilen yüzdelikler
genomes = ['Bacillus_subtilis_aa', 'Deinococcus_radiodurans_aa', 'Rhodococcus_erythropolis_aa']
species_specific_percentages = [13.5, 8.3, 27.7]
total_percentages = [58.4, 59.2, 64.8]

# Conserved yüzdelikleri hesapla
conserved_percentages = [total - species_specific for total, species_specific in zip(total_percentages, species_specific_percentages)]

# Bar plot oluşturma
plt.figure(figsize=(10, 6))
plt.bar(genomes, species_specific_percentages, color='skyblue', label='Species-specific')
plt.bar(genomes, conserved_percentages, bottom=species_specific_percentages, color='navy', label='Conserved')

# Eksen ve başlık ayarları
plt.xlabel('Genomlar')
plt.ylabel('Yüzde (%)')
plt.title('Species-Specific ve Conserved Ortogrupların Yüzdesi')

# Barların üzerine yüzde değerlerini yazma
for i in range(len(genomes)):
    plt.text(i, species_specific_percentages[i] + conserved_percentages[i] + 0.5, str(total_percentages[i]) + '%', ha='center')

# Legend
plt.legend()

# Plotu gösterme
plt.show()

#########
import matplotlib.pyplot as plt

# Verilen yüzdelikler
genomes = ['Bacillus_subtilis', 'Deinococcus_radiodurans', 'Rhodococcus_erythropolis']
species_specific_percentages = [13.5, 8.3, 27.7]
genes_in_orthogroups_percentages = [58.4, 59.2, 64.8]

# Conserved yüzdelikleri hesapla
conserved_percentages = [orthogroups - species_specific for orthogroups, species_specific in zip(genes_in_orthogroups_percentages, species_specific_percentages)]

# Bar plot oluşturma
plt.figure(figsize=(10, 6))
bar1 = plt.bar(genomes, species_specific_percentages, color='skyblue', label='Species-specific')
bar2 = plt.bar(genomes, conserved_percentages, bottom=species_specific_percentages, color='navy', label='Conserved')

# Barların üzerine yüzde değerlerini yazma
for bars in [bar1, bar2]:
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval, f"{yval:.2f}%", color='white', ha='center', va='bottom')

# Eksen ve başlık ayarları
plt.xlabel('Genomlar')
plt.ylabel('Yüzde (%)')
plt.title('Species-Specific ve Conserved Ortogrupların Yüzdesi')

# Legend
plt.legend()

# Plotu gösterme
plt.show()

########
#renk paleti değişik denenecek yarın seaborn yüklenmediği için olmadı.

import matplotlib.pyplot as plt
import seaborn as sns

# Seaborn'dan "Set2" renk paletini kullan
#sns.cubehelix_palette(start=.5, rot=-.75, as_cmap=True)
#sns.set_palette("rocket")
#sns.set_palette('set2')
#sns.color_palette("light:b", as_cmap=True)
sns.color_palette("ch:start=.2,rot=-.3", as_cmap=True)

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

# Legend
plt.legend()

# Plotu gösterme
plt.show()
