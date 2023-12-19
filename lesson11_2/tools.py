import random,csv
def getStudents(students_nums:int=1,scores_nums:int=2) ->list[list]:
    '''
    參數:student_nums -> 學生人數\n
    參數:scores_nums -> 科目數\n
    '''
    with open('names.txt',mode='r',encoding='utf-8') as file:
        names:str = file.read()

    nameList:list[str] = names.split('\n')

    students:list[list] = []   #建立二維list

    names:list[str] = random.choices(nameList,k=students_nums)
    for name in names:
        stu:list[int|str]=[]
        stu.append(name)
        for i in range(scores_nums):
            stu.append(random.randint(40,100))
        students.append(stu)

    return students

def saveToCSV(fileName:str,date:list[list],subject_nums:int)->None:
    fileName +=".csv"
    subjects = [f'科目{+1}'for i in range(subject_nums)]
    fields = ['姓名']
    fields.extend(subjects)
    with open (fileName,mode='w',encoding='utf-8',newline='') as file:
        try:
            writer = csv.writer(file)
            #fields = None (存檔失敗用)
            writer.writerow(fields)
            writer.writerows(date)
        except:
            return False
        else:
            return True
