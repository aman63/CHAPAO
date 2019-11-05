# -*- coding: utf-8 -*-
"""
Created on Fri Jul  6 07:06:15 2018

@author: User
"""

import Dmst
import math
import os
import sys
import compression2
import time
BITSINNUM=12
BITSIID = 12
BITPERBASE = 3
PER_CHARACTER_BIT=0#
SKIPLIMIT = 1
PER_CHARACTER_BIT2=0#
MAP_FOR_SYMBOL2={}


def loadData(fileName):
    f = open(fileName, 'r')
    Data = []
    Name = []
    a=0#
    ind=0#
    filetype='p'
    data=f.read().split("\n")
    if(">" in data[0]):
    	filetype='f'
    if(filetype=='f'): 
        f = open(fileName, 'r')
        data=f.read().split(">")  
        for i in data[1:]:
            j=i.split("\n")
            s=[]
            Name.append(j[0])
            for k in j[1:]:
                s.extend(k)
            Data.append(''.join(s).strip().lower())
            ind+=1
   
       
        len_check = [ len(i) for i in Data]
        if min(len_check)!= max(len_check):
            print("FATAL ERROR > LENGTHS NOT EQUAL ")
            raise Exception("FATAL ERROR > LENGTHS NOT EQUAL ")
        f.close()
        return len(Data), Data,Name#
    elif(filetype=='p'):

        lenn=len(data)
        #number = 0
        for i in data[1:]:
            if(i=='\n' or i==''):
                break
            species_name=i.split()[0]
            species_data=i.split()[1]
            Data.append(species_data)
            Name.append(species_name)
            #print("data load",number)
            #number+=1
     
        len_check = [ len(i) for i in Data]
        print(len(len_check))
        if min(len_check)!= max(len_check):
            print("FATAL ERROR > LENGTHS NOT EQUAL ")
            raise Exception("FATAL ERROR > LENGTHS NOT EQUAL ")
        f.close()
        return len(Data), Data,Name#
    raise Exception('please print appropriate file type')

def getProbability(Data, interval):
    length = len(Data[0])
    probabilities = [dict() for i in range(length)]
    num = len(Data)
    actual_lenth = len(Data[0])
    for i in range(actual_lenth):
        for j in range(len(Data)):
            if i+interval<=len(Data[0]):
                c = Data[j][i:i+interval]
            else :
                c = Data[j][i:] 
            if c in probabilities[i]:
                probabilities[i][c]+=1
            else:
                probabilities[i][c]=1
        for c in probabilities[i]:
            probabilities[i][c]=probabilities[i][c]/num
    return probabilities

def getExpectations(Data,probabilities,interval):
    expectation = []
    for i in Data:
        expec = 0
        #print(i)
        for j in range(len(i)) :
            #print(i[j])
            if j+interval<=len(i):
                c=i[j:j+interval]
            else:
                c=i[j:]
            expec += math.log(probabilities[j][c])
        
        expectation.append(expec)
    return expectation


def getExpectations_2(Data,probabilities,interval):
    l=[]
    distance_2=[]
    
    
    for i in probabilities:
        l.append( max(i,key=i.get))
    
    k=0
    for i in Data:
        #dis=0
        dis2=0
        for j in range(len(i)):
            if( l[j]!=i[j]):
                #dis+=1
                dis2+=1-probabilities[j][i[j]]
        #distance.append(dis)
        distance_2.append(dis2)
        k+=1
    orderedpairs_3 = [ (i,j) for  j,i in enumerate(distance_2) ]
    orderedpairs_3.sort()
    order_3 = [ i for j,i in orderedpairs_3]
    return order_3


def getDiff(r, t):
    Map = {}
    dict={}#
    j=-1
    for i in range(len(r)):
        if i<=j:
            continue
        if r[i] != t[i]:
            j = i
            while i < len(r) and (r[i] != t[i] or ((i+1)<len(r) and r[i:i+SKIPLIMIT]!=t[i:i+SKIPLIMIT])) :
                if( r[i]==t[i]):
                    if(t[j:i] in Map.keys()): break
                i += 1
            subs = t[j:i]
            index=j#
            j=i
            if subs in Map.keys():
                Map[subs] += 1
                dict[subs]+=","+str(index)#
            else:
                Map[subs] = 1
                dict[subs]=str(index)#
    cost = 0
    for j in Map.keys():
       # print(j)
        cost += len(j) * BITPERBASE + (Map[j]) * (BITSINNUM)
    return cost,dict#

def getDiff_2(r, t):
    Map = {}
    dict={}#
    j=-1 
    for i in range(len(r)):
        if i<=j:
            continue
        if r[i] != t[i]:
            j = i
            while i < len(r) and r[i] != t[i]:
                i += 1
            subs = t[j:i]
            index=j#
            j=i
            if subs in Map.keys():
                Map[subs] += 1
                dict[subs]+=","+str(index)#
            else:
                Map[subs] = 1
                dict[subs]=str(index)#
    cost = 0
    for j in Map.keys():
       # print(j)
        cost += len(j) * BITPERBASE + (Map[j]) * (BITSINNUM)
    return cost,dict#

def getReduceVal(s):
    global BITSINNUM
    cost=0
    count=0
    for c in s:
        if c!='-':
            if count>=5:
                count=0
                cost+=BITSINNUM
            cost+=3
        else:
            count+=1
    if count>=5:
        count=0
        cost+=BITSINNUM+6
    else:
        cost+=count*3
    return cost


def getmatrix(Data, num, length, overlap,order1):
    weights = {}
    dict = {}
    #for i in range(num):
    	#for j in range(num):
    		#weights[i,j]=-1

    for i in range(0,num-length,length-overlap):
        if(i+length>num):
            m=order1[i:]
            #m2=order2[i:]
        else:
            m=order1[i:i+length]
            #m2=order1[i:i+length]
        for i in m:
            for j in m:
                dict[i,j]={}#
                if(i!=j and (i,j) not in weights):
                    weights[i,j],dict[i,j]=getDiff(Data[i], Data[j])#
    
    for i in range(num):
        if i!=num-1:
            dict[num-1,i]={}#
            weights[num-1,i],dict[num-1,i]=getDiff(Data[num-1],Data[i])#
    return weights,dict#



def compressDataExpectation(fileName, window, overlap):
    global BITSINNUM
    global BITSIID
    start=time.time()
    Name=[]
    num, Data,Name = loadData(fileName)#
    BITSIID = int(math.log10(num))*4
    BITSINNUM = int(math.log10(len(Data[0])))*4
  
    prob = getProbability(Data,1)
   

    order3 = getExpectations_2(Data,prob,1)
    
    own = []
    for d in Data:
        own.append(getReduceVal(d))

    weights1,dict = getmatrix(Data,num,window,overlap,order3)
    del order3[:]
   
    Edges = []
    for i in range(num):
        for j in range(num):
            
            if(i==j):
                Edges.append((0,i+1,own[i],0,i+1))
            elif (i,j) not in weights1:
                continue
            else:
                Edges.append((i+1,j+1,weights1[i,j],i+1,j+1))
    solution, refmap2 =Dmst.dmst(num+1,Edges,0)
    del own[:]
    
    del weights1
   
    import os
    FolderName=fileName+'.mstcom/'
    
    os.makedirs(os.path.dirname(FolderName), exist_ok=True)
    fileName=FolderName+ "ref.txt"
    fileName2= FolderName+ "metadata.txt"

    file=open(fileName,'w')#
    file2=open(fileName2,'w')#

    bal=0#
    total_ref=0#
    total_non_ref=0#
    for i in refmap2:
        #print( i[0],i[1])
        j=i[0]
        k=i[1]
        bal+=1#
        
        if(i[0]==0):
            total_ref+=1
           
            file.write(str(i[1]-1)+','+Data[i[1]-1]+"\n")
        else :
            total_non_ref+=1
            compression2.check_mates(dict[i[0]-1,i[1]-1],Data[i[0]-1],Data[i[1]-1],file2,i[0]-1,i[1]-1)#,Data[i[3
            k+=1
    fff=str(num)
    for i in Name:
        fff=fff+"|"+i
    fff+="\n"
    file.write(fff)
  
    file2.write(compression2.final_final_string)
    file2.flush()
   

    file2.close()
    file.close()

    
    #print("ref",total_ref,"non",total_non_ref)
    import bz2
    compressionLevel=9
    import lzma
    Lzip = lzma.LZMACompressor()
    tarbz2contents1 = Lzip.compress(open(fileName, 'rb').read())
    tarbz2contents1+= Lzip.flush()
    
 
    
    size1_7 = sys.getsizeof(tarbz2contents1)
   

    tarbz2contents2 = bz2.compress(open(fileName2, 'rb').read(), compressionLevel)

    file=open(fileName,'wb')#
    file2=open(fileName2,'wb')#
    file.write(tarbz2contents1)
    file2.write(tarbz2contents2)


    file.flush()
    file2.flush()

    file.close()
    file2.close()


    size1_7 = sys.getsizeof(tarbz2contents1)
    size2_2 = sys.getsizeof(tarbz2contents2)
    size3_72 = size1_7 + size2_2
    print('size '+str(size3_72))
    print("ref",total_ref,"non",total_non_ref)

if __name__ == "__main__":
    filename=sys.argv[1]
    window = int(sys.argv[2])
    overlap = int(sys.argv[3])
    start=time.time()
    compressDataExpectation(filename,window,overlap)
    end=time.time()
    print('\nTime Required '+str(end-start))
