import math
    
def Q1(list, final_marks):
        if((list[0]==0 and list[1]==0) or (list[0]==0 and list[2]==0) or (list[1]==0 and list[2]==0)):
            if(final_marks <=44):
                print("Grade is Absent Failed (AF)")
        elif(final_marks <=44):
            print("Grade is Fail (F)")
        elif(list[0] != 0 and list[1] != 0 and list[2] != 0): 
            if(final_marks>= 45 and final_marks <= 49): 
                if ((list[0]<50 and list[1]<50) or (list[1]<50 and list[2]<50) or (list[0]<50 and list[2]<50)):
                    print("Grade is Fail (F)")
                elif((list[0] < 50 and list[1] > 50) or (list[0] > 50 and list[1] < 50)):
                    print("Grade is SA")
                elif(list[2]<50):
                    print("Grade is SE")      
            elif final_marks >= 50 and final_marks <= 64: 
                print("Grade is Pass")
            elif final_marks >= 65 and final_marks <= 74: 
                print("Grade is Credit")
            elif final_marks >= 75 and final_marks <= 84: 
                print("Grade is Distinction")
            elif final_marks >= 85 and final_marks <= 10:
                print("Grade is High Distiction")
        elif(list[0]==0 or list[1]==0 or list[2]==0) and final_marks >= 45 and final_marks <= 49:
            print("Grade is Fail (F)")
 
            
list =list(map(float,input("Enter the assessment marks ").split(",")))

final_marks = math.ceil((list[0]*0.2) + (list[1]*0.4) + (list[2]*0.4))

Q1(list, final_marks)

