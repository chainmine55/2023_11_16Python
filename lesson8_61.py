import pyinputplus as pyip

def getBMI(height:float, weight:float):
    BMI = weight/(height*0.01)**2
    message = ""

    if BMI < 18.5:
        message = "[您的體重過輕]"
    elif BMI < 24:
        message = "[您的體重為正常]"
    elif BMI < 27:
        message = "[您的體重為過重]"
    elif BMI < 30:
        message = "[您的體重為輕度肥胖]"
    elif BMI < 35:
        message = "[您的體重為中度肥胖]"
    else:
        message = "[您的體重為重度肥胖]"
    return (BMI,message)

while(True):
    h = pyip.inputInt("請輸入身高,單位為公分:")
    print(h)
    w = pyip.inputInt("請輸入體重,單位為公斤:")
    print(w) 
    bmi, message = getBMI(height=h, weight=w)
    print(f"您的BMI是{bmi:.2f},{message}")

