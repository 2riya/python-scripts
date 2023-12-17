import pandas as pd
import json


# Load the JSON data
with open('sample.json') as f:
    json_data = json.load(f)


# create pandas dataframe
columns = ["ID", "Title", "Company", "Difficulty"]
df = pd.DataFrame(columns=columns)


# Iterate through the JSON data and populate the DataFrame
for obj in json_data:
    id_, title, link, company, difficulty = int(obj[1]), obj[4], obj[6], obj[0], obj[7]

    # format company name
    company = " ".join(company.split('-'))

    # if row with question already exists, append company name
    if id_ in df["ID"].values:
        company_list = df.loc[df["ID"] == id_, "Company"].values[0].split(", ")

        if not company in company_list:
            df.loc[df["ID"] == id_, "Company"] += ", " + company
    else:
        title_with_link = f'=HYPERLINK("{link}", "{title}")'
        df = df._append({"ID": id_, "Title": title_with_link, "Company": company, "Difficulty": difficulty}, ignore_index=True)


# Save the DataFrame to an Excel file
df.to_excel("Problems List.xlsx", index=False)
