# CHAPAO
CHAPAO (Compressing  Alignments  using  Hierarchical  and  Probabilistic  Approach) is a novel reference-based technique for compressing MSA files.  This is to our knowledge the first application of the reference-based technique for compressing MSAs. Unlike conventional reference-based methods where an “extra” sequence (not included in the input sequences to compress) is used as the reference, we used a novel hierarchical referencing technique where a suitable subset of the input sequences in the MSA file is used as reference sequences. CHAPAO offers a substantial improvement in compression gain over the existing best alternate methods for both general purpose compression algorithms (zip, Bzip2, gzip, Lzma) and special purpose compression algorithm (CoMSA and MFCompress).

CHAPAO is currently under active development with an aim to develop platform independent user friendly executable and appropriate installer. The current version has been tested more on Linux operating system than on Windows.  

# Dependencies 
Python 3.0 or later 

# Usage 
### Input file format
Input files should be in FASTA or PHYLIP format.

### To compress a single file
For Linux OS:
```bash
python3 compressSingleFile.py PATH_OF_THE_FILE WINDOW_SIZE OVERLAP_AMOUNT
```
For Windows OS:

```bash
CHAPAOC64.exe PATH_OF_THE_FILE WINDOW_SIZE OVERLAP_AMOUNT
```
Example:
```bash
python3 compressSingleFile.py /home/Desktop/DATA/avian/chr1_96_s.fasta 30 28
```
**WINDOW_SIZE** and **OVERLAP_AMOUNT** are two important hyperparameters in our algorithm.  With the increase of **WINDOW_SIZE**, the compression gain generally increases at the cost of more compression time. **OVERLAP_AMOUNT** should be less than **WINDOW_SIZE** and its effect is similar to  **WINDOW_SIZE**.

This will create a folder with extention **.mstcom** which is the output of the compression algorithm. There will be two separate files in the folder, namely metadata.txt and ref.txt.

### Guidelines for hyperparameter selection
For smaller files (<100MB) **WINDOW_SIZE** of 40-50 and **OVERLAP_AMOUNT** of 35-48 will give a high compression ratio within reasonable amounts of time.
For larger files (>100MB) **WINDOW_SIZE** of 5-20 and **OVERLAP_AMOUNT** of 3-18 should be used to compress files within reasonable amounts of time.
### To compress a directory
```bash
python3 compressDirectory.py PATH_OF_THE_DIRECTORY
```
Example:
```bash
python3 compressDirectory.py /home/Desktop/DATA/avian/ 5 3
```

### To decompress:
For Linux OS:
```bash
python3 decompress.py PATH_OF_COMPRESSED_FOLDER OUTPUT_FORMAT(f/p)
```
For windows OS:
```bash
CHAPAOD64.exe PATH_OF_COMPRESSED_FOLDER OUTPUT_FORMAT(f/p)
```

OUTPUT_FORMAT = f to produce decompressed files in **FASTA** format

OUTPUT_FORMAT = p to produce decompressed files in **PHYLIP** format

Example:
```bash
python3 decompress.py /home/Desktop/DATA/avian/chr1_96_s.fasta.mstcom/ f
```
This will create the decompressed files inside the same folder.

## License
[MIT](https://choosealicense.com/licenses/mit/)

## Bug reports: ashiqbuet14@gmail.com
