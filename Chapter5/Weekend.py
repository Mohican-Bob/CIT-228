import datetime

weekDays = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

now = datetime.date.today()

dayOfWeek = now.weekday()

today = weekDays[dayOfWeek]

daysToWeekend = 6 - dayOfWeek
print("there are ", daysToWeekend-1, "days until the weekend")

quotePrinted = "false"

for left in weekDays[dayOfWeek:daysToWeekend]:
    if today == "Sunday" and quotePrinted == "fale":
        print(left, " Huck it, Chuck it, Football!")
        quotePrinted = "true"
    elif (today == "Monday" or today == "Tuesday" or today == "Wednesday") and quotePrinted == "false":
        print(left, "Busy Busy, School, then work, then work, then school")
        quotePrinted = "true"
    elif today == "Thursday" and quotePrinted == "false":
        print(left, "Thursday Nights are my Friday Nights")
        quotePrinted = "true"
    elif quotePrinted == "false":
        print(left, "Time to Fit in some funtime and maybe one day work on my business website")
        quotePrinted = "true"
    else:
        print(left)

