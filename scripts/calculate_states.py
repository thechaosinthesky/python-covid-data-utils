import csv
import json

covid_data_results = []

with open('./input_files/states-population.json') as states_json_file:
    states_population_data = json.load(states_json_file)
    for (state_str, population_str) in states_population_data.items():
        state_population = int(population_str)
        state_dictionary = {
            "name": state_str,
            "population": state_population,
        }
        total_state_cases = 0
        total_state_deaths = 0
        cases_by_date = {}
        with open('./input_files/covid-data.csv') as csv_covid_file:
            csv_covid_reader = csv.reader(csv_covid_file, delimiter=',')
            for covid_row in csv_covid_reader: 
                covid_row_state = covid_row[1] 
                if covid_row_state == state_str:
                    covid_row_date = covid_row[0]
                    covid_row_fips = covid_row[2]
                    covid_row_cases = covid_row[3]
                    covid_row_deaths = covid_row[4]
                    total_state_cases += int(covid_row_cases)
                    total_state_deaths += int(covid_row_deaths)
                    cases_by_date[covid_row_date] = {
                        "cases": int(covid_row_cases),
                        "deaths": int(covid_row_deaths)
                    }
            state_dictionary["cases"] = total_state_cases
            state_dictionary["deaths"] = total_state_cases
            state_dictionary["casesPer100K"] = (total_state_cases / state_population) * 100000
            state_dictionary["casesByDate"] = cases_by_date

        covid_data_results.append(state_dictionary)

json_object = json.dumps(covid_data_results, indent=4)
# Writing to sample.json
with open("./output_files/covid_data_results.json", "w") as outfile:
    outfile.write(json_object)