from snakemake.shell import shell

db = snakemake.input.db
#query = snakemake.params.outname
threads = snakemake.threads
output = snakemake.output[0]

shell(f'''RepeatModeler -database {db} -engine ncbi -pa {threads} > {output}''')


#RepeatModeler -database {database_name} -engine ncbi -pa { number of cores} -LTRStruct > out.log

#RepeatModeler -database /Users/macvbookpro/PycharmProjects/my_bioinformatics_project/data/Genome/Bacillus_subtilis.fasta -pa 6 -LTRStruct > out.log

# eğer çalışma yarıda kalırsa: -recoverDir <Previous Output Directory>

#

