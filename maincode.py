import random
player=0
cpu=0
print("Welcome to Rock Paper Scissors game!!")
print("Please enter your name:")
name=input()

for i in range(0,3):
    li=["rock","paper","scissors"]
    x=random.choice(li)
    print("Please enter your choice:")
    ch=input()
    if x=="rock" and ch=="paper":
        print("CPU result:",x)
        print(name,end=" ")
        print("result:",ch)
        print(name,end=" ")
        print("won")
        player=player+1
        
    if x=="rock" and ch=="scissors":
        print("CPU result:",x)
        print(name,end=" ")
        print("result:",ch)
        print("CPU won")
        cpu=cpu+1
           
    if x=="rock" and ch=="rock":
        print("CPU result:",x)
        print(name,end=" ")
        print("result:",ch)
        print("Tie between CPU and ",name)
        
    if x=="paper" and ch=="paper":
        print("CPU result:",x)
        print(name,end=" ")
        print("result:",ch)
        print("Tie between CPU and ",name)
    
          
    if x=="paper" and ch=="scissors":
        print("CPU result:",x)
        print(name,end=" ")
        print("result:",ch)
        print(name,end=" ")
        print("Won")
        player=player+1            
    
           
    if x=="paper" and ch=="rock":
        print("CPU result:",x)
        print(name,end=" ")
        print("result:",ch)
        print("CPU Won")
        cpu=cpu+1 
        
        
    if x=="scissors" and ch=="rock":
        print("CPU result:",x)
        print(name,end=" ")
        print("result:",ch)
        print(name,end=" ")
        print("Won")
        player=player+1 
        
        
    if x=="scissors" and ch=="scissors":
        print("CPU result:",x)
        print(name,end=" ")
        print("result:",ch)
        print(name,end=" ")
        print("Tie between CPU and ",name)
    
    if x=="scissors" and ch=="paper":
        print("CPU result:",x)
        print(name,end=" ")
        print("result:",ch)
        print("CPU Won")
        cpu=cpu+1       
    
if cpu>player:
    print("CPU won the tournament!!")
        
        
if cpu<player:
    print(name,end=" ")
    print("Won the tournament!!")
        
        
if cpu==player:
    print("Tournament tie between CPU and ",name)        
    
print("final score:")
print(name,end=" ")
print("score:",end=" ")
print(player)
print("CPU score:",cpu)
      
