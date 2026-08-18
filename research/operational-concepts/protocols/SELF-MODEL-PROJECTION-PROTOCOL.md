---
schema_version: 1
id: human.operational-protocol.self-model-projection
title: Self-Model Projection Protocol
profile: research
lifecycle: active
source_role: canonical-protocol
visibility: public
owners:
  - ordivon-human
updated: 2026-08-18
summary: Purpose-scoped, privacy-minimized self-model/identity projection protocol retained after generic Identity/Self-Model failed HOC-family admission. It is not OneUserProfile and not an HOC.
evidence_status: verified-synthesis
readiness: READY
---
# SelfModelProjectionProtocol

`SelfModelProjectionProtocol` is an **unnumbered cross-cutting protocol**, not a generic Identity HOC and not a permanent person dossier.

```text
SelfModelProjectionSpec = {
  use_question,
  substantive_owner,
  Human,
  self_referential_target,
  identity_relation_type,
  role/group/domain if relevant,
  temporal scope,
  transition/event if relevant,
  self-endorsed content,
  externally attributed content?,
  inference source?,
  salience/centrality only if decision-relevant,
  relation to goals/roles/habits/capability,
  direct statement evidence,
  behavioral/history evidence,
  contradictory evidence,
  cultural/developmental scope,
  uncertainty,
  update/contest rule,
  expiry/retention rule,
  downstream-use boundary,
  forbidden inferences,
  routing owner
}
```

Required firewall:

```text
AgentInferredIdentity != HumanEndorsedIdentity
```

Consumers should request only the minimum decision-relevant self-model dimension, preserve source/endorsement and contestability, expire stale projections, and route substantive action to the appropriate owner.

Provenance: post-HOC9 destructive tournament R5 and closure-falsification R7 under [`../`](../).
