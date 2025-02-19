from datetime import datetime, timedelta
class Driver:
    def __init__(self, name, license_category, holiday_start, holiday_end, price_km):
        self.name = name
        self.license_category = license_category
        if isinstance(holiday_start, str):
            holiday_start = datetime.strptime(holiday_start, "%Y-%m-%d")
        if isinstance(holiday_end, str):
            holiday_end = datetime.strptime(holiday_end, "%Y-%m-%d")
        self.holiday_start = holiday_start.strftime("%Y-%m-%d")
        self.holiday_end = holiday_end.strftime("%Y-%m-%d")
        self.price_km = price_km

    def can_work(self):
        holiday_start_dt = datetime.strptime(self.holiday_start, "%Y-%m-%d")
        holiday_end_dt = datetime.strptime(self.holiday_end, "%Y-%m-%d")
        if holiday_start_dt <= datetime.now() <= holiday_end_dt:
            return False
        return True

    def can_drive_truck(self):
        return self.license_category == "E"


class Car:
    def __init__(self,make, license_plate, fuel_type, vehicle_expenses, mot_check_date, insurance_date,
                 fuel_consumption_100km, driver):
        self.make = make
        self.license_plate = license_plate
        self.fuel_type = fuel_type
        self.vehicle_expenses = vehicle_expenses
        if isinstance(mot_check_date, str):
            mot_check_date = datetime.strptime(mot_check_date, "%Y-%m-%d")
        if isinstance(insurance_date, str):
            insurance_date = datetime.strptime(insurance_date, "%Y-%m-%d")
        self.mot_check_data = mot_check_date
        self.insurance_date = insurance_date
        self.fuel_consumption_100km = fuel_consumption_100km
        self.driver = driver

    def need_mot_check_or_insurance(self):
        if datetime.now() - self.insurance_date > timedelta(days=365):
            print('Need insurance')
        elif datetime.now() - self.mot_check_data > timedelta(days=365):
            print('Need MOT check')
        else:
            print('No need car can drive')

    def count_price(self, distance, fuel_price):
        fuel_consumption = (self.fuel_consumption_100km / 100) * distance * fuel_price
        driver_price = self.driver.price_km * distance
        return fuel_consumption + driver_price


class Bus(Car):
    def __init__(self,make, license_plate, fuel_type, vehicle_expenses, mot_check_date, insurance_date,fuel_consumption_100km, driver, seats):
        super().__init__(make,license_plate, fuel_type, vehicle_expenses, mot_check_date, insurance_date,fuel_consumption_100km, driver)
        self.seats = seats

    def driveable_bus(self, passenger_number):
        return -(-passenger_number // self.seats)

    def total_cost(self, passenger_number, distance, fuel_price):
        buses = self.driveable_bus(passenger_number)
        return buses * self.count_price(distance, fuel_price)


class Truck(Car):
    def __init__(self,make, license_plate, fuel_type, vehicle_expenses, mot_check_date, insurance_date,fuel_consumption_100km, driver, load_weight, can_tuck_tent, tent_weight):
        super().__init__(make,license_plate, fuel_type, vehicle_expenses, mot_check_date, insurance_date,fuel_consumption_100km, driver)
        self.load_weight = load_weight
        self.can_tuck_tent = can_tuck_tent
        self.tent_weight = tent_weight if can_tuck_tent else 0

    def driveable_truck(self, cargo_weight):
        trips_without_trailer = (cargo_weight // self.load_weight)
        trips_with_trailer = (cargo_weight // (self.load_weight + self.tent_weight)) if self.can_tuck_tent else trips_without_trailer
        return min(trips_without_trailer, trips_with_trailer)


if __name__ == "__main__":
    driver1 = Driver("Jonas Pajudaitis", "E", "2025-06-01", "2025-06-15", 0.5)
    print("Can Driver work?", driver1.can_work())
    print('_______________________________________________')
    car1 = Car('BMW 535i',"ABC-123", "Diesel", 500, "2023-05-10", "2023-07-01", 8, driver1)
    print(f"{car1.make} - {car1.license_plate} Does need MOT or insurance?", car1.need_mot_check_or_insurance())
    print('_______________________________________________')
    bus1 = Bus('Mercedes_Benz',"BUS-789", "Diesel", 700, "2023-05-10", "2024-07-01", 15, driver1, 50)
    print(f"{bus1.make} - {bus1.license_plate} Does need MOT or insurance?", bus1.need_mot_check_or_insurance())
    print("Buses needed:", bus1.driveable_bus(120))
    print("Total cost:", bus1.total_cost(120, 100, 1.5),'$')
    print('_______________________________________________')
    truck1 = Truck('Scania',"TRK-567", "Diesel", 1000, "2025-09-10", "2025-10-01", 30, driver1, 12, True, 5)
    print(f"{truck1.make} - {truck1.license_plate} Does need MOT or insurance?", truck1.need_mot_check_or_insurance())
    print("Trucks needed:", truck1.driveable_truck(30))
