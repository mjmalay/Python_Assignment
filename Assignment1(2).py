#2. Write a python program to find total and average mark of a student and take
#   5 different subject along with marks of 10 students using dictionary.

StudentName={'Ram','Syam','Hari','Keshab','Soundarya'}
StudentSubject={'C','CPP','Java','Python','Perl'}
StudentName['Ram']={StudentSubject[78,96,73,93,83]}
for key,value in StudentName.items():
    TotalMarks = sum(StudentName[key][StudentSubject])
    StudentName[key].update({"total_marks":TotalMarks})
print(TotalMarks)
