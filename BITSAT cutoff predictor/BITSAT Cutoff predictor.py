import pandas as pd
import math
from math import isnan

score=int(input("Please enter your score: "))
perc=score/390*100

sheet1=pd.read_excel(r"BITSAT cutoff analysis.xlsx")
#reading data from an excel file

#determining score is abbreviated as ds, so as to make the code shorter
#ds1=scores in 2022,ds2=scores in 2020

ds1=sheet1['score2'].tolist()
ds2=sheet1['score1'].tolist()
ds2 =[x for x in ds2 if isnan(x)==False]    #clears the NaN values in list

#now, we gather the no of people scoring in certain ranges in a list

scorers22=sheet1['cur_year'].tolist()
scorers20=sheet1['ref_year'].tolist()

#reading data from an excel file
sheet2=pd.read_excel(r"Cutoffs.xlsx")

#programs offered,cutoffs and campuses available are read
cutoffs=sheet2['Cutoff'].tolist()
programs=sheet2['Program '].tolist()
campuses=sheet2['Campus '].tolist()

k=len(ds1)-len(ds2)  #used later for index calculations

#making a list of programmes

choices=[]
for i in range(0,len(cutoffs)):
    program=[programs[i]]+[campuses[i]]
    choices.append(program)

#cutoff ranks of 2020 are appended to this list,determined using a gradient 'm'

cutoff_ranks=[]
for i in cutoffs:
    if 160<=i<ds2[k]:
        m=(40000-scorers20[4])/50
        rank_2020=40000-((i-160)*(m.__round__()))
        cutoff_ranks.append(rank_2020)
    elif ds2[k]<=i<ds2[k-1]:
        m=(scorers20[4]-scorers20[3])/50
        rank_2020=scorers20[4]-((i-ds2[4])*(m.__round__()))
        cutoff_ranks.append(rank_2020)
    elif ds2[k-1]<=i<ds2[k-2]:
         m=(scorers20[3]-scorers20[2])/50
         rank_2020=scorers20[3]-((i-ds2[3])*(m.__round__()))
         cutoff_ranks.append(rank_2020)
    elif ds2[k-2]<=i<ds2[k-3]:
         m=(scorers20[2]-scorers20[1])/50
         rank_2020=scorers20[2]-((i-ds2[2])*(m.__round__()))
         cutoff_ranks.append(rank_2020)
    elif ds2[k-3]<=i<ds2[0]:
         m=(scorers20[1]-scorers20[0])/50
         rank_2020=scorers20[1]-((i-ds2[1])*(m.__round__()))
         cutoff_ranks.append(rank_2020)

#the following function calculates your rank using your score, using a linear gradient
def calc_rank_2022(score,ds1,scorers22):

    if score >= ds1[0] and score < 390:
        grad = scorers22[0]-0/22
        rank_2022=scorers22[0]-((score-ds1[0])*(grad.__round__()))
    elif score>=ds1[1] and score<ds1[0]:
          grad=(scorers22[1]-scorers22[0])/22
          rank_2022=scorers22[1]-((score-ds1[1])*(grad.__round__()))
    elif score>=ds1[2] and score<ds1[1]:
          grad=(scorers22[2]-scorers22[1])/22
          rank_2022=scorers22[2]-((score-ds1[2])*(grad.__round__()))
    elif score>=ds1[3] and score<ds1[2]:
          grad=(scorers22[3]-scorers22[2])/22
          rank_2022=scorers22[3]-((score-ds1[3])*(grad.__round__()))
    elif score>=ds1[4] and score<ds1[3]:
          grad=(scorers22[4]-scorers22[3])/22
          rank_2022=scorers22[4]-((score-ds1[4])*(grad.__round__()))
    elif score>=ds1[5] and score<ds1[4]:
          grad=(scorers22[5]-scorers22[4])/22
          rank_2022=scorers22[5]-((score-ds1[5])*(grad.__round__()))
    elif score>=ds1[6] and score<ds1[5]:
          grad=(scorers22[6]-scorers22[5])/22
          rank_2022=scorers22[6]-((score-ds1[6])*(grad.__round__()))
    elif score>=ds1[7] and score<ds1[6]:
          grad=(scorers22[7]-scorers22[6])/22
          rank_2022=scorers22[7]-((score-ds1[7])*(grad.__round__()))
    else:
         print("sorry, try harder next time.")
    return rank_2022


rank_22=calc_rank_2022(score,ds1,scorers22)    #storing rank in a variable

#this list will display the choices you have depending on your score
list_options=[]

for i in range(0,len(cutoffs)):
    if rank_22<=cutoff_ranks[i]:
       list_options.append(choices[i])

#prints your choices
for i in list_options:
    option = ' '.join([str(elem) for elem in i])
    print(option)
print("\n")
print(f"Congrats! you have scored {perc} percent in BITSAT")





