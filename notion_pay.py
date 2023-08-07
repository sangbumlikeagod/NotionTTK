from datetime import datetime, timezone
published_date = datetime.now().astimezone(timezone.utc).isoformat()
published_date = datetime.now().date()
print(published_date)

next_day = datetime(published_date.year, published_date.month, published_date.day + 3)
print(next_day)
 
print(published_date) 