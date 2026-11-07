# OCES — Open Construction Engineering System

Node-Based IFC Construction Method Engineering Platform

## Vision
Develop an open, extensible engineering environment that turns architectural design concepts into verifiable construction methods, fabrication models, assembly sequences, and drawings.

## Architecture
- **OCES Studio:** React + TypeScript node editor and 3D preview
- **Skill Registry & Executor:** versioned, typed engineering skills with tests
- **LLM Gateway & Agent:** natural-language planning, human approval, model-agnostic providers
- **MCP / API Adapters:** Blender + Bonsai and FreeCAD Python API control
- **IFC Engineering Core:** IfcOpenShell, stable identity, properties, relationships, validation
- **2D Drawings:** OpenCADStudio integration subject to compatibility testing

## Principles
1. IFC is the primary exchange and engineering information format for Bonsai and FreeCAD.
2. A node is an instance of a reusable Skill; skills have schemas, versioning, and tests.
3. Geometry generation, engineering validation, and construction approval are distinct.
4. Never assume FreeCAD parametric feature history survives IFC round trips.
5. Never overwrite the source IFC model without a reviewed, reversible change.
6. LLMs propose plans; deterministic skills execute; engineers approve safety-critical outputs.

## First vertical slice
1. Read a sample IFC component.
2. Generate a parameterized steel bracket with FreeCAD.
3. Map the component to IFC while retaining identity and properties.
4. Open and inspect the result in Bonsai.
5. Produce a clash/clearance report and a basic drawing.
6. Repeat after changing one parameter and verify consistency.

## Development phases
- P0: project skeleton, IFC Core, skill contracts, test fixtures
- P1: node editor and workflow persistence
- P2: FreeCAD and Bonsai adapters with round-trip tests
- P3: construction-rule validation and 2D drawings
- P4: LLM Gateway, MCP, approval gates
- P5: skill evolution, regression testing, knowledge base

## Status
Planning / initial repository bootstrap. No production-ready engineering validation or live CAD control is claimed.

## Next steps
Add `plan.md`, architecture decision records, minimal executable IFC Skill, CI tests, and a first construction-method demonstration.
