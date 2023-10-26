import csv

print(f'Printint header row')
header_row = 'state,population,cases,casesPer100k\n'
print(header_row)
result_csv = open("./output_files/states-covid-data.txt", "w")
result_csv.write(header_row)

with open('./input_files/states-data.csv') as csv_states_file:
    csv_states_reader = csv.reader(csv_states_file, delimiter=',')
    line_count = 0
    for state_row in csv_states_reader:
        line_count += 1
        if line_count > 1: 
            state_row_state = state_row[0]
            with open('./input_files/covid-data.csv') as csv_covid_file:
                csv_covid_reader = csv.reader(csv_covid_file, delimiter=',')
                for covid_row in csv_covid_reader:  
                    covid_row_state = covid_row[0]
                    if covid_row_state == state_row_state:
                        population = state_row[1]
                        cases = covid_row[1]
                        casesPer100 = (int(cases) / int(population)) * 100000
                        print(f'{state_row[0]},{population},{cases},{int(casesPer100)}')
                        result_csv.write(f'{state_row[0]},{population},{cases},{int(casesPer100)}\n')
result_csv.close()