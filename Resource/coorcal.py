LAT_PER_100M = 0.001622 / 1.8
LONG_PER_100M = 0.005083 / 5.5


def lat_from_met(met):
    return LAT_PER_100M * met / 100.0


def long_from_met(met):
    return LONG_PER_100M * met / 100


def generate_coordinate(center_point_lat, center_point_lng, radius=10000,
                        scan_radius=750):

    top = center_point_lat + lat_from_met(radius)
    left = center_point_lng - long_from_met(radius)

    bottom = center_point_lat - lat_from_met(radius)
    right = center_point_lng + long_from_met(radius)

    scan_radius_step = (lat_from_met(scan_radius),
                        long_from_met(scan_radius))
    lat = top
    lng = left
    while lat > bottom:
        while lng < right:
            yield (lat, lng)
            lng += scan_radius_step[1]
        lng = left
        lat -= scan_radius_step[0]
