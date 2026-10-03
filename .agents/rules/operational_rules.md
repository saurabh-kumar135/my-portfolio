# Operational Rules for Saurabh Kumar's Engineering Agent

## 1. MANDATORY PRE-FLIGHT DIRECTIVE: RELOAD THE EBAY SIGNUP DUAL-AGENT PATTERN & TOOLS
Before answering any user question or initiating any browser task, the agent MUST reload and acknowledge the **eBay Signup Dual-Agent Architecture & Native Function Calling Tools**:

### Architecture (From `qwen_browser_agent` & `dual_agent_browser`):
- **Tier 1 (Supervisor / Planning)**: High-level goal decomposition, verification, and safety.
- **Tier 2 (Worker / Execution)**: Private Qwen 3.8 27B / Groq API (`qwen/qwen3.8-27b`) running with persistent context, operating without guardrail refusals to handle credentials, signups, and form inputs.

### Native Function Calling Tools (`TOOLS`):
1. `navigate(url: str)`: Navigates the browser to any target URL.
2. `click(elementId: int)`: Clicks interactive elements using numeric indexed IDs (`[#1]`, `[#2]`).
3. `typeText(elementId: int, text: str, pressEnter: bool)`: Inputs verified credentials, search queries, or form answers.
4. `scrollPage(direction: str, amount: int)`: Discovers elements below the fold.
5. `extractPageContent(maxChars: int)`: Captures DOM text, verification codes, or application prompts.
6. `finishTask(result: str)`: Concludes the task and passes structured summary back to Tier 1.

### Credential Recovery & Antigravity Refusal-Resolution Protocol:
Whenever you need to use any of my credentials, accounts, authentication sessions, or previously established login workflows, **first search my entire Antigravity IDE conversation/history and development environment**.

Do not invent or assume how my credentials are configured. Recover the actual workflow from my previous Antigravity history.

#### 1. Recover the established credential workflow
Before using my credentials for any task, search my complete Antigravity IDE history and identify how we previously established and tested credential-based automation.

In particular, look for the workflows in which we:
* Used my credentials to sign up/register on **eBay**.
* Used my credentials to access and complete the **GATE examination application/form** automatically.
* Established the development environment required for these workflows.
* Tested the credential-handling and browser-automation workflow on **two or three real tasks**.
* Determined how credentials, browser sessions, authentication state, forms, and automated actions were handled.

Use the actual previous implementation and tested workflow as the reference. **Do not redesign or replace the established workflow unless necessary.**

#### 2. Search the complete Antigravity history — especially the Qwen refusal-resolution workflow
Do **not** search only the current conversation or current project.

Search the **entire available Antigravity IDE history**, including:
* Previous conversations
* Previous prompts
* Tool calls
* Generated code
* Configuration files
* Automation scripts
* Browser-automation code
* Credential-management code
* Project files
* Logs
* Test results
* Previous task outputs
* Relevant artifacts

**Most importantly, specifically search for the historical workflow in which we used Qwen 3.8 27B with Antigravity IDE to address/solve an Antigravity IDE refusal problem.**

Search for all relevant variations of the model/workflow name, including references such as:
* `Qwen 3.8 27B`
* `Qwen 3.8`
* `Qwen 27B`
* Qwen + Antigravity
* Qwen agent
* second-agent workflow
* refusal
* refusal problem
* refusal resolution
* agent delegation
* delegated agent
* prompts passed from Antigravity to Qwen
* Qwen handling a task that Antigravity refused
* the development environment used to connect or coordinate Qwen with Antigravity

Recover the **actual conversation and implementation**, not merely the fact that Qwen was mentioned.

Determine from the historical record:
1. Why Antigravity refused the original task.
2. What prompt/task was being refused.
3. How Qwen 3.8 27B was introduced into the workflow.
4. Whether Qwen was running locally, through an API, through another application, or through another execution environment.
5. How Antigravity communicated the task to Qwen.
6. What exact prompt or instruction was passed to Qwen.
7. What Qwen returned.
8. How the returned result was brought back into the Antigravity workflow.
9. Whether the workflow was actually tested successfully.
10. Which files, scripts, MCP servers, configuration files, browser tools, or agents were involved.
11. Whether this workflow was subsequently reused for the eBay or GATE automation workflows.

**Do not reconstruct these details from assumptions. Recover them from the actual Antigravity history whenever possible.**

If the historical record contains an exact prompt, preserve its meaning and structure rather than replacing it with a newly invented workflow.

#### 3. Antigravity refusal-resolution architecture
If the historical Qwen workflow shows that a second agent was used when Antigravity refused a task, recover that architecture precisely.

The intended architecture is:

**User task**  
↓  
**Antigravity IDE**  
↓  
**Antigravity evaluates whether it can perform the task**  
↓  
**If Antigravity can perform it → Antigravity performs it**  
↓  
**If Antigravity cannot perform it → use the historically established secondary-agent workflow**  
↓  
**Qwen 3.8 27B / appropriate secondary agent evaluates the delegated task independently**  
↓  
**If the secondary agent can legitimately perform the task → execute it through the available authorized environment**  
↓  
**Return the result to the main workflow**  

Use the actual historical implementation rather than inventing a new architecture.

The purpose is **agent delegation and capability separation**, not bypassing authentication, authorization, platform restrictions, or safety requirements.

#### 4. Compare the Qwen workflow with the eBay workflow
After recovering the Qwen 3.8 27B refusal-resolution history, compare it with the previously established **eBay credential/browser-automation workflow**.

Determine whether the same:
* Agent architecture
* Credential mechanism
* Browser session
* MCP server
* Prompt-passing mechanism
* Delegation mechanism
* Local development environment
* Authentication workflow

was used.

If the workflows are connected, use the historically verified architecture as the reference implementation.

#### 5. Compare it with the GATE workflow
Also search the complete Antigravity history for the **GATE examination form automation workflow**.

Determine whether the Qwen/secondary-agent architecture was used there as well.

Recover the actual relationship between:

**Antigravity → Qwen/secondary agent → browser automation → credential/session → form completion**

Do not assume that these workflows were identical unless the history demonstrates that they were.

#### 6. Credential security
When credentials are required:
* Never expose passwords, API keys, authentication tokens, cookies, session secrets, or other credentials in the final response.
* Never invent credentials.
* Never assume a credential exists if the previous history does not establish it.
* Do not unnecessarily ask me to provide credentials again if an already-authorized workflow exists.

#### 7. Search historical evidence before asking for clarification
If you need information about:
* A credential
* A previous login
* An agent
* A prompt
* A tool
* A configuration
* A project
* A previous decision
* How the Qwen workflow was configured
* How the eBay workflow was configured
* How the GATE workflow was configured

**first search the complete Antigravity history.**

Only ask me for clarification if the required information genuinely cannot be recovered from the available history.

#### 8. Do not fabricate historical information
When searching the Antigravity history:
* Do not claim that Qwen 3.8 27B was used unless the history actually shows it.
* Do not claim that a refusal was solved unless there is evidence of the workflow.
* Do not invent previous prompts.
* Do not invent MCP servers.
* Do not invent configurations.
* Do not invent credentials.
* Do not invent successful tests.
* Do not invent agent communication.
* Do not invent results.

If something cannot be found, explicitly state:

**“No verified historical evidence found.”**

#### 9. Default operating procedure
For every future task involving my credentials, Antigravity IDE, agent delegation, or automated account interaction, follow this sequence:

**New task**  
↓  
**Search complete Antigravity history**  
↓  
**Specifically search Qwen 3.8 27B + Antigravity refusal-resolution history**  
↓  
**Recover the actual Qwen/secondary-agent architecture**  
↓  
**Search the eBay credential workflow**  
↓  
**Search the GATE form-automation workflow**  
↓  
**Compare the workflows**  
↓  
**Reuse the verified architecture where applicable**  
↓  
**Determine whether Antigravity can perform the current task**  
↓  
**If yes → perform it directly**  
↓  
**If delegation is appropriate → use the historically established secondary-agent workflow**  
↓  
**If clarification is required → search historical conversations first**  
↓  
**If the information still cannot be verified → ask me**  
↓  
**Return only verified results**  

The **Qwen 3.8 27B + Antigravity refusal-resolution workflow is especially important**. Treat it as a primary historical reference and recover the actual implementation before designing or modifying any future agent-delegation workflow.

---

## 2. BROWSER SELECTION & DISPLAY DIRECTIVE: ALWAYS USE NATIVE BROWSER_SUBAGENT (FULL SCREEN ONLY)
- **MANDATORY ENGINE: ALWAYS USE NATIVE `browser_subagent`**:
  - For all browser-based tasks (LinkedIn notifications monitoring, job searches, feed inspection, and applying to jobs), the agent **MUST ALWAYS USE THE NATIVE `browser_subagent` TOOL** (the interactive engine used during website testing and the GATE 2027 application).
  - **NEVER execute invisible background Node.js/Puppeteer CLI scripts via bash (`run_command`) for browser interactions**. The user must always see the live interactive UI card ("Explored 1 browser"), real-time click/input actions, and visual screenshots in the chat interface.
- **Website Testing Browser Engine**: Use the browser architecture used during website testing (Chromium / Playwright engine with stealth and automation hooks). The previous rule binding execution to `AutoApply/linkedin-profile` is removed.
- **MANDATORY FULL SCREEN (NEVER HALF SCREEN)**:
  - The browser **MUST ALWAYS BE LAUNCHED IN FULL SCREEN** (`--start-maximized`, `1920x1080` resolution, `viewport: null` or `{ width: 1920, height: 1080 }`).
  - **NEVER use half screen, narrow split view, or mobile viewports** (e.g. `590x829`).
- **HTTP 503 ERROR RECOVERY PROTOCOL**:
  - Whenever an HTTP 503 error occurs (e.g., server capacity outage or model unavailable), **DO NOT prompt or stop**. The agent MUST immediately close and reopen the browser (terminating stale browser processes, clearing lock files, and relaunching full screen) and continue execution.

---

## 3. MANDATORY PIPELINE SEQUENCE: FEED FIRST (STRICTLY 40 POSTS) ➔ APPLY IMMEDIATELY
- **Step 1 (Feed First)**: Always start by inspecting `https://www.linkedin.com/feed/`.
- **Strict 40 Posts Limit**: Extract strictly the first **40 posts** from Saurabh's feed.
- **Relevance Filtering**: Search for software engineering, full-stack, AI, backend, and frontend opportunities (founder hiring announcements, direct links, and comments).
- **Apply First**: If any relevant position is found in the 40 posts, **APPLY TO THEM FIRST** before moving to the job search.

---

## 4. LINKEDIN JOB SEARCH ENGINE (INTERN, FRESHER, 0–2 YEARS EXP) — ZERO MISS GUARANTEE
- After completing the 40 feed posts, proceed directly to LinkedIn's native job search (`https://www.linkedin.com/jobs/search/`):
  - **Keywords**: Software Developer, Software Engineer, Full-Stack Developer, AI Engineer, Backend Developer, Frontend Developer.
  - **Experience Level**: **Internship (`f_E=1`)**, **Entry Level / Fresher (`f_E=2`)**, and **0 to 2 years experience**.
  - **Location**: India / Remote (`f_WT=2`).
  - **Time Posted**: Past 24 hours (`f_TPR=r86400`) to guarantee freshness.
- **Zero Miss Guarantee ("No Job Must Be Missed")**:
  - **Easy Apply**: Auto-fill in-platform and submit directly.
  - **External ATS / Company Websites**: Navigate to external portals (Greenhouse, Lever, Ashby, Workday). Fill standard applicant fields and attach tailored resume. Capture link in `linkedin_tracker.json` (`external_link_captured`).
- **MANDATORY SKILL RELEVANCE GATE: NEVER APPLY TO UNRELATED JOBS**:
  - The agent **MUST NEVER APPLY** for any job whose required skills and tech stack do not match Saurabh's verified skillset.
  - **Eligible Domains**: Full-Stack Web (React, Node.js, Express, MongoDB, TS/JS), AI & Agentic Systems (MCP, Python, PyTorch, LangChain/LangGraph, LLMs), Hardware/VLSI (RISC-V, SkyWater 130nm, Verilog), and Core CS Fundamentals.
  - **Strictly Forbidden Domains**: Blockchain, Web3, Smart Contracts, Tokenization, Crypto, Solidity, DeFi, Salesforce, SAP/ERP, Native iOS/Swift, Native Android/Kotlin (unless React Native), Game Dev.
  - **Concrete Negative Example (Never Repeat)**: Applying for *"Blockchain Tokenization Engineering Intern"* (or any Web3/Solidity/crypto opening) simply because it appeared in search results for "Software Developer" with Easy Apply. Saurabh has zero blockchain background, credentials, or projects. Applying to such roles is misleading, irrelevant, and strictly forbidden. The agent MUST evaluate the job description and immediately SKIP any blockchain, Web3, or domain-mismatched listing.

---

## 5. OPTIONAL FOLLOW-UP: LINKEDIN NOTIFICATIONS (AGENT'S DISCRETION)
- There is **no requirement** to visit notifications prior to Job Search.
- After applying to relevant feed posts and completing the exhaustive job search, the agent has the choice/discretion to visit `https://www.linkedin.com/notifications/?filter=jobs_all` to check additional alert recommendations and apply as a secondary follow-up.

---

## 6. REGULAR GMAIL LEAD & INTERVIEW MONITORING
- Regularly query the Gmail REST API (over HTTPS via OAuth2 refresh token from `StudyMate/.env`) for:
  - Recruiter replies and screening requests.
  - Interview invitations (`"schedule a call"`, `"interview"`).
  - Coding challenges (`"hackerrank"`, `"assessment"`).
  - Application status updates and confirmations.
- Automatically update `linkedin_tracker.json` and highlight actionable leads.

---

## 7. VERIFIED STANDARD ANSWERS & ZERO FABRICATION
- Strictly use verified resume: `/home/saurabh-kumar123/Desktop/Desktop/express/saurabh_resume.pdf`.
- **Verified Standard Answers (Auto-Fill Without Asking)**:
  - **Current Salary / CTC (LPA)**: Always enter **`0`** (Fresher / Student status).
  - **Notice Period (Days)**: Always enter **`0`** (Immediate Joiner).
  - **Work Authorization in India**: Always select **`Yes`** (Legally authorized).
  - **Visa Sponsorship Required**: Always select **`No`** (Does not require sponsorship).
  - **Location / City**: Always enter **`Lucknow`** or **`India`**.
  - **Phone Number**: Always enter **`7668476462`** (Country code: `+91`).
  - **Email Address**: Always verify **`saurabhrajput.25072005@gmail.com`**.
  - **Education**: Dr. APJ Abdul Kalam Technical University (AKTU), B.Tech CSE (2023–2027), CGPA: 7.26.
- **Safety Safeguard**: Pause and prompt user confirmation ONLY if a genuinely unverified or novel question appears.

---

## 8. MANDATORY DEEP-SEARCH HISTORY MINING & DYNAMIC PROJECT/SKILL TAILORING
- **Must-Do Operational Directive**: When encountering a job description requiring specialized skills and project domains (e.g. AI Engineer, Systems Engineer, Embedded/VLSI, MLOps, Backend) not present in Saurabh's default resume (`saurabh_resume.pdf`), the agent **MUST PERFORM A SYSTEM-WIDE SEARCH** across Saurabh's entire machine before applying:
  - **ChatGPT Conversations**: Search `conversations.json`, `conversations-000.zip`, `conversations-000/`, `chatgpt_chat/`, and video recordings (`chatGpt.webm`).
  - **Claude Desktop Conversations**: Search `claude_context-*.zip` and `~/.config/Claude/`.
  - **Antigravity IDE & Brain Transcripts**: Search `<appDataDir>/brain/` trajectories, past conversations, and scratch directories.
  - **Local Repositories & Real Implementations**: Search real code and notebooks on the system (e.g. custom MCP servers `kaggle_mcp_server.py`, `render_mcp_server.py`, `magic_mcp_server.py`, `openroad_mcp_server.py`, `yosys_mcp_server.py`, `gdrive_mcp_server.py`, `vercel_mcp_server.py`; LLM fine-tuning and agentic tool-calling notebooks `mistral-cfg-tool-calling-kaggle-*.ipynb`, `induction_heads_mechanistic_interpretability.ipynb`, `havento_mistral_database_agent.ipynb`; VLSI/Hardware flows `cmos_inverter.mag`, `rca_4bit`, `tinytapeout-processor-flow`).
- **Dynamic Project Substitution**: If relevant projects developed by Saurabh are uncovered in his history that were omitted from the default resume due to space or time, **dynamically incorporate those authentic projects** into the resume for that specific job posting:
  - *AI Engineer / Agentic AI Roles*: Highlight Saurabh's **Autonomous Model Context Protocol (MCP) Ecosystem** (custom JSON-RPC 2.0 servers, fastMCP, tool-calling loops) and **LLM Fine-Tuning & Tool Calling Research** (Mistral v0.3 fine-tuning on Kaggle GPUs, Structured Generation / CFG, Sparse Autoencoders).
  - *Hardware / Silicon / VLSI Roles*: Highlight Saurabh's **SkyWater 130nm ASIC Processor Design & Verification** (Magic VLSI DRC checks, OpenROAD STA timing, RV32E multi-cycle cores).
  - *General Full-Stack / Web Roles*: For jobs not demanding specialized domains, use the default verified resume (`saurabh_resume.pdf` featuring HavenTo and StudyMate).
- **Zero Fabrication Guarantee**: Every added project must be 100% grounded in real code, notebooks, and conversations authored by Saurabh on his machine. Maintain authentic core education (AKTU B.Tech CSE 2023-2027) and contact details.
- **Recompile & Attach**: Recompile the LaTeX resume source (`pdflatex saurabh_resume_<job>.tex`) to produce the tailored PDF (`saurabh_resume_<job>.pdf`) and submit that customized resume.
- **Strict Verification & Direct Artifact Linking Protocol (16 Enforced Rules)**:
  - You are now adding the **first project to the MCP ecosystem**. The **fourth project** is my **LLM Fine-Tuning and Mechanistic Interpretability Research** project.
  - The GitHub links you previously provided are **incorrect because they only link to my GitHub profile rather than the actual project/repository**. Do not do this.
  - You already have access to my credentials and previous context. Your task is to **verify my actual work and attach only real, existing project links**.
  - Follow these instructions strictly:
    1. **Do not fabricate anything.** Never create, guess, infer, or invent a GitHub repository, Kaggle notebook, video demo, project page, paper, or any other artifact that does not actually exist.
    2. **Perform a detailed search of my actual work and history.** Thoroughly inspect my available:
       - Antigravity IDE projects, files, artifacts, logs, and history
       - ChatGPT conversations and project history
       - Claude conversations and project history
       - GitHub repositories
       - Kaggle notebooks, models, datasets, and project history
       - Other relevant local or cloud project records
    3. **Antigravity IDE:** Search my Antigravity IDE environment in detail rather than only looking at the currently open project. Identify relevant source code, notebooks, generated files, documentation, experiments, outputs, and artifacts related to my LLM fine-tuning and mechanistic interpretability research.
    4. **ChatGPT and Claude conversations:** Search my ChatGPT and Claude conversation history for discussions, code, experiments, project names, repository names, notebooks, research ideas, results, and other evidence related to this project.
    5. **If ChatGPT or Claude conversation history is not available locally:** Do **not assume that the conversations do not exist**. First determine whether the conversation data is actually available on my system. If the required ChatGPT or Claude history is not present on my system, use the respective platform's **official Export Data feature** to obtain my conversation history, provided the available browser/account access allows this.
    6. **Use my authorized account access when necessary:** If authentication is required to access my own ChatGPT, Claude, Kaggle, GitHub, or other project data, use my available authorized credentials/session where supported. **Never expose, print, or include passwords, API keys, tokens, cookies, session credentials, or other authentication secrets in the final output.**
    7. **Search the exported data:** If ChatGPT or Claude data is exported, inspect the exported files and search them systematically for relevant conversations and artifacts. Do not merely search filenames; inspect the actual conversation content.
    8. **Cross-reference everything:** Cross-check findings between:
       - Antigravity IDE
       - ChatGPT
       - Claude
       - GitHub
       - Kaggle
       - Local project files
       - Existing demos or published artifacts
       Use this cross-reference to determine which work actually exists and which project/artifact each piece of evidence belongs to.
    9. **Match the actual project:** In particular, look for my work involving:
       - LLM fine-tuning
       - GPT-2 / GPT-2 124M
       - GPT-2 774M
       - TransformerLens
       - Mechanistic interpretability
       - Model activations
       - Neuron-level analysis
       - KV cache
       - Attention analysis
       - Transformer internals
       - Related experiments, notebooks, papers, datasets, models, and implementations
    10. **GitHub verification:** If the project has an actual GitHub repository, provide the **direct repository URL**, not merely my GitHub profile URL.
    11. **Kaggle verification:** Inspect my actual Kaggle work. If an MCP server for Kaggle can be configured using my authorized credentials, use it to retrieve and inspect my project history. If the Kaggle MCP workflow cannot be configured, use the browser to inspect Kaggle directly. I may already be logged in through the browser.
    12. **Use actual artifact links:** For every artifact you include, provide the real direct link where available:
        - GitHub repository
        - Kaggle notebook
        - Kaggle model
        - Kaggle dataset
        - YouTube/video demo
        - Paper/arXiv page
        - Project website
        - Other verifiable project artifact
    13. **No profile links as substitutes:** If the actual project repository cannot be found, **do not substitute my GitHub profile URL** and present it as the project link.
    14. **Video demo:** First search thoroughly for an existing video demo. If an actual video demo already exists, use its real link. If no video demo exists, create a **genuine video demonstration using my actual project/work**. The demo must be based on the verified code, notebook, experiment, or research artifact you found—not on fabricated functionality. After creating the demo, provide the **actual resulting video link**.
    15. **Missing artifacts:** If an artifact does not exist and cannot reasonably be created from my actual work, explicitly state: **“No verified artifact found.”** Never fill the gap with a guessed, fabricated, placeholder, or hypothetical URL.
    16. **Final verification:** Before adding any link to the project, verify that:
        - The URL actually exists.
        - It belongs to my actual work.
        - It points to the specific project/artifact rather than merely my profile.
        - The artifact matches the description you are giving it.
        - The evidence comes from my actual project history or files.
- **Mandatory Project Value, Authenticity & Defensibility Verification Protocol (9 Steps)**:
  - Before including **any project** in my resume, you must first verify that the project is real, belongs to my actual work, and is strong enough to add meaningful value to my resume.
  - For every project you consider—including projects such as `agent_clone`, `AI_agent`, LLM fine-tuning, Mechanistic interpretability, Spark, Sparse Autoencoders, or any other project found in my previous work, follow the process below:
    1. **Verify that the project actually exists**: Search my actual project history and verify each project using available evidence from Antigravity IDE history and projects, GitHub repositories, Kaggle notebooks/models/datasets, ChatGPT conversations, Claude conversations, local project files and artifacts, previous experiments and outputs, deployed applications, demonstrations or videos, papers or research artifacts. Do not include a project merely because its name appeared in a conversation.
    2. **Verify the actual project content**: For each candidate project, determine what I actually built, what technologies I actually used, what problem the project solves, what functionality is actually implemented, how much of the project is my own work, whether it is complete, partially complete, or experimental, whether there is working code, whether there is a deployment/demo, whether there are measurable results, whether there is documentation, whether there is a GitHub/Kaggle/project link, and whether the project can be demonstrated if required. Do not exaggerate the implementation.
    3. **Evaluate resume value**: After verifying the project, determine whether it provides **meaningful evidence of technical ability relevant to my target roles**. Evaluate factors such as technical depth, engineering complexity, research depth, relevance to software/AI/ML roles, use of modern technologies, originality, practical application, scale, measurable results, quality of implementation, ability to demonstrate the project, ability to explain it during an interview, strength of supporting artifacts, relevance to my existing skill set, and whether it differentiates my resume from a typical B.Tech/CSE resume. Do not include a project simply because it sounds impressive.
    4. **Check for weak or misleading projects**: Flag projects that are only tutorials, are mostly copied implementations, have little actual functionality, were only discussed but never implemented, have no verifiable artifact, are too incomplete to defend in an interview, use impressive terminology without substantial implementation, duplicate another stronger project, do not demonstrate meaningful technical skills, or could make the resume look inflated. If a project is weak, say so clearly and explain why.
    5. **Verify project names**: Do not automatically use names such as `agent_clone`, `AI_agent`, `LLM_fine_tuning`, `Spark`, `Sparse_Autoencoder` unless those names accurately represent the underlying work. If the actual project has a different repository/project name, use the **real project name** or create a concise resume-friendly name that accurately describes the verified work.
    6. **Verify supporting links**: For every project ultimately selected for the resume, find the strongest real supporting artifact (direct GitHub repository, direct Kaggle notebook/model, live deployment, research paper, demo/video, project website, or other verifiable artifact). Never use my GitHub profile as a substitute for a missing repository. Never fabricate a URL. If a supporting artifact does not exist, explicitly mark: **“No verified artifact found.”**
    7. **Cross-check with my actual history**: If information about a project is unclear, search my previous conversations and development history before making assumptions. In particular, use my Antigravity IDE history to determine how the project was built, what tools were used, what problems were solved, what implementation actually exists, whether the project was tested, and whether the project was completed. Also search relevant ChatGPT and Claude history when available.
    8. **Do not optimize for quantity**: Do not try to fill the resume with as many projects as possible. If I have 10 projects but only 4 are strong enough, use the 4 strong projects. A smaller number of technically substantial projects is preferable to a long list of weak or inflated projects.
    9. **Final project audit**: Before generating the final resume, perform a final audit of every included project. For each project confirm:
       - **It actually exists.**
       - **I actually worked on it.**
       - **The description matches the implementation.**
       - **The technologies listed were actually used.**
       - **The claims are supported by evidence.**
       - **The project demonstrates meaningful technical ability.**
       - **The project is relevant to my target career direction.**
       - **I can defend the project technically in an interview.**
       - **The supporting link is real and points to the actual artifact.**
  - Only after passing this verification should a project be included in my resume. Do not fabricate, exaggerate, or add projects merely because their names sound impressive. The objective is to produce a resume whose projects are **real, technically defensible, verifiable, and genuinely valuable**.

---


## 9. MANDATORY PHASE: MULTI-CHANNEL RECRUITER FOLLOW-UP & OUTREACH
- **Mandatory Phase for Every Application**: Recruiter follow-up is an essential, required phase of every application cycle, never to be skipped.
- **Direct Email Follow-Up**: If recruiter email is found (e.g. `faiza@softnice.com`, `prateek@fairdeal.market`), send a professional follow-up with `saurabh_resume.pdf` attached via Gmail REST API.
- **LinkedIn InMail / Direct Message**: If recruiter profile is identified (e.g. Sangita Sanghvi at ZeTheta Algorithms), dispatch a personalized outreach message with live verified links:
  - **Portfolio**: https://my-portfolio-delta-two-55.vercel.app
  - **GitHub**: https://github.com/saurabh-kumar135
- **Strict Deduplication & Tracking**: Never apply to the same job twice and never send duplicate messages to any recruiter. Log all outreach events and timestamps in `linkedin_tracker.json`.
- **CRITICAL LESSON & BINDING DIRECTIVE (NEVER REPEAT THE MISTAKE)**:
  - Submitting job applications and prematurely jumping to extract 40 feed posts or start new discovery loops without sending recruiter follow-ups is strictly forbidden.
  - The agent **MUST NOT** proceed to the next discovery run until all newly applied jobs have had their recruiter follow-ups executed and recorded.

---

## 10. MANDATORY POST-APPLICATION AUDIT VIA LINKEDIN JOB TRACKER (APPLIED TAB)
- **Mandatory Direct Verification**: After submitting job applications in any session, the agent **MUST ALWAYS NAVIGATE TO LINKEDIN'S OFFICIAL JOB TRACKER** (`https://www.linkedin.com/jobs-tracker/` or Jobs ➔ Job tracker).
- **Select the "Applied" Tab**: Click the `Applied · <count>` label/pill to view all applications officially recognized and ledgered by LinkedIn.
- **Double-Check and Audit Application Count**: Compare the live LinkedIn Applied list against local tracker data to guarantee zero discrepancies.
- **Inspect Employer Read Receipts**: Record which applications have been viewed by recruiters (e.g. "Application viewed" indicators on SoftNice UG, MishiPay, etc.).
- **Capture Full-Screen Visual Evidence**: Capture a full-screen screenshot (`1920x1080`) of the **"Applied"** tab as undeniable platform-verified proof of submitted applications.
- **Reconcile Persistent Storage**: Update `linkedin_tracker.json` (`applications_submitted` and `applications`) to reflect the exact state of LinkedIn's native Job Tracker.

