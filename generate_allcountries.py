import os 
import json

src_dir = "./IconSet/AllCountries"
json_file_path = "./Other/Qure-AllCountries.json"

countries_png = os.listdir(src_dir)
url_prefix = "https://raw.githubusercontent.com/whoiszzj/Qure/master/IconSet/AllCountries"

countries_list = []


for i in range(len(countries_png)):
    countries_name = countries_png[i].split(".")[0]
    country_dict = {}
    country_dict["name"] = countries_name
    country_dict["url"] = url_prefix + "/" + countries_png[i]
    countries_list.append(country_dict)
print("countries_list: ", len(countries_list))

json_dict = {
    "name": "Qure AllCountries",
    "icons": countries_list,
    "description": "All countries flags in the world"
}    

# to json file
with open(json_file_path, "w") as f:
    json.dump(json_dict, f, indent=4)
    print("Json file has been generated successfully!")