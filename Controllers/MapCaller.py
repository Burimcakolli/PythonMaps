import googlemaps.client
import null as null

from Exceptions.NotDTOClassException import NotDTOClassException
from Models.DTO.LocationSearchDTO import LocationSearchDTO


class MapCaller:
    gmaps = null
    geocode_result = null

    def __init__(self, key):
        self.gmaps = googlemaps.Client(key=key)

    def GetLocation(self, addressDTO):
        # Validation if address is correct class object
        if isinstance(addressDTO, LocationSearchDTO):
            # Geocoding an address
            self.geocode_result = self.gmaps.geocode(addressDTO.address)
            return self.geocode_result
        else:
            print
            raise NotDTOClassException('Given object is not an expected DTO-Class')

