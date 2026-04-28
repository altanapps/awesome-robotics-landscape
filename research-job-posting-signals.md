# Robotics Job Posting Signals — Labour Market Research
Date: 2026-04-28
Scope: UK + EU + US. 8-15 web queries. Sources: LinkedIn, Indeed, Glassdoor, ZipRecruiter, roboticsjobs.co.uk, BuiltIn, company careers pages.

---

## A. Top 10 Employer-Types Hiring Robotics Ops

### 1. Warehouse / Fulfillment Automation (Largest segment)
**Industries:** E-commerce, 3PL, grocery fulfillment
**Named employers:** Ocado Technology (UK), Amazon Robotics, Locus Robotics, Symbotic, Geek+
**Open roles found:** 14+ at Locus alone; 519 robotics-adjacent postings in London on Adzuna (March 2026); Amazon Robotics hiring $104k–$241k roles on ZipRecruiter
**What they want:** Deployment engineers, systems integration, fleet software, distributed robotics systems, motion planning, scheduling algorithms
**Geographic concentration:** US (Boston, Austin, Dallas); UK (London, Cheshire, Coventry for Ocado)
**Salary signal:** £40,000–£60,000 for deployment/integration roles in UK; $104k–$241k for Amazon Robotics software roles in US

### 2. Humanoid Robot Pilots / Operators (Fastest-growing new category)
**Industries:** AI training data, industrial manufacturing pilots, logistics trials
**Named employers:** Figure.ai, Physical Intelligence, 1X Technologies
**Open roles found:** Multiple at Figure — "Humanoid Robot Pilot (Helix Team)", "Humanoid Robot Operator (Morning Shift)", "Helix Data Creator"; ZipRecruiter shows $25–$125/hr Robot Pilot listings
**What they want:** Ability to wear teleoperation equipment, teach robots behaviours, collect motion data, file JIRA tickets for failures, stand 8+ hour shifts, lift 50 lbs
**Geographic concentration:** Exclusively US so far — San Jose CA, Mountain View CA, Spartanburg SC
**Salary signal:** $35–$40/hr for full-time Robot Pilot at Figure; $16–$52/hr for general robot operators on ZipRecruiter
**UK signal:** Zero — no UK humanoid pilot roles found anywhere

### 3. Defence / Autonomous Systems (High-value, growing UK presence)
**Industries:** Defence, border security, autonomous weapons systems
**Named employers:** Anduril (London office active), BAE Systems, Thales
**Open roles found:** Anduril London hiring perception engineers, software engineers (robotics stack: CV, motion planning, SLAM, controls); 12-week Summer 2026 paid internship in London
**What they want:** Robotics stack specialists, autonomy engineers, C2 (command-and-control) web application engineers, field logistics
**Geographic concentration:** UK — London primarily; US — Orange County CA
**Salary signal:** Not publicly disclosed by Anduril; competitive with US rates

### 4. Agricultural Robotics
**Industries:** Precision agriculture, crop management, autonomous ground vehicles
**Named employers:** Carbon Robotics, Small Robot Company (UK), Burro, Monarch Tractor
**Open roles found:** Thin signal in search results — no prominent job board volume
**What they want:** Navigation engineers, perception, fleet coordination for outdoor unstructured environments
**Geographic concentration:** US (West Coast, Midwest); UK (rural South England, East Anglia)
**Salary signal:** Not clearly visible in search results

### 5. Construction / Infrastructure Robotics
**Industries:** Construction site monitoring, demolition automation, infrastructure inspection
**Named employers:** Built Robotics, Boston Dynamics (field inspection), Trimble
**Open roles found:** Minimal in search results — company career pages show engineering roles not ops-specific
**What they want:** Deployment engineers, remote monitoring, field technicians
**Geographic concentration:** US; nascent UK

### 6. Service Robotics — Food / Hospitality
**Industries:** Restaurants, hotels, hospitals (food delivery, cleaning)
**Named employers:** Pudu Robotics (new US HQ in Dallas, opened April 2026), Bear Robotics, Keenon
**Open roles found:** Pudu opened Dallas HQ April 23 2026 signalling US hiring push; Bear Robotics has ops roles in US markets
**What they want:** Field ops, customer success, robot deployment technicians
**Geographic concentration:** US (Dallas, CA); minimal UK footprint in job boards
**Salary signal:** $56k–$68k robot operator range per Glassdoor

### 7. Healthcare / Clinical Robotics
**Industries:** Surgical robotics, pharmacy automation, patient transport AMRs
**Named employers:** CMR Surgical (UK, Cambridge), Intuitive, Stryker
**Open roles found:** roboticsjobs.co.uk notes clinical/assistive robotics as growth area in UK; specific ops roles not prominent in search results
**What they want:** Safety-critical systems, human-robot interaction, regulatory compliance
**Geographic concentration:** UK — Cambridge (CMR Surgical cluster); US — West Coast
**Salary signal:** Not visible in job board results

### 8. Last-Mile Delivery Robotics
**Industries:** Delivery, QSR, campus logistics
**Named employers:** Serve Robotics, Starship Technologies (UK), Cartken, Coco
**Open roles found:** Serve Robotics "Robot Operations Manager — Global Allocation & Compliance" (BuiltIn LA) — one of the clearest "RaaS ops manager" JDs found; requires 3–7 years in operations, supply chain, robotics or mobility
**What they want:** Forecasting, regulatory alignment, fleet readiness, global market compliance
**Geographic concentration:** US (LA, SF); UK — Starship active in Milton Keynes and several UK university campuses
**Salary signal:** Not publicly listed by Serve Robotics

### 9. Industrial Inspection / Utility Robotics
**Industries:** Oil & gas, power generation, infrastructure
**Named employers:** Wayve (UK, autonomous driving), Reach Robotics (UK, inspection), Carnotec (UK, industrial AGVs)
**Open roles found:** roboticsjobs.co.uk lists Reach Robotics and Carnotec as 2026 UK employers to watch; roles in SLAM, localisation, fleet coordination
**What they want:** Navigation engineers, perception, autonomous vehicle fleet coordination
**Geographic concentration:** UK — London, Bristol; US — industrial heartland

### 10. Robotics Infrastructure / Tooling Companies
**Industries:** Developer tools, observability, simulation
**Named employers:** Foxglove (San Francisco), Formant, Waypoint Robotics, Polymath Robotics
**Open roles found:** Foxglove hiring "Senior Software Engineer, Data" (ZipRecruiter San Francisco); senior visualization engineer (Ashby)
**What they want:** Data infrastructure for multimodal sensor streams, MCAP format, petabyte-scale robotics data storage, ROS 2 integration
**Geographic concentration:** US (San Francisco)
**Salary signal:** Foxglove Series B ($40M, Nov 2025, led by Bessemer) suggests competitive SF-range salaries

---

## B. Tooling Mentioned in JDs

**Tier 1 — Universal mentions:**
- ROS / ROS 2 — referenced in nearly every engineering JD; "modular middleware" baseline requirement
- Python + C++ — standard pairing for perception/control work
- JIRA — mentioned explicitly in Figure's robot operator JD for failure logging

**Tier 2 — Increasingly expected:**
- Foxglove — dominant observability/visualization platform for ROS-based fleets; used by NVIDIA, Amazon, Anduril, Wayve per Foxglove's own customer list; raised $40M Series B Nov 2025 on this positioning; described as "the data stack for Physical AI"
- MCAP — open-source multimodal logging standard, Foxglove-led, becoming the default for data collection at scale
- AWS / cloud — referenced in Amazon Robotics JDs; AWS RoboMaker mentioned in ecosystem but not prominent in specific JDs found
- NVIDIA Isaac Sim — simulation standard for AI training pipelines
- Gazebo / Ignition — standard simulation environment; nearly universal

**Tier 3 — Niche but notable:**
- Nav2, ORB-SLAM3, Cartographer — autonomous navigation tooling
- MoveIt — manipulator arms
- TensorRT / ONNX Runtime — edge inference
- Tailscale Funnel — mentioned in Polymath/Foxglove fleet-sharing stack

**Conspicuously absent from JDs:**
- No fleet billing or usage-metering software named
- No RaaS revenue recognition tooling named
- No compliance-specific platforms for autonomous systems regulation
- No insurance or liability assessment tools
- Formant and Transitive Robotics (remote access/fleet ops platforms) exist but are not being named as required skills in ops JDs

---

## C. Gaps in Role Taxonomy

These roles should logically exist given the maturity of RaaS deployment but do not appear in any JD found:

**1. RaaS Revenue Ops / Robot Fleet Billing Administrator**
The RaaS billing complexity is well-documented (Hardfin blog, Deloitte RaaS writeup, TechTimes March 2026 piece on RaaS subscription models). Billing by robot-hour, per-acre, or usage threshold is inherently hard to reconcile with standard ERP systems. Yet no job title exists for this. Finance teams are absorbing it ad hoc.

**2. Autonomous Systems Compliance Officer / Robot Regulatory Analyst**
EU AI Act and UK AI governance frameworks are actively advancing. Serve Robotics' "Global Allocation & Compliance" manager JD hints at this need but bundles it with fleet ops generalism. No standalone compliance role for autonomous ground vehicles exists in any posting found.

**3. Robot Insurance Analyst / Actuarial Specialist**
Zero results. The liability question for deployed AMRs and humanoid robots in public/commercial settings is real and unresolved. No insurer appears to have created a named role yet.

**4. Robot Fleet Performance Analyst / Robotics BI Analyst**
SQL/data analyst roles exist generically but none are titled specifically for robotics fleet performance. Foxglove addresses the data capture side; no role exists to own the downstream analysis for ops decisions.

**5. Teleoperation Quality Assurance Specialist**
Figure hires "Robot Pilots" to teach behaviours, but no QA role exists to validate the data pipelines and training outputs from these human-supervised sessions. The function likely sits inside ML eng teams but is invisible in JDs.

**6. RaaS Customer Success Manager (hardware-native)**
Generic CSM roles exist. No CSM role tuned specifically to RaaS contract structures — uptime SLAs, hardware swap-outs, usage reconciliation, renewal triggers — appears in any posting.

---

## D. UK-Specific Picture

**Volume:**
- 315–519 robotics-related jobs listed in UK as of early 2026 (Glassdoor 315 in UK, Adzuna 519 in London alone)
- 126 open robotics engineer roles in London specifically (Glassdoor, April 2026)
- Caveat: these numbers include all robotics engineering roles, not just ops-focused positions

**Geographic concentration:**
- London — dominant; Anduril, Wayve, Shadow Robot, Fabric, numerous startups
- Cambridge — CMR Surgical, ARM's robotics ecosystem adjacency
- Bristol — Shadow Robot Company, Bristol Robotics Laboratory spinouts
- Coventry / Cheshire — Ocado fulfilment centre deployments, Amazon warehouse clusters
- Milton Keynes — Starship Technologies UK delivery operations

**Named UK employers actively hiring:**
- Ocado Technology (fleet software, systems integration, motion planning)
- Shadow Robot Company (Bristol — dexterous manipulation)
- Carnotec (industrial AGVs, fleet coordination)
- Reach Robotics (inspection, mobile robotics)
- Fabric (smart logistics automation)
- Anduril (London — perception, autonomy, defence)
- Amazon (multiple fulfilment centre deployment roles, £40k–£60k)
- Boston Dynamics (expanding UK field testing presence)

**Salary picture (UK):**
- Robotics engineer London median: £45,474 per year
- Range: £35,646 (25th pct) to £72,216 (90th pct)
- Amazon deployment/integration roles: £40,000–£60,000
- Senior/staff engineers at defence companies (Anduril-level): not publicly disclosed but likely £80k–£120k

**UK vs US comparison:**
- US robotics engineer average: $142,892/yr (~£113k at current rates) — roughly 2.5x UK median
- US robot operator (floor-level): $56k–$64k, comparable to or below UK robotics engineer entry
- UK lags in volume but is growing fast (+41% YoY in Q1 2025 per roboticsjobs.co.uk)
- UK has no humanoid robot trial jobs yet — that segment is entirely US-based at Figure, 1X, Physical Intelligence
- UK strength: defence autonomy (Anduril), warehouse automation (Ocado ecosystem), surgical robotics (CMR)

---

## E. Synthesis

The labour market is telling a clear story: **warehouse logistics and humanoid trials are where deployment density is highest right now, and the software tooling gap is the most actionable signal.**

Warehouse is the most mature sector — Ocado, Amazon, Locus, Symbotic, Geek+ are all hiring at volume and the roles are real and recurring. This is a solved-enough category that the ops tooling layer (Foxglove for observability, Nav2/ROS2 for navigation) is becoming standard. No new wedge there.

The genuinely underserved layer is **the business and compliance infrastructure surrounding RaaS deployments**. The RaaS market hit $8.2B in 2026 per FMI data, with billing models (per robot-hour, per-acre, per-task) creating finance and compliance complexity that no dedicated software or role taxonomy has addressed. Serve Robotics' "Global Allocation & Compliance" manager is the clearest signal of this — one person absorbing regulatory, forecasting, and fleet readiness that arguably needs three distinct functions.

The humanoid pilot category is a novel deployment signal: Figure is paying $35–$40/hr for humans to wear teleoperation suits and teach robots, with explicit "contract-to-hire" language. This suggests the industry knows these roles are transitional — they're building training data, not permanent headcount. The tooling to manage, QA, and commercialise that training data pipeline does not yet have a named role or named product.

UK lags the US by 2–3 years in robotics ops role maturity but is growing. The most relevant UK signal is Ocado's continued fleet software hiring and Anduril's London engineering investment. A UK-first robotics ops tool would find its first customers in warehouse and defence, not restaurant or last-mile. A US-first tool has 2–3× the role-density to sell into.

---

## Sources

- https://www.builtinla.com/job/robot-operations-manager-global-allocation-compliance/9006077 — Serve Robotics Robot Operations Manager JD
- https://job-boards.greenhouse.io/figureai/jobs/4406268006 — Figure Humanoid Robot Operator JD
- https://job-boards.greenhouse.io/figureai/jobs/4369739006 — Figure Humanoid Robot Pilot (Helix Team) JD
- https://foxglove.dev/about — Foxglove product and customer list
- https://www.businesswire.com/news/home/20251112126106/en/Foxglove-Raises-$40-Million-Series-B-to-Power-the-Future-of-Physical-AI — Foxglove Series B announcement
- https://roboticsjobs.co.uk/career-advice/new-robotics-employers-to-watch-in-2026-uk-and-global-companies-transforming-automation-careers — UK employers 2026
- https://roboticsjobs.co.uk/career-advice/robotics-jobs-skills-radar-2026-tools-frameworks-technologies — Robotics tools skills radar
- https://www.glassdoor.co.uk/Job/london-robotics-engineer-jobs-SRCH_IL.0,6_IC2671300_KO7,24.htm — London robotics engineer jobs
- https://www.glassdoor.co.uk/Salaries/london-robotics-engineer-salary-SRCH_IL.0,6_IM1035_KO7,24.htm — London robotics engineer salary
- https://www.techtimes.com/articles/314939/20260304/robotics-service-raas-business-models-how-subscription-robotics-transforming-industries.htm — RaaS business models 2026
- https://blog.hardfin.com/what-is-robots-as-a-service-raas — RaaS billing complexity analysis
- https://builtinlondon.uk/company/anduril/jobs — Anduril London jobs
- https://www.roboticstomorrow.com/news/2026/04/22/pudu-robotics-inaugurates-us-headquarters-in-dallas-accelerating-long-term-growth-in-the-americas/26461/ — Pudu US HQ opening
- https://www.symbotic.com/careers/open-positions/ — Symbotic open roles
- https://www.adzuna.co.uk/jobs/london/robotics — Adzuna London robotics listings
