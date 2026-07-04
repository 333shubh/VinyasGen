"use client";

import { Layer, Source } from "react-map-gl/maplibre";

import { useVinyasGenStore } from "@/store/useVinyasGenStore";

export default function DeckGLOverlay() {
  const layoutOptions = useVinyasGenStore((state) => state.layoutOptions);
  const activeLayoutId = useVinyasGenStore((state) => state.activeLayoutId);
  const officialBoundary = useVinyasGenStore((state) => state.officialBoundary);
  const showProposal = useVinyasGenStore((state) => state.showProposal);
  const activeLayout = layoutOptions.find((layout) => layout.layout_id === activeLayoutId);
  const accessPath = activeLayout?.emergency_access?.clear_path_geojson;

  if (!showProposal && officialBoundary) {
    return (
      <Source id="before-boundary" type="geojson" data={officialBoundary}>
        <Layer
          id="before-boundary-fill"
          type="fill"
          paint={{ "fill-color": "#17201b", "fill-opacity": 0.08 }}
        />
        <Layer
          id="before-boundary-line"
          type="line"
          paint={{ "line-color": "#17201b", "line-width": 3, "line-dasharray": [2, 2] }}
        />
      </Source>
    );
  }

  if (!activeLayout) {
    return null;
  }

  return (
    <>
      <Source id="active-layout" type="geojson" data={activeLayout.geojson}>
        <Layer
          id="active-layout-fill"
          type="fill"
          filter={["==", ["geometry-type"], "Polygon"]}
          paint={{
            "fill-color": ["coalesce", ["get", "fill"], ["get", "fill_color"], "#A8D5A2"],
            "fill-opacity": 0.5
          }}
        />
        <Layer
          id="active-layout-line"
          type="line"
          filter={["==", ["geometry-type"], "Polygon"]}
          paint={{
            "line-color": ["coalesce", ["get", "stroke"], ["get", "stroke_color"], "#17201b"],
            "line-width": 1.5,
            "line-opacity": 0.85
          }}
        />
        <Layer
          id="active-layout-points"
          type="circle"
          filter={["==", ["geometry-type"], "Point"]}
          paint={{
            "circle-color": ["coalesce", ["get", "fill"], "#166534"],
            "circle-radius": 4,
            "circle-stroke-color": "#ffffff",
            "circle-stroke-width": 1
          }}
        />
      </Source>

      {accessPath ? (
        <Source id="emergency-access-path" type="geojson" data={accessPath}>
          <Layer
            id="emergency-access-line"
            type="line"
            paint={{
              "line-color": activeLayout.emergency_access?.overall_status === "PASS" ? "#2E7D32" : "#E74C3C",
              "line-width": 5,
              "line-opacity": 0.85
            }}
          />
        </Source>
      ) : null}
    </>
  );
}
