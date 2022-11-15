
def iterate_dictionary(myDictionary):
    for county, code in myDictionary.parsed_json():
        print(county,code)