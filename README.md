![Biyoinformatik İş Akış Şemam](https://github.com/mnwrdmr/my_bioinformatics_project/assets/93953094/320ffc07-e036-44b4-8b6a-ad482834b31e)

Merhaba, bu depo içerisinde Miuul Biyoinformatik Bootcamp programı için hazırladığım bitirme projemin kodları yer almaktadır. Şimdi gelin size biraz neler yaptığımdan bahsedeyim;

Bitirme projem kapsamında biyoremediasyonda aktif olarak rol oynayan 3 bakteri türünün genom ve proteomlarını incelemek istedim.Seçtiğim bakteri türleri ve yapay zeka kullanarak oluşturduğum bu miniklerin görselleri;

1) Bacillus subtilis: Organik maddelerin parçalanması ve sindirilmesinde önemli rol oynar.  
2) Deinococcus radiodurans: Aşırı radyasyona dayanabilme özelliği sayesinde radyasyon temizliğinde uzmanlaşmıştır.
3) Rhodococcus erythropolis: Özellikle petrol hidrokarbonlarının parçalanması ve metabolizasyonunda uzmanlaşmıştır.

<img width="455" alt="Screenshot 2024-02-26 at 14 14 14" src="https://github.com/mnwrdmr/my_bioinformatics_project/assets/93953094/aa94e431-f039-46d6-abf5-1b812f323768">




Bu depo içerisinde;
1) Veri yönetimi ve kullanılan yazılımların iş akışı için; Snakemake boru hatlarına (Snakefile dosyasından) ve bağlı olduğu env/env.yaml klasöründen ulaşabilirsiniz.
2) 'data' klasörü; 3 bakteri türü için, genom ve proteom projesinde kullanılacak olan protein_aa.fasta ve nükleotid.fasta verilerini içermektedir.
3) 'output' klasörü içerisinde 3 bakteri türü için;
   a) 'barrnap' klasörü içerisinde barrnap yazılımının rRNA sayımı çıktıları,
   b) 'Orthofinder' klasörü içerisinde orthofinder yazılımının çıktıları,
   c) 'directory_with_processed_fasta_and_blast_results' klasörü içerisinde orthofinder yazılımına ait Orthologues istatistikleri; one-to-one, one-to-many, many-to-one ve many-to-many.tsv gibi bir çok istatistiksel sonucu içeren bilgilere,
   d) 'RepeatModeler_output' klasörü içeriside RepeatModeler yazılımının çıktılarına,
   e) 'RepeatMasker_output' klasörü içeriside RepeatMasker yazılımının çıktılarına,
   f) 'plot' klasörü içerisinde yazılımlarının sonnuçları dahilinde görselleştirilen plotlara ulaşabilirsiniz.




Genom Projesi Ödevi İçin; 

1) Öncelikle 'barrnap' yazılımı kullanılarak bakteri türlerinin rRNA sayımını gerçekleştirildi ve daha sonra sonuçlar görselleştirilerek 'Scatter Plot' oluşturuldu (https://github.com/mnwrdmr/my_bioinformatics_project/blob/main/scripts/2_DataAnalysis/barrnap_analysis.py).
2) Tekrarlı bölgeler için RepeatModeler ve RepeatMasker yazılımları kullanıldı ve sonuçlar ile 'PieChart' oluşturuldu.
3) Planlanan StainedGlass yazılımı için bütün gereklilikler yerine getirildi fakat çeşitli python uyuşmazlıkları ve hatalarından dolayı çıktı alınamadı.

<img width="942" alt="Screenshot 2024-02-27 at 02 09 45" src="https://github.com/mnwrdmr/my_bioinformatics_project/assets/93953094/415d50f0-1c8b-42ea-bdc3-e26fe7584a5b">




Proteom Projesi Ödevi İçin; 

1) Ortak gen kümeleri incelenmek istenildiği için 'Orthofinder' yazılımı kullanılarak çıktıları alındı.
2) Orthofinder yazılımı sonucunda çıkan istatistiksel çıktılar ile;
   a) Her bakteri türü için Species-Specific ve Conversed çıktıları doğrultusunda 'BarPlot'  oluşturuldu(https://github.com/mnwrdmr/my_bioinformatics_project/blob/main/scripts/2_DataAnalysis/Orthogroups_analysis_plots.py).
   b) Bacillus subtilis ile diğer 2 bakteri türünün Pairwise Orthologue Comparisons çıktıları; one-to-one, one-to-many, many-to-one ve many-to-many karşılaştırılarak 'Stacked Bar Plot' oluşturuldu.

<img width="908" alt="Screenshot 2024-02-26 at 15 58 43" src="https://github.com/mnwrdmr/my_bioinformatics_project/assets/93953094/d415e36e-e6dd-4da1-aca2-9f9a6202d7b8">

