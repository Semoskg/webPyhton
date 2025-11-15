def greeting (name:str,last_name):
    return  'hello '+ name


print(greeting('sami','fathername'))
# posinaol type argument based on the postion known arugumnet
# key word arugrment  with key passed with tge agrument 
print(greeting('sami',last_name='kebebe'))
# defulat argument if no argument is sent it uses the defults 



weight = float(input("Enter your weight : "))
height = float(input("Enter your height : "))
age = int(input("Enter your age: "))
gender = input('enter the Gender: ')


def cal_BMI(height, weight, ):
    return weight / (height * height)
bmi = cal_BMI(height, weight )
print(bmi)


def cal_bmr(height, weight, age, gender):
    if gender == 'male':
        bmr = (10 * weight) + (6.25 * height) + (5 * age) + 5
    else:
        bmr = (10 * weight) + (6.25 * height) - (5 * age) - 161
    return bmr  



bmr = cal_bmr(height, weight, age, gender)
print("BMR:", bmr)

 
 
        





print("Your BMI is:", bmi)


