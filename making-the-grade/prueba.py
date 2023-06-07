
def perfect_score(student_info):
    """Create a list that contains the name and grade of the first student to make a perfect score on the exam.

    :param student_info: list - of [<student name>, <score>] lists.
    :return: list - first `[<student name>, 100]` or `[]` if no student score of 100 is found.
    """
    salida=[]
    for i in range (0,len(student_info)):
        if(student_info[i][1]==100):
            if(len(salida)>=1):
                break
            salida.append(student_info[i])
    
    if(len(salida>0)):
        xd=[salida[0][0],salida[0][1]]
        print(xd)
        return xd
    else:
        aja=[]
        return aja


    pass


student_info=[["Charles", 100], ["Tony", 100], ["Alex", 100]]

(perfect_score(student_info))