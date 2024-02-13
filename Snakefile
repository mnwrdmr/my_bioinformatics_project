rule all:
    input:
            #expand('output/barrnap/{Genome}_rrna.gff3', Genome=['Bacillus_subtilis', 'Deinococcus_radiodurans', 'Rhodococcus_erythropolis']),
            #expand('output/RepeatModeler/{Genome}_db')

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
        multiext('output/{type}/RepeatModeler/db/{Genome}_db',
     '.ndb',
                '.nhr',
                '.nin',
                '.not',
                '.nsq',
                '.ntf',
                '.nto')
    params:
        outname='output/{type}/RepeatModeler/db/{Genome}_db'
    conda:
        '/Users/macvbookpro/opt/anaconda3/envs/blast'
    script:
        'makeblastdb -dbtype nucl -in {input} -out {params.outname}'


