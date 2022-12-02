from views import Cars

def main():
    client = Cars()
    client.save()
    print('Privet! tebe dostupno: \n\tLIST-1\n\tDETAIL-2\n\tCREATE-3\n\tUPDATE-4\n\tDELETE-5')
    choice = input('Enter action(1,2,3,4,5): ')
    if choice.strip() == '1':
        print(client.list())
    elif choice.strip() == '2':
        id = int(input('Enter id: '))
        print(client.detail(id))
    elif choice.strip() == '3':
        brand = input('Enter brand: ')
        marka = input('Enter marka: ')
        year_of_issue = int(input('Enter year of issue: '))
        engine_volume = float(input('Enter engine volume: '))
        color = input('Enter color: ')
        mileage = int(input('Enter miliage: '))
        price = float(input('Enter price: '))
        print(client.entry(brand, marka, year_of_issue, engine_volume, color, mileage, price))
        print(client.save())
    elif choice.strip() == '4':
        id = int(input('Enter id: '))
        izm = input('What do you want to change (brand, marka, year of issue, engine volume, body type, color, mileage, price): ').strip().lower()
        if izm == 'brand':
            change = input('Enter changes: ')
            print(client.patch(id, brand = change))
            print(client.save())
        elif izm =='marka':
            change = input('Enter changes: ')
            print(client.patch(id, marka = change))
            print(client.save())
        elif izm =='year of issue':
            change = int(input('Enter changes: '))
            print(client.patch(id, year_of_issue = change))
            print(client.save())
        elif izm =='engine volume':
            change = float(input('Enter changes: '))
            print(client.patch(id, engine_volume = round(change, 1)))
            print(client.save())
        elif izm =='color':
            change = input('Enter changes: ')
            print(client.patch(id, color = change))
            print(client.save())
        elif izm =='mileage':
            change = int(input('Enter changes: '))
            print(client.patch(id, mileage = change))
            print(client.save())
        elif izm =='price':
            change = float(input('Enter changes: '))
            print(client.patch(id, price = round(change, 2)))
            print(client.save())
        else:
            change = input('Enter changes: ')
            print(client.patch(id, body_type = change))
            print(client.save())
    elif choice.strip() == '5':
        id = int(input('Enter id: '))
        print(client.delete(id))
        print(client.save())
    else:
        print('Nevernii vibor!')

    answer = input("Hotite prodolzit'?(yes/no): ")
    if answer.lower().strip() == 'yes':
        main()
        
    else:
        print('Good bay!')

main()

    