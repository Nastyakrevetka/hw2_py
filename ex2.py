# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), 
# а Катя должна их отгадать. Для этого Петя делает две подсказки. 
# Он называет сумму этих чисел S и их произведение P. 
s= int(input("Введите сумму чисел: "))
p= int(input("Введите произведение чисел: "))

for x in range(1001):
    for y in range(1001):
        if p==(x*y) and s==(y+x):
            print ("x= ",x)
            print ("y= ",y)
        
        
  

