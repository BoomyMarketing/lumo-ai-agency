#!/usr/bin/env python3
"""Wave 3 — Batch 3:
   marketing-automation, retargeting, video-production, branding, sms-marketing
"""
import os, json

BASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "services")
os.makedirs(BASE, exist_ok=True)

SERVICES = {

    "marketing-automation": {
        "title_tag":  "Marketing Automation Agency | AI-Powered Workflows & Sequences | Lumo AI",
        "meta_desc":  "Marketing automation services from Lumo AI Agency. CRM automation, email sequences, lead scoring, drip campaigns, and AI-powered workflows that convert leads 24/7. Free automation audit.",
        "canonical":  "https://lumoaiagency.com/services/marketing-automation",
        "og_title":   "Marketing Automation Agency | Lumo AI Agency",
        "og_desc":    "Stop losing leads to slow follow-up. Lumo builds AI-powered marketing automation — email sequences, CRM workflows, lead scoring, and drip campaigns that convert while you sleep.",
        "h1_html":    "Marketing Automation That <span class=\"hl-lime\">Converts Leads</span> While You Sleep",
        "badge":      "Marketing Automation Specialists",
        "lead":       "Companies that automate lead management see a 451% increase in qualified leads. Lumo builds AI-powered automation workflows — from CRM setup to multi-step nurture sequences — that turn cold prospects into paying customers without adding headcount.",
        "stat1_num": "451%", "stat1_lbl": "More qualified leads with lead management automation",
        "stat2_num": "77%",  "stat2_lbl": "Of CMOs say automation increases revenue",
        "stat3_num": "14.5%","stat3_lbl": "Average boost in sales productivity from automation",
        "why_h2": "Why Marketing Automation Is No Longer Optional",
        "why_p1": "Manual follow-up is the enemy of growth. Studies show that leads contacted within 5 minutes are 100x more likely to convert than those contacted 30 minutes later — yet most businesses respond hours or days after a form submission. Marketing automation eliminates this gap entirely, triggering instant, personalised follow-up the moment a prospect takes action.",
        "why_p2": "The compounding effect is where automation truly shines. A well-built nurture sequence works continuously — scoring leads based on behaviour, sending the right message at the right stage, and alerting your sales team only when a prospect hits a qualified threshold. You're not just saving time; you're ensuring no lead falls through the cracks.",
        "why_p3": "Lumo designs automation architecture around your specific sales cycle, integrating CRM, email, SMS, and ad platforms into unified workflows. Our AI layer adds predictive lead scoring and dynamic content personalisation — so each prospect receives messaging calibrated to their interests, behaviour, and likelihood to convert.",
        "services_h2": "Our Marketing Automation Services",
        "services": [
            ("⚙️", "CRM Setup & Integration", "HubSpot, Salesforce, Klaviyo, or ActiveCampaign — we configure your CRM, build custom pipelines, set up contact properties, and integrate with your website, forms, and ad platforms for complete data flow."),
            ("📧", "Email Nurture Sequences", "Multi-step email workflows triggered by behaviour — form submission, page visit, content download, or inactivity. Each sequence is crafted with personalised content that moves prospects through your funnel toward conversion."),
            ("⭐", "Lead Scoring & Qualification", "Behavioural and demographic scoring models that assign points based on pages visited, emails opened, content consumed, and profile fit — automatically surfacing sales-ready leads and suppressing cold contacts."),
            ("🔄", "Drip Campaign Architecture", "Evergreen nurture campaigns that deliver value over weeks or months — educational content, case studies, offers — timed to match your typical sales cycle and adapted to prospect engagement signals."),
            ("🔗", "Cross-Platform Workflow Automation", "Zapier, Make, or native CRM workflows connecting your entire stack — from ad click to CRM entry to email sequence to Slack sales alert — with no manual hand-offs and full audit trails."),
            ("📊", "Automation Analytics & Optimisation", "Sequence performance reports, open/click/conversion tracking by automation step, A/B testing for subject lines and CTAs, and monthly optimisation reviews to improve conversion rates across all active workflows."),
        ],
        "process": [
            ("🗺️", "Audit & Strategy", "Map your current lead flow, identify automation gaps, define conversion goals, and design the automation architecture — sequences, triggers, scoring rules, and integration requirements."),
            ("🏗️", "Build & Integrate", "Configure CRM, build email templates, set up workflow triggers, connect integrations, and deploy lead scoring models — with full testing before any automation goes live."),
            ("🚀", "Launch & Monitor", "Activate automation workflows with monitoring in place — tracking deliverability, open rates, conversion events, and pipeline movement across the first 30 days."),
            ("📈", "Optimise & Expand", "Monthly performance reviews with A/B test results, sequence refinements, scoring model updates, and new workflow additions as your product and market evolve."),
        ],
        "price_from": "$1,500",
        "price_note": "per month — includes CRM configuration, sequence building, and ongoing optimisation",
        "faqs": [
            ("Which marketing automation platforms does Lumo work with?", "Lumo works across major platforms including HubSpot, Salesforce, Klaviyo, ActiveCampaign, Mailchimp, Drip, and Marketo — as well as workflow automation tools like Zapier and Make. Platform selection depends on your existing stack, team size, and budget. We'll recommend the right tool for your specific situation rather than defaulting to the most expensive option."),
            ("How long does it take to set up marketing automation?", "A standard CRM setup and email sequence deployment takes 3–4 weeks from kickoff to live automation. More complex builds with custom integrations, advanced lead scoring, and multi-channel workflows typically take 6–8 weeks. We prioritise getting your highest-impact workflows live first, then layer in complexity over time."),
            ("Do I need a large contact list for automation to be worthwhile?", "Automation ROI scales with contact volume, but the systems are worth building even with smaller lists — because they work correctly from the first lead. The sequences, scoring rules, and workflows you build now compound in value as your list grows. We've seen clients with 500-contact lists generate significant pipeline through well-designed nurture programs."),
            ("What's the difference between marketing automation and email marketing?", "Email marketing is typically campaign-based — one message sent to a segment at a scheduled time. Marketing automation is behaviour-based — triggered by what a specific person does, personalised to their profile, and part of a connected workflow that adapts based on how they respond. Automation includes email but also CRM updates, lead scoring changes, sales alerts, and cross-platform triggers."),
            ("Can Lumo integrate automation with our existing CRM?", "Yes — CRM integration is central to our automation builds. We work within your existing CRM environment rather than requiring you to switch platforms. This includes mapping data fields, configuring sync rules, building custom properties, and ensuring bi-directional data flow between your automation platform and CRM."),
        ],
        "cta_h2": "Ready to Convert More Leads Without Adding Headcount?",
        "cta_sub": "Get a free marketing automation audit — we'll map your current lead flow, identify automation gaps, and show you exactly how much pipeline you're leaving on the table.",
        "schema_service_name": "Marketing Automation Services",
        "schema_service_desc": "AI-powered marketing automation for US businesses — CRM setup, email nurture sequences, lead scoring, drip campaigns, and cross-platform workflow automation.",
    },

    "retargeting": {
        "title_tag":  "Retargeting Agency | AI-Powered Remarketing That Re-Engages Buyers | Lumo AI",
        "meta_desc":  "Retargeting and remarketing services from Lumo AI Agency. Dynamic retargeting on Google, Meta, LinkedIn, and programmatic — re-engage lost visitors and recover abandoned carts. Free audit.",
        "canonical":  "https://lumoaiagency.com/services/retargeting",
        "og_title":   "Retargeting Agency | Lumo AI Agency",
        "og_desc":    "97% of site visitors leave without converting. Lumo's AI-powered retargeting campaigns re-engage them — with personalised ads across Google, Meta, LinkedIn, and programmatic channels.",
        "h1_html":    "Retargeting Campaigns That <span class=\"hl-lime\">Win Back</span> Lost Visitors",
        "badge":      "Retargeting & Remarketing Specialists",
        "lead":       "97% of website visitors leave without converting. Retargeting lets you follow them with relevant ads across every platform they use — bringing them back when they're ready to buy. Lumo builds dynamic retargeting strategies across Google, Meta, LinkedIn, and programmatic channels.",
        "stat1_num": "97%",  "stat1_lbl": "Of visitors leave without converting — retargeting gets them back",
        "stat2_num": "10x",  "stat2_lbl": "Higher CTR for retargeted vs. cold display ads",
        "stat3_num": "70%",  "stat3_lbl": "Of consumers prefer ads relevant to their browsing history",
        "why_h2": "Why Retargeting Is Your Highest-ROI Advertising Channel",
        "why_p1": "Most advertising targets cold audiences — people who have never heard of your brand. Retargeting is fundamentally different: you're reaching people who already visited your site, engaged with your content, or interacted with your brand. They're warmer, more familiar, and significantly more likely to convert when shown a relevant ad.",
        "why_p2": "The economics are compelling. Retargeted ads cost more per impression than cold display, but they convert at dramatically higher rates — often 2–10x the conversion rate of prospecting campaigns. When you calculate cost-per-conversion rather than cost-per-click, retargeting consistently delivers the lowest CPA of any paid channel.",
        "why_p3": "Lumo builds multi-platform retargeting architecture that follows prospects across their entire digital journey — from Google search to Instagram feed to LinkedIn sidebar to streaming TV. Our dynamic creative personalises ad content based on which pages were visited, which products were viewed, and how far into your funnel the prospect progressed.",
        "services_h2": "Our Retargeting Services",
        "services": [
            ("🎯", "Google Remarketing", "RLSA (Remarketing Lists for Search Ads) and display remarketing across Google's network — adjusting bids and creative for past visitors, cart abandoners, and customer match audiences with Smart Bidding optimisation."),
            ("📘", "Meta Retargeting", "Custom audience retargeting on Facebook and Instagram — site visitors, video viewers, Instagram engagers, and lead form openers — with dynamic product ads for e-commerce and sequence-based creative for services."),
            ("💼", "LinkedIn Retargeting", "Website retargeting and Matched Audiences for B2B — re-engaging site visitors with Sponsored Content and Message Ads, with company and job title targeting layered on for account-based retargeting."),
            ("🖥️", "Programmatic Retargeting", "Open-web retargeting across premium publisher inventory, CTV, and audio — serving personalised ads to past visitors wherever they browse, stream, or listen via DSP-powered audience segments."),
            ("🛒", "Dynamic Product Retargeting", "Automated personalised ads showing the exact products or services a visitor viewed — with dynamic pricing, availability, and CTA updates — for e-commerce and high-SKU businesses."),
            ("📊", "Audience Segmentation & Attribution", "Funnel-stage audience segmentation — from first-time visitors to cart abandoners to loyal customers — with multi-touch attribution connecting retargeting impressions and clicks to actual conversions."),
        ],
        "process": [
            ("🏷️", "Pixel & Audience Setup", "Deploy tracking pixels, configure conversion events, build retargeting audience segments by funnel stage and behaviour, and set up custom audience exclusions to avoid ad fatigue."),
            ("🎨", "Creative & Sequence Design", "Develop retargeting ad creative per audience segment, design sequential messaging that builds toward conversion, and set frequency caps to maximise impact without over-exposing audiences."),
            ("🚀", "Launch & Optimise", "Go live across all retargeting channels simultaneously, monitor frequency, CTR, and conversion metrics daily, and apply optimisations within the first 7 days as data accumulates."),
            ("📈", "Scale & Expand", "Layer in new audience segments, expand to additional platforms, test dynamic creative variants, and expand budgets on highest-converting audiences as performance data matures."),
        ],
        "price_from": "$1,200",
        "price_note": "per month management fee — ad spend is separate (typically $1,000–$5,000/mo)",
        "faqs": [
            ("What's the difference between retargeting and remarketing?", "The terms are often used interchangeably. Technically, remarketing typically refers to Google's email-based re-engagement (contacting past customers via email lists), while retargeting refers to pixel-based ad campaigns that follow visitors across the web. In modern usage, both terms usually mean the same thing — showing ads to people who previously interacted with your brand."),
            ("How does retargeting tracking work?", "Retargeting uses small pieces of code (pixels) placed on your website. When someone visits, the pixel fires and adds them to a retargeting audience — which ad platforms then use to serve relevant ads. Different pages can create different audiences: homepage visitors get different ads than product page visitors or cart abandoners. This requires no personal data — it's cookied to anonymous browser IDs."),
            ("How long should retargeting audiences be?", "Audience window depends on your sales cycle. E-commerce typically uses 7–30 day windows. B2B services with longer decision cycles benefit from 60–90 day windows. We configure windows to match how long a typical prospect takes to move from awareness to decision, and set frequency caps to prevent oversaturation during that window."),
            ("What happens to retargeting with cookie deprecation?", "Third-party cookie deprecation affects some retargeting methods, but first-party data retargeting (your own email lists matched to ad platforms, or consent-based site visitors) remains fully effective. We're also building contextual and cohort-based retargeting strategies as part of every retargeting program to future-proof your campaigns."),
            ("Can retargeting work for B2B, not just e-commerce?", "Yes — B2B retargeting is often even more valuable than e-commerce retargeting because B2B sales cycles are longer. Staying visible to prospects as they research and evaluate options over weeks or months is a major competitive advantage. LinkedIn retargeting with job title and company filters is particularly powerful for B2B retargeting with high audience precision."),
        ],
        "cta_h2": "Ready to Win Back the 97% Who Left Without Converting?",
        "cta_sub": "Get a free retargeting audit — we'll analyse your current audience setup, identify missed opportunities, and build a multi-platform retargeting strategy for your business.",
        "schema_service_name": "Retargeting & Remarketing Services",
        "schema_service_desc": "AI-powered retargeting campaigns for US businesses — dynamic remarketing across Google, Meta, LinkedIn, and programmatic channels to re-engage and convert lost visitors.",
    },

    "video-production": {
        "title_tag":  "Video Production Agency | Marketing Video & Ad Creative | Lumo AI",
        "meta_desc":  "Video production services from Lumo AI Agency. Brand videos, ad creative, explainer videos, social content, and testimonial production optimised for conversion. Free video strategy call.",
        "canonical":  "https://lumoaiagency.com/services/video-production",
        "og_title":   "Video Production Agency | Lumo AI Agency",
        "og_desc":    "Marketing video that converts — not just looks good. Lumo produces brand videos, ad creative, explainers, and social content built around performance goals, not production awards.",
        "h1_html":    "Video Production That <span class=\"hl-lime\">Drives Conversions</span>, Not Just Views",
        "badge":      "Performance Video Specialists",
        "lead":       "Video drives 80% of all internet traffic and delivers 66% more qualified leads than text-based content. Lumo produces marketing video built around performance goals — brand stories, ad creative, explainers, and social content that converts viewers into customers.",
        "stat1_num": "80%", "stat1_lbl": "Of all internet traffic is video content",
        "stat2_num": "66%", "stat2_lbl": "More qualified leads from video vs. text content",
        "stat3_num": "54%", "stat3_lbl": "Of consumers want more brand video content",
        "why_h2": "Why Most Marketing Video Fails (And How Lumo Fixes It)",
        "why_p1": "Most marketing video is produced by creative teams optimised for awards, not outcomes. Beautiful cinematography, expensive post-production, and brand-approved messaging — but no hook that stops the scroll, no clear value proposition in the first 5 seconds, and no call-to-action that drives the next step. The result is high production cost and low conversion impact.",
        "why_p2": "Performance video starts from a completely different brief. Before cameras roll, we define the target audience, the specific conversion goal, the platform where it will run, and the message hierarchy that matters to the viewer — not the brand. The script is reverse-engineered from what drives action, not from what sounds impressive in a boardroom presentation.",
        "why_p3": "Lumo's video production combines creative storytelling with performance marketing expertise. Every video we produce is designed with platform requirements in mind — correct aspect ratios, hook timing, caption optimisation, and CTA placement for the specific channel where it will run. We measure success by conversion rate and ROAS, not YouTube view counts.",
        "services_h2": "Our Video Production Services",
        "services": [
            ("🎬", "Brand & Explainer Videos", "2–4 minute brand story or product explainer videos — scripted, produced, and edited to communicate your value proposition clearly and memorably to cold audiences encountering your brand for the first time."),
            ("📱", "Social Media Video Content", "Short-form vertical video for TikTok, Instagram Reels, and YouTube Shorts — hook-driven, platform-native content that stops the scroll and drives profile visits, follows, and direct response actions."),
            ("📺", "Video Ad Creative", "15, 30, and 60-second ad creative for YouTube, Meta, TikTok, and CTV — performance-oriented scripts with proven hooks, clear offers, and platform-specific aspect ratios for maximum conversion impact."),
            ("🎤", "Testimonial & Case Study Videos", "Customer testimonial and case study productions — scripted interview formats, b-roll integration, and post-production that builds trust credibility and objection-handling for mid-funnel audiences."),
            ("🏢", "Corporate & Event Video", "Company culture videos, product launch films, conference coverage, and internal communications — professional production that represents your brand correctly across hiring, investor, and partner touchpoints."),
            ("✂️", "Video Editing & Post-Production", "Post-production services for existing footage — editing, colour grading, motion graphics, caption creation, music licensing, and platform-specific export for teams with footage that needs professional finishing."),
        ],
        "process": [
            ("📝", "Script & Strategy", "Define conversion goal, target audience, and platform requirements. Develop script and storyboard with performance hooks, value proposition hierarchy, and CTA strategy built in from the first draft."),
            ("🎬", "Production", "Professional filming with directed talent, b-roll capture, and on-set art direction — or remote production for talking-head content — with raw footage and all assets delivered for post."),
            ("✂️", "Post-Production", "Editing, colour correction, motion graphics, music, voiceover, and caption integration — with review rounds and platform-specific export files for all intended distribution channels."),
            ("📊", "Launch & Optimise", "Deploy across target channels, monitor view-through rate, CTR, and conversion metrics, and iterate on hooks and CTAs based on performance data to improve results over time."),
        ],
        "price_from": "$2,500",
        "price_note": "per video — packages available for ongoing content production (4+ videos/mo from $1,800/video)",
        "faqs": [
            ("What types of video does Lumo produce?", "Lumo produces brand videos, product explainers, social media content (Reels, TikToks, Shorts), video ad creative (YouTube, Meta, CTV), testimonials, case study videos, company culture videos, and post-production/editing services. All video is produced with specific marketing objectives in mind, not general brand awareness."),
            ("Do you produce video remotely or on-location?", "Both. Lumo can direct and coordinate remote productions for talking-head content, screenshare demos, and customer testimonials — reducing cost and turnaround time for distributed teams. For higher-production brand videos and ad creative, we work with professional production crews in-market with full on-location production."),
            ("How long does the video production process take?", "Standard explainer or brand video: 4–6 weeks from brief to final delivery. Social content batches (4–8 videos): 2–3 weeks. Video ad creative: 2–3 weeks. Turnaround depends on approval cycles and revision rounds — we recommend allocating 2 revision rounds per video in the project timeline."),
            ("How do you measure video performance?", "We track platform-specific metrics aligned with your conversion goal: view-through rate and CTR for ad creative, click-to-play rate for embedded web video, engagement rate for social content, and conversion events (leads, purchases) connected via UTM parameters and pixel tracking. Performance data informs creative iteration on subsequent productions."),
            ("Can Lumo help distribute and promote the video once produced?", "Yes — Lumo integrates video production with paid promotion and organic distribution. We can manage YouTube ad campaigns, Meta and TikTok video ads, and organic posting strategies as an add-on to production. This end-to-end approach ensures the video is produced with platform requirements in mind and receives the distribution it needs to perform."),
        ],
        "cta_h2": "Ready to Make Video That Actually Converts?",
        "cta_sub": "Get a free video strategy session — we'll review your current content, identify the highest-impact video formats for your audience, and map a production plan around your conversion goals.",
        "schema_service_name": "Marketing Video Production Services",
        "schema_service_desc": "Performance-focused video production for US businesses — brand videos, ad creative, social content, explainers, and testimonials built for conversion, not awards.",
    },

    "branding": {
        "title_tag":  "Branding Agency | Brand Strategy & Visual Identity | Lumo AI",
        "meta_desc":  "Branding services from Lumo AI Agency. Brand strategy, visual identity, logo design, brand voice, and brand guidelines for US businesses ready to stand out and scale. Free brand audit.",
        "canonical":  "https://lumoaiagency.com/services/branding",
        "og_title":   "Branding Agency | Lumo AI Agency",
        "og_desc":    "Brand strategy and visual identity that makes you memorable. Lumo builds cohesive brand systems — strategy, positioning, logo, visual identity, and voice — for US businesses ready to scale.",
        "h1_html":    "Branding That Makes You <span class=\"hl-lime\">Impossible to Ignore</span>",
        "badge":      "Brand Strategy Specialists",
        "lead":       "Consistent brand presentation increases revenue by 33%. Lumo builds brand systems from strategy to visual identity — positioning, messaging, logo design, colour systems, and brand guidelines that make your business instantly recognisable and remarkably consistent across every touchpoint.",
        "stat1_num": "33%",  "stat1_lbl": "Revenue increase from consistent brand presentation",
        "stat2_num": "5–7x", "stat2_lbl": "More impressions needed to convert without strong branding",
        "stat3_num": "89%",  "stat3_lbl": "Of consumers stay loyal to brands that share their values",
        "why_h2": "Why Strong Branding Is a Revenue Strategy, Not a Vanity Project",
        "why_p1": "Weak branding forces you to compete on price. When your visual identity looks like everyone else's, your messaging sounds like everyone else's, and your positioning is undefined, prospects default to whichever option is cheapest. Strong branding creates the perception of premium value — justifying higher prices, reducing sales friction, and turning customers into advocates.",
        "why_p2": "Branding compounds over time in a way advertising doesn't. Every ad campaign starts from zero when the budget stops. But brand equity — the recognition, trust, and preference your brand accumulates — persists and grows with every consistent customer touchpoint. The businesses that dominate their categories have invested in branding early, not as an afterthought.",
        "why_p3": "Lumo approaches branding as a business strategy problem, not a design exercise. We start with positioning — who you are, who you serve, what makes you different, and what you stand for — before opening any design software. The visual identity, messaging framework, and brand voice all flow from a strategy that's grounded in your market and differentiated from your competitors.",
        "services_h2": "Our Branding Services",
        "services": [
            ("🎯", "Brand Strategy & Positioning", "Competitive positioning analysis, target audience definition, brand purpose and values development, and market differentiation strategy — the strategic foundation that every brand element is built on."),
            ("✏️", "Logo Design & Visual Identity", "Primary logo design, logo variations, colour palette, typography system, iconography, and visual design language — delivered in all required file formats with a comprehensive brand style guide."),
            ("📖", "Brand Messaging & Voice", "Brand voice definition, messaging hierarchy, elevator pitch, tagline development, and copy guidelines — ensuring your brand communicates consistently and compellingly across every channel."),
            ("📋", "Brand Guidelines", "Comprehensive brand standards document — logo usage rules, colour specifications, typography hierarchy, photography style, tone of voice guidelines, and do/don't examples for every major application."),
            ("🔄", "Brand Refresh & Rebrand", "Strategic brand evolution for established businesses — updating visual identity and messaging while preserving brand equity, with change management guidance for internal and external communication."),
            ("🏪", "Brand Applications", "Applying your new brand system across digital and physical touchpoints — website design direction, social media templates, email signature, presentation decks, business cards, and marketing collateral."),
        ],
        "process": [
            ("🔍", "Discovery & Research", "Stakeholder interviews, competitive audit, target audience analysis, and brand assessment — building the strategic foundation with the market context, customer insights, and competitive gaps that inform positioning."),
            ("🎯", "Strategy & Positioning", "Define brand purpose, values, and personality. Develop positioning statement, messaging architecture, and brand voice — signed off before any visual design begins."),
            ("🎨", "Visual Identity Design", "Logo concepts, colour palette, typography, and visual system — presented as strategic design options with rationale, refined through feedback, and finalised with all file deliverables."),
            ("📦", "Delivery & Rollout", "Deliver brand guidelines, asset files, and template library. Guide internal brand adoption and support initial rollout across digital and physical touchpoints."),
        ],
        "price_from": "$3,500",
        "price_note": "for brand strategy + visual identity — comprehensive brand system packages from $6,500",
        "faqs": [
            ("What's included in a full brand identity project?", "A full brand identity project from Lumo includes: brand strategy and positioning, logo design (primary + variations), colour palette, typography system, brand voice and messaging framework, brand guidelines document, and asset delivery in all required formats. Add-ons include website design direction, social media templates, and marketing collateral design."),
            ("How long does a branding project take?", "A complete brand strategy and visual identity project typically takes 6–10 weeks from kickoff to final delivery. Brand strategy and messaging development: 2–3 weeks. Visual identity design and refinement: 3–5 weeks. Brand guidelines documentation: 1–2 weeks. Timeline depends on the number of stakeholders involved and revision rounds."),
            ("What's the difference between a logo and a brand?", "A logo is a visual mark — one element of a brand. A brand is the complete experience and perception of your business: your positioning, personality, values, visual identity, messaging, and the feeling customers have when they interact with you. Lumo builds complete brand systems, not standalone logos. A great logo without strategy is just a graphic."),
            ("We already have a logo — do we need a full rebrand?", "Not necessarily. We offer targeted brand services for businesses that have core assets but need strategic reinforcement — a messaging refresh, brand guidelines to ensure consistency, or visual identity updates that modernise without full replacement. We'll audit your existing brand and recommend the scope of work required to achieve your goals."),
            ("How do you ensure the brand reflects our business, not just design trends?", "Our process starts with your business — not design trends or our own aesthetic preferences. The strategy phase (competitive analysis, audience research, positioning development) produces a clear brief that constrains the design direction. Visual concepts are evaluated against strategic criteria, not just how they look. We're designing for your market, not for a design portfolio."),
        ],
        "cta_h2": "Ready to Build a Brand That Commands Attention and Premium Pricing?",
        "cta_sub": "Get a free brand audit — we'll assess your current brand positioning, identify consistency gaps, and map a strategy to make your business unmistakably recognisable.",
        "schema_service_name": "Branding & Visual Identity Services",
        "schema_service_desc": "Brand strategy, visual identity, and messaging development for US businesses — from positioning and logo design to comprehensive brand guidelines and brand voice.",
    },

    "sms-marketing": {
        "title_tag":  "SMS Marketing Agency | Text Message Campaigns That Convert | Lumo AI",
        "meta_desc":  "SMS marketing services from Lumo AI Agency. Text message campaigns, automated flows, abandoned cart recovery, and promotional blasts with 98% open rates. Free SMS strategy session.",
        "canonical":  "https://lumoaiagency.com/services/sms-marketing",
        "og_title":   "SMS Marketing Agency | Lumo AI Agency",
        "og_desc":    "98% of text messages are read within 3 minutes. Lumo builds SMS marketing programs — promotional campaigns, automated flows, and cart recovery — that drive immediate revenue.",
        "h1_html":    "SMS Marketing With <span class=\"hl-lime\">98% Open Rates</span> — No Inbox Required",
        "badge":      "SMS Marketing Specialists",
        "lead":       "Email gets a 20% open rate. SMS gets 98% — and most texts are read within 3 minutes of receipt. Lumo builds compliant SMS marketing programs that drive immediate revenue: promotional campaigns, automated flows, cart abandonment recovery, and loyalty programs for US businesses.",
        "stat1_num": "98%", "stat1_lbl": "Of SMS messages are opened — vs. 20% for email",
        "stat2_num": "3min","stat2_lbl": "Average time to open a text message after receipt",
        "stat3_num": "19%", "stat3_lbl": "Average CTR for SMS campaigns vs. 2.5% for email",
        "why_h2": "Why SMS Is the Most Direct Marketing Channel Available",
        "why_p1": "Every other marketing channel competes for attention. Social media algorithms decide whether your post gets shown. Email providers filter messages to promotions folders or spam. Search ads require the prospect to actively search. SMS bypasses every one of these gatekeepers — your message arrives directly in the most personal communication channel your customer has, and they almost always read it.",
        "why_p2": "The engagement gap is staggering. Email achieves 20% open rates on a good day. SMS achieves 98%, with 90% of messages read within 3 minutes. Click-through rates follow suit — SMS CTR averages 19% versus email's 2.5%. For time-sensitive offers, abandoned carts, appointment reminders, and flash promotions, there is no channel that reaches customers faster or more reliably.",
        "why_p3": "Lumo builds SMS programs that are both high-performing and fully TCPA-compliant. Every program starts with consent architecture — ensuring opt-ins are explicit, documented, and legally defensible — before any messages are sent. We manage list health, carrier compliance, and message content to protect your brand and your customer relationships.",
        "services_h2": "Our SMS Marketing Services",
        "services": [
            ("📱", "SMS Campaign Management", "Promotional text campaigns for sales, launches, and limited offers — with audience segmentation, send-time optimisation, A/B testing, and post-campaign performance analysis."),
            ("🔄", "Automated SMS Flows", "Behaviour-triggered SMS sequences — welcome series, post-purchase flows, re-engagement campaigns, and milestone messages — that run automatically based on customer actions and lifecycle stage."),
            ("🛒", "Abandoned Cart Recovery", "Cart abandonment SMS sequences that recover lost e-commerce revenue — timed message series with personalised product references, social proof, and offer triggers to bring shoppers back to checkout."),
            ("📋", "List Building & Compliance", "Opt-in keyword setup, consent collection workflows, TCPA compliance architecture, subscriber segmentation, and list hygiene management — the legal and technical foundation of a healthy SMS program."),
            ("🎁", "Loyalty & VIP Programs", "VIP subscriber list management, exclusive SMS-first offers, birthday and anniversary triggers, and loyalty reward programs that increase customer lifetime value and repeat purchase rates."),
            ("📊", "SMS Analytics & Optimisation", "Delivery rate, open rate, click rate, conversion, and revenue-per-message tracking — with monthly reports and optimisation recommendations across campaigns, flows, and list segmentation."),
        ],
        "process": [
            ("📋", "Compliance & Setup", "Configure SMS platform (Klaviyo, Attentive, or Postscript), set up opt-in keywords, build consent collection, configure carrier settings, and establish TCPA-compliant list management procedures."),
            ("✍️", "Campaign & Flow Design", "Write campaign messaging, design automated flow sequences, set up segmentation logic, configure send-time windows, and establish frequency rules — balancing revenue performance with subscriber experience."),
            ("🚀", "Launch & Monitor", "Deploy flows and first campaigns, monitor delivery rates and carrier filtering, track opt-out rates as a health signal, and adjust messaging and timing based on early performance data."),
            ("📈", "Optimise & Expand", "A/B test message copy and CTAs, expand flow coverage, grow subscriber list through pop-up and checkout opt-in optimisation, and scale campaign frequency as subscriber engagement data matures."),
        ],
        "price_from": "$1,000",
        "price_note": "per month — includes platform setup, campaign management, and compliance monitoring (message costs separate)",
        "faqs": [
            ("Is SMS marketing legal?", "Yes, when implemented correctly. SMS marketing in the US is regulated by the Telephone Consumer Protection Act (TCPA), which requires explicit written consent before sending marketing texts. Lumo builds every SMS program with TCPA compliance as the foundation — proper opt-in consent collection, clear disclosures, easy opt-out mechanisms (STOP keyword), and documented consent records. Non-compliant SMS can result in significant fines, so we treat compliance as non-negotiable."),
            ("Which SMS marketing platforms does Lumo work with?", "Lumo works with Klaviyo, Attentive, Postscript, SMSBump, and Omnisend — selecting the platform based on your e-commerce setup, existing tech stack, and subscriber volume. For non-e-commerce businesses, we also work with Twilio and SimpleTexting for service-based SMS programs."),
            ("How do I build an SMS subscriber list?", "List building for SMS uses multiple collection points: website pop-ups with SMS opt-in, checkout opt-in for e-commerce, keyword opt-ins ('Text JOIN to 12345'), social media promotions driving keyword sign-ups, and integrated opt-in on email sign-up forms. Lumo designs a multi-channel list growth strategy alongside the SMS program itself to ensure subscriber volume grows consistently."),
            ("What's a good send frequency for SMS marketing?", "Frequency depends on your subscriber base and content quality. For e-commerce, 4–8 promotional SMS per month is the standard range — supplemented by automated flows triggered by behaviour. For service businesses, 2–4 per month is typical. The signal to watch is opt-out rate: above 2% per campaign suggests either too-high frequency or irrelevant messaging."),
            ("How does SMS work alongside email marketing?", "SMS and email are complementary, not competing. Email is better for longer content, storytelling, and content marketing. SMS is better for time-sensitive offers, urgency, and immediate engagement. The best programs use both — email for nurturing and relationship-building, SMS for promotions that need to be seen and acted on immediately. Lumo coordinates both channels to avoid message fatigue and overlap."),
        ],
        "cta_h2": "Ready to Reach Customers Where They're Guaranteed to See It?",
        "cta_sub": "Get a free SMS marketing audit — we'll review your current list size, compliance setup, and revenue opportunity, and show you what a compliant, high-converting SMS program looks like for your business.",
        "schema_service_name": "SMS Marketing Services",
        "schema_service_desc": "TCPA-compliant SMS marketing for US businesses — promotional campaigns, automated flows, cart abandonment recovery, and loyalty programs with 98% open rates.",
    },

}


# ── HTML Template ────────────────────────────────────────────────────────────
def build_page(slug, d):
    services_html = "\n".join(
        f"""          <div class="svc-card">
            <div class="svc-icon">{icon}</div>
            <h3>{title}</h3>
            <p>{desc}</p>
          </div>"""
        for icon, title, desc in d["services"]
    )

    process_html = "\n".join(
        f"""          <div class="step-card">
            <div class="step-num">{i+1:02d}</div>
            <div class="step-icon">{icon}</div>
            <h3>{title}</h3>
            <p>{desc}</p>
          </div>"""
        for i, (icon, title, desc) in enumerate(d["process"])
    )

    faq_html = "\n".join(
        f"""        <div class="faq-item">
          <button class="faq-q" aria-expanded="false">{q}<span class="faq-chevron">›</span></button>
          <div class="faq-a"><p>{a}</p></div>
        </div>"""
        for q, a in d["faqs"]
    )

    schema = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "WebPage",
                "@id": d["canonical"],
                "url": d["canonical"],
                "name": d["title_tag"],
                "description": d["meta_desc"],
                "breadcrumb": {
                    "@type": "BreadcrumbList",
                    "itemListElement": [
                        {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://lumoaiagency.com/"},
                        {"@type": "ListItem", "position": 2, "name": "Services", "item": "https://lumoaiagency.com/services"},
                        {"@type": "ListItem", "position": 3, "name": d["schema_service_name"], "item": d["canonical"]},
                    ]
                }
            },
            {
                "@type": "Service",
                "name": d["schema_service_name"],
                "description": d["schema_service_desc"],
                "provider": {
                    "@type": "Organization",
                    "name": "Lumo AI Agency",
                    "url": "https://lumoaiagency.com"
                },
                "areaServed": {"@type": "Country", "name": "United States"},
                "serviceType": d["schema_service_name"],
            },
            {
                "@type": "FAQPage",
                "mainEntity": [
                    {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}}
                    for q, a in d["faqs"]
                ]
            }
        ]
    }

    return f"""<!DOCTYPE html>
<html lang="en-US">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>{d["title_tag"]}</title>
  <meta name="description" content="{d["meta_desc"]}">
  <link rel="canonical" href="{d["canonical"]}">
  <meta property="og:type" content="website">
  <meta property="og:title" content="{d["og_title"]}">
  <meta property="og:description" content="{d["og_desc"]}">
  <meta property="og:url" content="{d["canonical"]}">
  <meta name="twitter:card" content="summary_large_image">
  <script type="application/ld+json">{json.dumps(schema, indent=2)}</script>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link href="https://fonts.googleapis.com/css2?family=Berkshire+Swash&family=Syne:wght@600;700;800&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
  <style>
    :root{{--bg:#0D0D14;--surface:#13131f;--primary:#B3FF00;--secondary:#7C3AED;--accent:#00F5FF;--text:#E8E8F0;--muted:#8888A8;--border:rgba(255,255,255,.08)}}
    *,*::before,*::after{{box-sizing:border-box;margin:0;padding:0}}
    html{{scroll-behavior:smooth}}
    body{{background:var(--bg);color:var(--text);font-family:'Inter',sans-serif;line-height:1.6;overflow-x:hidden}}
    a{{color:inherit;text-decoration:none}}
    img{{max-width:100%}}
    /* NAV */
    nav{{position:sticky;top:0;z-index:900;background:rgba(13,13,20,.92);backdrop-filter:blur(12px);border-bottom:1px solid var(--border)}}
    .nav-inner{{max-width:1180px;margin:0 auto;padding:0 24px;height:68px;display:flex;align-items:center;justify-content:space-between}}
    .nav-logo{{font-family:'Berkshire Swash',serif;font-size:1.45rem;background:linear-gradient(135deg,var(--primary),var(--accent));-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text}}
    .nav-links{{display:flex;gap:32px;list-style:none}}
    .nav-links a{{font-size:.9rem;font-weight:500;color:var(--muted);transition:color .2s}}
    .nav-links a:hover,.nav-links a.active{{color:#fff}}
    .nav-cta .btn-lime{{background:var(--primary);color:#000;font-weight:700;font-size:.85rem;padding:10px 22px;border-radius:8px;transition:opacity .2s}}
    .nav-cta .btn-lime:hover{{opacity:.85}}
    /* HERO */
    .hero{{padding:100px 24px 80px;text-align:center;background:radial-gradient(ellipse 80% 50% at 50% 0%,rgba(124,58,237,.18) 0%,transparent 70%)}}
    .hero-inner{{max-width:800px;margin:0 auto}}
    .breadcrumb{{font-size:.8rem;color:var(--muted);margin-bottom:24px}}
    .breadcrumb a{{color:var(--muted)}} .breadcrumb a:hover{{color:#fff}}
    .badge{{display:inline-block;background:rgba(179,255,0,.12);color:var(--primary);border:1px solid rgba(179,255,0,.3);padding:6px 16px;border-radius:999px;font-size:.8rem;font-weight:600;margin-bottom:24px;letter-spacing:.04em;text-transform:uppercase}}
    h1{{font-family:'Syne',sans-serif;font-size:clamp(2rem,5vw,3.2rem);font-weight:800;line-height:1.15;margin-bottom:24px}}
    .hl-lime{{color:var(--primary)}}
    .lead{{font-size:1.1rem;color:var(--muted);max-width:640px;margin:0 auto 40px}}
    .hero-ctas{{display:flex;gap:16px;justify-content:center;flex-wrap:wrap}}
    .btn-primary{{background:var(--primary);color:#000;font-weight:700;padding:14px 32px;border-radius:10px;font-size:1rem;transition:opacity .2s}}
    .btn-primary:hover{{opacity:.85}}
    .btn-outline{{border:1px solid var(--border);color:var(--text);padding:14px 32px;border-radius:10px;font-size:1rem;transition:border-color .2s}}
    .btn-outline:hover{{border-color:var(--primary)}}
    /* STATS */
    .stats{{background:var(--surface);border-top:1px solid var(--border);border-bottom:1px solid var(--border);padding:48px 24px}}
    .stats-inner{{max-width:900px;margin:0 auto;display:grid;grid-template-columns:repeat(3,1fr);gap:32px;text-align:center}}
    .stat-num{{font-family:'Syne',sans-serif;font-size:2.4rem;font-weight:800;color:var(--primary)}}
    .stat-lbl{{font-size:.85rem;color:var(--muted);margin-top:6px}}
    /* WHY */
    .why{{padding:96px 24px}}
    .why-inner{{max-width:1100px;margin:0 auto;display:grid;grid-template-columns:1fr 1fr;gap:64px;align-items:start}}
    .section-label{{font-size:.75rem;font-weight:700;color:var(--primary);letter-spacing:.1em;text-transform:uppercase;margin-bottom:12px}}
    .section-title{{font-family:'Syne',sans-serif;font-size:clamp(1.6rem,3vw,2.2rem);font-weight:800;line-height:1.2;margin-bottom:24px}}
    .why-text p{{color:var(--muted);margin-bottom:16px;line-height:1.75}}
    .why-card{{background:var(--surface);border:1px solid var(--border);border-radius:16px;padding:32px}}
    .why-card h3{{font-family:'Syne',sans-serif;font-size:1rem;font-weight:700;margin-bottom:16px;color:var(--primary)}}
    .why-card ul{{list-style:none;display:flex;flex-direction:column;gap:10px}}
    .why-card li{{font-size:.9rem;color:var(--muted);padding-left:20px;position:relative}}
    .why-card li::before{{content:'✓';position:absolute;left:0;color:var(--primary);font-weight:700}}
    /* SERVICES */
    .services{{padding:96px 24px;background:var(--surface)}}
    .services-inner{{max-width:1100px;margin:0 auto}}
    .section-header{{text-align:center;margin-bottom:56px}}
    .svc-grid{{display:grid;grid-template-columns:repeat(3,1fr);gap:24px}}
    .svc-card{{background:var(--bg);border:1px solid var(--border);border-radius:16px;padding:28px;transition:border-color .2s}}
    .svc-card:hover{{border-color:var(--primary)}}
    .svc-icon{{font-size:2rem;margin-bottom:16px}}
    .svc-card h3{{font-family:'Syne',sans-serif;font-size:1rem;font-weight:700;margin-bottom:10px}}
    .svc-card p{{font-size:.88rem;color:var(--muted);line-height:1.65}}
    /* PROCESS */
    .process{{padding:96px 24px}}
    .process-inner{{max-width:1100px;margin:0 auto}}
    .step-grid{{display:grid;grid-template-columns:repeat(4,1fr);gap:24px;margin-top:56px}}
    .step-card{{background:var(--surface);border:1px solid var(--border);border-radius:16px;padding:28px}}
    .step-num{{font-family:'Syne',sans-serif;font-size:2rem;font-weight:800;color:var(--primary);opacity:.4;line-height:1}}
    .step-icon{{font-size:1.6rem;margin:12px 0}}
    .step-card h3{{font-family:'Syne',sans-serif;font-size:.95rem;font-weight:700;margin-bottom:8px}}
    .step-card p{{font-size:.85rem;color:var(--muted);line-height:1.65}}
    /* PRICING */
    .pricing{{padding:96px 24px;background:var(--surface)}}
    .pricing-inner{{max-width:520px;margin:0 auto;text-align:center}}
    .pricing-box{{background:var(--bg);border:1px solid var(--border);border-radius:20px;padding:48px 40px;margin-top:40px}}
    .price-from{{font-size:.85rem;color:var(--muted);margin-bottom:8px}}
    .price-val{{font-family:'Syne',sans-serif;font-size:3rem;font-weight:800;color:var(--primary)}}
    .price-note{{font-size:.85rem;color:var(--muted);margin-top:8px;margin-bottom:32px}}
    /* FAQ */
    .faq{{padding:96px 24px}}
    .faq-inner{{max-width:760px;margin:0 auto}}
    .faq-list{{margin-top:48px;display:flex;flex-direction:column;gap:12px}}
    .faq-item{{background:var(--surface);border:1px solid var(--border);border-radius:12px;overflow:hidden}}
    .faq-q{{width:100%;background:none;border:none;color:var(--text);font-family:'Inter',sans-serif;font-size:.95rem;font-weight:600;padding:20px 24px;text-align:left;cursor:pointer;display:flex;justify-content:space-between;align-items:center;gap:16px}}
    .faq-chevron{{font-size:1.4rem;color:var(--primary);transition:transform .3s;flex-shrink:0}}
    .faq-q[aria-expanded="true"] .faq-chevron{{transform:rotate(90deg)}}
    .faq-a{{max-height:0;overflow:hidden;transition:max-height .35s ease}}
    .faq-a p{{padding:0 24px 20px;color:var(--muted);font-size:.9rem;line-height:1.7}}
    /* CTA BAND */
    .cta-band{{padding:96px 24px;background:radial-gradient(ellipse 70% 60% at 50% 50%,rgba(124,58,237,.25) 0%,transparent 70%);text-align:center}}
    .cta-band h2{{font-family:'Syne',sans-serif;font-size:clamp(1.6rem,3vw,2.4rem);font-weight:800;margin-bottom:16px}}
    .cta-band p{{color:var(--muted);max-width:560px;margin:0 auto 40px}}
    /* FOOTER */
    footer{{background:var(--surface);border-top:1px solid var(--border);padding:64px 24px 32px}}
    .footer-inner{{max-width:1180px;margin:0 auto}}
    .footer-top{{display:grid;grid-template-columns:1.4fr 1fr 1fr 1fr;gap:48px;margin-bottom:48px}}
    .footer-brand p{{color:var(--muted);font-size:.88rem;margin-top:12px;line-height:1.6;max-width:260px}}
    .footer-col h4{{font-size:.78rem;font-weight:700;color:var(--muted);letter-spacing:.08em;text-transform:uppercase;margin-bottom:16px}}
    .footer-col ul{{list-style:none;display:flex;flex-direction:column;gap:10px}}
    .footer-col li a{{font-size:.88rem;color:var(--muted);transition:color .2s}}
    .footer-col li a:hover{{color:#fff}}
    .footer-bottom{{border-top:1px solid var(--border);padding-top:24px;display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:12px}}
    .footer-bottom p{{font-size:.8rem;color:var(--muted)}}
    .footer-bottom-links{{display:flex;gap:24px}}
    .footer-bottom-links a{{font-size:.8rem;color:var(--muted);transition:color .2s}}
    .footer-bottom-links a:hover{{color:#fff}}
    /* SOCIAL */
    .social-links{{display:flex;gap:12px;margin-top:16px}}
    .social-links a{{width:34px;height:34px;border:1px solid var(--border);border-radius:8px;display:flex;align-items:center;justify-content:center;transition:border-color .2s;flex-shrink:0}}
    .social-links a:hover{{border-color:var(--primary)}}
    .social-links svg{{width:16px;height:16px;fill:var(--muted)}}
    /* RESPONSIVE */
    @media(max-width:900px){{
      .why-inner{{grid-template-columns:1fr}}
      .svc-grid{{grid-template-columns:repeat(2,1fr)}}
      .step-grid{{grid-template-columns:repeat(2,1fr)}}
      .footer-top{{grid-template-columns:1fr 1fr}}
    }}
    @media(max-width:600px){{
      .stats-inner{{grid-template-columns:1fr}}
      .svc-grid{{grid-template-columns:1fr}}
      .step-grid{{grid-template-columns:1fr}}
      .nav-links{{display:none}}
      .footer-top{{grid-template-columns:1fr}}
    }}
  </style>
</head>
<body>

<!-- NAV -->
<nav>
  <div class="nav-inner">
    <a href="../index.html" class="nav-logo">Lumo AI</a>
    <ul class="nav-links">
      <li><a href="../index.html">Home</a></li>
      <li><a href="../services.html" class="active">Services</a></li>
      <li><a href="../industries/seo-for-lawyers/index.html">Industries</a></li>
      <li><a href="../about.html">About</a></li>
      <li><a href="../pricing.html">Pricing</a></li>
    </ul>
    <div class="nav-cta"><a href="../contact.html" class="btn-lime">Get Started</a></div>
  </div>
</nav>

<!-- HERO -->
<section class="hero">
  <div class="hero-inner">
    <nav class="breadcrumb" aria-label="Breadcrumb">
      <a href="../index.html">Home</a> › <a href="../services.html">Services</a> › {d["schema_service_name"]}
    </nav>
    <div class="badge">{d["badge"]}</div>
    <h1>{d["h1_html"]}</h1>
    <p class="lead">{d["lead"]}</p>
    <div class="hero-ctas">
      <a href="../contact.html" class="btn-primary">Get a Free Strategy Call</a>
      <a href="../services.html" class="btn-outline">View All Services</a>
    </div>
  </div>
</section>

<!-- STATS -->
<section class="stats">
  <div class="stats-inner">
    <div><div class="stat-num">{d["stat1_num"]}</div><div class="stat-lbl">{d["stat1_lbl"]}</div></div>
    <div><div class="stat-num">{d["stat2_num"]}</div><div class="stat-lbl">{d["stat2_lbl"]}</div></div>
    <div><div class="stat-num">{d["stat3_num"]}</div><div class="stat-lbl">{d["stat3_lbl"]}</div></div>
  </div>
</section>

<!-- WHY -->
<section class="why">
  <div class="why-inner">
    <div class="why-text">
      <div class="section-label">Why It Matters</div>
      <h2 class="section-title">{d["why_h2"]}</h2>
      <p>{d["why_p1"]}</p>
      <p>{d["why_p2"]}</p>
      <p>{d["why_p3"]}</p>
    </div>
    <div class="why-card">
      <h3>What You Get With Lumo</h3>
      <ul>
        <li>Dedicated specialist team — not a generalist account manager</li>
        <li>Full strategy, execution, and reporting included</li>
        <li>AI-powered insights layer on every campaign</li>
        <li>Transparent monthly performance reports</li>
        <li>GEO optimisation built into every strategy</li>
        <li>No lock-in contracts — performance keeps you here</li>
      </ul>
    </div>
  </div>
</section>

<!-- SERVICES -->
<section class="services">
  <div class="services-inner">
    <div class="section-header">
      <div class="section-label">What We Do</div>
      <h2 class="section-title">{d["services_h2"]}</h2>
    </div>
    <div class="svc-grid">
{services_html}
    </div>
  </div>
</section>

<!-- PROCESS -->
<section class="process">
  <div class="process-inner">
    <div class="section-header">
      <div class="section-label">How It Works</div>
      <h2 class="section-title">Our Proven 4-Step Process</h2>
    </div>
    <div class="step-grid">
{process_html}
    </div>
  </div>
</section>

<!-- PRICING -->
<section class="pricing">
  <div class="pricing-inner">
    <div class="section-label" style="text-align:center">Investment</div>
    <h2 class="section-title" style="text-align:center">Simple, Transparent Pricing</h2>
    <div class="pricing-box">
      <div class="price-from">Starting from</div>
      <div class="price-val">{d["price_from"]}</div>
      <div class="price-note">{d["price_note"]}</div>
      <a href="../contact.html" class="btn-primary">Get a Custom Quote</a>
    </div>
  </div>
</section>

<!-- FAQ -->
<section class="faq">
  <div class="faq-inner">
    <div class="section-label" style="text-align:center">FAQ</div>
    <h2 class="section-title" style="text-align:center">Frequently Asked Questions</h2>
    <div class="faq-list">
{faq_html}
    </div>
  </div>
</section>

<!-- CTA BAND -->
<section class="cta-band">
  <h2>{d["cta_h2"]}</h2>
  <p>{d["cta_sub"]}</p>
  <a href="../contact.html" class="btn-primary">Book a Free Strategy Call</a>
</section>

<!-- FOOTER -->
<footer>
  <div class="footer-inner">
    <div class="footer-top">
      <div class="footer-brand">
        <a href="../index.html" class="nav-logo" style="font-family:'Berkshire Swash',serif;font-size:1.3rem;background:linear-gradient(135deg,#B3FF00,#00F5FF);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text">Lumo AI</a>
        <p>AI-powered marketing agency based in Austin, TX. We help US businesses grow with SEO, paid media, AI automation, and content marketing.</p>
        <div class="social-links">
          <a href="https://www.linkedin.com/company/lumo-ai-agency" aria-label="LinkedIn"><svg viewBox="0 0 24 24"><path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433a2.062 2.062 0 01-2.063-2.065 2.064 2.064 0 112.063 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/></svg></a>
          <a href="https://twitter.com/lumoaiagency" aria-label="Twitter/X"><svg viewBox="0 0 24 24"><path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-4.714-6.231-5.401 6.231H2.744l7.737-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"/></svg></a>
          <a href="https://www.facebook.com/lumoaiagency" aria-label="Facebook"><svg viewBox="0 0 24 24"><path d="M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.47h3.047V9.43c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.47h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z"/></svg></a>
        </div>
      </div>
      <div class="footer-col">
        <h4>Services</h4>
        <ul>
          <li><a href="../services/seo.html">SEO</a></li>
          <li><a href="../services/geo.html">GEO</a></li>
          <li><a href="../services/google-ads.html">Google Ads</a></li>
          <li><a href="../services/meta-ads.html">Meta Ads</a></li>
          <li><a href="../services/technical-seo.html">Technical SEO</a></li>
          <li><a href="../services/local-seo.html">Local SEO</a></li>
          <li><a href="../services/link-building.html">Link Building</a></li>
          <li><a href="../services/reputation-management.html">Reputation Mgmt</a></li>
          <li><a href="../services/marketing-automation.html">Marketing Automation</a></li>
          <li><a href="../services/sms-marketing.html">SMS Marketing</a></li>
          <li><a href="../services.html">All Services →</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h4>Industries</h4>
        <ul>
          <li><a href="../industries/seo-for-lawyers/index.html">Legal</a></li>
          <li><a href="../industries/seo-for-dentists/index.html">Dental</a></li>
          <li><a href="../industries/healthcare-seo/index.html">Healthcare</a></li>
          <li><a href="../industries/saas-marketing/index.html">SaaS</a></li>
          <li><a href="../industries/ecommerce-marketing/index.html">E-commerce</a></li>
          <li><a href="../industries/home-services-seo/index.html">Home Services</a></li>
          <li><a href="../industries/financial-services-marketing/index.html">Finance</a></li>
          <li><a href="../industries/restaurant-marketing/index.html">Restaurant</a></li>
          <li><a href="../industries/fitness-gym-marketing/index.html">Fitness</a></li>
          <li><a href="../industries/construction-marketing/index.html">Construction</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h4>Compare</h4>
        <ul>
          <li><a href="../compare/lumo-vs-webfx/index.html">Lumo vs WebFX</a></li>
          <li><a href="../compare/lumo-vs-thrive-agency/index.html">Lumo vs Thrive</a></li>
          <li><a href="../compare/lumo-vs-np-digital/index.html">Lumo vs NP Digital</a></li>
          <li><a href="../compare/lumo-vs-ignite-digital/index.html">Lumo vs Ignite</a></li>
          <li><a href="../compare/lumo-vs-disruptive-advertising/index.html">Lumo vs Disruptive</a></li>
          <li><a href="../compare/lumo-vs-smartsites/index.html">Lumo vs SmartSites</a></li>
        </ul>
        <h4 style="margin-top:24px">Company</h4>
        <ul>
          <li><a href="../about.html">About</a></li>
          <li><a href="../pricing.html">Pricing</a></li>
          <li><a href="../contact.html">Contact</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <p>© 2026 Lumo AI Agency LLC. All rights reserved.</p>
      <div class="footer-bottom-links">
        <a href="../privacy-policy.html">Privacy Policy</a>
        <a href="../terms-of-service.html">Terms of Service</a>
        <a href="../cookie-policy.html">Cookie Policy</a>
      </div>
    </div>
  </div>
</footer>

<script>
  document.querySelectorAll('.faq-q').forEach(btn => {{
    btn.addEventListener('click', () => {{
      const expanded = btn.getAttribute('aria-expanded') === 'true';
      document.querySelectorAll('.faq-q').forEach(b => {{
        b.setAttribute('aria-expanded','false');
        b.nextElementSibling.style.maxHeight = null;
      }});
      if (!expanded) {{
        btn.setAttribute('aria-expanded','true');
        btn.nextElementSibling.style.maxHeight = btn.nextElementSibling.scrollHeight + 'px';
      }}
    }});
  }});
</script>
</body>
</html>"""


def main():
    for slug, data in SERVICES.items():
        html = build_page(slug, data)
        path = os.path.join(BASE, f"{slug}.html")
        with open(path, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"Created: services/{slug}.html ({len(html):,} chars)")
    print(f"\nDone. {len(SERVICES)} pages created.")

if __name__ == "__main__":
    main()
