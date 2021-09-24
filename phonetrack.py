import phonenumbers
import argparse
import sys
from sys import argv
from phonenumbers import geocoder
from phonenumbers import carrier
from phonenumbers import timezone

parser = argparse.ArgumentParser()
parser.add_argument ("-v", help= "Phone Number", type=str, dest='target', required=True )

args = parser.parse_args()

#colours used
red = '\033[31m'
yellow = '\033[93m'
green = '\033[92m'
clear = '\033[0m'
bold = '\033[01m'
cyan = '\033[96m'

number = args.target
service_nmber = phonenumbers.parse(number, "RO")
ch_nmber = phonenumbers.parse(number, "CH")
            
print(yellow+bold+"-------------------[PHONE NUMBER TRACKING]-------------------"+bold+yellow)
print(green+"[Country Found]: "+green, geocoder.country_name_for_number(ch_nmber, "en"))
print(green+"[City/Area]: "+green, geocoder.description_for_number(ch_nmber, "en"))
print(green+"[Phone Number]: "+green, number)
print(green+"[Carrier]: "+green, carrier.name_for_number(service_nmber, "en"))
print(green+"[Timezone]: "+green, timezone.time_zones_for_number(ch_nmber))
