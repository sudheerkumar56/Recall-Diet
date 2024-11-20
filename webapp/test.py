
import datetime

def main():

	current_date = datetime.date.today()

	formatted_date = current_date.strftime("%d-%m-%Y")
	
	month_number = current_date.month

	iso_week_number = current_date.isocalendar()[1]

	d={'date':formatted_date, 'week':iso_week_number, 'month':month_number}
	return d

	
if __name__ == '__main__':
	print(main())