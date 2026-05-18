"""Batch 14 — Backlog Batch 9: competitor-analysis, marketing-strategy, revenue-operations, ab-testing, website-personalization"""
import json, os

SERVICES = {
    "competitor-analysis": {
        "title": "Competitor Analysis",
        "tagline": "Deep competitive intelligence that reveals gaps, opportunities, and winning strategies",
        "desc": "You can't win a race you don't understand. We deliver comprehensive competitor analysis — mapping their SEO strategy, paid advertising, content, positioning, pricing, and digital presence — so you can identify the gaps they're leaving open and the strategies worth replicating or countering.",
        "price": "$2,500",
        "stat1": "90%",
        "stat1_label": "of Fortune 500 companies use competitive intelligence",
        "stat2": "2x",
        "stat2_label": "faster market share growth with systematic competitor tracking",
        "stat3": "37%",
        "stat3_label": "of businesses identify competitor gaps as top growth opportunity",
        "deliverables": [
            ("🔍", "SEO Competitor Analysis", "Full organic search competitive analysis: competitor keyword portfolios, content gaps, backlink profiles, domain authority comparison, and ranking opportunities they're missing that you can capture."),
            ("💰", "Paid Advertising Intelligence", "Competitor ad strategy decoded: estimated ad spend, top-performing ad copy, landing page strategies, offer positioning, and the keywords they're bidding on — surfacing opportunities in your paid strategy."),
            ("📝", "Content Strategy Analysis", "Competitor content audit: blog topics, content formats, publishing frequency, engagement metrics, and content gaps — identifying the content territory they're leaving unclaimed."),
            ("💬", "Positioning & Messaging Analysis", "How competitors position themselves, what value propositions they lead with, how they differentiate, and where their messaging is weak — giving you clear differentiation angles."),
            ("💵", "Pricing & Offer Intelligence", "Competitor pricing structures, packaging, free trial policies, and offer mechanics — with recommendations for how to position your pricing competitively."),
            ("⭐", "Reputation & Review Analysis", "Competitor review sentiment analysis: what customers love, what they complain about, and the experience gaps that represent your opportunity to win on service quality."),
            ("📊", "Competitive Intelligence Report", "A comprehensive, actionable report with executive summary, channel-by-channel analysis, opportunity prioritization matrix, and 90-day action plan based on the findings."),
        ],
        "process": [
            ("🔍", "Competitor Identification", "We identify your true competitive set — not just who you think your competitors are, but who you're actually losing deals to and who ranks for your target keywords."),
            ("📊", "Data Collection & Analysis", "Multi-source data collection across SEO tools, ad intelligence platforms, review databases, and direct website analysis. Data synthesized into a unified competitive picture."),
            ("💡", "Insight Extraction", "We translate data into strategy: which opportunities are highest priority, which competitor weaknesses are exploitable, and which competitor strengths you need to counter or avoid."),
            ("📋", "Report & Action Plan", "Comprehensive report delivered with an executive briefing. Includes a prioritized 90-day action plan so findings translate directly into marketing decisions."),
        ],
        "faqs": [
            ("How many competitors do you analyze?", "Standard analysis covers your top 3–5 direct competitors. We can expand to 10+ competitors for a comprehensive market analysis at additional cost."),
            ("How current is the data?", "We pull live data at the time of the engagement — SEO rankings, ad activity, review counts — so the analysis reflects current market conditions, not stale data."),
            ("Can you do ongoing competitor monitoring?", "Yes — we offer quarterly competitive intelligence updates to track how the competitive landscape shifts over time and update your strategy accordingly."),
            ("What if our competitors don't advertise much?", "Limited paid advertising by competitors is itself a strategic insight — it may indicate the channel isn't effective in your market, or it may be an opportunity to dominate an uncrowded channel. We analyze what's present and what's absent."),
            ("Will you include indirect competitors?", "Yes — we analyze direct competitors (same product/service) and indirect competitors (alternative solutions your prospects consider). Understanding the full competitive context gives you a more complete strategic picture."),
        ],
        "schema_service_desc": "Competitor analysis — SEO intelligence, paid advertising analysis, content strategy, positioning review, pricing intelligence, and comprehensive competitive report.",
    },
    "marketing-strategy": {
        "title": "Marketing Strategy",
        "tagline": "Data-driven marketing strategy built for growth — not guesswork",
        "desc": "Most marketing plans are built on assumptions — target audiences defined by gut feel, channels chosen by familiarity, and budgets allocated by habit. We build marketing strategies grounded in data: customer research, competitive intelligence, channel analysis, and financial modeling that tell you exactly where to focus for maximum ROI.",
        "price": "$7,500",
        "stat1": "3x",
        "stat1_label": "higher ROI for businesses with a documented marketing strategy",
        "stat2": "64%",
        "stat2_label": "of businesses without a strategy report wasted marketing spend",
        "stat3": "73%",
        "stat3_label": "of marketers say strategy is their top challenge",
        "deliverables": [
            ("🔍", "Market & Customer Research", "Primary and secondary research: customer interviews, survey analysis, ICP validation, market sizing, and segment-level opportunity assessment — building strategy on real data, not assumptions."),
            ("🎯", "ICP & Positioning Development", "Precisely defined ideal customer profiles with psychographic depth — and a positioning statement that differentiates you clearly in your market and gives every marketing decision a filter."),
            ("📊", "Channel Strategy & Mix", "Data-driven channel selection and budget allocation: which channels to prioritize, in what sequence, with what budget ratios — based on your ICP, competitive intensity, and unit economics."),
            ("💰", "Marketing Budget Modeling", "Financial models for your marketing investment: projected customer acquisition cost, payback period, and revenue impact at different budget levels — so you can make investment decisions with confidence."),
            ("📅", "12-Month Marketing Roadmap", "A quarter-by-quarter execution roadmap: priorities, campaigns, channel launches, content themes, and resource requirements — turning strategy into an actionable plan."),
            ("📋", "Measurement Framework", "KPI framework and measurement plan: which metrics matter at each stage of growth, how to track them, and what thresholds trigger strategic adjustments."),
            ("🎓", "Strategy Presentation & Workshop", "Executive-level strategy presentation with a 90-minute workshop to align your team, answer questions, and pressure-test the strategy before execution begins."),
        ],
        "process": [
            ("🔍", "Discovery & Research", "Deep-dive into your business: customer interviews, data review, competitive analysis, and financial model review. We ask the questions most agencies never ask."),
            ("💡", "Strategy Development", "Strategy built from research findings: positioning, ICP, channel mix, budget model, and roadmap. Drafted for your review and iteration."),
            ("🔄", "Review & Refinement", "Strategy workshop with your team. Questions answered, assumptions challenged, and strategy refined based on internal knowledge we don't have access to from research alone."),
            ("📋", "Final Delivery & Handoff", "Final strategy document delivered with implementation guidance. Optional: we execute the strategy through our full-service marketing services."),
        ],
        "faqs": [
            ("How is this different from what a consultant does?", "Traditional strategy consultants deliver frameworks and recommendations. We deliver executable strategies: specific channels, specific content, specific budgets, and specific timelines — built from data, not theory. And we can execute it ourselves if needed."),
            ("How long does the strategy take to develop?", "A comprehensive marketing strategy takes 4–6 weeks: 2 weeks for research, 2 weeks for strategy development, and 1–2 weeks for review and refinement."),
            ("Do we need to execute the strategy through you?", "No — the strategy document is yours to execute internally or with any agency. Many clients use it to align internal teams or brief other vendors. We include execution guidance for every recommendation."),
            ("What if our business model changes after the strategy is delivered?", "We build strategies with key assumptions clearly documented. If a core assumption changes (new product, pivot, new market), we offer a strategy update engagement to revisit the most affected areas."),
            ("Is this a one-time project or ongoing?", "The core strategy is a one-time project. We recommend a quarterly strategy review (separate engagement) to update channel allocation, ICP refinements, and competitive positioning based on 3 months of real execution data."),
        ],
        "schema_service_desc": "Marketing strategy — customer research, ICP development, channel strategy, budget modeling, 12-month roadmap, measurement framework, and strategy workshop.",
    },
    "revenue-operations": {
        "title": "Revenue Operations",
        "tagline": "Align sales, marketing, and customer success around a unified revenue engine",
        "desc": "Revenue Operations (RevOps) eliminates the friction between marketing, sales, and customer success — aligning data, processes, and technology so your revenue team operates as a single, efficient machine. We design, implement, and optimize RevOps systems that accelerate pipeline velocity, reduce churn, and make your growth predictable.",
        "price": "$5,000/mo",
        "stat1": "19%",
        "stat1_label": "faster revenue growth for companies with aligned RevOps",
        "stat2": "36%",
        "stat2_label": "higher win rates with marketing and sales alignment",
        "stat3": "15%",
        "stat3_label": "average increase in deal velocity with RevOps implementation",
        "deliverables": [
            ("🔗", "Revenue Process Mapping", "End-to-end revenue process documentation: lead-to-close workflow, handoff criteria, stage definitions, and SLAs between marketing, sales, and customer success — identifying every friction point."),
            ("⚙️", "CRM Architecture & Optimization", "CRM design or redesign: deal stages, pipeline structure, custom properties, workflow automation, and reporting — so your CRM reflects your actual sales process and generates useful data."),
            ("📊", "Unified Revenue Reporting", "A single revenue dashboard integrating marketing pipeline data, sales performance, and customer success metrics — one source of truth for leadership reporting and decision-making."),
            ("🤝", "Sales & Marketing Alignment", "SLA definition between marketing and sales: lead qualification criteria, MQL/SQL definitions, handoff process, feedback loops, and shared metrics — eliminating the blame game."),
            ("🔄", "Lead Lifecycle Management", "Full lead lifecycle design: lead scoring, routing rules, nurture enrollment triggers, and disqualification criteria — ensuring every lead is handled correctly at every stage."),
            ("📈", "Forecasting & Pipeline Management", "Forecasting methodology implementation: pipeline coverage ratios, stage-weighted forecasting, deal risk signals, and weekly pipeline review process — making revenue predictable."),
            ("⚡", "Workflow Automation", "Automation of repetitive revenue processes: lead assignment, follow-up reminders, stage progression triggers, renewal alerts, and reporting — reducing manual work and eliminating process gaps."),
        ],
        "process": [
            ("🔍", "Revenue Audit", "We map your current revenue process: how leads flow, where they get stuck, how handoffs happen, and what data gaps prevent accurate forecasting. Full audit delivered with prioritized findings."),
            ("📋", "Design & Architecture", "New revenue process designed: CRM architecture, workflow logic, reporting structure, and team SLAs. Reviewed and approved before any implementation begins."),
            ("⚙️", "Implementation & Training", "CRM configured, automations built, reporting dashboards created, and team trained. We manage the migration from old to new process to minimize disruption."),
            ("📈", "Optimize & Scale", "Monthly RevOps review: pipeline health, forecast accuracy, process compliance, and automation performance. Iterative improvements as your team grows and processes mature."),
        ],
        "faqs": [
            ("What CRM do you work with?", "We primarily implement and optimize HubSpot, Salesforce, and Pipedrive. We can work with other CRMs with some adaptation. If you're choosing a CRM, we advise on the right fit for your stage and needs."),
            ("Do we need a large team for RevOps to matter?", "No — RevOps is most impactful at 5–50 person revenue teams where process gaps are already costing deals but aren't yet big enough to justify a full-time RevOps hire. We provide the expertise without the headcount."),
            ("How long does RevOps implementation take?", "Initial audit and design: 3–4 weeks. Core implementation (CRM, workflows, reporting): 6–10 weeks. Full optimization to steady state: 3–6 months of ongoing management."),
            ("What if marketing and sales have different tool stacks?", "Tool stack fragmentation is one of the most common RevOps challenges. We design the integration architecture to connect your tools — whether through native integrations, Zapier, or custom API work — so data flows where it needs to go."),
            ("Can you help us implement account-based marketing (ABM)?", "Yes — ABM is a natural extension of RevOps. We implement the account-level data structure, scoring, and workflow automation that ABM requires — alongside our Account-Based Marketing service for the strategy and execution."),
        ],
        "schema_service_desc": "Revenue operations — process mapping, CRM architecture, unified reporting, sales-marketing alignment, lead lifecycle, forecasting, and workflow automation.",
    },
    "ab-testing": {
        "title": "A/B Testing",
        "tagline": "Systematic experimentation that eliminates guesswork and compounds conversion gains",
        "desc": "A/B testing done right is one of the highest-ROI activities in marketing — each winning test permanently improves your conversion rate, compounding over time. We design, run, and analyze A/B tests across your website, landing pages, and ad creative — with statistical rigor that ensures you're making decisions on real signal, not noise.",
        "price": "$2,000/mo",
        "stat1": "12%",
        "stat1_label": "average conversion rate improvement per winning test",
        "stat2": "77%",
        "stat2_label": "of companies run A/B tests — but most lack statistical rigor",
        "stat3": "1.5–3x",
        "stat3_label": "conversion rate improvement after 12 months of systematic testing",
        "deliverables": [
            ("🧪", "Testing Roadmap & Prioritization", "A 12-month testing roadmap built from data: analytics-informed hypotheses ranked by expected impact and ease of implementation — so every test has a clear strategic rationale."),
            ("📊", "Heatmap & Session Recording Analysis", "Behavioral data analysis using Hotjar or Microsoft Clarity: where users click, scroll, and drop off — surfacing the friction points that inform high-impact test hypotheses."),
            ("✍️", "Test Design & Copy", "Test variant design for every experiment: new headlines, CTAs, layouts, form lengths, social proof placements, pricing presentations — built on conversion copywriting and UX best practices."),
            ("⚙️", "Test Implementation", "Technical test setup in Google Optimize, VWO, or Optimizely — including QA across browsers and devices, traffic allocation, and goal configuration before every test launches."),
            ("📐", "Statistical Analysis", "Rigorous statistical analysis for every test: sample size calculation, significance thresholds, and results interpretation — ensuring you only call winners when the data is conclusive."),
            ("💡", "Insight Documentation", "Every test result — win, loss, or inconclusive — documented with hypothesis, results, statistical confidence, and learnings. Your testing library compounds in value over time."),
            ("🔄", "Iterative Testing Cycles", "Continuous testing: each winner becomes the new control for the next test iteration. Each learning informs the next hypothesis. Conversion rate improvement compounds month over month."),
        ],
        "process": [
            ("🔍", "Audit & Research", "Analytics audit, heatmap analysis, and user research to identify high-impact testing opportunities. Testing roadmap built and prioritized by projected impact."),
            ("🧪", "Design & Launch", "Test variants designed and reviewed. Technical setup and QA. Test launched with proper traffic allocation and monitoring from day one."),
            ("📊", "Monitor & Analyze", "Test monitored daily for data quality issues. Analysis run at statistical significance — never called early based on early data trends."),
            ("💡", "Learn & Iterate", "Results documented, learnings extracted, and next test hypothesis developed. Winning variants implemented permanently. Testing cadence maintained at 2–4 tests per month."),
        ],
        "faqs": [
            ("How long does each A/B test run?", "Minimum 2 weeks (to capture weekly traffic variation), or until statistical significance is reached at 95% confidence — whichever is longer. We never call tests early, even when results look promising."),
            ("What do I need to have in place before starting?", "You need: enough traffic (minimum 1,000 monthly visitors per variant per page), Google Analytics or equivalent tracking, and the ability to implement code changes or use a testing tool. We assess your readiness in the audit phase."),
            ("What if our tests don't produce winners?", "Most tests are inconclusive or produce small lifts — that's normal and expected. Each result teaches us something about your audience. Our roadmap is designed so even losing tests produce insights that improve future test hypotheses."),
            ("Can you test email and ad creative as well as landing pages?", "Yes — we test across landing pages, email subject lines, ad copy, and ad creative. Each channel has different testing methodology (email uses send-time splits; ads use platform-native A/B tools), all managed under one testing program."),
            ("Do you handle the implementation, or does our dev team?", "We handle implementation using your testing platform (Google Optimize, VWO, or Optimizely). For tests that require significant development work (new page layouts, major functionality changes), we coordinate with your dev team."),
        ],
        "schema_service_desc": "A/B testing — testing roadmap, heatmap analysis, test design, implementation, statistical analysis, and iterative conversion rate optimization.",
    },
    "website-personalization": {
        "title": "Website Personalization",
        "tagline": "Dynamic website experiences tailored to each visitor — more relevance, more conversions",
        "desc": "One website can't be perfectly relevant to every visitor — different industries, company sizes, intent levels, and acquisition sources deserve different messages. We implement website personalization that dynamically adjusts headlines, CTAs, social proof, and content based on who's visiting — dramatically improving conversion rates for every segment.",
        "price": "$3,000/mo",
        "stat1": "80%",
        "stat1_label": "of consumers more likely to buy with personalized experiences",
        "stat2": "2.5x",
        "stat2_label": "higher conversion rates with personalized landing experiences",
        "stat3": "202%",
        "stat3_label": "more conversions for personalized CTAs vs. generic ones",
        "deliverables": [
            ("🗺️", "Personalization Strategy", "Audience segmentation and personalization logic design: which visitor segments get which experiences, what signals trigger personalization (UTM, company data, behavior, device), and what elements change."),
            ("🎯", "Segment Definition & Data Setup", "Visitor segment definition and data layer configuration: firmographic data (using Clearbit or 6sense), behavioral signals, traffic source parameters, and CRM-based personalization for known contacts."),
            ("✍️", "Personalized Content Creation", "Customized headlines, hero copy, social proof (testimonials, case studies, logos), CTAs, and value propositions for each defined visitor segment — every version conversion-optimized."),
            ("⚙️", "Personalization Implementation", "Technical implementation using Mutiny, Webflow, or custom JavaScript — no developer required for most changes. A/B testing personalized variants vs. control for every segment."),
            ("📊", "Segment Performance Analytics", "Segment-level reporting: conversion rate, engagement, and pipeline contribution by segment — showing exactly which personalizations are driving revenue impact."),
            ("🔗", "CRM & Marketing Automation Integration", "Integration with your CRM and marketing automation to personalize based on known contact data, deal stage, and prior engagement — enabling account-based personalization for target accounts."),
            ("🔄", "Continuous Optimization", "Monthly personalization review: segment performance analysis, new segment opportunities, content refresh, and testing of new personalization hypotheses."),
        ],
        "process": [
            ("🔍", "Audience & Data Audit", "We analyze your traffic segments, identify the visitor groups with the most conversion opportunity, and assess what data signals are available to trigger personalization."),
            ("🎯", "Strategy & Content Design", "Personalization strategy defined. Content variants written for each segment. Personalization logic mapped before any implementation begins."),
            ("⚙️", "Implement & Test", "Personalization rules implemented and QA'd. Each variant A/B tested against control. Conversion tracking configured at segment level."),
            ("📈", "Optimize & Expand", "Monthly performance review. Winning personalizations made permanent. New segments and personalization rules added as data accumulates."),
        ],
        "faqs": [
            ("What's the difference between personalization and A/B testing?", "A/B testing serves different variants randomly to all visitors to find the best universal version. Personalization serves specific variants to specific audience segments based on who they are — not randomly. Both work best when used together."),
            ("Do we need a lot of traffic for personalization to work?", "You need enough traffic per segment for statistically meaningful results — typically 500+ monthly visitors per segment. We design personalization programs appropriate to your traffic volume."),
            ("What tools do you use for personalization?", "We work with Mutiny (for B2B SaaS), Webflow CMS, Optimizely, or custom implementations. Tool selection is based on your CMS, tech stack, and personalization complexity."),
            ("Can you personalize for our ad campaigns specifically?", "Yes — UTM-based personalization ensures that visitors from specific campaigns, keywords, or ad groups land on pages that match exactly what they clicked. This alignment dramatically improves Quality Score and conversion rate."),
            ("How do we know personalization is actually helping?", "Every personalization is tested against a control (unpersonalized version). We measure lift in conversion rate, engagement, and pipeline value per segment — providing clear attribution for every personalization investment."),
        ],
        "schema_service_desc": "Website personalization — audience segmentation, dynamic content, CRM integration, A/B testing of variants, segment analytics, and continuous optimization.",
    },
}

NAV_HTML = """  <nav id="navbar">
    <div class="nav-inner">
      <a href="../index.html" class="nav-logo"><span class="logo-lumo">Lumo</span><span class="logo-ai"> AI</span></a>
      <ul class="nav-links">
        <li><a href="../services.html">Services</a></li>
        <li><a href="../industries/">Industries</a></li>
        <li><a href="../about.html">About</a></li>
        <li><a href="../pricing.html">Pricing</a></li>
      </ul>
      <div class="nav-cta"><a href="../contact.html" class="btn-lime">Get a Free Audit</a></div>
      <button class="nav-toggle" aria-label="Toggle menu">&#9776;</button>
    </div>
  </nav>"""

FOOTER_HTML = """  <footer>
    <div class="footer-inner">
      <div class="footer-top">
        <div class="footer-brand">
          <a href="../index.html" class="nav-logo footer-logo"><span class="logo-lumo">Lumo</span><span class="logo-ai"> AI</span></a>
          <p>AI-powered marketing agency helping US businesses grow faster with smarter systems.</p>
          <div class="footer-social">
            <a href="#" aria-label="LinkedIn"><svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433a2.062 2.062 0 01-2.063-2.065 2.064 2.064 0 112.063 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/></svg></a>
            <a href="#" aria-label="Twitter/X"><svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-4.714-6.231-5.401 6.231H2.744l7.73-8.835L1.254 2.25H8.08l4.259 5.631 5.905-5.631zm-1.161 17.52h1.833L7.084 4.126H5.117z"/></svg></a>
          </div>
        </div>
        <div class="footer-col">
          <h4>Services</h4>
          <ul>
            <li><a href="../services/seo.html">SEO</a></li>
            <li><a href="../services/geo.html">GEO</a></li>
            <li><a href="../services/google-ads.html">Google Ads</a></li>
            <li><a href="../services/meta-ads.html">Meta Ads</a></li>
            <li><a href="../services/competitor-analysis.html">Competitor Analysis</a></li>
            <li><a href="../services/marketing-strategy.html">Marketing Strategy</a></li>
            <li><a href="../services/revenue-operations.html">Revenue Operations</a></li>
            <li><a href="../services/ab-testing.html">A/B Testing</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h4>Company</h4>
          <ul>
            <li><a href="../about.html">About</a></li>
            <li><a href="../pricing.html">Pricing</a></li>
            <li><a href="../contact.html">Contact</a></li>
            <li><a href="../privacy-policy.html">Privacy Policy</a></li>
            <li><a href="../terms.html">Terms of Service</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h4>Industries</h4>
          <ul>
            <li><a href="../industries/seo-for-lawyers/">Law Firms</a></li>
            <li><a href="../industries/seo-for-dentists/">Dentists</a></li>
            <li><a href="../industries/healthcare-seo/">Healthcare</a></li>
            <li><a href="../industries/saas-marketing/">SaaS</a></li>
            <li><a href="../industries/ecommerce-marketing/">E-commerce</a></li>
            <li><a href="../industries/home-services-seo/">Home Services</a></li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        <p>&copy; 2026 Lumo AI Agency LLC. All rights reserved.</p>
        <p>Austin, TX &mdash; Serving clients across the United States</p>
      </div>
    </div>
  </footer>"""

def build_page(slug, d):
    services_html = ""
    for icon, title, desc in d["deliverables"]:
        services_html += f"""
        <div class="service-card">
          <div class="service-icon">{icon}</div>
          <h3>{title}</h3>
          <p>{desc}</p>
        </div>"""

    process_html = ""
    for i, (icon, title, desc) in enumerate(d["process"], 1):
        process_html += f"""
        <div class="process-step">
          <div class="step-number">{i:02d}</div>
          <div class="step-icon">{icon}</div>
          <h3>{title}</h3>
          <p>{desc}</p>
        </div>"""

    faq_html = ""
    faq_schema = []
    for q, a in d["faqs"]:
        faq_html += f"""
        <div class="faq-item">
          <button class="faq-q" aria-expanded="false">{q}<span class="faq-arrow">&#9660;</span></button>
          <div class="faq-a"><p>{a}</p></div>
        </div>"""
        faq_schema.append({"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}})

    schema = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "WebPage",
                "@id": f"https://lumoaiagency.com/services/{slug}",
                "url": f"https://lumoaiagency.com/services/{slug}",
                "name": f"{d['title']} | Lumo AI Agency",
                "description": d["schema_service_desc"],
                "breadcrumb": {
                    "@type": "BreadcrumbList",
                    "itemListElement": [
                        {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://lumoaiagency.com"},
                        {"@type": "ListItem", "position": 2, "name": "Services", "item": "https://lumoaiagency.com/services"},
                        {"@type": "ListItem", "position": 3, "name": d["title"], "item": f"https://lumoaiagency.com/services/{slug}"},
                    ],
                },
            },
            {
                "@type": "Service",
                "name": d["title"],
                "description": d["schema_service_desc"],
                "provider": {"@type": "Organization", "name": "Lumo AI Agency", "url": "https://lumoaiagency.com"},
                "areaServed": "US",
                "offers": {"@type": "Offer", "priceCurrency": "USD", "price": d["price"].replace("$", "").replace("/mo", "").replace(",", "")},
            },
            {"@type": "FAQPage", "mainEntity": faq_schema},
        ],
    }

    return f"""<!DOCTYPE html>
<html lang="en-US">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>{d['title']} | Lumo AI Agency</title>
  <meta name="description" content="{d['schema_service_desc']}">
  <link rel="canonical" href="https://lumoaiagency.com/services/{slug}">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Berkshire+Swash&family=Syne:wght@400;600;700;800&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
  <script type="application/ld+json">{json.dumps(schema, indent=2)}</script>
  <style>
    :root{{--bg:#0D0D14;--surface:#13131F;--primary:#B3FF00;--secondary:#7C3AED;--accent:#00F5FF;--text:#E8E8F0;--muted:#9090A8;--border:rgba(255,255,255,.08)}}
    *{{margin:0;padding:0;box-sizing:border-box}}
    body{{background:var(--bg);color:var(--text);font-family:'Inter',sans-serif;line-height:1.6}}
    a{{color:inherit;text-decoration:none}}
    #navbar{{position:fixed;top:0;left:0;right:0;z-index:1000;background:rgba(13,13,20,.95);backdrop-filter:blur(12px);border-bottom:1px solid var(--border)}}
    .nav-inner{{max-width:1180px;margin:0 auto;padding:0 24px;height:68px;display:flex;align-items:center;gap:40px}}
    .nav-logo{{font-family:'Berkshire Swash',serif;font-size:1.4rem}}
    .logo-lumo{{color:#fff}}.logo-ai{{color:var(--primary)}}
    .nav-links{{display:flex;gap:32px;list-style:none;margin-left:auto}}
    .nav-links a{{font-size:.95rem;color:var(--muted);transition:color .2s}}.nav-links a:hover{{color:#fff}}
    .nav-cta .btn-lime{{background:var(--primary);color:#000;font-weight:700;font-size:.85rem;padding:10px 22px;border-radius:8px;transition:opacity .2s}}
    .nav-cta .btn-lime:hover{{opacity:.85}}
    .nav-toggle{{display:none;background:none;border:none;color:#fff;font-size:1.5rem;cursor:pointer;margin-left:12px}}
    @media(max-width:768px){{.nav-links{{display:none;position:absolute;top:68px;left:0;right:0;background:rgba(13,13,20,.98);flex-direction:column;padding:20px 24px;gap:16px;border-bottom:1px solid var(--border)}}.nav-links.open{{display:flex}}.nav-toggle{{display:block}}}}
    .hero{{padding:140px 24px 80px;text-align:center;background:radial-gradient(ellipse 80% 60% at 50% 0%,rgba(124,58,237,.15),transparent)}}
    .hero-eyebrow{{display:inline-block;background:rgba(179,255,0,.1);color:var(--primary);border:1px solid rgba(179,255,0,.3);border-radius:100px;padding:6px 18px;font-size:.85rem;font-weight:600;margin-bottom:24px}}
    .hero h1{{font-family:'Syne',sans-serif;font-size:clamp(2.2rem,5vw,3.6rem);font-weight:800;line-height:1.1;margin-bottom:20px}}
    .hero h1 span{{color:var(--primary)}}
    .hero-sub{{font-size:1.1rem;color:var(--muted);max-width:620px;margin:0 auto 36px}}
    .hero-actions{{display:flex;gap:16px;justify-content:center;flex-wrap:wrap}}
    .btn-primary{{background:var(--primary);color:#0D0D14;padding:14px 32px;border-radius:10px;font-weight:700;font-size:1rem;transition:opacity .2s}}.btn-primary:hover{{opacity:.85}}
    .btn-secondary{{border:1px solid var(--border);color:#fff;padding:14px 32px;border-radius:10px;font-weight:600;font-size:1rem;transition:border-color .2s}}.btn-secondary:hover{{border-color:var(--primary)}}
    .stats-strip{{background:var(--surface);border-top:1px solid var(--border);border-bottom:1px solid var(--border);padding:40px 24px}}
    .stats-inner{{max-width:900px;margin:0 auto;display:grid;grid-template-columns:repeat(3,1fr);gap:24px;text-align:center}}
    .stat-val{{font-family:'Syne',sans-serif;font-size:2.4rem;font-weight:800;color:var(--primary)}}
    .stat-lbl{{font-size:.85rem;color:var(--muted);margin-top:4px}}
    section{{padding:80px 24px}}
    .section-inner{{max-width:1180px;margin:0 auto}}
    .section-label{{font-size:.8rem;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--primary);margin-bottom:12px}}
    .section-title{{font-family:'Syne',sans-serif;font-size:clamp(1.8rem,3.5vw,2.6rem);font-weight:800;margin-bottom:16px}}
    .section-sub{{color:var(--muted);max-width:640px;margin-bottom:48px}}
    .services-grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:24px}}
    .service-card{{background:var(--surface);border:1px solid var(--border);border-radius:16px;padding:28px;transition:border-color .2s}}.service-card:hover{{border-color:rgba(179,255,0,.35)}}
    .service-icon{{font-size:2rem;margin-bottom:14px}}
    .service-card h3{{font-family:'Syne',sans-serif;font-size:1.15rem;font-weight:700;margin-bottom:8px}}
    .service-card p{{color:var(--muted);font-size:.9rem;line-height:1.6}}
    .process-grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:24px}}
    .process-step{{background:var(--surface);border:1px solid var(--border);border-radius:16px;padding:28px;position:relative}}
    .step-number{{font-family:'Syne',sans-serif;font-size:2.5rem;font-weight:800;color:rgba(179,255,0,.15);position:absolute;top:20px;right:20px}}
    .step-icon{{font-size:1.8rem;margin-bottom:12px}}
    .process-step h3{{font-family:'Syne',sans-serif;font-size:1.05rem;font-weight:700;margin-bottom:8px}}
    .process-step p{{color:var(--muted);font-size:.88rem;line-height:1.6}}
    .pricing-box{{background:var(--surface);border:1px solid rgba(179,255,0,.3);border-radius:20px;padding:48px;max-width:600px;margin:0 auto;text-align:center}}
    .price-label{{font-size:.85rem;color:var(--muted);margin-bottom:8px}}
    .price-val{{font-family:'Syne',sans-serif;font-size:3rem;font-weight:800;color:var(--primary);margin-bottom:8px}}
    .price-note{{font-size:.9rem;color:var(--muted);margin-bottom:32px}}
    .faq-list{{max-width:780px;margin:0 auto;display:flex;flex-direction:column;gap:12px}}
    .faq-item{{background:var(--surface);border:1px solid var(--border);border-radius:12px;overflow:hidden}}
    .faq-q{{width:100%;background:none;border:none;color:#fff;font-family:'Inter',sans-serif;font-size:1rem;font-weight:600;text-align:left;padding:20px 24px;cursor:pointer;display:flex;justify-content:space-between;align-items:center;gap:12px}}
    .faq-arrow{{color:var(--primary);transition:transform .3s;flex-shrink:0}}
    .faq-q[aria-expanded="true"] .faq-arrow{{transform:rotate(180deg)}}
    .faq-a{{max-height:0;overflow:hidden;transition:max-height .3s ease}}
    .faq-a p{{padding:0 24px 20px;color:var(--muted);font-size:.95rem;line-height:1.7}}
    .cta-section{{background:linear-gradient(135deg,rgba(124,58,237,.2),rgba(179,255,0,.08));border-top:1px solid var(--border);border-bottom:1px solid var(--border);text-align:center;padding:80px 24px}}
    .cta-section h2{{font-family:'Syne',sans-serif;font-size:clamp(1.8rem,3.5vw,2.8rem);font-weight:800;margin-bottom:16px}}
    .cta-section p{{color:var(--muted);margin-bottom:36px;max-width:540px;margin-left:auto;margin-right:auto}}
    footer{{background:var(--surface);border-top:1px solid var(--border);padding:64px 24px 32px}}
    .footer-inner{{max-width:1180px;margin:0 auto}}
    .footer-top{{display:grid;grid-template-columns:1.4fr 1fr 1fr 1fr;gap:48px;margin-bottom:48px}}
    .footer-brand p{{color:var(--muted);font-size:.9rem;margin-top:12px;line-height:1.6;max-width:240px}}
    .footer-logo{{display:inline-block;margin-bottom:4px}}
    .footer-social{{display:flex;gap:12px;margin-top:16px}}
    .footer-social a{{color:var(--muted);transition:color .2s;display:flex;align-items:center;justify-content:center;width:32px;height:32px}}.footer-social a:hover{{color:var(--primary)}}
    .footer-col h4{{font-family:'Syne',sans-serif;font-weight:700;margin-bottom:16px;font-size:.95rem}}
    .footer-col ul{{list-style:none;display:flex;flex-direction:column;gap:10px}}
    .footer-col a{{color:var(--muted);font-size:.88rem;transition:color .2s}}.footer-col a:hover{{color:#fff}}
    .footer-bottom{{border-top:1px solid var(--border);padding-top:24px;display:flex;justify-content:space-between;flex-wrap:wrap;gap:8px}}
    .footer-bottom p{{color:var(--muted);font-size:.82rem}}
    @media(max-width:768px){{.stats-inner{{grid-template-columns:1fr 1fr}}.footer-top{{grid-template-columns:1fr 1fr}}.hero{{padding:120px 20px 60px}}}}
    @media(max-width:480px){{.stats-inner{{grid-template-columns:1fr}}.footer-top{{grid-template-columns:1fr}}}}
  </style>
</head>
<body>
{NAV_HTML}

  <section class="hero">
    <div class="hero-eyebrow">{d['title']}</div>
    <h1>{d['tagline'].split('—')[0].strip()} — <span>{d['tagline'].split('—')[1].strip() if '—' in d['tagline'] else d['title']}</span></h1>
    <p class="hero-sub">{d['desc'][:200]}...</p>
    <div class="hero-actions">
      <a href="../contact.html" class="btn-primary">Get a Free Strategy Call</a>
      <a href="../pricing.html" class="btn-secondary">View Pricing</a>
    </div>
  </section>

  <div class="stats-strip">
    <div class="stats-inner">
      <div><div class="stat-val">{d['stat1']}</div><div class="stat-lbl">{d['stat1_label']}</div></div>
      <div><div class="stat-val">{d['stat2']}</div><div class="stat-lbl">{d['stat2_label']}</div></div>
      <div><div class="stat-val">{d['stat3']}</div><div class="stat-lbl">{d['stat3_label']}</div></div>
    </div>
  </div>

  <section style="background:var(--surface);border-bottom:1px solid var(--border)">
    <div class="section-inner">
      <div class="section-label">What We Deliver</div>
      <h2 class="section-title">Everything Included in Our {d['title']} Service</h2>
      <p class="section-sub">Full-service {d['title'].lower()} — no outsourcing, no shortcuts.</p>
      <div class="services-grid">{services_html}</div>
    </div>
  </section>

  <section>
    <div class="section-inner">
      <div class="section-label">Our Process</div>
      <h2 class="section-title">How We Deliver Results</h2>
      <p class="section-sub">A proven 4-step process from discovery to delivery.</p>
      <div class="process-grid">{process_html}</div>
    </div>
  </section>

  <section style="background:var(--surface);border-top:1px solid var(--border);border-bottom:1px solid var(--border)">
    <div class="section-inner">
      <div class="section-label">Investment</div>
      <h2 class="section-title" style="text-align:center">Transparent Pricing</h2>
      <div class="pricing-box">
        <div class="price-label">{d['title']} — Starting From</div>
        <div class="price-val">{d['price']}</div>
        <div class="price-note">Custom quotes based on scope and goals</div>
        <a href="../contact.html" class="btn-primary" style="display:inline-block">Request a Custom Quote</a>
      </div>
    </div>
  </section>

  <section>
    <div class="section-inner">
      <div class="section-label">FAQ</div>
      <h2 class="section-title" style="text-align:center">Frequently Asked Questions</h2>
      <div class="faq-list">{faq_html}</div>
    </div>
  </section>

  <div class="cta-section">
    <h2>Ready to Get Started with {d['title']}?</h2>
    <p>Book a free strategy call. We'll review your current situation and show you exactly how we can help.</p>
    <a href="../contact.html" class="btn-primary">Schedule Your Free Consultation</a>
  </div>

{FOOTER_HTML}

  <script>
    const toggle = document.querySelector('.nav-toggle');
    const links = document.querySelector('.nav-links');
    if(toggle) toggle.addEventListener('click', () => links.classList.toggle('open'));
    document.querySelectorAll('.faq-q').forEach(btn => {{
      btn.addEventListener('click', () => {{
        const expanded = btn.getAttribute('aria-expanded') === 'true';
        document.querySelectorAll('.faq-q').forEach(b => {{ b.setAttribute('aria-expanded','false'); b.nextElementSibling.style.maxHeight = null; }});
        if(!expanded){{ btn.setAttribute('aria-expanded','true'); btn.nextElementSibling.style.maxHeight = btn.nextElementSibling.scrollHeight + 'px'; }}
      }});
    }});
  </script>
</body>
</html>"""


os.makedirs("services", exist_ok=True)
for slug, data in SERVICES.items():
    html = build_page(slug, data)
    path = f"services/{slug}.html"
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Created: {path} ({len(html):,} chars)")

print(f"\nDone. {len(SERVICES)} pages created.")
