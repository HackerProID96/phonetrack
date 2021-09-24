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

number = args.target
service_nmber = phonenumbers.parse(number, "RO")
ch_nmber = phonenumbers.parse(number, "CH")
            
print(red+"-------------------[PHONE NUMBER TRACKING]-------------------"+red)
print(green+"[Internasional Format]: "+green, phonenumbers.format_number(
            PhoneNumberObject, phonenumbers.PhoneNumberFormat.INTERNATIONAL).split(' ')[0])
print(green+"[Local Format]: "+green, phonenumbers.region_code_for_country_code(int(numberCountryCode)))
print(green+"[Country Found]: "+green, geocoder.country_name_for_number(ch_nmber, "en"))
print (green+"[City/Area]: "+green, geocoder.description_for_number(ch_nmber, "en"))
print(green+"[Carrier]: "+green, carrier.name_for_number(service_nmber, "en"))
print(green+"[Timezone]: "+green, timezone.time_zones_for_number(ch_nmber))

except KeyboardInterrupt:
        print ('Terminating, Bye'+lgreen)
        sys.exit(0)
except requests.exceptions.ConnectionError as e:
        print (red+"[~]"+" check your internet connection!"+clear)
sys.exit(1)
