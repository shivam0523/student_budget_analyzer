student = input("enter student name:")
total_income = float(input("enter total income:"))
food_expense = float(input("enter the food expenses:"))
travel_expense = float(input("enter the travel expense:"))
study_material = float(input("enter all study material expense:"))
internet_expense = float(input("enter all the internet and mobile expense:"))
other_expense = float(input("enter all the other expense:"))

print(" ")
print("|| SUMMARY REPORT || ")
print(" ")

print("student:" , student)
print( "total income is :" , total_income )
print( "all the food expense is :" , food_expense )
print( "travel expense is :" , travel_expense )
print( "study expense is :" , study_material )
print( "mobile/internet expense is :" , internet_expense )
print( "other expense is :" , other_expense )

total_expense = food_expense + travel_expense + study_material + internet_expense + other_expense
print("total_expense:", total_expense)

remaining_balance = total_income - total_expense
print("remaining_balance:" , remaining_balance)

saving_rate = int((remaining_balance / total_income ) * 100)
print("saving_rate :",saving_rate,"%")