secret_number = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")
number = int(input("enter an integer:"))
while number != secret_number:
    print("ha ha youre stuckim my loop!")
    
    number= int(input("enter an integer number:"))    
    print("well done,muggle ! you are free now.")
                  
