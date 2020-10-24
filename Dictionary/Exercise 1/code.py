# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 11:57:52 2020

@author: KM Zubair

"""


import os
import re
import sys

# Function 
def freq(): 
    
    d = {}
    count = 0
    
    
    
    for word in f1.lower().split():
            
            if word not in d:
                d[word] = 0
            d[word] += 1
            
            
    print()        
    print("Each unique word of the file and its frequency") 
    print()       
            
    for x in d.keys():
            
            print (x, d[x])
            
    for y in d:
        if 'of' in y:
            count += 1
        
    print()
    print('The word "of" is used : ', count , 'times.')  
    print()
       
    
    print('The words that end with "ly" are: ')
    print(re.findall(r'\b(\w+ly)\b',f1))        
          
    
if __name__== "__main__":
    
    os.chdir("C:/Users/Robot/Downloads/")
    file1 = open(r"recipe_Ital_115.txt","r") 
    f1 = file1.read()
    
    sys.stdout = open("results.txt", "w")
        
    freq()

    sys.stdout.close()
   
    
    
   
    
    
