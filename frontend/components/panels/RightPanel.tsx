"use client";

import { generateReport } from "@/lib/apiClient";
import { useVinyasGenStore } from "@/store/useVinyasGenStore";
import ComplianceStatus from "./ComplianceStatus";
import ImpactDashboard from "./ImpactDashboard";

export default function RightPanel() {
  const layoutOptions = useVinyasGenStore((state) => state.layoutOptions);
  const activeLayoutId = useVinyasGenStore((state) => state.activeLayoutId);
  const regulation = useVinyasGenStore((state) => state.regulation);
  const regulationStatus = useVinyasGenStore((state) => state.regulationStatus);
  const reportId = useVinyasGenStore((state) => state.reportId);
  const setReportId = useVinyasGenStore((state) => state.setReportId);
  const setBackendStatus = useVinyasGenStore((state) => state.setBackendStatus);
  const activeLayout = layoutOptions.find((layout) => layout.layout_id === activeLayoutId);

  const handleReport = async () => {
    if (!activeLayout) return;
    setBackendStatus("Generating report");
    try {
      const result = await generateReport(activeLayout);
      setReportId(result.report_id);
      setBackendStatus("Report ready");
      window.open(`http://127.0.0.1:8000${result.download_url}`, "_blank", "noopener,noreferrer");
    } catch (error) {
      setBackendStatus(error instanceof Error ? error.message : "Report generation failed");
    }
  };

  return (
    <aside
      className="pointer-events-auto max-h-[calc(100vh-7rem)] w-full max-w-sm overflow-auto rounded-md border border-slate-200 bg-white/95 p-5 shadow-sm"
      aria-label="Layout analysis"
    >
      <h2 className="text-xl font-semibold text-ink">Layout analysis</h2>
      <p className="mt-2 text-sm leading-6 text-slate-700" role="status" aria-live="polite">
        {activeLayout ? activeLayout.objective_profile : regulationStatus}
      </p>

      {!activeLayout && regulation ? (
        <section className="mt-4 space-y-3" aria-label="Regulation summary">
          <Constraint label="Authority" value={regulation.authority} />
          <Constraint label="FAR" value={String(regulation.constraints.max_far)} />
          <Constraint
            label="Green Area"
            value={`${Math.round(regulation.constraints.min_green_area_pct * 100)}% minimum`}
          />
          <Constraint label="Max Height" value={`${regulation.constraints.max_building_height_m}m`} />
        </section>
      ) : null}

      <div className="mt-4">
        <ComplianceStatus layout={activeLayout} />
      </div>

      <div className="mt-4">
        <ImpactDashboard layout={activeLayout} />
      </div>

      {activeLayout?.emergency_access ? (
        <section
          className={`mt-4 rounded-md border p-3 text-sm ${
            activeLayout.emergency_access.overall_status === "PASS"
              ? "border-green-300 bg-green-50 text-green-950"
              : "border-red-300 bg-red-50 text-red-950"
          }`}
          aria-label="Emergency access result"
        >
          <p className="font-semibold">Emergency access: {activeLayout.emergency_access.overall_status}</p>
          {activeLayout.emergency_access.violations.map((violation) => (
            <p key={`${violation.type}-${violation.detail}`} className="mt-1 leading-6">
              {violation.detail}
            </p>
          ))}
        </section>
      ) : null}

      <button
        type="button"
        disabled={!activeLayout}
        className="mt-4 w-full rounded-md bg-ink px-4 py-3 text-sm font-semibold text-white transition duration-200 disabled:cursor-not-allowed disabled:bg-slate-400"
        onClick={handleReport}
      >
        Generate PDF Report
      </button>

      {reportId ? (
        <p className="mt-3 rounded-md border border-slate-200 bg-mist p-3 text-sm text-slate-700">
          Latest report: {reportId}
        </p>
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
