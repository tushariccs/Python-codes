student_roll_no= list(map(float,input("Enter a student’s assessment marks: ").split(",")))
#print(student_roll_no)
marks1 = student_roll_no[0]*0.2
marks2 = student_roll_no[1]*0.4
marks3 = student_roll_no[2]*0.4
#taking total of all marks in sum variable 
sum_marks= marks1+marks2+marks3
sum_marks = round(sum_marks, 2)
#rounding to 2 decimal
#print(sum)
if (sum_marks <=100 and sum_marks>=80):
    print("HD")
if(sum_marks<=84 and sum_marks>=75):
    print("D") 
if(sum_marks<=74 and sum_marks>=65):
    print("C") 
if(sum_marks<=64 and sum_marks>=50):
    print("P")
if(sum_marks<=49 and sum_marks>=45):
    print("F or SE or SA")
if(sum_marks<=44 and sum_marks>=0):
    if(marks1==0 and marks2==0 or marks3==0):
        print("AF")
    elif():
        print("F")    
