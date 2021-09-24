import phonenumbers
import argparse
import sys
from sys import argv
from phonenumbers import geocoder

parser = argparse.ArgumentParser()
parser.add_argument ("-v", help= "Phone Number", type=str, dest='target', required=True )

args = parser.parse_args()

number = args.target
ch_nmber = phonenumbers.parse(number, "CH")
print (geocoder.description_for_number(ch_nmber, "en"))


from phonenumbers import carrier
service_nmber = phonenumbers.parse(number, "RO")
print(carrier.name_for_number(service_nmber, "en"))

except KeyboardInterrupt:
        print ('Terminating, Bye'+lgreen)
        sys.exit(0)
except requests.exceptions.ConnectionError as e:
        print (red+"[~]"+" check your internet connection!"+clear)
sys.exit(1)
