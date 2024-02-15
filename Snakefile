rule all:
    input:
            #expand('output/barrnap/{Genome}_rrna.gff3', Genome=['Bacillus_subtilis', 'Deinococcus_radiodurans', 'Rhodococcus_erythropolis']),
            expand('output/RepeatModeler/{Genome}_output.log', Genome=['Bacillus_subtilis', 'Deinococcus_radiodurans', 'Rhodococcus_erythropolis']),
            #expand('output/RepeatModeler/{Genome}.stk', Genome=['Bacillus_subtilis', 'Deinococcus_radiodurans', 'Rhodococcus_erythropolis']),

##Barrnap predicts the location of ribosomal RNA genes in genomes.
rule barrnap:
    input:
            genome = 'data/Genome/{Genome}.fasta'
    output:
            barrnap = 'output/barrnap/{Genome}_rrna.gff3'
    conda:
        'env/env.yaml'
    shell:
        '''barrnap --kingdom bac --quiet {input} > {output}'''

#barrnap outputları alındıktan sonra db ayrıldı tekrar çalıştırmak istenirse dikkat
#RepeatModeler için makeblastdb (db_fasta:bacillus_subtilis):
rule makeblastdb:
    input:
        'data/{type}/Genome/db/{Genome}.fasta'
    output:
        'output/{type}/RepeatModeler/db/{Genome}.ndb',
        'output/{type}/RepeatModeler/db/{Genome}.nhr',
        'output/{type}/RepeatModeler/db/{Genome}.nin',
        'output/{type}/RepeatModeler/db/{Genome}.not',
        'output/{type}/RepeatModeler/db/{Genome}.nsq',
        'output/{type}/RepeatModeler/db/{Genome}.ntf',
        'output/{type}/RepeatModeler/db/{Genome}.nto'
    params:
        outname='output/{type}/RepeatModeler/db/{Genome}'
    conda:
        '/Users/macvbookpro/opt/anaconda3/envs/blast'
    script:
        'makeblastdb -dbtype nucl -in {input} -out {params.outname}'

rule repeatmodeler:
    input:
        query='data/Genome/{Genome}.fasta',
        db='output/RepeatModeler/db/{Genome}.ndb'
    output:
        log='output/RepeatModeler/{Genome}_output.log'
    params:
        outdir='output/RepeatModeler/db/{Genome}',
        threads=6
    conda:
        'env/env.yaml'
    shell:
        '''RepeatModeler -database {input.db} -engine ncbi -pa {params.threads} -dir {params.outdir} > {output.log}'''

