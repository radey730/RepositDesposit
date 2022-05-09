
first_name= input("What is your first name? ") #asks the user what is their first name so they may enter it
last_name= input("What is your last name? ") #asks the user what is their last name so they may enter it
street_number= input("What is the street number of your home address? ") #asks the user what is the street number of their home adress so they may enter it
street_name= input("What is the street name of your home address? ") #asks the user what is the street name of their home adress so they may enter it
city= input("What city do you live in? ") #asks the user what city they live in so they may enter it
state= input("What state do you live in? ") #asks the user what state they live in so they may enter it
zip_code= input("What is your zip code? ") #asks the user what is the zip code of their home adress so they may enter it
po_apt= input("If you have a PO Box or Apartment, enter either 'APT Number' or 'PO Box' and then its number. If not, enter 'q'. ") #prompts the user to enter either 'PO BOX' or 'APT Number' before entering the number of whichever applies to them




if po_apt != 'q':  #checks if value entered for PO Box or Apartment number is 'q' or not and if not, runs the following code
    print(f"{last_name.title()}, {first_name.title()}") #prints the last name, then first name of the user, both names seperated by a comma
    print(f"{street_number} {street_name.title()}") #prints the street number and street name of the user's home address
    print(f"{po_apt} ") #prints the apartment number of the user's home address
    print(f"{city}, {state} {zip_code} ") #prints the city, state, and zip code of the user's home address, seperating the city and state with a comma
elif po_apt == 'q': #checks if value entered for PO Box or Apartment number is 'q' or not and if so, runs the following code
    print(f"{last_name.title()}, {first_name.title()}") #prints the last name, then first name of the user, both names seperated by a comma
    print(f"{street_number} {street_name.title()}") #prints the street number and street name of the user's home address
    print(f"{city}, {state} {zip_code} ") #prints the city, state, and zip code of the user's home address, seperating the city and state with a comma