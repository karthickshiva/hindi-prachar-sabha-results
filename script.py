from bs4 import BeautifulSoup
import csv
import requests 

API_ENDPOINT = "http://hindisabhatrichy.com/HTML/results.php?_s=1"
output_rows = []

examname = 113
fromno = 901697
end = 901701
exam = "Praveshika"

while fromno < end:
    tono = min(end, fromno+24)
    data = {'examyear': '2020', 
            'exammonth':['February', '2'], 
            'examname':examname, 
            'fromno':fromno,
            'tono': tono} 
    
    r = requests.post(url = API_ENDPOINT, data = data) 

    response = r.text 
    soup = BeautifulSoup(response)
    table = soup.findAll('table')[3]


    for table_row in table.findAll('tr'):
        columns = table_row.findAll('td')a
        output_row = []
        if columns[0].text[0].strip() == '':
            break
        for column in columns:
            output_row.append(column.text.strip())
        output_rows.append(output_row)
    fromno = tono+1
        
with open(exam+".csv", 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(output_rows)