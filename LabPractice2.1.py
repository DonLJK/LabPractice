import statistics
def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Intro to Python")
    v1 = get_user_input()
    display_main_menu(v1)
    calculate_average(v1)
    calc_min_max_temperature(v1)
    calc_med(v1)
    calc_median_temperature(v1)

def display_main_menu(v1):
    print("Values are:", v1)
    #print("display_main_menu")


def get_user_input():
    x = input("Enter some numbers separated by commas (e.g 5, 67, 32)\n")
    y = x.split(", ")
    for i in range(len(y)):
        y[i] = float(y[i])
    return y
    #print("Users_Input")

def calculate_average(v1):
    avg = sum(v1)/len(v1)
    print(avg)
    #print("Calculate Average")

def calc_min_max_temperature(v1):
    minimum = min(v1)
    maximum = max(v1)
    print("The Minimum is: ", minimum)
    print("The Maximum is: ", maximum)
    return minimum, maximum

def calc_median_temperature(v1):
    x = sorted(v1)
    print("This is the sorted value in ascending order: ", x)
    y = len(v1)
    if y % 2 == 0:
        med1= x[y//2]
        med2= x[y//2-1]
        med = (med1 + med2)/2
    else:
        med = x[y//2]
    print("median is: " + str(med))

def calc_med(v1):
    x = sorted(v1)
    y = statistics.median(x)
    print("The median value: ", y)


if __name__ == "__main__":
    main()