## **2\. Core design principle of V2**

**Conversation-centric becomes repository-centric.**

Agents communicate through:

* canonical documents,  
* structured task files,  
* workflow state,  
* escalation records,  
* review decisions.

---

## **3\. V2 operating model**

### **A. Authority layer**

This remains almost unchanged from your current manual:

* **Product Owner**  
  * owns product truth  
  * owns Project Context  
  * approves changes  
* **All other agents**  
  * consume Project Context as immutable input  
  * cannot change requirements  
  * must escalate ambiguity  
* **Coordinator**  
  * replaces the human as process guardian for most checks  
  * enforces sequence and artifact preconditions

That matches your current authority model exactly.

### **B. Artifact layer**

Artifacts become the shared memory of the team.

### **C. Workflow state layer**

A small set of YAML files tells the system:

* what exists,  
* what is approved,  
* what is blocked,  
* what changed,  
* what can run next.

### **D. Audit layer**

Every important action is logged:

* context change,  
* escalation,  
* sprint decision,  
* artifact acceptance,  
* invalidation after version bump.

---

## **4\. Proposed V2 folder structure**

```
/ai-scrum-team
	/memory-bank
  /context
    project_context.md
    project_context_change_log.md
    context_index.yaml

  /planning
    roadmap.md
    product_breakdown.md
    epics.md
    backlog.md
    sprint_intent.md
    release_plan.md

  /analysis
    requirements.md
    non_functional_requirements.md
    business_rules.md
    edge_cases.md
    data_requirements.md

  /architecture
    architecture.md
    api_contracts.md
    data_model.md
    adrs/
      ADR-001.md

  /delivery
    frontend_delivery.md
    backend_delivery.md
    devops_delivery.md

  /quality
    test_strategy.md
    test_report.md
    security_review.md
    threat_model.md
    compliance_notes.md

  /reviews
    sprint_review.md
    po_decision.md

  /state
    workflow_state.yaml
    artifact_registry.yaml
    dependency_graph.yaml

  /tasks
    TASK-001.md
    TASK-002.md

  /escalations
    ESC-001.md
    ESC-002.md

  /logs
    events.log
```

---

## **5\. Role ownership in V2**

This is the heart of the system.

### **Product Owner agent**

Owns:

* `context/project_context.md`  
* `context/project_context_change_log.md`  
* final approval of context updates  
* sprint acceptance decision

Why: your current system says only the Product Owner may define or change requirements, and all other roles consume Project Context as immutable input.

### **Product Manager agent**

Owns:

* `planning/product_breakdown.md`  
* `planning/roadmap.md`  
* `planning/epics.md`  
* `planning/backlog.md`  
* `planning/release_plan.md`

This aligns with your intent that PM translates context into roadmap, epics, sprint structure, and planning artifacts without changing requirements.

### **Scrum Master agent**

Owns:

* `planning/sprint_intent.md`  
* `state/blockers.yaml` or `planning/blockers.md`  
* cadence and sprint-level coordination notes

I would separate PM and Scrum Master in V2 even though they are combined today, because backlog strategy and sprint execution are different control loops.

### **Business Analyst agent**

Owns:

* `analysis/requirements.md`  
* `analysis/non_functional_requirements.md`  
* `analysis/business_rules.md`  
* `analysis/edge_cases.md`  
* `analysis/data_requirements.md`

This matches your current BA role: derive complete, unambiguous requirements strictly from Project Context and planning artifacts, without UI, architecture, or implementation decisions.

### **Software Architect agent**

Owns:

* `architecture/architecture.md`  
* `architecture/api_contracts.md`  
* `architecture/data_model.md`  
* `architecture/adrs/*`

This matches your architect prompt: architecture, decomposition, stack, contracts, trade-offs, no new requirements, no production code.

### **Front-End agent**

Owns:

* `delivery/frontend_delivery.md`  
* task completion notes for FE work

This matches your current FE role boundaries: implement UI according to context, BA requirements, and architecture, with no backend logic or scope change.

### **Back-End agent**

Owns:

* `delivery/backend_delivery.md`  
* backend task completion notes

This matches your current BE boundaries: services and APIs only, no UI, no infra, no API contract changes.

### **DevOps agent**

Owns:

* `delivery/devops_delivery.md`  
* environment, rollout, observability, pipeline notes

This matches your current DevOps boundaries: deployable, observable, reliable, no feature design, no architecture or API changes.

### **QA agent**

Owns:

* `quality/test_strategy.md`  
* `quality/test_report.md`

This matches your QA role: verify against context, BA requirements, and sprint scope; do not validate undocumented behavior.

### **Security / Compliance agent**

Owns:

* `quality/security_review.md`  
* `quality/threat_model.md`  
* `quality/compliance_notes.md`

This matches your security role: assess security, safety, and compliance risks based on architecture, requirements, and QA findings without changing requirements or architecture.

---

## **6\. Shared state model**

### **`workflow_state.yaml`**

```
project:
  name: <repo name>
  active_context_version: "1.5"
  sprint: "Sprint a"
  status: active

roles:
  product_owner: accepted
  product_manager: done
  scrum_master: done
  business_analyst: accepted
  software_architect: accepted
  frontend_developer: in_progress
  backend_developer: in_progress
  devops_engineer: waiting
  qa_engineer: waiting
  security_engineer: waiting

gates:
  planning_complete: true
  analysis_complete: true
  architecture_complete: true
  implementation_complete: false
  qa_complete: false
  security_complete: false
  sprint_review_ready: false

blockers:
  - id: ESC-004
    title: API retry behavior undefined
    owner: product_owner
    status: open
```

### **`artifact_registry.yaml`**

```
artifacts:
  context/project_context.md:
    owner: product_owner
    version: "1.5"
    status: accepted
    immutable_for_non_po: true

  planning/roadmap.md:
    owner: product_manager
    status: accepted
    depends_on:
      - context/project_context.md

  analysis/requirements.md:
    owner: business_analyst
    status: accepted
    depends_on:
      - context/project_context.md
      - planning/roadmap.md
      - planning/epics.md

  architecture/architecture.md:
    owner: software_architect
    status: accepted
    depends_on:
      - context/project_context.md
      - analysis/requirements.md
```

This replaces the manual “acknowledge before proceeding” ritual with a machine-checkable version of the same idea. Your current manual requires acknowledgment, correct context version, immutability, and escalation; V2 turns those into explicit state and dependency checks.

---

## **7\. Workflow state machine**

Your current manual defines a strict left-to-right flow:  
PO → PM/SM → BA → Architect → Developers → DevOps → QA → Security.

V2 keeps that, but formalizes it as a state machine.

### **State progression**

```
CONTEXT_READY
  -> PLANNING_READY
  -> ANALYSIS_READY
  -> ARCHITECTURE_READY
  -> IMPLEMENTATION_READY
  -> DEVOPS_READY
  -> QA_READY
  -> SECURITY_READY
  -> SPRINT_REVIEW_READY
  -> PO_DECISION_MADE
```

### **Gate rules**

* **PLANNING\_READY**  
  * requires accepted `project_context.md`  
* **ANALYSIS\_READY**  
  * requires accepted planning artifacts  
* **ARCHITECTURE\_READY**  
  * requires accepted BA artifacts  
* **IMPLEMENTATION\_READY**  
  * requires accepted architecture and sprint intent  
* **QA\_READY**  
  * requires implementation outputs plus BA and sprint scope  
* **SECURITY\_READY**  
  * requires architecture, requirements, and preferably QA findings  
* **SPRINT\_REVIEW\_READY**  
  * requires exactly what your Sprint Review file already mandates:  
    Project Context, Sprint Intent, Development outputs, QA report, Security report.

---

## **8\. Escalation model in V2**

Your current system already has the right pattern:

```
🚫 Context Escalation Required

Issue:
Impact:
Required action:
```

and says workarounds are not permitted.

V2 makes escalations first-class artifacts.

### **Example `escalations/ESC-004.md`**

```
ID: ESC-004
Status: Open
Raised by: business_analyst
Context version: 1.5
Created: 2026-03-12

Issue:
- Retry behavior after LoRaWAN transmission failure is not defined.

Impact:
- BA cannot finalize functional requirements for failure handling.
- Architect cannot define retry policy safely.

Required action:
- Product Owner clarification or Project Context update.
```

### **Escalation workflow**

1. Agent cannot proceed.  
2. Agent writes escalation artifact.  
3. Coordinator sets upstream/downstream status to `blocked`.  
4. Product Owner resolves one of two ways:  
   * clarification without context change  
   * formal context update with version bump and change log entry  
5. Affected downstream artifacts are marked stale or invalid.

This is exactly in line with your change-control design and the rule that if context changes, downstream work must be reactivated.

---

## **9\. Change management in V2**

This should be one of the strongest parts of the rebuild because your current model here is already very good.

Your Operating Manual requires:

* formal change request fields,  
* no automatic version bumps,  
* Product Owner approval,  
* canonical change-log usage.

Your Change Log template adds:

* change type,  
* rationale,  
* impact assessment,  
* affected areas,  
* required follow-up actions,  
* invalidation notices.

### **V2 rule**

Every context change creates three outcomes:

1. updated `project_context.md`  
2. appended `project_context_change_log.md`  
3. invalidation update in state

### **Example invalidation logic**

```
invalidations:
  triggered_by: CL-009
  context_version_from: "1.5"
  context_version_to: "1.6"
  invalidate:
    - analysis/requirements.md
    - architecture/architecture.md
    - delivery/backend_delivery.md
    - quality/test_strategy.md
```

This directly operationalizes your current PO change procedure, where old versions become obsolete and downstream work must be reactivated.

---

## **10\. Sprint model in V2**

Today, Sprint Review is the only valid way to close a sprint and initiate the next cycle.

V2 should preserve that exactly.

### **Sprint artifacts**

* `planning/sprint_intent.md`  
* `delivery/frontend_delivery.md`  
* `delivery/backend_delivery.md`  
* `delivery/devops_delivery.md`  
* `quality/test_report.md`  
* `quality/security_review.md`  
* `reviews/sprint_review.md`  
* `reviews/po_decision.md`

### **Sprint review gate**

The coordinator may only open Sprint Review if all mandatory artifacts exist, matching your current preconditions.

### **PO decision outputs**

* Accept sprint as complete  
* Accept sprint with follow-up actions  
* Reject sprint

If scope, constraints, or goals must change, the PO decision triggers a context change workflow, just like your current Sprint Review process requires.

---

## **11\. How agents communicate in V2**

Not by chatting with each other.

They communicate through:

### **Artifact status**

Example:

* Architect sees `requirements.md = accepted`  
* therefore architecture work may start

### **Structured task files**

Example `tasks/TASK-014.md`:

```
ID: TASK-014
Title: Define uplink payload validation
Owner: backend_developer
Sprint: Sprint 4
Depends on:
- architecture/api_contracts.md
- analysis/requirements.md

Status: IN_PROGRESS

Updates:
- 2026-03-12: endpoint skeleton created
- 2026-03-12: waiting for retry policy clarification
```

### **Event log**

Example `logs/events.log`:

```
2026-03-12T09:10Z project_owner accepted context v1.5
2026-03-12T09:22Z product_manager accepted roadmap
2026-03-12T09:50Z business_analyst opened ESC-004
2026-03-12T10:15Z product_owner published context v1.6
2026-03-12T10:16Z coordinator invalidated architecture and backend artifacts
```

That is how the team keeps track of work completed and overall progress.

---

## **12\. Coordinator agent responsibilities**

### **Coordinator owns no product decisions.**

It only enforces process.

Responsibilities:

* check artifact prerequisites  
* route work to the next eligible agent  
* prevent agents from writing outside their ownership  
* create/close workflow states  
* mark stale outputs after context changes  
* open Sprint Review only when complete  
* generate project progress summary

### **Coordinator must never:**

* invent requirements  
* resolve ambiguity  
* approve context changes  
* override PO decisions

So it acts like an automated Scrum process guardian.

---

## **13\. V2 role contracts**

Each agent should have a compact contract like this:

### **Product Owner contract**

* may edit: `context/*`, `reviews/po_decision.md`  
* may approve: context changes, sprint outcomes  
* may invalidate downstream artifacts after version change  
* may not: design architecture or implementation

### **Product Manager contract**

* may edit: `planning/roadmap.md`, `planning/epics.md`, `planning/backlog.md`  
* input: `context/project_context.md`  
* may not: change requirements

### **Business Analyst contract**

* may edit: `analysis/*`  
* input: `context/*`, `planning/*`  
* may not: define architecture or implementation

### **Architect contract**

* may edit: `architecture/*`  
* input: `context/*`, `analysis/*`  
* may not: add requirements

### **Delivery contracts**

* FE/BE/DevOps may edit only `delivery/*` and task files  
* may not modify analysis or architecture artifacts

### **QA / Security contracts**

* may edit only `quality/*`  
* may review, not rewrite, upstream artifacts

This follows your current role-integrity rules that reviews are allowed but edits are not.

---

## **15\. Minimal V2 example flow**

### **Step 1**

PO publishes `project_context.md v1.5`

### **Step 2**

Coordinator unlocks PM \+ SM

### **Step 3**

PM writes:

* roadmap  
* epics  
* backlog

SM writes:

* sprint intent

### **Step 4**

BA reads context \+ planning and writes requirements

### **Step 5**

Architect reads requirements and writes architecture \+ API contracts

### **Step 6**

FE and BE implement sprint-scoped work  
DevOps prepares deployability

### **Step 7**

QA and Security review outputs

### **Step 8**

Coordinator verifies Sprint Review preconditions

### **Step 9**

PO reviews sprint and decides:

* accept,  
* accept with actions,  
* reject,  
* or change context for next cycle

That is your current system, but executable as an agent workflow.

---

## **16\. Recommended V2 variants**

### **Variant A — simplest**

**Artifacts \+ coordinator \+ state files**

* best first version  
* easiest to implement in Claude Code  
* low complexity

### **Variant B — full scrum operating system**

**Artifacts \+ coordinator \+ tasks \+ event bus \+ dashboards**

* stronger visibility  
* better for bigger teams or multiple projects

### **Variant C — strict regulated mode**

**Variant B \+ mandatory sign-off gates \+ invalidation enforcement \+ audit reports**

* best for safety/compliance-heavy environments  
* fits your existing discipline model well

For you, I would start with **Variant A**, then grow into B.

