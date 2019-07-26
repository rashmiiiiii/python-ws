def showInfo(student_dict):
    for k,v in student_dict.items():
        print(f"{k}:{v}")

student_dict ={"NCET-EC001":"Rajesh","NCET-EC002":"Ramesh","NCET-EC003":"Rakesh"}
showInfo(student_dict)