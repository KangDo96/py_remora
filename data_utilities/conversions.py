from datetime import datetime

# fix_date converts strings starting with any of MM/DD/YYYY, M/DD/YYYY, or MM/D/YYYY to python datetime
# useful for when your data source drops 0s for month and day numeric values
# for additional possible formats add more try:strptime blocks
def fix_date(dt_string):
    if type(dt_string) != str:
        print('fix_date was pass a non-string of value {}'.format(dt_string))
        try:
            dt_string = str(dt_string)
        except:
            print('conversion of value {} of type {} to string failed'.format(dt_string, type(dt_string)))
            return None
        
    fixed_dt = None
    try:
        fixed_dt = datetime.strptime(dt_string[0:10], '%m/%d/%Y')
    except:
        pass
    if fixed_dt == None:
        try:
            fixed_dt = datetime.strptime('0{}'.format(dt_string[0:9]), '%m/%d/%Y')
        except:
            pass
    if fixed_dt == None:
        try:
            fixed_dt = datetime.strptime('{}0{}'.format(dt_string[0:3], dt_string[3:9]), '%m/%d/%Y')
        except:
            pass
    if fixed_dt == None:
        try:
            fixed_dt = datetime.strptime('0{}/0{}'.format(dt_string[0], dt_string[2:8]), '%m/%d/%Y')
        except:
            print('all date conversions failed on value {}'.format(dt_string))
            pass
    return fixed_dt