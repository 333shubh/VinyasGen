"use client";

import type { City } from "@/store/useVinyasGenStore";
import { useVinyasGenStore } from "@/store/useVinyasGenStore";

const ZONES_BY_CITY: Record<City, Array<{ label: string; value: string }>> = {
  noida: [{ label: "Residential Group Housing", value: "residential_group_housing" }],
  delhi: [{ label: "Residential Colony", value: "residential_colony" }],
  gurgaon: [{ label: "Group Housing", value: "group_housing" }]
};

export default function LeftPanel() {
  const backendStatus = useVinyasGenStore((state) => state.backendStatus);
  const city = useVinyasGenStore((state) => state.city);
  const zoneCode = useVinyasGenStore((state) => state.zoneCode);
  const officialBoundary = useVinyasGenStore((state) => state.officialBoundary);
  const setCity = useVinyasGenStore((state) => state.setCity);
  const setZoneCode = useVinyasGenStore((state) => state.setZoneCode);

  const zoneOptions = ZONES_BY_CITY[city];

  return (
    <aside
      className="pointer-events-auto w-full max-w-sm rounded-md border border-slate-200 bg-white/95 p-5 shadow-sm"
      aria-label="Project setup"
    >
      <p className="text-sm font-semibold uppercase tracking-normal text-leaf">VinyasGen</p>
      <h1 className="mt-2 text-2xl font-semibold text-ink">Define the site boundary</h1>
      <p className="mt-3 text-base leading-7 text-slate-700">
        Draw a road, gali, public plot, or open space on the map. The drawn polygon becomes
        the official boundary used by later analysis.
      </p>

      <div className="mt-5 rounded-md border border-slate-200 bg-mist p-4" role="status" aria-live="polite">
        <p className="text-sm font-medium text-slate-600">Backend</p>
        <p className="mt-1 text-lg font-semibold text-ink">
          {backendStatus === "Connected" ? "Backend: OK" : backendStatus}
        </p>
      </div>

      <div className="mt-5 space-y-4">
        <label className="block">
          <span className="text-sm font-semibold text-ink">City</span>
          <select
            className="mt-2 w-full rounded-md border border-slate-300 bg-white px-3 py-2 text-sm text-ink"
            value={city}
            onChange={(event) => {
              const nextCity = event.target.value as City;
              setCity(nextCity);
              setZoneCode(ZONES_BY_CITY[nextCity][0].value);
            }}
          >
            <option value="noida">Noida</option>
            <option value="delhi">Delhi</option>
            <option value="gurgaon">Gurgaon</option>
          </select>
        </label>

        <label className="block">
          <span className="text-sm font-semibold text-ink">Zone Type</span>
          <select
            className="mt-2 w-full rounded-md border border-slate-300 bg-white px-3 py-2 text-sm text-ink"
            value={zoneCode}
            onChange={(event) => setZoneCode(event.target.value)}
          >
            {zoneOptions.map((zone) => (
              <option key={zone.value} value={zone.value}>
                {zone.label}
              </option>
            ))}
          </select>
        </label>
      </div>

      <section className="mt-5 rounded-md border border-slate-200 p-4" aria-label="Boundary status">
        <h2 className="text-base font-semibold text-ink">Boundary</h2>
        <p className="mt-2 text-sm leading-6 text-slate-700">
          {officialBoundary
            ? "Official boundary captured. GeoJSON has been logged to the browser console."
            : "Use the polygon tool on the map to draw the official boundary."}
        </p>
      </section>
    </aside>
  );
}
