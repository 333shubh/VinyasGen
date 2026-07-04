"use client";

import { useVinyasGenStore } from "@/store/useVinyasGenStore";

export default function LayoutOptionsCarousel() {
  const layoutOptions = useVinyasGenStore((state) => state.layoutOptions);
  const activeLayoutId = useVinyasGenStore((state) => state.activeLayoutId);
  const setActiveLayoutId = useVinyasGenStore((state) => state.setActiveLayoutId);

  if (!layoutOptions.length) {
    return (
      <p className="rounded-md border border-slate-200 bg-mist p-4 text-sm text-slate-700">
        Draw an area to see layout options.
      </p>
    );
  }

  return (
    <section aria-label="Layout options">
      <h2 className="text-lg font-semibold text-ink">Layout options</h2>
      <div className="mt-3 grid gap-2">
        {layoutOptions.map((layout) => (
          <button
            key={layout.layout_id}
            type="button"
            className={`rounded-md border p-3 text-left transition duration-200 ${
              activeLayoutId === layout.layout_id
                ? "border-leaf bg-green-50"
                : "border-slate-200 bg-white hover:bg-mist"
            }`}
            onClick={() => setActiveLayoutId(layout.layout_id)}
          >
            <span className="block text-sm font-semibold text-ink">{layout.objective_profile}</span>
            <span className="mt-1 block text-sm text-slate-700">
              Green Cover {layout.metrics.green_cover_pct}% · Parking {layout.metrics.parking_spaces}
            </span>
          </button>
        ))}
      </div>
    </section>
  );
}
