"use client";

import { useVinyasGenStore } from "@/store/useVinyasGenStore";

export default function DisclaimerBanner() {
  const disclaimer = useVinyasGenStore((state) => state.disclaimer);

  return (
    <footer className="fixed inset-x-0 bottom-0 z-20 border-t border-slate-200 bg-white/95 px-4 py-3 text-sm text-slate-800 shadow-sm">
      <p className="mx-auto max-w-6xl leading-6">{disclaimer}</p>
    </footer>
  );
}
