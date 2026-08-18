---
schema_version: 1
id: human.deep-foundations.post-hd13.fourth-generation-rerank.sources
profile: research
lifecycle: completed
source_role: evidence
visibility: public
owners:
  - ordivon-human
audience:
  - researcher
  - agent
updated: 2026-08-18
summary: Primary evidence ledger supporting the post-HD13 whole-Human fourth-generation re-ranking and admission of HD14 Spatial Navigation, Place, Reference Frames and Cognitive Maps. Sources cover selective developmental topographical disorientation, self-report versus objective navigation measurement, allocentric versus egocentric spatial maps, landmark correction of path integration, distinct panoramic versus landmark-based view integration, allocentric-representation formation, nonvisual/blind navigation and reference-frame differences, and individual path-integration bias. Comparison evidence for Human-Agent adaptation and psychopathology is included only to rank marginal information and owner novelty. No source admits HF24.
evidence_status: verified
readiness: READY
related:
  - human.deep-foundations.post-hd13.fourth-generation-rerank
  - human.deep-foundations.hd14.continuation
---
# Post-HD13 Fourth-Generation Re-Ranking — Primary Evidence Ledger

## S01 — Iaria & Barton 2010 — selective developmental topographical disorientation

`Developmental Topographical Disorientation: a newly discovered cognitive disorder.`
Experimental Brain Research.
PMID: 20431873.
DOI: 10.1007/s00221-010-2256-9.

The study characterized a large set of DTD cases with severe lifelong orientation/navigation problems despite the absence of acquired brain injury and otherwise broadly preserved cognition; cognitive-map formation strongly differentiated affected participants from controls.

Use:

```text
GeneralCognitionPreserved
!= NavigationPreservedByDefinition
```

---

## S02 — Bonavita et al. 2025 — self-report vs actual navigation

`Dual Assessment of Developmental Topographical Disorientation: Comparing Self-Reported Measures with Actual Navigational Performance.`
Brain Sciences 15(3):318.
PMID: 40149839.
DOI: 10.3390/brainsci15030318.

N=185 college students. Self-report screening and computerized ecological navigation battery identified partly different potential DTD cases; only two participants were flagged by both approaches. The objective battery separated route knowledge, landmark knowledge, survey knowledge and landmark ordering.

Use:

```text
SenseOfDirectionSelfReport
!= ActualNavigationPerformance
NavigationAbility != OneScore
```

---

## S03 — Nett et al. 2025 — allocentric vs egocentric cognitive maps

`Behavioral investigation of allocentric and egocentric cognitive maps in human spatial memory.`
Neuropsychologia 217:109230.
PMID: 40721154.
DOI: 10.1016/j.neuropsychologia.2025.109230.

After virtual navigation, object–environment relationships predicted allocentric memory while object–participant distance/orientation predicted egocentric memory. Spatial feedback supported performance within allocentric and egocentric domains rather than transferring across them.

Use:

```text
AllocentricSpatialRepresentation
!= EgocentricSpatialRepresentation
```

---

## S04 — Naveilhan et al. 2025 — landmark correction of path integration

`Theta Activity Supports Landmark-Based Correction of Naturalistic Human Path Integration.`
Journal of Neuroscience 45(45):e1005252025.
PMID: 41006061.
DOI: 10.1523/JNEUROSCI.1005-25.2025.

Immersive VR + mobile EEG. Homing error accumulated during navigation and was corrected by brief landmark presentation; correction depended partly on confidence in self-motion-derived spatial estimates.

Use:

```text
PathIntegration != LandmarkNavigation
Navigation can require dynamic cue recalibration.
```

---

## S05 — Han & Epstein 2026 — distinct view-integration mechanisms

`Distinct Mechanisms for Panoramic and Landmark-Based View Integration in Human Place-Selective Cortex.`
Journal of Neuroscience 46(5):e0187252025.
PMID: 41475765.
DOI: 10.1523/JNEUROSCI.0187-25.2025.

Participants learned a virtual-city route. Panoramic associations across views from one vantage point and landmark associations across different views of a distal location recruited distinguishable place-selective processing.

Use:

```text
PanoramicViewIntegration
!= LandmarkBasedViewIntegration
```

---

## S06 — 2025 naturalistic virtual-city allocentric representation study

`Formation of allocentric representations after exposure to a novel, naturalistic, city-like, virtual reality environment.`
Neuropsychologia.
PMID: 41043647.
DOI: 10.1016/j.neuropsychologia.2025.109290.

The study directly tested development of allocentric spatial representations from navigation experience in a naturalistic VR environment.

Use:

```text
AllocentricRepresentation
= acquired/transformed spatial structure,
not a transparent copy of egocentric input.
```

---

## S07 — Kalia, Schrater & Legge 2013 — navigation without vision

`Combining path integration and remembered landmarks when navigating without vision.`
PLoS ONE.
PMID: 24039742.
DOI: 10.1371/journal.pone.0072170.

Blindfolded participants combined remembered landmark and path-integration information conditionally on cue congruence.

Use:

```text
NonvisualNavigation can combine body-based and remembered spatial evidence.
```

---

## S08 — congenital blindness / reference-frame study

`Centred egocentric, decentred egocentric, and allocentric spatial representations in the peripersonal space of congenital total blindness.`
Perception.
PMID: 19662943.
DOI: 10.1068/p5942.

Congenitally blind and sighted participants showed different costs across egocentric/allocentric conditions, with blindness producing greater difficulty especially for allocentric relations.

Use:

```text
SpatialRepresentation != VisualFormat
Egocentric != Allocentric
```

---

## S09 — 2023 sensory-substitution navigation

`Activation of human visual area V6 during egocentric navigation with and without visual experience.`
Current Biology.
PMID: 36863342.
DOI: 10.1016/j.cub.2023.02.025.

Sighted and congenitally blind participants performed egocentric navigation using a sensory-substitution device, demonstrating navigation-relevant cortical organization without normal visual experience.

Use:

```text
VisualExperience != NecessaryForEgocentricNavigationByDefinition
```

---

## S10 — Scherer et al. 2026 — persistent individual path-integration bias

`Uncovering persistent biases in human path integration by separating left and right trials.`
Scientific Reports 16:11611.
PMID: 41942606.
DOI: 10.1038/s41598-026-44217-w.

Re-analysis plus VR experiment found persistent individual left/right biases that can disappear under population-level averaging.

Use:

```text
PopulationMeanNavigationError
!= IndividualNavigationMechanism
```

---

# Ranking comparison: Human-Agent adaptation

## A01 — Guingrich & Graziano 2025

`A Longitudinal Randomized Control Study of Companion Chatbot Use: Anthropomorphism and Its Mediating Role on Social Impacts.`
AAAI/ACM AIES 2025.
DOI: 10.1609/aies.v8i2.36618.

N=183 randomized for 21 days. Companion-chatbot interaction did not significantly change social health/relationships versus control at the group level, while desire for social connection predicted anthropomorphism and anthropomorphism mediated reported social impact.

Use only for ranking:

```text
HumanAgentOutcome
is design/person-state dependent
and maps strongly to existing social/attachment/trust owners.
```

---

## A02 — 2025 randomized knowledge-retention study

`ChatGPT as a cognitive crutch: Evidence from a randomized controlled trial on knowledge retention.`
Social Sciences & Humanities Open 12:102287.
DOI: 10.1016/j.ssaho.2025.102287.

N=120 undergraduates. Unrestricted ChatGPT study assistance was associated with lower surprise-test retention 45 days later than traditional study in the reported trial.

Use only for ranking:

```text
AI support can alter HF7/HF6 learning/retention trajectories,
but this is not yet a new Human semantic owner.
```

---

# Ranking comparison: psychopathology

## P01 — Luther et al. 2026

`Computational phenotypes underlying effort-based decision-making and negative symptoms in a transdiagnostic severe mental illness sample.`
Molecular Psychiatry.
PMID: 41691110.
DOI: 10.1038/s41380-026-03474-x.

N=920 across multiple severe-mental-illness and risk groups. Different diagnostic groups showed different computational effort/reward profiles rather than one diagnosis-level process yielding negative symptoms.

Use only for ranking:

```text
Psychopathology = high falsifier value
but low diagnosis-level owner signal.
```

---

# Admission synthesis

```text
Spatial Navigation
→ major whole-domain coverage gap
→ ordinary Human function
→ clean developmental selective impairment
→ multiple reference-frame/task/cue-system dissociations
→ sensory-deprivation and active-navigation pressure
→ strong HF20/HF7/HF8/HF11/HF3 ownership ambiguity

Human-Agent Adaptation
→ very high Agent-era novelty
→ heavier existing owner allocation

Psychopathology
→ very high falsifier value
→ low new-owner signal
```

No source in this ledger admits HF24.
