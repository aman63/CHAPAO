import bz2
import lzma
import time
import sys
import os
'''
def recursive_path(mypath): 
    for f in listdir(mypath):
        if isfile(join(mypath, f)):
            #print(mypath,' ', f)
            if(f.find("part")==-1 or f.find("mastcom")==-1):
                onlyfiles.append(join(mypath,f))
        else:
            recursive_path(join(mypath,f))
'''
def recursive_path(mypath): 
    for f in listdir(mypath):
        if isfile(join(mypath, f)):
            #print(mypath,' ', f)
            if(f.find("ref.txt")!=-1):
                #print(f)
                onlyfiles.append(mypath)
        else:
            recursive_path(join(mypath,f))


    
if __name__ == "__main__":
    mypath = sys.argv[1]
    fasta=sys.argv[2]
    from os import listdir
    from os.path import isfile, join
    #onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    onlyfiles = []
    recursive_path(mypath)
    outputfile3=open('timedecompress'+str(mypath)+'.txt','w')
    #print(onlyfiles)
    #onlyfiles = onlyfiles[:10]
    array=[]
    decompressiontimes=[]
    
    for f in onlyfiles:
        #if 'mst' not in f and '.part' not in f:
        if '.part' not in f :
            start=time.time()
            os.system('python CHAPAOD64.py '+f+' '+str(fasta))
            #os.system('python CHAPAOD64.py '+f+'.mstcom'+' f')
            end=time.time()
            outputfile3.write(f+' '+str(end-start)+'\n')
            decompressiontimes.append(float(end-start))
    print('avg time' +str(sum(decompressiontimes)/len(decompressiontimes)))
	
