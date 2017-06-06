# Author        :   Burim Cakolli
# Last Updated  :   06.06.2017

from datetime import datetime

import googlemaps.client
import null as null

from Exceptions.NotDTOClassException import NotDTOClassException
from Models.DTO.LocationSearchDTO import LocationSearchDTO

# Class for Interactions with the Google Maps API
class MapCaller:
    gmaps = null
    geocode_result = null

    # Default Constructor
    # param: "key" is Google API key
    def __init__(self, key):
        self.gmaps = googlemaps.Client(key=key)

    # Gets Location of the given address
    # param: "addressDTO" is a DTO-Class and has the address-information in it
    def GetLocation(self, addressDTO):
        # Validation if address is correct class object
        if isinstance(addressDTO, LocationSearchDTO):
            # Geocoding an address
            self.geocode_result = self.gmaps.geocode(addressDTO.address)
            return self.geocode_result
        else:
            print
            raise NotDTOClassException('Given object is not an expected DTO-Class')

    # Gets Transit direction information of the given two addresses
    # param: "startAddress" is the address to start travelling
    # param: "endAddress" is the address where the journey ends
    def GetDistance(self, startAddress, endAddress):
        if isinstance(startAddress, LocationSearchDTO) and isinstance(endAddress, LocationSearchDTO):
            # Request directions via public transit
            now = datetime.now()
            directions_result = self.gmaps.directions(startAddress.address,
                                                 endAddress.address,
                                                 mode="transit",
                                                 departure_time=now)
            return directions_result
        else:
            print
            raise NotDTOClassException('Given object is not an expected DTO-Class')