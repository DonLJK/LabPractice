def main():
    calculate(1.76, 60)
    #calculate(weight="1.76", height="60")



def calculate(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))

    bmi = weight/(height * height)
    print(bmi)

    if (bmi < 18.5):
        print("Under Weight")
    elif(bmi <= 25.0):
        print("Normal Weight")
    else:
        print("Over Weight")












if __name__ == '__main__':
    main()