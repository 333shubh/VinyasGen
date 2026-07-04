"use client";

import { useEffect, useRef } from "react";

import { updateLayout } from "@/lib/apiClient";
import { useVinyasGenStore } from "@/store/useVinyasGenStore";

const sliders = [
  { key: "density_level", label: "Parking Density", min: 0.1, max: 0.9, step: 0.05 },
  { key: "greenery_pct", label: "Green Cover", min: 0.05, max: 0.4, step: 0.05 },
  { key: "pedestrian_priority", label: "Pedestrian Priority", min: 0.05, max: 0.9, step: 0.05 }
] as const;

export default function ConstraintSliders() {
  const officialBoundary = useVinyasGenStore((state) => state.officialBoundary);
  const city = useVinyasGenStore((state) => state.city);
  const zoneCode = useVinyasGenStore((state) => state.zoneCode);
  const siteType = useVinyasGenStore((state) => state.siteType);
  const sliderValues = useVinyasGenStore((state) => state.sliderValues);
  const setSliderValues = useVinyasGenStore((state) => state.setSliderValues);
  const layoutOptions = useVinyasGenStore((state) => state.layoutOptions);
  const activeLayoutId = useVinyasGenStore((state) => state.activeLayoutId);
  const setLayoutOptions = useVinyasGenStore((state) => state.setLayoutOptions);
  const setBackendStatus = useVinyasGenStore((state) => state.setBackendStatus);
  const debounceRef = useRef<ReturnType<typeof setTimeout> | null>(null);

  useEffect(() => () => {
    if (debounceRef.current) clearTimeout(debounceRef.current);
  }, []);

  const scheduleUpdate = (values = sliderValues) => {
    if (!officialBoundary || !layoutOptions.length) return;
    if (debounceRef.current) clearTimeout(debounceRef.current);
    debounceRef.current = setTimeout(async () => {
      setBackendStatus("Updating layout");
      const objectiveKey = activeLayoutId?.replace("layout_", "");
      const updated = await updateLayout(officialBoundary, city, zoneCode, siteType ?? "gali", values, objectiveKey);
      setLayoutOptions(layoutOptions.map((layout) => (layout.layout_id === activeLayoutId ? updated : layout)));
      setBackendStatus("Layouts ready");
    }, 150);
  };

  return (
    <section aria-label="Layout priorities">
      <h2 className="text-lg font-semibold text-ink">Layout priorities</h2>
      <div className="mt-3 space-y-4">
        {sliders.map((slider) => (
          <label key={slider.key} className="block">
            <span className="flex items-center justify-between text-sm font-medium text-slate-700">
              {slider.label}
              <span>{Math.round(sliderValues[slider.key] * 100)}%</span>
            </span>
            <input
              className="mt-2 w-full accent-leaf"
              type="range"
              min={slider.min}
              max={slider.max}
              step={slider.step}
              value={sliderValues[slider.key]}
              aria-label={slider.label}
              disabled={!layoutOptions.length}
              onChange={(event) => {
                const value = Number(event.target.value);
                const nextValues = { ...sliderValues, [slider.key]: value };
                setSliderValues({ [slider.key]: value });
                scheduleUpdate(nextValues);
              }}
            />
          </label>
        ))}
      </div>
    </section>
  );
}
