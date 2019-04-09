class Bmi:
    def __init__(self, hei, wei, name):
        self.hei = hei
        self.wei = wei
        self.name = name

    def bmi(self):
        bmi = (self.wei / (self.hei * self.hei))*0.00001

        if bmi >= 40:
            result = "고도 비만"
        elif bmi >= 35 and bmi <= 39.9:
            result = "중등도 비만"
        elif bmi >= 30 and bmi <= 34.9:
            result = "경도 비만"
        elif bmi >= 25 and bmi <= 29.9:
            result = "과체중"
        elif bmi >= 18.5 and bmi <= 24.9:
            result = "정상"
        else:
            result = "저체중"
        return result


