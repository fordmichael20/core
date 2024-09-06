from datetime import datetime, timedelta
import calendar
import inspect
import pandas as pd

def todays_date():
    print("running function " + inspect.stack()[0][0].f_code.co_name)
    
    return_date = datetime.today().date()
    return return_date

def get_month_end(as_of_date : str = None, return_type : str = "prior", exclude_weekends : bool = False):
    print("running function " + inspect.stack()[0][0].f_code.co_name)
    
    if as_of_date is None:
        print("No default supplied, running month end for today")
        eff_date = todays_date()
    else:
        if type(as_of_date) == str:
            eff_date = datetime.strptime(as_of_date, "%Y-%m-%d").date()
        else:
            eff_date = as_of_date
            
    mn = eff_date.month
    yr = eff_date.year
    
    if return_type == "prior":
        if mn == 1:
            mn_me = 12
            yr_me = yr - 1
        else:
            mn_me = mn - 1
            yr_me = yr
    elif return_type == "current":
        mn_me = mn
        yr_me = yr
        
    dt_me = calendar.monthrange(yr_me, mn_me)[1]
    dt = datetime(year=yr_me, month = mn_me, day = dt_me)

    if exclude_weekends == True:
        dt = latest_weekday(dt)
    

    return dt


def get_quarter_end(as_of_date : str = None, return_type : str = "prior", exclude_weekends : bool = False):
    print("running function " + inspect.stack()[0][0].f_code.co_name)
    if as_of_date is None:
        eff_date = todays_date()
    else:
        if type(as_of_date) == str:
            eff_date = datetime.strptime(as_of_date, "%Y-%m-%d").date()
        else:
            eff_date = as_of_date
        
    mn = eff_date.month
    yr = eff_date.year
    
    if return_type == "prior":
        if mn in [1, 2, 3]:
            mn_qe = 12
            dt_qe = 31
            yr_qe = yr - 1
        elif mn in [4, 5, 6]:
            mn_qe = 3
            dt_qe = 31
            yr_qe = yr
        elif mn in [7, 8, 9]:
            mn_qe = 6
            dt_qe = 30
            yr_qe = yr
        else:
            mn_qe = 9
            dt_qe = 30
            yr_qe = yr
    elif return_type == "current":
        if mn in [1, 2, 3]:
            mn_qe = 3
            dt_qe = 31
            yr_qe = yr
        elif mn in [4, 5, 6]:
            mn_qe = 6
            dt_qe = 30
            yr_qe = yr
        elif mn in [7, 8, 9]:
            mn_qe = 9
            dt_qe = 30
            yr_qe = yr
        else:
            mn_qe = 12
            dt_qe = 31
            yr_qe = yr
    
    dt = datetime(year=yr_qe, month = mn_qe, day = dt_qe)
    
    if exclude_weekends == True:
        dt = latest_weekday(dt)
    
    return dt

def latest_weekday(as_of_date : str):
    print("running function " + inspect.stack()[0][0].f_code.co_name)
    dow = datetime.weekday(as_of_date)
    if dow == 6:
        return_date = as_of_date - timedelta(days=2)
    elif dow == 5:
        return_date = as_of_date - timedelta(days=1)
    else:
        return_date = as_of_date
    
    return(return_date)

def get_dates_between(earlier_date : str, later_date : str, month_ends_only : bool =False, weekdays_only : bool = False):
    print("running function " + inspect.stack()[0][0].f_code.co_name)

    date_list = pd.date_range(earlier_date, later_date, freq="d")
    if month_ends_only == True:
        'fart'
    return 'barf'        




    
        

            