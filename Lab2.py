days_in_month = [('January',[31]),('February',[28,29]),('March',[31]),('April',[30]),('May',[31]),('June',[30]),('July',[31]),('August',[31]),('September',[30]),('October',[31]),('November',[30]),('December',[31])]

names_of_days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']


def  monthDays(month):

    #for j in range(days_in_month):
    if not month in [days_in_month[x][0] for x in range(len(days_in_month))]:
            return []
    else:
        for i in range(len(days_in_month)):
            if month == days_in_month[i][0]:
                return days_in_month[i][1]

def week_day(y, m, d):
    if m == 1 or m == 2:
        m = m + 12
        y = y - 1

    day = int(((int(13*m+3) / 5 + d + y + int(y / 4) - int(y / 100) + int(y / 400)) %7))
    #print(day)
    return names_of_days[day]

def unLucky(yr):
    # Write your code here
    #lst = []
    #for i in range(1,13):
        #print(week_day(yr,i,13))
        #if week_day(yr,i,13) == "Friday":
            #lst = lst + [(13,i,yr)]

    lst = [(13,i,yr) for i in range(1,13) if week_day(yr,i,13) == "Friday"]
    return lst

def so_Unlucky(start_year, end_year):
    # Write your code here
    yearlst = []
    for i in range(start_year, end_year+1):
        if len(unLucky(i)) > 2:
            yearlst = yearlst + [i]
    return yearlst
    
