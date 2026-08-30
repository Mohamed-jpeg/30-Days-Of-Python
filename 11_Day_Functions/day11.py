
#1
def add_two_numbers(a, b) ->int :
    return int(a + b)

#2
def area_of_circle(r) -> float:
    return (3.14*r*r);

#3
def add_all_nums(*args) :
    s=0
    for i in args:
        if (isinstance(i, (int, float,complex))) :
            s=s+i
    return s

#4
def cnvert(x)->float :
    return ( x*(9/5) )+32

#5
def check_season(month) -> str:
    seasons = {
        1: "Winter",
        2: "Winter",
        3: "Spring",
        4: "Spring",
        5: "Spring",
        6: "Summer",
        7: "Summer",
        8: "Summer",
        9: "Autumn",
        10: "Autumn",
        11: "Autumn",
        12: "Winter"
    }
    return seasons.get(month, "Invalid month")

#6
def calculate_slope(x1, y1, x2, y2):
    return (y2 - y1) / (x2 - x1)

#7
