import type { City, LayoutOption, RegulationDocument, SliderValues } from "@/store/useVinyasGenStore";

const API_BASE_URL = process.env.NEXT_PUBLIC_API_BASE_URL ?? "http://127.0.0.1:8000";

export async function getHealth() {
  return apiFetch<{ status: "ok"; version: string; timestamp: string; disclaimer: string }>("/api/health");
}

export async function getRegulations(city: City, zoneCode: string) {
  return apiFetch<RegulationDocument>(`/api/regulations/${city}/${zoneCode}`);
}

async function apiFetch<T>(path: string, init?: RequestInit): Promise<T> {
  const response = await fetch(`${API_BASE_URL}${path}`, {
    cache: "no-store",
    ...init,
    headers: {
      "Content-Type": "application/json",
      ...init?.headers
    }
  });

  if (!response.ok) {
    const message = await response.text();
    throw new Error(message || `Request failed with ${response.status}`);
  }

  return response.json() as Promise<T>;
}

export async function generateLayout(
  plotGeojson: GeoJSON.Feature,
  city: City,
  zoneCode: string,
  siteType: string,
  sliderValues?: SliderValues
) {
  return apiFetch<{ project_id: string; layout_options: LayoutOption[] }>("/api/layout/generate", {
    method: "POST",
    body: JSON.stringify({
      plot_geojson: plotGeojson,
      city,
      zone_code: zoneCode,
      site_type: siteType,
      slider_values: sliderValues
    })
  });
}

export async function updateLayout(
  plotGeojson: GeoJSON.Feature,
  city: City,
  zoneCode: string,
  siteType: string,
  sliderValues: SliderValues,
  objectiveProfileKey?: string
) {
  return apiFetch<LayoutOption>("/api/layout/update", {
    method: "POST",
    body: JSON.stringify({
      plot_geojson: plotGeojson,
      city,
      zone_code: zoneCode,
      site_type: siteType,
      slider_values: sliderValues,
      objective_profile_key: objectiveProfileKey
    })
  });
}

export async function sendCopilotMessage(message: string) {
  const response = await fetch(`${API_BASE_URL}/api/copilot/message`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ message })
  });

  if (!response.ok) {
    throw new Error("Copilot request failed");
  }

  return response.json();
}

export async function generateReport(layoutOption: LayoutOption) {
  return apiFetch<{ report_id: string; download_url: string }>("/api/report/generate", {
    method: "POST",
    body: JSON.stringify({ layout_option: layoutOption, acknowledge_emergency_override: true })
  });
}

export async function generatePdfReport(layoutOption: LayoutOption) {
  const response = await fetch(`${API_BASE_URL}/api/report/pdf`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ layout_option: layoutOption })
  });

  if (!response.ok) {
    throw new Error("PDF generation failed");
  }

  return response.json();
}

export async function exportDxf(layoutOption: LayoutOption) {
  const response = await fetch(`${API_BASE_URL}/api/export/dxf`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ layout_option: layoutOption })
  });

  if (!response.ok) {
    throw new Error("DXF export failed");
  }

  return response.text();
}

export async function submitVote(reportId: string, voteType: "support" | "concern" | "needs_changes", comment = "") {
  const response = await fetch(`${API_BASE_URL}/api/community/vote`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ report_id: reportId, vote_type: voteType, comment })
  });

  if (!response.ok) {
    throw new Error("Vote failed");
  }

  return response.json();
}

export async function getVotes(reportId: string) {
  const response = await fetch(`${API_BASE_URL}/api/community/${reportId}/votes`, { cache: "no-store" });
  if (!response.ok) {
    throw new Error("Vote summary failed");
  }
  return response.json();
}
