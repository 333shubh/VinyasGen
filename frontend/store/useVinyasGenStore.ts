import { create } from "zustand";

export type City = "noida" | "delhi" | "gurgaon";
export type SiteType = "road" | "gali" | "empty_plot" | "public_space";

export type RegulationConstraints = {
  max_far: number;
  max_ground_coverage_pct: number;
  min_setback_front_m: number;
  min_setback_side_m: number;
  min_setback_rear_m: number;
  max_building_height_m: number;
  min_green_area_pct: number;
  parking_norms: Record<string, number>;
  min_road_width_for_access_m?: number;
  fire_safety?: Record<string, number>;
};

export type RegulationDocument = {
  city: City;
  authority: string;
  zone_code: string;
  source_document: string;
  source_url?: string;
  last_verified?: string;
  last_updated?: string;
  review_status: "pending_review" | "verified" | string;
  constraints: RegulationConstraints;
  incentives?: Array<Record<string, unknown>>;
};

export type SliderValues = {
  density_level: number;
  greenery_pct: number;
  pedestrian_priority: number;
};

export type LayoutOption = {
  layout_id: string;
  objective_profile: string;
  geojson: GeoJSON.FeatureCollection;
  metrics: {
    site_area_sqm: number;
    green_cover_pct: number;
    built_cover_pct: number;
    parking_spaces: number;
    parking_efficiency_pct: number;
    tree_count: number;
    livability_score: number;
    walking_priority: number;
    estimated_cost_lakh: number;
  };
  compliance_summary: {
    status: "valid" | "warning" | "violation";
    checks?: Array<{
      check: string;
      status: "valid" | "warning" | "violation";
      detail: string;
      source_citation?: string;
    }>;
    violations?: unknown[];
    disclaimer?: string;
  };
};

type VinyasGenState = {
  activeProjectId: string | null;
  wardProjectId: string | null;
  city: City;
  zoneCode: string;
  siteType: SiteType | null;
  officialBoundary: GeoJSON.Feature | null;
  actualBoundary: GeoJSON.Feature | null;
  activeLayoutGeoJSON: GeoJSON.FeatureCollection | null;
  materialChoices: Record<string, string>;
  complianceResults: unknown[];
  emergencyAccessResult: unknown | null;
  monsoonTestResult: unknown | null;
  encroachments: unknown[];
  beforeAfterMode: "before" | "after";
  activeTab: "layout" | "analysis" | "encroachment" | "phasing";
  mapMode: "2d" | "3d";
  regulation: RegulationDocument | null;
  regulationStatus: string;
  backendStatus: string;
  disclaimer: string;
  drawnFeature?: GeoJSON.Feature;
  layoutOptions: LayoutOption[];
  activeLayoutId?: string;
  sliderValues: SliderValues;
  copilotReply: string;
  reportText: string;
  reportId: string;
  showProposal: boolean;
  voteSummary: { support: number; concern: number; needs_changes: number };
  setCity: (city: City) => void;
  setZoneCode: (zoneCode: string) => void;
  setSiteType: (siteType: SiteType | null) => void;
  setOfficialBoundary: (feature: GeoJSON.Feature) => void;
  setRegulation: (regulation: RegulationDocument | null) => void;
  setRegulationStatus: (status: string) => void;
  setBeforeAfterMode: (mode: "before" | "after") => void;
  setActiveTab: (tab: "layout" | "analysis" | "encroachment" | "phasing") => void;
  setBackendStatus: (status: string) => void;
  setDisclaimer: (disclaimer: string) => void;
  setDrawnFeature: (feature: GeoJSON.Feature) => void;
  setLayoutOptions: (options: LayoutOption[]) => void;
  setActiveLayoutId: (layoutId: string) => void;
  setSliderValues: (values: Partial<SliderValues>) => void;
  setCopilotReply: (reply: string) => void;
  setReportText: (report: string) => void;
  setReportId: (reportId: string) => void;
  setShowProposal: (showProposal: boolean) => void;
  setVoteSummary: (summary: { support: number; concern: number; needs_changes: number }) => void;
};

export const useVinyasGenStore = create<VinyasGenState>((set) => ({
  activeProjectId: null,
  wardProjectId: null,
  city: "noida",
  zoneCode: "residential_group_housing",
  siteType: null,
  officialBoundary: null,
  actualBoundary: null,
  activeLayoutGeoJSON: null,
  materialChoices: {},
  complianceResults: [],
  emergencyAccessResult: null,
  monsoonTestResult: null,
  encroachments: [],
  beforeAfterMode: "before",
  activeTab: "layout",
  mapMode: "2d",
  regulation: null,
  regulationStatus: "Select a city and zone",
  backendStatus: "Checking",
  layoutOptions: [],
  sliderValues: {
    density_level: 0.45,
    greenery_pct: 0.25,
    pedestrian_priority: 0.4
  },
  copilotReply: "",
  reportText: "",
  reportId: "",
  showProposal: true,
  voteSummary: { support: 0, concern: 0, needs_changes: 0 },
  disclaimer:
    "VinyasGen is a decision-support and visualization tool. Compliance results are indicative, based on digitized regulatory data, and do not constitute statutory approval. All proposals must be verified with the relevant municipal authority before implementation.",
  setCity: (city) => set({ city }),
  setZoneCode: (zoneCode) => set({ zoneCode }),
  setSiteType: (siteType) => set({ siteType }),
  setOfficialBoundary: (officialBoundary) => set({ officialBoundary, drawnFeature: officialBoundary }),
  setRegulation: (regulation) => set({ regulation }),
  setRegulationStatus: (regulationStatus) => set({ regulationStatus }),
  setBeforeAfterMode: (beforeAfterMode) => set({ beforeAfterMode }),
  setActiveTab: (activeTab) => set({ activeTab }),
  setBackendStatus: (backendStatus) => set({ backendStatus }),
  setDisclaimer: (disclaimer) => set({ disclaimer }),
  setDrawnFeature: (drawnFeature) => set({ drawnFeature }),
  setLayoutOptions: (layoutOptions) =>
    set({
      layoutOptions,
      activeLayoutId: layoutOptions[0]?.layout_id
    }),
  setActiveLayoutId: (activeLayoutId) => set({ activeLayoutId }),
  setSliderValues: (values) =>
    set((state) => ({
      sliderValues: { ...state.sliderValues, ...values }
    })),
  setCopilotReply: (copilotReply) => set({ copilotReply }),
  setReportText: (reportText) => set({ reportText }),
  setReportId: (reportId) => set({ reportId }),
  setShowProposal: (showProposal) => set({ showProposal }),
  setVoteSummary: (voteSummary) => set({ voteSummary })
}));
