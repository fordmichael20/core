from datetime import datetime

def handle_date_default(asof_date=None):
    if asof_date is None:
      eff_date=datetime.today()
    else:
      eff_date=asof_date.dt.date
    return eff_date

def get_month_end(as_of_date=None):
    eff_date=handle_date_default()
    
def get_quarter_end(as_of_date=None):
    
def get_year_end:
    
def get_last_friday