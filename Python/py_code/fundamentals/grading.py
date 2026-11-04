
score = 85
grade=''

if score >=90:
    grade='A'
elif score >=75:
    grade='B'
elif score >=60:
    grade='C'
elif score >=50:
    grade='D'
else:
    grade='F'

print(f"Score: {score}, Grade: {grade}")

age = int(input("enter a num"))
if age>=18:
    print("can vote")
else:
    print("cannot vote")

status = "eligible" if age >= 18 else "not eligible"
print(f"you are {status} to vote")