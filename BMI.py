def run(a,b):
    if(a == "M"):
        print("M")
        if b < 20:
            print("M < 20")
        elif b > 25:
            print("M > 25")
        else :
            print("M OK")

    if (a == "F"):
        print("F")
        if b < 18:
            print("F > 18")
        elif b > 22:
            print("F > 22")
        else:
            print("F OK")

gender = str(input("輸入性別(男生請打M,女聲請打F)"))
height = eval(input()) #以公尺為單位
weight = eval(input()) #以公斤為單位
BMI = weight/(height*height)

if (gender == "M"):
    run = run(gender,BMI)

if (gender == "F"):
    run = run(gender,BMI)

else:
    print("機掰性別打錯了")
    exit()