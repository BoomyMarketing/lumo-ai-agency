#!/usr/bin/env python3
"""Generate 6 comparison pages under /compare/{slug}/index.html."""
import os, json

BASE = os.path.dirname(os.path.abspath(__file__))

# ---------------------------------------------------------------------------
# COMPARISON PAGE DATA
# ---------------------------------------------------------------------------
COMPARISONS = {
    "lumo-vs-webfx": {
        "slug":        "lumo-vs-webfx",
        "competitor":  "WebFX",
        "title_tag":   "Lumo AI Agency vs WebFX — Which Agency Is Right for You? (2026)",
        "meta_desc":   "Lumo AI Agency vs WebFX: honest side-by-side comparison of services, pricing, AI capabilities, and who each agency is best for. Make the right choice for your business.",
        "og_title":    "Lumo AI Agency vs WebFX (2026 Comparison)",
        "h1_part1":    "Lumo AI Agency",
        "h1_part2":    "WebFX",
        "summary":     "WebFX is a large traditional digital marketing agency with a broad service menu and a well-established process-driven approach. Lumo AI Agency is purpose-built around AI — offering GEO, Voice AI, custom AI automations, and LLM development alongside performance marketing. If you need a proven large-agency operation, WebFX is a solid choice. If you want AI-native marketing that goes beyond standard SEO and ads, Lumo is the better fit.",
        "table_rows": [
            ("AI-First Approach",           "✅ Core to every service",         "❌ Traditional agency model"),
            ("GEO / AI Search Optimisation", "✅ Dedicated service + strategy",  "❌ Not offered"),
            ("Voice AI Agents",              "✅ Custom phone agents 24/7",       "❌ Not offered"),
            ("Custom AI Automations",        "✅ n8n, Make, Python pipelines",    "❌ Not offered"),
            ("LLM / AI Development",         "✅ Custom AI apps & RAG pipelines", "❌ Not offered"),
            ("SEO Services",                 "✅ AI-powered + technical",         "✅ Full-service SEO"),
            ("Google & Meta Ads",            "✅ AI bidding + CRO",               "✅ Full paid media"),
            ("LinkedIn Ads",                 "✅ B2B pipeline focus",             "✅ Available"),
            ("Transparent Pricing",          "✅ Published on website",           "⚠️  Quote-based"),
            ("Contract Lock-in",             "✅ No long-term contracts",         "⚠️  Often 12-month"),
            ("Team Size",                    "⚠️  Boutique, dedicated PMs",       "✅ 500+ employees"),
            ("Industry Verticals",           "✅ 10 specialist pages",            "✅ Many verticals"),
        ],
        "choose_lumo": [
            "You want AI-native services — GEO, Voice AI, automations — not just traditional digital marketing.",
            "You need custom AI development (LLM apps, RAG systems, AI SDR) alongside marketing.",
            "You prefer working with a boutique, hands-on team rather than a large agency production line.",
            "You want month-to-month flexibility without being locked into a 12-month contract.",
            "You're a startup or scale-up that needs to move fast and integrate AI across your business.",
        ],
        "choose_competitor": [
            "You need a very large internal team managing dozens of channels simultaneously.",
            "You want an agency with a 20+ year track record and thousands of published case studies.",
            "Your business requires highly specialised enterprise-level reporting and client portal features.",
            "You prefer a highly process-driven, structured agency model with formal SLAs.",
        ],
        "faqs": [
            ("Is Lumo AI Agency comparable in size to WebFX?", "No — and that's a feature, not a bug. Lumo is a boutique AI-first agency where senior strategists manage your account directly. WebFX has 500+ employees and a more tiered model. Clients who choose Lumo typically value direct access and AI specialisation over agency scale."),
            ("Does WebFX offer AI marketing services like Lumo?", "WebFX uses technology tools (MarketingCloudFX) in their process, but does not offer GEO optimisation, Voice AI agents, custom AI automations, or LLM development. These AI-native services are core Lumo differentiators that traditional agencies, including WebFX, have not yet built out."),
            ("How do Lumo's prices compare to WebFX?", "Both agencies are premium-tier. Lumo publishes transparent starting prices on its pricing page — WebFX typically requires a discovery call for custom quotes. For comparable service scopes, pricing is broadly similar, with Lumo often offering more AI-specific deliverables within equivalent engagements."),
            ("Can Lumo handle the same scale as WebFX?", "Lumo works with startups through to multi-million dollar businesses. For clients needing hundreds of simultaneous campaign assets across 50+ locations managed by large teams, WebFX's scale may be advantageous. Lumo compensates for team size through AI-driven efficiency — automating tasks that traditionally require large teams."),
        ],
        "cta_sub": "Not sure which agency is the right fit? Book a free 30-minute strategy call with Lumo — no pressure, just an honest conversation about whether we're the right partner for your specific goals.",
    },
    "lumo-vs-thrive-agency": {
        "slug":        "lumo-vs-thrive-agency",
        "competitor":  "Thrive Agency",
        "title_tag":   "Lumo AI Agency vs Thrive Agency — Which Is Right for You? (2026)",
        "meta_desc":   "Lumo AI Agency vs Thrive Agency: honest comparison of AI capabilities, services, pricing, and who each agency serves best. Make an informed decision for your marketing investment.",
        "og_title":    "Lumo AI Agency vs Thrive Agency (2026 Comparison)",
        "h1_part1":    "Lumo AI Agency",
        "h1_part2":    "Thrive Agency",
        "summary":     "Thrive Agency is a well-established US full-service digital marketing agency known for multi-channel campaign management at scale. Lumo AI Agency is purpose-built around AI — offering GEO, Voice AI, AI automations, and LLM development that traditional agencies like Thrive simply don't have. If you need a reliable full-service digital agency with a proven track record, Thrive is worth considering. If AI-powered marketing is a priority — or if you need services beyond standard SEO and ads — Lumo is the stronger choice.",
        "table_rows": [
            ("AI-First Approach",            "✅ Every service built on AI",      "❌ Traditional digital agency"),
            ("GEO / AI Search Optimisation", "✅ Dedicated GEO service",          "❌ Not offered"),
            ("Voice AI Agents",              "✅ Custom AI phone agents",          "❌ Not offered"),
            ("Custom AI Automations",        "✅ Workflow automation builds",      "❌ Not offered"),
            ("LLM / AI App Development",     "✅ Custom AI products & RAG",        "❌ Not offered"),
            ("SEO Services",                 "✅ AI-enhanced technical SEO",       "✅ Full-service SEO"),
            ("PPC / Google Ads",             "✅ AI bidding optimisation",         "✅ Full PPC management"),
            ("Social Media Management",      "✅ AI-assisted content",             "✅ Multi-platform social"),
            ("Web Design & Development",     "✅ Conversion-focused builds",       "✅ Web design services"),
            ("Transparent Pricing",          "✅ Published on site",               "⚠️  Quote-based"),
            ("Contract Flexibility",         "✅ Month-to-month available",        "⚠️  Typically 6-12 months"),
            ("Dedicated Account Manager",    "✅ Senior strategist direct",        "✅ Account manager assigned"),
        ],
        "choose_lumo": [
            "You want AI-powered services — GEO, Voice AI, automations — as part of your marketing strategy.",
            "You need your marketing agency to also build AI tools, LLM apps, or automation systems for your business.",
            "You value direct access to senior strategists rather than being managed by junior account teams.",
            "You prefer month-to-month flexibility rather than committing to long-term contracts upfront.",
            "You're a startup, SaaS company, or growth-stage business that needs an agile, AI-native partner.",
        ],
        "choose_competitor": [
            "You need a very large multi-channel team managing high-volume campaigns across many platforms.",
            "You want an agency with a long-standing US reputation and large library of published client results.",
            "Your business requires specific enterprise reporting tools or integration with large marketing tech stacks.",
            "You are primarily focused on standard SEO and social media and don't need AI-specific capabilities.",
        ],
        "faqs": [
            ("What makes Lumo different from Thrive Agency?", "The fundamental difference is that Lumo is built from the ground up around AI — GEO optimisation, Voice AI agents, custom automations, and LLM development are core services, not add-ons. Thrive is a traditional full-service agency that has grown very large. Clients choosing Lumo prioritise AI-native capabilities and boutique-level attention over agency scale."),
            ("Does Thrive Agency offer AI marketing services?", "Thrive uses digital marketing tools in their workflow, but does not offer GEO (Generative Engine Optimisation), Voice AI agents, custom n8n/Make automation builds, or LLM app development. These are core Lumo services with no equivalent at traditional agencies like Thrive."),
            ("Is Thrive Agency more affordable than Lumo?", "Both agencies are positioned in the mid-to-premium tier. Lumo's pricing is published transparently on its website. Thrive typically provides custom quotes. For comparable service scopes, the investment levels are broadly similar — the key difference is what you get: AI-specific capabilities at Lumo vs. traditional digital services at Thrive."),
            ("Can Lumo handle large enterprise accounts like Thrive?", "Lumo works with startups, SMBs, and established businesses across the US. For accounts requiring 50+ simultaneous large-scale campaigns managed by hundreds of staff, Thrive's scale has advantages. Lumo's strength is AI-driven efficiency — delivering outsized results for clients who want AI integration, not just manpower."),
        ],
        "cta_sub": "Evaluating multiple agencies? Book a free strategy call with Lumo — we'll be upfront about whether we're the right fit and what results you can realistically expect from an AI-first approach.",
    },
    "lumo-vs-np-digital": {
        "slug":        "lumo-vs-np-digital",
        "competitor":  "NP Digital",
        "title_tag":   "Lumo AI Agency vs NP Digital — Which Agency Is Right for You? (2026)",
        "meta_desc":   "Lumo AI Agency vs NP Digital: side-by-side comparison of SEO, content, AI capabilities, pricing model, and who each agency is best suited for in 2026.",
        "og_title":    "Lumo AI Agency vs NP Digital (2026 Comparison)",
        "h1_part1":    "Lumo AI Agency",
        "h1_part2":    "NP Digital",
        "summary":     "NP Digital (Neil Patel's agency) is a globally known content-and-SEO focused agency with significant brand recognition and a large content-marketing footprint. Lumo AI Agency is an AI-first growth agency that combines performance marketing with AI-native services — GEO, Voice AI, automations, and custom LLM development — that NP Digital does not offer. If you need content-heavy SEO at global scale, NP Digital is compelling. If you want an AI-powered marketing partner that builds AI into your operations, not just your content, Lumo is the better choice.",
        "table_rows": [
            ("AI-First Approach",            "✅ AI-native across all services",  "⚠️  Content-first, AI-assisted"),
            ("GEO / AI Search Optimisation", "✅ Dedicated GEO service",          "❌ Not a core offering"),
            ("Voice AI Agents",              "✅ Custom AI phone agents",          "❌ Not offered"),
            ("Custom AI Automations",        "✅ Workflow automation builds",      "❌ Not offered"),
            ("LLM / AI App Development",     "✅ Custom AI products & RAG",        "❌ Not offered"),
            ("SEO & Content Marketing",      "✅ AI-powered + GEO",               "✅ Core strength, high volume"),
            ("Paid Ads Management",          "✅ Google, Meta, LinkedIn, TikTok", "✅ Full paid media"),
            ("CRO Services",                 "✅ A/B testing, funnel analysis",    "✅ CRO services available"),
            ("Brand Name / Awareness",       "⚠️  Boutique, growing brand",       "✅ Neil Patel brand recognition"),
            ("Transparent Pricing",          "✅ Published on site",               "⚠️  Enterprise quote-based"),
            ("Contract Flexibility",         "✅ Month-to-month available",        "⚠️  Typically annual"),
            ("Dedicated Senior Contact",     "✅ Direct senior strategist",        "⚠️  Large team, tiered access"),
        ],
        "choose_lumo": [
            "You want an AI-native partner that builds GEO, Voice AI, automations, and AI tools into your growth strategy.",
            "You need AI development capabilities (custom LLMs, RAG pipelines, AI SDRs) alongside marketing.",
            "You want a hands-on boutique agency relationship with direct access to senior strategists.",
            "You prefer flexible month-to-month engagements without annual commitment requirements.",
            "You're scaling fast and need agility — not a process-heavy large-agency model.",
        ],
        "choose_competitor": [
            "You need very high-volume content production (50+ SEO articles per month) at global scale.",
            "Brand association with the Neil Patel name is valuable for your business positioning.",
            "You primarily need content-led SEO and are not currently interested in AI-specific services.",
            "You need a large agency with offices across multiple continents managing international campaigns.",
        ],
        "faqs": [
            ("How is Lumo different from NP Digital's SEO approach?", "NP Digital is built around Neil Patel's content marketing methodology — high-volume, data-informed content production at scale. Lumo's SEO integrates AI-powered keyword research, GEO (Generative Engine Optimisation for AI search), and technical SEO engineering. Lumo also offers services NP Digital doesn't: Voice AI, custom automations, and LLM development."),
            ("Does NP Digital offer GEO or AI marketing services?", "NP Digital produces AI-assisted content and uses data tools in their SEO process, but does not offer Generative Engine Optimisation (GEO), Voice AI agents, custom automation builds, or LLM application development. These AI-native services are core Lumo differentiators."),
            ("Is NP Digital more suitable for large enterprises than Lumo?", "NP Digital's scale suits large enterprises needing global content operations. Lumo works with startups, SMBs, and growth-stage businesses that want AI-integrated marketing and operations — not just content at scale. Lumo's boutique model delivers higher-touch strategy and AI-specific outcomes that enterprise content factories can't replicate."),
            ("How does Lumo's pricing compare to NP Digital?", "NP Digital typically operates at enterprise pricing with annual commitments for meaningful engagements. Lumo publishes transparent pricing and offers month-to-month flexibility. For growth-stage businesses, Lumo typically provides more accessible pricing with a wider range of AI-specific services included."),
        ],
        "cta_sub": "Comparing agencies for your 2026 marketing strategy? Book a free Lumo strategy call — we'll show you exactly what an AI-first approach delivers vs. traditional content-led SEO.",
    },
    "lumo-vs-ignite-digital": {
        "slug":        "lumo-vs-ignite-digital",
        "competitor":  "Ignite Digital",
        "title_tag":   "Lumo AI Agency vs Ignite Digital — Which Is Right for You? (2026)",
        "meta_desc":   "Lumo AI Agency vs Ignite Digital: honest 2026 comparison of services, AI capabilities, pricing, and who each agency is best suited for. Make the right choice for your growth goals.",
        "og_title":    "Lumo AI Agency vs Ignite Digital (2026 Comparison)",
        "h1_part1":    "Lumo AI Agency",
        "h1_part2":    "Ignite Digital",
        "summary":     "Ignite Digital is a growing North American digital marketing agency focused primarily on SEO and paid media. Lumo AI Agency goes significantly further — combining AI-native services (GEO, Voice AI, custom automations, LLM development) with performance marketing. For businesses wanting strong traditional digital marketing, Ignite Digital is a reasonable choice. For businesses that want AI woven into their marketing and operations from the ground up, Lumo is the clear winner.",
        "table_rows": [
            ("AI-First Approach",            "✅ Core to every service",          "❌ Traditional digital model"),
            ("GEO / AI Search Optimisation", "✅ Dedicated GEO service",          "❌ Not offered"),
            ("Voice AI Agents",              "✅ Custom AI phone agents 24/7",     "❌ Not offered"),
            ("Custom AI Automations",        "✅ n8n, Make, Python pipelines",     "❌ Not offered"),
            ("LLM / AI App Development",     "✅ Custom AI & RAG systems",         "❌ Not offered"),
            ("SEO Services",                 "✅ AI-enhanced + GEO",               "✅ SEO management"),
            ("Google Ads",                   "✅ AI bidding + full funnel",         "✅ PPC management"),
            ("Meta Ads",                     "✅ Creative testing framework",       "✅ Social ads"),
            ("LinkedIn Ads",                 "✅ B2B pipeline focus",               "✅ LinkedIn ads"),
            ("Transparent Pricing",          "✅ Published on website",            "⚠️  Quote-based"),
            ("Contract Flexibility",         "✅ Month-to-month available",        "⚠️  Annual contracts common"),
            ("E-commerce SEO",               "✅ Shopify/WooCommerce specialist",  "⚠️  General SEO only"),
        ],
        "choose_lumo": [
            "You want an agency that treats AI as a core capability — not a buzzword added to a traditional pitch.",
            "You need GEO optimisation to appear in ChatGPT, Perplexity, and Google AI Overviews for your category.",
            "You want Voice AI agents, custom automations, or AI development as part of your growth stack.",
            "You're a SaaS company, e-commerce brand, or B2B business that needs AI across marketing and operations.",
            "You want direct access to senior strategists and month-to-month engagement flexibility.",
        ],
        "choose_competitor": [
            "You need a straightforward SEO and paid media management relationship without AI-specific deliverables.",
            "You have a large Canadian or US operation that fits Ignite Digital's core focus areas.",
            "Budget is the primary constraint and you need baseline digital marketing coverage.",
            "You prefer an agency with a more traditional account management model.",
        ],
        "faqs": [
            ("What does Lumo offer that Ignite Digital doesn't?", "The most significant differences are Lumo's AI-native services: GEO (Generative Engine Optimisation), Voice AI agents, custom workflow automations, and LLM/AI app development. These are core Lumo services with no equivalent at Ignite Digital. Lumo also brings more advanced e-commerce SEO specialisation and a published pricing model."),
            ("Is Ignite Digital better for Canadian businesses?", "Ignite Digital has a strong Canadian presence and may suit Canadian businesses prioritising local agency relationships. Lumo is a US-based agency (Austin, TX) serving businesses across the entire US market, with specific expertise in US search landscapes and AI-native growth strategies."),
            ("How does Lumo's SEO compare to Ignite Digital's?", "Both agencies offer technical SEO and content-led strategies. Lumo's differentiation is AI-powered keyword clustering, GEO optimisation for AI search engines (ChatGPT, Perplexity, Google AI Overviews), and deeper e-commerce SEO specialisation. Lumo also integrates SEO with AI automation to accelerate content production and link building at scale."),
            ("Is Lumo more expensive than Ignite Digital?", "Lumo publishes transparent pricing starting points on its website — Ignite Digital typically requires a custom quote. For businesses comparing similar service scopes, Lumo often provides more AI-specific deliverables at comparable investment levels. Book a free Lumo audit for a direct comparison."),
        ],
        "cta_sub": "Comparing agencies? Book a free Lumo strategy call — no pitch, just an honest conversation about whether our AI-first model is the right fit for your specific goals and budget.",
    },
    "lumo-vs-disruptive-advertising": {
        "slug":        "lumo-vs-disruptive-advertising",
        "competitor":  "Disruptive Advertising",
        "title_tag":   "Lumo AI Agency vs Disruptive Advertising — Which Is Right for You? (2026)",
        "meta_desc":   "Lumo AI Agency vs Disruptive Advertising: 2026 comparison of paid media, AI capabilities, services, and which agency fits your specific growth goals. Free audit available.",
        "og_title":    "Lumo AI Agency vs Disruptive Advertising (2026 Comparison)",
        "h1_part1":    "Lumo AI Agency",
        "h1_part2":    "Disruptive Advertising",
        "summary":     "Disruptive Advertising is a well-regarded US paid media agency specialising in Google Ads, Meta Ads, and paid search management. Lumo AI Agency covers paid media as one component of a broader AI-native growth stack — adding GEO, Voice AI, automations, and LLM development that Disruptive doesn't offer. If paid media is your exclusive focus and you want a large dedicated PPC team, Disruptive is a strong choice. If you need paid media integrated with AI-powered SEO, automations, and AI development, Lumo is the better partner.",
        "table_rows": [
            ("AI-First Approach",            "✅ AI across all services",          "⚠️  AI bidding tools in PPC"),
            ("GEO / AI Search Optimisation", "✅ Dedicated GEO service",           "❌ Not offered"),
            ("Voice AI Agents",              "✅ Custom AI phone agents",           "❌ Not offered"),
            ("Custom AI Automations",        "✅ Full automation builds",           "❌ Not offered"),
            ("LLM / AI Development",         "✅ Custom AI apps & pipelines",       "❌ Not offered"),
            ("Google Ads",                   "✅ AI bidding + full funnel",          "✅ Core strength"),
            ("Meta Ads",                     "✅ Creative testing framework",        "✅ Core strength"),
            ("LinkedIn Ads",                 "✅ B2B pipeline focus",                "✅ Managed"),
            ("TikTok Ads",                   "✅ UGC creative + targeting",          "✅ Managed"),
            ("SEO Services",                 "✅ AI-powered + GEO",                  "⚠️  Not a primary service"),
            ("CRO Services",                 "✅ A/B testing + funnel analysis",     "✅ CRO available"),
            ("Transparent Pricing",          "✅ Published on website",              "⚠️  Quote-based"),
        ],
        "choose_lumo": [
            "You want paid media integrated with AI-powered SEO, GEO, and automation — not standalone PPC management.",
            "You need AI-native services (Voice AI, automations, LLM development) alongside your paid media strategy.",
            "You want organic and paid channels managed cohesively by one partner rather than siloed agencies.",
            "You need e-commerce, SaaS, or B2B specialist knowledge across multiple channels — not just paid search.",
            "You value transparent pricing and month-to-month flexibility.",
        ],
        "choose_competitor": [
            "Your entire marketing budget is allocated to paid media and you want a dedicated PPC-specialist team.",
            "You already have strong SEO and only need help with Google and Meta Ads specifically.",
            "You prefer a paid media agency with a very large team exclusively focused on PPC optimisation.",
            "You want access to Disruptive's proprietary analytics dashboards and enterprise reporting tools.",
        ],
        "faqs": [
            ("Is Lumo a paid media agency or a full-service agency?", "Lumo is a full-service AI-powered growth agency — paid media is one of 19 services we offer. We manage Google Ads, Meta Ads, LinkedIn Ads, TikTok Ads, and YouTube Ads as part of integrated strategies that include SEO, GEO, and AI automation. Clients who want dedicated PPC-only management from a specialist team may prefer Disruptive's singular focus."),
            ("How does Lumo's Google Ads management compare to Disruptive Advertising?", "Both agencies use AI-powered bidding and conversion tracking. Lumo's differentiation is in cross-channel integration — we connect paid media performance data to SEO, CRO, and automation in ways that siloed PPC agencies can't. Lumo also optimises landing pages and conversion funnels alongside ad management, rather than treating paid media in isolation."),
            ("Does Disruptive Advertising offer GEO or AI services like Lumo?", "Disruptive Advertising uses AI tools within their PPC workflow (Smart Bidding, automated rules) but does not offer Generative Engine Optimisation (GEO), Voice AI agents, custom automation builds, or LLM application development. These AI-native capabilities are exclusive to Lumo in this comparison."),
            ("Can Lumo manage only paid media without the other services?", "Yes — Lumo can manage paid media as a standalone service. However, clients who also use Lumo for SEO and CRO typically see significantly better ROAS, as organic rankings improve Quality Scores and landing page optimisation directly reduces cost-per-conversion. We're happy to start with paid media and expand from there."),
        ],
        "cta_sub": "Running paid ads and want to know if Lumo can improve your ROAS? Book a free paid media audit — we'll analyse your current campaigns and show you where the biggest improvement opportunities are.",
    },
    "lumo-vs-smartsites": {
        "slug":        "lumo-vs-smartsites",
        "competitor":  "SmartSites",
        "title_tag":   "Lumo AI Agency vs SmartSites — Which Is Right for You? (2026)",
        "meta_desc":   "Lumo AI Agency vs SmartSites: 2026 side-by-side comparison of services, AI capabilities, pricing transparency, and which agency fits SMB and growth-stage businesses best.",
        "og_title":    "Lumo AI Agency vs SmartSites (2026 Comparison)",
        "h1_part1":    "Lumo AI Agency",
        "h1_part2":    "SmartSites",
        "summary":     "SmartSites is a well-reviewed US digital marketing agency known for serving small and mid-sized businesses with SEO, PPC, and web design. Lumo AI Agency serves the same SMB and growth-stage market — but with an AI-first approach that includes GEO, Voice AI, automations, and LLM development that SmartSites doesn't offer. For businesses that want straightforward digital marketing from a reputable agency, SmartSites is a proven option. For businesses that want AI to be a genuine competitive advantage, not just a marketing term, Lumo is the stronger choice.",
        "table_rows": [
            ("AI-First Approach",            "✅ AI-native across all services",  "⚠️  Traditional with AI tools"),
            ("GEO / AI Search Optimisation", "✅ Dedicated GEO service",          "❌ Not offered"),
            ("Voice AI Agents",              "✅ Custom AI phone agents",          "❌ Not offered"),
            ("Custom AI Automations",        "✅ Full automation builds",          "❌ Not offered"),
            ("LLM / AI App Development",     "✅ Custom AI products & RAG",        "❌ Not offered"),
            ("SEO Services",                 "✅ AI-powered technical SEO",        "✅ Core SEO service"),
            ("PPC / Google Ads",             "✅ AI bidding + conversion focus",   "✅ PPC management"),
            ("Web Design & Development",     "✅ Conversion-engineered builds",    "✅ Web design core service"),
            ("E-commerce SEO",               "✅ Shopify/WooCommerce specialist",  "✅ E-commerce SEO"),
            ("Transparent Pricing",          "✅ Published on website",            "⚠️  Quote-based"),
            ("Contract Flexibility",         "✅ Month-to-month available",        "⚠️  Typically 6-12 months"),
            ("SMB-Friendly",                 "✅ Yes — built for growth stage",    "✅ Yes — SMB focus"),
        ],
        "choose_lumo": [
            "You want an AI-native agency that builds GEO, Voice AI, and automations into your marketing — not just SEO and PPC.",
            "You're planning to integrate AI tools (chatbots, automations, LLM apps) into your business operations.",
            "You want your marketing agency to actively contribute to your AI strategy, not just manage campaigns.",
            "You need specialist e-commerce SEO for Shopify or WooCommerce alongside paid media management.",
            "You prefer month-to-month engagement flexibility with fully transparent pricing.",
        ],
        "choose_competitor": [
            "You need a straightforward SEO and PPC relationship without AI-specific deliverables.",
            "Web design is a primary need and you want a agency with a large web design portfolio.",
            "You've received a strong SmartSites referral and prefer working with a well-reviewed established agency.",
            "Your budget is tight and you need bare-minimum digital marketing coverage at the lowest possible price point.",
        ],
        "faqs": [
            ("Is Lumo AI Agency suitable for small businesses like SmartSites serves?", "Yes. Lumo works with small businesses, startups, and growth-stage companies — not just enterprises. Our packages start at accessible price points, and our AI-first approach means we can deliver more impact per dollar through automation and AI efficiency than traditional agencies of similar size. Book a free audit to see if we're a fit for your budget."),
            ("What does Lumo offer that SmartSites doesn't?", "The key differences are Lumo's AI-native services: GEO (Generative Engine Optimisation for ChatGPT and AI search), Voice AI agents, custom workflow automations, and LLM/AI app development. These aren't offered by SmartSites. Additionally, Lumo publishes transparent pricing on its website — SmartSites typically requires a custom quote."),
            ("How does Lumo's web design compare to SmartSites?", "Both agencies build conversion-focused websites. Lumo's differentiation is AI integration — we build AI chatbots, booking automation, and lead qualification into web projects alongside the design. SmartSites has a larger web design portfolio and may have stronger visual design capabilities for businesses where aesthetics are the primary priority."),
            ("Does Lumo work with the same types of businesses as SmartSites?", "Yes — both agencies serve SMBs, local businesses, and growth-stage companies across a range of industries. The key difference is capability level: SmartSites offers standard digital marketing services, while Lumo adds an AI layer across SEO, automation, and development that allows clients to build genuine competitive advantages."),
        ],
        "cta_sub": "Deciding between Lumo and SmartSites? Book a free Lumo audit first — we'll show you exactly what an AI-first approach would do differently for your specific business and goals.",
    },
}

# ---------------------------------------------------------------------------
# SHARED CSS + JS
# ---------------------------------------------------------------------------
CSS = """
    :root{--bg:#0D0D14;--bg-card:#13131F;--bg-dark:#09090F;--primary:#B3FF00;--secondary:#7C3AED;--accent:#00F5FF;--text:#F0F0FF;--muted:#6B7280;--border:rgba(179,255,0,0.15);--radius:14px;--radius-lg:20px;--transition:0.25s cubic-bezier(0.4,0,0.2,1);}
    *,*::before,*::after{box-sizing:border-box;margin:0;padding:0;}
    html{scroll-behavior:smooth;-webkit-font-smoothing:antialiased;}
    body{font-family:'Inter',system-ui,sans-serif;background:var(--bg);color:var(--text);overflow-x:hidden;line-height:1.6;}
    h1,h2,h3,h4{line-height:1.15;}
    a{color:inherit;text-decoration:none;}
    ul{list-style:none;}
    button{font-family:inherit;cursor:pointer;border:none;background:none;}
    .container{max-width:1100px;margin:0 auto;padding:0 24px;}
    .btn{display:inline-flex;align-items:center;gap:8px;padding:14px 30px;border-radius:50px;font-weight:700;font-size:0.95rem;letter-spacing:0.02em;transition:var(--transition);white-space:nowrap;}
    .btn-lime{background:var(--primary);color:#0D0D14;}
    .btn-lime:hover{background:#c8ff26;transform:translateY(-2px);box-shadow:0 8px 30px rgba(179,255,0,0.45);}
    .btn-ghost{background:transparent;color:var(--text);border:1.5px solid rgba(240,240,255,0.2);}
    .btn-ghost:hover{border-color:var(--primary);color:var(--primary);transform:translateY(-2px);}
    /* Navbar */
    #navbar{position:fixed;top:0;left:0;right:0;z-index:900;background:rgba(13,13,20,0.85);backdrop-filter:blur(16px);-webkit-backdrop-filter:blur(16px);border-bottom:1px solid rgba(179,255,0,0.06);transition:background 0.3s,border-color 0.3s;}
    #navbar.scrolled{background:rgba(13,13,20,0.97);border-bottom-color:rgba(179,255,0,0.12);}
    .nav-inner{display:flex;align-items:center;justify-content:space-between;height:68px;max-width:1180px;margin:0 auto;padding:0 24px;}
    .nav-logo{font-family:'Berkshire Swash',serif;font-size:1.6rem;color:var(--primary);letter-spacing:-0.01em;text-shadow:0 0 20px rgba(179,255,0,0.4);}
    .nav-links{display:flex;align-items:center;gap:36px;}
    .nav-links a{font-size:0.88rem;font-weight:500;color:var(--muted);transition:color var(--transition);letter-spacing:0.02em;}
    .nav-links a:hover{color:var(--primary);}
    .nav-cta{display:flex;align-items:center;}
    .nav-hamburger{display:none;flex-direction:column;gap:5px;padding:8px;}
    .nav-hamburger span{display:block;width:24px;height:2px;background:var(--text);border-radius:2px;transition:var(--transition);}
    .mobile-menu{display:none;flex-direction:column;background:rgba(13,13,20,0.98);border-top:1px solid var(--border);padding:8px 24px 16px;}
    .mobile-menu.open{display:flex;}
    .mobile-menu a{padding:14px 0;border-bottom:1px solid rgba(255,255,255,0.05);color:var(--muted);font-size:0.95rem;}
    .mobile-menu a:last-child{border-bottom:none;}
    .mobile-menu a:hover{color:var(--primary);}
    @media(max-width:768px){.nav-links,.nav-cta{display:none;}.nav-hamburger{display:flex;}}
    /* Hero */
    .page-hero{padding:130px 0 70px;position:relative;overflow:hidden;}
    .blob-wrap{position:absolute;inset:0;pointer-events:none;overflow:hidden;}
    .blob{position:absolute;border-radius:50%;filter:blur(80px);}
    .blob-lime{width:480px;height:480px;background:radial-gradient(circle,rgba(179,255,0,0.16) 0%,transparent 70%);top:-80px;left:-80px;animation:da 18s ease-in-out infinite;}
    .blob-violet{width:380px;height:380px;background:radial-gradient(circle,rgba(124,58,237,0.13) 0%,transparent 70%);bottom:0;right:-60px;animation:db 22s ease-in-out infinite;}
    @keyframes da{0%,100%{transform:translate(0,0);}50%{transform:translate(60px,50px);}}
    @keyframes db{0%,100%{transform:translate(0,0);}50%{transform:translate(-50px,-40px);}}
    .hero-inner{position:relative;z-index:2;}
    .breadcrumb{display:flex;align-items:center;gap:8px;font-size:0.8rem;color:var(--muted);margin-bottom:20px;}
    .breadcrumb a:hover{color:var(--primary);}
    .breadcrumb-sep{color:rgba(179,255,0,0.3);}
    .compare-badge{display:inline-flex;align-items:center;gap:8px;font-size:0.72rem;font-weight:700;letter-spacing:0.12em;text-transform:uppercase;color:var(--primary);background:rgba(179,255,0,0.08);border:1px solid rgba(179,255,0,0.2);padding:6px 14px;border-radius:50px;margin-bottom:22px;}
    .page-hero h1{font-family:'Berkshire Swash',serif;font-size:clamp(2.2rem,4.5vw,3.8rem);color:var(--text);line-height:1.1;margin-bottom:18px;}
    .hl-lime{color:var(--primary);}
    .vs-sep{color:var(--muted);font-size:0.7em;margin:0 4px;}
    .hero-sub{font-size:1rem;color:var(--muted);max-width:560px;margin-bottom:32px;line-height:1.7;}
    /* Summary box */
    .summary-box{background:var(--bg-card);border:1px solid var(--border);border-radius:var(--radius-lg);padding:36px;margin:60px 0;}
    .summary-box h2{font-family:'Berkshire Swash',serif;font-size:1.35rem;color:var(--primary);margin-bottom:14px;}
    .summary-box p{font-size:0.95rem;color:var(--muted);line-height:1.8;}
    /* Comparison table */
    .compare-section{padding:70px 0;}
    .section-eyebrow{display:inline-flex;align-items:center;gap:8px;font-size:0.72rem;font-weight:700;letter-spacing:0.12em;text-transform:uppercase;color:var(--primary);margin-bottom:16px;}
    .section-eyebrow::before{content:'';display:block;width:24px;height:2px;background:var(--primary);border-radius:2px;}
    .section-h2{font-family:'Berkshire Swash',serif;font-size:clamp(1.8rem,3.5vw,2.7rem);color:var(--text);margin-bottom:32px;}
    .compare-table{width:100%;border-collapse:collapse;border-radius:var(--radius-lg);overflow:hidden;}
    .compare-table thead th{background:var(--bg-dark);padding:18px 24px;font-size:0.8rem;font-weight:700;letter-spacing:0.08em;text-transform:uppercase;color:var(--muted);text-align:left;}
    .compare-table thead th:first-child{width:40%;}
    .compare-table thead th:nth-child(2){color:var(--primary);}
    .compare-table tbody tr{border-bottom:1px solid rgba(255,255,255,0.05);}
    .compare-table tbody tr:last-child{border-bottom:none;}
    .compare-table tbody tr:nth-child(even){background:rgba(255,255,255,0.015);}
    .compare-table tbody td{padding:16px 24px;font-size:0.88rem;color:var(--muted);}
    .compare-table tbody td:first-child{font-weight:600;color:var(--text);}
    .compare-table tbody td:nth-child(2){color:var(--text);}
    @media(max-width:680px){.compare-table thead th:first-child{display:none;}.compare-table tbody td:first-child{display:none;}.compare-table{font-size:0.82rem;}}
    /* Choose section */
    .choose-grid{display:grid;grid-template-columns:1fr 1fr;gap:28px;margin-top:40px;}
    .choose-card{background:var(--bg-card);border:1px solid rgba(255,255,255,0.06);border-radius:var(--radius-lg);padding:32px;}
    .choose-card.lumo-card{border-color:rgba(179,255,0,0.25);background:rgba(179,255,0,0.03);}
    .choose-card h3{font-family:'Berkshire Swash',serif;font-size:1.15rem;margin-bottom:20px;}
    .choose-card.lumo-card h3{color:var(--primary);}
    .choose-card ul li{display:flex;align-items:flex-start;gap:10px;padding:9px 0;border-bottom:1px solid rgba(255,255,255,0.05);font-size:0.87rem;color:var(--muted);line-height:1.55;}
    .choose-card ul li:last-child{border-bottom:none;}
    .choose-check{color:var(--primary);font-size:0.8rem;flex-shrink:0;margin-top:2px;}
    .choose-card.comp-card .choose-check{color:var(--muted);}
    @media(max-width:640px){.choose-grid{grid-template-columns:1fr;}}
    /* FAQ */
    .faq-section{padding:70px 0;background:var(--bg-dark);border-top:1px solid rgba(255,255,255,0.04);}
    .faq-wrap{max-width:720px;margin:0 auto;}
    .faq-item{border-bottom:1px solid rgba(179,255,0,0.08);}
    .faq-q{width:100%;text-align:left;padding:20px 0;font-size:0.96rem;font-weight:600;color:var(--text);display:flex;justify-content:space-between;align-items:center;gap:16px;background:none;border:none;font-family:inherit;cursor:pointer;}
    .faq-arrow{width:20px;height:20px;border-radius:50%;background:rgba(179,255,0,0.08);border:1px solid rgba(179,255,0,0.2);display:flex;align-items:center;justify-content:center;flex-shrink:0;transition:transform 0.3s;color:var(--primary);font-size:0.65rem;}
    .faq-item.open .faq-arrow{transform:rotate(180deg);}
    .faq-a{max-height:0;overflow:hidden;transition:max-height 0.35s ease;}
    .faq-a p{font-size:0.88rem;color:var(--muted);line-height:1.75;padding-bottom:18px;}
    .faq-item.open .faq-a{max-height:280px;}
    /* CTA */
    .cta-band{background:var(--bg);border-top:1px solid rgba(179,255,0,0.06);text-align:center;padding:90px 0;}
    .cta-band h2{font-family:'Berkshire Swash',serif;font-size:clamp(1.8rem,3.5vw,2.9rem);margin-bottom:16px;}
    .cta-band p{color:var(--muted);max-width:480px;margin:0 auto 32px;font-size:0.97rem;}
    .cta-btns{display:flex;gap:14px;justify-content:center;flex-wrap:wrap;}
    /* Footer */
    footer{background:var(--bg-dark);border-top:1px solid rgba(179,255,0,0.08);padding:56px 0 28px;}
    .footer-inner{max-width:1180px;margin:0 auto;padding:0 24px;}
    .footer-top{display:grid;grid-template-columns:1.4fr 1fr 1fr 1fr;gap:44px;margin-bottom:44px;}
    .footer-logo{font-family:'Berkshire Swash',serif;font-size:1.5rem;color:var(--primary);display:block;margin-bottom:12px;text-shadow:0 0 20px rgba(179,255,0,0.4);}
    .footer-top>div>p{font-size:0.84rem;color:var(--muted);line-height:1.7;}
    .footer-col h4{font-size:0.77rem;font-weight:700;letter-spacing:0.1em;text-transform:uppercase;color:var(--text);margin-bottom:16px;}
    .footer-col ul{display:flex;flex-direction:column;gap:10px;}
    .footer-col a{font-size:0.84rem;color:var(--muted);transition:color 0.22s;}
    .footer-col a:hover{color:var(--primary);}
    .footer-bottom{border-top:1px solid rgba(255,255,255,0.06);padding-top:20px;display:flex;justify-content:space-between;flex-wrap:wrap;gap:12px;align-items:center;}
    .footer-bottom p,.footer-bottom a{font-size:0.79rem;color:var(--muted);}
    .footer-bottom a:hover{color:var(--primary);}
    .footer-bl{display:flex;gap:20px;}
    @media(max-width:900px){.footer-top{grid-template-columns:1fr 1fr;}}
    @media(max-width:560px){.footer-top{grid-template-columns:1fr;}.footer-bottom{flex-direction:column;text-align:center;}}
    #scroll-top{position:fixed;bottom:28px;right:28px;width:44px;height:44px;border-radius:12px;background:var(--primary);color:#0D0D14;display:flex;align-items:center;justify-content:center;cursor:pointer;z-index:800;opacity:0;transform:translateY(10px);transition:opacity 0.3s,transform 0.3s;border:none;}
    #scroll-top.visible{opacity:1;transform:translateY(0);}
    #scroll-top:hover{box-shadow:0 0 20px rgba(179,255,0,0.5);}
"""

JS = """
(function(){
  var nb=document.getElementById('navbar');
  var hb=document.getElementById('hamburger');
  var mm=document.getElementById('mobile-menu');
  var open=false;
  window.addEventListener('scroll',function(){nb.classList.toggle('scrolled',window.scrollY>20);},{passive:true});
  if(hb){hb.addEventListener('click',function(){open=!open;mm.classList.toggle('open',open);hb.setAttribute('aria-expanded',String(open));mm.setAttribute('aria-hidden',String(!open));});
  mm.querySelectorAll('a').forEach(function(l){l.addEventListener('click',function(){open=false;mm.classList.remove('open');hb.setAttribute('aria-expanded','false');mm.setAttribute('aria-hidden','true');});});}
  var st=document.getElementById('scroll-top');
  if(st){window.addEventListener('scroll',function(){st.classList.toggle('visible',window.scrollY>400);},{passive:true});st.addEventListener('click',function(){window.scrollTo({top:0,behavior:'smooth'});});}
  document.querySelectorAll('.faq-q').forEach(function(btn){
    btn.addEventListener('click',function(){
      var item=this.closest('.faq-item');
      var isOpen=item.classList.contains('open');
      document.querySelectorAll('.faq-item.open').forEach(function(i){i.classList.remove('open');});
      if(!isOpen){item.classList.add('open');}
    });
  });
  if(document.querySelector('.faq-item')){document.querySelector('.faq-item').classList.add('open');}
})();
"""


def build_faq_schema(faqs):
    items = [{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in faqs]
    return {"@context":"https://schema.org","@type":"FAQPage","mainEntity":items}


def build_page(c):
    slug       = c["slug"]
    competitor = c["competitor"]
    canon      = f"https://lumoaiagency.com/compare/{slug}"

    schema = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "WebPage",
                "name":  c["title_tag"],
                "description": c["meta_desc"],
                "url":   canon,
                "datePublished": "2026-05-13",
                "dateModified":  "2026-05-13",
                "breadcrumb": {
                    "@type": "BreadcrumbList",
                    "itemListElement": [
                        {"@type":"ListItem","position":1,"name":"Home","item":"https://lumoaiagency.com"},
                        {"@type":"ListItem","position":2,"name":"Compare","item":"https://lumoaiagency.com/compare"},
                        {"@type":"ListItem","position":3,"name":f"Lumo vs {competitor}","item":canon},
                    ]
                }
            },
            build_faq_schema(c["faqs"])
        ]
    }

    # Table rows
    table_html = ""
    for feature, lumo_val, comp_val in c["table_rows"]:
        table_html += f"""      <tr>
        <td>{feature}</td>
        <td>{lumo_val}</td>
        <td>{comp_val}</td>
      </tr>\n"""

    # Choose lists
    lumo_items = "".join(
        f'<li><span class="choose-check">✓</span>{item}</li>\n' for item in c["choose_lumo"]
    )
    comp_items = "".join(
        f'<li><span class="choose-check">→</span>{item}</li>\n' for item in c["choose_competitor"]
    )

    # FAQ html
    faq_html = ""
    for i, (q, a) in enumerate(c["faqs"]):
        faq_html += f"""    <div class="faq-item">
      <button class="faq-q" aria-expanded="false">{q}<span class="faq-arrow" aria-hidden="true">▼</span></button>
      <div class="faq-a"><p>{a}</p></div>
    </div>\n"""

    html = f"""<!DOCTYPE html>
<html lang="en-US">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <meta name="robots" content="index, follow" />
  <meta name="description" content="{c['meta_desc']}" />
  <meta property="og:title" content="{c['og_title']}" />
  <meta property="og:description" content="{c['meta_desc']}" />
  <meta property="og:url" content="{canon}" />
  <meta property="og:type" content="website" />
  <meta property="og:image" content="https://lumoaiagency.com/og-image.jpg" />
  <meta name="twitter:card" content="summary_large_image" />
  <link rel="canonical" href="{canon}" />
  <title>{c['title_tag']}</title>

  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Berkshire+Swash&family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet" />

  <script type="application/ld+json">
{json.dumps(schema, ensure_ascii=False, indent=2)}
  </script>

  <style>{CSS}</style>
</head>
<body>

<header>
  <nav class="navbar" id="navbar" role="navigation" aria-label="Main navigation">
    <div class="nav-inner">
      <a href="../../index.html" class="nav-logo" aria-label="Lumo AI Agency — Home">Lumo<span>.</span></a>
      <ul class="nav-links" role="menubar">
        <li role="none"><a href="../../services.html" role="menuitem">Services</a></li>
        <li role="none"><a href="../../about.html" role="menuitem">About</a></li>
        <li role="none"><a href="../../pricing.html" role="menuitem">Pricing</a></li>
        <li role="none"><a href="../../contact.html" role="menuitem">Contact</a></li>
      </ul>
      <div class="nav-cta"><a href="../../contact.html" class="btn btn-lime" style="padding:10px 22px;font-size:0.85rem;">Get Started</a></div>
      <button class="nav-hamburger" id="hamburger" aria-label="Open menu" aria-expanded="false" aria-controls="mobile-menu">
        <span></span><span></span><span></span>
      </button>
    </div>
    <div class="mobile-menu" id="mobile-menu" role="menu" aria-hidden="true">
      <a href="../../services.html" role="menuitem">Services</a>
      <a href="../../about.html" role="menuitem">About</a>
      <a href="../../pricing.html" role="menuitem">Pricing</a>
      <a href="../../contact.html" role="menuitem">Contact</a>
      <a href="../../contact.html" role="menuitem">Get Started &rarr;</a>
    </div>
  </nav>
</header>

<main>

  <!-- HERO -->
  <section class="page-hero">
    <div class="blob-wrap" aria-hidden="true"><div class="blob blob-lime"></div><div class="blob blob-violet"></div></div>
    <div class="container hero-inner">
      <nav class="breadcrumb" aria-label="Breadcrumb">
        <a href="../../index.html">Home</a>
        <span class="breadcrumb-sep" aria-hidden="true">›</span>
        <span>Compare</span>
        <span class="breadcrumb-sep" aria-hidden="true">›</span>
        <span>Lumo vs {competitor}</span>
      </nav>
      <div class="compare-badge">⚖️ Agency Comparison · 2026</div>
      <h1><span class="hl-lime">{c['h1_part1']}</span> <span class="vs-sep">vs</span> {c['h1_part2']}</h1>
      <p class="hero-sub">An honest, side-by-side comparison of both agencies — services, AI capabilities, pricing, and who each one is best suited for. No spin.</p>
      <div style="display:flex;gap:14px;flex-wrap:wrap;">
        <a href="../../contact.html" class="btn btn-lime">Book Free Lumo Audit <svg width="16" height="16" viewBox="0 0 16 16" fill="none" aria-hidden="true"><path d="M3 8h10M9 4l4 4-4 4" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg></a>
        <a href="../../pricing.html" class="btn btn-ghost">See Lumo Pricing</a>
      </div>
    </div>
  </section>

  <!-- SUMMARY -->
  <section style="padding:0 0 20px;">
    <div class="container">
      <div class="summary-box">
        <h2>Quick Summary</h2>
        <p>{c['summary']}</p>
      </div>
    </div>
  </section>

  <!-- COMPARISON TABLE -->
  <section class="compare-section" aria-labelledby="table-h2">
    <div class="container">
      <p class="section-eyebrow">Side by Side</p>
      <h2 class="section-h2" id="table-h2">Feature Comparison</h2>
      <div style="overflow-x:auto;border-radius:var(--radius-lg);border:1px solid rgba(255,255,255,0.06);">
        <table class="compare-table" role="table" aria-label="Lumo vs {competitor} feature comparison">
          <thead>
            <tr>
              <th scope="col">Feature</th>
              <th scope="col">Lumo AI Agency</th>
              <th scope="col">{competitor}</th>
            </tr>
          </thead>
          <tbody>
{table_html}          </tbody>
        </table>
      </div>
    </div>
  </section>

  <!-- WHEN TO CHOOSE -->
  <section style="padding:60px 0;background:var(--bg-dark);border-top:1px solid rgba(255,255,255,0.04);" aria-labelledby="choose-h2">
    <div class="container">
      <p class="section-eyebrow">Making the Right Choice</p>
      <h2 class="section-h2" id="choose-h2">Which Agency Is Right for You?</h2>
      <div class="choose-grid">
        <div class="choose-card lumo-card">
          <h3>Choose Lumo AI Agency if…</h3>
          <ul>{lumo_items}</ul>
        </div>
        <div class="choose-card comp-card">
          <h3>Consider {competitor} if…</h3>
          <ul>{comp_items}</ul>
        </div>
      </div>
    </div>
  </section>

  <!-- FAQ -->
  <section class="faq-section" aria-labelledby="faq-h2">
    <div class="container">
      <div style="text-align:center;margin-bottom:44px;">
        <p class="section-eyebrow" style="justify-content:center;">Common Questions</p>
        <h2 class="section-h2" id="faq-h2" style="max-width:600px;margin:0 auto;">Frequently Asked Questions About <span class="hl-lime">Lumo vs {competitor}</span></h2>
      </div>
      <div class="faq-wrap">
{faq_html}      </div>
    </div>
  </section>

  <!-- CTA -->
  <section class="cta-band" aria-labelledby="cta-h2">
    <div class="container">
      <p class="section-eyebrow" style="justify-content:center;">Still Deciding?</p>
      <h2 id="cta-h2">Get a <span class="hl-lime">Second Opinion</span></h2>
      <p>{c['cta_sub']}</p>
      <div class="cta-btns">
        <a href="../../contact.html" class="btn btn-lime">Book Free Strategy Call <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14M12 5l7 7-7 7"/></svg></a>
        <a href="../../pricing.html" class="btn btn-ghost">View Lumo Pricing</a>
      </div>
    </div>
  </section>

</main>

<footer role="contentinfo">
  <div class="footer-inner">
    <div class="footer-top">
      <div>
        <a href="../../index.html" class="footer-logo" aria-label="Lumo AI Agency home">Lumo<span>.</span></a>
        <p>Austin's AI-powered marketing agency. SEO, paid ads, AI automation &amp; web design built for the future.</p>
      </div>
      <div class="footer-col">
        <h4>Services</h4>
        <ul>
          <li><a href="../../services/seo.html">SEO &amp; Content</a></li>
          <li><a href="../../services/google-ads.html">Google Ads</a></li>
          <li><a href="../../services/meta-ads.html">Meta Ads</a></li>
          <li><a href="../../services/linkedin-ads.html">LinkedIn Ads</a></li>
          <li><a href="../../services/geo.html">GEO / AI Search</a></li>
          <li><a href="../../services/ai-automations.html">AI Automations</a></li>
          <li><a href="../../services/cro.html">CRO</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h4>Compare</h4>
        <ul>
          <li><a href="../../compare/lumo-vs-webfx/">Lumo vs WebFX</a></li>
          <li><a href="../../compare/lumo-vs-thrive-agency/">Lumo vs Thrive</a></li>
          <li><a href="../../compare/lumo-vs-np-digital/">Lumo vs NP Digital</a></li>
          <li><a href="../../compare/lumo-vs-ignite-digital/">Lumo vs Ignite Digital</a></li>
          <li><a href="../../compare/lumo-vs-disruptive-advertising/">Lumo vs Disruptive</a></li>
          <li><a href="../../compare/lumo-vs-smartsites/">Lumo vs SmartSites</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h4>Company</h4>
        <ul>
          <li><a href="../../about.html">About Us</a></li>
          <li><a href="../../services.html">All Services</a></li>
          <li><a href="../../pricing.html">Pricing</a></li>
          <li><a href="../../contact.html">Contact</a></li>
        </ul>
        <h4 style="margin-top:20px;">Contact</h4>
        <ul>
          <li><a href="tel:+16473701888">(647) 370-1888</a></li>
          <li><a href="mailto:hello@lumoaiagency.com">hello@lumoaiagency.com</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <p>&copy; 2026 Lumo AI Agency. All rights reserved.</p>
      <div class="footer-bl">
        <a href="../../privacy-policy.html">Privacy Policy</a>
        <a href="../../terms.html">Terms of Service</a>
        <a href="../../cookie-policy.html">Cookie Policy</a>
      </div>
    </div>
  </div>
</footer>

<button id="scroll-top" aria-label="Scroll to top">
  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 19V5M5 12l7-7 7 7"/></svg>
</button>

<script>{JS}</script>
</body>
</html>"""
    return html


def main():
    for slug, comp in COMPARISONS.items():
        out_dir = os.path.join(BASE, "compare", slug)
        os.makedirs(out_dir, exist_ok=True)
        html = build_page(comp)
        with open(os.path.join(out_dir, "index.html"), "w", encoding="utf-8") as f:
            f.write(html)
        print(f"Created: compare/{slug}/index.html ({len(html):,} chars)")
    print(f"Done. {len(COMPARISONS)} pages created.")


if __name__ == "__main__":
    main()
