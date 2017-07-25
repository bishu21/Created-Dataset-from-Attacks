# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 17:29:00 2017

@author: bishwendra
"""
import string
import glob
import collections
from collections import Counter
# training addusers
lis ={}
lis1={}
LIST={}
LIST1={}
count =0
l = ['Adduser','Hydra_FTP','Hydra_SSH','Java_Meterpreter','Meterpreter','Web_Shell']

for prefix in l:
    count=count+1;
    f1 = open("A"+str(count)+".txt", "w+")
    for j in range (1,8):    
       
       for filename in sorted (glob.iglob('C://Users//bishwendra//Desktop//python//ADFA-LD//Attack_Data_Master//'+str(prefix)+'_'+str(j)+'/**/*.txt', recursive=True)):
           f=open(filename,'r')
           for line in f:
               f1.write(line)
               
    f1.seek(0)    
    dict1_7={}
    string = f1.read()
    strparts=string.split()
    for i in range(len(strparts)):
        try:
            dict1_7[tuple(strparts[i:i+7])]+=1
        except:
            dict1_7[tuple(strparts[i:i+7])]=1

            
    
    
    
    lis = collections.Counter(dict1_7).most_common(int(len(dict1_7)*0.3))
    for key in lis :
        LIST[key[0]]=key[1]
   
    
    LIST = Counter(LIST)
    LIST1 = Counter(LIST1)
    LIST1 =LIST1 + LIST
    print(len(LIST1))
        
    
   
    
   
   
    
   
    
                  
          


  
f1 = open("A7.txt", "w+")
for filename in glob.iglob('C://Users//bishwendra//Desktop//python//ADFA-LD//Training_Data_Master/**/*.txt', recursive=True):
    f=open(filename,'r')
    f1.write(f.read())
    
   
f1.seek(0)
    
dict1_7={}
string = f1.read()
strparts=string.split()
for i in range(len(strparts)):
    try:
        dict1_7[tuple(strparts[i:i+7])]+=1
    except:
        dict1_7[tuple(strparts[i:i+7])]=1

            
lis = collections.Counter(dict1_7).most_common(int(len(dict1_7)*0.3))

for key in lis :
     LIST[key[0]]=key[1]


LIST = Counter(LIST)
LIST1 = Counter(LIST1)
LIST1 =LIST1 + LIST
print(len(LIST1))
    

   
f3=open  ("final.txt",'w+')
   
for prefix in l:
    
    for j in range (1,8):
         
         for filename in glob.iglob('C://Users//bishwendra//Desktop//python//ADFA-LD//Attack_Data_Master//'+str(prefix)+'_'+str(j)+'/**/*.txt', recursive=True):
            f3.write("\n"+prefix+str(j)+"\n")
            f=open(filename,'r')
            temp={}
            string = f.read()
            strparts=string.split()
            for i in range(len(strparts)):
                try:
                    temp[tuple(strparts[i:i+7])]+=1
                except:
                    temp[tuple(strparts[i:i+7])]=1

            LIST2 ={}
            for key in LIST1 :
                LIST2[key]=0
            
            for key in temp :
                 if(LIST2.get(key,1)==0):
                     LIST2[key] = temp[key]
            
        
            for key in LIST2:
                f3.write(str(LIST2[key])+" ")
               
for filename in glob.iglob('C://Users//bishwendra//Desktop//python//ADFA-LD//Training_Data_Master//**/*.txt', recursive=True):
            f3.write("\n Training \n")
            f=open(filename,'r')
            temp={}
            string = f.read()
            strparts=string.split()
            for i in range(len(strparts)):
                try:
                    temp[tuple(strparts[i:i+7])]+=1
                except:
                    temp[tuple(strparts[i:i+7])]=1

            LIST2 ={}
            for key in LIST1 :
                LIST2[key]=0
            
            for key in temp :
                 if(LIST2.get(key,1)==0):
                     LIST2[key] = temp[key]
            
        
            for key in LIST2:
                f3.write(str(LIST2[key])+" ")               
   
              

