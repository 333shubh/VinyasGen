import type { LayoutOption } from "@/store/useVinyasGenStore";

export default function ImpactDashboard({ layout }: { layout?: LayoutOption }) {
  if (!layout) {
    return null;
  }

  const metrics = [
    ["Parking", `${layout.metrics.parking_spaces} bays`],
    ["Green Cover", `${layout.metrics.green_cover_pct}%`],
    ["Walkable Path", `${layout.metrics.walkable_path_m ?? 0} m`],
    ["Thermal Score", `${layout.metrics.thermal_score_delta_c ?? 0} C`],
    ["Drainage", `${layout.metrics.drainage_capacity_mm_hr ?? 0} mm/hr`],
    ["Compliance", layout.compliance_summary.status],
    ["Cost", `Rs ${layout.metrics.estimated_cost_lakh} lakh`],
    ["Emergency", layout.emergency_access?.overall_status ?? "FAIL"]
  ];

  return (
    <section aria-label="Impact dashboard" className="grid grid-cols-2 gap-3">
      {metrics.map(([label, value]) => (
        <div key={label} className="rounded-md border border-slate-200 bg-mist p-3">
          <p className="text-xs font-medium text-slate-600">{label}</p>
          <p className="mt-1 text-base font-semibold text-ink">{value}</p>
        </div>
      ))}
    </section>
  );
}
