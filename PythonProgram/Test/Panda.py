import  pandas as pd
df = pd.ExcelFile("userinformation.xlsx")
df1 = df.parse("credential")
df1.to_html("a.html")