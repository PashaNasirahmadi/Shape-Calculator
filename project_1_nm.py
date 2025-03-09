import numpy as np
shape_1 = input("شکل مورد نظر خودتان رو بین ، دایره ،مربع ، مثلث ، مستطیل انتخاب کنید")
if shape_1 == "مربع":
    side = int(input("مقدار ضلع را وارد کنید"))
    perimeter = np.multiply(side , 4)
    area = np.multiply(side , side)
    print(f"محیط مربع شما {perimeter}")
    print(f"مساحت مربع شما {area}")
elif shape_1 == "مستطیل":
    side_1 = int(input("ضلع اول مستطیل را وارد کنید"))
    side_2 = int(input("ضلع دوم مستطیل را وارد کنید"))
    perimeter = np.add(side_1 , side_2)
    area = np.multiply(side_1 , side_2)
    print(f"محیط مستطیل شما{perimeter * 2}")
    print(f"مساحت مستطیل شما{area}")
elif shape_1 == "دایره":
    Radius = int(input("شعاع دایره را وارد کنید"))
    diameter = np.multiply(Radius , 2)
    perimeter = np.multiply(diameter , 3.14 )
    area_1 = np.multiply(Radius , Radius )
    area_2 = np.multiply(area_1 , 3.14)
    print(f"محیط دایره شما{perimeter}")
    print(f"مساحت دایره شما{area_2}")
elif shape_1 == "مثلث":
    shape_2 = input("نوع مثلث مورد نظر را از بین ، متساوی الاضلاع ، قائمه ، متساوی الساقین انتخاب کنید")

    if shape_2 == "متساوی الاضلاع":
        side = float(input("ضلع مثلث را وارد کنید: "))
        base = side
        height = float(input("ارتفاع مثلث را وارد کنید: "))
        perimeter = np.multiply(side , 3)
        area_1 = np.multiply(base , height)
        area_2 = np.multiply(area_1 , 0.5)
        print(f"محیط مثلث شما{perimeter}")
        print(f"مساحت مثلث شما{area_2}")

    elif shape_2 == "قائمه":
        side_1 = float(input("ضلع اول را وارد کنید: "))
        side_2 = float(input("ضلع دوم را وارد کنید: "))
        side_3 = float(input("ضلع سوم را وارد کنید: "))
        perimeter_1 = np.add(side_1, side_2)
        perimeter = np.add(perimeter_1 , side_3)
        base = float(input("پایه مثلث را وارد کنید: "))
        height = float(input("ارتفاع مثلث را وارد کنید: "))
        area_1 = np.multiply(base , height)
        area_2 = np.multiply(area_1 , 0.5)
        print(f"محیط مثلث شما{perimeter}")
        print(f"مساحت مثلث شما{area_2}")

    elif shape_2 == "متساوی الساقین":
        side_1 = float(input("مقدار ضلع ساق را وارد کنید"))
        side_2 = float(input("ضلع دوم عادی را وارد کنید"))
        perimeter_1 = np.multiply(side_1 , 2)
        perimeter = np.add(perimeter_1 , side_2)
        base = side_2
        height = float(input("مقدار ارتفاع را وارد کنید"))
        area_1 = np.multiply(base , height)
        area_2 = np.multiply(area_1 , 0.5)
        print(f"محیط مثلث شما{perimeter}")
        print(f"مساحت مثلث شما{area_2}")

    else:
        print("مثلث ورودی اشتباه است")

else:
    print("شکل ورودی اشتباه است")





