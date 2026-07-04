from math import hypot

from shapely.geometry import shape

from engine.geo_utils import to_utm, to_utm43n, to_wgs84


NOIDA_SECTOR_62_POLYGON = {
    "type": "Feature",
    "properties": {"name": "Noida Sector 62 sample plot"},
    "geometry": {
        "type": "Polygon",
        "coordinates": [
            [
                [77.39095, 28.61385],
                [77.39108, 28.61385],
                [77.39108, 28.61398],
                [77.39095, 28.61398],
                [77.39095, 28.61385],
            ]
        ],
    },
}


def test_noida_sector_62_round_trip_within_one_centimeter():
    utm_geom = to_utm(NOIDA_SECTOR_62_POLYGON)
    round_tripped = to_wgs84(utm_geom)
    round_tripped_utm = to_utm43n(round_tripped)

    original_coords = list(utm_geom.exterior.coords)
    returned_coords = list(round_tripped_utm.exterior.coords)

    max_delta_m = max(
        hypot(original[0] - returned[0], original[1] - returned[1])
        for original, returned in zip(original_coords, returned_coords)
    )

    assert max_delta_m <= 0.01
    assert shape(round_tripped).is_valid
