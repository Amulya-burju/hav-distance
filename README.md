# hav-distance

## Problem Statement

An app that will accept Latitude and longitude positions of the source and destination and calculates the great-circle distance between them usinf the Haversine Formula.

a = sin²(Δφ/2) + cos φ1 ⋅ cos φ2 ⋅ sin²(Δλ/2)
c = 2 ⋅ atan2( √a, √(1−a) )
d = R ⋅ c

where	φ is latitude, 
      λ is longitude, 
      R is earth’s radius (mean radius = 6,371km);
      
 NOTE that angles need to be in radians to pass to trig functions!
