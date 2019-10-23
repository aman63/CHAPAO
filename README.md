# CHAPAO
CHAPAO, a novel reference-based technique for compressing MSAfiles.  This is to our knowledge the first application of reference-based technique for compressingMSAs.  Unlike conventional reference-based methods where an “extra” sequence (not includedin the input sequence to compress) is used as a reference, we used a novelhierarchical referencingtechnique where a suitable subset of the input sequences in the MSA file is used as reference sequence. CHAPAO offers substantial improvement in compression gain over the existing best alternate methods for both general perpose comression algorithms ( zip, Bzip2, gzip, Lzma) and special perpose compression algorithm (COmsa and MFComspress).

## Dependencies 
Python 3.0 or later 

## Usage 
CHAPAO is not still available as python package.

To compress single file
```bash
python3 compressSingleFile.py PATH_OF_THE_FILE
```
This will create a folder with extention **.mstcom** which is the output of out programe. There will be two seprate file in the folder metadata.txt and ref.txt.

To compress whole directory
```bash
python3 compressDirectory.py PATH_OF_THE_DIRECTORY
```
Example:
```bash
python3 compressDirectory.py /home/Desktop/DATA/avian/
```

To decompress:

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
