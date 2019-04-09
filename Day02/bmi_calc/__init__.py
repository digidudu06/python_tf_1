from bmi_calc.bmi import Bmi

def main():
    bmi = Bmi(float(input("키 ="))
              ,float(input("몸무게="))
              ,(input("이름=")))


    print("{}는 {}입니다.".format(bmi.name
                              , bmi.bmi()))

if __name__ == '__main__':
    main()