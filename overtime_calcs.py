

hours_worked = int( input ("Enter hours worked "))
hourly_rate = int (input ("Enter the hourly rate "))

if hours_worked >40:
    print ("Over")
    overtime_hours = hours_worked -40
    regular_pay = 40 * hourly_rate
    overtime_pay = overtime_hours * hourly_rate *1.5
    gross_pay = regular_pay + overtime_pay
    print ("You will be paid $ ", gross_pay)
else:
    gross_pay =hours_worked * hourly_rate
    print  ("You will be paid $ ", gross_pay)
