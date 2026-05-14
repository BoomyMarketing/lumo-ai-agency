"""Batch 17 — Backlog Batch 12: ai-content, ai-ad-creative, crm-setup, sales-funnel-automation, lead-nurture, workflow-automation"""
import json, os

SERVICES = {
    "ai-content": {
        "title": "AI Content Strategy",
        "tagline": "AI-powered content creation at scale — SEO-optimized, on-brand, and human-edited",
        "desc": "AI has transformed content production — but AI-only content fails on quality, brand voice, and credibility. We combine AI-powered production with human editorial oversight to create high-volume, high-quality content that ranks, converts, and sounds unmistakably like your brand. Scale your content without scaling your team.",
        "price": "$3,000/mo",
        "stat1": "10x",
        "stat1_label": "content production speed with AI-assisted workflows",
        "stat2": "72%",
        "stat2_label": "of marketers report AI improves content quality when used correctly",
        "stat3": "3x",
        "stat3_label": "more organic traffic for companies with AI-augmented content programs",
        "deliverables": [
            ("🤖", "AI Content Strategy & Workflow", "A custom AI content workflow designed for your brand: which content types to automate, which require human authorship, prompt engineering frameworks, and quality control checkpoints."),
            ("🔍", "AI-Powered Keyword Research", "Semantic keyword clustering using AI tools: topic gap identification, search intent classification, and content brief generation at scale — identifying hundreds of content opportunities in hours."),
            ("✍️", "Content Production at Scale", "High-volume content production using AI models with human editorial review: blog articles, landing pages, product descriptions, social copy, and email content — with consistent brand voice throughout."),
            ("🎯", "Content Brief Automation", "AI-generated content briefs for every target keyword: outline, key points, competitor summary, target word count, internal links, and FAQs — briefing system your team or writers can execute immediately."),
            ("📐", "Editorial Review & Quality Control", "Every piece of AI-generated content reviewed by human editors: factual verification, brand voice alignment, SEO optimization, and quality gate before publication."),
            ("📊", "Content Performance Analytics", "AI-assisted content performance analysis: automated tracking of what's ranking, what's converting, and what needs refreshing — with prioritized content improvement recommendations."),
            ("🔄", "Content Refresh Program", "Systematic content refreshing using AI to identify underperforming content, generate improvement recommendations, and produce updated drafts for human editorial review."),
        ],
        "process": [
            ("🔍", "Strategy & Workflow Design", "We define your content strategy, design the AI workflow, establish quality standards, and build the prompt frameworks and templates before any production begins."),
            ("⚙️", "Workflow Implementation", "AI tools configured, editorial workflow established, brand voice guide built into prompts, and quality control process implemented. First content batch reviewed and approved."),
            ("✍️", "Production & Publishing", "Regular content production: AI drafts generated, human-edited, SEO-optimized, and published on schedule. Editorial calendar maintained and updated monthly."),
            ("📈", "Analyze & Optimize", "Monthly content performance review: ranking improvements, traffic impact, and content refresh priorities. Workflow refined based on quality outcomes."),
        ],
        "faqs": [
            ("Is AI-generated content penalized by Google?", "Google penalizes low-quality, spammy content regardless of how it was produced. Human-edited, high-quality AI content performs just as well as purely human-written content. Our editorial process ensures every piece meets Google's helpful content standards."),
            ("How do you maintain brand voice with AI content?", "Brand voice is encoded into our prompt frameworks through a detailed style guide, tone examples, and prohibited phrasing. Every piece goes through human editorial review to catch any voice drift before publication."),
            ("What types of content can AI produce effectively?", "AI excels at: informational blog content, product descriptions, FAQ pages, meta descriptions, social copy, and email templates. It requires more human involvement for: thought leadership, original research, highly technical content, and nuanced brand storytelling."),
            ("How much human editing is involved?", "Every piece gets human editorial review — typically 20–40% editing depending on content type. More complex or brand-sensitive content gets heavier editing. We never publish raw AI output."),
            ("Can we use this for content types beyond blog articles?", "Yes — we use AI content workflows for: product descriptions, landing page copy, email sequences, social media content, meta descriptions, and internal documentation. The workflow adapts to any content type."),
        ],
        "schema_service_desc": "AI content strategy — AI-powered production, keyword research, content briefs, editorial review, performance analytics, and systematic content refresh program.",
    },
    "ai-ad-creative": {
        "title": "AI Ad Creative",
        "tagline": "AI-generated and human-refined ad creative that scales testing and maximizes ROAS",
        "desc": "AI has fundamentally changed ad creative production — enabling brands to test 10x more creative variations at the same cost. We use AI image generation, copy tools, and video production to produce high-volume ad creative that's rigorously tested, human-refined for quality, and continuously optimized based on performance data.",
        "price": "$2,500/mo",
        "stat1": "10x",
        "stat1_label": "more creative variations testable with AI production",
        "stat2": "70%",
        "stat2_label": "of ad performance is determined by creative — not targeting",
        "stat3": "3.2x",
        "stat3_label": "average ROAS improvement with systematic creative testing at scale",
        "deliverables": [
            ("🎨", "AI Creative Strategy", "Creative strategy built around AI capabilities: which formats to AI-generate, which to produce traditionally, and how to structure testing to maximize learning velocity."),
            ("🖼️", "AI Image Creative Production", "High-volume static ad creative using Midjourney, DALL-E, and Adobe Firefly — generating diverse visual concepts, product scenarios, and lifestyle imagery at scale for testing."),
            ("✍️", "AI Copy Generation", "Multi-variant ad copy produced using LLMs: headlines, body copy, and CTAs in dozens of variations — testing different value propositions, emotional angles, and audience-specific messaging."),
            ("🎬", "AI-Assisted Video Creative", "Short-form video ad production using AI video tools (Runway, Pika), voiceover generation, and AI motion graphics — dramatically reducing production time and cost for video ad testing."),
            ("🔄", "Human Creative Refinement", "Every AI-generated asset reviewed and refined by human creatives: brand alignment check, quality gate, compliance review, and strategic improvement before any ad goes live."),
            ("🧪", "Systematic Creative Testing", "Structured testing framework: creative matrix design, statistical significance thresholds, winner identification, and loser elimination — extracting maximum learning from every test."),
            ("📊", "Creative Performance Analytics", "Creative-level reporting: CTR, CPM, thumb-stop rate, conversion rate, and ROAS by creative variant — with clear recommendations for scaling winners and developing next-iteration tests."),
        ],
        "process": [
            ("🔍", "Creative Audit & Strategy", "We audit your current creative performance, identify top-performing elements to scale, and build the AI creative strategy and testing roadmap."),
            ("🎨", "Produce & Refine", "AI creative production begins: images, copy, and video concepts generated, human-refined, and organized into test matrices. Brand compliance verified."),
            ("📣", "Launch & Test", "Creative launched across ad platforms with proper test structure. Performance monitored from day one. Statistical significance tracked."),
            ("📈", "Analyze & Iterate", "Bi-weekly creative performance review. Winners scaled, losers replaced. New test hypotheses developed from learnings. AI prompts refined for next production cycle."),
        ],
        "faqs": [
            ("How is AI ad creative different from regular performance creative?", "AI ad creative uses generative AI tools to produce creative at 10x the speed and volume of traditional production — enabling more tests, faster learning, and lower cost per variation. The strategy and human refinement remain the same; the production pipeline is radically faster."),
            ("Does AI creative look lower quality?", "Not with proper human refinement. The best AI creative outputs are indistinguishable from traditionally produced creative. Our human review process filters out low-quality outputs and refines the best AI concepts to production quality."),
            ("Can AI creative be used for all ad platforms?", "Yes — AI creative is adaptable to Meta, TikTok, Google Display, LinkedIn, YouTube, and programmatic. Each platform has different format requirements we account for in our production workflow."),
            ("Do you use AI for video ads too?", "Yes — we use Runway, Pika, and other AI video tools for short-form video concepts, animated static ads, and AI voiceover production. Full AI-generated video has limitations for some creative requirements; we advise on when traditional production is still the right choice."),
            ("How do you ensure AI creative is brand-safe?", "We build brand guidelines into our AI prompts and review every output against brand standards before it goes into testing. Prohibited content categories, required brand elements, and visual style constraints are all encoded into our production workflow."),
        ],
        "schema_service_desc": "AI ad creative — AI image and video production, copy generation, human refinement, creative testing framework, and performance analytics.",
    },
    "crm-setup": {
        "title": "CRM Setup & Integration",
        "tagline": "CRM implementation, data migration, and workflow automation for your revenue team",
        "desc": "A badly configured CRM creates more problems than it solves — cluttered pipelines, missing data, manual data entry, and reporting you don't trust. We implement and configure your CRM correctly from day one: the right deal stages, the right custom properties, clean data migration, and the automations that make your sales team actually use it.",
        "price": "$6,000",
        "stat1": "29%",
        "stat1_label": "average increase in sales productivity with a properly configured CRM",
        "stat2": "74%",
        "stat2_label": "of sales teams report their CRM improves access to customer data",
        "stat3": "8%",
        "stat3_label": "average revenue increase reported after CRM implementation",
        "deliverables": [
            ("🗺️", "CRM Requirements & Architecture", "Discovery sessions with your sales, marketing, and CS teams to define requirements: deal stages, pipeline structure, custom properties, reporting needs, and integration requirements — before any configuration begins."),
            ("⚙️", "CRM Configuration", "Full CRM configuration: deal stages with exit criteria, contact and company property structure, pipeline setup, user permissions, and team organization — built to your actual sales process, not a template."),
            ("📦", "Data Migration", "Clean data migration from your existing CRM, spreadsheets, or scattered sources: data mapping, deduplication, normalization, and import — with validation to ensure data integrity after migration."),
            ("🔗", "Tool Integrations", "Integration with your existing tech stack: email (Gmail, Outlook), calendar, marketing automation, billing (Stripe, QuickBooks), support desk, and other business tools via native integrations or Zapier."),
            ("🤖", "Workflow Automation", "Sales workflow automation: lead assignment rules, deal stage progression triggers, follow-up task creation, notification routing, and data enrichment — eliminating manual CRM data entry for your team."),
            ("📊", "Reporting & Dashboards", "Custom reporting dashboards for leadership and individual reps: pipeline health, forecast accuracy, activity metrics, win/loss analysis, and revenue attribution — data your team actually uses."),
            ("🎓", "Team Training & Adoption", "Role-specific training for sales reps, managers, and admins — covering daily workflows, data entry standards, reporting, and CRM best practices to maximize adoption."),
        ],
        "process": [
            ("🔍", "Discovery & Design", "Requirements gathered from all stakeholders. CRM architecture designed: pipeline structure, property taxonomy, integration map, and automation logic. Design reviewed before any configuration begins."),
            ("⚙️", "Configure & Integrate", "CRM configured to spec. Integrations connected and tested. Automation workflows built and validated. Reporting dashboards created."),
            ("📦", "Data Migration & QA", "Historical data migrated, deduplicated, and validated. Data quality report delivered. Issues resolved before team access is granted."),
            ("🎓", "Train & Launch", "Team training delivered by role. CRM launched with your team actively using it. 30-day hypercare support period for questions and adjustments."),
        ],
        "faqs": [
            ("Which CRM do you implement?", "We primarily implement HubSpot, Salesforce, and Pipedrive. We can also configure Close, Monday CRM, Zoho, and other platforms. If you haven't chosen a CRM yet, we advise on the right fit for your team size, budget, and sales motion."),
            ("Can you migrate data from our current CRM?", "Yes — data migration is a core part of every CRM implementation. We handle mapping, cleaning, deduplication, and import. Complex migrations (multiple sources, inconsistent data) take longer but are fully manageable."),
            ("How long does CRM implementation take?", "Standard HubSpot or Pipedrive implementation: 4–6 weeks. Salesforce implementation: 6–10 weeks. Timelines extend for complex data migrations, custom development, or large team sizes."),
            ("What if our team doesn't use the CRM after implementation?", "Adoption is the hardest part of CRM implementation — and we address it directly. Role-specific training, simplified data entry workflows, and automation that removes manual work are all designed to make adoption the path of least resistance."),
            ("Do you provide ongoing CRM support?", "Yes — we offer monthly CRM administration retainers for ongoing support: new workflow automation, reporting additions, integration updates, and user training as your team grows."),
        ],
        "schema_service_desc": "CRM setup — requirements discovery, full configuration, data migration, tool integrations, workflow automation, reporting dashboards, and team training.",
    },
    "sales-funnel-automation": {
        "title": "Sales Funnel Automation",
        "tagline": "Automated sales funnels that nurture leads and convert them without manual follow-up",
        "desc": "Most leads don't buy the first time they encounter you — they need nurturing, follow-up, and the right offer at the right moment. We build automated sales funnels that do this at scale: lead capture, multi-step nurture sequences, behavioral triggers, and conversion optimization — turning more of your traffic into revenue without adding headcount.",
        "price": "$4,000/mo",
        "stat1": "77%",
        "stat1_label": "of leads never get followed up with adequately",
        "stat2": "5x",
        "stat2_label": "more revenue for companies with mature lead nurture automation",
        "stat3": "35%",
        "stat3_label": "average close rate increase with automated multi-touch follow-up",
        "deliverables": [
            ("🗺️", "Funnel Strategy & Architecture", "Full funnel design: entry points, lead magnet strategy, nurture sequence logic, conversion triggers, and sales handoff criteria — mapped across your buyer journey before any automation is built."),
            ("📝", "Lead Magnet Creation", "High-converting lead magnets designed for your ICP: guides, calculators, assessments, templates, or webinars — with landing pages and opt-in forms optimized for conversion."),
            ("📧", "Email Nurture Sequences", "Multi-step email sequences for every funnel stage: awareness nurture, consideration-stage education, objection handling, and conversion sequences — written in your brand voice with behavioral branching."),
            ("⚡", "Behavioral Triggers & Automation", "Behavior-based automation: email sequences triggered by page visits, content downloads, link clicks, and time delays — serving the right message at the right moment based on actual prospect behavior."),
            ("🔔", "Sales Notification & Handoff", "Automated sales team alerts when leads reach sales-ready signals: lead score thresholds, high-intent page visits, demo requests, and pricing page views — with contextual data for personalized outreach."),
            ("📊", "Funnel Analytics & Conversion Tracking", "Full-funnel conversion tracking: traffic to lead, lead to MQL, MQL to SQL, and SQL to closed — identifying the exact stages where leads are dropping and prioritizing optimization."),
            ("🔄", "Funnel Optimization", "Ongoing A/B testing and optimization: email subject lines, sequence timing, lead magnet conversion, and landing page performance — continuously improving funnel conversion rates."),
        ],
        "process": [
            ("🔍", "Funnel Audit & Strategy", "We audit your current funnel (or start from scratch), map the buyer journey, and design the full funnel architecture before building anything."),
            ("⚙️", "Build & Configure", "Funnel built in your marketing automation platform: landing pages, forms, email sequences, automation rules, and CRM integrations. QA'd end-to-end before launch."),
            ("🚀", "Launch & Monitor", "Funnel launched with traffic directed to entry points. Conversion rates monitored from day one. Issues identified and fixed within 48 hours."),
            ("📈", "Optimize & Scale", "Monthly funnel performance review: conversion rates by stage, email performance, and lead quality. A/B tests run on highest-leverage elements. Winning variants implemented."),
        ],
        "faqs": [
            ("What marketing automation platform do you use?", "We build funnels in HubSpot, ActiveCampaign, Klaviyo (e-commerce), Mailchimp, GoHighLevel, and other platforms. Tool selection is based on your existing stack and funnel complexity requirements."),
            ("How long until the funnel starts generating leads?", "A new funnel can be built and live within 3–4 weeks. Results depend on traffic volume to funnel entry points. If you have existing traffic, results appear quickly. If traffic needs to be built, we recommend pairing with SEO or paid advertising."),
            ("Do you write the email sequences?", "Yes — email copy is written by our team as part of the engagement. We develop a detailed content brief for your review before writing, and deliver polished sequences ready for your final approval."),
            ("What's the difference between a sales funnel and a marketing automation system?", "A sales funnel is the specific journey from lead capture to conversion — it's the strategy. Marketing automation is the technology that executes the funnel. We design the strategy and implement it using the right marketing automation platform for your needs."),
            ("Can you automate follow-up for our existing sales team?", "Yes — sales follow-up automation is one of the highest-ROI use cases. We automate: post-demo follow-up sequences, proposal follow-ups, re-engagement of stalled deals, and renewal reminders — so your reps focus on selling, not chasing."),
        ],
        "schema_service_desc": "Sales funnel automation — funnel strategy, lead magnets, email sequences, behavioral triggers, sales handoff, conversion tracking, and ongoing optimization.",
    },
    "lead-nurture": {
        "title": "Lead Nurture Programs",
        "tagline": "Multi-channel lead nurture sequences that convert cold leads into sales-ready opportunities",
        "desc": "Most leads aren't ready to buy when they first engage — they need education, trust-building, and relevance over time before they're sales-ready. We build multi-channel lead nurture programs that move leads systematically through the funnel: email sequences, retargeting, content tracks, and sales signals — turning cold databases into active pipelines.",
        "price": "$2,500/mo",
        "stat1": "50%",
        "stat1_label": "more sales-ready leads with mature lead nurture programs",
        "stat2": "33%",
        "stat2_label": "lower cost per qualified lead with systematic nurture",
        "stat3": "9x",
        "stat3_label": "more likely to convert leads nurtured vs. non-nurtured",
        "deliverables": [
            ("🗺️", "Lead Nurture Strategy", "Nurture program design: audience segmentation, buyer journey stage mapping, content track logic, and channel mix (email, retargeting, LinkedIn) — tailored to your sales cycle and ICP."),
            ("📧", "Multi-Stage Email Sequences", "Behavior-based email sequences for each funnel stage: awareness nurture (education content), consideration nurture (comparison, ROI content), and intent nurture (testimonials, case studies, demos) — with dynamic branching based on engagement."),
            ("🎯", "Retargeting Integration", "Retargeting campaigns synchronized with email nurture: when an email sequence starts, complementary ads appear across Meta, Google Display, and LinkedIn — multi-channel presence that dramatically improves conversion."),
            ("🏷️", "Lead Scoring Implementation", "Lead scoring model built in your CRM or marketing automation: engagement-based scoring (email opens, page visits, content downloads) and demographic scoring — identifying sales-ready leads automatically."),
            ("📣", "Content Track Development", "Nurture content production: educational emails, case study summaries, ROI calculators, and comparison guides — each piece designed to advance leads to the next funnel stage."),
            ("🔔", "Sales Alert System", "Automated sales team alerts when nurture leads reach sales-readiness thresholds: lead score milestones, high-intent content consumption, and behavioral signals that indicate purchase intent."),
            ("📊", "Nurture Performance Analytics", "Monthly reporting: lead progression by stage, email engagement rates, retargeting click-through, lead score distribution, and sales-ready lead volume — with recommendations for improving conversion at each stage."),
        ],
        "process": [
            ("🔍", "Audience & Journey Mapping", "We segment your lead database, map buyer journey stages, and identify the content and touchpoints needed to advance leads from cold to sales-ready."),
            ("📝", "Content & Sequence Development", "Nurture content produced and email sequences written. Retargeting audiences configured. Lead scoring model built. All reviewed before launch."),
            ("🚀", "Launch & Activate", "Nurture sequences activated for existing leads. New leads automatically enrolled based on source and behavior. Retargeting campaigns synchronized and live."),
            ("📈", "Optimize & Report", "Monthly performance review: lead progression rates, email engagement, and sales conversion. Underperforming sequences refined. New content tracks added for emerging segments."),
        ],
        "faqs": [
            ("How long is a typical nurture sequence?", "Nurture sequence length depends on your sales cycle. Short sales cycles (under 30 days): 3–5 email sequences. Medium cycles (30–90 days): 8–12 emails. Long enterprise cycles: 15+ emails over 6+ months with behavioral branching."),
            ("What if leads don't engage with emails?", "We build re-engagement sequences for inactive leads and test subject lines, send times, and content formats to improve engagement. Chronically unengaged leads are moved to a low-frequency track or cleaned from the database to protect deliverability."),
            ("Can you nurture existing leads in our database?", "Yes — database reactivation is one of the highest-ROI applications of lead nurture. We segment existing leads by age, source, and last activity, and build tailored nurture sequences for each segment."),
            ("How do you integrate nurture with our sales team?", "Nurture programs are designed to hand off to sales at the right moment — when leads reach defined sales-readiness signals. We configure the CRM handoff: lead record updated, rep notified, and context about the lead's engagement history provided."),
            ("What channels do you use beyond email?", "Primary channel is email. Secondary channels: LinkedIn outreach (for B2B), Meta and Google Display retargeting, and SMS (for consumer-facing businesses). We recommend the channel mix based on your audience and sales cycle."),
        ],
        "schema_service_desc": "Lead nurture programs — multi-stage email sequences, retargeting integration, lead scoring, content development, sales alerts, and nurture analytics.",
    },
    "workflow-automation": {
        "title": "Workflow Automation",
        "tagline": "Business process automation that eliminates manual work and scales your operations",
        "desc": "Manual processes are the hidden tax on your growth — every repetitive task your team does is time not spent on high-value work. We map, design, and implement workflow automations across your marketing, sales, and operations — using Zapier, Make, n8n, and native platform integrations to eliminate manual work and create processes that scale without headcount.",
        "price": "$4,000/mo",
        "stat1": "40%",
        "stat1_label": "of work tasks can be automated with current technology",
        "stat2": "3.2x",
        "stat2_label": "higher team output per person with workflow automation in place",
        "stat3": "89%",
        "stat3_label": "of businesses report that automation improves employee satisfaction",
        "deliverables": [
            ("🗺️", "Process Mapping & Audit", "Comprehensive workflow audit: we interview your team, document current processes, and identify the highest-volume, highest-friction manual tasks — prioritized by time saved and error reduction impact."),
            ("⚙️", "Automation Design & Architecture", "For each automation: process design document covering trigger events, action sequences, conditional logic, error handling, and exception workflows — reviewed and approved before any implementation."),
            ("🔧", "Zapier / Make / n8n Implementation", "Automation built using the right tool for each workflow: Zapier for simple 2-step automations, Make (Integromat) for complex multi-step logic, n8n for self-hosted or code-heavy workflows, or native platform automation where available."),
            ("🔗", "Cross-Platform Integrations", "Integration of your tech stack: CRM, marketing automation, project management, billing, communication tools, file storage, and databases — eliminating manual data transfer between systems."),
            ("🧪", "QA & Error Handling", "Every automation QA'd end-to-end with real data: edge case testing, error handling configuration, and monitoring alerts for failed automations — so exceptions are caught and handled gracefully."),
            ("📊", "Automation Analytics", "Usage monitoring for all automations: tasks executed per month, error rates, time saved estimates, and ROI calculation — making the value of automation visible and measurable."),
            ("🔄", "Ongoing Maintenance & Expansion", "Monthly automation maintenance: monitoring for broken workflows caused by API changes, adding new automations as your team identifies new opportunities, and optimizing existing flows for reliability."),
        ],
        "process": [
            ("🔍", "Process Audit", "We interview stakeholders across departments to document manual workflows, estimate time spent, and identify automation opportunities. Priority list delivered with time-saved projections."),
            ("📋", "Design & Approve", "Automation design documents produced for top-priority workflows. Logic reviewed with your team before any implementation — ensuring automations match how your business actually works."),
            ("⚙️", "Build & Test", "Automations built and QA'd with real-world test data. Edge cases tested and error handling configured. Monitoring alerts activated."),
            ("🔄", "Monitor & Expand", "Monthly monitoring report: automation health, tasks executed, and errors caught. New automations added monthly as opportunities are identified. Existing automations maintained and optimized."),
        ],
        "faqs": [
            ("What tools do you use for automation?", "Zapier (most accessible, largest integration library), Make/Integromat (more powerful multi-step logic, lower cost at volume), n8n (self-hosted, unlimited, code-extensible), and native platform automations (HubSpot workflows, Salesforce Flow). We recommend the right tool for each use case."),
            ("Can you automate processes that involve our internal tools?", "If your internal tools have APIs or webhooks, yes — we can automate processes that touch them. We assess API documentation and integration options during the discovery phase."),
            ("How do you handle automation failures?", "Every automation we build includes error handling: automatic retry logic, failure notifications (Slack, email), and fallback actions to ensure data isn't lost when an automation fails. We monitor all automations for failure patterns."),
            ("What processes are best suited for automation?", "Best candidates: repetitive data entry between systems, notification routing (lead assigned, deal stage changed), report generation and distribution, file organization, and status update communications. Poor candidates: decisions requiring judgment, relationship-based tasks, and processes requiring frequent exception handling."),
            ("Can you automate processes that involve AI tools?", "Yes — we build automations that incorporate AI: AI-powered email classification, automatic content generation triggered by events, AI data enrichment workflows, and ChatGPT or Claude API calls embedded in automation sequences."),
        ],
        "schema_service_desc": "Workflow automation — process mapping, automation design, Zapier/Make/n8n implementation, cross-platform integration, QA, and ongoing maintenance.",
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
            <li><a href="../services/ai-consulting.html">AI Consulting</a></li>
            <li><a href="../services/ai-chatbot.html">AI Chatbot</a></li>
            <li><a href="../services/workflow-automation.html">Workflow Automation</a></li>
            <li><a href="../services/crm-setup.html">CRM Setup</a></li>
            <li><a href="../services/sales-funnel-automation.html">Sales Funnel</a></li>
            <li><a href="../services/lead-nurture.html">Lead Nurture</a></li>
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
