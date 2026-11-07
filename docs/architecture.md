# Architecture decisions

## IFC as engineering exchange contract
IfcOpenShell handles model inspection and IFC editing. FreeCAD native FCStd files retain editable feature history; IFC is the shared engineering representation. Bonsai is the BIM coordination application. No assumption of lossless IFC round-trip.

## Node / Skill separation
A node refers to a versioned Skill and supplies typed inputs. Graph execution is topologically ordered. Production implementation must add schema validation, cancellation, resource limits, audit logging, authorization, and transactional IFC revisions.

## MVP boundary
Current code is a foundation only: IFC inspection + simple deterministic skill runner. There is no live Bonsai/FreeCAD MCP, UI, LLM gateway, or engineering validation yet.
