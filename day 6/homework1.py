#მომხმარებლის ნიშნებისგან გამოანგარიშება საშუალო არითმეტიკული და თუ ცხრაზე მეტი იქნება:
#დაუპრინტეთ გილოცავ მატრიცელო შენ გადმოგეცა 300 ლარიანი ბანძი ტოსტერი რასაც შეალიე შენი ცხოვრების წლები
#თუ ეს იქნება 5ზე ნაკლები: დაუპრინტე გილოცავ გაექეცი მატრიცას
#თუ იქნება 5 იდან 9 მდე: დაუპრინტე YOU ARE MID
#თუ იქნება 10ზე მეტი ან 0ზე ნაკლები: დაუპრინტე there is something wrong with you 


score1 = int(input("enter score1: "))
score2 = int(input("enter score2: "))
score3 = int(input("enter score3: "))
score4 = int(input("enter score4: "))
avg_score = (score1 + score2 + score3 + score4) / 4
if avg_score > 9:
    print("გილოცავ მატრიცელო შენ გადმოგეცა 300 ლარიანი ბანძი ტოსტერი რასაც შეალიე შენი ცხოვრების წლები,,")
elif avg_score < 5:
    print("გილოცავ გაექეცი მატრიცას")
elif avg_score >= 5 and avg_score <= 9:
    print("you are mid")
else:
    print("there is something wrong with you")