"use client";

import { useState } from "react";
import type { StyleSpecification } from "maplibre-gl";
import Map from "react-map-gl/maplibre";

const NOIDA_SECTOR_62_CENTER = { longitude: 77.391, latitude: 28.6139 };

const FREE_RASTER_STYLE: StyleSpecification = {
  version: 8,
  sources: {
    osm: {
      type: "raster",
      tiles: ["https://tile.openstreetmap.org/{z}/{x}/{y}.png"],
      tileSize: 256,
      attribution: "(c) OpenStreetMap contributors"
    }
  },
  layers: [
    {
      id: "osm",
      type: "raster",
      source: "osm"
    }
  ]
};

export default function MapLibreBaseMap({ children }: { children?: React.ReactNode }) {
  const [isMapReady, setIsMapReady] = useState(false);

  return (
    <Map
      initialViewState={{
        ...NOIDA_SECTOR_62_CENTER,
        zoom: 16
      }}
      mapStyle={FREE_RASTER_STYLE}
      style={{ width: "100%", height: "100%" }}
      attributionControl
      aria-label="Interactive map centered on Noida Sector 62"
      onLoad={(event) => {
        event.target.resize();
        setIsMapReady(true);
      }}
    >
      {isMapReady ? children : null}
    </Map>
  );
}
