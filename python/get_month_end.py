def get_month_end(as_of_date=None):
    import datetime
    if as_of_date == None:
        as_ofdate = datetime.date.today()
    else:
        as_ofdate = datetime.date(as_of_date)
    return(as_ofdate)
        
        
