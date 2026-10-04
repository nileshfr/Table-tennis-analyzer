def valid_scores(Scores):
     temp= max(Scores[0],Scores[1])
     return temp >= 11 and (abs(Scores[0]-Scores[1])>=2)
me =input("Enter your name:")#Input taken
opponent=input("Enter your opponent's name:")
sets=int(input("Enter the Number of sets:"))
print(f"{me} vs {opponent}")
print(f"Number of Sets:{sets}")
score_list=[]
for i in range(sets):#Sets scores input taken
    score=input(f"Enter score for Set {i+1}:")
    points=score.split("-")
    score_list.append(points)
int_scorelist=[]
for index,i in enumerate(score_list):#converting list to int list with exception handling
    while True:
        temp=[]
        try:
            if len(i)==2 :
                temp.append(int(i[0]))
                temp.append(int(i[1]))
                int_scorelist.append(temp)
                break 
            else:
                 print("DONT ENTER MULTI DASHES THAT DOESNT HAPPEN IN A MATCH")
                 temp1=input("Enter a valid score:")
                 temp2=temp1.split("-")
                 score_list[index]=temp2
                 i=temp2
        except ValueError :          
            print("DONT INPUT STRING ")
            final=input("ENTER VALID SCORES:")
            validpoints=final.split("-")
            score_list[index]=validpoints
            i = validpoints 
for index,i in enumerate(int_scorelist):#validity of scores
    while(valid_scores(i)==False):
        print(f"The Set Score for Set{index+1} is INVALID")
        temp=(input("Enter a valid Set score please:"))
        temp_points=temp.split("-")
        int_tempoints=[]
        while True:
             try:
               if len(temp_points)==2:
                    for x in temp_points:
                         nilu=int(x)
                         int_tempoints.append(nilu)
                    int_scorelist[index]=int_tempoints
                    i=int_tempoints  
                    break
               else:
                    print("DONT ENTER MULTI DASHES THAT DOESNT HAPPEN IN A MATCH")
                    temp1=input("Enter a valid score:")
                    temp_points=temp1.split("-")
                    
             except ValueError:
                    print("DONT INPUT STRING ")
                    final=input("ENTER VALID SCORES:")
                    temp_points=final.split("-")
        
s=1
me_won=0
opponent_won=0
for i in int_scorelist:#winer of sets
    if(i[0]>i[1]):
            print(f"{me} won Set{s}")
            me_won+=1
    else:
            print(f"{opponent} won Set{s}")  
            opponent_won+=1 
    s+=1
if(me_won>opponent_won):#winner of match
     print(f"{me} wins the match")  
elif(opponent_won>me_won):
     print(f"{opponent} wins the match")  
else:
     print("DRAW")     
        