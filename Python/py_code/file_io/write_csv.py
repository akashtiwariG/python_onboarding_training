import os 

csv_content=""

with open("order_details.csv","w") as fi:
    fi.write(csv_content)

for file in os.listdir("."):
    if file.endswith(".csv"):
        print(file)