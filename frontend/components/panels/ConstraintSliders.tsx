"use client";

import { generateLayout } from "@/lib/apiClient";
import { useVinyasGenStore } from "@/store/useVinyasGenStore";

const sliders = [
  { key: "density_level", label: "Community Use", min: 0.1, max: 0.75, step: 0.05 },
  { key: "greenery_pct", label: "Green Cover", min: 0.08, max: 0.65, step: 0.05 },
  { key: "pedestrian_priority", label: "Walking Comfort", min: 0.05, max: 0.8, step: 0.05 }
] as const;

export default function ConstraintSliders() {
  const drawnFeature = useVinyasGenStore((state) => state.drawnFeature);
  const sliderValues = useVinyasGenStore((state) => state.sliderValues);
  const setSliderValues = useVinyasGenStore((state) => state.setSliderValues);
  const setLayoutOptions = useVinyasGenStore((state) => state.setLayoutOptions);
  const setBackendStatus = useVinyasGenStore((state) => state.setBackendStatus);

  const regenerate = async (values = sliderValues) => {
    if (!drawnFeature) {
      return;
    }
    setBackendStatus("Updating layouts");
    const response = await generateLayout(drawnFeature, values);
    setLayoutOptions(response.layout_options);
    setBackendStatus("Layouts ready");
  };

  return (
    <section aria-label="Layout priorities">
      <h2 className="text-lg font-semibold text-ink">Priorities</h2>
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
              onChange={(event) => {
                const nextValues = { ...sliderValues, [slider.key]: Number(event.target.value) };
                setSliderValues({ [slider.key]: Number(event.target.value) });
                void regenerate(nextValues);
              }}
            />
          </label>
        ))}
      </div>
    </section>
  );
}
