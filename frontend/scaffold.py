import os

pages = {
    "about.html": """
    <section class="section-padding text-center">
        <h1 style="font-family: var(--font-display); font-size: clamp(3rem, 5vw, 4.5rem); line-height: 1.05; margin-bottom: 32px;" class="fade-enter visible">Built by people who have stood where you stand.</h1>
        <p style="font-family: var(--font-serif); font-size: 1.2rem; color: var(--cream); max-width: 800px; margin: 0 auto 48px;" class="fade-enter visible">Beyond Bridge was created for professionals whose careers began in command, service, discipline, operations, and responsibility — and who now want to move into business leadership.</p>
    </section>
    <section style="background: var(--charcoal); border-top: 1px solid var(--border);">
        <div class="section-padding">
            <h2 style="font-family: var(--font-display); font-size: 2.5rem; margin-bottom: 32px; color: var(--cream);">The Insight</h2>
            <p style="color: var(--text-dim); margin-bottom: 24px; line-height: 1.8;">Beyond Bridge was born from a simple insight: many mariners and defence professionals are outstanding MBA candidates, but they often struggle to present their experience in a way that business schools immediately understand.</p>
            <p style="color: var(--text-dim); margin-bottom: 24px; line-height: 1.8;">A seafarer may have managed multinational crews, vessel operations, safety audits, crisis response, compliance, multimillion-dollar assets, vendor coordination, and global logistics. A defence professional may have led teams under pressure, managed resources, handled mission-critical operations, developed discipline, and built deep leadership maturity.</p>
            <p style="color: var(--cream); font-weight: 500; font-size: 1.2rem; margin-bottom: 48px;">These are not ordinary experiences. They are business-school-relevant experiences.</p>
            
            <h2 style="font-family: var(--font-display); font-size: 2.5rem; margin-bottom: 32px; color: var(--cream);">Our Positioning</h2>
            <p style="color: var(--text-dim); margin-bottom: 48px; line-height: 1.8;">We are ex-mariners and business-school graduates from elite institutions in India and abroad. After moving ashore, we built careers in strategy, operations, consulting, healthcare, supply chain, transformation, GCC/GBS, and leadership roles. We created Beyond Bridge to help the next generation of mariners and service professionals make the same shift with more clarity, confidence, and structure.</p>
            
            <h2 style="font-family: var(--font-display); font-size: 2.5rem; margin-bottom: 32px; color: var(--cream);">What Makes Us Different</h2>
            <ul style="color: var(--text-dim); line-height: 2; list-style: none; padding: 0;">
                <li style="margin-bottom: 16px; border-bottom: 1px solid var(--border); padding-bottom: 16px;"><strong style="color: var(--accent);">Specialist focus:</strong> We do not treat mariners and defence candidates as generic applicants.</li>
                <li style="margin-bottom: 16px; border-bottom: 1px solid var(--border); padding-bottom: 16px;"><strong style="color: var(--accent);">Lived experience:</strong> We understand sea life, service life, hierarchy, discipline, command, operational pressure, and transition anxiety.</li>
                <li style="margin-bottom: 16px; border-bottom: 1px solid var(--border); padding-bottom: 16px;"><strong style="color: var(--accent);">Business translation:</strong> We convert technical and operational experience into MBA-relevant leadership stories.</li>
                <li style="margin-bottom: 16px; border-bottom: 1px solid var(--border); padding-bottom: 16px;"><strong style="color: var(--accent);">Career-first approach:</strong> We help you think beyond admission — into roles, industries, compensation, geography, and long-term career direction.</li>
                <li style="margin-bottom: 16px; border-bottom: 1px solid var(--border); padding-bottom: 16px;"><strong style="color: var(--accent);">Practical guidance:</strong> No unnecessary jargon, no false promises, no over-selling. Only structured, honest, high-quality advisory.</li>
            </ul>
        </div>
    </section>
    """,
    "pathways.html": """
    <section class="section-padding text-center">
        <h1 style="font-family: var(--font-display); font-size: clamp(3rem, 5vw, 4.5rem); line-height: 1.05; margin-bottom: 32px;" class="fade-enter visible">Choose the MBA path that fits your experience, ambition, and life stage.</h1>
        <p style="font-family: var(--font-serif); font-size: 1.2rem; color: var(--cream); max-width: 800px; margin: 0 auto 48px;" class="fade-enter visible">For mariners and defence professionals, an MBA is not just another degree. It can be a structured route into strategy, consulting, operations, supply chain, leadership, entrepreneurship, and global business roles.</p>
    </section>
    <section style="background: var(--charcoal); border-top: 1px solid var(--border);">
        <div class="section-padding">
            <div class="grid-3">
                <div class="card">
                    <h3 style="font-family: var(--font-display); font-size: 1.5rem; margin-bottom: 16px; color: var(--accent);">Pathway 1: Indian One-Year / Exec MBA</h3>
                    <p style="color: var(--text-dim); line-height: 1.6; margin-bottom: 16px;">Best for experienced professionals seeking a fast, focused transition into leadership roles in India or emerging markets.</p>
                    <p style="color: var(--cream); font-size: 0.9rem;"><strong>Examples:</strong> ISB PGP, IIM one-year MBA, XLRI, SPJIMR.</p>
                </div>
                <div class="card">
                    <h3 style="font-family: var(--font-display); font-size: 1.5rem; margin-bottom: 16px; color: var(--accent);">Pathway 2: Global Full-Time MBA</h3>
                    <p style="color: var(--text-dim); line-height: 1.6; margin-bottom: 16px;">Best for candidates targeting global mobility, consulting, international business, leadership programs, or career change.</p>
                    <p style="color: var(--cream); font-size: 0.9rem;"><strong>Examples:</strong> INSEAD, LBS, Oxford, Cambridge, US MBAs.</p>
                </div>
                <div class="card">
                    <h3 style="font-family: var(--font-display); font-size: 1.5rem; margin-bottom: 16px; color: var(--accent);">Pathway 3: Executive MBA</h3>
                    <p style="color: var(--text-dim); line-height: 1.6; margin-bottom: 16px;">Best for senior professionals (Captains, senior defence officers) who want to continue working while studying.</p>
                </div>
                <div class="card">
                    <h3 style="font-family: var(--font-display); font-size: 1.5rem; margin-bottom: 16px; color: var(--accent);">Pathway 4: Specialized Master's</h3>
                    <p style="color: var(--text-dim); line-height: 1.6; margin-bottom: 16px;">Best for younger candidates or those seeking focused business knowledge in finance, analytics, supply chain, or international business.</p>
                </div>
                <div class="card">
                    <h3 style="font-family: var(--font-display); font-size: 1.5rem; margin-bottom: 16px; color: var(--accent);">Pathway 5: Transition Without MBA</h3>
                    <p style="color: var(--text-dim); line-height: 1.6; margin-bottom: 16px;">Not everyone needs an MBA immediately. Some candidates may be better served by a phased transition, certifications, or targeted networking.</p>
                </div>
            </div>
        </div>
    </section>
    """,
    "services.html": """
    <section class="section-padding text-center">
        <h1 style="font-family: var(--font-display); font-size: clamp(3rem, 5vw, 4.5rem); line-height: 1.05; margin-bottom: 32px;" class="fade-enter visible">End-to-end MBA admissions and career transition advisory.</h1>
        <p style="font-family: var(--font-serif); font-size: 1.2rem; color: var(--cream); max-width: 800px; margin: 0 auto 48px;" class="fade-enter visible">From profile diagnosis to school selection, essays, interviews, scholarships, and post-MBA career planning — we guide you with structure, clarity, and accountability.</p>
    </section>
    <section style="background: var(--charcoal); border-top: 1px solid var(--border);">
        <div class="section-padding">
            <div class="grid-3">
                <div class="card">
                    <h3 style="font-family: var(--font-display); font-size: 1.5rem; margin-bottom: 16px; color: var(--accent);">1. MBA Profile Diagnostic</h3>
                    <p style="color: var(--text-dim); font-size: 0.9rem;">Profile evaluation, academic review, career review, leadership mapping, test readiness, and recommended next steps.</p>
                </div>
                <div class="card">
                    <h3 style="font-family: var(--font-display); font-size: 1.5rem; margin-bottom: 16px; color: var(--accent);">2. Strategy & School Selection</h3>
                    <p style="color: var(--text-dim); font-size: 0.9rem;">Target school list, reach-fit-safe classification, geography selection, and career outcome mapping.</p>
                </div>
                <div class="card">
                    <h3 style="font-family: var(--font-display); font-size: 1.5rem; margin-bottom: 16px; color: var(--accent);">3. Personal Story Narrative</h3>
                    <p style="color: var(--text-dim); font-size: 0.9rem;">Deep-dive sessions to identify your leadership stories, transition logic, career goals, and why MBA.</p>
                </div>
                <div class="card">
                    <h3 style="font-family: var(--font-display); font-size: 1.5rem; margin-bottom: 16px; color: var(--accent);">4. Resume Transformation</h3>
                    <p style="color: var(--text-dim); font-size: 0.9rem;">MBA-format resume, technical-to-business translation, and school-specific refinement.</p>
                </div>
                <div class="card">
                    <h3 style="font-family: var(--font-display); font-size: 1.5rem; margin-bottom: 16px; color: var(--accent);">5. Essay & SOP Advisory</h3>
                    <p style="color: var(--text-dim); font-size: 0.9rem;">Essay brainstorming, storyline development, draft review, and admissions committee alignment.</p>
                </div>
                <div class="card">
                    <h3 style="font-family: var(--font-display); font-size: 1.5rem; margin-bottom: 16px; color: var(--accent);">6. LOR Strategy</h3>
                    <p style="color: var(--text-dim); font-size: 0.9rem;">Recommender selection, briefing, leadership examples, and guidance notes.</p>
                </div>
                <div class="card">
                    <h3 style="font-family: var(--font-display); font-size: 1.5rem; margin-bottom: 16px; color: var(--accent);">7. Interview Preparation</h3>
                    <p style="color: var(--text-dim); font-size: 0.9rem;">Mock interviews, behavioural questions, school fit, and final readiness feedback.</p>
                </div>
                <div class="card">
                    <h3 style="font-family: var(--font-display); font-size: 1.5rem; margin-bottom: 16px; color: var(--accent);">8. Scholarship Guidance</h3>
                    <p style="color: var(--text-dim); font-size: 0.9rem;">Scholarship essay review, positioning, education loan readiness, and ROI discussion.</p>
                </div>
                <div class="card">
                    <h3 style="font-family: var(--font-display); font-size: 1.5rem; margin-bottom: 16px; color: var(--accent);">9. Career Transition Advisory</h3>
                    <p style="color: var(--text-dim); font-size: 0.9rem;">Post-MBA options, industry mapping, LinkedIn positioning, and networking strategy.</p>
                </div>
                <div class="card">
                    <h3 style="font-family: var(--font-display); font-size: 1.5rem; margin-bottom: 16px; color: var(--accent);">10. Defence/Maritime Translation</h3>
                    <p style="color: var(--text-dim); font-size: 0.9rem;">Specialized translation of rank, command, audits, and compliance into business language.</p>
                </div>
            </div>
        </div>
    </section>
    """,
    "pricing.html": """
    <section class="section-padding text-center">
        <p style="font-size: 0.75rem; letter-spacing: 0.25em; color: var(--accent); text-transform: uppercase; margin-bottom: 24px;" class="fade-enter visible">Client Confidential</p>
        <h1 style="font-family: var(--font-display); font-size: clamp(3rem, 5vw, 4.5rem); line-height: 1.05; margin-bottom: 32px;" class="fade-enter visible">Packages & Pricing</h1>
        <p style="font-family: var(--font-sans); font-size: 1rem; color: var(--text-dim); max-width: 800px; margin: 0 auto 48px;" class="fade-enter visible">Beyond Bridge is an advisory platform. We do not guarantee admission, scholarship, or placement. Prices are introductory. Taxes/GST, if applicable, will be charged separately.</p>
    </section>
    <section style="background: var(--charcoal); border-top: 1px solid var(--border);">
        <div class="section-padding">
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(400px, 1fr)); gap: 40px;">
                <div class="card">
                    <h3 style="font-family: var(--font-display); font-size: 1.5rem; margin-bottom: 8px;">Free Discovery Call</h3>
                    <p style="font-size: 2rem; font-weight: 300; margin-bottom: 16px; color: var(--accent);">Free</p>
                    <p style="color: var(--text-dim); font-size: 0.9rem; margin-bottom: 16px;">60 minutes. Basic profile discussion and pathway suggestion.</p>
                    <a href="contact.html" class="btn-primary" style="text-decoration: none; display: inline-block;">Book Now</a>
                </div>
                <div class="card">
                    <h3 style="font-family: var(--font-display); font-size: 1.5rem; margin-bottom: 8px;">BridgeStart Diagnostic</h3>
                    <p style="font-size: 2rem; font-weight: 300; margin-bottom: 16px; color: var(--accent);">₹3,999</p>
                    <p style="color: var(--text-dim); font-size: 0.9rem; margin-bottom: 16px;">90 minutes. Serious assessment before committing. Fee adjusted if upgraded.</p>
                    <a href="contact.html" class="btn-primary" style="text-decoration: none; display: inline-block;">Book Now</a>
                </div>
                <div class="card">
                    <h3 style="font-family: var(--font-display); font-size: 1.5rem; margin-bottom: 8px;">Resume & LinkedIn</h3>
                    <p style="font-size: 2rem; font-weight: 300; margin-bottom: 16px; color: var(--accent);">₹9,999</p>
                    <p style="color: var(--text-dim); font-size: 0.9rem; margin-bottom: 16px;">MBA resume, corporate angle, LinkedIn positioning.</p>
                </div>
                <div class="card" style="border-color: var(--accent);">
                    <div style="position: absolute; top: 0; right: 48px; background: var(--accent); color: var(--dark); font-size: 0.65rem; font-weight: bold; letter-spacing: 0.1em; padding: 4px 12px; text-transform: uppercase; transform: translateY(-50%);">Popular</div>
                    <h3 style="font-family: var(--font-display); font-size: 1.5rem; margin-bottom: 8px;">Single School - India</h3>
                    <p style="font-size: 2rem; font-weight: 300; margin-bottom: 16px; color: var(--accent);">₹39,999</p>
                    <p style="color: var(--text-dim); font-size: 0.9rem; margin-bottom: 16px;">ISB, IIM one-year, SPJIMR, XLRI. Full strategy & 1 mock interview.</p>
                </div>
                <div class="card">
                    <h3 style="font-family: var(--font-display); font-size: 1.5rem; margin-bottom: 8px;">Three-School India Pack</h3>
                    <p style="font-size: 2rem; font-weight: 300; margin-bottom: 16px; color: var(--accent);">₹89,999</p>
                    <p style="color: var(--text-dim); font-size: 0.9rem; margin-bottom: 16px;">End-to-end for 3 Indian programs.</p>
                </div>
                <div class="card" style="border-color: var(--accent);">
                    <div style="position: absolute; top: 0; right: 48px; background: var(--accent); color: var(--dark); font-size: 0.65rem; font-weight: bold; letter-spacing: 0.1em; padding: 4px 12px; text-transform: uppercase; transform: translateY(-50%);">Global</div>
                    <h3 style="font-family: var(--font-display); font-size: 1.5rem; margin-bottom: 8px;">Single School - Global</h3>
                    <p style="font-size: 2rem; font-weight: 300; margin-bottom: 16px; color: var(--accent);">₹69,999</p>
                    <p style="color: var(--text-dim); font-size: 0.9rem; margin-bottom: 16px;">INSEAD, LBS, US MBAs. Full strategy & 1 mock interview.</p>
                </div>
                <div class="card">
                    <h3 style="font-family: var(--font-display); font-size: 1.5rem; margin-bottom: 8px;">Global 3-School Pack</h3>
                    <p style="font-size: 2rem; font-weight: 300; margin-bottom: 16px; color: var(--accent);">₹1,79,999</p>
                    <p style="color: var(--text-dim); font-size: 0.9rem; margin-bottom: 16px;">End-to-end strategy for 3 international programs.</p>
                </div>
                <div class="card">
                    <h3 style="font-family: var(--font-display); font-size: 1.5rem; margin-bottom: 8px;">MBA360 Premium</h3>
                    <p style="font-size: 2rem; font-weight: 300; margin-bottom: 16px; color: var(--accent);">₹2,99,999</p>
                    <p style="color: var(--text-dim); font-size: 0.9rem; margin-bottom: 16px;">Comprehensive 5-school campaign, post-MBA transition, unlimited mocks.</p>
                </div>
                <div class="card">
                    <h3 style="font-family: var(--font-display); font-size: 1.5rem; margin-bottom: 8px;">Interview Mastery</h3>
                    <p style="font-size: 2rem; font-weight: 300; margin-bottom: 16px; color: var(--accent);">₹14,999</p>
                    <p style="color: var(--text-dim); font-size: 0.9rem; margin-bottom: 16px;">2 mock interviews, feedback report, question bank.</p>
                </div>
                <div class="card">
                    <h3 style="font-family: var(--font-display); font-size: 1.5rem; margin-bottom: 8px;">Ding Analysis</h3>
                    <p style="font-size: 2rem; font-weight: 300; margin-bottom: 16px; color: var(--accent);">₹19,999</p>
                    <p style="color: var(--text-dim); font-size: 0.9rem; margin-bottom: 16px;">For rejected candidates to understand what went wrong.</p>
                </div>
                <div class="card">
                    <h3 style="font-family: var(--font-display); font-size: 1.5rem; margin-bottom: 8px;">Hourly Advisory</h3>
                    <p style="font-size: 2rem; font-weight: 300; margin-bottom: 16px; color: var(--accent);">₹5,999 / hr</p>
                    <p style="color: var(--text-dim); font-size: 0.9rem; margin-bottom: 16px;">Targeted help for specific essays or questions.</p>
                </div>
            </div>
        </div>
    </section>
    """,
    "process.html": """
    <section class="section-padding text-center">
        <h1 style="font-family: var(--font-display); font-size: clamp(3rem, 5vw, 4.5rem); line-height: 1.05; margin-bottom: 32px;" class="fade-enter visible">A structured journey from confusion to confident submission.</h1>
    </section>
    <section style="background: var(--charcoal); border-top: 1px solid var(--border);">
        <div class="section-padding" style="max-width: 800px;">
            <div style="border-left: 1px solid var(--accent); padding-left: 40px; margin-left: 20px;">
                <div style="margin-bottom: 48px; position: relative;">
                    <div style="position: absolute; left: -46px; top: 0; width: 12px; height: 12px; border-radius: 50%; background: var(--accent);"></div>
                    <h3 style="font-family: var(--font-display); font-size: 1.5rem; margin-bottom: 8px; color: var(--cream);">Step 1: Discovery</h3>
                    <p style="color: var(--text-dim);">We understand your background, goals, constraints, budget, geography preference, and career ambition.</p>
                </div>
                <div style="margin-bottom: 48px; position: relative;">
                    <div style="position: absolute; left: -46px; top: 0; width: 12px; height: 12px; border-radius: 50%; background: var(--accent);"></div>
                    <h3 style="font-family: var(--font-display); font-size: 1.5rem; margin-bottom: 8px; color: var(--cream);">Step 2: Profile Diagnosis</h3>
                    <p style="color: var(--text-dim);">We evaluate your strengths, gaps, differentiators, and risk areas.</p>
                </div>
                <div style="margin-bottom: 48px; position: relative;">
                    <div style="position: absolute; left: -46px; top: 0; width: 12px; height: 12px; border-radius: 50%; background: var(--accent);"></div>
                    <h3 style="font-family: var(--font-display); font-size: 1.5rem; margin-bottom: 8px; color: var(--cream);">Step 3: MBA Pathway Design</h3>
                    <p style="color: var(--text-dim);">We recommend the right MBA path: Indian one-year, global, executive, or specialized.</p>
                </div>
                <div style="margin-bottom: 48px; position: relative;">
                    <div style="position: absolute; left: -46px; top: 0; width: 12px; height: 12px; border-radius: 50%; background: var(--accent);"></div>
                    <h3 style="font-family: var(--font-display); font-size: 1.5rem; margin-bottom: 8px; color: var(--cream);">Step 4: Story Architecture</h3>
                    <p style="color: var(--text-dim);">We build your narrative: who you are, what shaped you, why MBA, why now, and why this school.</p>
                </div>
                <div style="margin-bottom: 48px; position: relative;">
                    <div style="position: absolute; left: -46px; top: 0; width: 12px; height: 12px; border-radius: 50%; background: var(--accent);"></div>
                    <h3 style="font-family: var(--font-display); font-size: 1.5rem; margin-bottom: 8px; color: var(--cream);">Step 5: Application Build</h3>
                    <p style="color: var(--text-dim);">We work on resume, essays, SOPs, application forms, and recommendation strategy.</p>
                </div>
                <div style="margin-bottom: 48px; position: relative;">
                    <div style="position: absolute; left: -46px; top: 0; width: 12px; height: 12px; border-radius: 50%; background: var(--accent);"></div>
                    <h3 style="font-family: var(--font-display); font-size: 1.5rem; margin-bottom: 8px; color: var(--cream);">Step 6: Review & Refinement</h3>
                    <p style="color: var(--text-dim);">We review for clarity, authenticity, school fit, and business relevance.</p>
                </div>
                <div style="margin-bottom: 48px; position: relative;">
                    <div style="position: absolute; left: -46px; top: 0; width: 12px; height: 12px; border-radius: 50%; background: var(--accent);"></div>
                    <h3 style="font-family: var(--font-display); font-size: 1.5rem; margin-bottom: 8px; color: var(--cream);">Step 7: Interview Preparation</h3>
                    <p style="color: var(--text-dim);">We conduct mocks, refine answers, and prepare you for school-specific interviews.</p>
                </div>
                <div style="position: relative;">
                    <div style="position: absolute; left: -46px; top: 0; width: 12px; height: 12px; border-radius: 50%; background: var(--accent);"></div>
                    <h3 style="font-family: var(--font-display); font-size: 1.5rem; margin-bottom: 8px; color: var(--cream);">Step 8: Final Submission & Beyond</h3>
                    <p style="color: var(--text-dim);">We help with final checks, waitlist strategy, scholarships, and career transition direction.</p>
                </div>
            </div>
        </div>
    </section>
    """,
    "contact.html": """
    <section class="section-padding text-center">
        <h1 style="font-family: var(--font-display); font-size: clamp(3rem, 5vw, 4.5rem); line-height: 1.05; margin-bottom: 32px;" class="fade-enter visible">Start with one honest conversation.</h1>
        <p style="font-family: var(--font-serif); font-size: 1.2rem; color: var(--cream); max-width: 800px; margin: 0 auto 48px;" class="fade-enter visible">Tell us where you are, where you want to go, and what is stopping you. We will help you understand the right MBA pathway and next steps.</p>
    </section>
    <section style="background: var(--charcoal); border-top: 1px solid var(--border);">
        <div class="section-padding" style="max-width: 800px; margin: 0 auto;">
            <form class="auth-form fade-enter visible" onsubmit="event.preventDefault(); alert('Consultation requested. You will receive a confirmation email shortly.'); this.reset();" style="padding: 56px; border: 1px solid var(--border); background: var(--dark);">
                <div class="form-row" style="display: grid; grid-template-columns: 1fr 1fr; gap: 24px; margin-bottom: 24px;">
                    <div class="field" style="display: flex; flex-direction: column; gap: 8px;">
                        <label style="color: var(--cream); font-size: 0.85rem; text-transform: uppercase; letter-spacing: 0.1em;">Full Name</label>
                        <input type="text" required placeholder="John Doe" style="background: var(--charcoal); border: 1px solid var(--border); color: var(--cream); padding: 16px; outline: none;">
                    </div>
                    <div class="field" style="display: flex; flex-direction: column; gap: 8px;">
                        <label style="color: var(--cream); font-size: 0.85rem; text-transform: uppercase; letter-spacing: 0.1em;">Email</label>
                        <input type="email" required placeholder="you@example.com" style="background: var(--charcoal); border: 1px solid var(--border); color: var(--cream); padding: 16px; outline: none;">
                    </div>
                </div>
                <div class="form-row" style="display: grid; grid-template-columns: 1fr 1fr; gap: 24px; margin-bottom: 24px;">
                    <div class="field" style="display: flex; flex-direction: column; gap: 8px;">
                        <label style="color: var(--cream); font-size: 0.85rem; text-transform: uppercase; letter-spacing: 0.1em;">WhatsApp Number</label>
                        <input type="text" required placeholder="+91..." style="background: var(--charcoal); border: 1px solid var(--border); color: var(--cream); padding: 16px; outline: none;">
                    </div>
                    <div class="field" style="display: flex; flex-direction: column; gap: 8px;">
                        <label style="color: var(--cream); font-size: 0.85rem; text-transform: uppercase; letter-spacing: 0.1em;">Current Profession</label>
                        <select style="background: var(--charcoal); border: 1px solid var(--border); color: var(--cream); padding: 16px; outline: none;">
                            <option>Merchant Navy</option>
                            <option>Defence / Ex-Defence</option>
                            <option>Other Service Background</option>
                        </select>
                    </div>
                </div>
                <div class="form-row" style="display: grid; grid-template-columns: 1fr 1fr; gap: 24px; margin-bottom: 24px;">
                    <div class="field" style="display: flex; flex-direction: column; gap: 8px;">
                        <label style="color: var(--cream); font-size: 0.85rem; text-transform: uppercase; letter-spacing: 0.1em;">Rank / Designation</label>
                        <input type="text" required placeholder="e.g. Chief Officer" style="background: var(--charcoal); border: 1px solid var(--border); color: var(--cream); padding: 16px; outline: none;">
                    </div>
                    <div class="field" style="display: flex; flex-direction: column; gap: 8px;">
                        <label style="color: var(--cream); font-size: 0.85rem; text-transform: uppercase; letter-spacing: 0.1em;">Target MBA Year</label>
                        <input type="text" required placeholder="2026/2027" style="background: var(--charcoal); border: 1px solid var(--border); color: var(--cream); padding: 16px; outline: none;">
                    </div>
                </div>
                <div class="field" style="display: flex; flex-direction: column; gap: 8px; margin-bottom: 24px;">
                    <label style="color: var(--cream); font-size: 0.85rem; text-transform: uppercase; letter-spacing: 0.1em;">Main Concern or Goal</label>
                    <textarea required placeholder="What do you need help with?" style="background: var(--charcoal); border: 1px solid var(--border); color: var(--cream); padding: 16px; outline: none; min-height: 120px; font-family: var(--font-sans);"></textarea>
                </div>
                <button type="submit" class="btn-primary" style="width: 100%; padding: 16px; margin-top: 16px;">Book Discovery Call</button>
            </form>
            
            <div class="text-center" style="margin-top: 48px;">
                <p style="color: var(--text-dim);">Or reach us directly at:</p>
                <a href="mailto:connect@beyond-bridge.com" style="color: var(--accent); text-decoration: none; font-size: 1.2rem;">connect@beyond-bridge.com</a>
            </div>
        </div>
    </section>
    """,
    "faq.html": """
    <section class="section-padding text-center">
        <h1 style="font-family: var(--font-display); font-size: clamp(3rem, 5vw, 4.5rem); line-height: 1.05; margin-bottom: 32px;" class="fade-enter visible">Frequently Asked Questions</h1>
        <p style="font-family: var(--font-serif); font-size: 1.2rem; color: var(--cream); max-width: 800px; margin: 0 auto 48px;" class="fade-enter visible">We understand that moving from sea, defence, or service-led careers into business school is a big decision. This page answers the most common questions.</p>
    </section>
    <section style="background: var(--charcoal); border-top: 1px solid var(--border);">
        <div class="section-padding" style="max-width: 800px; margin: 0 auto;">
            
            <h2 style="font-family: var(--font-display); font-size: 2rem; color: var(--accent); margin-bottom: 24px;">About Beyond Bridge</h2>
            <div style="border-top: 1px solid var(--border); padding: 24px 0; cursor: pointer;" onclick="const p = this.querySelector('p'); p.style.display = p.style.display === 'none' ? 'block' : 'none';">
                <h3 style="font-family: var(--font-display); font-size: 1.3rem; margin-bottom: 8px;">1. What is Beyond Bridge?</h3>
                <p style="color: var(--text-dim); display: none; margin-top: 16px;">Beyond Bridge is a specialist MBA admissions and career transition advisory platform for merchant navy professionals, defence officers, veterans, and service-background leaders who want to move into business education and corporate careers.</p>
            </div>
            <div style="border-top: 1px solid var(--border); padding: 24px 0; cursor: pointer;" onclick="const p = this.querySelector('p'); p.style.display = p.style.display === 'none' ? 'block' : 'none';">
                <h3 style="font-family: var(--font-display); font-size: 1.3rem; margin-bottom: 8px;">2. Is Beyond Bridge an MBA coaching institute?</h3>
                <p style="color: var(--text-dim); display: none; margin-top: 16px;">No. Beyond Bridge is not a classroom coaching institute. We are an MBA admissions and career transition advisory platform focusing on strategy, profile building, and narratives.</p>
            </div>
            
            <h2 style="font-family: var(--font-display); font-size: 2rem; color: var(--accent); margin-bottom: 24px; margin-top: 64px;">MBA Decision & Eligibility</h2>
            <div style="border-top: 1px solid var(--border); padding: 24px 0; cursor: pointer;" onclick="const p = this.querySelector('p'); p.style.display = p.style.display === 'none' ? 'block' : 'none';">
                <h3 style="font-family: var(--font-display); font-size: 1.3rem; margin-bottom: 8px;">3. I am still sailing. Can I apply for an MBA?</h3>
                <p style="color: var(--text-dim); display: none; margin-top: 16px;">Yes. Many candidates begin MBA planning while still sailing. The key is to plan early. We support you remotely through video calls, WhatsApp, and online document review.</p>
            </div>
            <div style="border-top: 1px solid var(--border); padding: 24px 0; cursor: pointer;" onclick="const p = this.querySelector('p'); p.style.display = p.style.display === 'none' ? 'block' : 'none';">
                <h3 style="font-family: var(--font-display); font-size: 1.3rem; margin-bottom: 8px;">4. Do I need a GMAT, GRE, or Executive Assessment?</h3>
                <p style="color: var(--text-dim); display: none; margin-top: 16px;">It depends on the school and program. Some require it, while others offer waivers. We help you evaluate which test path is practical based on your profile.</p>
            </div>
            
            <h2 style="font-family: var(--font-display); font-size: 2rem; color: var(--accent); margin-bottom: 24px; margin-top: 64px;">Services & Outcomes</h2>
            <div style="border-top: 1px solid var(--border); padding: 24px 0; cursor: pointer;" onclick="const p = this.querySelector('p'); p.style.display = p.style.display === 'none' ? 'block' : 'none';">
                <h3 style="font-family: var(--font-display); font-size: 1.3rem; margin-bottom: 8px;">5. Do you write essays for candidates?</h3>
                <p style="color: var(--text-dim); display: none; margin-top: 16px;">No. We help candidates develop and refine their essays, but the final content must be authentic. We do not encourage plagiarized or fake content.</p>
            </div>
            <div style="border-top: 1px solid var(--border); border-bottom: 1px solid var(--border); padding: 24px 0; cursor: pointer;" onclick="const p = this.querySelector('p'); p.style.display = p.style.display === 'none' ? 'block' : 'none';">
                <h3 style="font-family: var(--font-display); font-size: 1.3rem; margin-bottom: 8px;">6. Do you guarantee admission?</h3>
                <p style="color: var(--text-dim); display: none; margin-top: 16px;">No. Beyond Bridge does not guarantee admission. We improve your preparation and positioning, but we cannot control admissions decisions.</p>
            </div>
        </div>
    </section>
    """,
    "resources.html": """
    <section class="section-padding text-center">
        <h1 style="font-family: var(--font-display); font-size: clamp(3rem, 5vw, 4.5rem); line-height: 1.05; margin-bottom: 32px;" class="fade-enter visible">MBA Insights for Sea, Service & Business Transitions.</h1>
        <p style="font-family: var(--font-serif); font-size: 1.2rem; color: var(--cream); max-width: 800px; margin: 0 auto 48px;" class="fade-enter visible">An MBA is not just about getting into a business school. It is about making the right career decision.</p>
    </section>
    <section style="background: var(--charcoal); border-top: 1px solid var(--border);">
        <div class="section-padding">
            <div class="grid-3">
                <div class="card">
                    <p style="color: var(--accent); text-transform: uppercase; font-size: 0.75rem; letter-spacing: 0.1em; margin-bottom: 12px;">MBA Basics</p>
                    <h3 style="font-family: var(--font-display); font-size: 1.5rem; margin-bottom: 16px;">Understanding Global MBA Timelines for Mariners</h3>
                    <p style="color: var(--text-dim); font-size: 0.9rem; margin-bottom: 24px;">How to plan your GMAT and applications while completing your final sailing contracts.</p>
                    <a href="#" style="color: var(--cream); text-decoration: none; border-bottom: 1px solid var(--border);">Read Article →</a>
                </div>
                <div class="card">
                    <p style="color: var(--accent); text-transform: uppercase; font-size: 0.75rem; letter-spacing: 0.1em; margin-bottom: 12px;">Defence to MBA</p>
                    <h3 style="font-family: var(--font-display); font-size: 1.5rem; margin-bottom: 16px;">Translating Military Command into Corporate Execution</h3>
                    <p style="color: var(--text-dim); font-size: 0.9rem; margin-bottom: 24px;">A guide for veterans on structuring operations and crisis management for admissions essays.</p>
                    <a href="#" style="color: var(--cream); text-decoration: none; border-bottom: 1px solid var(--border);">Read Article →</a>
                </div>
                <div class="card">
                    <p style="color: var(--accent); text-transform: uppercase; font-size: 0.75rem; letter-spacing: 0.1em; margin-bottom: 12px;">Career Outcomes</p>
                    <h3 style="font-family: var(--font-display); font-size: 1.5rem; margin-bottom: 16px;">Why Consulting Firms Value Sea Experience</h3>
                    <p style="color: var(--text-dim); font-size: 0.9rem; margin-bottom: 24px;">Exploring post-MBA transitions into McKinsey, BCG, and Bain for operational leaders.</p>
                    <a href="#" style="color: var(--cream); text-decoration: none; border-bottom: 1px solid var(--border);">Read Article →</a>
                </div>
            </div>
        </div>
    </section>
    """,
    "mariners.html": """
    <section class="section-padding text-center">
        <h1 style="font-family: var(--font-display); font-size: clamp(3rem, 5vw, 4.5rem); line-height: 1.05; margin-bottom: 32px;" class="fade-enter visible">Your sea experience is not a limitation. It is your leadership advantage.</h1>
        <p style="font-family: var(--font-serif); font-size: 1.2rem; color: var(--cream); max-width: 800px; margin: 0 auto 48px;" class="fade-enter visible">We help merchant navy professionals translate sea-based responsibility into MBA-ready business leadership stories.</p>
    </section>
    <section style="background: var(--charcoal); border-top: 1px solid var(--border);">
        <div class="section-padding" style="max-width: 1000px; margin: 0 auto;">
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 80px; align-items: center;">
                <div>
                    <h2 style="font-family: var(--font-display); font-size: 2.5rem; margin-bottom: 24px; color: var(--cream);">The Challenge</h2>
                    <p style="color: var(--text-dim); margin-bottom: 24px; line-height: 1.8;">A career at sea builds discipline, resilience, multicultural leadership, asset responsibility, safety mindset, operational excellence, crisis management, and global exposure. These are powerful MBA traits.</p>
                    <p style="color: var(--cream); line-height: 1.8;">The challenge is not your experience. The challenge is explaining it in the language of business schools and recruiters.</p>
                </div>
                <div>
                    <h2 style="font-family: var(--font-display); font-size: 2rem; margin-bottom: 24px; color: var(--accent);">We Help Mariners With:</h2>
                    <ul style="color: var(--cream); list-style: none; padding: 0; line-height: 2.2;">
                        <li style="border-bottom: 1px solid var(--border);">✓ Rank-to-leadership translation</li>
                        <li style="border-bottom: 1px solid var(--border);">✓ Technical-to-business resume conversion</li>
                        <li style="border-bottom: 1px solid var(--border);">✓ Shipping-to-consulting transition planning</li>
                        <li style="border-bottom: 1px solid var(--border);">✓ Operations and safety experience positioning</li>
                        <li style="border-bottom: 1px solid var(--border);">✓ MBA school selection</li>
                    </ul>
                </div>
            </div>
            <div class="text-center" style="margin-top: 80px;">
                <a href="contact.html" class="btn-primary" style="text-decoration: none;">Book a Mariner MBA Consultation</a>
            </div>
        </div>
    </section>
    """,
    "defence.html": """
    <section class="section-padding text-center">
        <h1 style="font-family: var(--font-display); font-size: clamp(3rem, 5vw, 4.5rem); line-height: 1.05; margin-bottom: 32px;" class="fade-enter visible">From command responsibility to corporate leadership.</h1>
        <p style="font-family: var(--font-serif); font-size: 1.2rem; color: var(--cream); max-width: 800px; margin: 0 auto 48px;" class="fade-enter visible">We help defence officers and veterans convert service experience into a compelling MBA and career transition narrative.</p>
    </section>
    <section style="background: var(--charcoal); border-top: 1px solid var(--border);">
        <div class="section-padding" style="max-width: 1000px; margin: 0 auto;">
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 80px; align-items: center;">
                <div>
                    <h2 style="font-family: var(--font-display); font-size: 2.5rem; margin-bottom: 24px; color: var(--cream);">The Strategic Shift</h2>
                    <p style="color: var(--text-dim); margin-bottom: 24px; line-height: 1.8;">Defence professionals bring discipline, leadership, execution, crisis response, team management, resource optimization, and mission focus. Business schools value these traits when they are presented with clarity and relevance.</p>
                    <p style="color: var(--cream); line-height: 1.8;">Beyond Bridge helps you position your defence career for MBA admissions and post-MBA career opportunities.</p>
                </div>
                <div>
                    <h2 style="font-family: var(--font-display); font-size: 2rem; margin-bottom: 24px; color: var(--accent);">We Help Defence Candidates With:</h2>
                    <ul style="color: var(--cream); list-style: none; padding: 0; line-height: 2.2;">
                        <li style="border-bottom: 1px solid var(--border);">✓ Service-to-business story development</li>
                        <li style="border-bottom: 1px solid var(--border);">✓ Leadership example mapping</li>
                        <li style="border-bottom: 1px solid var(--border);">✓ Indian and global MBA school selection</li>
                        <li style="border-bottom: 1px solid var(--border);">✓ Corporate transition strategy</li>
                        <li style="border-bottom: 1px solid var(--border);">✓ Networking and LinkedIn positioning</li>
                    </ul>
                </div>
            </div>
            <div class="text-center" style="margin-top: 80px;">
                <a href="contact.html" class="btn-primary" style="text-decoration: none;">Start Your Defence-to-MBA Journey</a>
            </div>
        </div>
    </section>
    """
}

# The wrapper provides the standard `<head>`, `<nav>`, `<script>`, and `<footer>` for all subpages.
wrapper_top = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Beyond Bridge Advisory</title>
    <link rel="stylesheet" href="style.css" />
    <style>
        body { opacity: 0; animation: fadeIn 0.8s ease forwards; }
        @keyframes fadeIn { to { opacity: 1; } }
        .section-padding { padding: 120px 60px; max-width: 1200px; margin: 0 auto; }
        .text-center { text-align: center; }
        .grid-3 { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 40px; }
        .card { padding: 48px; border: 1px solid var(--border); background: var(--dark); transition: transform 0.3s; position: relative;}
        .card:hover { transform: translateY(-8px); }
        .btn-primary { background: var(--accent); color: var(--dark); padding: 16px 32px; border-radius: 2px; text-transform: uppercase; font-size: 0.8rem; letter-spacing: 0.1em; font-weight: bold; border: none; cursor: pointer; transition: background 0.3s; }
        .btn-primary:hover { background: #d32f2f; }
    </style>
</head>
<body>
    <!-- NAVBAR -->
    <nav style="display: flex; justify-content: space-between; align-items: center; padding: 24px 60px; border-bottom: 1px solid var(--border); position: sticky; top: 0; background: rgba(11, 11, 11, 0.9); backdrop-filter: blur(10px); z-index: 100;">
        <a href="home.html" style="text-decoration: none;">
            <img src="assets/logo-cropped.png" alt="Beyond Bridge" class="logo-main" style="height: 32px;">
        </a>
        <div style="display: flex; gap: 24px; align-items: center; font-size: 0.75rem; letter-spacing: 0.1em; text-transform: uppercase;">
            <a href="home.html" style="color: var(--cream); text-decoration: none;">Home</a>
            <a href="about.html" style="color: var(--cream); text-decoration: none;">About</a>
            <a href="mariners.html" style="color: var(--cream); text-decoration: none;">Mariners</a>
            <a href="defence.html" style="color: var(--cream); text-decoration: none;">Defence</a>
            <a href="pathways.html" style="color: var(--cream); text-decoration: none;">Pathways</a>
            <a href="services.html" style="color: var(--cream); text-decoration: none;">Services</a>
            <a href="pricing.html" style="color: var(--cream); text-decoration: none;">Pricing</a>
            <a href="process.html" style="color: var(--cream); text-decoration: none;">Process</a>
            <a href="resources.html" style="color: var(--cream); text-decoration: none;">Resources</a>
            <a href="contact.html" style="color: var(--cream); text-decoration: none;">Contact</a>
            
            <a href="dashboard.html" style="color: var(--cream); text-decoration: none; border-left: 1px solid var(--border); padding-left: 24px;">Dashboard</a>
            <a href="#" onclick="handleLogout()" style="color: var(--text-dim); text-decoration: none;">Logout</a>
        </div>
    </nav>
"""

wrapper_bottom = """
    <!-- FOOTER -->
    <footer style="padding: 60px; text-align: center; font-size: 0.8rem; color: var(--text-dim); border-top: 1px solid var(--border); background: var(--charcoal);">
        <div style="margin-bottom: 32px;">
            <img src="assets/logo-cropped.png" alt="Beyond Bridge" class="logo-main" style="height: 40px;">
        </div>
        <div style="display: flex; justify-content: center; gap: 24px; margin-bottom: 32px; flex-wrap: wrap;">
            <a href="legal.html" style="color: var(--text-muted); text-decoration: none;">Privacy & Legal</a>
            <a href="mailto:connect@beyond-bridge.com" style="color: var(--text-muted); text-decoration: none;">connect@beyond-bridge.com</a>
        </div>
        <p>&copy; 2026 Beyond Bridge Advisory. All rights reserved.</p>
    </footer>

    <script src="script.js"></script>
    <script>
        // Ensure user is logged in for subpages
        window.onload = function() {
            if(localStorage.getItem('loggedIn') !== 'true') {
                window.location.href = 'index.html';
            }
        };

        function handleLogout() {
            localStorage.removeItem('loggedIn');
            window.location.href = 'index.html';
        }
    </script>
</body>
</html>
"""

for filename, content in pages.items():
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(wrapper_top + content + wrapper_bottom)
    print(f"Created {filename}")
