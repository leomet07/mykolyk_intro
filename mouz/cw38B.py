# From Ms. M
from tkinter import simpledialog, messagebox
from tkinter import*
print("Ask the Expert - Capital Cities of the World")
root = Tk()
root.withdraw()
the_world = {}

def read_from_file():
    with open('capital_data.txt') as file:
        for line in file:
            line = line.rstrip('\n')
            line1 = line.split()
            country = line1[0]
            city = line1[1]
            the_world[country] = city
def write_to_file(country_name, city_name):
    with open('capital_data.txt', 'a') as file:
        file.write('\n' + country_name + '  ' + city_name)
    file.close()
read_from_file()

while True:
    query_country = simpledialog.askstring('Country', 'Type the name of a country:')
    if query_country[0].isupper() == False:
        let = query_country.capitalize()
        new = (let)
        if new in the_world:
            result = the_world[new]
            messagebox.showinfo('Answer', 'The capital city of ' + new + ' is ' + result + '!')
        else:
            new_city = simpledialog.askstring('Teach me', 'I do not know!' + 'What is the capital city of ' + new + '?')
            the_world[new] = new_city
            write_to_file(new, new_city)
        
    elif query_country in the_world:
        result = the_world[query_country]
        messagebox.showinfo('Answer', 'The capital city of ' + query_country + ' is ' + result + '!')
    else:
        new_city = simpledialog.askstring('Teach me', 'I do not know!' + 'What is the capital city of ' + query_country + '?')
        the_world[query_country] = new_city
        write_to_file(query_country, new_city)
root.mainloop()
