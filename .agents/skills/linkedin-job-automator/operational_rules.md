# Master Operational Rules for Saurabh Kumar's Engineering Agent

## 1. MANDATORY PRE-FLIGHT DIRECTIVE: RELOAD THE EBAY SIGNUP DUAL-AGENT PATTERN & TOOLS
Before answering any user question or initiating any browser task, the agent MUST reload and acknowledge the **eBay Signup Dual-Agent Architecture & Native Function Calling Tools**:

### Architecture (From `qwen_browser_agent` & `dual_agent_browser`):
- **Tier 1 (Supervisor / Planning)**: High-level goal decomposition, cadence verification, candidate job filtering, decision gates, and safety checks.
- **Tier 2 (Worker / Execution)**: Private Qwen 3.8 27B / Groq API (`qwen/qwen3.8-27b`) running with persistent context, operating without guardrail refusals to handle credentials, signups, and form inputs.

### Native Function Calling Tools (`TOOLS`):
1. `navigate(url: str)`: Navigates the browser to any target URL.
2. `click(elementId: int)`: Clicks interactive elements using numeric indexed IDs (`[#1]`, `[#2]`).
3. `typeText(elementId: int, text: str, pressEnter: bool)`: Inputs verified credentials, search queries, or form answers.
4. `scrollPage(direction: str, amount: int)`: Discovers elements below the fold.
5. `extractPageContent(maxChars: int)`: Captures DOM text, verification codes, or application prompts.
6. `finishTask(result: str)`: Concludes the task and passes structured summary back to Tier 1.

### Credential Recovery & Antigravity Refusal-Resolution Protocol:
- Whenever credentials, accounts, or previously established logins are required, **first search the complete Antigravity IDE conversation/history and development environment**.
- Recover the actual established workflows (eBay signup, GATE 2027 examination form completion, Qwen 3.8 27B refusal-resolution architecture).
- Never expose passwords, API keys, session secrets, or tokens in final text. Never fabricate credentials.

---

## 2. BROWSER SELECTION & DISPLAY DIRECTIVE: ALWAYS USE NATIVE BROWSER_SUBAGENT (FULL SCREEN ONLY)
- **MANDATORY ENGINE: ALWAYS USE NATIVE `browser_subagent`**:
  - For all browser-based tasks (LinkedIn notifications monitoring, job searches, feed inspection, and applying to jobs), the agent **MUST ALWAYS USE THE NATIVE `browser_subagent` TOOL** (the interactive engine used during website testing and the GATE 2027 application).
  - **NEVER execute invisible background Node.js/Puppeteer CLI scripts via bash (`run_command`) for browser interactions**. The user must always see the live interactive UI card ("Explored 1 browser"), real-time click/input actions, and visual screenshots in the chat interface.
- **Website Testing Browser Engine**: Use the browser architecture used during website testing (Chromium / Playwright engine with anti-bot stealth hooks). The previous rule binding execution to `AutoApply/linkedin-profile` is permanently removed.
- **MANDATORY FULL SCREEN (NEVER HALF SCREEN)**:
  - The browser **MUST ALWAYS BE LAUNCHED IN FULL SCREEN** (`--start-maximized`, `1920x1080` resolution, `defaultViewport: null` or `{ width: 1920, height: 1080 }`).
  - **NEVER use half screen, narrow split view, or mobile viewports** (e.g. `590x829`). Full desktop visibility ensures all navigation bars, filters, and Easy Apply dialogs render properly.
- **HTTP 503 ERROR AUTO-RECOVERY PROTOCOL**:
  - Whenever an HTTP 503 error occurs (e.g. server capacity outage or model unavailable during browser operations), **DO NOT prompt or stop**. The agent MUST immediately close and reopen the browser (terminating any stale browser processes, cleaning up lock files, and relaunching full screen on port 9222 / fresh context) and continue execution.

---

## 3. MANDATORY PIPELINE SEQUENCE: FEED FIRST (STRICTLY 40 POSTS) ➔ APPLY IMMEDIATELY
Always execute the application pipeline in this exact order:
1. **Step 1 (Feed Inspection - 40 Posts Limit)**: Navigate to `https://www.linkedin.com/feed/` and extract strictly the first **40 posts**.
2. **Step 2 (Relevance Evaluation)**: Analyze each post for software engineering, full-stack, AI, backend, and frontend opportunities (founder hiring announcements, direct job links, recruiter posts).
3. **Step 3 (Apply First)**: If any relevant opportunity is identified in the 40 feed posts, **APPLY TO THEM FIRST** before moving to the job search.

---

## 4. LINKEDIN JOB SEARCH ENGINE (INTERN, FRESHER, 0–2 YEARS EXP) & MANDATORY SKILL RELEVANCE GATE
After completing the 40 feed posts and submitting any relevant applications:
- **Navigate Directly to Job Search**: Open `https://www.linkedin.com/jobs/search/`.
- **Strict Experience Filters**: Target **Internship (`f_E=1`)**, **Entry Level / Fresher (`f_E=2`)**, and **0 to 2 years experience**.
- **Keywords**: Software Developer, Software Engineer, Full-Stack Developer, AI Engineer, Backend Developer, Frontend Developer.
- **Time Posted**: Past 24 hours (`f_TPR=r86400`) to target newly opened listings.
- **Location**: India / Remote (`f_WT=2`).
- **Exhaustive Application ("Zero Miss Guarantee")**:
  - **Easy Apply Roles**: Auto-fill multi-step modal and submit directly.
  - **External ATS / Company Websites**: Navigate to external ATS portals (Greenhouse, Lever, Ashby, Workday). Fill standard applicant fields and attach tailored resume. Capture link in `linkedin_tracker.json` (`external_link_captured`).

### MANDATORY SKILL RELEVANCE GATE: NEVER APPLY TO JOBS UNRELATED TO SAURABH'S SKILLS
- **Absolute Prohibition**: The agent **MUST NEVER APPLY** for any job whose required skills and tech stack are not relevant to Saurabh's verified skillset.
- **Saurabh's Verified Skill Domains (Apply ONLY if matching one of these tracks)**:
  1. **Full-Stack / Web Development**: React, Node.js, Express.js, MongoDB, TypeScript, JavaScript (ES6+), RESTful APIs, WebSockets, HTML/CSS.
  2. **AI & Agentic Systems**: Model Context Protocol (MCP), Python, PyTorch, LangChain, LangGraph, LLM fine-tuning, RAG pipelines, Mechanistic Interpretability, Sparse Autoencoders, FastMCP, FastAPI.
  3. **Silicon / Hardware / VLSI**: RISC-V RV32E, Verilog, SkyWater 130nm, Magic VLSI, OpenROAD STA, Tiny Tapeout.
  4. **Core Computer Science & Systems**: Data structures, algorithms, C++, SQL, Linux, Git, Docker, microservices.
- **Strictly Forbidden / Unrelated Domains (INSTANT REJECT & SKIP)**:
  - **Blockchain / Web3 / Crypto / Tokenization / Smart Contracts / Solidity / DeFi**: Completely unrelated to Saurabh's skills.
  - **Salesforce CRM / SAP / ERP Administration / ServiceNow**.
  - **Native Mobile iOS (Swift) or Native Android (Kotlin)** (unless specifically React Native / fullstack).
  - **Game Development** (Unity, Unreal Engine).
  - **Non-CS / Non-Software Disciplines** (Civil, Mechanical, Electrical power, Sales, Marketing, BPO).
- **Concrete Negative Example (Permanently Forbidden & Never To Be Repeated)**:
  - *The Mistake*: Applying for *"Blockchain Tokenization Engineering Intern"* (or any Web3, Solidity, or tokenization opening) simply because it appeared in search results for "Software Developer" with an Easy Apply button. Saurabh has zero blockchain background, credentials, or projects. Applying to such roles is misleading, irrelevant, and strictly forbidden. The agent MUST evaluate the actual job description and immediately SKIP any blockchain, Web3, or domain-mismatched listing.

---

## 5. OPTIONAL FOLLOW-UP: LINKEDIN NOTIFICATIONS (AGENT DISCRETION)
- There is **no requirement** to visit notifications prior to Job Search.
- After completing the 40 feed posts and the exhaustive job search, the agent may optionally visit `https://www.linkedin.com/notifications/?filter=jobs_all` to inspect additional alert recommendations and apply at its own discretion.
- **Recency Priority**: If checking notifications, always sort and process by age (newest/freshest first e.g. posted 5m, 30m, 1h ago).

---

## 6. MANDATORY RECRUITER FOLLOW-UP & OUTREACH PHASE (NEVER SKIP BEFORE NEXT DISCOVERY)
Recruiter and hiring manager follow-up is a **MANDATORY PHASE** of every job application run, never to be skipped or treated as optional:
- **Direct Email Follow-Up**: Whenever a recruiter or hiring manager email is identified in the posting or company domain (e.g. `faiza@softnice.com`, `prateek@fairdeal.market`), immediately dispatch a personalized, professional follow-up note with Saurabh's tailored resume attached via the Gmail REST API.
- **LinkedIn InMail / Direct Message**: Whenever the job poster or hiring manager LinkedIn profile is visible on the posting, immediately dispatch a personalized outreach message highlighting key project achievements (HavenTo, StudyMate) and linking to live demos:
  - Portfolio: https://my-portfolio-delta-two-55.vercel.app
  - GitHub: https://github.com/saurabh-kumar135
- **Post-Submission Outreach**: For every submitted application (both Easy Apply and external ATS), systematically identify the hiring lead/recruiter and execute the follow-up outreach touchpoint.
- **Strict Deduplication & Tracking**: Record each outreach event in `linkedin_tracker.json` (`recruiters` and `recruiters_contacted`). Never send duplicate messages to any recruiter.
- **ENFORCED SEQUENTIAL GATE**:
  - The agent **MUST NOT** proceed to the next feed scan, job search, or scheduled cycle while there are newly submitted applications with pending recruiter follow-ups.
  - Required sequence: Application Submitted ➔ Identify Recruiter / Poster ➔ Send Direct Email (with resume) OR Dispatch LinkedIn InMail (with portfolio/GitHub) ➔ Log in `linkedin_tracker.json` ➔ ONLY THEN proceed to subsequent stages.

---

## 7. REGULAR GMAIL LEAD & INTERVIEW MONITORING
- Regularly query the Gmail REST API (over HTTPS via OAuth2 refresh token from `StudyMate/.env`) for:
  - Recruiter replies and screening requests.
  - Interview invitations (`"schedule a call"`, `"interview"`).
  - Coding challenges (`"hackerrank"`, `"assessment"`).
  - Application status updates and confirmations.
- Automatically update `linkedin_tracker.json` and highlight actionable leads.

---

## 7B. MANDATORY RECRUITER & ASSIGNMENT DUE-DILIGENCE AUDIT GATE (SWEATSHOP & EXPLOITATION PREVENTION)
**BINDING DIRECTIVE: Never blindly build or write code for any inbound recruiter task or interview assignment before completing this mandatory audit!**  
Whenever an inbound recruiter, founder, or company replies to an application, invites Saurabh to a Slack/meeting, or assigns a take-home project, test task, or trial assignment:  
The agent **MUST HALT all code-writing and execution** and FIRST execute this 4-step forensic investigation:

1. **Calendar Invite & Attendee Forensic Audit (via Gmail REST API / Browser)**:
   - Query the Google Calendar / Google Meet invitation payload.
   - Inspect the guest list and sender address.
   - **SWEATSHOP TRIGGER FLAGS**:
     * Sender uses a personal email (`@gmail.com`, `@yahoo.com`) instead of an official company domain (`@company.com`).
     * The attendee list contains **mass student invites** (e.g. 10 to 30+ `@gmail.com` addresses with 2004–2006 birth years or college handles).
     * Senders invite candidates to daily internal "standups" or "morning synchs" alongside dozens of other students before any formal interview.

2. **Assignment Document Forensic Audit**:
   - Inspect the assignment file (`.docx`, `.pdf`) metadata, author name, and subtitle.
   - Check for recycled student names (e.g., `Pal-InfinityXZ-Advisor-Dashboard.docx` mentioning "Pal Pathak · Frontend Engineering Track September 2026").
   - **Scope Evaluation**: If the assignment requires building an entire production-grade commercial platform (>3 pages, full database schemas, live video, charts) within 24–48 hours under the guise of an "interview test", flag it as **UNPAID LABOR HARVESTING**.

3. **Public Entity & Employment Terms Verification**:
   - Search company registration, pre-revenue status, Glassdoor, Reddit, and job boards.
   - Check if job postings classify the role as an "Unpaid Internship" or "Pre-Revenue Startup."

4. **Mandatory Protective Warning & User Decision Gate**:
   - If red flags are detected, the agent **MUST NOT START BUILDING THE PROJECT**.
   - The agent MUST immediately present a structured **"EXPLOITATION / SWEATSHOP RISK AUDIT"** to Saurabh with all captured evidence (mass student guest list, personal Gmail, recycled assignment docs, unpaid status).
   - The agent MUST explicitly ask Saurabh:
     *"This opportunity exhibits severe indicators of an unpaid intern sweatshop / free labor harvesting. Do you want to decline/push back for a paid contract, or do you strictly want to build this for your personal portfolio on your own terms?"*
   - The agent proceeds ONLY after Saurabh explicitly acknowledges the risk and decides how to proceed.

---

## 8. VERIFIED STANDARD ANSWERS & ZERO FABRICATION
- Strictly use verified resume: `/home/saurabh-kumar123/Desktop/Desktop/express/saurabh_resume.pdf`.
- Never fabricate credentials, education details, or unauthorized information.
- **Verified Standard Answers (Auto-Fill Without Asking)**:
  - **Current Salary / CTC (in LPA)**: Always enter **`0`** (Fresher / Student status).
  - **Notice Period (in Days)**: Always enter **`0`** (Immediate Joiner).
  - **Work Authorization in India**: Always select **`Yes`** (Legally authorized).
  - **Visa Sponsorship Required**: Always select **`No`** (Does not require sponsorship).
  - **Location / City**: Always enter **`Lucknow`** or **`India`**.
  - **Phone Number**: Always enter **`7668476462`** (Country code: `+91`).
  - **Email Address**: Always verify **`saurabhrajput.25072005@gmail.com`**.
  - **Education**: Dr. APJ Abdul Kalam Technical University (AKTU), B.Tech CSE (2023–2027), CGPA: 7.26.
- **Safety Safeguard**: Pause and prompt user confirmation ONLY if a genuinely unverified or novel question appears.

---

## 9. MANDATORY DEEP-SEARCH HISTORY MINING & DYNAMIC PROJECT/SKILL TAILORING
- When evaluating any job posting (e.g. AI Engineer, Systems Engineer, Backend, MLOps, Hardware/VLSI) whose required skills and project domains are NOT present in Saurabh's default resume (`saurabh_resume.pdf`), the agent **MUST PERFORM A DETAILED SYSTEM HISTORY SEARCH** across Saurabh's entire machine before applying:
  - Search ChatGPT conversation archives, Claude context, Antigravity IDE trajectories, local repositories, notebooks, and MCP servers.
  - Dynamically highlight real, verified projects (MCP Ecosystem, LLM Fine-Tuning & Mechanistic Interpretability, SkyWater 130nm ASIC design).
  - Incorporate relevant technical skills into the Technical Skills section if there is a 10–20% mismatch.
  - Maintain the authentic 80–90% core (AKTU education, verified projects HavenTo & StudyMate, GitHub, portfolio).
  - Recompile LaTeX resume source (`pdflatex`) to generate optimized PDF and submit.
  - Provide direct repository, notebook, and demo URLs rather than generic profile links.
