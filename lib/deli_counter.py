katz_deli =[]


def line(deli):

    s="The line is currently:"
    if len(deli)>0:
        for i,name in enumerate(deli):
            s=s+" "+str(i+1)+". "+name  
        print(s)
        return s
    else:
        print("The line is currently empty.")
        return "The line is currently empty."

def take_a_number(katz_deli,name):
    katz_deli.append(name)
    print(f"Welcome, {name}. You are number {len(katz_deli)} in line.")
    pass

def now_serving(katz_deli):
     if len(katz_deli)>0:
         print(f"Currently serving {katz_deli[0]}.")
         katz_deli.pop(0)
     else:
         print("There is nobody waiting to be served!")
         

take_a_number(katz_deli, "Ada") #=> Welcome, Ada. You are number 1 in line.
take_a_number(katz_deli, "Grace") #=> Welcome, Grace. You are number 2 in line.
take_a_number(katz_deli, "Kent") #=> Welcome, Kent. You are number 3 in line.
         

line(katz_deli)

now_serving(katz_deli)

line(katz_deli)



    
    