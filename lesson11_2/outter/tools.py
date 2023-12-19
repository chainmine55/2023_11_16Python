import csv

def saveToCSV(fileName:str,date:list[list],subject_nums:int) -> bool:
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
