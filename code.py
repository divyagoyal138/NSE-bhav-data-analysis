import pandas as pd

# Load files
mon = pd.read_csv("sec_bhavdata_full_06042026.csv")
tue = pd.read_csv("sec_bhavdata_full_07042026.csv")
wed = pd.read_csv("sec_bhavdata_full_08042026.csv")
thu = pd.read_csv("sec_bhavdata_full_09042026.csv")
fri = pd.read_csv("sec_bhavdata_full_10042026.csv")

# Step 0: Remove extra spaces from column names
mon.columns = mon.columns.str.strip()
tue.columns = tue.columns.str.strip()
wed.columns = wed.columns.str.strip()
thu.columns = thu.columns.str.strip()
fri.columns = fri.columns.str.strip()

# Step 1: Filter only EQ series
mon = mon[mon['SERIES'] == ' EQ']
tue = tue[tue['SERIES'] == ' EQ']
wed = wed[wed['SERIES'] == ' EQ']
thu = thu[thu['SERIES'] == ' EQ']
fri = fri[fri['SERIES'] == ' EQ']


print(mon.columns)
# (Important) Ensure same order of shares
mon = mon.sort_values('SYMBOL').reset_index(drop=True)
tue = tue.sort_values('SYMBOL').reset_index(drop=True)
wed = wed.sort_values('SYMBOL').reset_index(drop=True)
thu = thu.sort_values('SYMBOL').reset_index(drop=True)
fri = fri.sort_values('SYMBOL').reset_index(drop=True)

# Step 2: Create report
report = pd.DataFrame()

# Share column
report['Share'] = mon['SYMBOL']

# 1. Opening Price
report['Opening'] = mon['OPEN_PRICE']

# 2. Closing Price
report['Closing'] = fri['CLOSE_PRICE']

# 3. High Price
report['High'] = pd.concat([
    mon['HIGH_PRICE'], tue['HIGH_PRICE'], wed['HIGH_PRICE'], thu['HIGH_PRICE'], fri['HIGH_PRICE']
], axis=1).max(axis=1)

# 4. Lowest Price
report['Lowest'] = pd.concat([
    mon['LOW_PRICE'], tue['LOW_PRICE'], wed['LOW_PRICE'], thu['LOW_PRICE'], fri['LOW_PRICE']
], axis=1).min(axis=1)

# 5. Weekly Average (use given column)
report['Avg'] = (
    mon['AVG_PRICE'] +
    tue['AVG_PRICE'] +
    wed['AVG_PRICE'] +
    thu['AVG_PRICE'] +
    fri['AVG_PRICE']) / 5

report['h-l'] = report['High'] - report['Lowest']
#6. fibonacci levels
report["-161.8"] = report['Avg'] -( report['h-l'] *0.1618)    
report["-138.2"] = report['Avg'] -( report['h-l'] *0.1382)
report["-1"] = report['Avg'] -( report['h-l'] * 1)
report["-76.4"] = report['Avg'] -( report['h-l'] *0.764)
report["-61.8"] = report['Avg'] -( report['h-l'] *0.618)
report["-50"] = report['Avg'] -( report['h-l'] *0.5)
report["-38.2"] = report['Avg'] -( report['h-l'] *0.382)
report["-23.6"] = report['Avg'] -( report['h-l'] *0.236)  

report['AVG'] = report['Avg']

report["+23.6"] = report['Avg'] +( report['h-l'] *0.236)  
report["+38.2"] = report['Avg'] +( report['h-l'] *0.382)
report["+50"] = report['Avg'] +( report['h-l'] *0.5)
report["+61.8"] = report['Avg'] +( report['h-l'] *0.618)
report["+76.4"] = report['Avg'] +( report['h-l'] *0.764)
report["+1"] = report['Avg'] +( report['h-l'] * 1)
report["+138.2"] = report['Avg'] +( report['h-l'] *0.1382)
report["+161.8"] = report['Avg'] +( report['h-l'] *0.1618)


# Show result
print(report)
# Show result
print(report)

# Save to new Excel file
report.to_csv("Weekly_Stock_Report.csv", index=False)