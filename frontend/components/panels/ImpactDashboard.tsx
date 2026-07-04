import type { LayoutOption } from "@/store/useVinyasGenStore";

export default function ImpactDashboard({ layout }: { layout?: LayoutOption }) {
  if (!layout) {
    return null;
  }

  const metrics = [
    ["Site Area", `${layout.metrics.site_area_sqm} sqm`],
    ["Green Cover", `${layout.metrics.green_cover_pct}%`],
    ["Parking", `${layout.metrics.parking_spaces} spaces`],
    ["Trees", `${layout.metrics.tree_count}`],
    ["Score", `${layout.metrics.livability_score}/100`],
    ["Cost", `Rs ${layout.metrics.estimated_cost_lakh} lakh`]
  ];

  return (
    <section aria-label="Impact dashboard" className="grid grid-cols-2 gap-3">
      {metrics.map(([label, value]) => (
        <div key={label} className="rounded-md border border-slate-200 bg-mist p-3">
          <p className="text-xs font-medium text-slate-600">{label}</p>
          <p className="mt-1 text-lg font-semibold text-ink">{value}</p>
        </div>
      ))}
    </section>
  );
}
