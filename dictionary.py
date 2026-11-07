STUDENT={
    "NAME":"SURYAJEET MAURYA",
    "COURSE":{
        "COURSE NAME":"B.TECH",
        "COURSE DURATION":"4 YEARS",
        "BRANCH":"CSE(AI)",
        "SEMESTER":"1ST SEM"
    },
    "SUBJECTS":['MATHS','FOC','PCS','LPCC',"IKS",'BEE']
}

print(dict.keys(STUDENT))

print(STUDENT.values())

print(dict.items(STUDENT))

print(STUDENT.get("NAME"))

print(STUDENT["NAME"])

STUDENT.update({"AGE":17})
print(STUDENT)

