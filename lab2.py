def calculate_bmi(height, weight):
 print("Height = " + str(height))
 print("Weight = " + str(weight))
 bmi=weight/(height*height)
 print(str(bmi))
 if(bmi<18.5):
    print("Under Weight ")
    print("-1")
 elif(bmi>25.0):
   print("Over Weight")
   print("1")
 else:
   print("Normal Weight")
   print("1")
 

def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67,32)")

def get_user_input():
    numbers=input()
    num=numbers.split(",")
    num_float=[float(x) for x in num]
    return(num_float)
    

def calc_average(n):
   total=0
   for x in n:
      total=total+x
   avg=total/(len(n))
   print("the average temperature value is "+ str(avg))
    
def find_min_max(n):
   maximum=max(n)
   minimum=min(n)
   print("minimum value is "+str(minimum)+",  maximum value is "+str(maximum))
   

def sort_temperature():
    print("display_main_menU")

def calc_median_temperature(n):
   print()
 

def main():
   value=[]
   calculate_bmi(weight=57, height=1.73)
   display_main_menu()
   value=get_user_input()
   calc_average(value)
   find_min_max(value)

main()

   




