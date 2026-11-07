# OCES Development Plan (v0.1)

## Mission
An IFC-centric, node-based construction method engineering platform: design intent → parametric details → constructability checks → reviewed drawings.

## Core design decisions
- **IFC is the exchange contract**, not a replacement for FreeCAD native feature history. Persist FCStd alongside IFC where editable CAD history is required.
- **Skill ≠ Node**: a Skill is a versioned capability; a Node is a configured invocation of that capability.
- **Execution is deterministic**: the LLM proposes a typed DAG; the runner validates the graph and invokes approved skills.
- **Single-writer IFC workflow**: immutable input revision, working copy, validated output revision, atomic promotion; prevent simultaneous edits from Bonsai and FreeCAD.
- **Stable identity**: preserve IFC GlobalId for unchanged elements; create new GlobalIds for newly created elements; log replacements and lineage.
- **Engineering safety**: geometric clearance checks do not establish structural adequacy or code compliance; engineering approval remains mandatory.

## Components
1. Studio: React + TypeScript + React Flow, 3D viewer, property panel, validation report.
2. API: FastAPI with job execution and audit log.
3. Skill Engine: manifest + JSON Schema + versioned registry + DAG executor.
4. IFC Core: IfcOpenShell parsing, identity, metadata, model snapshots and validation.
5. FreeCAD Adapter: separate Python process, native Part/Sketcher and IFC export mapping.
6. Bonsai Adapter: Blender process + Bonsai/IfcOpenShell APIs; import/inspect/validate.
7. Drawing Adapter: 2D projections and annotation; investigate OpenCADStudio capabilities before promising integration.
8. LLM Gateway: pluggable providers; plan generation with structured output; human approval before execution.

## Milestones
### P0: reproducible IFC + Skill foundation
- Project skeleton, pinned Python dependencies, CI, JSON Schema contracts.
- Read IFC STEP header, list IFC elements with IfcOpenShell, deterministic JSON output.
- Execute first Skill without CAD applications installed.
- Tests for malformed inputs, missing IFC, duplicate node IDs, cycles, unknown skill types.
**Acceptance:** `pytest` passes and CLI reads an example IFC.

### P1: node editor
- Canvas, typed ports, DAG serialization, run controls, progress/errors, history.
**Acceptance:** save/reopen/run the same workflow and inspect results.

### P2: CAD adapters
- FreeCAD parametric steel bracket generation and IFC mapping.
- Bonsai IFC import, inspect, round-trip geometry/property checks.
- Process isolation, timeouts, cancellation, logs, API version checks.
**Acceptance:** a thickness change updates geometry and IFC while unaffected GUIDs remain stable.

### P3: construction checks and drawings
- Clashes, tolerances, access envelopes, component counts, basic drawing exports.
- Explicit distinction between rule-based checks and engineer-approved designs.

### P4: Agent + MCP
- Model gateway, schema-validated proposed graph, tool permissions, approval gates.
- MCP servers expose approved operations; API remains execution authority.

### P5: skill evolution
- Regression fixtures, release gates, semantic versioning, reproducible workflows, knowledge base.

## First reference case
1800 × 1200 mm cladding panel and a steel bracket assembly. Inputs include panel thickness, support spacing, anchors, substrate, tolerances and load cases. Unspecified engineering values remain TODO, not fabricated.

## Risks
- IFC round-trips may alter geometry, properties or classifications.
- FreeCAD feature trees are not reliably preserved in IFC.
- Bonsai/FreeCAD versions and IFC4/IFC4.3 support require explicit compatibility tests.
- Drawing tool capability and fidelity must be independently verified.
- LLM hallucinations and destructive CAD edits require approval and sandboxing.

## Definition of done
A feature is complete only with documented behavior, automated tests, example data, logs, and reproducible acceptance steps.
