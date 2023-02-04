marks =list(map(float,input("Enter the subject marks: ").split(",")))
print(marks)

final_marks = int((marks[0] * 0.2 + marks[1] * 0.4 + marks[2] * 0.4) + 0.5)

if(final_marks >=85 and final_marks <= 100):
    print("High Distinction =", final_marks, 'Grade =HD')
elif(final_marks >= 75 and final_marks < 84):
     print("Distinction =", final_marks, 'Grade =D')
elif(final_marks >= 65 and final_marks < 74):
     print("Credit =", final_marks, 'Grade =C')
elif(final_marks >= 50 and final_marks < 64):
     print(" Pass =", final_marks, 'Grade = P')
     
elif(marks[0] != 0 and marks[1] != 0 and marks[2] != 0):
     if(final_marks >=45 and final_marks <49 ):
          if((marks[0] < 50 and marks[1] < 50) or (marks[1] < 50 and marks[2] < 50) or (marks[0] < 50 and marks[2] < 50)):
               print('Grade = F')
          elif((marks[0] > 50 and marks[1] > 50) or (marks[0] > 50 and marks[1] > 50) or (marks[2]>50)):
               print('Grade = SP')
               
if((marks[0] == 0 and marks[1] == 0) or (marks[0] == 0 and marks[2] == 0) or (marks[1] == 0 and marks[2] == 0) or (marks[0] == 0 and marks[2] == 0) ): 
       print( 'Grade = F')
elif(final_marks <= 44):
    print('Grade = F')