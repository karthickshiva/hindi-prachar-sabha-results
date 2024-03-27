from bs4 import BeautifulSoup
import csv
import requests

API_ENDPOINT = "https://hindisabhatrichy.com/HTML/results.php?_s=1"
output_rows = []

fromno = 900944
end = 900946
exam = "Praveshika"
exam_year = 2024
exam_month = ['February', 2]

examname_map = {
    'Prathmic': 110,
    'Madhyama': 111,
    'Rashtrabasha': 112,
    'Praveshika': 113
}

skip_first_row = False

while fromno < end:
    tono = min(end, fromno+24)
    data = {'examyear': exam_year,
            'exammonth': exam_month,
            'examname': examname_map[exam],
            'fromno':fromno,
            'tono': tono}

    r = requests.post(url = API_ENDPOINT, data = data)

    response = r.text
    soup = BeautifulSoup(response)
    table = soup.findAll('table')[3]


    rows = table.findAll('tr')[1:] if skip_first_row else table.findAll('tr')
    skip_first_row = True
    for table_row in rows:
        columns = table_row.findAll('td')
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
