#IMPORT DATY

import datetime

#ZBIÓR DANYCH

defaut_names = ["Justin", "john", "Emilee", "Jim", "Ron", "Sandra", "veronica", "Whitney"]
defaut_amounts = [123.32, 94.23, 124.32, 323.4, 23, 322.122323, 32.4, 99.99]

#TEKST WIADOMOŚCI

message = """Hi {name}! 
Thank you for the purchase on {date}. 
We hope you are exicted about using it.
Just as a reminder the purcase total was {amount}.
Have a great one!
Team CFE
"""

#FUNKCJA make_message DO WYSYŁANIA WIADOMOŚCI

def make_message(name_list, amount_list):
   if len(name_list) == len(amount_list):
      i = 0
      now = datetime.datetime.now()
      date_text = now.strftime("%Y/%m/%d")
      for names in name_list:
         mod_name = names[0].upper() + names[1:]
         form_message = message.format(
            name = mod_name,
            date = date_text,
            amount = "%.2f" %(amount_list[i]) 
            )
         print(form_message)
         i = i+1

make_message(defaut_names, defaut_amounts)