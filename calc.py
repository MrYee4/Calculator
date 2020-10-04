# Spencer Nettles
# CS246
# Calculator program will take exations and solve them
import math

def magVector():
    Vx = float(input("Vx = "))
    Vy = float(input("Vy = "))
    mag = math.sqrt((Vx * Vx) + (Vy * Vy))
    print("Magnitude of the vector = ", mag)

def angleVector():
    Vx = float(input("Vx = "))
    Vy = float(input("Vy = "))    
    ang = math.atan(math.radians(Vy/Vx))
    print("Angle of the vector = ", ang)

def findVx():
    mag = float(input("Magnitude = "))
    ang = float(input("Angle = "))    
    Vx = mag * math.cos(math.radians(ang))
    print("Vx = ", Vx)

def findVy():
    mag = float(input("Magnitude = "))
    ang = float(input("Angle = "))    
    Vy = mag * math.sin(math.radians(ang))
    print("Vy = ", Vy)

def findVxYAxis():
    mag = float(input("Magnitude = "))
    ang = float(input("Angle = "))    
    Vx = mag * math.sin(math.radians(ang))
    print("Vx from y axis = ", Vx)

def findVyYAxis():
    mag = float(input("Magnitude = "))
    ang = float(input("Angle = "))    
    Vy = mag * math.cos(math.radians(ang))
    print("Vy from y axis = ", Vy)

def main():
    print("Select One:")
    print("1. Magnitude of vector")
    print("2. Angle of Vector")
    print("3. Find Vx")
    print("4. Find Vy")
    print("5. Find Vx from y axis")
    print("6. Find Vy from y axis")
    print("q. Quit")
    choice = input()
    
    while choice != "q":
        if choice == "1":
            magVector()
        elif choice == "2":
            angleVector()
        elif choice == "3":
            findVx()
        elif choice == "4":
            findVy()
        elif choice == "5":
            findVxYAxis()
        elif choice == "6":
            findVyYAxis()
        choice = input()


if __name__ == "__main__":
    main()
