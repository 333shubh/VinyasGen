"use client";

import { useRef } from "react";
import { useControl } from "react-map-gl/maplibre";
import MaplibreDraw from "maplibre-gl-draw";

type DrawControlProps = {
  onPolygonReady: (feature: GeoJSON.Feature) => void;
};

export default function DrawControl({ onPolygonReady }: DrawControlProps) {
  const drawRef = useRef<MaplibreDraw | null>(null);
  const handlerRef = useRef<(() => void) | null>(null);

  useControl<MaplibreDraw>(
    () => {
      const draw = new MaplibreDraw({
        displayControlsDefault: false,
        controls: {
          polygon: true,
          trash: true
        }
      });
      drawRef.current = draw;
      return draw;
    },
    ({ map }) => {
      const handleChange = () => {
        const feature = drawRef.current?.getAll().features[0];
        if (feature) {
          console.info("VinyasGen drawn GeoJSON", feature);
          onPolygonReady(feature);
        }
      };

      handlerRef.current = handleChange;
      map.on("draw.create", handleChange);
      map.on("draw.update", handleChange);
    },
    ({ map }) => {
      if (handlerRef.current) {
        map.off("draw.create", handlerRef.current);
        map.off("draw.update", handlerRef.current);
      }
    },
    {
      position: "top-left"
    }
  );

  return null;
}
