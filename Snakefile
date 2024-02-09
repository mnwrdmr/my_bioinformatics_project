rule all:
    input:
            expand('output/barrnap/{Genome}_rrna.gff3', Genome=['Bacillus_subtilis', 'Deinococcus_radiodurans', 'Rhodococcus_erythropolis']),

rule barrnap:
    input:
            genome = 'data/Genome/{Genome}.fasta'
    output:
            barrnap = 'output/barrnap/{Genome}_rrna.gff3'
    conda:
        'env/env.yaml'
    shell:
        '''barrnap --kingdom euk --quiet {input.genome} > {output.barrnap}'''