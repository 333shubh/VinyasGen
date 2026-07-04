"use client";

import { generateLayout } from "@/lib/apiClient";
import type { City, SiteType } from "@/store/useVinyasGenStore";
import { useVinyasGenStore } from "@/store/useVinyasGenStore";
import ConstraintSliders from "./ConstraintSliders";
import LayoutOptionsCarousel from "./LayoutOptionsCarousel";

const ZONES_BY_CITY: Record<City, Array<{ label: string; value: string }>> = {
  noida: [{ label: "Residential Group Housing", value: "residential_group_housing" }],
  delhi: [{ label: "Residential Colony", value: "residential_colony" }],
  gurgaon: [{ label: "Group Housing", value: "group_housing" }]
};

const SITE_TYPES: Array<{ label: string; value: SiteType }> = [
  { label: "Gali / Lane", value: "gali" },
  { label: "Road Corridor", value: "road" },
  { label: "Empty Plot", value: "empty_plot" },
  { label: "Public Space", value: "public_space" }
];

export default function LeftPanel() {
  const backendStatus = useVinyasGenStore((state) => state.backendStatus);
  const city = useVinyasGenStore((state) => state.city);
  const zoneCode = useVinyasGenStore((state) => state.zoneCode);
  const siteType = useVinyasGenStore((state) => state.siteType);
  const officialBoundary = useVinyasGenStore((state) => state.officialBoundary);
  const sliderValues = useVinyasGenStore((state) => state.sliderValues);
  const isGeneratingLayouts = useVinyasGenStore((state) => state.isGeneratingLayouts);
  const setCity = useVinyasGenStore((state) => state.setCity);
  const setZoneCode = useVinyasGenStore((state) => state.setZoneCode);
  const setSiteType = useVinyasGenStore((state) => state.setSiteType);
  const setLayoutOptions = useVinyasGenStore((state) => state.setLayoutOptions);
  const setBackendStatus = useVinyasGenStore((state) => state.setBackendStatus);
  const setIsGeneratingLayouts = useVinyasGenStore((state) => state.setIsGeneratingLayouts);

  const zoneOptions = ZONES_BY_CITY[city];

  const handleGenerate = async () => {
    if (!officialBoundary) return;
    setIsGeneratingLayouts(true);
    setBackendStatus("Generating layouts");
    try {
      const response = await generateLayout(officialBoundary, city, zoneCode, siteType ?? "gali", sliderValues);
      setLayoutOptions(response.layout_options);
      setBackendStatus("Layouts ready");
    } catch (error) {
      setBackendStatus(error instanceof Error ? error.message : "Layout generation failed");
    } finally {
      setIsGeneratingLayouts(false);
    }
  };

  return (
    <aside
      className="pointer-events-auto max-h-[calc(100vh-7rem)] w-full max-w-sm overflow-auto rounded-md border border-slate-200 bg-white/95 p-5 shadow-sm"
      aria-label="Project setup"
    >
      <p className="text-sm font-semibold uppercase tracking-normal text-leaf">VinyasGen</p>
      <h1 className="mt-2 text-2xl font-semibold text-ink">Regenerate the street layout</h1>
      <p className="mt-3 text-base leading-7 text-slate-700">
        Draw the official boundary, choose the planning context, then generate five deterministic layout options.
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

        <label className="block">
          <span className="text-sm font-semibold text-ink">Site Type</span>
          <select
            className="mt-2 w-full rounded-md border border-slate-300 bg-white px-3 py-2 text-sm text-ink"
            value={siteType ?? "gali"}
            onChange={(event) => setSiteType(event.target.value as SiteType)}
          >
            {SITE_TYPES.map((type) => (
              <option key={type.value} value={type.value}>
                {type.label}
              </option>
            ))}
          </select>
        </label>
      </div>

      <section className="mt-5 rounded-md border border-slate-200 p-4" aria-label="Boundary status">
        <h2 className="text-base font-semibold text-ink">Boundary</h2>
        <p className="mt-2 text-sm leading-6 text-slate-700">
          {officialBoundary
            ? "Official boundary captured. Generate layouts when ready."
            : "Use the polygon tool on the map to draw the official boundary."}
        </p>
      </section>

      <button
        type="button"
        disabled={!officialBoundary || isGeneratingLayouts}
        className="mt-5 w-full rounded-md bg-ink px-4 py-3 text-sm font-semibold text-white transition duration-200 disabled:cursor-not-allowed disabled:bg-slate-400"
        onClick={handleGenerate}
      >
        {isGeneratingLayouts ? "Generating layouts" : "Generate Layouts"}
      </button>

      {isGeneratingLayouts ? (
        <div className="mt-5 space-y-2" aria-label="Layout loading state">
          {[0, 1, 2].map((item) => (
            <div key={item} className="h-16 animate-pulse rounded-md bg-slate-100" />
          ))}
        </div>
      ) : null}

      <div className="mt-5">
        <ConstraintSliders />
      </div>

      <div className="mt-5">
        <LayoutOptionsCarousel />
      </div>
    </aside>
  );
}
