# Author        :   Burim Cakolli
# Last Updated  :   06.06.2017

import unittest
from Controllers.MapCaller import MapCaller
from Models.DTO.LocationSearchDTO import LocationSearchDTO

class MapCallerTest(unittest.TestCase):

    def test_GetLocation(self):
        mapCaller = MapCaller('AIzaSyAymSvbwBm5dvL_XhvHEYe7xsNfPvET1Ok')
        locationName = LocationSearchDTO("Fachstrasse 28A 8942 Oberrieden")
        geoLocation = mapCaller.GetLocation(locationName)
        geoLocation = geoLocation[0]['geometry']['location']

        # Checks coordinates of = Fachstrasse 28A 8942 Oberrieden
        self.assertEqual(geoLocation['lat'], 47.27771389999999)
        self.assertEqual(geoLocation['lng'], 8.5785527)

    def test_GetDistance(self):
        mapCaller = MapCaller('AIzaSyAymSvbwBm5dvL_XhvHEYe7xsNfPvET1Ok')
        startAddress = LocationSearchDTO("Fachstrasse 28A 8942 Oberrieden")
        endAddress = LocationSearchDTO("Roswiesenstrasse 34 8051 Zürich")
        result = mapCaller.GetDistance(startAddress, endAddress)
        print(result)