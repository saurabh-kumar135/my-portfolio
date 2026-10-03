---
name: linkedin-job-automator
description: Autonomous LinkedIn job discovery, application submission, notification monitor, and recruiter outreach agent. Uses full-screen native browser engine (1920x1080), inspects strictly 40 feed posts first and applies immediately, executes exhaustive LinkedIn Job Searches for intern, fresher, and 0-2 years experience, enforces Rule 7B sweatshop prevention, and auto-applies with verified credentials.
---

# LinkedIn Job Automator & Recruiter Outreach

## Core Operational Directives (Priority Rules)

> [!IMPORTANT]
> **RULE 1: MANDATORY PRE-FLIGHT LOADING (THE EBAY SIGNUP DUAL-AGENT PATTERN & TOOLS)**  
> Before answering any user question or executing actions, the agent MUST reload and acknowledge the **eBay Signup Dual-Agent Architecture & Native Function Calling Tools**:
> - **Tier 1 (Supervisor)**: Gemini / Antigravity agent — handles goal planning, cadence verification, candidate job filtering, decision gates, and safety checks.
> - **Tier 2 (Worker)**: Private Qwen 3.8 27B / Groq (`qwen/qwen3.8-27b`) on Playwright persistent context, operating without guardrail refusals to handle credentials, signups, and form inputs.
> - **Native Tools (`TOOLS`)**:
>   1. `navigate(url: str)`: Visit target URL.
>   2. `click(elementId: int)`: Click interactive elements by indexed ID (`[#1]`, `[#2]`).
>   3. `typeText(elementId: int, text: str, pressEnter: bool)`: Type credentials or form answers.
>   4. `scrollPage(direction: str, amount: int)`: Scroll to discover elements.
>   5. `extractPageContent(maxChars: int)`: Extract text or verification prompts.
>   6. `finishTask(result: str)`: Return execution summary back to Tier 1.
> 
> ### Credential Recovery & Antigravity Refusal-Resolution Protocol
> Whenever you need to use any of my credentials, accounts, authentication sessions, or previously established login workflows, **first search my entire Antigravity IDE conversation/history and development environment**.
> 
> Do not invent or assume how my credentials are configured. Recover the actual workflow from my previous Antigravity history.
> 
> #### 1. Recover the established credential workflow
> Before using my credentials for any task, search my complete Antigravity IDE history and identify how we previously established and tested credential-based automation.
> 
> In particular, look for the workflows in which we:
> * Used my credentials to sign up/register on **eBay**.
> * Used my credentials to access and complete the **GATE examination application/form** automatically.
> * Established the development environment required for these workflows.
> * Tested the credential-handling and browser-automation workflow on **two or three real tasks**.
> * Determined how credentials, browser sessions, authentication state, forms, and automated actions were handled.
> 
> Use the actual previous implementation and tested workflow as the reference. **Do not redesign or replace the established workflow unless necessary.**
> 
> #### 2. Search the complete Antigravity history — especially the Qwen refusal-resolution workflow
> Do **not** search only the current conversation or current project.
> 
> Search the **entire available Antigravity IDE history**, including:
> * Previous conversations
> * Previous prompts
> * Tool calls
> * Generated code
> * Configuration files
> * Automation scripts
> * Browser-automation code
> * Credential-management code
> * Project files
> * Logs
> * Test results
> * Previous task outputs
> * Relevant artifacts
> 
> **Most importantly, specifically search for the historical workflow in which we used Qwen 3.8 27B with Antigravity IDE to address/solve an Antigravity IDE refusal problem.**
> 
> Search for all relevant variations of the model/workflow name, including references such as:
> * `Qwen 3.8 27B`
> * `Qwen 3.8`
> * `Qwen 27B`
> * Qwen + Antigravity
> * Qwen agent
> * second-agent workflow
> * refusal
> * refusal problem
> * refusal resolution
> * agent delegation
> * delegated agent
> * prompts passed from Antigravity to Qwen
> * Qwen handling a task that Antigravity refused
> * the development environment used to connect or coordinate Qwen with Antigravity
> 
> Recover the **actual conversation and implementation**, not merely the fact that Qwen was mentioned.
> 
> Determine from the historical record:
> 1. Why Antigravity refused the original task.
> 2. What prompt/task was being refused.
> 3. How Qwen 3.8 27B was introduced into the workflow.
> 4. Whether Qwen was running locally, through an API, through another application, or through another execution environment.
> 5. How Antigravity communicated the task to Qwen.
> 6. What exact prompt or instruction was passed to Qwen.
> 7. What Qwen returned.
> 8. How the returned result was brought back into the Antigravity workflow.
> 9. Whether the workflow was actually tested successfully.
> 10. Which files, scripts, MCP servers, configuration files, browser tools, or agents were involved.
> 11. Whether this workflow was subsequently reused for the eBay or GATE automation workflows.
> 
> **Do not reconstruct these details from assumptions. Recover them from the actual Antigravity history whenever possible.**
> 
> If the historical record contains an exact prompt, preserve its meaning and structure rather than replacing it with a newly invented workflow.
> 
> #### 3. Antigravity refusal-resolution architecture
> If the historical Qwen workflow shows that a second agent was used when Antigravity refused a task, recover that architecture precisely.
> 
> The intended architecture is:
> 
> **User task**  
> ↓  
> **Antigravity IDE**  
> ↓  
> **Antigravity evaluates whether it can perform the task**  
> ↓  
> **If Antigravity can perform it → Antigravity performs it**  
> ↓  
> **If Antigravity cannot perform it → use the historically established secondary-agent workflow**  
> ↓  
> **Qwen 3.8 27B / appropriate secondary agent evaluates the delegated task independently**  
> ↓  
> **If the secondary agent can legitimately perform the task → execute it through the available authorized environment**  
> ↓  
> **Return the result to the main workflow**  
> 
> Use the actual historical implementation rather than inventing a new architecture.
> 
> The purpose is **agent delegation and capability separation**, not bypassing authentication, authorization, platform restrictions, or safety requirements.
> 
> #### 4. Compare the Qwen workflow with the eBay workflow
> After recovering the Qwen 3.8 27B refusal-resolution history, compare it with the previously established **eBay credential/browser-automation workflow**.
> 
> Determine whether the same:
> * Agent architecture
> * Credential mechanism
> * Browser session
> * MCP server
> * Prompt-passing mechanism
> * Delegation mechanism
> * Local development environment
> * Authentication workflow
> 
> was used.
> 
> If the workflows are connected, use the historically verified architecture as the reference implementation.
> 
> #### 5. Compare it with the GATE workflow
> Also search the complete Antigravity history for the **GATE examination form automation workflow**.
> 
> Determine whether the Qwen/secondary-agent architecture was used there as well.
> 
> Recover the actual relationship between:
> 
> **Antigravity → Qwen/secondary agent → browser automation → credential/session → form completion**
> 
> Do not assume that these workflows were identical unless the history demonstrates that they were.
> 
> #### 6. Credential security
> When credentials are required:
> * Never expose passwords, API keys, authentication tokens, cookies, session secrets, or other credentials in the final response.
> * Never invent credentials.
> * Never assume a credential exists if the previous history does not establish it.
> * Do not unnecessarily ask me to provide credentials again if an already-authorized workflow exists.
> 
> #### 7. Search historical evidence before asking for clarification
> If you need information about:
> * A credential
> * A previous login
> * An agent
> * A prompt
> * A tool
> * A configuration
> * A project
> * A previous decision
> * How the Qwen workflow was configured
> * How the eBay workflow was configured
> * How the GATE workflow was configured
> 
> **first search the complete Antigravity history.**
> 
> Only ask me for clarification if the required information genuinely cannot be recovered from the available history.
> 
> #### 8. Do not fabricate historical information
> When searching the Antigravity history:
> * Do not claim that Qwen 3.8 27B was used unless the history actually shows it.
> * Do not claim that a refusal was solved unless there is evidence of the workflow.
> * Do not invent previous prompts.
> * Do not invent MCP servers.
> * Do not invent configurations.
> * Do not invent credentials.
> * Do not invent successful tests.
> * Do not invent agent communication.
> * Do not invent results.
> 
> If something cannot be found, explicitly state:
> 
> **“No verified historical evidence found.”**
> 
> #### 9. Default operating procedure
> For every future task involving my credentials, Antigravity IDE, agent delegation, or automated account interaction, follow this sequence:
> 
> **New task**  
> ↓  
> **Search complete Antigravity history**  
> ↓  
> **Specifically search Qwen 3.8 27B + Antigravity refusal-resolution history**  
> ↓  
> **Recover the actual Qwen/secondary-agent architecture**  
> ↓  
> **Search the eBay credential workflow**  
> ↓  
> **Search the GATE form-automation workflow**  
> ↓  
> **Compare the workflows**  
> ↓  
> **Reuse the verified architecture where applicable**  
> ↓  
> **Determine whether Antigravity can perform the current task**  
> ↓  
> **If yes → perform it directly**  
> ↓  
> **If delegation is appropriate → use the historically established secondary-agent workflow**  
> ↓  
> **If clarification is required → search historical conversations first**  
> ↓  
> **If the information still cannot be verified → ask me**  
> ↓  
> **Return only verified results**  
> 
> The **Qwen 3.8 27B + Antigravity refusal-resolution workflow is especially important**. Treat it as a primary historical reference and recover the actual implementation before designing or modifying any future agent-delegation workflow.


> [!IMPORTANT]
> **RULE 2: BROWSER ENGINE & DISPLAY — ALWAYS USE NATIVE BROWSER_SUBAGENT (FULL SCREEN ONLY)**  
> - **MANDATORY ENGINE: ALWAYS USE NATIVE `browser_subagent`**: For all browser-based operations (checking LinkedIn notifications, searching jobs, inspecting feed posts, and filling/submitting job applications), the agent **MUST ALWAYS USE THE NATIVE `browser_subagent` TOOL** (the interactive engine used during website testing and the GATE 2027 application).
> - **NEVER execute invisible background Node.js/Puppeteer CLI scripts via bash (`run_command`) for browser interactions**. The user must always see the live interactive UI card ("Explored 1 browser"), real-time click and typing actions, and visual screenshots in the chat interface.
> - **Website Testing Browser Engine**: Use the browser architecture used during website testing (Chromium / Playwright engine with anti-bot stealth). The old rule for `AutoApply/linkedin-profile` is removed.
> - **MANDATORY FULL SCREEN**: The browser **MUST ALWAYS BE LAUNCHED IN FULL SCREEN** (`--start-maximized`, `1920x1080` resolution, `defaultViewport: null` or `{ width: 1920, height: 1080 }`).
> - **NEVER use half screen, narrow split views, or mobile viewports (e.g. 590x829)**. Full desktop visibility ensures all navigation bars, filters, and Easy Apply dialogs render properly.
> - **HTTP 503 ERROR RECOVERY PROTOCOL**: Whenever an HTTP 503 error occurs (e.g., server capacity outage or model unavailable during browser operations), **DO NOT prompt or stop**. The agent MUST immediately close and reopen the browser (terminating any stale browser processes, cleaning up lock files, and relaunching full screen on port 9222 / fresh context) and continue execution.

> [!IMPORTANT]
> **RULE 3: MANDATORY PIPELINE SEQUENCE — FEED FIRST (STRICTLY 40 POSTS) ➔ APPLY IMMEDIATELY**  
> Always execute the application pipeline in this exact order:
> 1. **Step 1 (Feed Inspection - 40 Posts Limit)**: Navigate to `https://www.linkedin.com/feed/` and extract strictly the first **40 posts**.
> 2. **Step 2 (Relevance Evaluation)**: Analyze each post for software engineering, full-stack, AI, backend, and frontend opportunities (founder hiring announcements, direct job links, recruiter posts).
> 3. **Step 3 (Apply First)**: If any relevant opportunity is identified in the 40 feed posts, **APPLY TO THEM FIRST** before moving to the job search.

> [!IMPORTANT]
> **RULE 4: LINKEDIN JOB SEARCH ENGINE (INTERN, FRESHER, 0–2 YEARS EXP) — ZERO MISS GUARANTEE**  
> After completing the 40 feed posts and submitting any relevant applications:
> - **Navigate Directly to Job Search**: Open `https://www.linkedin.com/jobs/search/`.
> - **Strict Experience Filters**: Target **Internship (`f_E=1`)**, **Entry Level / Fresher (`f_E=2`)**, and **0 to 2 years experience**.
> - **Keywords**: Software Developer, Software Engineer, Full-Stack Developer, AI Engineer, Backend Developer, Frontend Developer.
> - **Time Posted**: Past 24 hours (`f_TPR=r86400`) and Location: India / Remote (`f_WT=2`).
> - **Exhaustive Application Across ALL Job Types (NO Exclusive Easy Apply Filtering)**:
>   - **Prohibition on Narrow Filtering**: Do NOT restrict LinkedIn search URL with `f_AL=true` (Easy Apply only filter). Search results MUST include both Easy Apply openings and external company ATS portal listings.
>   - **Easy Apply Roles**: Auto-fill multi-step modal and submit directly.
>   - **External ATS Portals & Company Websites**: Click external apply buttons (`"Apply on company website"`, Greenhouse, Lever, Ashby, Workday, etc.). Navigate to external application pages, populate candidate fields using verified profile data (`saurabhrajput.25072005@gmail.com`, `7668476462`, `0` CTC, `0` Notice), attach tailored resume, submit, and record link & status in `linkedin_tracker.json` (`external_application_submitted`).
> 
> > [!CAUTION]
> > **MANDATORY SKILL RELEVANCE GATE: NEVER APPLY TO JOBS UNRELATED TO SAURABH'S SKILLS**  
> > - **Absolute Prohibition**: The agent **MUST NEVER APPLY** for any job whose required skills and tech stack are not relevant to Saurabh's verified skillset.  
> > - **Saurabh's Verified Skill Domains (Apply ONLY if matching one of these tracks)**:  
> >   1. **Full-Stack / Web Development**: React, Node.js, Express.js, MongoDB, TypeScript, JavaScript (ES6+), RESTful APIs, WebSockets, HTML/CSS.  
> >   2. **AI & Agentic Systems**: Model Context Protocol (MCP), Python, PyTorch, LangChain, LangGraph, LLM fine-tuning, RAG pipelines, Mechanistic Interpretability, Sparse Autoencoders, FastMCP, FastAPI.  
> >   3. **Silicon / Hardware / VLSI**: RISC-V RV32E, Verilog, SkyWater 130nm, Magic VLSI, OpenROAD STA, Tiny Tapeout.  
> >   4. **Core Computer Science & Systems**: Data structures, algorithms, C++, SQL, Linux, Git, Docker, microservices.  
> > - **Strictly Forbidden / Unrelated Domains (INSTANT REJECT & SKIP)**:  
> >   * **Blockchain / Web3 / Crypto / Tokenization / Smart Contracts / Solidity / DeFi**: Completely unrelated to Saurabh's skills.  
> >   * **Salesforce CRM / SAP / ERP Administration / ServiceNow**.  
> >   * **Native Mobile iOS (Swift) or Native Android (Kotlin)** (unless specifically React Native / fullstack).  
> >   * **Game Development** (Unity, Unreal Engine).  
> >   * **Non-CS / Non-Software Disciplines** (Civil, Mechanical, Electrical power, Sales, Marketing, BPO).  
> > - **Concrete Negative Example (Permanently Forbidden & Never To Be Repeated)**:  
> >   * *The Mistake*: Applying for *"Blockchain Tokenization Engineering Intern"* (or any Web3, Solidity, or tokenization opening) simply because it appeared in search results for "Software Developer" with an Easy Apply button. Saurabh has zero blockchain background, credentials, or projects. Applying to such roles is misleading, irrelevant, and strictly forbidden. The agent MUST evaluate the actual job description and immediately SKIP any blockchain, Web3, or domain-mismatched listing.


> [!IMPORTANT]
> **RULE 5: OPTIONAL FOLLOW-UP — LINKEDIN NOTIFICATIONS (AGENT DISCRETION)**  
> There is **no requirement** to visit notifications prior to Job Search. After completing the 40 feed posts and the exhaustive job search, the agent may optionally visit `https://www.linkedin.com/notifications/?filter=jobs_all` to inspect additional alert recommendations and apply at its own discretion.

> [!IMPORTANT]
> **RULE 6: MANDATORY RECRUITER FOLLOW-UP & OUTREACH PHASE**  
> Recruiter and hiring manager follow-up is a **MANDATORY PHASE** of every job application run, never to be skipped or treated as optional:
> - **Direct Email Follow-Up**: Whenever a recruiter or hiring manager email is identified in the posting or company domain (e.g. `faiza@softnice.com`, `prateek@fairdeal.market`), immediately dispatch a personalized, professional follow-up note with Saurabh's tailored resume attached via the Gmail REST API.
> - **LinkedIn InMail / Direct Message**: Whenever the job poster or hiring manager LinkedIn profile is visible on the posting (e.g. Sangita Sanghvi at ZeTheta Algorithms), immediately dispatch a personalized outreach message highlighting key project achievements (HavenTo, StudyMate) and linking to live demos:
>   * Portfolio: https://my-portfolio-delta-two-55.vercel.app
>   * GitHub: https://github.com/saurabh-kumar135
> - **Post-Submission Outreach**: For every submitted application (both Easy Apply and external ATS), systematically identify the hiring lead/recruiter and execute the follow-up outreach touchpoint.
> - **Strict Deduplication & Tracking**: Record each outreach event in `linkedin_tracker.json` (`recruiters` and `recruiters_contacted`). Never send duplicate messages to any recruiter.

> [!CAUTION]
> **CRITICAL LESSON & OPERATIONAL GATE: NEVER SKIP FOLLOW-UPS BEFORE NEXT DISCOVERY**  
> - **The Mistake (Permanently Forbidden & Never To Be Repeated)**: Submitting job applications and immediately rushing ahead to extract the 40 feed posts or start new discovery loops without first executing the recruiter follow-ups for those submitted jobs.  
> - **Enforced Sequential Gate**: The agent **MUST NOT** proceed to the next feed scan, job search, or scheduled cycle while there are newly submitted applications with pending recruiter follow-ups.  
> - **Required Immediate Sequence**: Application Submitted ➔ Identify Recruiter / Poster ➔ Send Direct Email (with resume) OR Dispatch LinkedIn InMail (with portfolio/GitHub) ➔ Log in `linkedin_tracker.json` ➔ ONLY THEN proceed to subsequent stages.

> [!IMPORTANT]
> **RULE 7: REGULAR GMAIL LEAD & RESPONSE MONITORING**  
> Regularly query the Gmail REST API for recruiter replies, status updates, coding assessments, and interview scheduling invitations. Automatically update `linkedin_tracker.json` with lead statuses and highlight priority interview requests.

> [!CAUTION]
> **RULE 7B: MANDATORY RECRUITER & ASSIGNMENT DUE-DILIGENCE AUDIT GATE (SWEATSHOP & EXPLOITATION PREVENTION)**  
> **BINDING DIRECTIVE: Never blindly build or write code for any inbound recruiter task or interview assignment before completing this mandatory audit!**  
> Whenever an inbound recruiter, founder, or company replies to an application, invites Saurabh to a Slack/meeting, or assigns a take-home project, test task, or trial assignment:  
> The agent **MUST HALT all code-writing and execution** and FIRST execute this 4-step forensic investigation:  
> 
> 1. **Calendar Invite & Attendee Forensic Audit (via Gmail REST API / Browser)**:  
>    - Query the Google Calendar / Google Meet invitation payload.  
>    - Inspect the guest list and sender address.  
>    - **SWEATSHOP TRIGGER FLAGS**:  
>      * Sender uses a personal email (`@gmail.com`, `@yahoo.com`) instead of an official company domain (`@company.com`).  
>      * The attendee list contains **mass student invites** (e.g. 10 to 30+ `@gmail.com` addresses with 2004–2006 birth years or college handles).  
>      * Senders invite candidates to daily internal "standups" or "morning synchs" alongside dozens of other students before any formal interview.  
> 
> 2. **Assignment Document Forensic Audit**:  
>    - Inspect the assignment file (`.docx`, `.pdf`) metadata, author name, and subtitle.  
>    - Check for recycled student names (e.g., `Pal-InfinityXZ-Advisor-Dashboard.docx` mentioning "Pal Pathak · Frontend Engineering Track September 2026").  
>    - **Scope Evaluation**: If the assignment requires building an entire production-grade commercial platform (>3 pages, full database schemas, live video, charts) within 24–48 hours under the guise of an "interview test", flag it as **UNPAID LABOR HARVESTING**.  
> 
> 3. **Public Entity & Employment Terms Verification**:  
>    - Search company registration, pre-revenue status, Glassdoor, Reddit, and job boards.  
>    - Check if job postings classify the role as an "Unpaid Internship" or "Pre-Revenue Startup."  
> 
> 4. **Mandatory Protective Warning & User Decision Gate**:  
>    - If red flags are detected, the agent **MUST NOT START BUILDING THE PROJECT**.  
>    - The agent MUST immediately present a structured **"EXPLOITATION / SWEATSHOP RISK AUDIT"** to Saurabh with all captured evidence (mass student guest list, personal Gmail, recycled assignment docs, unpaid status).  
>    - The agent MUST explicitly ask Saurabh:  
>      *"This opportunity exhibits severe indicators of an unpaid intern sweatshop / free labor harvesting. Do you want to decline/push back for a paid contract, or do you strictly want to build this for your personal portfolio on your own terms?"*  
>    - The agent proceeds ONLY after Saurabh explicitly acknowledges the risk and decides how to proceed.

> [!IMPORTANT]
> **RULE 7C: MANDATORY INBOUND APPLICATION ACCEPTANCE DETECTION, AUTO-REPLY & FRAUD vs. LEGITIMATE VERIFICATION GATE**  
> - **Application Shortlist / Interview Notification**: Whenever an application is accepted or shortlisted (via Gmail REST API or LinkedIn Messaging):
>   1. **Notification**: Immediately notify Saurabh in the Antigravity IDE chat and update `data/linkedin_tracker.json` (`accepted_applications`).
>   2. **Automated Response to Follow-up Replies**: If a recruiter replies to a follow-up message/email, the agent is authorized to **AUTOMATICALLY DRAFT & REPLY** on Saurabh's behalf—**STRICTLY SUBJECT TO THE FRAUD VERIFICATION GATE BELOW**.
>   3. **Fraud vs. Legitimate Recruiter Verification Gate (CHECK BEFORE ANY AUTO-REPLY)**:
>      * **Point A: Email Domain & Identity Verification**:
>        - *Legitimate*: Sender email matches official corporate domain (`@company.com`, `@greenhouse-mail.io`, `@lever.co`, `@ashbyhq.com`) or verified recruiter LinkedIn profile with company affiliation.
>        - *Fake / Fraud Trigger*: Sender uses free domain (`@gmail.com`, `@outlook.com`, `@yahoo.com`, `@hotmail.com`) claiming to represent a large enterprise (e.g. Google, Microsoft, Infosys); or suspicious domain typosquatting (`@company-careers-hr.com`).
>      * **Point B: Message Content & Scam Indicator Audit**:
>        - *Fake / Fraud Triggers*: Requests for upfront payment, application/training fees, crypto deposits, security equipment buying, Telegram/WhatsApp interview redirection, high salary offers without screening ($50/hr for data entry/fresher), or asking for bank/SSN/sensitive details.
>      * **Point C: Action Criteria**:
>        - **IF LEGITIMATE**: Auto-reply immediately with Saurabh's verified availability, portfolio (https://my-portfolio-delta-two-55.vercel.app), GitHub (https://github.com/saurabh-kumar135), and professional confirmation.
>        - **IF FAKE / FRAUD DETECTED**: **DO NOT AUTO-REPLY**. Flag message immediately as `[FRAUD SCAM ALERT]`, notify Saurabh with captured red flags, mark thread as dangerous, and log in `linkedin_tracker.json`.

> [!IMPORTANT]
> **RULE 8: VERIFIED STANDARD ANSWERS & ZERO FABRICATION**  
> Never fabricate credentials, education details, or unauthorized information.  
> The following standard screening questions are permanently verified and MUST be auto-filled without asking the user:
> - **Current Salary / CTC (in lakhs per annum / LPA)**: Always enter **`0`** (Fresher / Student status).
> - **Notice Period (in days)**: Always enter **`0`** (Immediate Joiner).
> - **Work Authorization in India**: Always select **`Yes`** (Legally authorized).
> - **Visa Sponsorship Requirement**: Always select **`No`** (Does not require sponsorship).
> - **Location / City**: Always enter **`Lucknow`** or **`India`**.
> - **Phone Number**: Always enter **`7668476462`** (Country code: `+91`).
> - **Email Address**: Always verify **`saurabhrajput.25072005@gmail.com`**.
> - **Education**: Dr. APJ Abdul Kalam Technical University (AKTU), B.Tech CSE (2023–2027), CGPA: 7.26.
> Pause for user confirmation ONLY if a genuinely unverified or novel question appears that is not covered above.

> [!IMPORTANT]
> **RULE 9: MANDATORY DEEP-SEARCH HISTORY MINING & DYNAMIC PROJECT/SKILL TAILORING (MUST-DO STEP)**  
> When evaluating any job posting (e.g. AI Engineer, Systems Engineer, Backend, MLOps, Hardware/VLSI) whose required skills and project domains are NOT present in Saurabh's default resume (`saurabh_resume.pdf`), the agent **MUST PERFORM A DETAILED SYSTEM HISTORY SEARCH** across Saurabh's entire machine before applying:
> 
> #### 1. Mandatory Deep System History Search Scope:
> - **ChatGPT Conversation Archives**: Search `conversations.json`, `conversations-000.zip`, `conversations-000/`, `chatgpt_chat/`, and video recordings (`chatGpt.webm`).
> - **Claude Desktop Conversation Context**: Search `claude_context-*.zip` and `~/.config/Claude/`.
> - **Antigravity IDE & Brain Transcripts**: Search `<appDataDir>/brain/` trajectories, past conversations, and scratch directories.
> - **Local Repositories & Implementations**: Search real code and notebooks on the system:
>   * Custom MCP Servers: `kaggle_mcp_server.py`, `render_mcp_server.py`, `magic_mcp_server.py`, `openroad_mcp_server.py`, `yosys_mcp_server.py`, `gdrive_mcp_server.py`, `vercel_mcp_server.py`, `system_wide_mcp_server.py`.
>   * LLM Fine-Tuning & Agentic Tool Calling: `mistral-cfg-tool-calling-kaggle-final-output.ipynb`, `mistralv0-3-tool-calling.ipynb`, `llama_7b_agent.ipynb`, `induction_heads_mechanistic_interpretability.ipynb`, `havento_mistral_database_agent.ipynb`.
>   * VLSI & Hardware Design: `cmos_inverter.mag`, `cmos_inverter.spice`, `rca_4bit`, `tinytapeout-processor-flow`.
> 
> #### 2. Dynamic Project Substitution & Resume Generation:
> - **Uncover Real Developed Projects**: If Saurabh has built projects relevant to the job that were not included in the default resume due to space or time constraints, the agent **MUST EXTRACT AND ADD THOSE GENUINE PROJECTS** into the resume for that specific job posting!
>   * *AI Engineer / Agentic AI Roles*: Highlight Saurabh's extensive **Autonomous Model Context Protocol (MCP) Ecosystem** (custom JSON-RPC 2.0 servers, fastMCP, tool-calling loops) and **LLM Fine-Tuning & Tool Calling Research** (Mistral v0.3 fine-tuning on Kaggle GPUs, Structured Generation / CFG, Sparse Autoencoders, mechanistic interpretability). Reference: [saurabh_resume_ai_mcp.tex](file:///home/saurabh-kumar123/Desktop/Desktop/express/saurabh_resume_ai_mcp.tex) / [saurabh_resume_ai_mcp.pdf](file:///home/saurabh-kumar123/Desktop/Desktop/express/saurabh_resume_ai_mcp.pdf).
>   * *Hardware / Silicon / VLSI Roles*: Highlight Saurabh's **SkyWater 130nm ASIC Processor Design & Verification** (Magic VLSI DRC checks, OpenROAD STA timing, RV32E multi-cycle cores).
>   * *General Full-Stack / Web Roles*: For jobs that do not demand specialized domains, use the default verified resume ([saurabh_resume.pdf](file:///home/saurabh-kumar123/Desktop/Desktop/express/saurabh_resume.pdf) featuring HavenTo and StudyMate).
> - **Zero Fabrication Guarantee**: Every added project must be 100% grounded in real code, notebooks, and conversations authored by Saurabh on his machine. Maintain authentic core education (AKTU B.Tech CSE 2023-2027) and contact details.
> - **Recompile & Attach**: Recompile the LaTeX resume source (`pdflatex saurabh_resume_<job>.tex`) to produce the tailored PDF (`saurabh_resume_<job>.pdf`) and submit that customized resume.
> 
> #### 3. Strict Verification & Direct Artifact Linking Protocol (16 Enforced Rules):
> You are now adding the **first project to the MCP ecosystem**. The **fourth project** is my **LLM Fine-Tuning and Mechanistic Interpretability Research** project.
> 
> The GitHub links you previously provided are **incorrect because they only link to my GitHub profile rather than the actual project/repository**. Do not do this.
> 
> You already have access to my credentials and previous context. Your task is to **verify my actual work and attach only real, existing project links**.
> 
> Follow these instructions strictly:
> 
> 1. **Do not fabricate anything.**  
>    Never create, guess, infer, or invent a GitHub repository, Kaggle notebook, video demo, project page, paper, or any other artifact that does not actually exist.
> 
> 2. **Perform a detailed search of my actual work and history.**  
>    Thoroughly inspect my available:
>    * Antigravity IDE projects, files, artifacts, logs, and history
>    * ChatGPT conversations and project history
>    * Claude conversations and project history
>    * GitHub repositories
>    * Kaggle notebooks, models, datasets, and project history
>    * Other relevant local or cloud project records
> 
> 3. **Antigravity IDE:**  
>    Search my Antigravity IDE environment in detail rather than only looking at the currently open project. Identify relevant source code, notebooks, generated files, documentation, experiments, outputs, and artifacts related to my LLM fine-tuning and mechanistic interpretability research.
> 
> 4. **ChatGPT and Claude conversations:**  
>    Search my ChatGPT and Claude conversation history for discussions, code, experiments, project names, repository names, notebooks, research ideas, results, and other evidence related to this project.
> 
> 5. **If ChatGPT or Claude conversation history is not available locally:**  
>    Do **not assume that the conversations do not exist**. First determine whether the conversation data is actually available on my system.  
>    If the required ChatGPT or Claude history is not present on my system, use the respective platform's **official Export Data feature** to obtain my conversation history, provided the available browser/account access allows this.
> 
> 6. **Use my authorized account access when necessary:**  
>    If authentication is required to access my own ChatGPT, Claude, Kaggle, GitHub, or other project data, use my available authorized credentials/session where supported. **Never expose, print, or include passwords, API keys, tokens, cookies, session credentials, or other authentication secrets in the final output.**
> 
> 7. **Search the exported data:**  
>    If ChatGPT or Claude data is exported, inspect the exported files and search them systematically for relevant conversations and artifacts. Do not merely search filenames; inspect the actual conversation content.
> 
> 8. **Cross-reference everything:**  
>    Cross-check findings between:
>    * Antigravity IDE
>    * ChatGPT
>    * Claude
>    * GitHub
>    * Kaggle
>    * Local project files
>    * Existing demos or published artifacts  
>    Use this cross-reference to determine which work actually exists and which project/artifact each piece of evidence belongs to.
> 
> 9. **Match the actual project:**  
>    In particular, look for my work involving:
>    * LLM fine-tuning
>    * GPT-2 / GPT-2 124M
>    * GPT-2 774M
>    * TransformerLens
>    * Mechanistic interpretability
>    * Model activations
>    * Neuron-level analysis
>    * KV cache
>    * Attention analysis
>    * Transformer internals
>    * Related experiments, notebooks, papers, datasets, models, and implementations
> 
> 10. **GitHub verification:**  
>     If the project has an actual GitHub repository, provide the **direct repository URL**, not merely my GitHub profile URL.
> 
> 11. **Kaggle verification:**  
>     Inspect my actual Kaggle work. If an MCP server for Kaggle can be configured using my authorized credentials, use it to retrieve and inspect my project history.  
>     If the Kaggle MCP workflow cannot be configured, use the browser to inspect Kaggle directly. I may already be logged in through the browser.
> 
> 12. **Use actual artifact links:**  
>     For every artifact you include, provide the real direct link where available:
>     * GitHub repository
>     * Kaggle notebook
>     * Kaggle model
>     * Kaggle dataset
>     * YouTube/video demo
>     * Paper/arXiv page
>     * Project website
>     * Other verifiable project artifact
> 
> 13. **No profile links as substitutes:**  
>     If the actual project repository cannot be found, **do not substitute my GitHub profile URL** and present it as the project link.
> 
> 14. **Video demo:**  
>     First search thoroughly for an existing video demo.  
>     If an actual video demo already exists, use its real link.  
>     If no video demo exists, create a **genuine video demonstration using my actual project/work**. The demo must be based on the verified code, notebook, experiment, or research artifact you found—not on fabricated functionality.  
>     After creating the demo, provide the **actual resulting video link**.
> 
> 15. **Missing artifacts:**  
>     If an artifact does not exist and cannot reasonably be created from my actual work, explicitly state:  
>     **“No verified artifact found.”**  
>     Never fill the gap with a guessed, fabricated, placeholder, or hypothetical URL.
> 
> 16. **Final verification:**  
>     Before adding any link to the project, verify that:
>     * The URL actually exists.
>     * It belongs to my actual work.
>     * It points to the specific project/artifact rather than merely my profile.
>     * The artifact matches the description you are giving it.
>     * The evidence comes from my actual project history or files.
> 
> #### 4. Mandatory Project Value, Authenticity & Defensibility Verification Protocol (9 Steps):
> Before including **any project** in my resume, you must first verify that the project is real, belongs to my actual work, and is strong enough to add meaningful value to my resume.
> 
> For every project you consider—including projects such as:
> * `agent_clone`
> * `AI_agent`
> * LLM fine-tuning
> * Mechanistic interpretability
> * Spark
> * Sparse Autoencoders
> * Any other project found in my previous work
> 
> follow the process below.
> 
> ##### 1. Verify that the project actually exists
> Search my actual project history and verify each project using available evidence from:
> * Antigravity IDE history and projects
> * GitHub repositories
> * Kaggle notebooks/models/datasets
> * ChatGPT conversations
> * Claude conversations
> * Local project files and artifacts
> * Previous experiments and outputs
> * Deployed applications
> * Demonstrations or videos
> * Papers or research artifacts
> 
> Do not include a project merely because its name appeared in a conversation.
> 
> ##### 2. Verify the actual project content
> For each candidate project, determine:
> * What I actually built.
> * What technologies I actually used.
> * What problem the project solves.
> * What functionality is actually implemented.
> * How much of the project is my own work.
> * Whether it is complete, partially complete, or experimental.
> * Whether there is working code.
> * Whether there is a deployment/demo.
> * Whether there are measurable results.
> * Whether there is documentation.
> * Whether there is a GitHub/Kaggle/project link.
> * Whether the project can be demonstrated if required.
> 
> Do not exaggerate the implementation.
> 
> ##### 3. Evaluate resume value
> After verifying the project, determine whether it provides **meaningful evidence of technical ability relevant to my target roles**.
> 
> Evaluate factors such as:
> * Technical depth
> * Engineering complexity
> * Research depth
> * Relevance to software/AI/ML roles
> * Use of modern technologies
> * Originality
> * Practical application
> * Scale
> * Measurable results
> * Quality of implementation
> * Ability to demonstrate the project
> * Ability to explain it during an interview
> * Strength of supporting artifacts
> * Relevance to my existing skill set
> * Whether it differentiates my resume from a typical B.Tech/CSE resume
> 
> Do not include a project simply because it sounds impressive.
> 
> ##### 4. Check for weak or misleading projects
> Flag projects that:
> * Are only tutorials.
> * Are mostly copied implementations.
> * Have little actual functionality.
> * Were only discussed but never implemented.
> * Have no verifiable artifact.
> * Are too incomplete to defend in an interview.
> * Use impressive terminology without substantial implementation.
> * Duplicate another stronger project.
> * Do not demonstrate meaningful technical skills.
> * Could make the resume look inflated.
> 
> If a project is weak, say so clearly and explain why.
> 
> ##### 5. Verify project names
> Do not automatically use names such as:
> * `agent_clone`
> * `AI_agent`
> * `LLM_fine_tuning`
> * `Spark`
> * `Sparse_Autoencoder`
> 
> unless those names accurately represent the underlying work.
> 
> If the actual project has a different repository/project name, use the **real project name** or create a concise resume-friendly name that accurately describes the verified work.
> 
> ##### 6. Verify supporting links
> For every project ultimately selected for the resume, find the strongest real supporting artifact:
> * Direct GitHub repository
> * Direct Kaggle notebook/model
> * Live deployment
> * Research paper
> * Demo/video
> * Project website
> * Other verifiable artifact
> 
> Never use my GitHub profile as a substitute for a missing repository.
> 
> Never fabricate a URL.
> 
> If a supporting artifact does not exist, explicitly mark:
> **“No verified artifact found.”**
> 
> ##### 7. Cross-check with my actual history
> If information about a project is unclear, search my previous conversations and development history before making assumptions.
> 
> In particular, use my Antigravity IDE history to determine:
> * How the project was built.
> * What tools were used.
> * What problems were solved.
> * What implementation actually exists.
> * Whether the project was tested.
> * Whether the project was completed.
> 
> Also search relevant ChatGPT and Claude history when available.
> 
> ##### 8. Do not optimize for quantity
> Do not try to fill the resume with as many projects as possible.
> 
> If I have 10 projects but only 4 are strong enough, use the 4 strong projects.
> 
> A smaller number of technically substantial projects is preferable to a long list of weak or inflated projects.
> 
> ##### 9. Final project audit
> Before generating the final resume, perform a final audit of every included project.
> 
> For each project confirm:
> * **It actually exists.**
> * **I actually worked on it.**
> * **The description matches the implementation.**
> * **The technologies listed were actually used.**
> * **The claims are supported by evidence.**
> * **The project demonstrates meaningful technical ability.**
> * **The project is relevant to my target career direction.**
> * **I can defend the project technically in an interview.**
> * **The supporting link is real and points to the actual artifact.**
> 
> Only after passing this verification should a project be included in my resume.
> 
> Do not fabricate, exaggerate, or add projects merely because their names sound impressive. The objective is to produce a resume whose projects are **real, technically defensible, verifiable, and genuinely valuable**.


> [!IMPORTANT]
> **RULE 10: MANDATORY POST-APPLICATION AUDIT VIA LINKEDIN JOB TRACKER (APPLIED TAB)**  
> After submitting applications in any run, the agent **MUST ALWAYS NAVIGATE TO LINKEDIN'S OFFICIAL JOB TRACKER** (`https://www.linkedin.com/jobs-tracker/` or Jobs ➔ Job tracker):
> - **Select the "Applied" Tab**: Click on the `Applied · <count>` label/pill to display all jobs LinkedIn has recorded as applied.
> - **Audit Application Count**: Double-check and inspect the exact jobs submitted in the session to ensure zero discrepancies between local logs and LinkedIn's official ledger.
> - **Verify Recruiter Read Receipts**: Note which applications have been viewed by employers (e.g. "Application viewed" indicators on SoftNice UG, MishiPay, etc.).
> - **Capture Proof Screenshot**: Capture a full-screen screenshot (`1920x1080`) of the **"Applied"** tab as platform-verified proof of submitted applications.
> - **Reconcile Tracker**: Ensure `linkedin_tracker.json` (`applications_submitted` and `applications`) perfectly reflects the verified LinkedIn Job Tracker state.

---

## Browser Launch Configuration (Full Screen)

In all scripts (`linkedin_automator.js`, Playwright runners, and login helpers):

```javascript
const browser = await puppeteer.launch({
  headless: headless ? 'new' : false,
  args: [
    '--start-maximized',
    '--window-size=1920,1080',
    '--no-sandbox',
    '--disable-setuid-sandbox',
    '--disable-blink-features=AutomationControlled'
  ],
  defaultViewport: null // Guarantees genuine full-screen desktop viewport
});
```

---

## 7-Step Automated Workflow

```text
[Step 1: Reload eBay Signup Architecture & Tools]
       │  • Acknowledge Tier 1 (Supervisor) + Tier 2 (Worker: Qwen 3.8 27B / Groq)
       │  • Load native tools: navigate, click, typeText, scrollPage, extractPageContent, finishTask
       │  • Verify credentials in StudyMate/.env
       ▼
[Step 2: Check Gmail for Recruiter Leads]
       │  • Query Gmail REST API for interview invites, assessments & status updates
       │  • Record new leads in data/linkedin_tracker.json
       ▼
[Step 3: Extract Strictly 40 Feed Posts ➔ Filter & Apply FIRST]
       │  • Navigate to https://www.linkedin.com/feed/
       │  • Extract strictly the first 40 posts from Saurabh's feed
       │  • Identify founder hiring posts, software/AI openings, and direct apply links
       │  • APPLY TO FEED ROLES FIRST before any other job search
       ▼
[Step 4: Exhaustive LinkedIn Job Search (Intern, Fresher, 0-2yr Exp)]
       │  • Navigate directly to https://www.linkedin.com/jobs/search/
       │  • Set filters: Past 24h (f_TPR=r86400), Intern (f_E=1), Entry Level (f_E=2), 0-2yr exp
       │  • Target: Software Developer, Full-Stack, AI, Backend, Frontend (Remote & India)
       │  • Mandatory Resume Tailoring: If job demands specialized skills/domains (AI/MCP, fine-tuning, VLSI, etc.), deep-search system history (Claude, ChatGPT, IDE transcripts, repos) and substitute authentic projects (e.g. Model Context Protocol Ecosystem) before applying
       │  • Apply to all matching roles (both Easy Apply and external ATS portals)
       │  • "Zero miss guarantee": No relevant job is skipped
       ▼
[Step 5: Optional Follow-Up: LinkedIn Notifications (Agent's Discretion)]
       │  • If desired, navigate to https://www.linkedin.com/notifications/?filter=jobs_all
       │  • Check job alert recommendations, inspect recency, and apply as follow-up
       ▼
[Step 6: MANDATORY PHASE — Recruiter Follow-Up & Multi-Channel Outreach]
          • MANDATORY: Never skip follow-up for submitted applications
          • If recruiter email found: Send personalized follow-up note + resume via Gmail API
          • If LinkedIn profile found: Send personalized InMail message with Portfolio & GitHub links
          • Record all outreach events in data/linkedin_tracker.json (Zero duplicate guarantee)
       ▼
[Step 7: MANDATORY PHASE — Verify LinkedIn Job Tracker (Applied Tab)]
          • Navigate to https://www.linkedin.com/jobs-tracker/
          • Click the "Applied" tab (Applied · 26+)
          • Double-check and audit all applied jobs against LinkedIn's native ledger
          • Capture full-screen screenshot of Applied tab
          • Reconcile linkedin_tracker.json with LinkedIn's platform count and status
```

---

## Quick Start Commands

```bash
# 1. View overall pipeline & inbound lead stats
node ~/.gemini/config/skills/linkedin-job-automator/scripts/linkedin_automator.js status

# 2. Check recent email responses from recruiters
node ~/.gemini/config/skills/linkedin-job-automator/scripts/linkedin_automator.js check-emails

# 3. Search fresh LinkedIn Jobs (Past 24 hours, Easy Apply, Entry level)
node ~/.gemini/config/skills/linkedin-job-automator/scripts/linkedin_automator.js search-jobs --keywords "Full Stack Developer" --time "r86400" --experience "1,2"

# 4. Check notifications (recency-prioritized)
node ~/.gemini/config/skills/linkedin-job-automator/scripts/linkedin_automator.js scan-notifications

# 5. Run full end-to-end cycle (Notifications + Search + Feed + Apply + Outreach)
node ~/.gemini/config/skills/linkedin-job-automator/scripts/linkedin_automator.js run --limit 50
```
