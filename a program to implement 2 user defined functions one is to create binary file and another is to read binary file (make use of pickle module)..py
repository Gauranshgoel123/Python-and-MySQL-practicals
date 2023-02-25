import pickle
#dictionary objects that are stored in the binary file Emp.dat
emp1={'Empno':1201,'Name':'Anushree','Age': 25,'Salary': 47000}
emp2={'Empno':1211,'Name':'Zoya','Age': 30,'Salary': 48000}
emp3={'Empno':1251,'Name':'Simarjeet','Age': 27,'Salary': 49000}
emp4={'Empno':1266,'Name':'Alex','Age': 29,'Salary': 50000}
#openfile in read mode
empfile=open('Emp.dat','rb')
#read from a file
try:
    while True:
        emp=pickle.load(empfile)
        print(emp)
except EOFError:
        empfile.close(
)
