import datetime, bday_nessages 
date1 = datetime.date.today()
date2 = datetime.date(2025, 3, 2)
days_away = date1 - date2
if days_away == 0:
    print(bday_nessages.bday_wish)
else:
    print(f"My next birthday is {days_away.days} days away")
