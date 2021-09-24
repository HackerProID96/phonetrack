import phonenumbers
import argparse
import sys
parser = argparse.ArgumentParser()
parser.add_argument ("-v", help= "target/host IP address", type=str, dest='target', required=True )
from sys import argv
from phonenumbers import geocoder

args = parser.parse_args()



number = args.target
ch_nmber = phonenumbers.parse(number, "CH")
print (geocoder.description_for_number(ch_nmber, "en"))


from phonenumbers import carrier
service_nmber = phonenumbers.parse(number, "RO")
print(carrier.name_for_number(service_nmber, "en"))
