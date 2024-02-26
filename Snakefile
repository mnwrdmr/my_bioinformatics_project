rule all:
    input:  #expand('output/orthofinder/'),
            #expand('output/barrnap1/{Genome}_rrna.gff3', Genome=['Bacillus_subtilis', 'Deinococcus_radiodurans', 'Rhodococcus_erythropolis']),
            #expand('output/RepeatModeler_output/{Genome}_output.log', Genome=['Bacillus_subtilis', 'Deinococcus_radiodurans', 'Rhodococcus_erythropolis']),
            #expand('output/RepeatMasker_output/{Genome}.fasta', Genome=['Bacillus_subtilis', 'Deinococcus_radiodurans', 'Rhodococcus_erythropolis']),

##Barrnap predicts the location of ribosomal RNA genes in genomes.
rule barrnap:
    input:
            genome = 'data/Genome/{Genome}.fasta'
    output:
            barrnap = 'output/barrnap1/{Genome}_rrna.gff3'
    conda:
        'env/env.yaml'
    shell:
        '''barrnap --kingdom euk --quiet {input.genome} > {output.barrnap}'''

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
    shell:
        'makeblastdb -dbtype nucl -in {input} -out {params.outname}'

rule repeatmodeler:
    input:
        genome='data/Genome/{Genome}.fasta',
        db='output/RepeatModeler/db/{Genome}_BuildDatabase'
    output:
        log='output/RepeatModeler_output/{Genome}_output.log'
    conda:
        'env/env.yaml'
    shell:
        '''RepeatModeler -database {input.db} -pa 6 -LTRStruct > {output.log}'''

rule repeatmasker:
    input:
        fasta='RepeatModeler_output/{Genome}.consensi.fa.classified'
    output:
        out='data/Genome/{Genome}.fasta',
        dir='output/RepeatMasker_output/{Genome}'
    conda:
        'env/env.yaml'
    shell: '''RepeatMasker -pa 36 -gff -lib {input.fasta} -dir {output.dir} {output.out}'''

rule orthofinder:
    input:
        fasta = 'data/orthofinder/',
    output:
        directory('output/orthofinder/')
    conda:
        'env/env.yaml'
    script:
          'scripts/1_BioinformaticsTools/orthofinder.py'
