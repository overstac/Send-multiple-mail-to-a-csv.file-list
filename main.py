import yagmail
import os
import pandas
sender= "pintilei92@gmail.com"
subject= "This is the subject!"
x= chr(13)

df = pandas.read_csv("contacts.csv")

yag= yagmail.SMTP(user= sender, password=os.environ['PASS'])

for index, row in df.iterrows():
  contents= [f"Hey, {row['name']} you have to pay {row['amount']} Bill is attached!", row["filepath"]]
  yag.send(to= row["email"], subject= subject, contents= contents)
  print("Email sent!")    
