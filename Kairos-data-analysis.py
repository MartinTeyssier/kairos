# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import matplotlib.pyplot as plt
import csv

data = []
with open('../Downloads/fakedata.csv','r') as file:
    csvreader = csv.reader(file)
    counter = 0
    for row in csvreader:
        if (counter > 0):
            data1 = {'id': int(row[0]), 'age' : int(row[1]), 'sexe' : row[2], 'quartier' : int(row[3]), 'occ' : row[4], 'avis' : row[5]}
            data.append(data1)
        counter =+1

# data = [{'id': 45,'age' : 52, 'sexe' : 'M', 'quartier' : 2, 'occ' : 'E', 'avis' : 'Y'}, {'id': 19,'age' : 19, 'sexe' : 'F', 'quartier' : 8, 'occ' : 'C', 'avis' : 'Y'},{'id': 45,'age' : 52, 'sexe' : 'M', 'quartier' : 2, 'occ' : 'S', 'avis' : 'Y'}]


#x and y axis can be 'age','sex','post'
def get_certain_data(data,num_of_samp,age_range, post_range,sex_range  ,occ_range, avis_range):
    size = len(data)
    data_to_ret = []
    counter = 0
   
    
    num_of_m = 0
    num_of_f = 0
    num_of_nb = 0
    num_of_x = 0
    
    num_of_s = 0
    num_of_e = 0
    num_of_c = 0
    
    num_of_yes = 0
    num_of_no = 0
    num_of_b = 0
    
    for data1 in data:
        id_ = data1.get('id')
        age = data1.get('age')
        sexe = data1.get('sexe')
        quartier = data1.get('quartier')
        occ = data1.get('occ')
        avis = data1.get('avis')
        
        if (age_range[0] <= age and age_range[1]>= age and (sexe in sex_range) and (quartier in post_range) and (occ in occ_range) and (avis in avis_range)):
            data_to_ret.append(data1)
            
            if (sexe == 'M'): num_of_m +=1;
            elif (sexe == 'F'): num_of_f +=1;
            elif (sexe == 'NB'): num_of_nb+=1;
            elif (sexe == 'X'): num_of_x+=1;
            
            if (occ == 'S'): num_of_s +=1;
            elif (occ == 'E'): num_of_e +=1;
            elif (occ == 'C'): num_of_c +=1;
            
            if (avis == 'Y'): num_of_yes+=1;
            elif (avis == 'N'): num_of_no+=1;
            elif (avis == 'B'): num_of_b+=1;
            
            
        counter = counter +1
        
        if (counter >= num_of_samp):
            break
        
    return data_to_ret, [num_of_m,num_of_f,num_of_nb,num_of_x],[num_of_s,num_of_e,num_of_c],[num_of_yes,num_of_no,num_of_b]

#different mode : basic - age_(yes,no,b) - occ_(yes,no,b) - region_(yes,no,b)- - sex_(yes,no,b)
def plot_our_data(data,mode,num_of_samp,age_gap = 5,age_min = 18,age_max = 80,post_wanted = [1,2,3,4,5,6,7,8,9] ,sex_wanted = ['M','F','NB','X'] ,occ_wanted =  ['S','E','C'] ,avis_wanted =['Y','N','B']):
    
    data_clean, sexe_data, occ_data, opinion_data = get_certain_data(data,num_of_samp,[age_min,age_max],post_wanted,sex_wanted, occ_wanted, avis_wanted)
    
    
    #Total number of Yes and No
    if (mode == 'basic'):
        
        counts = []
        for data1 in data_clean:
            counts.append(data1.get('avis'))
            
        
        #plt.hist(counts)
        n, bins, patches = plt.hist(counts, bins=3, facecolor='#2ab0ff', edgecolor='#e0e0e0', linewidth=0.2, alpha=0.7)
        n = n.astype('int')
        
        for i in range(len(patches)):
            patches[i].set_facecolor(plt.cm.viridis(n[i]/max(n)))
        plt.title('Numbers of person in our dataset agreeing (Y), disagreeing(N), or voting blank (B)')
        plt.ylabel('Counts', fontsize = 12)
        plt.xlabel('Agreement',fontsize = 10)
        
    #Age vs number of Yes, No or Blank
    elif (mode == 'age_yes'):
        num_of_bin = int( (age_max - age_min)/age_gap)
        
        counts_yes =[]
        
        for data1 in data_clean:
            
            if (data1.get('avis') == 'Y'):
                counts_yes.append(data1.get('age'))
        
        #plt.hist(counts_yes, bins = num_of_bin)
        n, bins, patches = plt.hist(counts_yes, bins=num_of_bin, facecolor='#2ab0ff', edgecolor='#e0e0e0', linewidth=0.2, alpha=0.7)
        n = n.astype('int')
        
        for i in range(len(patches)):
            patches[i].set_facecolor(plt.cm.viridis(n[i]/max(n)))
            
        plt.title('Agreement repartition by age from ' +str(age_min) +' to ' + str(age_max) + ' yo with grouped by ' + str(age_gap) +' years')
        plt.ylabel('Number of person agreeing', fontsize = 12)
        plt.xlabel('Age',fontsize = 10)
        
    
    elif (mode == 'age_no'):
        num_of_bin = int( (age_max - age_min)/age_gap)
        
        counts_yes =[]
        
        for data1 in data_clean:
            
            if (data1.get('avis') == 'N'):
                counts_yes.append(data1.get('age'))
                
        
        #plt.hist(counts_yes, bins = num_of_bin)
        n, bins, patches = plt.hist(counts_yes, bins=num_of_bin, facecolor='#2ab0ff', edgecolor='#e0e0e0', linewidth=0.2, alpha=0.7)
        n = n.astype('int')
        
        for i in range(len(patches)):
            patches[i].set_facecolor(plt.cm.viridis(n[i]/max(n)))
            
        plt.title('Disagreement repartition by age from ' +str(age_min) +' to ' + str(age_max) + ' yo with grouped by ' + str(age_gap) +' years')
        plt.ylabel('Number of person disagreeing', fontsize = 12)
        plt.xlabel('Age',fontsize = 10)
        
        
    elif (mode == 'age_b'):
        num_of_bin = int( (age_max - age_min)/age_gap)
        
        counts_yes =[]
        
        for data1 in data_clean:
            
            if (data1.get('avis') == 'B'):
                counts_yes.append(data1.get('age'))
                
        
        #plt.hist(counts_yes, bins = num_of_bin)
        n, bins, patches = plt.hist(counts_yes, bins=num_of_bin, facecolor='#2ab0ff', edgecolor='#e0e0e0', linewidth=0.2, alpha=0.7)
        n = n.astype('int')
        
        for i in range(len(patches)):
            patches[i].set_facecolor(plt.cm.viridis(n[i]/max(n)))
            
        plt.title('Blank votes repartition by age from ' +str(age_min) +' to ' + str(age_max) + ' yo with grouped by ' + str(age_gap) +' years')
        plt.ylabel('Number of person disagreeing', fontsize = 12)
        plt.xlabel('Age',fontsize = 10)
        
    elif (mode == 'occ_yes'):
        
        
        counts_yes =[]
        
        for data1 in data_clean:
            
            if (data1.get('avis') == 'Y'):
                counts_yes.append(data1.get('occ'))
        
        #plt.hist(counts_yes, bins = 3)
        n, bins, patches = plt.hist(counts_yes, bins=3, facecolor='#2ab0ff', edgecolor='#e0e0e0', linewidth=0.2, alpha=0.7)
        n = n.astype('int')
        
        for i in range(len(patches)):
            patches[i].set_facecolor(plt.cm.viridis(n[i]/max(n)))
            
        plt.title('Agreement repartion of the populations occupation : S for Students, E for Employed and C for Unemployed')
        plt.ylabel('Number of person agreeing', fontsize = 12)
        plt.xlabel('Occupation',fontsize = 10)
        
    elif (mode == 'occ_no'):
        num_of_bin = int( (age_max - age_min)/age_gap)
        
        counts_yes =[]
        
        for data1 in data_clean:
            
            if (data1.get('avis') == 'N'):
                counts_yes.append(data1.get('occ'))
        
        #plt.hist(counts_yes, bins = num_of_bin)
        
        n, bins, patches = plt.hist(counts_yes, bins=3, facecolor='#2ab0ff', edgecolor='#e0e0e0', linewidth=0.2, alpha=0.7)
        n = n.astype('int')
        
        for i in range(len(patches)):
            patches[i].set_facecolor(plt.cm.viridis(n[i]/max(n)))
            
        plt.title('Disagreement repartion of the populations occupation : S for Students, E for Employed and C for Unemployed')
        plt.ylabel('Number of person disagreeing', fontsize = 12)
        plt.xlabel('Occupation',fontsize = 10)
        
        
    elif (mode == 'occ_b'):
        num_of_bin = int( (age_max - age_min)/age_gap)
        
        counts_yes =[]
        
        for data1 in data_clean:
            
            if (data1.get('avis') == 'B'):
                counts_yes.append(data1.get('occ'))
        
        #plt.hist(counts_yes, bins = num_of_bin)
        n, bins, patches = plt.hist(counts_yes, bins=3, facecolor='#2ab0ff', edgecolor='#e0e0e0', linewidth=0.2, alpha=0.7)
        n = n.astype('int')
        
        for i in range(len(patches)):
            patches[i].set_facecolor(plt.cm.viridis(n[i]/max(n)))
            
        plt.title('Blank vote repartion of the populations occupation : S for Students, E for Employed and C for Unemployed')
        plt.ylabel('Number of person voting blank', fontsize = 12)
        plt.xlabel('Occupation',fontsize = 10)
        
    elif (mode == 'region_yes'):
        num_of_bin = int( (age_max - age_min)/age_gap)
        
        counts_yes =[]
        
        for data1 in data_clean:
            
            if (data1.get('avis') == 'Y'):
                counts_yes.append(data1.get('quartier'))
        
        #plt.hist(counts_yes, bins = num_of_bin)
        n, bins, patches = plt.hist(counts_yes, bins=9, facecolor='#2ab0ff', edgecolor='#e0e0e0', linewidth=0.2, alpha=0.7)
        n = n.astype('int')
        
        for i in range(len(patches)):
            patches[i].set_facecolor(plt.cm.viridis(n[i]/max(n)))
            
        plt.title('Agreement repartition of the population by Montreal Districts')
        plt.ylabel('Number of person agreeing', fontsize = 12)
        plt.xlabel('Montreal Districts',fontsize = 10)
        
        
    elif (mode == 'region_no'):
        num_of_bin = int( (age_max - age_min)/age_gap)
        
        counts_yes =[]
        
        for data1 in data_clean:
            
            if (data1.get('avis') == 'N'):
                counts_yes.append(data1.get('quartier'))
        
        #plt.hist(counts_yes, bins = num_of_bin)
        n, bins, patches = plt.hist(counts_yes, bins=9, facecolor='#2ab0ff', edgecolor='#e0e0e0', linewidth=0.2, alpha=0.7)
        n = n.astype('int')
        
        for i in range(len(patches)):
            patches[i].set_facecolor(plt.cm.viridis(n[i]/max(n)))
            
        plt.title('Disagreement repartition of the population by Montreal Districts')
        plt.ylabel('Number of person disagreeing', fontsize = 12)
        plt.xlabel('Montreal Districts',fontsize = 10)
        
       
    elif (mode == 'region_b'):
        num_of_bin = int( (age_max - age_min)/age_gap)
        
        counts_yes =[]
        
        for data1 in data_clean:
            
            if (data1.get('avis') == 'B'):
                counts_yes.append(data1.get('quartier'))
        
        #plt.hist(counts_yes, bins = num_of_bin)
        n, bins, patches = plt.hist(counts_yes, bins=9, facecolor='#2ab0ff', edgecolor='#e0e0e0', linewidth=0.2, alpha=0.7)
        n = n.astype('int')
        
        for i in range(len(patches)):
            patches[i].set_facecolor(plt.cm.viridis(n[i]/max(n)))
            
        plt.title('Blank vote repartition of the population by Montreal Districts')
        plt.ylabel('Number of person voting blank', fontsize = 12)
        plt.xlabel('Montreal Districts',fontsize = 10)
        
    elif (mode == 'sexe_yes'):
         num_of_bin = int( (age_max - age_min)/age_gap)
         
         counts_yes =[]
         
         for data1 in data_clean:
             
             if (data1.get('avis') == 'Y'):
                 counts_yes.append(data1.get('sexe'))
         
         #plt.hist(counts_yes, bins = num_of_bin)
         n, bins, patches = plt.hist(counts_yes, bins=4, facecolor='#2ab0ff', edgecolor='#e0e0e0', linewidth=0.2, alpha=0.7)
         n = n.astype('int')
         
         for i in range(len(patches)):
             patches[i].set_facecolor(plt.cm.viridis(n[i]/max(n)))
             
         plt.title('Agreement repartition of the population by sex : M for men, W for women, NB for non-binary and X for Prefer not to say')
         plt.ylabel('Number of person agreeing', fontsize = 12)
         plt.xlabel('Sex',fontsize = 10)
         
    elif (mode == 'sexe_no'):
         num_of_bin = int( (age_max - age_min)/age_gap)
         
         counts_yes =[]
        
         for data1 in data_clean:
             
             if (data1.get('avis') == 'N'):
                 counts_yes.append(data1.get('sexe'))
         
         #plt.hist(counts_yes, bins = num_of_bin)
         n, bins, patches = plt.hist(counts_yes, bins=4, facecolor='#2ab0ff', edgecolor='#e0e0e0', linewidth=0.2, alpha=0.7)
         n = n.astype('int')
         
         for i in range(len(patches)):
             patches[i].set_facecolor(plt.cm.viridis(n[i]/max(n)))
             
         plt.title('Disagreement repartition of the population by sex : M for men, W for women, NB for non-binary and X for Prefer not to say')
         plt.ylabel('Number of person disagreeing', fontsize = 12)
         plt.xlabel('Sex',fontsize = 10)
         
    elif (mode == 'sexe_b'):
         num_of_bin = int( (age_max - age_min)/age_gap)
         
         counts_yes =[]
         
         for data1 in data_clean:
             
             if (data1.get('avis') == 'B'):
                 counts_yes.append(data1.get('sexe'))
         
         #lt.hist(counts_yes, bins = num_of_bin)
         n, bins, patches = plt.hist(counts_yes, bins=4, facecolor='#2ab0ff', edgecolor='#e0e0e0', linewidth=0.2, alpha=0.7)
         n = n.astype('int')
         
         for i in range(len(patches)):
             patches[i].set_facecolor(plt.cm.viridis(n[i]/max(n)))
             
         plt.title('Blank vote repartition of the population by sex : M for men, W for women, NB for non-binary and X for Prefer not to say')
         plt.ylabel('Number of person voting blank', fontsize = 12)
         plt.xlabel('Age',fontsize = 10)
        
    else:
        print("Please return a valid mode")
        
    plt.show()
    print("Total stats on populations sex; Men: ",sexe_data[0],"; Women: ",sexe_data[1],"; Non-binary: ",sexe_data[2],"; Prefer not to say: ", sexe_data[3])
    print("Total stats on populations occupation; Students: ", occ_data[0]," ; Employed: ", occ_data[1]," ; Unemployed: ",occ_data[2])
    print("Total opinion of the population; Agrees: ", opinion_data[0], ' ; Disagrees: ', opinion_data[1]," No opinion/Refuses to choose : ", opinion_data[2])

plot_our_data(data,'sexe_b',200)
           
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                