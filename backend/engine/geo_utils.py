from collections.abc import Mapping
from typing import Any

import pyproj
from shapely.geometry import mapping, shape
from shapely.ops import transform
from shapely.validation import make_valid

WGS84 = "EPSG:4326"
UTM_43N = "EPSG:32643"

_to_utm43n = pyproj.Transformer.from_crs(WGS84, UTM_43N, always_xy=True).transform
_to_wgs84 = pyproj.Transformer.from_crs(UTM_43N, WGS84, always_xy=True).transform


def _geometry_from_geojson(geojson: Mapping[str, Any]):
    geometry = geojson.get("geometry", geojson)
    geom = make_valid(shape(geometry))
    if geom.is_empty:
        raise ValueError("GeoJSON geometry is empty.")
    return geom


def to_utm43n(geojson: Mapping[str, Any]):
    """Convert a WGS84 GeoJSON geometry or feature to a Shapely geometry in UTM Zone 43N."""
    return transform(_to_utm43n, _geometry_from_geojson(geojson))


def to_utm(geojson: Mapping[str, Any]):
    """Convert a WGS84 GeoJSON geometry or feature to UTM Zone 43N."""
    return to_utm43n(geojson)


def to_wgs84(shapely_geom) -> dict[str, Any]:
    """Convert a Shapely geometry in UTM Zone 43N back to a WGS84 GeoJSON geometry."""
    return dict(mapping(transform(_to_wgs84, shapely_geom)))
