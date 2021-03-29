set +o posix
mkdir results_$1
cd results_$1
name_1=len$1.1.fq # first read for reads that can be aligned
name_2=len$1.2.fq # second read for reads that can be aligned
name_3=len$1er.1.fq # first read for reads that cannot be aligned
name_4=len$1er.2.fq # second read for reads that cannot be aligned
another_name=len$1er.fq
# the first arguments passed in is the read lengths
touch time.log
(time wgsim -1 $1 -2 $1 $6 $name_1 $name_2) 2>>time.log
(time wgsim -1 $1 -2 $1 -e 1.0 $6 $name_3 $name_4)  2>>time.log
(time bwa mem -t $2 $3 $name_1 $name_2 >> bwa_mem.$1.sam)  2>>time.log
(time bwa mem -t $2 $3 $name_3 $name_4 >> bwa_mem.$1.er.sam)  2>>time.log
(time bowtie2 -p $2 -X 650 -x $4 -1 $name_1   -2 $name_2  >> bowtie2.$1.sam) 2>>time.log
(time bowtie2 -p $2 -X 650 -x $4  -1 $name_3   -2 $name_4  >> bowtie2.$1.er.sam) 2>>time.log
(time bowtie --sam -p $2 -X 650 $4 -1 $name_1   -2 $name_2 bowtie.$1.sam) 2>>time.log
(time bowtie --sam -p $2 -X 650 $4 -1 $name_3   -2 $name_4 bowtie.$1.er.sam) 2>>time.log
(time subread-align  -t 1 -T $2  -i $5 -r $name_1  -R $name_2  -o subread.$1.sam) 2>>time.log
(time subread-align  -t 1 -T $2  -i $5 -r $name_3  -R $name_4  -o subread.$1.er.sam) 2>>time.log
touch output.log
echo "Reads can be aligned - BWA" >> output.log
samtools flagstat bwa_mem.$1.sam >> output.log
echo "\n\n">>output.log
echo "Reads cannot be aligned - BWA" >>output.log
samtools flagstat bwa_mem.$1.er.sam>>output.log
echo "\n\n">>output.log
echo "Reads can be aligned - Bowtie2">>output.log
samtools flagstat bowtie2.$1.sam>>output.log
echo "\n\n">>output.log
echo "Reads cannot be aligned - Bowtie2">>output.log
samtools flagstat bowtie2.$1.er.sam>>output.log
echo "\n\n">>output.log
echo "Reads can be aligned - Bowtie">>output.log
samtools flagstat bowtie.$1.sam>>output.log
echo "\n\n">>output.log
echo "Reads cannot be aligned - Bowtie">>output.log
samtools flagstat bowtie.$1.er.sam>>output.log
echo "\n\n">>output.log
echo "Reads can be aligned - Subread" >>output.log
samtools flagstat subread.$1.sam >>output.log
echo "\n\n">>output.log
echo "Reads cannot be aligned - Subread" >>output.log
samtools flagstat subread.$1.er.sam >>output.log
echo "\n\n">>output.log
cd ..
python file_handler.py $1 ./results_$1/output.log ./results_$1/time.log
cat report

