import math 
class Q2:
    
    def average(self, dict):
        avg_marks_1, avg_marks_2, avg_marks_3, avg_marks_4, avg_point = 0, 0, 0, 0, 0
        for a in dict.keys():
            avg_marks_1 += dict[a][0]
            avg_marks_2 += dict[a][1]
            avg_marks_3 += dict[a][2]
            avg_marks_4 += dict[a][3]
            grade = dict[a][4]
            if grade=='HD':
                avg_point+=4.0
            elif grade=='D':
                avg_point+=3.0
            elif grade=='C':
                avg_point+=2.0
            elif grade=='P':
                avg_point+=1.0
            elif grade=='SP':
                avg_point+=0.5
            elif grade=='F':
                avg_point+=0.0
            elif grade=='AF':
                avg_point+=0.0
        
        avg_marks_1 /= len(dict1.keys())
        avg_marks_2 /= len(dict1.keys())
        avg_marks_3 /= len(dict1.keys())
        avg_marks_4 /= len(dict1.keys())
        avg_point /= len(dict1.keys())
        return (avg_marks_1, avg_marks_2, avg_marks_3,avg_marks_4,avg_point)

    
    def count_grades(self, dict1): # function to count the number of grades
        hd,d,c,p,sp,f,af=0,0,0,0,0,0,0

        for a in dict1.keys():
            grade=dict1[a][4]
            if grade=='HD':
                hd+=1
            elif grade=='D':
                d+=1
            elif grade=='C':
                c+=1
            elif grade=='P':
                p+=1
            elif grade=='SP':
                sp+=1
            elif grade=='F':
                f+=1
            elif grade=='AF':
                af+=1
        return (hd,d,c,p,sp,f,af)
    
    def result(self, list, final_marks): # function to grade
        global grade
        if((list[0]==0 and list[1]==0) or (list[0]==0 and list[2]==0) or (list[1]==0 and list[2]==0)):
            if(final_marks <=44):
                # print("Grade is Absent Failed (AF)")
                grade = 'AF'
        elif(final_marks <=44):
            # print("Grade is Fail (F)")
            grade = 'F'
        elif(list[0] != 0 and list[1] != 0 and list[2] != 0): # They do not have any assessment marked zero
            if(final_marks>= 45 and final_marks <= 49): # Their final mark is between 45 – 49 (inclusive)
                if ((list[0]<50 and list[1]<50) or (list[1]<50 and list[2]<50) or (list[0]<50 and list[2]<50)):
                    # print("Grade is Fail (F)")
                    grade = 'F'
                elif((list[0] < 50 and list[1] > 50) or (list[0] > 50 and list[1] < 50)):
                    # print("Grade is SA")
                    grade = 'SA'
                elif(list[2]<50):
                    # print("Grade is SE")  
                    grade = 'SE'    
            elif final_marks >= 50 and final_marks <= 64: # Pass
                # print("Grade is Pass")
                grade = 'P'
            elif final_marks >= 65 and final_marks <= 74: # Credit
                # print("Grade is Credit")
                grade = 'C'
            elif final_marks >= 75 and final_marks <= 84: # Distinction
                # print("Grade is Distinction") 
                grade = 'D'                
            elif final_marks >= 85 and final_marks <= 100: # High Distinction
                # print("Grade is High Distiction")
                grade = 'HD'
        elif(list[0]==0 or list[1]==0 or list[2]==0) and final_marks >= 45 and final_marks <= 49:
            # print("Grade is Fail (F)")
            grade = 'F'
        return grade
    
count = 0
dict1 = {} # declaring a dictionary
a = Q2() # Making object of class

# Taking Input
while True:  
    list = input("Enter three values(Lab Exercise, Report, Final Examination), type letter N to finish : ")  
    if list == 'N':
        break
    list =[float(x) for x in list.split(",")]
    list = [math.ceil(a) for a in list]
    final_marks = math.ceil((list[0]*0.2) + (list[1]*0.4) + (list[2]*0.4))
    list.append(final_marks)
    list.append(a.result(list, final_marks))
        
    if grade=='SA' or grade=='SE':
        supp_marks=float(input("What is this student's supplementary assestment mark: "))
        list.append(int(supp_marks))

        if supp_marks>50:
                                
            list[4]='SP'

        else:

            list[4]='F'

    dict1[count]=list
    count+=1
    
# calling the function to count the number of different grades
count_grade = a.count_grades(dict1)

# Display the number of students
print("Number of students : ", count)

# Display Student's pass rate
pass_rate = ((count_grade[0]+count_grade[1]+count_grade[2]+count_grade[3]+count_grade[4])/count)
print("Student's pass rate : ", pass_rate, 2)

# Display adjusted pass rate
adjusted_pass_rate = ((count_grade[0]+count_grade[1]+count_grade[2]+count_grade[3]+count_grade[4])/(count - count_grade[6]))
print("Student's adjusted pass rate : ", adjusted_pass_rate, 2)

avg = a.average(dict1)


# Average marks
print('Average mark for Assessment 1: %.2f'%round(avg[0], 2))
print('Average mark for Assessment 2: %.2f'%round(avg[1],2))
print('Average mark for Assessment 3: %.2f'%round(avg[2],2))
print('Average final mark: %.2f'%round(avg[3],2))
print('Average grade point: %.2f'%round(avg[4],2))


# Display the list of number of different grades
print('Number of HDs: ',count_grade[0])
print('Number of Ds: ',count_grade[1])
print('Number of Cs: ',count_grade[2])
print('Number of Ps: ',count_grade[3])
print('Number of SPs: ',count_grade[4])
print('Number of Fs: ',count_grade[5]+count_grade[6])

print(dict1)
