"use client";

import { useMemo, useRef } from "react";
import { useControl } from "react-map-gl/maplibre";
import MaplibreDraw from "maplibre-gl-draw";

type DrawControlProps = {
  onPolygonReady: (feature: GeoJSON.Feature) => void;
};

export default function DrawControl({ onPolygonReady }: DrawControlProps) {
  const draw = useMemo(
    () =>
      new MaplibreDraw({
        displayControlsDefault: false,
        controls: {
          polygon: true,
          trash: true
        }
      }),
    []
  );
  const drawRef = useRef<MaplibreDraw | null>(null);
  const handlerRef = useRef<(() => void) | null>(null);

  useControl<MaplibreDraw>(
    () => draw,
    ({ map }) => {
      drawRef.current = draw;

      const handleChange = () => {
        const activeDraw = drawRef.current;
        if (!activeDraw || typeof activeDraw.getAll !== "function") {
          return;
        }

        const polygons = activeDraw
          .getAll()
          .features.filter((feature) => feature.geometry?.type === "Polygon");
        const feature = polygons.at(-1);
        if (feature) {
          console.info("VinyasGen drawn GeoJSON", feature);
          onPolygonReady(feature);
        }
      };

      handlerRef.current = handleChange;
      map.on("draw.create", handleChange);
      map.on("draw.update", handleChange);
      map.on("draw.delete", handleChange);
    },
    ({ map }) => {
      if (handlerRef.current) {
        map.off("draw.create", handlerRef.current);
        map.off("draw.update", handlerRef.current);
        map.off("draw.delete", handlerRef.current);
      }
      handlerRef.current = null;
      drawRef.current = null;
    },
    {
      position: "top-left"
    }
  );

  return null;
}
