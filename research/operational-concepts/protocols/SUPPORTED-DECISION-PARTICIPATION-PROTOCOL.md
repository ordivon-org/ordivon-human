---
schema_version: 1
id: human.operational-protocol.supported-decision-participation
title: Supported Decision Participation Protocol
profile: research
lifecycle: active
source_role: canonical-protocol
visibility: public
owners:
  - ordivon-human
updated: 2026-08-18
summary: Purpose-bound protocol for representing actual Human decision participation, support, control, authority, communication and revision without collapsing autonomy or capacity into a score. It is not an HOC and does not adjudicate legal/normative authority.
evidence_status: verified-synthesis
readiness: READY
---
# SupportedDecisionParticipationProtocol

`SupportedDecisionParticipationProtocol` is an **unnumbered cross-cutting consumption protocol**. It coordinates existing decision, capability, goal/control, role/authority, understanding and communication owners; it does not own legal or normative authority.

Minimal reasoning grammar:

1. Declare the exact decision and consequence.
2. Identify the substantive owner and legal/institutional authority regime.
3. Record the Human's actual decision role; do not infer it from diagnosis, age, support need or role label.
4. Elicit goals/preferences/values using accessible communication.
5. Assess only decision-relevant understanding/capability under realistic support.
6. Name supporters/advisers/proxies and their authority separately.
7. Record dependence, power asymmetry, pressure/coercion and option-set restrictions.
8. Distinguish advice/support from substitution.
9. Check whether the Human can revise, refuse, stop or override where the domain permits.
10. Record whether Human input actually affected the outcome.
11. Route legal/rights disputes to the appropriate institutional/normative owner; do not adjudicate them from Human scores.
12. Update/expire rapidly when support, health, authority, communication or decision context changes.

Canonical firewalls include:

```text
Support != Substitution
Advice != Decision
Dependence != Consent
Preference != Consent
DecisionCompetenceEvidence != DecisionAuthority
SupportNeed != NoDecisionAgency
CommunicationSupportNeed != NoDecisionVoice
Care != Authority
AIRecommendation != HumanPreference
HumanRelianceOnAI != TransferOfHumanAuthority
```

Provenance: post-HOC9 unknown-continent R6 and closure-falsification R7 under [`../`](../).
