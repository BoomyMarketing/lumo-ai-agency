#!/usr/bin/env python3
"""Generate Wave 3 service pages — Batch 1 of 5:
   technical-seo, local-seo, reputation-management,
   link-building, google-local-services-ads
"""
import os, json

BASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "services")
os.makedirs(BASE, exist_ok=True)

SERVICES = {

    "technical-seo": {
        "title_tag":  "Technical SEO Agency | Fix What's Holding Your Rankings Back | Lumo AI",
        "meta_desc":  "Technical SEO audits and fixes from Lumo AI Agency. Core Web Vitals, site architecture, crawlability, schema markup — we identify and fix every issue killing your rankings. Free audit.",
        "canonical":  "https://lumoaiagency.com/services/technical-seo",
        "og_title":   "Technical SEO Agency | Lumo AI Agency",
        "og_desc":    "Full technical SEO audits: Core Web Vitals, crawlability, structured data, site speed, and indexation fixes. Results you can see in 30 days.",
        "h1_html":    "Technical SEO That <span class=\"hl-lime\">Removes</span> Every Ranking Blocker",
        "badge":      "Technical SEO Specialists",
        "lead":       "Most agencies run campaigns on broken foundations. Lumo audits every technical layer of your site and fixes the crawlability, speed, and structure issues that silently suppress your rankings.",
        "stat1_num": "340%", "stat1_lbl": "Average organic traffic lift after technical fix",
        "stat2_num": "48h",  "stat2_lbl": "Full technical audit turnaround time",
        "stat3_num": "97%",  "stat3_lbl": "Core Web Vitals pass rate after Lumo audit",
        "why_h2": "Why Technical SEO Is the Foundation of Every Ranking",
        "why_p1": "You can publish great content and earn quality backlinks — and still not rank. If Googlebot can't efficiently crawl your site, if your pages load slowly on mobile, or if duplicate content fragments your authority, every other SEO investment is undermined. Technical SEO is the infrastructure everything else sits on.",
        "why_p2": "Most agencies ignore technical SEO because it's less visible than content or link building. Lumo starts every SEO engagement with a deep technical audit — identifying crawl traps, Core Web Vitals failures, schema errors, hreflang issues, and site architecture problems before we write a single piece of content.",
        "why_p3": "AI crawlers add a new dimension to technical SEO in 2026. ChatGPT, Perplexity, and Google's AI systems have their own crawlers with specific requirements. Lumo audits AI crawler accessibility — ensuring your site is as visible to GPTBot and Anthropic's crawler as it is to Googlebot.",
        "services_h2": "What Our Technical SEO Service Covers",
        "services": [
            ("🔍", "Full Technical Audit", "180-point audit covering crawlability, indexation, site speed, mobile usability, duplicate content, canonical tags, structured data, internal linking, and more — delivered as a prioritised fix list."),
            ("⚡", "Core Web Vitals Optimization", "LCP, CLS, and INP improvements — from image compression and lazy loading to JavaScript deferral and server-side rendering fixes that move your pages into the 'Good' CWV range."),
            ("🏗️", "Site Architecture & Internal Linking", "URL structure review, siloing strategy, crawl depth analysis, and internal linking optimisation — ensuring PageRank flows efficiently to your highest-value pages."),
            ("🤖", "Schema & Structured Data", "Implementation and validation of JSON-LD schema: Article, FAQPage, LocalBusiness, Product, BreadcrumbList, HowTo — enabling rich results and improving AI search citability."),
            ("🗺️", "XML Sitemap & Robots.txt", "Sitemap audit (orphaned pages, blocked URLs, outdated entries), robots.txt optimisation, and crawl budget management for large and complex sites."),
            ("🌐", "Crawlability & Indexation Fixes", "Identify and resolve crawl traps, soft 404s, redirect chains, mixed-content issues, hreflang errors, and pagination problems that confuse search engine crawlers."),
        ],
        "process": [
            ("🔎", "Technical Audit", "We crawl your entire site with enterprise-grade tools (Screaming Frog, Sitebulb, GSC data) and produce a prioritised issues list ranked by ranking impact."),
            ("📋", "Fix Roadmap", "Every issue gets a severity rating, estimated effort, and implementation instructions — whether your team fixes it or Lumo handles the dev work directly."),
            ("🛠️", "Implementation", "Lumo's technical team handles Core Web Vitals fixes, schema implementation, redirect mapping, and architecture changes — no waiting on your dev queue."),
            ("📊", "Monitor & Verify", "Post-fix monitoring in Google Search Console, CrUX, and our crawler to confirm issues are resolved and rankings respond — with monthly technical health reports."),
        ],
        "price_from": "$1,500",
        "price_note": "per month — Technical SEO audit + fixes + monthly health monitoring",
        "faqs": [
            ("What is a technical SEO audit?", "A technical SEO audit is a comprehensive analysis of your website's technical infrastructure — crawlability, indexation, site speed, mobile usability, structured data, and more. Lumo's audit produces a prioritised list of issues ranked by their impact on rankings, so you know exactly what to fix first."),
            ("How long does it take to see results from technical SEO fixes?", "Many technical fixes show results within 2–4 weeks as Google recrawls and reindexes fixed pages. Core Web Vitals improvements often appear in CrUX data within 28 days. Structural fixes (site architecture, canonicals) may take 4–8 weeks to fully reflect in rankings."),
            ("Do you fix the issues or just report them?", "Both. Lumo provides a full audit report AND handles implementation. Our technical team can fix Core Web Vitals issues, implement schema markup, resolve redirect chains, and update your sitemap directly — we don't just hand you a spreadsheet of problems."),
            ("What tools does Lumo use for technical SEO?", "Lumo uses Screaming Frog, Sitebulb, Google Search Console, PageSpeed Insights, Web.dev, Schema Markup Validator, Ahrefs Site Audit, and custom crawl scripts. We cross-reference data from multiple tools to catch issues that any single tool would miss."),
            ("Is technical SEO a one-time fix or ongoing?", "Both. The initial audit and fix sprint resolves existing issues. Ongoing technical SEO monitoring catches new problems introduced by site updates, new content, or platform changes — and ensures your Core Web Vitals stay in the 'Good' range as your site evolves."),
        ],
        "cta_h2": "Ready to Unblock Your Rankings?",
        "cta_sub": "Get a free technical SEO audit — we'll identify the top issues suppressing your organic traffic and show you exactly what needs to be fixed.",
        "schema_service_name": "Technical SEO Services",
        "schema_service_desc": "Comprehensive technical SEO audits and fixes — Core Web Vitals, crawlability, structured data, site architecture, and indexation optimization for US businesses.",
    },

    "local-seo": {
        "title_tag":  "Local SEO Agency | Dominate Google Maps & Local Search | Lumo AI",
        "meta_desc":  "Local SEO services from Lumo AI Agency. Google Business Profile, local citations, map pack rankings, and review strategy for US businesses. Get found by nearby customers. Free audit.",
        "canonical":  "https://lumoaiagency.com/services/local-seo",
        "og_title":   "Local SEO Agency | Lumo AI Agency",
        "og_desc":    "Rank in the Google Map Pack and local search results. Lumo AI Agency builds local SEO strategies that drive foot traffic, calls, and qualified leads from nearby customers.",
        "h1_html":    "Local SEO That Puts You <span class=\"hl-lime\">Top of the Map</span>",
        "badge":      "Local SEO Specialists",
        "lead":       "When someone searches for your service in your city, are you in the top 3? Lumo builds local SEO strategies that plant you in the Google Map Pack and keep you there — turning nearby searches into customers.",
        "stat1_num": "3.9x", "stat1_lbl": "Average local lead ROI for Lumo clients",
        "stat2_num": "78%",  "stat2_lbl": "Of local searches result in an in-store visit",
        "stat3_num": "60d",  "stat3_lbl": "Average time to top-3 Map Pack ranking",
        "why_h2": "Why Local SEO Is the Highest-ROI Channel for Local Businesses",
        "why_p1": "Over 46% of all Google searches have local intent — people looking for businesses, services, and products near them. The three businesses that appear in the Google Map Pack capture the overwhelming majority of those clicks and calls. If you're not in the top three, you're invisible to the most valuable local searchers.",
        "why_p2": "Local SEO is fundamentally different from traditional SEO. It's driven by Google Business Profile signals, citation consistency, review velocity, and hyper-local content — not just backlinks and keywords. Lumo builds local SEO strategies that address every factor Google uses to rank local businesses.",
        "why_p3": "AI search is changing local discovery too. When someone asks Google's AI Overview 'best plumber near me' or ChatGPT 'top-rated Italian restaurant in Austin,' the businesses cited are selected from a complex set of local authority signals. Lumo's GEO-integrated local SEO ensures your business is cited in AI-generated local recommendations.",
        "services_h2": "Our Local SEO Services",
        "services": [
            ("📍", "Google Business Profile Management", "Complete GBP optimisation and ongoing management — category selection, service areas, photo strategy, post scheduling, Q&A management, and attribute optimisation for maximum map pack visibility."),
            ("📋", "Local Citation Building", "Consistent NAP (Name, Address, Phone) citations across 80+ high-authority local directories — Yelp, BBB, Foursquare, Apple Maps, Bing Places, and industry-specific directories relevant to your business type."),
            ("⭐", "Review Generation & Management", "A systematic, ethical review generation process that increases your Google review count and star rating — plus professional response management for every review, positive or negative."),
            ("📝", "Local Content & Landing Pages", "City-targeted service pages, neighbourhood content, and locally-relevant blog posts that rank for geo-specific keywords and build topical authority in your service area."),
            ("🔗", "Local Link Building", "High-quality local backlinks from city-relevant sources — local news, chamber of commerce, sponsorships, community organisations, and local business associations."),
            ("📊", "Local Rank Tracking & Reporting", "Weekly rank tracking for your target keywords across your service area — including Map Pack positions, organic local rankings, and call/direction request tracking from your GBP."),
        ],
        "process": [
            ("🔎", "Local SEO Audit", "We audit your GBP, existing citations, competitor rankings, review profile, and local content gaps — identifying exactly what's holding you back from the top 3."),
            ("⚙️", "GBP & Citation Optimization", "Immediate GBP improvements and citation cleanup: fix NAP inconsistencies, add missing directories, optimise categories, and upload geo-tagged photos."),
            ("📈", "Content & Links", "Build local landing pages, target neighborhood-level keywords, and acquire local backlinks from city-relevant authoritative sources."),
            ("📊", "Monitor & Report", "Weekly rank tracking with Map Pack geo-grid reports — showing your local ranking across your entire service area, not just one city center point."),
        ],
        "price_from": "$1,200",
        "price_note": "per month — GBP management + citation building + rank tracking + monthly reporting",
        "faqs": [
            ("How long does local SEO take to show results?", "Most businesses see Google Business Profile ranking improvements within 30–60 days. Map Pack top-3 rankings for competitive keywords typically take 60–90 days. Organic local search rankings for longer-tail terms can improve within 30 days of publishing optimised local content."),
            ("What's the difference between local SEO and regular SEO?", "Local SEO focuses specifically on ranking in Google Maps, the local pack, and geo-specific search results — driven by Google Business Profile signals, local citations, review velocity, and proximity. Regular (organic) SEO focuses on blue-link rankings for broader keywords. Both matter for local businesses — Lumo optimises both in parallel."),
            ("How important are Google reviews for local SEO?", "Critical. Review count, average star rating, and review recency are all direct ranking signals in Google's local algorithm. Businesses with 50+ recent 4.5★+ reviews consistently outrank competitors with fewer reviews — regardless of other factors. Lumo's review generation system typically triples review velocity within 60 days."),
            ("Do you manage Google Business Profile for multiple locations?", "Yes. Lumo manages multi-location GBP portfolios — with individual optimisation strategies for each location, separate local citation profiles, and location-specific content. Each location needs its own local signals to rank independently in its market."),
            ("What is a local citation and why does it matter?", "A local citation is any online mention of your business name, address, and phone number (NAP). Consistency across 80+ directories signals trustworthiness to Google and contributes to local pack rankings. Inconsistent citations — different phone numbers, old addresses — actively harm local rankings. Lumo audits and fixes all citation inconsistencies."),
        ],
        "cta_h2": "Ready to Own the Map Pack in Your Market?",
        "cta_sub": "Book a free local SEO audit — we'll analyse your GBP, citation profile, and competitor rankings and show you exactly what it takes to reach the top 3.",
        "schema_service_name": "Local SEO Services",
        "schema_service_desc": "Local SEO strategy for US businesses — Google Business Profile management, citation building, review generation, and map pack ranking optimization.",
    },

    "reputation-management": {
        "title_tag":  "Reputation Management Agency | Control Your Online Story | Lumo AI",
        "meta_desc":  "Online reputation management from Lumo AI Agency. Review generation, negative content suppression, brand monitoring, and crisis response for US businesses. Protect and grow your reputation. Free audit.",
        "canonical":  "https://lumoaiagency.com/services/reputation-management",
        "og_title":   "Online Reputation Management | Lumo AI Agency",
        "og_desc":    "Take control of what people find when they search your brand. Lumo builds review profiles, suppresses negative content, and monitors your online reputation 24/7. Free reputation audit.",
        "h1_html":    "Reputation Management That <span class=\"hl-lime\">Builds Trust</span> at Scale",
        "badge":      "ORM Specialists",
        "lead":       "Your reputation is your most valuable marketing asset. Lumo builds and protects it — generating genuine reviews, monitoring every mention, and suppressing negative content before it costs you business.",
        "stat1_num": "4.7★", "stat1_lbl": "Average star rating achieved within 90 days",
        "stat2_num": "63%",  "stat2_lbl": "Of consumers check reviews before a purchase",
        "stat3_num": "90d",  "stat3_lbl": "Average reputation transformation timeline",
        "why_h2": "Why Your Online Reputation Determines Your Revenue",
        "why_p1": "93% of consumers say online reviews influence their purchase decisions. A business with a 3.5★ rating loses up to 70% of potential customers to competitors with 4.5★+. In markets where your competitors have similar services and prices, your online reputation is often the deciding factor — and most businesses manage it reactively, if at all.",
        "why_p2": "Online reputation management is no longer just about responding to negative reviews. In 2026, AI search tools summarise your reputation — ChatGPT and Perplexity pull review sentiment, news mentions, and brand signals when recommending businesses. Lumo builds an AI-visible reputation that converts on every platform where buyers research.",
        "why_p3": "Lumo's approach is proactive, not reactive. We build systematic review generation processes, monitor 50+ platforms for brand mentions, create positive content that outranks negative results, and develop crisis response protocols — so your reputation is an asset you control rather than a liability that controls you.",
        "services_h2": "Our Reputation Management Services",
        "services": [
            ("⭐", "Review Generation Campaigns", "Ethical, automated review request systems — post-purchase email and SMS sequences, QR code review cards, and in-person request scripts that consistently drive 4★+ reviews on Google, Yelp, Trustpilot, and industry-specific platforms."),
            ("👁️", "Brand Monitoring & Alerts", "24/7 monitoring across Google, Yelp, social media, news, forums, and review platforms — with real-time alerts for any new mentions so nothing slips through unnoticed."),
            ("💬", "Review Response Management", "Professional, on-brand responses to every review — positive and negative — that demonstrate exceptional service and convert browsers into buyers. All responses written and published within 24 hours."),
            ("📉", "Negative Content Suppression", "SEO-driven content strategy that creates and ranks positive brand content — pushing negative reviews, articles, or social posts off the first page of search results for your brand name."),
            ("🚨", "Crisis Response", "Rapid-response protocols for reputation emergencies — coordinated content publishing, review platform reporting, PR outreach, and escalation management when your brand faces a serious threat."),
            ("📊", "Reputation Reporting", "Monthly reputation health reports — star rating trends, review velocity, sentiment analysis, and share of voice across platforms — with ROI attribution tied to conversion uplift."),
        ],
        "process": [
            ("🔎", "Reputation Audit", "We audit your current reputation across 50+ platforms — star ratings, review volume, sentiment breakdown, negative content ranking, and competitive comparison."),
            ("📋", "Strategy & Playbook", "Custom reputation roadmap: review generation system setup, monitoring configuration, response templates, and suppression content plan tailored to your business and industry."),
            ("🚀", "Execute & Build", "Launch review campaigns, publish positive brand content, set up monitoring alerts, and begin proactive review response management."),
            ("📊", "Monitor & Report", "Ongoing monitoring, response management, and monthly reputation health reporting — with strategy adjustments as your reputation evolves."),
        ],
        "price_from": "$1,000",
        "price_note": "per month — monitoring + review generation + response management + monthly reporting",
        "faqs": [
            ("Can you remove negative reviews from Google?", "Google only removes reviews that violate its policies (fake reviews, spam, off-topic content, conflicts of interest). Lumo reports policy-violating reviews for removal and has a strong track record of successful removals. For legitimate negative reviews that don't violate policies, our strategy focuses on generating high-volume positive reviews that dilute their impact, and responding professionally to demonstrate service quality."),
            ("How long does reputation management take to show results?", "Review velocity improvements typically appear within 30 days as our automated systems begin generating new reviews. Star rating improvements follow within 60–90 days as positive volume accumulates. Negative content suppression (pushing bad results off page one) takes 3–6 months depending on the content's age and authority."),
            ("What review platforms does Lumo manage?", "Lumo manages Google, Yelp, Trustpilot, Facebook, BBB, Glassdoor, G2, Capterra, Houzz, TripAdvisor, Healthgrades, Zocdoc, and industry-specific platforms relevant to your business. The platform mix is customised to where your customers actually research."),
            ("How does Lumo generate reviews ethically?", "Lumo uses post-transaction email and SMS sequences, QR code-triggered review requests, and in-person request scripts — all compliant with Google's and other platforms' guidelines. We never incentivise reviews with discounts or payments, and never use fake or manufactured reviews. The system works by making it easy for genuinely satisfied customers to leave reviews they would have left anyway."),
            ("What happens during a reputation crisis?", "Lumo's crisis response protocol activates within 2 hours of a major reputation event. We coordinate immediate review platform reporting (if applicable), draft and publish an official response, identify and suppress damaging content in search results, and escalate to PR partners if media coverage is involved. Every Lumo reputation management client has a crisis playbook prepared before it's needed."),
        ],
        "cta_h2": "Ready to Take Control of Your Reputation?",
        "cta_sub": "Book a free reputation audit — we'll show you exactly how your brand appears online and what it's costing you in lost customers.",
        "schema_service_name": "Online Reputation Management Services",
        "schema_service_desc": "Online reputation management for US businesses — review generation, brand monitoring, negative content suppression, and crisis response.",
    },

    "link-building": {
        "title_tag":  "Link Building Agency | High-Authority Backlinks That Move Rankings | Lumo AI",
        "meta_desc":  "White-hat link building from Lumo AI Agency. Digital PR, guest posting, niche edits, and HARO outreach that earn DR50+ backlinks and build domain authority. Free link audit.",
        "canonical":  "https://lumoaiagency.com/services/link-building",
        "og_title":   "Link Building Agency | Lumo AI Agency",
        "og_desc":    "Earn high-authority backlinks that move rankings. Lumo's link building team delivers DR50+ placements through Digital PR, guest posting, and white-hat outreach. Free audit.",
        "h1_html":    "Link Building That <span class=\"hl-lime\">Moves Rankings</span> Not Just Metrics",
        "badge":      "Link Building Specialists",
        "lead":       "Backlinks are still the strongest ranking signal. But most agencies chase volume over quality. Lumo builds fewer, higher-authority links — from real publications that Google trusts — that compound into durable first-page rankings.",
        "stat1_num": "DR55+", "stat1_lbl": "Average Domain Rating of placements",
        "stat2_num": "100%",  "stat2_lbl": "White-hat, manual outreach — no PBNs ever",
        "stat3_num": "2.8x",  "stat3_lbl": "Average domain authority growth in 6 months",
        "why_h2": "Why Link Building Still Determines Who Ranks on Page One",
        "why_p1": "Google's own engineers have repeatedly confirmed that links remain one of the top three ranking signals. In competitive industries, the difference between position 1 and position 5 is almost always authority — and authority comes from the quality and quantity of sites linking to you. Content alone won't bridge that gap.",
        "why_p2": "The problem is that most 'link building' services are either low-quality (PBNs, link farms, paid links) or ineffective (directory submissions, random guest posts). These approaches worked in 2015 — in 2026, they're either irrelevant or actively risky. Lumo builds links the only sustainable way: earning them through real content, digital PR, and manual relationship-based outreach.",
        "why_p3": "In the AI search era, backlinks serve double duty. High-authority links increase your Google rankings AND signal to AI systems that your content is trustworthy enough to cite. Lumo's link building strategy is calibrated for both traditional search and AI citation visibility — future-proofing your domain authority investment.",
        "services_h2": "Our Link Building Services",
        "services": [
            ("📰", "Digital PR & Media Placements", "Pitch your brand's data, expertise, and stories to journalists at Forbes, Inc., Entrepreneur, and industry publications — earning editorial backlinks that carry the highest authority and are immune to Google penalties."),
            ("✍️", "Guest Posting", "Strategic guest posts on vetted, topically relevant DR40–70 sites in your niche — real editorial sites with real traffic, not link farms dressed up as blogs."),
            ("🔗", "Niche Edit Placements", "Contextual link insertions into existing, indexed articles on high-authority sites — often faster to place than guest posts and highly effective for targeting specific keyword gaps."),
            ("📣", "HARO & Journalist Outreach", "Respond to journalist queries (Help A Reporter Out, Qwoted, Featured) to earn citations in major publications — building both backlinks and brand authority simultaneously."),
            ("🔍", "Competitor Gap Analysis", "Identify every high-value site linking to your top 3 competitors but not to you — then systematically pursue placements on those exact domains."),
            ("💔", "Broken Link Building", "Find broken links on authoritative sites in your niche, create or identify matching content on your site, and contact site owners to replace the dead link with yours."),
        ],
        "process": [
            ("🔎", "Backlink Audit", "Analyse your current link profile — domain authority distribution, toxic link identification, competitor gap map, and quick-win opportunities that can be pursued immediately."),
            ("🎯", "Target Prospect List", "Build a vetted list of 100+ link prospects monthly — scored by DR, topical relevance, traffic, and likelihood of placement — so every outreach effort is efficient."),
            ("📧", "Outreach & Placement", "Manual, personalised outreach campaigns — no templates, no mass emailing. Real relationship-based pitching that earns placements on sites that actually matter."),
            ("📊", "Report & Compound", "Monthly link placement reports with DR, traffic, and anchor text data — and ongoing strategy refinement to compound your authority gains over time."),
        ],
        "price_from": "$1,500",
        "price_note": "per month — 5–10 DR50+ placements guaranteed monthly",
        "faqs": [
            ("How many backlinks do I need to rank?", "There's no universal number — it depends on your industry competition. Lumo starts with a gap analysis: how many DR50+ links do your top-ranking competitors have vs. you? That gap, combined with link velocity modeling, tells us exactly how many links you need and how long it will take to close the gap."),
            ("Are guest posts risky after Google's link spam updates?", "Guest posts on genuine, editorially-controlled sites with real traffic are not risky. Guest posts on sites that exist only for link selling are. Lumo's guest post vetting process includes traffic verification, editorial control check, and niche relevance scoring — we only place on sites Google sees as legitimate publications."),
            ("Do you use PBNs (Private Blog Networks)?", "Never. PBNs are high-risk link schemes that can result in manual penalties and deindexation. Lumo uses only white-hat, manual outreach methods. Every link we build could be scrutinised by a Google quality rater — and would pass."),
            ("How long does link building take to impact rankings?", "Individual link placements typically impact rankings within 4–8 weeks as Google crawls and processes the new links. The cumulative effect of a sustained link building campaign usually becomes visible in rankings at the 3–4 month mark, with compounding growth continuing beyond that."),
            ("Can you build links for a new website?", "Yes, but the strategy is different. New sites need foundational links first — local citations, business directories, industry associations — before moving to high-DR editorial placements. Lumo builds a phased link acquisition plan appropriate for your domain's current authority level."),
        ],
        "cta_h2": "Ready to Build Authority That Lasts?",
        "cta_sub": "Get a free backlink audit — we'll analyse your link profile, map your competitor gap, and show you exactly which placements will move your rankings.",
        "schema_service_name": "Link Building Services",
        "schema_service_desc": "White-hat link building for US businesses — digital PR, guest posting, niche edits, and HARO outreach earning DR50+ backlinks that build lasting domain authority.",
    },

    "google-local-services-ads": {
        "title_tag":  "Google Local Services Ads Management | Pay Per Lead, Not Per Click | Lumo AI",
        "meta_desc":  "Google Local Services Ads management from Lumo AI Agency. Get the Google Screened badge, pay only per verified lead, and dominate above-the-fold local search. Free LSA setup consultation.",
        "canonical":  "https://lumoaiagency.com/services/google-local-services-ads",
        "og_title":   "Google Local Services Ads | Lumo AI Agency",
        "og_desc":    "Google Local Services Ads appear above everything else in local search — and you only pay when a lead calls or messages. Lumo manages your LSA campaigns for maximum verified leads.",
        "h1_html":    "Google Local Services Ads That <span class=\"hl-lime\">Pay Per Lead</span>, Not Per Click",
        "badge":      "Google LSA Specialists",
        "lead":       "Google Local Services Ads appear above paid search, above organic — right at the top of every local search. And unlike Google Ads, you only pay when a real customer calls or messages you. Lumo sets up, verifies, and manages your LSA campaigns for maximum lead volume at minimum cost.",
        "stat1_num": "$18",  "stat1_lbl": "Average cost-per-lead across LSA campaigns",
        "stat2_num": "2.3x", "stat2_lbl": "Higher CTR vs. standard Google Search Ads",
        "stat3_num": "5.4x", "stat3_lbl": "Average ROAS for Lumo-managed LSA accounts",
        "why_h2": "Why Google Local Services Ads Are the Highest-ROI Local Ad Format",
        "why_p1": "Google Local Services Ads (LSAs) appear above everything else in local search results — above Google Ads, above the Map Pack, above organic results. When someone searches 'plumber near me' or 'electrician Austin TX,' your LSA listing with the Google Screened or Google Guaranteed badge is the first thing they see. The click-through rates are 2–3x higher than standard ads.",
        "why_p2": "The pay-per-lead model is what makes LSAs truly unique. Unlike Google Ads where you pay for every click whether or not it converts, LSAs charge only when a customer actually calls or messages your business. That means no wasted budget on irrelevant clicks, no paying for people who bounce immediately — only genuine leads who actively chose to contact you.",
        "why_p3": "The Google Screened and Google Guaranteed badges that appear on LSA listings carry enormous trust weight with consumers. Businesses with these badges see significantly higher lead-to-conversion rates because prospects know Google has verified the business's licenses and insurance. Lumo handles the full verification process and ongoing badge maintenance.",
        "services_h2": "Our Google Local Services Ads Management",
        "services": [
            ("✅", "LSA Setup & Verification", "End-to-end LSA account creation, business category selection, service area configuration, and Google verification process — including license verification, insurance documentation, and background check coordination."),
            ("🥇", "Google Screened Badge", "Full support through the Google Screened or Google Guaranteed verification process — the badge that increases lead conversion rates by demonstrating Google-verified trustworthiness."),
            ("💰", "Bid Strategy & Budget Management", "Weekly bid optimisation for lead volume and cost efficiency — adjusting bids by service type, day of week, and time of day to maximise lead volume within your budget."),
            ("📞", "Lead Quality Management", "Review and dispute low-quality or irrelevant leads (wrong service area, wrong service type) with Google — recovering budget on leads that don't meet your criteria."),
            ("🔍", "Category & Service Optimization", "Ongoing refinement of your service categories, job types, and service areas to maximise reach for high-value job types while filtering out low-value lead categories."),
            ("📊", "LSA Reporting & Attribution", "Monthly reporting on lead volume, cost-per-lead, lead type breakdown, and booking conversion rate — with recommendations for improving your lead quality score."),
        ],
        "process": [
            ("📋", "Setup & Verify", "Create your LSA account, complete the Google verification process, configure service areas and categories, and obtain your Google Screened or Guaranteed badge."),
            ("🚀", "Launch & Calibrate", "Go live with initial bids and monitor lead quality for the first 2 weeks — adjusting categories and service areas based on actual lead data."),
            ("⚙️", "Optimize", "Weekly bid adjustments, lead dispute management, category refinement, and review generation to maximise your lead quality score and ad position."),
            ("📊", "Report & Scale", "Monthly performance reports with lead volume, CPL trends, and ROI data — with budget recommendations as we identify the highest-performing job categories."),
        ],
        "price_from": "$750",
        "price_note": "per month management fee — LSA ad spend is separate and goes directly to Google",
        "faqs": [
            ("What is the difference between Google Local Services Ads and Google Ads?", "Google Ads (Search) charges per click and appears below LSAs in search results. Google Local Services Ads appear above everything else, charge per verified lead (not per click), and require Google verification. For local service businesses, LSAs typically deliver lower cost-per-lead and higher-quality leads than standard Google Ads — Lumo recommends running both in most cases."),
            ("Which businesses are eligible for Google Local Services Ads?", "LSAs are available for a wide range of local service businesses including: home services (plumbers, HVAC, electricians, cleaners, locksmiths, roofers, landscapers), professional services (lawyers, financial advisors, tax preparers), real estate agents, healthcare providers, and more. Lumo checks your eligibility in the free consultation."),
            ("How much does it cost to run Google Local Services Ads?", "LSA costs vary by industry and market. Average costs range from $8–$15 per lead for home services in less competitive markets to $30–$80 per lead for legal and financial services in major metros. Lumo's $750/mo management fee is separate from ad spend, which goes directly to Google. We provide a CPL estimate for your specific category and market in the free consultation."),
            ("How does Google verify my business for LSA?", "Google verifies your business through a combination of: license verification (submitting your contractor license or professional certification), insurance verification (uploading your liability insurance certificate), and background check (for the business owner and employees in some categories). The process takes 1–4 weeks. Lumo guides you through every step."),
            ("Can I dispute leads I don't think I should pay for?", "Yes. LSAs have a dispute process for leads that don't meet your criteria — wrong service area, wrong service type, spam calls, etc. Lumo actively monitors your lead feed and disputes low-quality leads on your behalf, recovering budget that shouldn't have been charged."),
        ],
        "cta_h2": "Ready to Start Getting Leads, Not Just Clicks?",
        "cta_sub": "Book a free LSA consultation — we'll check your eligibility, estimate your cost-per-lead, and walk you through exactly how Local Services Ads work for your business.",
        "schema_service_name": "Google Local Services Ads Management",
        "schema_service_desc": "Google Local Services Ads setup, verification, and management for US local service businesses — pay-per-lead advertising with Google Screened and Guaranteed badge management.",
    },
}

# ---------------------------------------------------------------------------
# SHARED FOOTER (1 level deep: services/*.html → ../)
# ---------------------------------------------------------------------------
FOOTER_HTML = """\
<footer role="contentinfo">
  <div class="footer-inner">
    <div class="footer-top">
      <div class="footer-brand">
        <a href="../index.html" class="footer-logo" aria-label="Lumo AI Agency home">Lumo<span>.</span></a>
        <p class="footer-tagline">Austin's AI-powered marketing agency. SEO, paid ads, AI automation &amp; web design built for the future.</p>
        <div class="footer-socials">
          <a href="https://instagram.com/lumoaiagency" class="social-link" target="_blank" rel="noopener noreferrer" aria-label="Instagram">&#9679;</a>
          <a href="https://linkedin.com/company/lumoaiagency" class="social-link" target="_blank" rel="noopener noreferrer" aria-label="LinkedIn">in</a>
          <a href="https://twitter.com/lumoaiagency" class="social-link" target="_blank" rel="noopener noreferrer" aria-label="X">&#120143;</a>
        </div>
      </div>
      <div class="footer-col">
        <h4>Services</h4>
        <ul>
          <li><a href="../services/seo.html">SEO</a></li>
          <li><a href="../services/geo.html">GEO / AI Search</a></li>
          <li><a href="../services/google-ads.html">Google Ads</a></li>
          <li><a href="../services/meta-ads.html">Meta Ads</a></li>
          <li><a href="../services/technical-seo.html">Technical SEO</a></li>
          <li><a href="../services/local-seo.html">Local SEO</a></li>
          <li><a href="../services/link-building.html">Link Building</a></li>
          <li><a href="../services/reputation-management.html">Reputation Mgmt</a></li>
          <li><a href="../services/ecommerce-seo.html">E-commerce SEO</a></li>
          <li><a href="../services/cro.html">CRO</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h4>Industries</h4>
        <ul>
          <li><a href="../industries/seo-for-lawyers/">Law Firms</a></li>
          <li><a href="../industries/seo-for-dentists/">Dentists</a></li>
          <li><a href="../industries/digital-marketing-for-real-estate/">Real Estate</a></li>
          <li><a href="../industries/healthcare-seo/">Healthcare</a></li>
          <li><a href="../industries/ecommerce-marketing/">E-commerce</a></li>
          <li><a href="../industries/saas-marketing/">SaaS &amp; Tech</a></li>
          <li><a href="../industries/home-services-seo/">Home Services</a></li>
          <li><a href="../industries/construction-marketing/">Construction</a></li>
          <li><a href="../industries/fitness-gym-marketing/">Fitness &amp; Gyms</a></li>
          <li><a href="../industries/hospitality-marketing/">Hotels</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h4>Compare</h4>
        <ul>
          <li><a href="../compare/lumo-vs-webfx/">Lumo vs WebFX</a></li>
          <li><a href="../compare/lumo-vs-thrive-agency/">Lumo vs Thrive</a></li>
          <li><a href="../compare/lumo-vs-np-digital/">Lumo vs NP Digital</a></li>
          <li><a href="../compare/lumo-vs-ignite-digital/">Lumo vs Ignite</a></li>
          <li><a href="../compare/lumo-vs-disruptive-advertising/">Lumo vs Disruptive</a></li>
          <li><a href="../compare/lumo-vs-smartsites/">Lumo vs SmartSites</a></li>
        </ul>
        <h4 style="margin-top:24px">Company</h4>
        <ul>
          <li><a href="../about.html">About Us</a></li>
          <li><a href="../services.html">All Services</a></li>
          <li><a href="../pricing.html">Pricing</a></li>
          <li><a href="../contact.html">Contact</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <span class="footer-copy">&copy; 2026 Lumo AI Agency. All rights reserved.</span>
      <div class="footer-bl">
        <a href="../privacy-policy.html">Privacy Policy</a>
        <a href="../terms.html">Terms of Service</a>
      </div>
    </div>
  </div>
</footer>"""

# ---------------------------------------------------------------------------
# CSS
# ---------------------------------------------------------------------------
CSS = """    :root{--bg:#0D0D14;--bg-card:#13131F;--bg-dark:#09090F;--primary:#B3FF00;--secondary:#7C3AED;--accent:#00F5FF;--text:#F0F0FF;--muted:#6B7280;--border:rgba(179,255,0,0.15);--glow-lime:0 0 30px rgba(179,255,0,0.35);--radius-sm:8px;--radius:14px;--radius-lg:20px;--transition:0.25s cubic-bezier(0.4,0,0.2,1);}
    *,*::before,*::after{box-sizing:border-box;margin:0;padding:0;}
    html{scroll-behavior:smooth;-webkit-font-smoothing:antialiased;}
    body{font-family:'Inter',system-ui,sans-serif;background:var(--bg);color:var(--text);overflow-x:hidden;line-height:1.6;}
    h1,h2,h3,h4{font-family:'Syne',sans-serif;line-height:1.15;}
    a{color:inherit;text-decoration:none;}
    ul{list-style:none;}
    .container{max-width:1180px;margin:0 auto;padding:0 24px;}
    .section-pad{padding:100px 0;}
    .btn{display:inline-flex;align-items:center;gap:8px;padding:14px 30px;border-radius:50px;font-weight:700;font-size:0.95rem;transition:var(--transition);white-space:nowrap;}
    .btn-lime{background:var(--primary);color:#0D0D14;}
    .btn-lime:hover{background:#c8ff26;transform:translateY(-2px);box-shadow:0 8px 30px rgba(179,255,0,0.45);}
    .btn-ghost{background:transparent;color:var(--text);border:1.5px solid rgba(240,240,255,0.2);}
    .btn-ghost:hover{border-color:var(--primary);color:var(--primary);transform:translateY(-2px);}
    #navbar{position:fixed;top:0;left:0;right:0;z-index:900;background:rgba(13,13,20,0.85);backdrop-filter:blur(16px);border-bottom:1px solid rgba(179,255,0,0.06);transition:background .3s,border-color .3s;}
    #navbar.scrolled{background:rgba(13,13,20,0.97);border-bottom-color:rgba(179,255,0,0.12);}
    .nav-inner{display:flex;align-items:center;justify-content:space-between;height:68px;max-width:1180px;margin:0 auto;padding:0 24px;}
    .nav-logo{font-family:'Berkshire Swash',serif;font-size:1.6rem;color:var(--primary);letter-spacing:-0.01em;text-shadow:0 0 20px rgba(179,255,0,0.4);}
    .nav-links{display:flex;align-items:center;gap:36px;}
    .nav-links a{font-size:0.88rem;font-weight:500;color:var(--muted);transition:color var(--transition);}
    .nav-links a:hover,.nav-links a.active{color:var(--primary);}
    .nav-cta{display:flex;align-items:center;gap:16px;}
    .nav-hamburger{display:none;flex-direction:column;gap:5px;padding:8px;cursor:pointer;}
    .nav-hamburger span{display:block;width:24px;height:2px;background:var(--text);border-radius:2px;transition:var(--transition);}
    .mobile-menu{display:none;flex-direction:column;background:rgba(13,13,20,0.98);border-top:1px solid var(--border);padding:8px 24px 16px;}
    .mobile-menu.open{display:flex;}
    .mobile-menu a{padding:14px 0;border-bottom:1px solid rgba(255,255,255,0.05);color:var(--muted);font-size:0.95rem;font-weight:500;transition:color var(--transition);}
    .mobile-menu a:hover{color:var(--primary);}
    @media(max-width:768px){.nav-links,.nav-cta{display:none;}.nav-hamburger{display:flex;}}
    .page-hero{padding:140px 0 80px;position:relative;overflow:hidden;}
    .blob-wrap{position:absolute;inset:0;pointer-events:none;overflow:hidden;}
    .blob{position:absolute;border-radius:50%;filter:blur(80px);}
    .blob-lime{width:500px;height:500px;background:radial-gradient(circle,rgba(179,255,0,0.18) 0%,transparent 70%);top:-80px;left:-80px;animation:drift-a 18s ease-in-out infinite;}
    .blob-violet{width:400px;height:400px;background:radial-gradient(circle,rgba(124,58,237,0.15) 0%,transparent 70%);bottom:0;right:-60px;animation:drift-b 22s ease-in-out infinite;}
    @keyframes drift-a{0%,100%{transform:translate(0,0) scale(1);}50%{transform:translate(60px,50px) scale(1.08);}}
    @keyframes drift-b{0%,100%{transform:translate(0,0) scale(1);}50%{transform:translate(-50px,-40px) scale(1.06);}}
    .hero-noise{position:absolute;inset:0;background-image:linear-gradient(rgba(179,255,0,0.02) 1px,transparent 1px),linear-gradient(90deg,rgba(179,255,0,0.02) 1px,transparent 1px);background-size:60px 60px;pointer-events:none;}
    .page-hero-inner{position:relative;z-index:2;}
    .breadcrumb{display:flex;align-items:center;gap:8px;font-size:0.8rem;color:var(--muted);margin-bottom:28px;}
    .breadcrumb a:hover{color:var(--primary);}
    .breadcrumb-sep{color:rgba(179,255,0,0.3);}
    .hero-badge{display:inline-flex;align-items:center;gap:8px;padding:7px 16px;border:1px solid var(--primary);border-radius:50px;font-size:0.78rem;font-weight:600;color:var(--primary);letter-spacing:0.06em;text-transform:uppercase;background:rgba(179,255,0,0.06);margin-bottom:24px;}
    .page-hero h1{font-family:'Syne',sans-serif;font-size:clamp(2.8rem,6vw,5rem);color:var(--text);line-height:1.08;margin-bottom:24px;}
    .hl-lime{color:var(--primary);text-shadow:0 0 30px rgba(179,255,0,0.45);}
    .page-hero p.lead{font-size:1.1rem;color:var(--muted);max-width:620px;margin-bottom:36px;}
    .hero-btns{display:flex;gap:14px;flex-wrap:wrap;}
    .stats-strip{background:var(--bg-dark);border-top:1px solid rgba(179,255,0,0.06);border-bottom:1px solid rgba(179,255,0,0.06);}
    .stats-row{display:grid;grid-template-columns:repeat(3,1fr);}
    .stat-item{padding:50px 40px;text-align:center;position:relative;}
    .stat-item:not(:last-child)::after{content:'';position:absolute;right:0;top:25%;bottom:25%;width:1px;background:rgba(179,255,0,0.08);}
    .stat-num{font-size:clamp(2.2rem,3.5vw,3rem);font-weight:900;color:var(--primary);line-height:1;text-shadow:0 0 20px rgba(179,255,0,0.3);}
    .stat-label{font-size:0.82rem;color:var(--muted);margin-top:8px;font-weight:500;}
    @media(max-width:600px){.stats-row{grid-template-columns:1fr;}.stat-item::after{display:none;}.stat-item{padding:32px 24px;}}
    .section-eyebrow{display:inline-flex;align-items:center;gap:8px;font-size:0.72rem;font-weight:700;letter-spacing:0.12em;text-transform:uppercase;color:var(--primary);margin-bottom:16px;}
    .section-eyebrow::before{content:'';display:block;width:24px;height:2px;background:var(--primary);border-radius:2px;}
    .section-h2{font-family:'Syne',sans-serif;font-size:clamp(2rem,4.5vw,3.2rem);color:var(--text);margin-bottom:16px;}
    .section-sub{color:var(--muted);font-size:1rem;max-width:620px;margin-bottom:56px;}
    .why-grid{display:grid;grid-template-columns:1fr 1fr;gap:40px;align-items:start;}
    @media(max-width:860px){.why-grid{grid-template-columns:1fr;}}
    .why-text p{color:var(--muted);font-size:0.95rem;line-height:1.8;margin-bottom:16px;}
    .why-card{background:var(--bg-card);border:1px solid var(--border);border-radius:var(--radius-lg);padding:32px;}
    .why-card h3{font-size:1.1rem;color:var(--primary);margin-bottom:16px;}
    .why-card ul{display:flex;flex-direction:column;gap:10px;}
    .why-card li{font-size:0.88rem;color:var(--muted);padding-left:20px;position:relative;}
    .why-card li::before{content:'→';position:absolute;left:0;color:var(--primary);}
    .svc-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:20px;}
    @media(max-width:900px){.svc-grid{grid-template-columns:1fr 1fr;}}
    @media(max-width:560px){.svc-grid{grid-template-columns:1fr;}}
    .svc-card{background:var(--bg-card);border:1px solid rgba(255,255,255,0.05);border-radius:var(--radius);padding:28px 24px;transition:border-color .25s,transform .25s,box-shadow .25s;}
    .svc-card:hover{border-color:rgba(179,255,0,0.3);transform:translateY(-4px);box-shadow:0 12px 40px rgba(179,255,0,0.08);}
    .svc-icon{font-size:1.6rem;margin-bottom:14px;}
    .svc-title{font-size:1rem;font-weight:700;color:var(--text);margin-bottom:10px;}
    .svc-desc{font-size:0.84rem;color:var(--muted);line-height:1.65;}
    .process-bg{background:var(--bg-dark);}
    .process-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:20px;}
    @media(max-width:768px){.process-grid{grid-template-columns:1fr 1fr;}}
    @media(max-width:460px){.process-grid{grid-template-columns:1fr;}}
    .step-card{background:var(--bg-card);border:1px solid rgba(255,255,255,0.05);border-radius:var(--radius);padding:28px 20px;text-align:center;transition:border-color .28s,transform .28s;}
    .step-card:hover{border-color:rgba(0,245,255,0.3);transform:translateY(-4px);}
    .step-num{width:52px;height:52px;border-radius:50%;background:rgba(179,255,0,0.1);border:2px solid rgba(179,255,0,0.35);display:flex;align-items:center;justify-content:center;font-size:1rem;font-weight:800;color:var(--primary);margin:0 auto 16px;}
    .step-icon{font-size:1.4rem;margin-bottom:10px;}
    .step-title{font-size:0.95rem;font-weight:700;color:var(--text);margin-bottom:8px;}
    .step-desc{font-size:0.82rem;color:var(--muted);line-height:1.6;}
    .pricing-box{background:var(--bg-card);border:1px solid var(--border);border-radius:var(--radius-lg);padding:48px;text-align:center;max-width:620px;margin:0 auto;}
    .pricing-box h3{font-size:1.6rem;color:var(--text);margin-bottom:10px;}
    .price-from{font-size:clamp(3rem,5vw,4rem);font-weight:900;color:var(--primary);line-height:1;text-shadow:0 0 24px rgba(179,255,0,0.3);margin:16px 0 8px;}
    .price-note{font-size:0.88rem;color:var(--muted);margin-bottom:28px;}
    #faq{background:var(--bg-dark);}
    .faq-wrap{max-width:820px;margin:0 auto;}
    .faq-item{border-bottom:1px solid rgba(255,255,255,0.06);}
    .faq-item:first-child{border-top:1px solid rgba(255,255,255,0.06);}
    .faq-q{display:flex;justify-content:space-between;align-items:center;padding:22px 0;cursor:pointer;gap:16px;}
    .faq-q-text{font-size:0.98rem;font-weight:600;color:var(--text);}
    .faq-icon{width:28px;height:28px;border-radius:8px;background:rgba(179,255,0,0.08);border:1px solid rgba(179,255,0,0.2);display:flex;align-items:center;justify-content:center;flex-shrink:0;transition:transform .25s,background .25s;}
    .faq-item.open .faq-icon{transform:rotate(45deg);background:rgba(179,255,0,0.18);}
    .faq-a{max-height:0;overflow:hidden;transition:max-height .35s ease;}
    .faq-a p{font-size:0.9rem;color:var(--muted);line-height:1.75;padding-bottom:20px;}
    .faq-item.open .faq-a{max-height:500px;}
    .cta-band{background:linear-gradient(135deg,rgba(179,255,0,0.04) 0%,rgba(124,58,237,0.06) 100%);border-top:1px solid rgba(179,255,0,0.08);text-align:center;padding:100px 0;}
    .cta-band h2{font-family:'Syne',sans-serif;font-size:clamp(2rem,4vw,3.2rem);margin-bottom:20px;}
    .cta-band p{color:var(--muted);font-size:1rem;max-width:520px;margin:0 auto 36px;}
    .cta-btns{display:flex;gap:14px;justify-content:center;flex-wrap:wrap;}
    footer{background:var(--bg-dark);border-top:1px solid rgba(179,255,0,0.08);padding:60px 0 30px;}
    .footer-inner{max-width:1180px;margin:0 auto;padding:0 24px;}
    .footer-top{display:grid;grid-template-columns:1.4fr 1fr 1fr 1fr;gap:48px;margin-bottom:48px;}
    .footer-brand .footer-logo{font-family:'Berkshire Swash',serif;font-size:1.5rem;color:var(--primary);display:inline-block;margin-bottom:16px;}
    .footer-tagline{font-size:0.85rem;color:var(--muted);line-height:1.7;margin-bottom:24px;}
    .footer-socials{display:flex;gap:10px;}
    .social-link{width:38px;height:38px;border-radius:10px;background:rgba(124,58,237,0.12);border:1px solid rgba(124,58,237,0.25);display:flex;align-items:center;justify-content:center;color:var(--secondary);font-size:0.9rem;font-weight:700;transition:background .25s,border-color .25s,transform .25s;}
    .social-link:hover{background:rgba(124,58,237,0.25);border-color:var(--secondary);transform:translateY(-3px);color:#fff;}
    .footer-col h4{font-size:0.78rem;font-weight:700;letter-spacing:0.1em;text-transform:uppercase;color:var(--text);margin-bottom:20px;}
    .footer-col ul{display:flex;flex-direction:column;gap:10px;}
    .footer-col a{font-size:0.85rem;color:var(--muted);transition:color .22s;}
    .footer-col a:hover{color:var(--primary);}
    .footer-bottom{border-top:1px solid rgba(255,255,255,0.06);padding-top:24px;display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:12px;}
    .footer-copy{font-size:0.8rem;color:var(--muted);}
    .footer-bl{display:flex;gap:24px;}
    .footer-bl a{color:var(--primary);font-size:0.8rem;}
    #scroll-top{position:fixed;bottom:30px;right:30px;width:46px;height:46px;border-radius:12px;background:var(--primary);color:#0D0D14;display:flex;align-items:center;justify-content:center;cursor:pointer;z-index:800;opacity:0;transform:translateY(10px);transition:opacity .3s,transform .3s;border:none;}
    #scroll-top.visible{opacity:1;transform:translateY(0);}
    #scroll-top:hover{box-shadow:0 0 20px rgba(179,255,0,0.5);transform:translateY(-3px);}
    @media(max-width:900px){.footer-top{grid-template-columns:1fr 1fr;}}
    @media(max-width:560px){.footer-top{grid-template-columns:1fr;gap:32px;}.footer-bottom{flex-direction:column;text-align:center;}.footer-bl{flex-direction:column;gap:10px;align-items:center;}}"""

JS = """  const nav=document.getElementById('navbar');
  const st=document.getElementById('scroll-top');
  window.addEventListener('scroll',()=>{
    nav.classList.toggle('scrolled',window.scrollY>40);
    st.classList.toggle('visible',window.scrollY>300);
  });
  const hamburger=document.querySelector('.nav-hamburger');
  const mobileMenu=document.getElementById('mobile-menu');
  if(hamburger){hamburger.addEventListener('click',()=>{
    const open=mobileMenu.classList.toggle('open');
    hamburger.setAttribute('aria-expanded',open);
  });}
  st.addEventListener('click',()=>window.scrollTo({top:0,behavior:'smooth'}));
  document.querySelectorAll('.faq-q').forEach(q=>{
    q.addEventListener('click',()=>{
      const item=q.parentElement;
      item.classList.toggle('open');
    });
  });"""

def build_page(slug, d):
    services_cards = ""
    for icon, title, desc in d["services"]:
        services_cards += f"""      <div class="svc-card">
        <div class="svc-icon">{icon}</div>
        <div class="svc-title">{title}</div>
        <div class="svc-desc">{desc}</div>
      </div>\n"""

    process_steps = ""
    for i, (icon, title, desc) in enumerate(d["process"], 1):
        process_steps += f"""      <div class="step-card">
        <div class="step-num">{i:02d}</div>
        <div class="step-icon">{icon}</div>
        <div class="step-title">{title}</div>
        <div class="step-desc">{desc}</div>
      </div>\n"""

    faq_items = ""
    schema_faqs = []
    for q, a in d["faqs"]:
        faq_items += f"""    <div class="faq-item">
      <div class="faq-q" role="button" tabindex="0" aria-expanded="false">
        <span class="faq-q-text">{q}</span>
        <span class="faq-icon" aria-hidden="true">
          <svg width="12" height="12" viewBox="0 0 12 12" fill="none">
            <line x1="6" y1="0" x2="6" y2="12" stroke="currentColor" stroke-width="2"/>
            <line x1="0" y1="6" x2="12" y2="6" stroke="currentColor" stroke-width="2"/>
          </svg>
        </span>
      </div>
      <div class="faq-a"><p>{a}</p></div>
    </div>\n"""
        schema_faqs.append({"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}})

    schema = {
        "@context":"https://schema.org",
        "@graph":[
            {
                "@type":"WebPage",
                "@id": d["canonical"],
                "url": d["canonical"],
                "name": d["title_tag"],
                "description": d["meta_desc"],
                "breadcrumb":{
                    "@type":"BreadcrumbList",
                    "itemListElement":[
                        {"@type":"ListItem","position":1,"name":"Home","item":"https://lumoaiagency.com/"},
                        {"@type":"ListItem","position":2,"name":"Services","item":"https://lumoaiagency.com/services.html"},
                        {"@type":"ListItem","position":3,"name":d["schema_service_name"],"item":d["canonical"]},
                    ]
                }
            },
            {
                "@type":"Service",
                "name": d["schema_service_name"],
                "description": d["schema_service_desc"],
                "provider":{"@type":"LocalBusiness","name":"Lumo AI Agency","url":"https://lumoaiagency.com"},
                "areaServed":{"@type":"Country","name":"United States"},
                "serviceType": d["schema_service_name"],
            },
            {
                "@type":"FAQPage",
                "mainEntity": schema_faqs
            }
        ]
    }

    return f"""<!DOCTYPE html>
<html lang="en-US">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <meta name="description" content="{d['meta_desc']}" />
  <meta name="robots" content="index, follow" />
  <meta property="og:type" content="website" />
  <meta property="og:title" content="{d['og_title']}" />
  <meta property="og:description" content="{d['og_desc']}" />
  <meta property="og:url" content="{d['canonical']}" />
  <link rel="canonical" href="{d['canonical']}" />
  <title>{d['title_tag']}</title>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Berkshire+Swash&family=Inter:wght@400;500;600;700;900&family=Syne:wght@700;800&display=swap" rel="stylesheet" />
  <script type="application/ld+json">{json.dumps(schema, ensure_ascii=False)}</script>
  <style>
{CSS}
  </style>
</head>
<body>

<!-- NAVBAR -->
<nav id="navbar" role="navigation" aria-label="Main navigation">
  <div class="nav-inner">
    <a href="../index.html" class="nav-logo" aria-label="Lumo AI Agency home">Lumo<span style="color:#B3FF00">.</span></a>
    <div class="nav-links">
      <a href="../index.html">Home</a>
      <a href="../services.html" class="active">Services</a>
      <a href="../industries/seo-for-lawyers/">Industries</a>
      <a href="../about.html">About</a>
      <a href="../pricing.html">Pricing</a>
    </div>
    <div class="nav-cta">
      <a href="../contact.html" class="btn btn-lime" style="padding:10px 22px;font-size:0.85rem;">Get Started</a>
    </div>
    <button class="nav-hamburger" aria-label="Open menu" aria-expanded="false" aria-controls="mobile-menu">
      <span></span><span></span><span></span>
    </button>
  </div>
  <div class="mobile-menu" id="mobile-menu" role="menu">
    <a href="../index.html" role="menuitem">Home</a>
    <a href="../services.html" role="menuitem">Services</a>
    <a href="../about.html" role="menuitem">About</a>
    <a href="../pricing.html" role="menuitem">Pricing</a>
    <a href="../contact.html" role="menuitem">Get Started</a>
  </div>
</nav>

<!-- HERO -->
<section class="page-hero">
  <div class="blob-wrap">
    <div class="blob blob-lime"></div>
    <div class="blob blob-violet"></div>
  </div>
  <div class="hero-noise"></div>
  <div class="container page-hero-inner">
    <nav class="breadcrumb" aria-label="Breadcrumb">
      <a href="../index.html">Home</a>
      <span class="breadcrumb-sep">›</span>
      <a href="../services.html">Services</a>
      <span class="breadcrumb-sep">›</span>
      <span>{d['schema_service_name']}</span>
    </nav>
    <div class="hero-badge">{d['badge']}</div>
    <h1>{d['h1_html']}</h1>
    <p class="lead">{d['lead']}</p>
    <div class="hero-btns">
      <a href="../contact.html" class="btn btn-lime">Get a Free Audit</a>
      <a href="../pricing.html" class="btn btn-ghost">View Pricing</a>
    </div>
  </div>
</section>

<!-- STATS -->
<section class="stats-strip" aria-label="Key metrics">
  <div class="stats-row">
    <div class="stat-item">
      <div class="stat-num">{d['stat1_num']}</div>
      <div class="stat-label">{d['stat1_lbl']}</div>
    </div>
    <div class="stat-item">
      <div class="stat-num">{d['stat2_num']}</div>
      <div class="stat-label">{d['stat2_lbl']}</div>
    </div>
    <div class="stat-item">
      <div class="stat-num">{d['stat3_num']}</div>
      <div class="stat-label">{d['stat3_lbl']}</div>
    </div>
  </div>
</section>

<!-- WHY -->
<section class="section-pad">
  <div class="container">
    <div class="why-grid">
      <div class="why-text">
        <div class="section-eyebrow">Why It Matters</div>
        <h2 class="section-h2">{d['why_h2']}</h2>
        <p>{d['why_p1']}</p>
        <p>{d['why_p2']}</p>
        <p>{d['why_p3']}</p>
      </div>
      <div class="why-card">
        <h3>What You Get With Lumo</h3>
        <ul>
          <li>Dedicated account strategist</li>
          <li>Monthly performance reports</li>
          <li>Transparent pricing — no hidden fees</li>
          <li>No long-term lock-in contracts</li>
          <li>AI-integrated strategy across every service</li>
          <li>GEO optimisation included as standard</li>
          <li>Results tied to your revenue goals</li>
        </ul>
      </div>
    </div>
  </div>
</section>

<!-- SERVICES -->
<section class="section-pad process-bg">
  <div class="container">
    <div class="section-eyebrow">What We Do</div>
    <h2 class="section-h2">{d['services_h2']}</h2>
    <p class="section-sub">Every deliverable is tracked, reported, and tied to business outcomes — not just activity metrics.</p>
    <div class="svc-grid">
{services_cards}    </div>
  </div>
</section>

<!-- PROCESS -->
<section class="section-pad">
  <div class="container">
    <div class="section-eyebrow">How We Work</div>
    <h2 class="section-h2">Our Process</h2>
    <p class="section-sub">A clear four-step process from first conversation to measurable results.</p>
    <div class="process-grid">
{process_steps}    </div>
  </div>
</section>

<!-- PRICING -->
<section class="section-pad process-bg">
  <div class="container">
    <div class="section-eyebrow">Investment</div>
    <h2 class="section-h2" style="text-align:center;margin-bottom:40px;">Simple, Transparent Pricing</h2>
    <div class="pricing-box">
      <h3>{d['schema_service_name']}</h3>
      <div class="price-from">Starting at {d['price_from']}<span style="font-size:1.2rem;font-weight:400">/mo</span></div>
      <p class="price-note">{d['price_note']}</p>
      <a href="../contact.html" class="btn btn-lime">Get a Custom Quote</a>
    </div>
  </div>
</section>

<!-- FAQ -->
<section id="faq" class="section-pad">
  <div class="container">
    <div class="section-eyebrow">FAQ</div>
    <h2 class="section-h2" style="text-align:center;margin-bottom:48px;">Common Questions</h2>
    <div class="faq-wrap">
{faq_items}    </div>
  </div>
</section>

<!-- CTA -->
<section class="cta-band">
  <div class="container">
    <h2>{d['cta_h2']}</h2>
    <p>{d['cta_sub']}</p>
    <div class="cta-btns">
      <a href="../contact.html" class="btn btn-lime">Get a Free Audit</a>
      <a href="../pricing.html" class="btn btn-ghost">View Pricing</a>
    </div>
  </div>
</section>

{FOOTER_HTML}

<button id="scroll-top" aria-label="Back to top">
  <svg width="16" height="16" viewBox="0 0 16 16" fill="none">
    <path d="M8 12V4M4 8l4-4 4 4" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
  </svg>
</button>

<script>
{JS}
</script>
</body>
</html>"""


for slug, data in SERVICES.items():
    html = build_page(slug, data)
    path = os.path.join(BASE, f"{slug}.html")
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Created: services/{slug}.html ({len(html):,} chars)")

print(f"\nDone. {len(SERVICES)} pages created.")
