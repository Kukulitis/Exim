figura=int(input('1-Trijsturis ,2-Kvadrats ,3-Taisnsturis'))

if figura==1:
    a=int(input("Side 1 : "))
    b=int(input("Side 2 : "))
    c=int(input("Side 3 : "))
    if a+b>=c and b+c>=a and c+a>=b:
        perimeter=a + b + c
        print("Trijstura perimetrs : ",perimeter)
    else:
        print('Neiespejams Trijsturis')
elif figura==2:
    a=int(input("Side 1 : "))
    perimeter=a*4
    print("Kvadrata perimetrs : ",perimeter)
elif figura==3:
    a=int(input("Side 1 : "))
    b=int(input("Side 2 : "))
    perimeter=a*2+b*2
    print("Taisnstura perimetrs : ",perimeter)
else:
    print("Nepareizs skaitlis, ievadi atbilstošu skaitli.")
    