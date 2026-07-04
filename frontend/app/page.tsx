"use client";

import { useEffect } from "react";

import DrawControl from "@/components/map/DrawControl";
import MapLibreBaseMap from "@/components/map/MapLibreBaseMap";
import DisclaimerBanner from "@/components/panels/DisclaimerBanner";
import LeftPanel from "@/components/panels/LeftPanel";
import RightPanel from "@/components/panels/RightPanel";
import DeckGLOverlay from "@/components/map/DeckGLOverlay";
import BeforeAfterToggle from "@/components/map/BeforeAfterToggle";
import { getHealth, getRegulations } from "@/lib/apiClient";
import { useVinyasGenStore } from "@/store/useVinyasGenStore";

export default function Home() {
  const setBackendStatus = useVinyasGenStore((state) => state.setBackendStatus);
  const setDisclaimer = useVinyasGenStore((state) => state.setDisclaimer);
  const setOfficialBoundary = useVinyasGenStore((state) => state.setOfficialBoundary);
  const city = useVinyasGenStore((state) => state.city);
  const zoneCode = useVinyasGenStore((state) => state.zoneCode);
  const setRegulation = useVinyasGenStore((state) => state.setRegulation);
  const setRegulationStatus = useVinyasGenStore((state) => state.setRegulationStatus);

  useEffect(() => {
    getHealth()
      .then((health) => {
        setBackendStatus("Connected");
        setDisclaimer(health.disclaimer);
      })
      .catch(() => setBackendStatus("Start backend on port 8000"));
  }, [setBackendStatus, setDisclaimer]);

  useEffect(() => {
    setRegulationStatus("Loading regulations");
    getRegulations(city, zoneCode)
      .then((regulation) => {
        setRegulation(regulation);
        setRegulationStatus(`${regulation.authority} constraints loaded`);
      })
      .catch(() => {
        setRegulation(null);
        setRegulationStatus("Could not load regulations");
      });
  }, [city, setRegulation, setRegulationStatus, zoneCode]);

  const handlePolygonReady = (feature: GeoJSON.Feature) => {
    console.info("VinyasGen official boundary GeoJSON", feature);
    setOfficialBoundary(feature);
  };

  return (
    <main className="relative h-screen overflow-hidden bg-mist pb-24 text-ink">
      <MapLibreBaseMap>
        <DrawControl onPolygonReady={handlePolygonReady} />
        <DeckGLOverlay />
      </MapLibreBaseMap>

      <div className="pointer-events-none absolute inset-0 z-10 grid gap-4 p-4 md:grid-cols-[minmax(280px,384px)_1fr_minmax(280px,360px)]">
        <div className="self-start">
          <LeftPanel />
        </div>
        <div aria-hidden="true" />
        <div className="self-start md:justify-self-end">
          <RightPanel />
        </div>
        <div className="self-end md:col-start-2 md:justify-self-center">
          <BeforeAfterToggle />
        </div>
      </div>

      <DisclaimerBanner />
    </main>
  );
}
