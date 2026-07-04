import type { LayoutOption } from "@/store/useVinyasGenStore";

const statusCopy = {
  valid: "Compliant",
  warning: "Needs review",
  violation: "Has issues"
};

export default function ComplianceStatus({ layout }: { layout?: LayoutOption }) {
  if (!layout) {
    return (
      <section className="rounded-md border border-amber-300 bg-amber-50 p-4 text-amber-950">
        <p className="text-sm font-semibold">Status: Draw and generate</p>
        <p className="mt-1 text-sm leading-6">Compliance checks appear after layouts are generated.</p>
      </section>
    );
  }

  const status = layout.compliance_summary.status;
  const statusClass =
    status === "valid"
      ? "border-green-300 bg-green-50 text-green-950"
      : status === "violation"
        ? "border-red-300 bg-red-50 text-red-950"
        : "border-amber-300 bg-amber-50 text-amber-950";

  return (
    <section className={`rounded-md border p-4 ${statusClass}`} aria-label="Compliance status">
      <p className="text-sm font-semibold">Status: {statusCopy[status]}</p>
      <div className="mt-2 space-y-3">
        {layout.compliance_summary.checks?.map((check) => (
          <div key={check.check} className="text-sm leading-6">
            <p>
              <span className="font-semibold">{check.check}:</span> {check.detail}
            </p>
            {check.source_citation ? (
              <p className="mt-1 text-xs opacity-80">Citation: {check.source_citation}</p>
            ) : null}
          </div>
        ))}
      </div>
    </section>
  );
}
