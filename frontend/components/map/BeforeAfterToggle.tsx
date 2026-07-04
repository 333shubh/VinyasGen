"use client";

import { useVinyasGenStore } from "@/store/useVinyasGenStore";

export default function BeforeAfterToggle() {
  const showProposal = useVinyasGenStore((state) => state.showProposal);
  const setShowProposal = useVinyasGenStore((state) => state.setShowProposal);

  return (
    <div className="pointer-events-auto rounded-md border border-slate-200 bg-white/95 p-2 shadow-sm">
      <div className="flex gap-2" role="group" aria-label="Before and after map view">
        <button
          type="button"
          className={`rounded-md px-3 py-2 text-sm font-semibold ${!showProposal ? "bg-ink text-white" : "bg-mist text-ink"}`}
          onClick={() => setShowProposal(false)}
        >
          Before
        </button>
        <button
          type="button"
          className={`rounded-md px-3 py-2 text-sm font-semibold ${showProposal ? "bg-ink text-white" : "bg-mist text-ink"}`}
          onClick={() => setShowProposal(true)}
        >
          After
        </button>
      </div>
    </div>
  );
}
