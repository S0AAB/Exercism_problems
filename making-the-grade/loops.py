"""Functions for organizing and calculating student exam scores."""


from tkinter.messagebox import RETRY


def round_scores(student_scores):
    """Round all provided student scores.

    :param student_scores: list - float or int of student exam scores.
    :return: list - student scores *rounded* to nearest integer value.
    """
    rounded = []
    for i in range (0,len(student_scores)):
        rounded.append(round(student_scores[i]))
    
    return rounded 

    pass


def count_failed_students(student_scores):
    """Count the number of failing students out of the group provided.

    :param student_scores: list - containing int student scores.
    :return: int - count of student scores at or below 40.
    """
    n=0
    for i in student_scores:
        if(i<=40):
            n+=1
    return n
    pass


def above_threshold(student_scores, threshold):
    """Determine how many of the provided student scores were 'the best' based on the provided threshold.

    :param student_scores: list - of integer scores.
    :param threshold: int - threshold to cross to be the "best" score.
    :return: list - of integer scores that are at or above the "best" threshold.
    """
    salida=[]
    for i in student_scores:
        if(i>=threshold):
            salida.append(i)
    return salida
    pass


def letter_grades(highest):
    """Create a list of grade thresholds based on the provided highest grade.

    :param highest: int - value of highest exam score.
    :return: list - of lower threshold scores for each D-A letter grade interval.
            For example, where the highest score is 100, and failing is <= 40,
            The result would be [41, 56, 71, 86]:

            41 <= "D" <= 55
            56 <= "C" <= 70
            71 <= "B" <= 85
            86 <= "A" <= 100
    """
    calculo=(highest-40)//4
    resultado=[]
    D=41;
    C=D+calculo;
    B=C+calculo;
    A=B+calculo;
   
    resultado= [D,C,B,A]
    return resultado

    pass


def student_ranking(student_scores, student_names):
    """Organize the student's rank, name, and grade information in ascending order.

    :param student_scores: list - of scores in descending order.
    :param student_names: list - of string names by exam score in descending order.
    :return: list - of strings in format ["<rank>. <student name>: <score>"].
    """
    n=0;
    nombre=[]
    notas=[]
    for i in range (0,len(student_scores)):
        ind=student_scores.index(max(student_scores))
        nombre.append(student_names[ind])
        notas.append(student_scores[ind])
        student_names.pop(ind)
        student_scores.pop(ind)
    
    
    salida=[]

    for i in range(0,len(notas)):
        salida.append ((str(i+1))+". "+(str(nombre[i]))+": "+(str(notas[i])))
    

    return salida;

    pass


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
    
    if(len(salida)>0):
        xd=[salida[0][0],salida[0][1]]
        print(xd)
        return xd
    else:
        aja=[]
        return aja


    pass







