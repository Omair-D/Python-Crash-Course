def make_car(manufacturer, model, **options):
    # Make dictionary to represent car
    car_dict = {
        'manufacturer': manufacturer.title(),
        'model': model.title(),
        }
    
    for option, value in options.items():
        car_dict[option] = value
    
    return car_dict

car1 = make_car('Nissan', 'GTR', color = 'black', tow_package = True)
print(car1)

car2 = make_car('Mazda', 'RX7', year = 2002, color = 'yellow')
print(car2)