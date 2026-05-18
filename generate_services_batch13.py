"""Batch 13 — Backlog Batch 8: franchise-marketing, multi-location-marketing, marketing-analytics, conversion-tracking, marketing-attribution"""
import json, os

SERVICES = {
    "franchise-marketing": {
        "title": "Franchise Marketing",
        "tagline": "Scalable marketing systems for franchise networks — brand compliance at every location",
        "desc": "Franchise marketing requires a unique balance: national brand consistency and local market relevance at every location. We build scalable marketing systems for franchise networks — centralized strategy, templated local execution, and the technology stack to manage hundreds of locations without losing brand control or local effectiveness.",
        "price": "$5,000/mo",
        "stat1": "785K+",
        "stat1_label": "franchise establishments operating in the US",
        "stat2": "2.3x",
        "stat2_label": "faster growth for franchises with centralized marketing systems",
        "stat3": "67%",
        "stat3_label": "of franchise buyers research online before contacting a franchisor",
        "deliverables": [
            ("🏢", "Franchise Marketing System Design", "A centralized marketing infrastructure: brand standards, templated campaigns, asset libraries, and approval workflows that allow local execution without brand drift."),
            ("📍", "Local SEO for Each Location", "Individual Google Business Profile management, local citation building, and location-specific landing pages for every franchise unit — driving local organic traffic to each location."),
            ("🎯", "Paid Advertising (National + Local)", "Tiered paid advertising: brand-level campaigns managed centrally and local campaigns co-funded and co-managed with individual franchisees — consistent strategy, local targeting."),
            ("📱", "Social Media Templates", "Franchisee-ready social media templates for every platform — editable with local details (address, phone, offers) while maintaining brand visual standards."),
            ("📣", "Franchise Development Marketing", "Lead generation campaigns targeting qualified franchise buyers — for franchisors looking to grow their network through franchise sales."),
            ("📊", "Multi-Location Reporting Dashboard", "A unified reporting dashboard showing marketing performance by location, region, and network — enabling comparison, benchmarking, and resource allocation decisions."),
            ("🎓", "Franchisee Marketing Training", "Training programs for franchisees: how to use templates, manage their GBP, respond to reviews, and execute local marketing within brand guidelines."),
        ],
        "process": [
            ("🔍", "Network Audit & Strategy", "We audit your current franchise marketing setup, interview franchisees, and identify gaps in consistency, local execution, and technology. We build a phased marketing system plan."),
            ("⚙️", "System Build & Integration", "Marketing infrastructure built: asset library, templated campaigns, reporting dashboard, and technology integrations. GBP management setup for all locations."),
            ("🚀", "Launch & Franchisee Onboarding", "Network-wide rollout with franchisee training and onboarding. Local campaigns activated location by location. Central campaigns launched."),
            ("📈", "Optimize & Scale", "Monthly network-level performance review. Location-level coaching for underperforming units. System improvements rolled out network-wide."),
        ],
        "faqs": [
            ("Do you work with both franchisors and franchisees?", "Yes — we work with franchisors building network-wide systems and with individual franchisees who want to maximize marketing within their territory. Our approach is always aligned with the franchisor's brand standards."),
            ("How do you handle different budgets across franchisees?", "We design tiered marketing programs: a base tier fully funded by the franchisor, and optional add-on tiers franchisees can purchase for additional local marketing support. This respects budget variation while maintaining consistency."),
            ("Can you manage locations in multiple states?", "Yes — we manage multi-state and national franchise networks. Our reporting infrastructure is designed for geographic segmentation at the region, state, DMA, and individual location level."),
            ("How do you maintain brand consistency across locations?", "Through asset libraries, locked templates, an approval workflow for custom creative, and regular brand compliance audits. Franchisees have flexibility within defined parameters — never full creative freedom."),
            ("Do you handle franchise lead generation?", "Yes — franchise development marketing (recruiting new franchisees) is a separate service we offer alongside local marketing for existing locations."),
        ],
        "schema_service_desc": "Franchise marketing — marketing system design, local SEO per location, paid advertising, social templates, franchisee training, and multi-location reporting dashboard.",
    },
    "multi-location-marketing": {
        "title": "Multi-Location Marketing",
        "tagline": "Unified digital marketing strategy across every location — consistent and locally optimized",
        "desc": "Multi-location businesses face a unique marketing challenge: how to maintain brand consistency while driving local relevance at every location. We build and manage integrated marketing programs for businesses with 2–200+ locations — from local SEO and GBP management to location-specific paid campaigns and centralized reporting.",
        "price": "$3,500/mo",
        "stat1": "46%",
        "stat1_label": "of Google searches have local intent",
        "stat2": "76%",
        "stat2_label": "of local searches result in a store visit within 24 hours",
        "stat3": "28%",
        "stat3_label": "of local searches result in a purchase",
        "deliverables": [
            ("🗺️", "Location Strategy & Prioritization", "We analyze performance by location and identify where marketing investment will generate the highest return — ensuring resources are allocated to the locations with the greatest growth potential."),
            ("📍", "Local SEO Per Location", "Location-specific landing pages, Google Business Profile optimization, and local citation management for every location — maximizing organic visibility in each market."),
            ("🎯", "Geo-Targeted Paid Campaigns", "Location-specific paid search and social campaigns with geo-targeting, local offer customization, and budget allocation calibrated to each market's competitive intensity."),
            ("📱", "Location-Specific Social", "Social media content tailored for each location's market — local events, staff features, community involvement, and location-specific offers — managed from a central content system."),
            ("⭐", "Review Management", "Centralized review monitoring and response across Google, Yelp, and industry platforms for all locations — maintaining reputation consistency while allowing location-specific response personalization."),
            ("📊", "Unified Analytics Dashboard", "A single reporting view across all locations: traffic, leads, conversions, and revenue by location — enabling apples-to-apples comparison and data-driven resource allocation."),
            ("🔄", "Cross-Location Optimization", "Insights from top-performing locations applied network-wide. What's working in Location A gets implemented in Location B — accelerating network-wide improvement."),
        ],
        "process": [
            ("🔍", "Audit & Baseline", "We audit every location's current digital presence, identify performance gaps, and establish baseline metrics. Location performance ranked to prioritize quick wins."),
            ("⚙️", "Infrastructure Setup", "Location pages built or optimized, GBPs claimed and configured, analytics tracking established for all locations, and campaign structures built."),
            ("🚀", "Launch & Localize", "Campaigns activated location by location, with local customization applied for each market. Centralized monitoring begins from day one."),
            ("📈", "Optimize Continuously", "Monthly cross-location performance review. Best practices from top locations propagated. Budget shifted toward highest-performing markets."),
        ],
        "faqs": [
            ("How many locations can you manage?", "We manage businesses with 2 to 200+ locations. Our processes and technology stack are designed for scale — adding a location doesn't linearly increase management overhead."),
            ("Does each location get its own campaigns?", "Yes — each location gets geo-targeted campaigns, a dedicated GBP, and location-specific landing pages. The creative and messaging are templated from a central system but locally customized."),
            ("How do you handle locations in different competitive markets?", "Budget and bidding are calibrated per market. A location in a low-competition suburban market gets a different strategy than one in a dense urban market. We optimize each location's approach to its competitive environment."),
            ("Can we add or remove locations during the engagement?", "Yes — our program is designed to scale up and down. Adding a new location triggers our onboarding checklist; closing a location triggers an orderly wind-down of its marketing programs."),
            ("What's the minimum number of locations you work with?", "We work with businesses starting at 2 locations. The multi-location infrastructure becomes especially valuable at 5+ locations, where centralization dramatically reduces per-location management cost."),
        ],
        "schema_service_desc": "Multi-location marketing — local SEO per location, GBP management, geo-targeted campaigns, review management, and unified analytics dashboard.",
    },
    "marketing-analytics": {
        "title": "Marketing Analytics",
        "tagline": "Full-funnel data visibility — know exactly what's working and what's wasting budget",
        "desc": "Most businesses are flying blind — running campaigns without reliable data on what's generating revenue. We build and manage your marketing analytics infrastructure: tracking setup, data integration, attribution modeling, and reporting dashboards that give you clear answers to the questions that drive marketing decisions.",
        "price": "$2,500/mo",
        "stat1": "5x",
        "stat1_label": "ROI for companies using data-driven marketing",
        "stat2": "64%",
        "stat2_label": "of marketers cite analytics as critical to competitive advantage",
        "stat3": "39%",
        "stat3_label": "average budget waste eliminated with proper attribution",
        "deliverables": [
            ("📊", "Analytics Audit & Strategy", "A comprehensive audit of your current analytics setup — tracking gaps, data quality issues, attribution blind spots, and reporting gaps — with a prioritized remediation plan."),
            ("⚙️", "Tracking Implementation", "Full tracking implementation via Google Tag Manager: GA4 events, Meta Pixel, LinkedIn Insight Tag, conversion tracking for all marketing channels, and custom events for key user actions."),
            ("🔗", "Data Integration & Warehousing", "Integration of marketing data sources (Google Ads, Meta, LinkedIn, HubSpot, Salesforce) into a centralized data warehouse (BigQuery or Snowflake) for unified reporting and analysis."),
            ("📈", "Custom Reporting Dashboards", "Executive and channel-level dashboards in Looker Studio or Tableau: ROAS by channel, CAC by source, LTV by cohort, funnel conversion rates, and revenue attribution — built to your reporting needs."),
            ("🎯", "Attribution Modeling", "Custom attribution model development: first-touch, last-touch, linear, time-decay, or data-driven — with implementation across your ad platforms and CRM for consistent revenue attribution."),
            ("🔍", "Anomaly Detection & Alerts", "Automated alerts for tracking breakage, significant performance changes, and data quality issues — so you catch problems immediately rather than discovering them at month-end reporting."),
            ("📋", "Monthly Analytics Review", "Monthly analytics review meeting: performance against benchmarks, emerging trends, channel efficiency analysis, and data-driven budget reallocation recommendations."),
        ],
        "process": [
            ("🔍", "Audit & Gap Analysis", "We audit every analytics touchpoint — website tracking, ad platform tracking, CRM integration, and reporting — and produce a gap analysis with prioritized fixes."),
            ("⚙️", "Build & Implement", "Tracking infrastructure built in GTM, integrations configured, data warehouse connected, and dashboards built. QA'd against live traffic before sign-off."),
            ("✅", "Validate & Baseline", "Data quality validated across all channels. Baselines established for all KPIs. Attribution model tested and calibrated against historical revenue data."),
            ("📈", "Monitor & Advise", "Ongoing monitoring, monthly review meetings, and proactive recommendations based on the data — turning analytics from a reporting tool into a decision-making engine."),
        ],
        "faqs": [
            ("We already have Google Analytics — why do we need this?", "Having GA4 installed is not the same as having reliable analytics. Most GA4 setups are missing 30–50% of conversions, have broken event tracking, and lack cross-channel attribution. We audit what you have and fill the gaps."),
            ("What's the difference between analytics and attribution?", "Analytics tracks what happened (traffic, conversions, revenue). Attribution assigns credit for conversions to the marketing touchpoints that drove them. Both are needed — attribution is the layer that tells you which channels to invest in."),
            ("Do you need access to our ad platforms?", "Yes — read-level access to all advertising platforms (Google Ads, Meta, LinkedIn, etc.), your CRM, and your website analytics. We document all access requirements upfront and work within your security policies."),
            ("Can you fix tracking that was set up incorrectly?", "Yes — fixing broken tracking setups is often the most impactful quick win. We audit, identify the issues, and implement corrections — often revealing significant conversion volume that was being missed."),
            ("What tools do you use for reporting?", "We build dashboards in Looker Studio (free, widely accessible) or Tableau/Power BI for enterprise clients. Data warehousing via Google BigQuery or Snowflake. All dashboards are yours — they don't disappear if you leave."),
        ],
        "schema_service_desc": "Marketing analytics — tracking audit, GTM implementation, data integration, custom dashboards, attribution modeling, and monthly performance reviews.",
    },
    "conversion-tracking": {
        "title": "Conversion Tracking",
        "tagline": "Accurate, cross-channel conversion tracking that makes every ad dollar accountable",
        "desc": "If your conversion tracking isn't accurate, your ad platforms are optimizing toward the wrong signals — wasting budget and making bad decisions at scale. We implement and maintain bulletproof conversion tracking across every marketing channel: server-side tracking, GA4 events, and CRM integration that gives you the data to make the right calls.",
        "price": "$1,500/mo",
        "stat1": "40%",
        "stat1_label": "average conversion data lost with client-side tracking alone",
        "stat2": "3x",
        "stat2_label": "better ROAS when ad platforms receive accurate conversion signals",
        "stat3": "iOS 14+",
        "stat3_label": "privacy changes require server-side tracking for accurate data",
        "deliverables": [
            ("⚙️", "Conversion Audit & Diagnosis", "A complete audit of your current conversion tracking: what's firing, what's broken, what's double-counting, and what's missing — with a prioritized fix list and estimated data recovery impact."),
            ("🖥️", "Server-Side Tracking Implementation", "Server-side tracking via Google Tag Manager Server-Side or Segment — bypassing ad blockers and iOS privacy restrictions to recover 30–50% of conversions typically missed by client-side tracking."),
            ("📊", "GA4 Event Configuration", "Full GA4 event taxonomy: purchase, lead, sign-up, engagement, and custom micro-conversion events — properly parameterized for segmentation and funnel analysis."),
            ("🎯", "Ad Platform Conversion Setup", "Google Ads enhanced conversions, Meta Conversions API (CAPI), LinkedIn Insight Tag, TikTok Events API — all configured for maximum signal quality and privacy-compliant data transmission."),
            ("🔗", "CRM & Offline Conversion Import", "CRM integration for offline conversion tracking: sales closed, qualified opportunities, and LTV data imported back into ad platforms for full-funnel optimization — not just lead tracking."),
            ("🔍", "Cross-Device & Cross-Session Attribution", "Identity resolution setup for cross-device conversion tracking — connecting mobile app, web, and CRM data to build a complete picture of the customer journey."),
            ("🔔", "Monitoring & Alerting", "Automated monitoring for conversion tracking health: volume drop alerts, tag firing errors, and data quality checks — so tracking issues are caught in hours, not months."),
        ],
        "process": [
            ("🔍", "Audit & Diagnose", "We audit every tracking touchpoint — GTM container, GA4, ad platforms, CRM — and produce a complete picture of what's working, what's broken, and what the data quality impact is."),
            ("⚙️", "Implement & Configure", "Server-side container setup, event configurations, ad platform integrations, and CRM connections implemented and QA'd against live traffic."),
            ("✅", "Validate & Verify", "Every conversion event verified end-to-end: trigger fires correctly, parameters pass accurately, ad platform receives the signal. Deduplication rules configured."),
            ("🔔", "Monitor & Maintain", "Ongoing health monitoring, monthly data quality review, and updates for platform changes (iOS updates, browser policy changes, GA4 updates)."),
        ],
        "faqs": [
            ("What is server-side tracking and why do I need it?", "Client-side tracking (standard GTM) runs in the browser — where ad blockers, iOS privacy settings, and browser restrictions can block 30–50% of conversion data. Server-side tracking runs on your server before the browser blocks it, recovering that lost data and sending cleaner signals to ad platforms."),
            ("Will this improve our ad performance?", "Yes — directly. Google Smart Bidding and Meta Advantage+ use conversion signals to optimize. When those signals are incomplete or inaccurate, the algorithms optimize poorly. Better data means better algorithmic decisions and measurably lower CPAs."),
            ("Do we need to change our website?", "Minimal changes required. We implement everything through Google Tag Manager and server-side containers. Some implementations require a small code snippet or pixel placement, but we handle the full technical implementation."),
            ("What about GDPR and CCPA compliance?", "Our server-side implementations are built with privacy compliance built in: consent mode integration, data minimization, and proper data processing agreements. We implement tracking that respects user consent signals."),
            ("How long does implementation take?", "Standard implementation (GA4 + Google Ads + Meta CAPI) takes 2–3 weeks. Complex implementations with CRM integration, custom events, and multiple ad platforms take 4–6 weeks."),
        ],
        "schema_service_desc": "Conversion tracking — server-side tracking, GA4 events, ad platform conversions API, CRM integration, offline conversion import, and ongoing monitoring.",
    },
    "marketing-attribution": {
        "title": "Marketing Attribution",
        "tagline": "Multi-touch attribution modeling that reveals the true source of your revenue",
        "desc": "Last-click attribution is lying to you — crediting the final touch while ignoring every channel that built awareness and drove consideration. We implement multi-touch attribution modeling that accurately distributes revenue credit across your full marketing mix, revealing which channels truly deserve investment and which are just showing up at the end of journeys they didn't create.",
        "price": "$2,500/mo",
        "stat1": "76%",
        "stat1_label": "of marketers use last-click attribution — the most misleading model",
        "stat2": "4.2x",
        "stat2_label": "more accurate budget allocation with multi-touch attribution",
        "stat3": "23%",
        "stat3_label": "average media budget freed up by eliminating misattributed spend",
        "deliverables": [
            ("🔍", "Attribution Audit", "A diagnostic review of your current attribution setup: what model you're using, where credit is being misallocated, and the estimated budget impact of attribution blind spots."),
            ("🗺️", "Customer Journey Mapping", "We map your actual customer journeys — average touchpoint counts, channel sequences, time-to-conversion by segment — to understand the real path to purchase before building the attribution model."),
            ("⚙️", "Attribution Model Implementation", "Custom attribution model implemented across your ad platforms and analytics stack: first-touch, linear, time-decay, position-based, or data-driven (for sufficient conversion volume)."),
            ("🔗", "Cross-Channel Data Unification", "Integration of all marketing channel data into a unified attribution view — paid search, paid social, organic, email, direct, referral — so every touchpoint appears in the same model."),
            ("📊", "Attribution Dashboard", "A dedicated attribution dashboard showing revenue credit by channel, channel-level CPA and ROAS under the correct attribution model, and journey-level path analysis."),
            ("💡", "Budget Reallocation Recommendations", "Data-driven budget reallocation recommendations based on attribution-corrected performance — with modeled projections of revenue impact from shifting budget between channels."),
            ("🔄", "Ongoing Attribution Review", "Monthly attribution review: model performance, new journey pattern analysis, and budget recommendations — ensuring the model evolves as your channel mix and customer behavior change."),
        ],
        "process": [
            ("🔍", "Journey Analysis", "We analyze your historical conversion data to map actual customer journeys and identify the attribution gaps that are currently distorting your channel performance view."),
            ("⚙️", "Model Selection & Build", "Attribution model selected based on your business model, conversion volume, and sales cycle. Built in your analytics stack and validated against historical revenue data."),
            ("📊", "Dashboard & Baseline", "Attribution dashboard built. Channel performance re-baselined under the new model — revealing the real winners and losers in your channel mix."),
            ("💡", "Advise & Optimize", "Monthly attribution review with budget reallocation recommendations. Model calibrated quarterly as new conversion data accumulates."),
        ],
        "faqs": [
            ("Why is last-click attribution a problem?", "Last-click gives 100% of the conversion credit to the final touchpoint before purchase — typically branded search or direct. This makes top-of-funnel channels (display, social awareness, content) look worthless, leading businesses to cut the channels that are actually driving demand."),
            ("What's the difference between attribution and analytics?", "Analytics measures what happened. Attribution assigns credit for what happened to the marketing activities that caused it. Attribution is the layer that answers 'which channels drove this revenue?' rather than just 'which channel was last touched.'"),
            ("Do we need a lot of conversions for this to work?", "Data-driven attribution requires 3,000+ monthly conversions to train accurately. For lower-volume businesses, we implement rule-based models (position-based or time-decay) that are more accurate than last-click without requiring high conversion volume."),
            ("Will this change how our ad platforms optimize?", "Yes — and that's the point. Once ad platforms receive corrected conversion signals, Smart Bidding and automated bidding strategies optimize toward the right goal. The budget efficiency gains typically pay for the attribution work within 60–90 days."),
            ("Can you integrate with our CRM for revenue attribution?", "Yes — CRM integration is a core part of our attribution implementation. We import pipeline stages and closed revenue back into ad platforms and analytics, enabling true revenue attribution rather than lead attribution."),
        ],
        "schema_service_desc": "Marketing attribution — multi-touch attribution modeling, cross-channel data unification, attribution dashboard, budget reallocation recommendations, and ongoing model optimization.",
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
            <li><a href="../services/marketing-analytics.html">Marketing Analytics</a></li>
            <li><a href="../services/conversion-tracking.html">Conversion Tracking</a></li>
            <li><a href="../services/marketing-attribution.html">Marketing Attribution</a></li>
            <li><a href="../services/franchise-marketing.html">Franchise Marketing</a></li>
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
