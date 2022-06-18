import pandas as pd
def create_companyDF(income, expenses, years):
    """
    Создайте функцию create_companyDF(income, expenses, years), которая  возвращает DataFrame, 
    составленный из входных данных со столбцами “Income” и “Expenses” и индексами, соответствующим годам рассматриваемого периода.
    """
    profit_dict = {'Income': income, 'Expenses': expenses}
    df = pd.DataFrame(profit_dict)
    df.index = years
    return df

def get_profit(df, year):
    """
    А также напишите функцию get_profit(df, year), которая возвращает разницу между доходом и расходом, записанных в таблице df, за год year.
    Учтите, что если информация за запрашиваемый год не указана в вашей таблице вам необходимо вернуть None. 
    """
    import pandas as pd
    if year in df.index:
        income = df.loc[year, "Income"]
        expenses = df.loc[year, "Expenses"]
        profit = income - expenses
    else:
        profit = None
    return profit
    
if __name__ == '__main__':
    expenses = [156, 130, 270]
    income = [478, 512, 196]
    years = [2018, 2019, 2020]
    
    scienceyou = create_companyDF(income, expenses, years)
    print(scienceyou.loc[2020, "Income"])
    print(get_profit(scienceyou, 2020)) #-74