import csv
def create_csv_file(infolist):
	with open("StudentAdmn.csv","a",newline="") as csv_file:
		writer=csv.writer(csv_file)
		writer.writerow(infolist)
condition=True
while(condition):
	studentinfo=input("Enter student info separated by space: ")
	print("Entered student info: ",studentinfo)
	studentinfolist=studentinfo.split()
	print("Entered student info as list: ",studentinfolist)
	create_csv_file(studentinfolist)
	check=input("Enter yes to continue or no to terminate: ")
	if check=="yes" or check=="Yes":
		condition=True
	elif check=="no" or check=="No":
		condition=False
