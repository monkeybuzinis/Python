"""
(e) Modify the program from part (a) and the dictionary so that the user does not have to
know how to spell the month name exactly. That is, all they have to do is spell the first
three letters of the month name correctly.
"""

days = {'January':31, 'February':28, 'March':31, 'April':30,
'May':31, 'June':30, 'July':31, 'August':31,
'September':30, 'October':31, 'November':30, 'December':31}

month_enter=input("enter the month: ")
y=0
for month in days:
    if month.lower()[0:3]==month_enter.lower():
        print("the number of ", month, "is: ", days[month])
        y+=1
if y==0:
    print("there is no such month")

