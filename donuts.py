#arr with grades
arr = [83,82,82,85,82,83,85,87,85,78]
#creating function
def donuts(donut_celebration):
    donut_celebration = []
    avg = 0
# for loop, looks at each index value and measures avg
    for num in arr:
#formula for avg
        avg = avg + num
    avg = num /10

    if num >= 90:
        print(" You all got an A. You all get a donut!")
    elif num >= 80:
        if num < 90:
            print(" You all got a B. You all get half a donut!")
    elif num >= 70:
        if num <80:
            print(" You all got a C. You all get one third of a donut!")
    elif num >= 65:
        if num <70:
            print(" You all got a D. You all owe Mr. James half a donut!")
    elif num <= 65:
        if num <70:
            print(" You all got an F. You all fail")
    print (donut_celebration)
#calling function
donuts(arr)
