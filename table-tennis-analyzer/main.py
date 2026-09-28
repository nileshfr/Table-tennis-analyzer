me =input("Enter your name:")#Input taken
opponent=input("Enter your opponent's name:")
sets=int(input("Enter the Number of sets:"))
print(f"{me} vs {opponent}")
print(f"Number of Sets:{sets}")
score_list=[]
for i in range(sets):#Sets scores input taken
    score=input(f"Enter score for Set{i+1}:")
    points=score.split("-")
    score_list.append(points)
int_scorelist=[]
for i in score_list:#converting list to int list
    int_setpoint=[]
    for x in i:
        temp=int(x)
        int_setpoint.append(temp)
    int_scorelist.append(int_setpoint)
s=1
me_won=0
opponent_won=0
for i in int_scorelist:
    if(i[0]>i[1]):
            print(f"{me} won Set{s}")
            me_won+=1
    else:
            print(f"{opponent} won Set{s}")  
            opponent_won+=1 
    s+=1
if(me_won>opponent_won):
     print(f"{me} wins the match")  
elif(opponent_won>me_won):
     print(f"{opponent} wins the match")  
else:
     print("DRAW")     
        