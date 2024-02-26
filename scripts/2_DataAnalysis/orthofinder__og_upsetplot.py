#OG_UPSETPLOT
import pandas as pd
from matplotlib import pyplot as plt
from upsetplot import UpSet
import seaborn as sns

path_OG_count = "/Users/macvbookpro/PycharmProjects/my_bioinformatics_project/output/orthofinder/OrthoFinder/Results_Feb16/Orthogroups/Orthogroups.GeneCount.tsv"
path_singletons = "/Users/macvbookpro/PycharmProjects/my_bioinformatics_project/output/orthofinder/OrthoFinder/Results_Feb16/Orthogroups/Orthogroups_UnassignedGenes.tsv"
out_0 = '/Users/macvbookpro/PycharmProjects/miuul/output/plot/OG_analysis_upsetplot.png'

#"OG with at least two genes"
df_count = pd.read_csv(path_OG_count, sep="\t", header='infer')
df_count = df_count.set_index("Orthogroup").sort_values(by="Total", ascending=False)
df_count.loc[df_count["Total"] > 1, "Type"] = "OG"

#"Single genes which are excluded from the OG"
df_sing = pd.read_csv(path_singletons, sep="\t", header='infer')
df_sing = df_sing.set_index("Orthogroup").fillna(0)
df_sing["Total"] = 1
df_sing = df_sing.map(lambda x: 1 if isinstance(x, str) == True else x)

#"Concatanate OG and singleton dataframes"
df_count_s = pd.concat([df_count, df_sing], axis=0)
df_count_s.loc[df_count_s["Total"] > 1, "Type"] = "OG"
df_count_s.loc[df_count_s["Total"] == 1, "Type"] = "singleton"

df_count_s = df_count_s.rename(columns={"Bacillus_subtilis_aa": "B.subtilis",
                                        "Deinococcus_radiodurans_aa": "D.radiodurans",
                                        "Rhodococcus_erythropolis_aa": "R.erythropolis"})

#"Upset plot for both OG and singletons marked different colors"
df_stack = df_count_s.set_index(df_count_s["B.subtilis"] >= 1). \
    set_index(df_count_s["D.radiodurans"] >= 1, append=True). \
    set_index(df_count_s["R.erythropolis"] >= 1, append=True)

#""" plot upset0 """
upset0 = UpSet(df_stack.sort_values(by="Total", ascending=True),
               min_subset_size=10,
               intersection_plot_elements=0,
               show_counts=True)

#pal = sns.color_palette("mako", as_cmap=True)
#pal = sns.color_palette("Set2")
#pal = sns.color_palette("Paired")
#pal = sns.cubehelix_palette(start=.5, rot=-.5, as_cmap=True)
#sl = sns.color_palette("dark:salmon_r", as_cmap=True)
#dn = sns.cubehelix_palette(as_cmap=True)
pal = sns.color_palette("Paired", n_colors=2)
upset0.add_stacked_bars(by="Type",
                        colors=pal,
                        title="Count by type",
                        elements=5)

upset0.style_subsets(max_degree=1,
                     facecolor="white",
                     edgecolor="black",
                     label="Species-specific")

sns.set_style("whitegrid", {'axes.grid': False})
upset0.plot()
plt.suptitle("OG Upset plot")
plt.savefig(out_0, format="png", bbox_inches='tight', dpi=1200)
plt.show()