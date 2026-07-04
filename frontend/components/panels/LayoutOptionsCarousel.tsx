"use client";

import { useVinyasGenStore } from "@/store/useVinyasGenStore";

export default function LayoutOptionsCarousel() {
  const layoutOptions = useVinyasGenStore((state) => state.layoutOptions);
  const activeLayoutId = useVinyasGenStore((state) => state.activeLayoutId);
  const setActiveLayoutId = useVinyasGenStore((state) => state.setActiveLayoutId);

  if (!layoutOptions.length) {
    return (
      <p className="rounded-md border border-slate-200 bg-mist p-4 text-sm text-slate-700">
        Generate layouts to compare five options.
      </p>
    );
  }

  return (
    <section aria-label="Layout options">
      <h2 className="text-lg font-semibold text-ink">Layout options</h2>
      <div className="mt-3 grid gap-2">
        {layoutOptions.map((layout) => {
          const active = activeLayoutId === layout.layout_id;
          const accessStatus = layout.emergency_access?.overall_status ?? layout.metrics.emergency_access ?? "FAIL";
          return (
            <button
              key={layout.layout_id}
              type="button"
              className={`rounded-md border p-3 text-left transition duration-200 ${
                active ? "border-leaf bg-green-50" : "border-slate-200 bg-white hover:bg-mist"
              }`}
              onClick={() => setActiveLayoutId(layout.layout_id)}
            >
              <span className="block text-sm font-semibold text-ink">{layout.objective_profile}</span>
              <span className="mt-1 block text-sm text-slate-700">
                Green {layout.metrics.green_cover_pct}% | Parking {layout.metrics.parking_spaces} | Access {accessStatus}
              </span>
              <span className="mt-2 block h-2 overflow-hidden rounded-full bg-slate-100">
                <span
                  className="block h-full bg-leaf"
                  style={{ width: `${Math.min(100, layout.metrics.livability_score)}%` }}
                />
              </span>
            </button>
          );
        })}
      </div>
    </section>
  );
}
