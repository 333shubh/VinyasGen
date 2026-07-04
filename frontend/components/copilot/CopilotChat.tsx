"use client";

import { useState } from "react";

import { generateLayout, sendCopilotMessage } from "@/lib/apiClient";
import { useVinyasGenStore } from "@/store/useVinyasGenStore";

export default function CopilotChat() {
  const [message, setMessage] = useState("");
  const drawnFeature = useVinyasGenStore((state) => state.drawnFeature);
  const sliderValues = useVinyasGenStore((state) => state.sliderValues);
  const setSliderValues = useVinyasGenStore((state) => state.setSliderValues);
  const setLayoutOptions = useVinyasGenStore((state) => state.setLayoutOptions);
  const copilotReply = useVinyasGenStore((state) => state.copilotReply);
  const setCopilotReply = useVinyasGenStore((state) => state.setCopilotReply);

  const submit = async () => {
    if (!message.trim()) {
      return;
    }
    const response = await sendCopilotMessage(message);
    setCopilotReply(response.reply_text);
    const payload = response.suggested_action?.payload;
    if (payload && drawnFeature) {
      const nextValues = { ...sliderValues, ...payload };
      setSliderValues(payload);
      const layoutResponse = await generateLayout(drawnFeature, nextValues);
      setLayoutOptions(layoutResponse.layout_options);
    }
    setMessage("");
  };

  return (
    <section aria-label="Copilot">
      <h2 className="text-lg font-semibold text-ink">Copilot</h2>
      <div className="mt-2 flex gap-2">
        <input
          className="min-w-0 flex-1 rounded-md border border-slate-300 px-3 py-2 text-sm"
          value={message}
          onChange={(event) => setMessage(event.target.value)}
          placeholder="Ask for more green or parking"
          aria-label="Copilot message"
        />
        <button
          type="button"
          className="rounded-md bg-leaf px-3 py-2 text-sm font-semibold text-white"
          onClick={submit}
        >
          Send
        </button>
      </div>
      {copilotReply ? <p className="mt-2 text-sm leading-6 text-slate-700">{copilotReply}</p> : null}
    </section>
  );
}
