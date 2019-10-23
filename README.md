# CHAPAO
CHAPAO(Compressing  Alighments  using  Hierarchical  and  Probabilistic  Approach) is a novel reference-based technique for compressing MSAfiles.  This is to our knowledge the first application of reference-based technique for compressing MSAs. Unlike conventional reference-based methods where an “extra” sequence (not includedin the input sequence to compress) is used as a reference, we used a novel hierarchical referencing technique where a suitable subset of the input sequences in the MSA file is used as reference sequence. CHAPAO offers substantial improvement in compression gain over the existing best alternate methods for both general perpose comression algorithms ( zip, Bzip2, gzip, Lzma) and special perpose compression algorithm (COmsa and MFComspress).

# Dependencies 
Python 3.0 or later 

# Usage 

### To compress single file
```bash
python3 compressSingleFile.py PATH_OF_THE_FILE WINDOW_SIZE OVERLAP_AMOUNT
```
Example:
```bash
python3 compressSingleFile.py /home/Desktop/DATA/avian/chr1_96_s.fasta 30 28
```
**WINDOW_SIZE** and **OVERLAP_AMOUNT** are two important hyperparameter in our algorithm. With the increase of **WINDOW_SIZE** compression ratio generally increases but algorithm takes more time to compress. **OVERLAP_AMOUNT** should be less than **WINDOW_SIZE**. The effect of **OVERLAP_AMOUNT** is same as **WINDOW_SIZE**, when it is increased compression ratio increases but with more time. These two parameter must be integer.

This will create a folder with extention **.mstcom** which is the output of out programe. There will be two seprate file in the folder metadata.txt and ref.txt.
### Guide line for hyperparameter
For smaller files(<100MB) **WINDOW_SIZE** of 40-50 and **OVERLAP_AMOUNT** of 38-48 will give high compression ratio with reasonable amount of time.
For larger files(>100MB) **WINDOW_SIZE** of 5-20 and **OVERLAP_AMOUNT** of 3-18 should be used to compress files with reasonable amount of time.
### To compress whole directory
```bash
python3 compressDirectory.py PATH_OF_THE_DIRECTORY
```
Example:
```bash
python3 compressDirectory.py /home/Desktop/DATA/avian/ 5 3
```

### To decompress:

```bash
python3 decompress.py PATH_OF_COMPRESSED_FOLDER OUTPUT_FORMAT(f/p)
```
OUTPUT_FORMAT = f to produce decompressed file in **FASTA** format

OUTPUT_FORMAT = p to produce decompressed file in **PHYLIP** format

Example:
```bash
python3 decompress.py /home/Desktop/DATA/avian/chr1_96_s.fasta.mstcom/ f
```
This will create the decompressed file inside the same folder.

## License
[MIT](https://choosealicense.com/licenses/mit/)
