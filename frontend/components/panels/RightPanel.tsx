"use client";

import { useVinyasGenStore } from "@/store/useVinyasGenStore";

export default function RightPanel() {
  const regulation = useVinyasGenStore((state) => state.regulation);
  const regulationStatus = useVinyasGenStore((state) => state.regulationStatus);

  return (
    <aside
      className="pointer-events-auto w-full max-w-sm rounded-md border border-slate-200 bg-white/95 p-5 shadow-sm"
      aria-label="Regulation constraints"
    >
      <h2 className="text-xl font-semibold text-ink">Regulation constraints</h2>
      <p className="mt-2 text-sm leading-6 text-slate-700" role="status" aria-live="polite">
        {regulationStatus}
      </p>

      {regulation ? (
        <section className="mt-4 space-y-3" aria-label="Five key constraints">
          <Constraint label="Authority" value={regulation.authority} />
          <Constraint label="FAR" value={String(regulation.constraints.max_far)} />
          <Constraint
            label="Setbacks"
            value={`${regulation.constraints.min_setback_front_m}m front, ${regulation.constraints.min_setback_side_m}m side, ${regulation.constraints.min_setback_rear_m}m rear`}
          />
          <Constraint
            label="Parking Norms"
            value={Object.entries(regulation.constraints.parking_norms)
              .map(([key, value]) => `${formatKey(key)}: ${value}`)
              .join(", ")}
          />
          <Constraint
            label="Green Area"
            value={`${Math.round(regulation.constraints.min_green_area_pct * 100)}% minimum`}
          />
          <Constraint label="Max Height" value={`${regulation.constraints.max_building_height_m}m`} />
          <div className="rounded-md border border-amber-200 bg-amber-50 p-3 text-sm text-amber-950">
            <p className="font-semibold">Review status: {regulation.review_status}</p>
            <p className="mt-1 leading-6">{regulation.source_document}</p>
          </div>
        </section>
      ) : null}
    </aside>
  );
}

function Constraint({ label, value }: { label: string; value: string }) {
  return (
    <div className="rounded-md border border-slate-200 p-3">
      <p className="text-xs font-semibold uppercase tracking-normal text-slate-500">{label}</p>
      <p className="mt-1 text-sm font-semibold leading-6 text-ink">{value}</p>
    </div>
  );
}

function formatKey(key: string) {
  return key.replaceAll("_", " ");
}
