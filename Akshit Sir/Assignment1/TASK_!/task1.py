import math
class task1:
    
    def result(self, list, final_marks):
        if((list[0]==0 and list[1]==0) or (list[0]==0 and list[2]==0) or (list[1]==0 and list[2]==0)):
            if(final_marks <=44):
                print("Grade is Absent Failed (AF)")
        elif(final_marks <=44):
            print("Grade is Fail (F)")
        elif(list[0] != 0 and list[1] != 0 and list[2] != 0): # They do not have any assessment marked zero
            if(final_marks>= 45 and final_marks <= 49): # Their final mark is between 45 – 49 (inclusive)
                if ((list[0]<50 and list[1]<50) or (list[1]<50 and list[2]<50) or (list[0]<50 and list[2]<50)):
                    print("Grade is Fail (F)")
                elif((list[0] < 50 and list[1] > 50) or (list[0] > 50 and list[1] < 50)):
                    print("Grade is SA")
                elif(list[2]<50):
                    print("Grade is SE")      
            elif final_marks >= 50 and final_marks <= 64: # Pass
                print("Grade is Pass")
            elif final_marks >= 65 and final_marks <= 74: # Credit
                print("Grade is Credit")
            elif final_marks >= 75 and final_marks <= 84: # Distinction
                print("Grade is Distinction")
            elif final_marks >= 85 and final_marks <= 100: # High Distinction
                print("Grade is High Distiction")
        elif(list[0]==0 or list[1]==0 or list[2]==0) and final_marks >= 45 and final_marks <= 49:
            print("Grade is Fail (F)")
 
            
list =[float(x) for x in input("Enter three values(Lab Exercise, Report, Final Examination) : ").split(",")]
list = [math.ceil(a) for a in list]

final_marks = math.ceil((list[0]*0.2) + (list[1]*0.4) + (list[2]*0.4))
# print(f"The final marks is {final_marks}")

task = task1()
task.result(list, final_marks)
