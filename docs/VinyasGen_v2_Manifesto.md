VinyasGen — Complete Product & Technical Manifesto
Version 2.0 — Final Agentic Build Brief
"Generative Intelligence for Indian Urban Regeneration"
---
CRITICAL INSTRUCTIONS FOR ANY AI AGENT READING THIS
This document is the **single source of truth** for building VinyasGen. Read it completely before writing a single line of code. Every section connects to another — the data models feed the engines, the engines feed the API, the API feeds the frontend. Build in the exact phase order specified. Do not skip phases or combine them.
**Non-negotiable rules that apply to every line of code you write:**
1. All bylaw/regulation constraints live in editable JSON files — never hardcoded in Python or JavaScript
2. The LLM (AI Copilot) never performs geometry math or outputs coordinates — it only translates user language into structured JSON constraint objects that the deterministic Python engine then processes
3. Every compliance flag shown to the user must include a citation: document name, section, and value
4. Every report, every screen, every PDF must display the legal disclaimer defined in Section 11
5. Use only free and open-source tools — full list in Section 19
6. Build exactly one phase at a time. Do not start Phase 2 until Phase 1 passes all tests defined in that phase
---
Table of Contents
1. Project Identity & Mission
2. The Problem Being Solved
3. Who Uses This (Primary Users)
4. Competitive Landscape — What Exists vs. What VinyasGen Does
5. The Full Feature Set — Tiers and Descriptions
6. System Architecture — How Everything Connects
7. The Road-Gali-Ground Network (Scope of Physical Coverage)
8. Data Models & Database Design
9. The Regulation Engine
10. The 2D Generative Geometry Engine
11. The Encroachment Detection System
12. The Specialized Analysis Modules
13. The AI Agent Ecosystem
14. The AI Copilot
15. Frontend Architecture & UX
16. Backend Architecture
17. API Specification
18. Repository & Folder Structure
19. Free Stack — Every Tool Used
20. Phase 1 — Foundation (Weeks 1–3)
21. Phase 2 — Core Engines (Weeks 4–8)
22. Phase 3 — Differentiator Features (Weeks 9–14)
23. Phase 4 — Intelligence Layer (Weeks 15–20)
24. Phase 5 — Polish & Scale (Weeks 21–26)
25. Testing Strategy per Phase
26. Deployment per Phase
27. Legal Disclaimer Requirements
28. Appendix — Sample JSON Schemas, Code Stubs, Agent Prompts
---
1. Project Identity & Mission
**Name:** VinyasGen
**Tagline:** Generative Intelligence for Indian Urban Regeneration
**Sanskrit Root:** Vinyas (विन्यास) = intentional arrangement, deliberate placement
**Gen** = Generative — AI-driven, algorithmic, automated
**Mission:** Give government urban planners, architects, and civic agencies in Indian cities the ability to take any road, gali, lane, or empty public plot — understand what is wrong with it, generate a regulation-compliant redesign, test it against monsoon flooding and fire safety, document it professionally, and produce a submission-ready proposal — all within minutes instead of days or weeks.
**What VinyasGen is NOT:**
- Not a real estate developer tool (that is TestFit's domain)
- Not a 3D architectural modelling tool (that is Revit's domain)
- Not a government enforcement system (it is a Decision Support System)
- Not a consumer app for general public browsing
**Legal Disclaimer (must appear on every screen and every report):**
> "VinyasGen is a decision-support and visualization tool. All outputs — layouts, compliance results, cost estimates, and encroachment flags — are indicative only, based on digitized regulatory data, and do not constitute statutory approval, legal measurement, or enforcement action. All proposals must be verified with the relevant municipal authority before implementation. Encroachment flags are potential indicators requiring field verification — they do not constitute legal evidence."
---
2. The Problem Being Solved
Indian cities — particularly in the NCR region (Delhi, Noida/Greater Noida, Gurgaon) — face a cluster of interconnected street-level urban problems that existing software does not address:
**A. Encroachment & Road Width Loss**
Buildings in dense Indian colonies extend beyond their official plot boundaries into public road space. A gali officially 9 metres wide may have an actual usable width of only 5.5 metres after accounting for extended construction on both sides. No accessible tool exists to measure, document, and visualize this loss for planning purposes.
**B. No Footpaths or Broken Footpaths**
Most internal colony roads and galis have no designated pedestrian space. Pedestrians walk in vehicle lanes. Where footpaths exist, they are encroached, broken, or at wrong levels.
**C. Thermal Discomfort**
Standard concrete and asphalt surfaces in Indian streets reach 60–70°C in summer. Peak urban heat island effect in NCR cities adds 3–5°C to ambient temperatures. No planning tool helps designers choose and compare thermally appropriate Indian paving materials with cost and temperature data together.
**D. Monsoon Waterlogging**
Only 20% of India's urban road network is covered by stormwater drains. Urban flooding causes approximately $4 billion in annual losses in India. Infrastructure projects are planned in silos without considering water flow. No planning tool for Indian streets runs a simple drainage adequacy check.
**E. Chaotic Parking**
Two-wheelers are the dominant vehicle in Indian galis but no parking planning tool treats them as the primary type. Unplanned parking consumes road width, blocks emergency access, and creates permanently congested entry points.
**F. Poor Street Lighting**
Street lights are placed without geometry-based coverage analysis. Dark spots, glare into homes, poles blocking footpaths, and poles under tree canopy whose growth will block light within 2 years — all are routine problems that a simple placement engine could prevent.
**G. Emergency Access Failure**
Encroachments, parked vehicles, and poor road design mean fire trucks and ambulances cannot reach large portions of Indian residential colonies. This is life-safety critical and legally required to address in any development proposal.
**H. No Professional Tool for Government Planners**
Government architects and urban planners in municipal bodies and agencies currently use AutoCAD for drawing, Excel for calculations, and Word for reports — three separate tools with no regulatory intelligence. Producing one feasibility report for one gali intervention takes 2–3 days. VinyasGen reduces this to under an hour.
---
3. Who Uses This (Primary Users)
**Primary — Government Urban Planners & Architects**
Staff at municipal corporations (MCD, NMMC, GMC), development authorities (DDA, GNIDA, DTCP), Smart Cities Mission offices, and Public Works Departments. They produce official proposals for ward-level street improvements, redevelopment schemes, and infrastructure projects. They need speed, compliance accuracy, and professional output formats.
**Primary — Architecture & Urban Planning Agencies**
Private firms contracted by government bodies to produce urban design proposals. They need the same outputs as government planners but also need to manage multiple sites simultaneously and present polished visualizations to clients.
**Secondary — Civic Tech NGOs & Research Institutions**
Organizations running neighbourhood improvement programs who interface with government and need professional-grade documentation to be taken seriously.
**Tertiary (Future) — RWAs & Community Groups**
Access through a simplified "view and comment" interface on proposals created by primary users. Not layout designers themselves in the current scope.
---
4. Competitive Landscape
| Dimension | TestFit (Global) | UrbanEyes.in (Indian) | VinyasGen |
|---|---|---|---|
| Primary problem | New construction feasibility for developers | Site analysis reports for architects | Street/gali regeneration for government planners |
| Scale | City blocks, large sites | Any site, macro analysis | Roads, galis, public plots — street level |
| Regulation base | US/Western zoning codes | General GIS overlays | Indian municipal bye-laws as structured data |
| Encroachment detection | None | None | CV-assisted + manual, flagged with measurements |
| Monsoon simulation | None | None | Hydrology stress test per layout |
| Indian material selector | None | None | Indian paving materials with INR cost + thermal data |
| Two-wheeler parking | None | None | Primary parking type, herringbone + kerb-conversion |
| Emergency access check | None | None | Mandatory pre-submission geometry check |
| Phased budget planning | None | None | Phase-by-phase cost split aligned to municipal budgets |
| Output format | 3D massing + financials | PDF site analysis report | MCD/authority-ready submission report |
**The gap VinyasGen fills:** No tool in the world takes a chaotic Indian street, quantifies its problems, generates a compliant redesign, tests it for monsoon drainage and fire safety, and produces a government-submission-ready document. This is the product.
---
5. The Full Feature Set
Tier 1 — Foundation Features (Phase 1 & 2, Must Launch With These)
**F1. Multi-Input Site Boundary Tool**
Users define a site in three ways: (a) draw a polygon or click a road segment directly on the MapLibre map, (b) upload a boundary file — GeoJSON, KML, CAD DXF, or Shapefile, (c) geocode-search an address to centre the map then draw. All three inputs produce a standardized GeoJSON polygon stored in the database. Supports roads, galis, empty plots, and public spaces. The drawn/uploaded boundary becomes the "official boundary" reference for all subsequent analysis.
**F2. City + Zone Regulation Loader**
User selects city (Noida, Delhi, Gurgaon — expandable) and zone type (residential sector, residential colony, commercial road, mixed-use, etc.). System loads the matching regulation JSON file and applies it to every subsequent calculation. Incentives (TOD zone near metro, green building certification) are user-toggleable and apply bonuses to FAR/setback constraints automatically. Every constraint shown has its source document, section, and value displayed to the user.
**F3. Gali / Road Cross-Section Regenerator**
Given a total road or lane width (user-measured or from official boundary), the system generates the optimal allocation of that width into functional zones: vehicle carriageway, parking bay (two-wheeler and/or car), footpath, open or covered stormwater drain channel, and green/planter strip. Shows two states side by side: (a) "Current State" — usable width after encroachments, (b) "Post-Reclamation State" — full legal width if encroachments removed. Works for any width from 2.5m (narrow gali) to 24m (sector road). Output is a dimensioned cross-section diagram in GeoJSON that becomes the layout foundation.
**F4. 2D Generative Layout Engine**
Takes the cross-section zones and generates 3–5 complete alternative site layouts, each optimized for a different primary objective:
- Option A: Maximum Parking (two-wheeler-first)
- Option B: Maximum Green Cover & Thermal Comfort
- Option C: Pedestrian-First / Woonerf (shared space)
- Option D: Fire Safety Optimized (emergency access priority)
- Option E: Balanced Community (equal weighting across all objectives)
Each option is a complete GeoJSON FeatureCollection with every zone polygon labelled, coloured, and annotated with area and compliance status. All 5 options are generated simultaneously and shown in a carousel. The user selects one and edits it with sliders.
**F5. Real-Time Constraint Solver (Sliders)**
After selecting a layout option, three sliders let the user shift the balance:
- Parking Density (Low ↔ High)
- Green Cover % (5% ↔ 40%)
- Pedestrian Priority (Vehicle-First ↔ Pedestrian-First)
Moving a slider triggers a debounced API call (150ms after user stops dragging). Backend recomputes geometry using Shapely and returns updated GeoJSON within 300ms. Deck.gl animates the transition on the map. Impact Dashboard updates simultaneously. This is the core "TestFit interaction moment."
**F6. Compliance Checker**
Runs automatically on every generated and edited layout. Checks every regulation in the active zone's JSON file: setbacks, ground coverage, green area minimum, parking count minimum, road width minimums, drain clearance. Returns per-zone compliance status: valid (green), warning (yellow), violation (red). Every flag includes the exact bylaw text, document name, section number, and required vs. actual value. No compliance result is shown without its citation.
**F7. Emergency Access Checker**
Mandatory check that runs before any layout can be exported or submitted. Geometric check: (a) Is there a continuous clear path of minimum 4.5m width through the entire site? (b) At every junction, is there a minimum 9m turning radius (fire truck standard per NBC 2016)? (c) Are all zones reachable from the main road access point? Zones that fail are highlighted in red with a specific note. No PDF report can be generated for a layout that has unresolved emergency access violations — the system blocks export and requires the user to resolve or explicitly acknowledge and override with a written justification.
**F8. Parking Optimizer (Two-Wheeler-First)**
Dedicated module for packing maximum valid parking stalls into any shape of available space. Uses Google OR-Tools CP-SAT solver. Vehicle types and standard Indian dimensions:
- Two-wheeler bay: 1.0m × 2.5m
- Car bay: 2.5m × 5.0m
- Aisle width (two-wheeler): minimum 3.0m
- Aisle width (car): minimum 6.0m
Supports layout patterns: perpendicular, parallel, herringbone (most efficient for two-wheelers in irregular spaces), and kerb-conversion (marking a lane edge as a formal parallel parking strip). Output: parking layout GeoJSON + total count by vehicle type + parking efficiency score (used area / total allocated area).
**F9. Live Impact Dashboard**
Persistent right-side panel that updates in real time with every layout change:
- Parking: total bays (car + two-wheeler), change vs. current state
- Green Cover: % of total area, change vs. current state
- Walkable Path: total metres of footpath, change vs. current state
- Thermal Score: estimated surface temperature reduction from material choices (°C)
- Drainage Capacity: estimated max rainfall handled (mm/hr) — updated by monsoon module
- Compliance Status: summary of all checks (pass/warn/fail)
- Estimated Cost: INR range (low / expected / high) per phase
- Emergency Access: pass/fail
**F10. Before/After Toggle**
Top-centre switch on the map. "Before" shows the current satellite/street tile imagery with the user's official boundary outline. "After" shows the generated vector layout overlaid on a muted basemap. Both states show the same scale and zoom level. This is the primary tool for stakeholder presentations — a non-technical audience understands the proposal in one visual switch.
**F11. MCD/Authority Submission Report (PDF)**
Generates a professionally formatted proposal document containing:
- Project title, date, preparer name/agency, site coordinates
- Site location map with north arrow and scale bar
- Before/After layout diagrams (plan view)
- Dimensioned cross-section diagram
- Regulation compliance table (constraint / required value / proposed value / status / citation)
- Impact metrics table
- Phased implementation plan with cost estimates
- Emergency access certification (pass/fail with geometry evidence)
- Legal disclaimer (mandatory, cannot be removed or hidden)
- Signature block for authority use
Generated using WeasyPrint (free, open-source HTML-to-PDF). The HTML template is version-controlled so the format can be updated without touching the backend logic.
---
Tier 2 — Differentiator Features (Phase 3, VinyasGen's Innovation)
**F12. Encroachment Quantifier (Manual Mode — Phase 2 completion)**
User draws two overlapping polygons on the map: (a) the official road right-of-way boundary (from uploaded municipal records or user measurement), (b) the actual usable road boundary (measured in the field or estimated from map imagery). The system calculates the difference geometry — the areas that fall inside the official ROW but outside the actual usable width. These areas are the encroachments. Each encroachment zone is labelled with: estimated depth into the road (metres), estimated area (sqm), and an anonymised ID (Structure A, B, C — never property owner names or addresses). The "Reclamation Potential" calculation shows total width recoverable and what the cross-section looks like if all encroachments are removed. This reclaimed cross-section can be directly sent to the Cross-Section Regenerator (F3) as the new baseline.
**F13. CV-Assisted Encroachment Detection (Three Input Modes — Phase 3)**
The system detects potential encroachments automatically from imagery. Three modes, all producing the same output:
*Mode 1 — Map-First (Primary):* User draws a frame around a gali or clicks a road segment on the MapLibre map. System captures the map tile imagery within that frame. Runs building footprint extraction model on the captured image. Compares detected structure polygons against the official boundary. Anything outside the official boundary is flagged red.
*Mode 2 — Upload Drone/Satellite Image:* User uploads a georeferenced image from a drone survey or downloaded from ISRO Bhuvan. System georeferences it using the user's drawn boundary as anchor. Runs the same footprint extraction pipeline.
*Mode 3 — Upload Official Cadastral File:* User uploads GeoJSON/Shapefile of official plot boundaries per the municipal cadastral record. System uses these as the authoritative boundary layer. Combined with Mode 1 or Mode 2 imagery, this produces the most accurate encroachment detection.
*Model:* Mask R-CNN fine-tuned on Indian urban building imagery (SpaceNet dataset + Cartosat Indian imagery). Runs server-side on the FastAPI backend via PyTorch inference endpoint.
*Resolution handling:* System detects image resolution and shows a "Detection Confidence" indicator:
- Standard map tiles (~50cm/px): estimated accuracy ±0.5m, flagged as "indicative"
- Cartosat/Bhuvan imagery (~25cm/px): accuracy ±0.25m, flagged as "planning grade"
- Drone imagery (≤10cm/px): accuracy ±0.05m, flagged as "survey grade"
*Output:* Red polygon overlays on map. Summary table with anonymised IDs, encroachment depth, and estimated area. "Verify" button per flagged structure (user confirms or dismisses each one). Only confirmed encroachments carry through to the report.
**F14. Indian Material Thermal Selector**
A material library specific to Indian construction and urban contexts. Stored as a JSON file under `/data/materials/indian_paving_materials.json`. User selects materials for each zone in the layout (footpath, vehicle lane, parking bay, green strip) from a dropdown picker. The impact dashboard updates the Thermal Score immediately.
Material library includes (minimum, expandable):
| Material | Temp Reduction (°C) | Cost INR/sqm (Expected) | Availability | Maintenance |
|---|---|---|---|---|
| Standard grey concrete | 0 (baseline) | 350 | Universal | Low |
| Shahabad stone (natural) | 3–4 | 550 | North India | Low |
| Kota stone (natural) | 2–3 | 480 | Most cities | Low |
| ILC interlocking brick pavers (red/buff) | 2–3 | 600 | Universal | Medium |
| Sand-set clay brick pavers | 3–4 | 520 | Universal | Medium |
| Cool-coat reflective asphalt coating | 5–8 | 180 (coating only) | Major cities | High |
| Compressed stabilized earth blocks | 4–5 | 420 | Regional | Medium |
| Grass/gravel parking grid | 6–8 | 700 | Universal | High |
| Permeable concrete | 4–6 | 850 | Major cities | High |
Each material also has a `runoff_coefficient` property (used by the Monsoon Stress Test) and a `thermal_mass` property (used in future solar gain calculations).
**F15. Monsoon Stress Test**
After the user finalises a layout, they press "Test in Monsoon." The system performs a simple hydrology calculation (no complex simulation — this is deterministic arithmetic):
```
For each surface zone in the layout:
  Runoff_Volume (L/hr) = Rainfall_Intensity (mm/hr)
                         × Zone_Area (sqm)
                         × Runoff_Coefficient (from material library)
Total_Runoff = sum of all zone runoff volumes
Drain_Capacity (L/hr) = Drain_Width (m)
                        × Drain_Depth (m)
                        × Flow_Velocity (m/hr)  [standard Manning's value for concrete drain]
                        × Number_of_Drain_Segments
If Total_Runoff > Drain_Capacity:
  → Pooling will occur
  → Show which zones contribute most runoff
  → Suggest: add drain segment / increase drain size / use more permeable material
  → Calculate max rainfall intensity the layout CAN handle: solve for Rainfall_Intensity
    where Total_Runoff = Drain_Capacity
Output: "Your layout handles up to X mm/hr before pooling occurs.
         NCR design storm is 80mm/hr. [Status: PASS / FAIL]
         To achieve 80mm/hr capacity: [specific suggestion]."
```
User can run this test multiple times as they adjust materials or add drain segments, watching the capacity number change in real time. This is shown as a dedicated tab in the Impact Dashboard.
**F16. Drainage Slot Indicator**
Integrated with the Cross-Section Regenerator. When the user inputs a cross-section, the system:
1. Asks for the road's slope direction (dropdown: slopes toward left edge / right edge / centre / flat)
2. Automatically places a drain channel indicator on the lowest edge of the cross-section
3. Suggests drain type based on available width:
   - Width ≥ 0.6m available: Bioswale/tree trench (permeable, green, doubles as planting bed)
   - Width 0.3–0.6m available: Covered drain with grating (pedestrian-safe)
   - Width < 0.3m available: Open concrete channel (minimal footprint)
4. Shows estimated cost per running metre for each type in INR
5. Drain position and type feed directly into the Monsoon Stress Test (F15)
**F17. Street Light Placement Engine**
Input: the gali/road geometry (already known from the cross-section) + existing pole positions if known (user-marks them on the map as point features).
The engine calculates:
1. **Coverage zones:** Each pole illuminates a circular radius based on pole height and luminaire type (default: 7m pole, 18W LED, ~12m illumination radius at footpath level, recommended 4500K colour temperature based on pedestrian safety research)
2. **Gaps:** Areas of the gali where no pole's coverage circle reaches — shown as dark grey zones on the map
3. **Optimal new pole positions:** Computed by placing poles at intervals such that coverage circles overlap by 20% (standard practice for uniform illumination) with no gaps
4. **Dangerous existing poles:** Flags any existing pole that: (a) sits within the footpath zone reducing walkable width below minimum, (b) sits directly under where a tree will be placed (canopy will block light within 3–5 years), (c) is within 1.5m of a marked electrical infrastructure position
Output: recommended pole positions as point features on the map, estimated pole + wiring cost per new pole, list of existing poles recommended for relocation.
**Electrical Infrastructure Placeholder Layer:** A separate map layer called "Utility Infrastructure" where users can manually mark: distribution transformers (box), LT/HT poles, cable corridors (line). These are treated as fixed obstacles — no tree is placed under a cable corridor, no light pole within 1.5m of a transformer. This layer is blank by default and filled by the user from their field survey or DISCOM records. Full DISCOM data integration is a future phase feature.
**F18. Phased Implementation Planner**
After finalising a layout, the user assigns every element in the layout to a phase (Phase 1 / Phase 2 / Phase 3) by clicking elements on the map or using the left-panel list. Rules:
- Phase 1 must always include Emergency Access compliance elements first
- User can override this rule with a written justification (logged in the project record)
System auto-calculates:
- Cost per phase (low/expected/high range in INR)
- Elements per phase shown as distinct coloured layers (Phase 1 = solid, Phase 2 = hatched, Phase 3 = dotted)
- Timeline estimate per phase based on element types and quantities
- Phase 1 is submission-ready immediately; Phases 2 and 3 are flagged as "future works"
The PDF report includes a phasing table and a phased layout diagram. Government planners align phases with annual municipal capital expenditure cycles.
**F19. Multi-Site Ward Project Manager**
A project management layer for government users working on an entire ward (typically 40–100 sites simultaneously).
Features:
- Create a "Ward Project" that contains multiple individual sites
- Ward-level map view: all sites visible simultaneously, colour-coded by status:
  - Grey: boundary drawn only
  - Blue: analysis complete
  - Yellow: layout proposed
  - Orange: submitted to authority
  - Green: approved
  - Purple: under construction
- Click any site on the ward map to open it in the main editor
- Ward-level summary report: total sites, total area addressed, aggregate cost estimate, aggregate impact metrics (total parking added across ward, total green cover added, etc.)
- Export ward-level report as PDF
---
Tier 3 — Phase 4/5 Features (After Core Is Proven)
**F20. 3D Presentation Mode**
A toggle on top of the 2D plan. Not a separate mode — a layer. When activated:
- All zone polygons are extruded to their respective heights (buildings on either side from OSM building height data, walls, retaining elements)
- Shows the "street canyon" effect — how tall structures on both sides of a gali restrict ventilation and light
- Sun-shadow simulation: user picks date and time, shadows cast by adjacent buildings and proposed trees are shown on the cross-section
- Export as a static 3D render image for inclusion in reports
Built using Three.js (free, open-source). Connected to the existing Deck.gl layer via a shared GeoJSON data store — no separate data pipeline needed.
**F21. Vertical Green Finder**
When a gali or road is narrower than 4.5m (too narrow for standard tree pits), the system automatically flags this in the impact dashboard: "This section is too narrow for ground-level trees. Wall-mounted planters or creeper trellises on south/west-facing walls are recommended." The user can then click a "Add Vertical Green" button which places wall planter markers on eligible wall surfaces (auto-detected from the building boundary geometry).
**F22. Pocket Park / Dead Space Converter**
Automatically identifies dead spaces: triangular corners, widened junctions, dead-end road terminations, and areas between buildings wider than 3m with no current designation. For each identified space, suggests a use from the Kit-of-Parts library: community seating, water point, children's corner, waste collection bay, or tree grove. User selects a suggestion and the element is placed in the layout.
**F23. Community Consultation Layer**
A shareable link generated from any finalized layout. Recipients (residents, other stakeholders) can view the Before/After toggle and impact metrics in a read-only map view. They can submit structured feedback: (a) approve the proposal, (b) suggest a change (text comment linked to a location on the map), (c) flag a concern. Feedback is aggregated in the project dashboard and can be exported as a consultation summary appendix to the PDF report. This supports the formal public consultation process required for many government-led urban improvement schemes.
---
6. System Architecture — How Everything Connects
```
┌─────────────────────────────────────────────────────────────────┐
│                    CLIENT LAYER (Browser)                        │
│                                                                  │
│  Next.js App (TypeScript)                                        │
│  ├── MapLibre GL JS — base map tiles (OSM/free provider)         │
│  ├── MapLibre GL Draw — polygon/point drawing tools              │
│  ├── Deck.gl — vector overlay rendering (GeoJSON layers)         │
│  ├── Three.js — 3D presentation mode (Phase 4)                   │
│  ├── Turf.js — lightweight client-side geometry preview          │
│  ├── Zustand — global state (active layout, sliders, map state)  │
│  └── Tailwind CSS — styling                                      │
└──────────────────────────┬──────────────────────────────────────┘
                           │ REST API (JSON)
                           │ ~300ms target response time
┌──────────────────────────▼──────────────────────────────────────┐
│                    API LAYER (FastAPI / Python)                   │
│                                                                  │
│  Routes:                                                         │
│  ├── /api/layout/*      — generative engine endpoints            │
│  ├── /api/regulations/* — bylaw loading and compliance           │
│  ├── /api/encroachment/*— detection and analysis                 │
│  ├── /api/analysis/*    — monsoon, lighting, drainage, access    │
│  ├── /api/report/*      — PDF generation                         │
│  ├── /api/project/*     — ward project management                │
│  └── /api/copilot/*     — AI copilot (LLM orchestration only)    │
│                                                                  │
│  Engines (deterministic Python modules):                         │
│  ├── geometry_engine.py   — Shapely: setback, subdivision,       │
│  │                          zone allocation, boolean ops          │
│  ├── parking_optimizer.py — OR-Tools: stall packing              │
│  ├── compliance_checker.py— regulation JSON validation           │
│  ├── encroachment.py      — boundary comparison, measurement     │
│  ├── cv_detector.py       — Mask R-CNN inference (Phase 3)       │
│  ├── monsoon_test.py      — hydrology calculation                │
│  ├── lighting_engine.py   — pole coverage geometry               │
│  ├── drainage_engine.py   — drain slot placement and sizing      │
│  ├── access_checker.py    — emergency access geometry            │
│  ├── phase_planner.py     — cost aggregation by phase            │
│  ├── report_generator.py  — WeasyPrint PDF assembly              │
│  └── geo_utils.py         — CRS conversion (WGS84 ↔ UTM43N)     │
└──────────────────────────┬──────────────────────────────────────┘
                           │
┌──────────────────────────▼──────────────────────────────────────┐
│                    DATA LAYER                                     │
│                                                                  │
│  SQLite (MVP) → PostgreSQL + PostGIS (Scale)                     │
│  ├── projects table          — site boundaries, metadata         │
│  ├── layout_options table    — generated GeoJSON layouts         │
│  ├── compliance_results table— per-check results                 │
│  ├── ward_projects table     — multi-site project management     │
│  └── reports table           — generated PDF metadata            │
│                                                                  │
│  File-based data (JSON):                                         │
│  ├── /data/regulations/      — bylaw JSON per city/zone          │
│  ├── /data/materials/        — Indian paving material library    │
│  ├── /data/kit_of_parts/     — reusable design elements          │
│  └── /data/cost_reference/   — INR cost data per element         │
└──────────────────────────┬──────────────────────────────────────┘
                           │
┌──────────────────────────▼──────────────────────────────────────┐
│                    AGENT LAYER (Antigravity-Orchestrated)         │
│                                                                  │
│  Agent 1: Regulation Researcher — PDF → JSON extraction          │
│  Agent 2: Geometry Optimizer   — writes & tests Shapely code     │
│  Agent 3: Visual QA            — browser automation testing      │
│  Agent 4: Copilot              — NL → constraint JSON (LLM)      │
│  Agent 5: Report Content       — layout metrics → PDF prose      │
└─────────────────────────────────────────────────────────────────┘
```
---
7. The Road-Gali-Ground Network (Scope of Physical Coverage)
VinyasGen covers the full hierarchy of public road and path infrastructure in Indian urban areas. This is not a gali-only tool — it handles every level of the network:
| Level | Description | Typical Width | Primary VinyasGen Use |
|---|---|---|---|
| Sector/Arterial Road | Major planned roads in Noida/Gurgaon sectors | 18–45m | Full cross-section design, TOD zone detection, lighting |
| Colony Main Road | Primary internal road of a residential colony | 9–18m | Cross-section, parking, green strip, drainage |
| Colony Internal Road | Secondary roads within a colony | 6–12m | Cross-section, two-wheeler parking, footpath |
| Gali (Lane) | Narrow residential lanes | 2.5–9m | Encroachment detection, cross-section, emergency access |
| Footpath / Pavement | Pedestrian-only paths | 0.9–3m | Material selection, lighting, accessibility |
| Public Plot / Dead Space | Unused/underused land parcels | Any | Pocket park, parking lot, community space design |
All of these are valid inputs to the site boundary tool. The cross-section regenerator and generative layout engine adapt to the width automatically — a 2.5m gali produces very different options than a 24m sector road, but both go through the same pipeline.
---
8. Data Models & Database Design
8.1 Core Tables
```sql
-- Projects: each site the user works on
CREATE TABLE projects (
    project_id      TEXT PRIMARY KEY,
    ward_project_id TEXT REFERENCES ward_projects(id),
    user_id         TEXT,
    site_name       TEXT,
    city            TEXT,
    zone_code       TEXT,
    site_type       TEXT,  -- 'road', 'gali', 'empty_plot', 'public_space'
    plot_geojson    TEXT,  -- official boundary, WGS84
    actual_geojson  TEXT,  -- actual usable boundary (post-encroachment measurement)
    total_width_m   REAL,
    usable_width_m  REAL,
    slope_direction TEXT,
    status          TEXT DEFAULT 'boundary_drawn',
    created_at      DATETIME,
    updated_at      DATETIME
);
-- Layout options generated for each project
CREATE TABLE layout_options (
    layout_id           TEXT PRIMARY KEY,
    project_id          TEXT REFERENCES projects(project_id),
    objective_profile   TEXT,  -- 'max_parking', 'max_green', etc.
    geojson             TEXT,  -- full FeatureCollection
    metrics_json        TEXT,  -- parking count, green%, path length, etc.
    slider_values_json  TEXT,  -- density, greenery_pct, pedestrian_priority
    material_choices    TEXT,  -- JSON: zone_id → material_id
    phase_assignments   TEXT,  -- JSON: feature_id → phase number
    is_active           INTEGER DEFAULT 0,
    created_at          DATETIME
);
-- Compliance results per layout
CREATE TABLE compliance_results (
    result_id       TEXT PRIMARY KEY,
    layout_id       TEXT REFERENCES layout_options(layout_id),
    check_name      TEXT,
    status          TEXT,   -- 'valid', 'warning', 'violation'
    required_value  TEXT,
    actual_value    TEXT,
    detail          TEXT,
    citation        TEXT,   -- document, section, page
    created_at      DATETIME
);
-- Encroachment records per project
CREATE TABLE encroachments (
    encroachment_id     TEXT PRIMARY KEY,
    project_id          TEXT REFERENCES projects(project_id),
    anon_label          TEXT,   -- 'Structure A', 'Structure B', etc.
    geometry_geojson    TEXT,   -- the encroachment polygon
    depth_m             REAL,
    area_sqm            REAL,
    detection_mode      TEXT,   -- 'manual', 'cv_map', 'cv_upload'
    confidence          TEXT,   -- 'indicative', 'planning', 'survey'
    verified            INTEGER DEFAULT 0,
    created_at          DATETIME
);
-- Generated reports
CREATE TABLE reports (
    report_id       TEXT PRIMARY KEY,
    layout_id       TEXT REFERENCES layout_options(layout_id),
    report_type     TEXT,   -- 'mcd_submission', 'consultation', 'phase_1_only'
    pdf_path        TEXT,
    generated_at    DATETIME
);
-- Ward-level project management
CREATE TABLE ward_projects (
    id              TEXT PRIMARY KEY,
    ward_name       TEXT,
    city            TEXT,
    authority       TEXT,
    planner_name    TEXT,
    financial_year  TEXT,
    created_at      DATETIME
);
```
8.2 Coordinate Reference System Policy
- **Storage and transport:** WGS84 (EPSG:4326) — standard lat/lng, required by GeoJSON spec
- **All computation:** Reproject to UTM Zone 43N (EPSG:32643) which covers all of NCR with metre accuracy, then reproject back to WGS84 before returning to frontend
- **Every distance/area calculation must happen in UTM — never in degrees**
- The `geo_utils.py` module handles all conversions. Every other engine imports from `geo_utils.py`. Nothing does its own CRS conversion.
---
9. The Regulation Engine
9.1 Philosophy: Regulation-as-Data
Every regulation constraint is stored in a JSON file. No regulation is hardcoded in Python. This means:
- Updating a bylaw requires editing a JSON file, not redeploying code
- Adding a new city requires creating a new JSON file, not writing new logic
- The Regulation Researcher Agent can update files; a human reviewer approves before they go live
9.2 Regulation JSON Schema (Complete)
```json
{
  "city": "noida",
  "authority": "GNIDA",
  "zone_code": "residential_group_housing",
  "source_document": "Noida Building Bye-Laws (as amended)",
  "source_url": "https://noidaauthorityonline.in/",
  "last_verified": "2026-06-01",
  "review_status": "pending_review",
  "constraints": {
    "max_far": 3.5,
    "max_ground_coverage_pct": 0.35,
    "min_setback_front_m": 6.0,
    "min_setback_side_m": 4.5,
    "min_setback_rear_m": 4.5,
    "max_building_height_m": 45,
    "min_green_area_pct": 0.15,
    "min_road_width_m": 9.0,
    "parking_norms": {
      "two_wheeler_per_100sqm": 1.0,
      "four_wheeler_per_100sqm": 1.5,
      "min_aisle_width_car_m": 6.0,
      "min_aisle_width_2w_m": 3.0
    },
    "footpath_min_width_m": 1.5,
    "fire_safety": {
      "min_clear_access_width_m": 4.5,
      "min_turning_radius_m": 9.0,
      "max_dead_end_length_m": 30,
      "source": "NBC 2016, Part 4, Clause 4.2"
    },
    "drain_clearance_min_m": 0.3
  },
  "incentives": [
    {
      "name": "TOD Zone FAR Bonus",
      "condition": "within_500m_of_metro",
      "effect": { "max_far_bonus": 0.5 },
      "source": "GNIDA TOD Policy 2023"
    },
    {
      "name": "Green Building Bonus",
      "condition": "igbc_gold_certified",
      "effect": { "max_far_bonus": 0.2 },
      "source": "GNIDA Notification 2022-15"
    }
  ]
}
```
9.3 Cities to Build at Launch (Noida First, Others Follow)
| City | Authority | Zone Focus for MVP |
|---|---|---|
| Noida / Greater Noida | GNIDA | Residential sector, group housing |
| Delhi | DDA / MCD | Residential colony, unauthorized colony |
| Gurgaon | DTCP Haryana | Group housing, colony road |
Each is a separate folder under `/data/regulations/{city}/`. Each zone type within a city is a separate JSON file. Adding a new city = creating a new folder and JSON files. No code changes needed.
9.4 Human-in-the-Loop Workflow
The Regulation Researcher Agent puts new/updated files in `/data/regulations/pending_review/`. A human reviewer checks the values against the source document (URL provided in JSON). Only a human can move a file from `/pending_review/` to the live `/data/regulations/{city}/` folder. The system will not load any regulation file with `"review_status": "pending_review"` — it must be changed to `"approved"` by the human reviewer.
---
10. The 2D Generative Geometry Engine
10.1 Core Operations in Order
Every layout generation runs through these steps in order. Each step is a separate function in `geometry_engine.py`.
**Step 1: Normalize and Validate**
```python
def normalize_boundary(geojson_geometry: dict) -> Polygon:
    """
    Convert GeoJSON polygon to Shapely Polygon.
    Fix self-intersections using make_valid().
    Ensure the polygon is closed (first point = last point).
    Raise ValueError with clear message if geometry is invalid after repair.
    """
```
**Step 2: Project to Metric CRS**
```python
def to_utm(shapely_geom) -> Polygon:
    """
    Reproject from WGS84 to UTM Zone 43N (EPSG:32643).
    All subsequent operations happen in metres.
    Import from geo_utils.py — do not implement CRS logic here.
    """
```
**Step 3: Apply Setback Buffer (Plot Mode) or Width Allocation (Road Mode)**
For plots:
```python
def apply_setback(plot_utm: Polygon, setback_m: float) -> Polygon:
    """
    Negative buffer using join_style=2 (mitre = square corners for buildings).
    If result is empty, raise SetbackExceedsPlotError with user-friendly message.
    If result is MultiPolygon, return the largest piece and log a warning.
    """
```
For roads/galis (cross-section mode):
```python
def generate_cross_section_zones(
    centerline_utm: LineString,
    total_width_m: float,
    allocation: dict  # {'vehicle': 0.5, 'parking': 0.2, 'footpath': 0.15, 'drain': 0.05, 'green': 0.1}
) -> dict:
    """
    Buffer centerline by total_width/2 to get the road corridor polygon.
    Create parallel offset lines at cumulative allocation distances.
    Use shapely.ops.split to divide corridor into zone strips.
    Return dict of zone_name -> Polygon (in UTM).
    """
```
**Step 4: Generate Layout Options**
```python
OBJECTIVE_PROFILES = {
    'max_parking': {'vehicle': 0.45, 'parking': 0.30, 'footpath': 0.12, 'drain': 0.05, 'green': 0.08},
    'max_green':   {'vehicle': 0.40, 'parking': 0.10, 'footpath': 0.18, 'drain': 0.07, 'green': 0.25},
    'pedestrian':  {'vehicle': 0.35, 'parking': 0.10, 'footpath': 0.30, 'drain': 0.07, 'green': 0.18},
    'fire_safe':   {'vehicle': 0.55, 'parking': 0.20, 'footpath': 0.12, 'drain': 0.05, 'green': 0.08},
    'balanced':    {'vehicle': 0.42, 'parking': 0.20, 'footpath': 0.18, 'drain': 0.06, 'green': 0.14},
}
def generate_all_options(road_geometry, total_width_m, constraints):
    """
    Run generate_cross_section_zones for each objective profile.
    Run compliance checker on each result.
    Run parking optimizer on each parking zone.
    Return list of 5 layout dicts, each with geojson + metrics + compliance.
    All 5 are computed before returning — do not stream them one by one.
    """
```
**Step 5: Convert Back to GeoJSON**
```python
def zones_to_geojson(zones_utm: dict, metadata: dict) -> dict:
    """
    Reproject each zone polygon back to WGS84.
    Build a GeoJSON FeatureCollection.
    Each Feature has properties: zone_type, area_sqm, compliance_status,
    compliance_detail, style (fill_color, stroke_color, opacity).
    """
```
10.2 Zone Colour Coding (Consistent Across All Layouts)
| Zone Type | Fill Colour | Border Colour |
|---|---|---|
| Vehicle carriageway | #D9D9D9 (light grey) | #999999 |
| Two-wheeler parking | #A8C8E8 (light blue) | #4A90D9 |
| Car parking | #7BA7D0 (medium blue) | #2E6DA4 |
| Footpath | #F5E6C8 (warm beige) | #C4A46B |
| Green / planter strip | #A8D5A2 (light green) | #4F9D69 |
| Drain channel | #85C1E9 (sky blue) | #2E86AB |
| Encroachment (flagged) | #E74C3C (red, 50% opacity) | #C0392B |
| Emergency access path | #F39C12 (amber) | #D68910 |
| Compliance violation | #E74C3C (red border only, 30% fill) | #C0392B |
| Compliance warning | #F39C12 (amber border, 20% fill) | #D68910 |
---
11. The Encroachment Detection System
11.1 Manual Mode (Phase 2 — Built First)
The user interface presents two drawing tools active simultaneously on the map:
**Tool A — Official Boundary** (blue outline): The user draws or uploads the official road right-of-way as defined by municipal records. This represents the legal public space.
**Tool B — Actual Boundary** (red outline): The user draws the actual usable road space — the boundary beyond which structures are physically present.
The backend calculates: `encroachment_geometry = official_boundary.difference(actual_boundary)`
This difference geometry represents the road space that has been physically occupied. The system:
1. Splits the encroachment geometry into individual polygons per structure (using spatial clustering)
2. Labels each polygon anonymously: Structure A, Structure B, etc.
3. Calculates depth into the road (maximum perpendicular distance from the official boundary) and area (sqm)
4. Shows total reclamable width and what the cross-section looks like with encroachments removed
11.2 CV-Assisted Mode (Phase 3 — Built Second)
Architecture:
```
Image Input (map tile capture / uploaded image)
    ↓
Preprocessing: resize to 512×512 tiles with 20% overlap
    ↓
Mask R-CNN inference (PyTorch, server-side)
    → Model: pretrained on SpaceNet building dataset
    → Fine-tuned on: Indian urban imagery (Cartosat + manually annotated NCR samples)
    → Output: instance segmentation masks (one polygon per detected structure)
    ↓
Polygonization: convert masks to Shapely polygons
    ↓
Geolocation: align detected polygons to map coordinates
    using the official boundary as the georeferencing anchor
    ↓
Intersection test: detected_polygon.intersection(official_boundary)
    → Any detected structure with intersection area > 0.5 sqm
      is flagged as "potential encroachment"
    ↓
Confidence scoring based on image resolution:
    - Map tiles (~50cm/px): confidence = 'indicative'
    - Cartosat (~25cm/px): confidence = 'planning_grade'
    - Drone (≤10cm/px): confidence = 'survey_grade'
    ↓
Human verification step:
    Each flagged structure shown to user with [Confirm] [Dismiss] buttons
    Only confirmed encroachments appear in the report
```
11.3 Privacy Rules (Non-Negotiable in Code)
These rules must be enforced at the data model level, not just the UI level:
1. Encroachment records in the database store `anon_label` (Structure A, B, C) — never property owner name, house number, or owner contact information
2. The PDF report uses only anon labels
3. The shareable consultation link shows only anon labels
4. The system has no field for entering or storing owner identity
5. These constraints are documented in a `PRIVACY_CONSTRAINTS.md` file in the repository root that every agent must read before working on the encroachment module
---
12. The Specialized Analysis Modules
12.1 Emergency Access Checker (`access_checker.py`)
```python
def check_emergency_access(layout_geojson: dict, constraints: dict) -> dict:
    """
    Input: completed layout FeatureCollection + active regulation constraints
    Check 1 — Minimum Clear Width:
        For each 2m segment along the main path through the site:
        Calculate perpendicular clear width (road space minus all obstacles).
        If clear_width < constraints['fire_safety']['min_clear_access_width_m']:
            Mark segment as FAIL. Record location and actual width.
    Check 2 — Turning Radius:
        At every junction/bend in the layout:
        Measure the inside turning radius available.
        If radius < constraints['fire_safety']['min_turning_radius_m']:
            Mark junction as FAIL.
    Check 3 — Dead End Length:
        Identify all dead-end road segments.
        If length > constraints['fire_safety']['max_dead_end_length_m']:
            Mark as FAIL (fire truck cannot reverse safely beyond this length).
    Returns:
        {
          'overall_status': 'PASS' | 'FAIL',
          'violations': [{'type': str, 'location': [lng, lat], 'detail': str}],
          'clear_path_geojson': FeatureCollection of path segments coloured by status
        }
    IMPORTANT: If overall_status is 'FAIL', the report_generator must block PDF
    export and require user acknowledgement before proceeding.
    """
```
12.2 Monsoon Stress Test (`monsoon_test.py`)
```python
DESIGN_STORM_NCR = 80.0  # mm/hr — standard NCR design storm intensity
def run_monsoon_test(layout_geojson: dict, rainfall_intensity_mm_hr: float = DESIGN_STORM_NCR) -> dict:
    """
    For each zone Feature in the layout:
        Get zone_area_sqm from properties.
        Get runoff_coefficient from material library using properties['material_id'].
        runoff_volume_lph = rainfall_intensity_mm_hr/1000 * zone_area_sqm * 3600 * runoff_coefficient
    total_runoff_lph = sum of all zone runoff volumes
    For each drain Feature in the layout:
        drain_capacity_lph = drain_width_m * drain_depth_m * manning_velocity_mhr * 1000
        (manning_velocity for concrete drain, slope 1:200 ≈ 3600 m/hr)
    total_drain_capacity_lph = sum of all drain capacities
    max_handleable_intensity = solve: total_drain_capacity / (sum of area * coeff) * 1000/3600
    Return:
        {
          'status': 'PASS' if total_drain_capacity >= total_runoff else 'FAIL',
          'max_handleable_mm_hr': max_handleable_intensity,
          'design_storm_mm_hr': rainfall_intensity_mm_hr,
          'surplus_or_deficit_lph': total_drain_capacity - total_runoff,
          'highest_runoff_zones': [top 3 zones by runoff contribution],
          'suggestions': [generated based on what would fix a FAIL — add drain / use permeable material / etc.]
        }
    """
```
12.3 Lighting Engine (`lighting_engine.py`)
```python
STANDARD_POLE = {
    'height_m': 7.0,
    'luminaire_type': '18W_LED',
    'illumination_radius_m': 12.0,
    'recommended_colour_temp_k': 4500,
    'overlap_factor': 0.20  # coverage circles overlap by 20% for uniform illumination
}
def optimize_lighting(road_geometry_utm, existing_poles: list, obstacles: list) -> dict:
    """
    1. Generate candidate pole positions at intervals of:
       illumination_radius * (1 - overlap_factor) * 2 = spacing_m
       along the road centreline.
    2. For each candidate position:
       - Check it is not within the footpath zone (would reduce walkable width)
       - Check no tree is placed within illumination_radius/2 (canopy would block light)
       - Check no utility obstacle within 1.5m
       If any check fails, offset candidate by 0.5m increments until valid.
    3. For each existing pole:
       - Calculate its coverage circle
       - Flag as 'dangerous' if: within footpath zone, under planned tree, near utility obstacle
       - Flag as 'redundant' if its coverage circle is fully covered by optimal new placement
    4. Calculate gap zones: areas with no coverage from any pole (existing + new)
    Return:
        {
          'optimal_new_poles': [{'position': [lng, lat], 'spacing_from_prev_m': float}],
          'flagged_existing_poles': [{'position': [lng, lat], 'issue': str, 'recommendation': str}],
          'gap_zones': GeoJSON of uncovered areas,
          'coverage_pct': float,
          'estimated_cost_inr': float  # poles + wiring, from cost_reference.json
        }
    """
```
---
13. The AI Agent Ecosystem
Five specialized agents, each with a narrow, specific responsibility. They support the deterministic engines — they never replace them.
Agent 1 — Regulation Researcher
**Responsibility:** Convert government bylaw PDFs into approved regulation JSON files.
**Input:** PDF of a municipal bylaw document (provided by the human manager)
**Process:**
1. Extract text from PDF using PyPDF2 or pdfplumber
2. Pass text to LLM with this exact prompt structure:
```
You are extracting building regulation data for VinyasGen.
From the following bylaw document text, extract ONLY the following fields
and return them as a JSON object matching this exact schema: [schema].
For every field you extract, record the page number and section heading
where you found it. If you cannot find a field, set its value to null —
do not guess or invent a value.
Document text: [text]
```
3. Validate the returned JSON against the regulation schema (Pydantic)
4. Write output to `/data/regulations/pending_review/{city}_{zone}_{date}.json`
5. Write a summary file listing every extracted value and its source location
6. Never write directly to `/data/regulations/{city}/` — only to pending_review
**Human checkpoint:** A human reads the summary, verifies values against the source PDF, changes `review_status` from `"pending_review"` to `"approved"`, and moves the file to the live folder.
Agent 2 — Geometry Optimization Agent
**Responsibility:** Write, test, and debug Python geometry functions.
**Constraint:** Every function written must have unit tests using three fixture geometries: `square_plot.geojson` (20m × 20m), `l_shaped_plot.geojson`, and `narrow_lane_4m.geojson`. Tests run automatically. Agent does not declare a function complete until all three tests pass.
**Output location:** `/backend/engine/` for functions, `/backend/tests/` for tests.
Agent 3 — Visual QA Agent
**Responsibility:** Automated browser testing of the frontend.
**Process:** Opens the running app in a browser, loads test plot geometries, triggers layout generation, drags sliders, checks that:
- All 5 layout options render without overlapping polygons
- Slider changes update the map overlay within 500ms
- Compliance violations appear in red with tooltip text
- Before/After toggle switches correctly
- PDF export downloads a valid file
**Output:** Screenshot report + pass/fail list. Any failure is logged with screenshot and line reference.
Agent 4 — Copilot Agent
**The Golden Rule for this agent:** It translates natural language to structured JSON. It never calculates areas, distances, or counts. It never outputs coordinates.
**Example:**
- User: "I want more parking but I need at least one tree near the entrance"
- Agent output (JSON sent to geometry engine):
```json
{
  "intent": "modify_layout",
  "constraint_updates": {
    "parking_weight": "increase",
    "preserve_elements": [{"type": "tree", "location_hint": "entrance", "min_count": 1}]
  },
  "explanation_for_user": "Increasing parking allocation while preserving at least one tree near the entrance zone."
}
```
The geometry engine processes the JSON. The agent then phrases the result back to the user in plain language.
**Context passed to every LLM call:** Active layout metrics JSON + active regulation JSON + a system prompt that says: "You are VinyasGen's planning assistant. You help government urban planners and architects design better Indian streets and galis. You do not calculate geometry — you translate user requests into structured constraint updates. You speak plainly and professionally, like a helpful colleague, not like a chatbot."
Agent 5 — Report Content Agent
**Responsibility:** Generate the plain-language descriptive text sections of the PDF report.
**Input:** Final layout metrics JSON + compliance results JSON + project metadata.
**Output:** Structured text for: project summary paragraph, compliance narrative, impact summary, phasing justification narrative.
**Constraint:** Every factual claim (areas, counts, distances, costs) must be directly sourced from the input JSON. The agent must not invent or round numbers. Numbers in the generated text must exactly match the metrics JSON.
---
14. The AI Copilot
A persistent chat widget in the right panel of the UI. Powered by Agent 4.
**Capabilities:**
- "Why is this zone highlighted red?" → Fetches the compliance result for the zone the user clicked and explains it in plain language with the bylaw citation
- "How can I fit more parking here?" → Translates to constraint update JSON, triggers re-generation, reports result
- "What does this thermal score mean?" → Explains the calculation using the actual numbers from the active layout
- "Is this layout ready to submit?" → Runs a summary check across all compliance, emergency access, and monsoon test results and gives a go/no-go with specific issues to resolve
- "Summarize this proposal for my report" → Triggers Report Content Agent to generate the summary paragraph
**What the Copilot cannot do (hard-blocked):**
- Output coordinates, areas, or distance numbers as "calculations" — it can only report numbers that came from the geometry engine
- Modify the layout directly — it can only generate constraint update JSON that the user then reviews and applies
- Override a compliance violation or emergency access failure
---
15. Frontend Architecture & UX
15.1 Screen Layout
```
┌────────────────────────────────────────────────────────────┐
│ HEADER: VinyasGen logo | City Selector | Project Name | [New Project] [Ward View] │
├──────────┬────────────────────────────────┬────────────────┤
│          │                                │                │
│  LEFT    │         MAP CANVAS             │  RIGHT PANEL   │
│  PANEL   │   (MapLibre + Deck.gl)         │                │
│          │                                │  ┌──────────┐  │
│ Kit-of-  │  [Before] ●────── [After]      │  │ Sliders  │  │
│ Parts    │                                │  ├──────────┤  │
│          │  ┌─────────────────────────┐   │  │Compliance│  │
│ Layer    │  │ Layout Options Carousel │   │  ├──────────┤  │
│ Toggles  │  │ [A][B][C][D][E]         │   │  │ Impact   │  │
│          │  └─────────────────────────┘   │  │Dashboard │  │
│ Site     │                                │  ├──────────┤  │
│ Analysis │  [Draw] [Upload] [Detect       │  │ Copilot  │  │
│ Tools    │   Encroachments] [Run Tests]   │  │  Chat    │  │
│          │                                │  └──────────┘  │
└──────────┴────────────────────────────────┴────────────────┘
```
15.2 UX Principles (Apply to Every Component Built)
**Minimal:** Generous whitespace. Only show controls relevant to the current workflow step. Advanced options hidden behind "Show more" expand. No dense toolbars. No technical jargon visible to the user — "Ground Coverage %" not "GCR," "Green Cover" not "Permeable Surface Coefficient."
**Smooth:** Every layout change animates (200ms transition on Deck.gl layers). Loading states use skeleton screens, not spinners. No full page reloads. Slider changes debounce at 150ms. Target API response: under 300ms for slider updates, under 2s for full layout regeneration.
**Accessible for all users:** 
- WCAG AA contrast minimum on all text
- Every icon has a visible text label or tooltip — no icon-only controls
- Sliders and toggles instead of raw numeric text inputs wherever possible
- Colour coding always paired with text/icon (for colour-blind users: red violation = red + ⚠️ icon + text, not colour alone)
- Fully responsive — works on tablet and mobile browser (government planners review on tablets in the field)
- Keyboard navigable throughout
- Proper ARIA labels on all map controls and panel elements
**Professional:** The visual aesthetic is clean, light, and authoritative — not playful. This tool produces government submission documents. It should look like it belongs in that context. White background, muted grey basemap, clean sans-serif typography (Inter or similar), no gradients or decorative elements. The data and layouts are the visual focus, not the UI chrome.
15.3 Technology Stack (Frontend)
| Technology | Version | Purpose |
|---|---|---|
| Next.js | 14+ | App framework, TypeScript, App Router |
| TypeScript | 5+ | Type safety across all components |
| Tailwind CSS | 3+ | Utility-first styling |
| MapLibre GL JS | 4+ | Free, open-source base map (no usage caps) |
| react-map-gl | 7+ | React wrapper for MapLibre |
| @maplibre/maplibre-gl-draw | Latest | Polygon/point drawing tools on map |
| Deck.gl | 8+ | High-performance GeoJSON vector overlays |
| Three.js | r128 | 3D presentation mode (Phase 4) |
| Turf.js | 6+ | Lightweight client-side geometry preview |
| Zustand | 4+ | Global state management |
| react-pdf | Latest | In-browser PDF preview |
15.4 Zustand Store Shape
```typescript
interface VinyasGenStore {
  // Project
  activeProjectId: string | null;
  wardProjectId: string | null;
  city: string;
  zoneCode: string;
  siteType: 'road' | 'gali' | 'empty_plot' | 'public_space' | null;
  // Boundaries
  officialBoundary: GeoJSON.Feature | null;
  actualBoundary: GeoJSON.Feature | null;
  // Layouts
  layoutOptions: LayoutResponse[];
  activeLayoutId: string | null;
  activeLayoutGeoJSON: GeoJSON.FeatureCollection | null;
  // Controls
  sliders: { parkingDensity: number; greenCoverPct: number; pedestrianPriority: number };
  materialChoices: Record<string, string>; // zone_id → material_id
  // Analysis results
  complianceResults: ComplianceCheck[];
  emergencyAccessResult: AccessCheckResult | null;
  monsoonTestResult: MonsoonTestResult | null;
  encroachments: EncroachmentFeature[];
  // UI
  beforeAfterMode: 'before' | 'after';
  activeTab: 'layout' | 'analysis' | 'encroachment' | 'phasing';
  mapMode: '2d' | '3d';
  // Actions (all are async, call API and update state)
  generateLayouts: () => Promise<void>;
  updateSlider: (key: string, value: number) => void;
  runEmergencyCheck: () => Promise<void>;
  runMonsoonTest: () => Promise<void>;
  runEncroachmentDetection: (mode: 'manual' | 'cv_map' | 'cv_upload') => Promise<void>;
  generateReport: (reportType: string) => Promise<void>;
}
```
---
16. Backend Architecture
16.1 Technology Stack
| Technology | Purpose |
|---|---|
| Python 3.11+ | Core language |
| FastAPI | REST API framework with automatic OpenAPI docs |
| Shapely 2.0+ | 2D geometry operations |
| PyProj 3+ | CRS conversions (WGS84 ↔ UTM43N) |
| GeoPandas | File reading (Shapefile, GeoJSON), batch operations |
| PyClipper | Complex polygon offsetting for non-convex shapes |
| Google OR-Tools | CP-SAT solver for parking optimization |
| PyTorch | Mask R-CNN inference for CV encroachment detection (Phase 3) |
| SQLAlchemy | ORM for SQLite (Phase 1) → PostgreSQL (Phase 5) |
| Pydantic v2 | Request/response validation |
| WeasyPrint | HTML-to-PDF report generation |
| PyPDF2 / pdfplumber | PDF text extraction for Regulation Researcher Agent |
| Uvicorn | ASGI server |
16.2 Module Structure
```
backend/
├── main.py                     # FastAPI app, CORS, route mounting
├── routes/
│   ├── layout_routes.py        # /api/layout/*
│   ├── regulation_routes.py    # /api/regulations/*
│   ├── encroachment_routes.py  # /api/encroachment/*
│   ├── analysis_routes.py      # /api/analysis/*
│   ├── report_routes.py        # /api/report/*
│   ├── project_routes.py       # /api/project/*
│   └── copilot_routes.py       # /api/copilot/*
├── engine/
│   ├── geo_utils.py            # CRS conversions — imported by all engines
│   ├── geometry_engine.py      # Core generative geometry
│   ├── parking_optimizer.py    # OR-Tools stall packing
│   ├── compliance_checker.py   # Regulation validation
│   ├── access_checker.py       # Emergency access geometry
│   ├── encroachment.py         # Boundary comparison, manual mode
│   ├── cv_detector.py          # Mask R-CNN inference (Phase 3)
│   ├── monsoon_test.py         # Hydrology calculation
│   ├── lighting_engine.py      # Pole placement optimization
│   ├── drainage_engine.py      # Drain slot placement and sizing
│   ├── phase_planner.py        # Cost aggregation by phase
│   └── report_generator.py     # WeasyPrint PDF assembly
├── models/
│   ├── schemas.py              # Pydantic request/response models
│   └── db_models.py            # SQLAlchemy table models
├── agents/
│   ├── regulation_researcher/
│   ├── geometry_optimizer/
│   ├── visual_qa/
│   ├── copilot/
│   └── report_content/
├── tests/
│   ├── test_geometry_engine.py
│   ├── test_parking_optimizer.py
│   ├── test_compliance_checker.py
│   ├── test_access_checker.py
│   ├── test_monsoon_test.py
│   ├── test_lighting_engine.py
│   └── fixtures/
│       ├── square_plot.geojson
│       ├── l_shaped_plot.geojson
│       └── narrow_lane_4m.geojson
├── requirements.txt
└── .env.example
```
16.3 CORS Configuration (Required — Without This the Frontend Cannot Call the Backend)
```python
from fastapi.middleware.cors import CORSMiddleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "https://vinyasgen.vercel.app"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```
---
17. API Specification (Core Endpoints)
All endpoints return JSON. All geometry in WGS84 GeoJSON. All distances in metres. All areas in square metres. All costs in INR.
| Method | Endpoint | Input | Output |
|---|---|---|---|
| POST | /api/layout/generate | plot_geojson, city, zone_code, site_type, width_m | 5 layout options with GeoJSON + metrics + compliance |
| POST | /api/layout/update | layout_id, slider_values, material_choices | Updated single layout |
| GET | /api/layout/{id} | — | Saved layout |
| GET | /api/regulations/{city}/{zone} | — | Effective constraints (base + incentives) |
| POST | /api/encroachment/calculate | official_geojson, actual_geojson | Encroachment polygons + measurements |
| POST | /api/encroachment/detect | mode, image_data, official_geojson | CV-detected encroachment polygons + confidence |
| POST | /api/encroachment/verify | encroachment_id, verified: bool | Updates verification status |
| POST | /api/analysis/emergency-access | layout_id | Pass/fail + violation locations |
| POST | /api/analysis/monsoon | layout_id, rainfall_mm_hr | Stress test result + suggestions |
| POST | /api/analysis/lighting | layout_id, existing_poles | Optimal pole positions + flagged poles |
| POST | /api/analysis/drainage | layout_id, slope_direction | Drain slot recommendations |
| POST | /api/report/generate | layout_id, report_type, preparer_info | PDF file (download link) |
| POST | /api/project/ward/create | ward_name, city, authority, planner | Ward project record |
| GET | /api/project/ward/{id}/sites | — | All sites in ward + status + summary metrics |
| POST | /api/copilot/message | project_id, layout_id, message | AI reply + optional constraint_updates JSON |
---
18. Repository & Folder Structure
```
vinyasgen/
├── README.md
├── PRIVACY_CONSTRAINTS.md          # Encroachment anonymity rules — agents must read this
├── .gitignore
├── .env.example
├── docker-compose.yml              # Optional local dev convenience
│
├── frontend/
│   ├── app/
│   │   ├── page.tsx                # Main map view
│   │   ├── layout.tsx              # App shell
│   │   └── ward/page.tsx           # Ward project manager view
│   ├── components/
│   │   ├── map/
│   │   │   ├── MapLibreBaseMap.tsx
│   │   │   ├── DeckGLOverlay.tsx
│   │   │   ├── DrawControl.tsx
│   │   │   └── BeforeAfterToggle.tsx
│   │   ├── panels/
│   │   │   ├── LeftPanel.tsx
│   │   │   ├── RightPanel.tsx
│   │   │   ├── ConstraintSliders.tsx
│   │   │   ├── ComplianceStatus.tsx
│   │   │   ├── ImpactDashboard.tsx
│   │   │   ├── LayoutOptionsCarousel.tsx
│   │   │   ├── MonsoonTestPanel.tsx
│   │   │   ├── LightingPanel.tsx
│   │   │   └── PhasingPanel.tsx
│   │   ├── copilot/
│   │   │   └── CopilotChat.tsx
│   │   └── ward/
│   │       └── WardProjectMap.tsx
│   ├── store/
│   │   └── useVinyasGenStore.ts
│   ├── lib/
│   │   ├── apiClient.ts
│   │   └── geoHelpers.ts
│   ├── styles/
│   ├── public/
│   ├── package.json
│   └── tailwind.config.ts
│
├── backend/
│   └── [as defined in Section 16.2]
│
├── data/
│   ├── regulations/
│   │   ├── pending_review/         # Agent output — awaits human approval
│   │   ├── noida/
│   │   │   └── residential_group_housing.json
│   │   ├── delhi/
│   │   │   └── residential_colony.json
│   │   └── gurgaon/
│   │       └── group_housing.json
│   ├── materials/
│   │   └── indian_paving_materials.json
│   ├── kit_of_parts/
│   │   ├── street_furniture.json
│   │   └── green_elements.json
│   └── cost_reference/
│       └── inr_unit_costs.json
│
├── docs/
│   ├── VinyasGen_v2_Manifesto.md   # This document
│   └── PHASE_LOG.md                # Agent logs current phase and completion status here
└── ml_models/                      # Phase 3
    └── encroachment_detector/
        ├── model_weights/
        └── inference.py
```
---
19. Free Stack — Every Tool Used
| Category | Tool | Free Basis |
|---|---|---|
| Frontend framework | Next.js | Open-source, MIT |
| Styling | Tailwind CSS | Open-source, MIT |
| Map rendering | MapLibre GL JS | Open-source, BSD — no usage caps, no API key for the library |
| Map tiles | OSM-based free tile provider | Free tier — use MapTiler free tier or similar |
| Draw tools | @maplibre/maplibre-gl-draw | Open-source |
| Vector overlays | Deck.gl | Open-source, Apache 2.0 |
| Client geometry | Turf.js | Open-source, MIT |
| State management | Zustand | Open-source, MIT |
| Backend framework | FastAPI | Open-source, MIT |
| 2D geometry | Shapely | Open-source, BSD |
| CRS conversion | PyProj | Open-source, MIT |
| Spatial data | GeoPandas | Open-source, BSD |
| Polygon offsetting | PyClipper | Open-source, MIT |
| Optimization | Google OR-Tools | Open-source, Apache 2.0 |
| ML inference | PyTorch (CPU inference) | Open-source, BSD |
| ML model | Mask R-CNN / SpaceNet pretrained | Open weights |
| PDF generation | WeasyPrint | Open-source, BSD |
| PDF reading | pdfplumber | Open-source, MIT |
| Database (MVP) | SQLite | Built into Python |
| Database (scale) | PostgreSQL + PostGIS | Open-source |
| ORM | SQLAlchemy | Open-source, MIT |
| 3D visualization | Three.js r128 | Open-source, MIT |
| Frontend hosting | Vercel | Free Hobby tier |
| Backend hosting | Render | Free Web Service tier |
| CI/CD | GitHub Actions | Free for public repos |
| LLM (Copilot) | Free-tier LLM API (verify current provider quotas) | Free tier |
| Version control | GitHub | Free |
**Zero-cost checklist for any new dependency:** (1) Is there an open-source alternative? Use it. (2) If paid service, does it have a sufficient free tier? (3) Are usage limits understood? (4) Is the API key stored in `.env`, never committed?
---
20. Phase 1 — Foundation (Weeks 1–3)
**Goal:** A working app where a government planner can draw a gali or road boundary on a map, select a city/zone, and see the regulation constraints loaded. Health-check round trip confirmed. No layout generation yet.
What to Build
**Backend:**
- Initialize FastAPI project with folder structure from Section 18
- `main.py` with CORS middleware configured for localhost:3000
- `GET /api/health` returning `{"status": "ok", "version": "0.1.0", "timestamp": "<ISO8601>"}`
- `GET /api/regulations/{city}/{zone_code}` that reads and returns the matching JSON file from `/data/regulations/`
- `geo_utils.py` with `to_utm()` and `to_wgs84()` functions
- `requirements.txt` with all backend dependencies
- SQLite database initialized with all tables from Section 8.1
- Three regulation JSON files created (noida/residential_group_housing, delhi/residential_colony, gurgaon/group_housing) with placeholder values clearly marked `"review_status": "pending_review"` — values are illustrative and flagged for human verification
- `indian_paving_materials.json` with all 9 materials from Section F14
- `inr_unit_costs.json` with cost data for all Kit-of-Parts elements
**Frontend:**
- Initialize Next.js (TypeScript, Tailwind, App Router) project
- MapLibre GL JS integrated via react-map-gl
- Map centred on Noida Sector 62 (28.6139°N, 77.3910°E) at zoom 16
- @maplibre/maplibre-gl-draw installed and working — user can draw a polygon on the map and the GeoJSON is logged to console
- City selector dropdown (Noida / Delhi / Gurgaon) in header
- Zone type selector (updates based on city selection)
- When city + zone selected: frontend calls `GET /api/regulations/{city}/{zone}` and displays a simple sidebar card showing the 5 key constraints (FAR, setbacks, parking norms, green area %, max height)
- `lib/apiClient.ts` with base fetch wrapper (handles errors, returns typed responses)
- Zustand store initialized with all state fields from Section 15.4 (most empty at this stage)
- `PRIVACY_CONSTRAINTS.md` in repository root
Phase 1 Tests (All Must Pass Before Phase 2 Starts)
1. `GET /api/health` returns 200 with correct JSON
2. `GET /api/regulations/noida/residential_group_housing` returns the full JSON
3. Frontend loads without errors, map renders at correct location
4. User can draw a polygon on the map and GeoJSON appears in browser console
5. City selector + zone selector update the sidebar constraint card correctly
6. Changing city to Delhi loads Delhi regulations, not Noida
7. `geo_utils.py` unit test: convert a known Noida Sector 62 coordinate to UTM and back, verify round-trip error < 1cm
**Phase 1 deliverable:** A working map with boundary drawing and regulation display. No layout generation. This is the "scaffolding is up" milestone.
---
21. Phase 2 — Core Engines (Weeks 4–8)
**Goal:** Full Tier 1 feature set working end-to-end. User can draw a boundary, generate 5 layout options, edit with sliders, see compliance results, run emergency access check, optimize parking, and download a basic PDF report.
What to Build
**Backend — Geometry Engine:**
- `geometry_engine.py`: all functions from Section 10.1 implemented and tested
- `parking_optimizer.py`: OR-Tools CP-SAT solver with two-wheeler-first priority
- `compliance_checker.py`: all checks for all constraints in the regulation JSON
- `access_checker.py`: emergency access geometry checks from Section 12.1
- `scoring.py`: impact metrics calculation (parking count, green%, path length, thermal score)
**Backend — API Endpoints:**
- `POST /api/layout/generate`: full pipeline (normalize → load regulations → generate 5 options → run compliance → run access check → return all 5)
- `POST /api/layout/update`: recompute single layout with new slider values
- `POST /api/analysis/emergency-access`: standalone access check
- `POST /api/project/create`: create project record in SQLite
- `POST /api/report/generate`: basic PDF using WeasyPrint with all required elements from F11
**Frontend — Main Interaction:**
- After user draws boundary and selects city/zone: [Generate Layouts] button
- Loading state while API computes (skeleton cards in carousel)
- Layout Options Carousel: 5 options shown as thumbnails with objective label and key metrics
- Deck.gl vector overlay: renders the active layout GeoJSON with correct colours from Section 10.2
- Before/After toggle functional
- ConstraintSliders.tsx: three sliders wired to debounced `POST /api/layout/update`
- ComplianceStatus.tsx: shows all checks with colour coding and citation text
- ImpactDashboard.tsx: live metrics updating on every layout change
- Emergency access result shown as a coloured band on the map + pass/fail indicator
**Backend — Encroachment (Manual Mode):**
- `encroachment.py`: boundary difference calculation, spatial clustering, anonymised labelling
- `POST /api/encroachment/calculate`: takes official_geojson + actual_geojson, returns encroachment polygons
- Frontend: two-boundary drawing mode, encroachment result overlay in red, reclamation width calculation shown
Phase 2 Tests (All Must Pass Before Phase 3 Starts)
1. Generate layouts for square_plot, l_shaped_plot, and narrow_lane_4m fixtures — all 5 options return valid, non-overlapping GeoJSON
2. Slider changes return updated layout within 500ms (measured)
3. Compliance checker correctly flags ground coverage violation when forced by extreme slider
4. Compliance checker correctly flags setback violation when building polygon overlaps setback zone
5. Access checker correctly fails a layout where no 4.5m clear path exists
6. OR-Tools parking optimizer returns valid non-overlapping stall arrangement for all three fixture geometries, terminates within 10 seconds
7. PDF report generates and downloads successfully, contains all required elements including legal disclaimer
8. Manual encroachment calculation: known encroachment of 2.0m on a test gali returns correct depth measurement within ±0.1m
9. Visual QA Agent: all checks from Section 13 Agent 3 pass
---
22. Phase 3 — Differentiator Features (Weeks 9–14)
**Goal:** All Tier 2 features working. This is what makes VinyasGen unique. Every feature in this phase has no equivalent in any other tool for Indian cities.
What to Build
**CV Encroachment Detection:**
- `ml_models/encroachment_detector/inference.py`: Mask R-CNN inference pipeline
- Load pretrained SpaceNet weights, run on 512×512 tiles of input image
- Polygonize output masks to Shapely polygons
- Geolocation: align detected polygons to map coordinates using official boundary as anchor
- `cv_detector.py`: wraps inference pipeline, handles the three input modes (map tile capture, uploaded image, cadastral overlay)
- `POST /api/encroachment/detect`: full CV pipeline endpoint
- Frontend: "Detect Encroachments" button, mode selector (map / upload / cadastral), confidence indicator, per-flag Verify/Dismiss buttons
- All privacy constraints from PRIVACY_CONSTRAINTS.md enforced at data model level
**Indian Material Thermal Selector:**
- Material picker UI: dropdown per zone in the layout (footpath, vehicle lane, parking, green strip)
- Materials loaded from `indian_paving_materials.json`
- Impact dashboard Thermal Score updates immediately on material change
- Material choices stored in layout_options.material_choices JSON column
- Monsoon runoff coefficient per material feeds into monsoon test
**Monsoon Stress Test:**
- `monsoon_test.py`: full hydrology calculation from Section 12.2
- `POST /api/analysis/monsoon`: endpoint
- Frontend: MonsoonTestPanel.tsx — dedicated tab in Impact Dashboard
- Visual: zones coloured by runoff contribution (high runoff = warm red, low = cool blue)
- "Run Monsoon Test" button, result shows max handleable intensity vs design storm, suggestions for improvement
**Drainage Slot Indicator:**
- `drainage_engine.py`: drain placement logic from F16
- Integrated into cross-section regenerator — drain slot appears automatically
- Drain type selector: bioswale / covered channel / open channel
- Cost per running metre shown from `inr_unit_costs.json`
- Drain position and dimensions feed into monsoon_test.py
**Street Light Placement Engine:**
- `lighting_engine.py`: pole coverage geometry from Section 12.3
- `POST /api/analysis/lighting`: endpoint
- Frontend: LightingPanel.tsx in left panel
- Map overlay: coverage circles as semi-transparent circles, gap zones as dark grey areas
- Flagged existing poles shown with issue tooltip
- Utility Infrastructure Layer: blank placeholder layer where users mark transformers/cables
**Phased Implementation Planner:**
- `phase_planner.py`: cost aggregation per phase
- Frontend: PhasingPanel.tsx — element list with phase selector per element
- Map overlay: Phase 1 = solid, Phase 2 = hatched pattern, Phase 3 = dotted
- PDF report updated to include phasing table and phased layout diagram
**Multi-Site Ward Project Manager:**
- Ward project creation and management in SQLite
- Ward-level map view: WardProjectMap.tsx showing all sites colour-coded by status
- Summary metrics aggregation across all sites in a ward
- Ward-level PDF report
Phase 3 Tests
1. CV detector correctly identifies at least 80% of manually annotated building footprints in 5 test images of NCR galis (precision/recall measurement)
2. CV detector returns correct confidence level based on image resolution metadata
3. Monsoon test: for a layout with known drain capacity and surface areas, result matches hand-calculated value within 5%
4. Monsoon test FAIL correctly suggests adding a drain segment when capacity is insufficient
5. Material change from concrete to Shahabad stone updates thermal score by correct delta (3–4°C)
6. Lighting engine produces zero gap zones for a straight 50m gali with standard pole spacing
7. Lighting engine correctly flags a pole placed inside a footpath zone
8. Phasing: assigning all elements to Phase 1 produces same total cost as unphased layout ± 1%
9. Ward project: creating 3 sites and updating their statuses shows correct colour coding on ward map
---
23. Phase 4 — Intelligence Layer (Weeks 15–20)
**Goal:** 3D presentation mode, full AI Copilot, advanced Regulation Researcher Agent automation, community consultation layer.
What to Build
**3D Presentation Mode:**
- Three.js integration alongside existing Deck.gl layer
- Map mode toggle in header: [2D Plan] [3D View]
- In 3D mode: zone polygons extruded to heights (adjacent buildings from OSM building height tag, walls at 0.3m, poles at 7m)
- Street canyon visualization: shows vertical walls of buildings on either side of gali
- Sun-shadow simulation: user picks date + time, shadow polygons cast by extruded buildings shown on the cross-section
- Export: static PNG render of 3D view for inclusion in PDF report
**Regulation Researcher Agent (Automated Pipeline):**
- Python script that monitors a designated folder for new PDF drops
- Runs extraction pipeline, writes to pending_review, sends notification
- Human review dashboard: list of pending regulation files with source citations for easy verification
**Full Copilot Integration:**
- Copilot connected to all analysis modules — can query compliance, monsoon, access, lighting results
- "Is this ready to submit?" command runs all checks and returns structured go/no-go
- Copilot suggestions trigger constraint update JSON sent to geometry engine
- Conversation history maintained within session (not across sessions)
**Community Consultation Layer:**
- Shareable link generation for finalized layouts
- Read-only map view for recipients (Before/After toggle, impact metrics, no editing)
- Structured feedback form: approve / suggest change / flag concern
- Feedback aggregation in project dashboard
- Consultation summary export for PDF report appendix
Phase 4 Tests
1. 3D view renders without THREE.js errors for all three fixture geometries
2. Sun-shadow simulation produces shadows in correct direction for 12 June at 14:00
3. Copilot "is this ready to submit?" correctly identifies a layout with a pending emergency access violation
4. Regulation Researcher Agent extracts FAR, setbacks, parking norms from a test PDF with ≥90% field accuracy
5. Shareable link renders correctly in a second browser without the original user's session
---
24. Phase 5 — Polish & Scale (Weeks 21–26)
**Goal:** Production-ready deployment, performance optimization, PostgreSQL + PostGIS migration, full test coverage, documentation.
What to Build
- Migrate SQLite to PostgreSQL + PostGIS (spatial indexes on geometry columns)
- Add spatial indexing to speed up encroachment intersection queries on large datasets
- Add `/api/project/ward/{id}/export` ward-level bulk PDF export
- Add user authentication (simple email + password, JWT tokens) for government agency accounts
- Add `/api/analysis/lighting` integration into main PDF report template
- Pocket Park / Dead Space Converter (F22) — detects dead spaces automatically and suggests Kit-of-Parts placements
- Vertical Green Finder (F21) — narrow gali detection and wall planter suggestions
- Performance: layout generation target < 500ms for standard site, < 2s for large sector road
- Load test: 50 concurrent users without degradation
- Comprehensive API documentation (auto-generated by FastAPI, manually reviewed)
- Deployment: Vercel (frontend) + Render or Railway (backend) with environment variables configured
- GitHub Actions CI/CD: test suite runs on every push, blocks deploy on failure
---
25. Testing Strategy per Phase
Fixture Geometries (Create These First in Phase 1, Use in All Phases)
**`square_plot.geojson`:** A 20m × 20m square plot in Noida Sector 62. Known area: 400 sqm. Used to verify area calculations and setback buffers.
**`l_shaped_plot.geojson`:** An L-shaped plot typical of a corner plot in an Indian colony. Tests how the engine handles concave shapes and non-standard setback application.
**`narrow_lane_4m.geojson`:** A 4m-wide, 60m-long gali centerline. Tests the minimum-width cross-section allocation and emergency access failure (4m is below the 4.5m minimum clear width).
**`sector_road_12m.geojson`:** A 12m-wide, 200m-long sector road. Tests the full cross-section regenerator at a width that can accommodate all zone types.
Test Approach per Module
Every engine module (`geometry_engine.py`, `parking_optimizer.py`, etc.) has a corresponding test file in `/backend/tests/`. Every test file must test each fixture geometry. Tests run with `pytest` from the backend directory. No module is declared complete until all its tests pass on all fixture geometries.
---
26. Deployment per Phase
**Phase 1–2:** Local development only. Frontend on `localhost:3000`, backend on `localhost:8000`. SQLite database as a file in `/backend/`.
**Phase 3:** Deploy to Vercel (frontend) and Render free tier (backend). Environment variables configured in both platforms. SQLite database on Render's ephemeral filesystem — acceptable for demo, not for persistent production data.
**Phase 4:** Same deployment, add environment variable for LLM API key (Copilot).
**Phase 5:** Migrate backend to PostgreSQL (Render's free tier offers a managed Postgres instance). Add user authentication. Production deployment with proper environment separation (dev / staging / production).
---
27. Legal Disclaimer Requirements
The following disclaimer text is mandatory and must appear in three places:
**1. In the UI:** A persistent small banner at the bottom of every screen. Never hideable. Font size minimum 12px. Grey text, not alarming but clearly visible.
**2. In every generated PDF:** On the first page, below the title and before any content. Slightly larger than body text. Framed with a thin border to distinguish it.
**3. In the Copilot system prompt:** The LLM is told this in every API call: "You are a decision-support tool. Always remind users that your outputs are indicative only and require verification with the relevant municipal authority."
**The exact disclaimer text:**
> VinyasGen is a decision-support and visualization tool. All outputs — layouts, compliance results, cost estimates, and encroachment flags — are indicative only, based on digitized regulatory data, and do not constitute statutory approval, legal measurement, or enforcement action. All proposals must be verified with the relevant municipal authority before implementation. Encroachment flags are potential indicators requiring field verification — they do not constitute legal evidence of unauthorized construction.
---
28. Appendix
28.1 First Three Tasks for Any Agent Starting Phase 1
Given to Antigravity or any coding agent as the opening instruction:
> "You are beginning Phase 1 of VinyasGen as defined in the manifesto at docs/VinyasGen_v2_Manifesto.md. Complete these three tasks in order. Do not start Task 2 until Task 1 passes its test. Do not start Task 3 until Task 2 passes its test.
>
> Task 1: Initialize the frontend (Next.js + TypeScript + Tailwind + App Router) and backend (FastAPI) with the exact folder structure in Section 18. Add CORS middleware to main.py allowing localhost:3000. Create GET /api/health endpoint. Confirm the frontend can call it and display 'Backend: OK' on screen.
>
> Task 2: In frontend, integrate react-map-gl with MapLibre GL JS using a free vector tile style. Centre the map on 28.6139°N, 77.3910°E at zoom 16. Install @maplibre/maplibre-gl-draw. Confirm a user can draw a polygon and the GeoJSON is logged to console.
>
> Task 3: In backend, create geo_utils.py with to_utm() and to_wgs84() using pyproj. Write unit tests using a known Noida Sector 62 coordinate. Confirm round-trip conversion error is less than 1cm. Create the three regulation JSON files with placeholder values and review_status: pending_review. Create indian_paving_materials.json with all 9 materials from Section F14 of the manifesto. Confirm GET /api/regulations/noida/residential_group_housing returns the JSON correctly."
28.2 Sample `indian_paving_materials.json`
```json
{
  "version": "1.0",
  "last_updated": "2026-07-01",
  "materials": [
    {
      "material_id": "grey_concrete",
      "name": "Standard Grey Concrete",
      "temp_reduction_c": 0,
      "cost_inr_per_sqm": { "low": 280, "expected": 350, "high": 450 },
      "availability": "universal",
      "maintenance_level": "low",
      "runoff_coefficient": 0.90,
      "thermal_mass": "high",
      "notes": "Baseline material. High heat absorption."
    },
    {
      "material_id": "shahabad_stone",
      "name": "Shahabad Stone (Natural)",
      "temp_reduction_c": 3.5,
      "cost_inr_per_sqm": { "low": 480, "expected": 550, "high": 650 },
      "availability": "north_india",
      "maintenance_level": "low",
      "runoff_coefficient": 0.70,
      "thermal_mass": "medium",
      "notes": "Naturally porous. Widely used in Delhi NCR. Cools significantly."
    },
    {
      "material_id": "kota_stone",
      "name": "Kota Stone (Natural)",
      "temp_reduction_c": 2.5,
      "cost_inr_per_sqm": { "low": 420, "expected": 480, "high": 560 },
      "availability": "most_cities",
      "maintenance_level": "low",
      "runoff_coefficient": 0.75,
      "thermal_mass": "medium",
      "notes": "Rajasthan origin, widely available. Good thermal performance."
    },
    {
      "material_id": "ilc_interlocking_pavers",
      "name": "ILC Interlocking Brick Pavers (Red/Buff)",
      "temp_reduction_c": 2.5,
      "cost_inr_per_sqm": { "low": 520, "expected": 600, "high": 720 },
      "availability": "universal",
      "maintenance_level": "medium",
      "runoff_coefficient": 0.60,
      "thermal_mass": "medium",
      "notes": "Gaps between pavers allow some drainage. Standard municipal choice."
    },
    {
      "material_id": "sand_set_brick_pavers",
      "name": "Sand-Set Clay Brick Pavers",
      "temp_reduction_c": 3.5,
      "cost_inr_per_sqm": { "low": 460, "expected": 520, "high": 620 },
      "availability": "universal",
      "maintenance_level": "medium",
      "runoff_coefficient": 0.55,
      "thermal_mass": "low",
      "notes": "Sand bed allows infiltration. Good for narrow footpaths."
    },
    {
      "material_id": "cool_coat_asphalt",
      "name": "Cool-Coat Reflective Asphalt Coating",
      "temp_reduction_c": 6.5,
      "cost_inr_per_sqm": { "low": 150, "expected": 180, "high": 240 },
      "availability": "major_cities",
      "maintenance_level": "high",
      "runoff_coefficient": 0.85,
      "thermal_mass": "medium",
      "notes": "Applied over existing asphalt. High temp reduction but reapplication needed every 3-5 years."
    },
    {
      "material_id": "compressed_earth_blocks",
      "name": "Compressed Stabilized Earth Blocks",
      "temp_reduction_c": 4.5,
      "cost_inr_per_sqm": { "low": 380, "expected": 420, "high": 500 },
      "availability": "regional",
      "maintenance_level": "medium",
      "runoff_coefficient": 0.50,
      "thermal_mass": "low",
      "notes": "Low embodied carbon. Good for green-rated projects."
    },
    {
      "material_id": "grass_gravel_grid",
      "name": "Grass/Gravel Parking Grid",
      "temp_reduction_c": 7.0,
      "cost_inr_per_sqm": { "low": 620, "expected": 700, "high": 850 },
      "availability": "universal",
      "maintenance_level": "high",
      "runoff_coefficient": 0.20,
      "thermal_mass": "low",
      "notes": "Best thermal and drainage performance. Suitable for low-traffic parking only."
    },
    {
      "material_id": "permeable_concrete",
      "name": "Permeable Concrete",
      "temp_reduction_c": 5.0,
      "cost_inr_per_sqm": { "low": 750, "expected": 850, "high": 1000 },
      "availability": "major_cities",
      "maintenance_level": "high",
      "runoff_coefficient": 0.25,
      "thermal_mass": "medium",
      "notes": "Excellent drainage and thermal performance. Higher cost. Requires maintenance to prevent clogging."
    }
  ]
}
```
28.3 Sample `inr_unit_costs.json` (Partial)
```json
{
  "version": "1.0",
  "last_updated": "2026-07-01",
  "currency": "INR",
  "items": {
    "rwa_bench_precast": { "low": 3500, "expected": 4500, "high": 6500, "unit": "per_unit" },
    "bollard_ms_painted": { "low": 600, "expected": 900, "high": 1400, "unit": "per_unit" },
    "parking_stall_marking_2w": { "low": 150, "expected": 250, "high": 400, "unit": "per_stall" },
    "parking_stall_marking_car": { "low": 300, "expected": 450, "high": 700, "unit": "per_stall" },
    "tree_sapling_with_guard_pit": { "low": 800, "expected": 1200, "high": 2000, "unit": "per_unit" },
    "open_drain_concrete_300mm": { "low": 800, "expected": 1100, "high": 1500, "unit": "per_running_m" },
    "covered_drain_with_grating": { "low": 1200, "expected": 1600, "high": 2200, "unit": "per_running_m" },
    "bioswale_tree_trench": { "low": 900, "expected": 1300, "high": 1900, "unit": "per_running_m" },
    "street_light_pole_7m_led": { "low": 18000, "expected": 24000, "high": 32000, "unit": "per_pole_installed" },
    "light_pole_relocation": { "low": 8000, "expected": 12000, "high": 18000, "unit": "per_pole" },
    "waste_collection_bay_small": { "low": 15000, "expected": 22000, "high": 35000, "unit": "per_unit" },
    "speed_breaker_rubber": { "low": 2500, "expected": 3500, "high": 5000, "unit": "per_unit" },
    "directional_signage": { "low": 1800, "expected": 2500, "high": 4000, "unit": "per_sign" }
  }
}
```
28.4 Phase Log Template
Create `docs/PHASE_LOG.md` at project start. Every agent updates this file when completing a phase:
```markdown
VinyasGen Phase Log
Phase 1 — Foundation
- Status: [ ] Not Started / [ ] In Progress / [ ] Complete
- Started: 
- Completed: 
- All tests passing: Y/N
- Notes:
Phase 2 — Core Engines
- Status: [ ] Not Started / [ ] In Progress / [ ] Complete
- Depends on: Phase 1 complete
- Started:
- Completed:
- All tests passing: Y/N
- Notes:
[Repeat for each phase]
```
---
*End of VinyasGen v2.0 Technical Manifesto*
*This document supersedes VinyasGen v1.0 (June 2026)*
*Any agent working on this project must use this document, not the v1.0 manifesto*
