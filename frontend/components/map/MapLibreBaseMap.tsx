"use client";

import Map from "react-map-gl/maplibre";

const NOIDA_SECTOR_62_CENTER = { longitude: 77.391, latitude: 28.6139 };
const FREE_MAP_STYLE_URL = "https://demotiles.maplibre.org/style.json";

export default function MapLibreBaseMap({ children }: { children?: React.ReactNode }) {
  return (
    <Map
      initialViewState={{
        ...NOIDA_SECTOR_62_CENTER,
        zoom: 16
      }}
      mapStyle={FREE_MAP_STYLE_URL}
      style={{ width: "100%", height: "100%" }}
      attributionControl
      aria-label="Interactive map centered on Noida Sector 62"
    >
      {children}
    </Map>
  );
}
