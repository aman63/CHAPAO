import bz2
import lzma
import sys
MAP_FOR_REFERENCE_INDEX={}
current_index=0
total_koyta_sequence=0
non_ref=0
ref_=0
reference_list=[]
non_reference_list=[]
final_list=[]
non_ref_dict={}
non_ref={}
non_ref_index={}
non_ref_string={}
class reference_class:
        strings=""
        sequence_number=0
        def __init__(self, sequence_number,strings):
            self.sequence_number = sequence_number
            self.strings = strings

    
def find_data_until_hash(a,current_index):#return a key
    final_data=''
    con=''
    for i in a[current_index:]:
        con+=i   
        if(con=='#'):
           break
        final_data+=con
        current_index+=1
    return final_data,current_index+1

            
    
def find_index_of_sequence(a):
    current_index=0
    mainrefstringindex=''
    while(a[current_index]!=','):
        mainrefstringindex+=a[current_index]
        current_index+=1
    reference=int(mainrefstringindex)
    current_index+=1
    mainnonrefindex=''
    while(current_index<len(a)):
        mainnonrefindex+=a[current_index]
        current_index+=1
        if(current_index==len(a)):
            break
        elif(a[current_index].isdigit()==False):
            break
    non_reference=int(mainnonrefindex)
    return reference,non_reference,current_index
def main_loop(singlerefnonrefdata):
    if(len(singlerefnonrefdata)==0):
        return
    reference,non_reference,current_index=find_index_of_sequence(singlerefnonrefdata)
    loop_around_a_specific_reference_non_reference(reference,non_reference,singlerefnonrefdata,current_index)
    #print('h')
    
    
def loop_around_a_specific_reference_non_reference(reference,non_reference,data,current_index):
    global non_reference_list
    global non_ref
    global non_ref_index
    global non_ref_string
    #A_NON_REFERENCE=non_reference_class(reference,non_reference)
    #A_NON_REFERENCE.strings=[]
    #A_NON_REFERENCE.indexes=[]

    non_ref[reference,non_reference]=[]
    non_ref_index[reference,non_reference]=[]
    non_ref_string[reference,non_reference]=[]
    
    
  
    if(current_index==len(data)):#ref data and nonref data same
        #non_reference_list.append(A_NON_REFERENCE)
        return
    keyindex=[]
    keyindex=data[current_index:].split('#')
    i=0
    allindexofasinglekey=[]
    for singlekeyindex in keyindex:
        if i%2 == 0:
             if(len(singlekeyindex)>0):
                
                 #A_NON_REFERENCE.add_strings(singlekeyindex)
                 non_ref_string[reference,non_reference].append(singlekeyindex)
        else:
            allindexofasinglekey=singlekeyindex.split(',')
            indexes=[]
            
            for j in allindexofasinglekey:
                indexes.append(int(j))
            non_ref_index[reference,non_reference].append(indexes)
            #A_NON_REFERENCE.add_indexes(indexes)
        i+=1
    #non_reference_list.append(A_NON_REFERENCE)
    #non_ref_index[reference,non_reference]=A_NON_REFERENCE.indexes
    #non_ref_string[reference,non_reference]=A_NON_REFERENCE.strings
    #del A_NON_REFERENCE
            
   
def decompressData(data):
    global total_koyta_sequence
    global reference_list
    global PER_CHARACTER_BIT2
    highest_index2=0
    indexes = []
    all_strings = []
    strs=data.split("\n")
    Name={}
    for p in strs:
        if(p.find(",")==-1):
            ind=p.split("|")
            highest_index2=int(ind[0])
            Name=ind[1:]
            break
        else:
            ind=p.split(",")
            index=int(ind[0])
            string=ind[1]
            indexes.append(index)
            all_strings.append(string)
            reference_list.append(reference_class(index,string))
    return indexes, all_strings,Name,highest_index2 
 

def convert__from_ref_to_non_ref(r,t):
    global non_ref_dict
    global final_list
    global non_ref
    global non_ref_index
    global non_ref_string
    s=final_list[r]
    j=0
    for ii in non_ref_string[r,t]:
        prev=0
        for index in non_ref_index[r,t][j]:
            if(prev==0):
                s=s[:index]+str(ii)+s[index+len(ii):]
                prev=index
            else:
                prev+=index
                s=s[:prev]+str(ii)+s[prev+len(ii):]
        j+=1
    final_list[t]=s
    
if __name__ == "__main__":
    filename=sys.argv[1]
    filetype= sys.argv[2]
    highest_index2=0
    file = open(filename+"metadata.txt", "rb")	       
    a=file.read()
    a=bz2.decompress(a)
    a= a.decode("utf-8")

    #print(a)
   
    current_index=0
    file.close()

    sequence_number_indexing=0#cuto
    f=open(filename+"ref.txt","rb")
    data=f.read()
    Lzip = lzma.LZMADecompressor()
    data=Lzip.decompress(data)
    data= data.decode("utf-8")
    
    f.close()
    data=str(data)
    Name={}
    aa, b,Name,highest_index2 = decompressData(data)
   
    for i in range(len(aa)):
        ref_+=1
        MAP_FOR_REFERENCE_INDEX[aa[i]]=b[i]
    f.close()
    non_ref_=0
    fialsplitteddata=a.split('\n')
    for singlerefnonrefdata in fialsplitteddata[:len(fialsplitteddata)-1]:
        main_loop(singlerefnonrefdata)
        non_ref_+=1
       
    ss=""
    len__=highest_index2
   
    is_visited={}
    for ii in range(len__):
        is_visited[ii]=0
    edges={}
    for ii in range(len__):
        edges[ii]=[]
    indeg={}
    for ii in range(len__):
        indeg[ii]=0
    visited={}
    for ii in range(len__):
        visited[ii]=0
    final_list={}
    for ii in range(len__):
        final_list[ii]=""
   
    for key in MAP_FOR_REFERENCE_INDEX:
        final_list[key]=MAP_FOR_REFERENCE_INDEX[key]
    for i in non_ref.keys():
        edges[i[0]].append(i[1])
        indeg[i[1]]+=1
    c=0
    o=0
    while(c<len__-1):
        for i in range(0,len__):
            if(visited[i]==0 and indeg[i]==0):
                visited[i]=1
                for j in edges[i]:
                    indeg[j]-=1
                    if(indeg[j]==0):
                        convert__from_ref_to_non_ref(i,j)
                        o+=1
                        
                c+=1
    agsa=open(filename+"Decompressed.txt",'w')
    if(filetype=='f'):
        for i in range(len__):
            agsa.write(">"+Name[i]+"\n")
            agsa.write(final_list[i]+"\n")
    elif(filetype=='p'):
        agsa.write(str(len(Name))+'\t'+str(len(final_list[i]))+"\n")
        for i in range(len__):
            agsa.write(Name[i])
            howmany=10-len(Name[i])
            for j in range(howmany):
                agsa.write(' ')
            agsa.write(final_list[i]+"\n")
        
    agsa.close()
