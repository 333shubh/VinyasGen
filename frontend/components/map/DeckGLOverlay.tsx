"use client";

import { Layer, Source } from "react-map-gl/maplibre";

import { useVinyasGenStore } from "@/store/useVinyasGenStore";

export default function DeckGLOverlay() {
  const layoutOptions = useVinyasGenStore((state) => state.layoutOptions);
  const activeLayoutId = useVinyasGenStore((state) => state.activeLayoutId);
  const drawnFeature = useVinyasGenStore((state) => state.drawnFeature);
  const showProposal = useVinyasGenStore((state) => state.showProposal);
  const activeLayout = layoutOptions.find((layout) => layout.layout_id === activeLayoutId);

  if (!showProposal && drawnFeature) {
    return (
      <Source id="before-boundary" type="geojson" data={drawnFeature}>
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
    <Source id="active-layout" type="geojson" data={activeLayout.geojson}>
      <Layer
        id="active-layout-fill"
        type="fill"
        paint={{
          "fill-color": ["get", "fill"],
          "fill-opacity": 0.46
        }}
      />
      <Layer
        id="active-layout-line"
        type="line"
        paint={{
          "line-color": "#17201b",
          "line-width": 2,
          "line-opacity": 0.7
        }}
      />
      <Layer
        id="active-layout-tree-points"
        type="circle"
        filter={["==", ["get", "zone"], "tree"]}
        paint={{
          "circle-color": "#166534",
          "circle-radius": 5,
          "circle-stroke-color": "#ffffff",
          "circle-stroke-width": 1
        }}
      />
    </Source>
  );
}
