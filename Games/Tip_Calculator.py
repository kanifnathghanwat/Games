'''
Title: Tip Calculator
Programming language: Python
Developer name: Kanifnath Ghanwat
Guid by: Amol Bhavsar Sir
Date: 20/07/2022
'''

print("***** Tip Calculator *****")
amount=int(input("Enter your total bill amount: "))  # Total amount
tip=int(input("Enter Tip percent: "))                # Tip in percent
person=int(input("Total number of Person: "))
tip=(amount*tip)/100                                 # It gives total tip amount
amount=amount+tip                                    # Add tip in total amount
amount=amount/person                                 # Divide total amount in number of persons
amount = round(amount, 2)                            # Rounds amount upto 2 decimal
print(f"Each Person will pay: {amount}")             # It print total bill of each person

'''
output:

***** Tip Calculator *****

Enter your total bill amount: 2000
Enter Tip percent: 15
Total number of Person: 5
Each Person will pay: 460.
'''
