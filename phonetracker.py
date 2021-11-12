import phonenumbers
from phonenumbers import timezone,geocoder,carrier

print("Author : ./HACODE")
number = input("Enter Phone Number +__ : ")
phone = phonenumbers.parse(number)
time = timezone.time_zones_for_number(phone)
car = carrier.name_for_number(phone, "en")
reg = geocoder.description_for_number(phone, "en")

print("")
print(phone)
print(time)
print(car)
print(reg)