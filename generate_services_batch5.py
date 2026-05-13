#!/usr/bin/env python3
"""Wave 3 — Batch 5:
   enterprise-seo, franchise-seo, b2b-seo, international-seo,
   app-store-optimization
"""
import os, json

BASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "services")
os.makedirs(BASE, exist_ok=True)

SERVICES = {

    "enterprise-seo": {
        "title_tag":  "Enterprise SEO Agency | Large-Scale SEO for Complex Sites | Lumo AI",
        "meta_desc":  "Enterprise SEO services from Lumo AI Agency. Technical SEO at scale, site architecture strategy, content programmes, and international SEO for large US businesses. Free enterprise audit.",
        "canonical":  "https://lumoaiagency.com/services/enterprise-seo",
        "og_title":   "Enterprise SEO Agency | Lumo AI Agency",
        "og_desc":    "Enterprise-grade SEO for large, complex websites. Lumo manages technical SEO at scale, content architecture, international expansion, and cross-team coordination for Fortune 1000 and high-growth brands.",
        "h1_html":    "Enterprise SEO That Scales <span class=\"hl-lime\">Organic Revenue</span> Across Complex Sites",
        "badge":      "Enterprise SEO Specialists",
        "lead":       "Enterprise SEO is not SMB SEO at higher volume — it's a fundamentally different discipline. JavaScript rendering, crawl budget management, site architecture across thousands of URLs, cross-team stakeholder alignment, and content at scale require enterprise-grade strategy. Lumo delivers it.",
        "stat1_num": "53%", "stat1_lbl": "Of B2B enterprise buying journeys start with organic search",
        "stat2_num": "8x",  "stat2_lbl": "More organic traffic for enterprises with mature SEO programs",
        "stat3_num": "$1M+","stat3_lbl": "Average monthly organic revenue for Lumo enterprise clients",
        "why_h2": "Why Enterprise SEO Requires a Different Approach",
        "why_p1": "Enterprise websites face challenges that don't exist at smaller scale: JavaScript rendering across tens of thousands of product pages, crawl budget allocation across complex site architectures, duplicate content management across regional and language variants, and content governance across departments that create content independently. Standard SMB SEO approaches don't solve these problems.",
        "why_p2": "Stakeholder management is as important as technical execution in enterprise SEO. Changes to site architecture require engineering resources. Content strategy requires coordination with product, legal, and brand teams. International expansion involves regional market managers. Lumo builds enterprise SEO programs with internal change management, stakeholder communication frameworks, and technical implementation playbooks that get changes implemented — not just recommended.",
        "why_p3": "Lumo's enterprise SEO practice is built on a foundation of technical depth combined with commercial acumen. We connect organic performance to revenue through robust attribution modelling, forecast organic traffic impact of architectural decisions, and build quarterly roadmaps that prioritise initiatives by revenue potential — not just SEO impact. Our clients speak our language because we speak theirs.",
        "services_h2": "Our Enterprise SEO Services",
        "services": [
            ("🏗️", "Site Architecture Strategy", "Large-scale site architecture audits and redesign strategy — URL structure, category hierarchy, internal link architecture, crawl budget optimisation, and content silo design for sites with 10,000+ pages."),
            ("⚙️", "Technical SEO at Scale", "JavaScript SEO and rendering audits, server log analysis, crawl budget management, Core Web Vitals at scale, structured data implementation across dynamic templates, and canonical/hreflang management."),
            ("📝", "Enterprise Content Strategy", "Topical authority content architecture, content cluster design, content governance frameworks, editorial calendar management, and content performance measurement across large publishing operations."),
            ("🔗", "Digital PR & Authority Building", "Enterprise-scale link acquisition through digital PR campaigns, brand mention monitoring, competitor backlink analysis, and editorial relationship building with top-tier publications."),
            ("🌐", "International & Multilingual SEO", "hreflang implementation, regional site architecture, international keyword research, country-level technical SEO, and content localisation strategy for US businesses expanding internationally."),
            ("📊", "SEO Analytics & Forecasting", "Custom enterprise SEO dashboards, organic revenue attribution, share-of-voice tracking, search demand forecasting, and quarterly business review reporting for C-suite and board presentations."),
        ],
        "process": [
            ("🔍", "Enterprise Audit", "Comprehensive technical audit, content gap analysis, backlink profile review, competitive landscape mapping, and stakeholder interviews — producing a prioritised opportunity roadmap with revenue impact estimates."),
            ("🏗️", "Architecture & Strategy", "Site architecture redesign recommendations, content strategy framework, technical SEO implementation plan, and internal linking strategy — with engineering-ready specifications for each recommendation."),
            ("⚙️", "Implementation & Governance", "Technical SEO deployment support, content programme launch, link acquisition campaign execution, and cross-team coordination — with monthly check-ins and quarterly strategy reviews."),
            ("📈", "Measure & Optimise", "Organic revenue reporting, share-of-voice monitoring, search visibility tracking, and strategic roadmap updates — connecting SEO performance to business outcomes at every reporting cycle."),
        ],
        "price_from": "$5,000",
        "price_note": "per month — enterprise engagements typically $8,000–$20,000/mo depending on site scale and scope",
        "faqs": [
            ("What defines 'enterprise' SEO in your context?", "Lumo considers a site enterprise-scale when it has 10,000+ indexable URLs, operates in multiple geographic markets or languages, has significant JavaScript rendering requirements, or requires cross-departmental coordination for SEO implementation. The common characteristic is that SEO changes require engineering resources and stakeholder alignment — not just content updates."),
            ("How does enterprise SEO differ from standard SEO?", "Standard SEO focuses on page-level optimisation, content creation, and link building for sites where one person can implement changes directly. Enterprise SEO adds site architecture strategy, crawl budget management, JavaScript rendering audits, hreflang implementation, content governance across teams, and change management across engineering and product organisations. The technical depth and stakeholder complexity are categorically different."),
            ("How long before we see results from enterprise SEO?", "Enterprise SEO improvements often have longer implementation timelines because changes require engineering resources and deployment cycles. That said, technical fixes (crawl issues, rendering problems, Core Web Vitals) can show traffic impact within 4–8 weeks of implementation. Content and authority building programmes typically show meaningful compounding results at the 6–12 month mark, with enterprise-scale impact visible at 12–18 months."),
            ("Do you work with in-house SEO teams?", "Yes — many Lumo enterprise clients have in-house SEO teams. In these cases, Lumo functions as a strategic partner and specialist resource: providing technical SEO depth, content strategy architecture, and link acquisition capabilities that complement in-house resources. We define the collaboration model in the onboarding phase to ensure clear ownership and avoid duplication."),
            ("Can you integrate with our existing analytics and reporting stack?", "Yes. Lumo can deliver reporting through your existing BI tools, data warehouses, or dashboarding platforms (Tableau, Looker, Google Data Studio, Power BI) rather than requiring you to log in to a separate platform. We can also work with your data engineering team to set up organic data pipelines and custom attribution models within your existing analytics infrastructure."),
        ],
        "cta_h2": "Ready to Build an Enterprise SEO Program That Drives Revenue at Scale?",
        "cta_sub": "Get a free enterprise SEO audit — we'll assess your site architecture, technical health, content strategy, and competitive position, then map the highest-impact opportunities for your organisation.",
        "schema_service_name": "Enterprise SEO Services",
        "schema_service_desc": "Enterprise-grade SEO for large US businesses — site architecture strategy, technical SEO at scale, content programs, international SEO, and organic revenue attribution.",
    },

    "franchise-seo": {
        "title_tag":  "Franchise SEO Agency | Multi-Location SEO That Drives Leads | Lumo AI",
        "meta_desc":  "Franchise SEO services from Lumo AI Agency. Multi-location SEO, franchise location pages, GBP management, and brand-consistent local optimisation at scale. Free franchise SEO audit.",
        "canonical":  "https://lumoaiagency.com/services/franchise-seo",
        "og_title":   "Franchise SEO Agency | Lumo AI Agency",
        "og_desc":    "SEO built for franchise networks. Lumo manages brand-level and location-level SEO — franchise location pages, GBP profiles, local citations, and content at scale — for US franchise brands.",
        "h1_html":    "Franchise SEO That Grows Every <span class=\"hl-lime\">Location's</span> Organic Leads",
        "badge":      "Franchise SEO Specialists",
        "lead":       "Franchise SEO requires balancing national brand authority with hyper-local relevance for each location. Lumo builds franchise SEO programs that generate leads for every location — through optimised location pages, Google Business Profile management, and local SEO at scale — without sacrificing brand consistency.",
        "stat1_num": "46%",  "stat1_lbl": "Of all Google searches have local intent",
        "stat2_num": "78%",  "stat2_lbl": "Of local mobile searches lead to in-store visits within 24h",
        "stat3_num": "350%", "stat3_lbl": "Average organic lead growth for Lumo franchise clients",
        "why_h2": "Why Franchise SEO Is More Complex Than Single-Location SEO",
        "why_p1": "Franchise SEO has a fundamental tension: national brand authority requires consistent brand signals across all locations, while local SEO requires uniquely optimised content for each location's specific market. Handle this wrong and you end up with duplicate content penalties (identical location pages), weak local signals (no location-specific authority), or brand inconsistency (franchisees creating their own off-brand profiles).",
        "why_p2": "Google Business Profile management at franchise scale introduces another layer of complexity. Each location needs its own GBP, optimised with location-specific hours, photos, services, and review management — while remaining consistent with brand guidelines. Managing 50+ GBP profiles without a systematic approach leads to incomplete profiles, outdated information, and missed local ranking opportunities.",
        "why_p3": "Lumo builds franchise SEO systems that solve both problems simultaneously. Our location page templates generate unique, location-specific content at scale — local landmarks, service area details, location-specific FAQs, and local schema — while maintaining brand-consistent structure and messaging. GBP management is systemised across all locations with centralised monitoring and local execution.",
        "services_h2": "Our Franchise SEO Services",
        "services": [
            ("📍", "Location Page Creation & Optimisation", "SEO-optimised location pages for every franchise location — unique content per location (not duplicate templates), local keyword targeting, schema markup, and internal linking to national brand authority pages."),
            ("🗺️", "Google Business Profile Management", "GBP setup, optimisation, and ongoing management for every franchise location — complete profiles, photo management, post scheduling, Q&A management, and review response across all locations."),
            ("⭐", "Franchise Review Management", "Systematic review generation programs for each location, review response management at scale, and brand reputation monitoring — maintaining rating standards across the franchise network."),
            ("🔗", "Local Citation Building", "NAP consistency across directories (Yelp, YellowPages, Bing Places, Apple Maps) for every franchise location — building local authority signals for each market independently."),
            ("📝", "Local Content Strategy", "Location-specific content creation — local blog posts, area guides, community partnership content — that builds genuine local relevance for each franchise market beyond location page boilerplate."),
            ("📊", "Franchise SEO Reporting", "Brand-level and location-level reporting dashboards — organic traffic, ranking positions, GBP insights, and lead attribution per location — giving franchisors visibility across the network."),
        ],
        "process": [
            ("🔍", "Network Audit", "Audit all existing location pages, GBP profiles, citation consistency, and review health across the franchise network — identifying gaps, inconsistencies, and highest-priority locations."),
            ("🏗️", "System & Template Design", "Design location page template system, GBP management workflow, review generation program, and reporting infrastructure — built for scale across your full franchise network."),
            ("🚀", "Network Rollout", "Systematic deployment across all franchise locations — prioritised by market opportunity — with training for local operators and centralised quality control from the franchisor team."),
            ("📈", "Monitor & Optimise", "Monthly performance reporting per location, GBP insights analysis, review health monitoring, and content updates — with quarterly network-wide strategy reviews and new location onboarding."),
        ],
        "price_from": "$2,500",
        "price_note": "per month for up to 10 locations — additional locations at $150–$250/location/month",
        "faqs": [
            ("How do you handle duplicate content across franchise location pages?", "Lumo builds location page systems with a dynamic content architecture that generates unique page content per location — not just swapping the city name in a template. This includes location-specific statistics, service area descriptions, local landmarks, location-specific testimonials, and unique FAQ content per market. Every location page passes Copyscape duplication checks."),
            ("Should franchise locations have their own social media and GBP profiles?", "Yes — separate GBP profiles for each location are essential for local SEO. Social media is a more nuanced decision that depends on your franchise model. We recommend a brand-controlled GBP for each location (rather than franchisee-managed) to ensure consistency and brand protection, while social strategy is customised based on whether franchisees have resources for local social management."),
            ("Can you manage franchise SEO while individual franchisees also do their own marketing?", "Yes — this is common. Lumo establishes brand-level SEO guidelines and manages national and location-level SEO assets, while local franchisees manage paid advertising or social media independently. We create brand guidelines and training materials for franchisees to ensure local marketing activities complement rather than conflict with the national SEO strategy."),
            ("How long does it take to roll out SEO across a 50-location franchise network?", "A 50-location rollout — including location page creation, GBP optimisation, and citation building — typically takes 8–12 weeks for full deployment. We prioritise locations by market opportunity (search volume, competition level) and deploy in phases, so high-opportunity markets benefit from optimisation quickly rather than waiting for the entire network to be complete."),
            ("Do you work with the franchisor, franchisees, or both?", "Lumo works primarily with the franchisor (or their marketing team) to ensure brand-consistent SEO standards across the network. Where franchisees have local marketing autonomy, we provide guidelines, training, and reporting access so local operators can see their location's performance. All strategic decisions are made at the franchisor level to protect brand equity."),
        ],
        "cta_h2": "Ready to Grow Organic Leads Across Every Franchise Location?",
        "cta_sub": "Get a free franchise SEO audit — we'll assess your location page quality, GBP profiles, citation consistency, and review health across your network, then show you the revenue opportunity in organic search.",
        "schema_service_name": "Franchise SEO Services",
        "schema_service_desc": "Multi-location franchise SEO for US franchise brands — location pages, GBP management, local citations, review management, and network-wide reporting at scale.",
    },

    "b2b-seo": {
        "title_tag":  "B2B SEO Agency | Organic Lead Generation for B2B Companies | Lumo AI",
        "meta_desc":  "B2B SEO services from Lumo AI Agency. Organic lead generation, content strategy for long buying cycles, technical SEO, and account-based content for B2B companies. Free B2B SEO audit.",
        "canonical":  "https://lumoaiagency.com/services/b2b-seo",
        "og_title":   "B2B SEO Agency | Lumo AI Agency",
        "og_desc":    "SEO built for B2B buying cycles. Lumo drives qualified organic pipeline for B2B companies — through buyer-journey content, technical SEO, and authority building that converts researchers into leads.",
        "h1_html":    "B2B SEO That Generates <span class=\"hl-lime\">Qualified Pipeline</span>, Not Just Traffic",
        "badge":      "B2B SEO Specialists",
        "lead":       "B2B buyers conduct 12+ digital touchpoints before engaging sales. Lumo builds B2B SEO programs that intercept buyers at every stage of a complex, multi-stakeholder purchase cycle — through technical SEO, buyer-journey content, and authority signals that make your brand the default choice before the first sales call.",
        "stat1_num": "71%", "stat1_lbl": "Of B2B buyers start with generic Google searches",
        "stat2_num": "12+", "stat2_lbl": "Average digital touchpoints before B2B purchase decision",
        "stat3_num": "57%", "stat3_lbl": "Of purchase decision made before first sales contact",
        "why_h2": "Why B2B SEO Is Different From B2C SEO",
        "why_p1": "B2B SEO serves a fundamentally different buyer journey. B2C buyers make purchase decisions in minutes or hours. B2B buyers conduct research over weeks or months, involve multiple stakeholders, require education before evaluation, and make decisions worth tens or hundreds of thousands of dollars. The content strategy, keyword targeting, and conversion architecture required to capture this buying process is entirely different from e-commerce or consumer SEO.",
        "why_p2": "B2B keyword research requires understanding how buyers actually search — not just what they search for. A CFO and a CTO researching your software product search differently. A VP of Marketing and a Director of Marketing ask different questions and need different types of content. B2B SEO maps content to specific buyer personas at each stage of their research process — creating a path from first search to MQL.",
        "why_p3": "Lumo's B2B SEO programs focus on pipeline quality, not just traffic volume. We track organic-attributed MQLs, SQLs, and closed revenue — not just rankings and sessions. Our content strategy is built around your ideal customer profile, with content that attracts buyers you can close, not researchers who will never buy. Every content decision is evaluated against its expected pipeline contribution.",
        "services_h2": "Our B2B SEO Services",
        "services": [
            ("🎯", "Buyer Persona Keyword Research", "ICP-driven keyword research mapping search behaviour to buyer personas, job roles, and decision stages — identifying high-intent queries that attract buyers with authority and budget, not just general researchers."),
            ("📝", "Buyer-Journey Content Strategy", "Content architecture mapping awareness, consideration, and decision-stage content — thought leadership, comparison guides, ROI calculators, case studies, and solution pages that move prospects through the funnel."),
            ("⚙️", "Technical B2B SEO", "Technical SEO for B2B site architectures — solution pages, product category structure, integration pages, customer story organisation, and technical SEO for gated content and lead capture flows."),
            ("🔗", "B2B Link Building & PR", "B2B-specific digital PR and link acquisition — industry publication contributions, analyst relations, partner co-marketing links, and conference/event citation building that builds category authority."),
            ("💼", "LinkedIn & Intent Signal Integration", "Connecting B2B SEO with LinkedIn retargeting — identifying organic visitors from target accounts, building LinkedIn audiences from search-engaged prospects, and coordinating content messaging across channels."),
            ("📊", "Pipeline Attribution & Reporting", "Organic-to-MQL and organic-to-closed-revenue attribution, share-of-voice tracking, content performance by buyer stage, and monthly reporting that connects SEO investment to pipeline and revenue outcomes."),
        ],
        "process": [
            ("🔍", "ICP & Keyword Audit", "Define ideal customer profile, map buyer personas and job roles, conduct persona-specific keyword research, and audit existing content against buyer journey — identifying gaps and highest-opportunity terms."),
            ("📋", "Content Architecture", "Design buyer-journey content architecture, prioritise content by pipeline impact, create editorial calendar, and build technical SEO implementation plan for site structural improvements."),
            ("✍️", "Produce & Optimise", "Create target content by buyer stage, optimise existing pages for persona-specific keywords, build internal linking architecture, and launch link acquisition campaigns targeting B2B publications."),
            ("📈", "Measure Pipeline Impact", "Monthly reporting on organic MQLs and pipeline contribution, content performance by funnel stage, share-of-voice vs. competitors, and quarterly strategy updates based on revenue attribution data."),
        ],
        "price_from": "$3,000",
        "price_note": "per month — enterprise B2B programmes from $6,000/mo based on content volume and technical scope",
        "faqs": [
            ("How do you measure B2B SEO success when deals take months to close?", "Lumo uses a multi-stage attribution model for B2B SEO: we track organic-influenced first touch (which searches initiated the research process), organic assists (organic content consumed during evaluation), and organic-attributed closed revenue (where the first or last significant touch was organic). We also track MQL volume and quality from organic, pipeline from organic, and organic share-of-voice vs. competitors — giving you leading indicators while deals work through the cycle."),
            ("How does B2B SEO work with our existing ABM strategy?", "B2B SEO and ABM are complementary. SEO creates inbound surface area for target accounts that are already in research mode — these buyers find you through Google rather than through outbound outreach. Intent data from SEO can also inform your ABM targeting: if a company from your ICP list is consuming your SEO content, they're likely in-market. Lumo can help coordinate SEO content strategy with your ABM targeting list."),
            ("Should we focus on brand terms or non-brand keywords?", "Both, for different reasons. Brand terms protect you from competitor conquesting and capture buyers already aware of you. Non-brand terms capture the much larger pool of buyers who don't know you yet but are searching for what you do — 'enterprise data integration platform' rather than '[Your Company Name] review'. Non-brand content drives new pipeline; brand terms protect existing pipeline. Lumo allocates content resources across both based on your competitive situation."),
            ("How long does B2B SEO take to generate pipeline?", "B2B SEO is a 6–18 month investment cycle. Technical SEO fixes show traffic impact within 4–8 weeks. New content targeting competitive keywords typically takes 3–6 months to rank. Content that ranks then needs to convert — which depends on content quality, offer clarity, and conversion path design. Lumo sets realistic timelines with leading indicator targets (rankings, organic sessions, content engagement) alongside lagging pipeline metrics."),
            ("How do you handle SEO for long-tail B2B keywords with very low search volume?", "Low search volume in B2B often masks high commercial value. A query with 50 monthly searches that attracts VP-level buyers at enterprise companies may be worth more than a 5,000-search query from early-career researchers. Lumo evaluates B2B keywords by ICP fit and commercial intent, not just search volume — targeting low-volume, high-intent terms that attract qualified buyers rather than chasing traffic from terms that won't convert."),
        ],
        "cta_h2": "Ready to Build a B2B SEO Program That Generates Real Pipeline?",
        "cta_sub": "Get a free B2B SEO audit — we'll assess your current keyword position, content coverage across the buyer journey, and organic pipeline attribution, then map the highest-impact opportunities for your ICP.",
        "schema_service_name": "B2B SEO Services",
        "schema_service_desc": "Organic pipeline generation SEO for US B2B companies — buyer persona keyword research, buyer-journey content strategy, technical SEO, and pipeline attribution reporting.",
    },

    "international-seo": {
        "title_tag":  "International SEO Agency | Global SEO Strategy for US Brands | Lumo AI",
        "meta_desc":  "International SEO services from Lumo AI Agency. hreflang implementation, country-specific site architecture, multilingual content strategy, and global search visibility for US businesses expanding internationally.",
        "canonical":  "https://lumoaiagency.com/services/international-seo",
        "og_title":   "International SEO Agency | Lumo AI Agency",
        "og_desc":    "Expand globally with confidence. Lumo builds international SEO programs — hreflang, country site architecture, multilingual content strategy, and geo-targeting — for US businesses entering new markets.",
        "h1_html":    "International SEO That Opens <span class=\"hl-lime\">New Markets</span> Through Organic Search",
        "badge":      "International SEO Specialists",
        "lead":       "Expanding into international markets without proper SEO architecture creates compounding technical debt that limits organic growth for years. Lumo builds international SEO programs from the foundation — hreflang, URL structure, content localisation, and market-specific keyword research — that position US businesses to win organic market share globally.",
        "stat1_num": "75%", "stat1_lbl": "Of internet users make purchases in their native language",
        "stat2_num": "60%", "stat2_lbl": "Of Google searches happen outside the United States",
        "stat3_num": "3x",  "stat3_lbl": "Higher conversion rates from localised vs. translated content",
        "why_h2": "Why International SEO Is More Than Just Translation",
        "why_p1": "The most common international SEO failure is treating expansion as a translation project: take the US site, translate it into Spanish or French, host it somewhere, and expect it to rank. This approach produces sites that are technically broken for international search (no hreflang, wrong canonical configuration, IP-based geo-detection conflicts) and commercially ineffective (translated copy that doesn't reflect local market culture, pricing, or buyer behaviour).",
        "why_p2": "International SEO requires architectural decisions that are expensive to change later: ccTLD vs. subdomain vs. subdirectory structure, hreflang implementation across all language/region variants, server location and CDN configuration for local speed signals, and country-specific Google Search Console property management. Getting these decisions wrong at launch creates technical debt that constrains your international organic growth for years.",
        "why_p3": "Lumo approaches international SEO as a market-entry strategy, not a technical implementation project. We research each target market's search landscape — which keywords matter, how competitors structure their sites, what content formats perform locally — before making technical architecture recommendations. The result is an international SEO foundation built around your specific target markets, not generic global best practices.",
        "services_h2": "Our International SEO Services",
        "services": [
            ("🌐", "International Site Architecture", "Country/language targeting strategy — ccTLD vs. subdomain vs. subdirectory analysis, URL structure design, hreflang implementation plan, and technical architecture specification for international expansion."),
            ("🏷️", "hreflang Implementation & Audit", "Correct hreflang tag implementation across all language and region variants, return tag verification, canonical tag alignment, and XML sitemap configuration for international URL sets."),
            ("🔍", "Market-Specific Keyword Research", "Country-level keyword research in target languages — not translation of US terms, but native-language research identifying actual search behaviour in each target market."),
            ("📝", "Content Localisation Strategy", "Localisation beyond translation — adapting content for local market context, cultural references, pricing formats, regulations, and buyer expectations that make content genuinely relevant to local audiences."),
            ("📍", "Geo-Targeting Configuration", "Google Search Console international targeting configuration, IP-based vs. hreflang-based targeting strategy, CDN and server configuration for local performance signals, and geo-redirect architecture."),
            ("📊", "International SEO Reporting", "Market-level organic performance reporting — traffic, rankings, and conversion by country — with competitive share-of-voice tracking for each target market independently."),
        ],
        "process": [
            ("🗺️", "Market Research & Architecture", "Target market analysis, competitor landscape per country, site architecture recommendations, hreflang strategy, and technical specification — agreed before any implementation begins."),
            ("🏗️", "Technical Implementation", "hreflang deployment, URL structure implementation, GSC international property setup, XML sitemap update, and crawl verification — ensuring correct technical signals for all target markets."),
            ("📝", "Content & Localisation", "Market-specific keyword research, content gap analysis per country, localisation of priority pages, and new content creation for highest-opportunity market-specific terms."),
            ("📈", "Monitor & Expand", "Monthly reporting per market, ranking tracking in local Google variants, international content expansion, and new market entry support as your global presence grows."),
        ],
        "price_from": "$3,500",
        "price_note": "per month for up to 3 target markets — additional markets from $800/market/month",
        "faqs": [
            ("Should we use ccTLDs, subdomains, or subdirectories for international SEO?", "This is the most consequential international SEO architecture decision. ccTLDs (example.co.uk) give the strongest local signal but require building domain authority separately for each country. Subdomains (uk.example.com) are easier to manage but Google treats them somewhat independently. Subdirectories (example.com/uk/) leverage your main domain's authority and are easiest to manage — but give a weaker local signal. Lumo recommends based on your domain authority, budget, and market priority."),
            ("What is hreflang and why does it matter?", "hreflang is the HTML attribute that tells Google which language and country variant of a page to show users in different locations. Without hreflang, Google may show US-English users your French-language pages, or show French users your US site — creating a poor user experience that damages both rankings and conversion. Hreflang implementation is complex (requiring return tags on every variant) and commonly misconfigured — Lumo audits and corrects hreflang as a priority."),
            ("Is content localisation different from translation?", "Significantly. Translation converts words from one language to another. Localisation adapts the content for the target market — this includes cultural references, examples, case studies, pricing formats (€ not $, comma not decimal), local regulations and compliance requirements, date formats, imagery, and the tone and style that feels native to local readers. Localised content converts at 3x the rate of translated content — the investment is commercially justified."),
            ("How long does it take to rank internationally?", "International SEO follows the same timeline as new market entry in any SEO program — 6–12 months for competitive terms, faster for brand terms and lower-competition markets. Markets with strong competitors who have invested in local SEO for years take longer. Markets where competitors have weak localisation (English-only sites targeting non-English markets) offer faster organic opportunity. Lumo prioritises target markets by competitive density and opportunity."),
            ("Can you help us enter markets where Google isn't the dominant search engine?", "Yes — Lumo has experience with Baidu optimisation for China market entry, Naver for South Korea, Yandex for Russia and CIS markets, and Bing international search for markets where Microsoft has significant share. Each search engine has different technical requirements, content guidelines, and ranking signals. We provide market-specific technical guidance beyond standard Google SEO for non-Google-dominant markets."),
        ],
        "cta_h2": "Ready to Build Your International Organic Search Presence?",
        "cta_sub": "Get a free international SEO audit — we'll assess your current site architecture for international readiness, identify hreflang issues, and map the highest-opportunity target markets for organic search expansion.",
        "schema_service_name": "International SEO Services",
        "schema_service_desc": "International SEO for US businesses — hreflang implementation, country site architecture, multilingual content strategy, and market-specific organic search visibility.",
    },

    "app-store-optimization": {
        "title_tag":  "App Store Optimization Agency | ASO for iOS & Android | Lumo AI",
        "meta_desc":  "App Store Optimization (ASO) services from Lumo AI Agency. iOS and Android ASO, keyword optimisation, conversion rate optimisation, and review management for US app publishers. Free ASO audit.",
        "canonical":  "https://lumoaiagency.com/services/app-store-optimization",
        "og_title":   "App Store Optimization Agency | Lumo AI Agency",
        "og_desc":    "65% of app downloads come from App Store search. Lumo's ASO programs improve app discoverability, store page conversion, and review ratings — driving organic installs without ad spend.",
        "h1_html":    "App Store Optimization That <span class=\"hl-lime\">Drives Organic Installs</span> Without Ad Spend",
        "badge":      "ASO Specialists",
        "lead":       "65% of all app downloads start with an App Store search — yet most apps invest nothing in app store discoverability. Lumo's ASO programs optimise iOS and Android app store presence through keyword research, metadata optimisation, creative A/B testing, and review management — driving organic installs that compound over time.",
        "stat1_num": "65%", "stat1_lbl": "Of app downloads come from App Store and Play Store search",
        "stat2_num": "3.5M","stat2_lbl": "Apps competing in the App Store — discoverability is everything",
        "stat3_num": "40%", "stat3_lbl": "Increase in organic installs from professional ASO programs",
        "why_h2": "Why Most Apps Are Invisible in the App Store",
        "why_p1": "Most app publishers focus their acquisition budget on paid user acquisition — Apple Search Ads, Meta app install campaigns, Google UAC — while leaving their App Store presence unoptimised. The result is a paid acquisition ceiling: when ad spend stops, installs stop. ASO creates organic acquisition that doesn't switch off — search-driven installs that continue long after the initial optimisation investment.",
        "why_p2": "App store algorithms behave differently from web search. Keyword placement in the app title carries 3–5x the weight of keywords in the description. Screenshots and preview videos drive conversion from listing to install — a well-designed screenshot sequence can double install rates with no change to the app itself. Review velocity and rating score affect both ranking and conversion. These levers require platform-specific expertise, not general SEO skills.",
        "why_p3": "Lumo's ASO practice combines metadata optimisation with creative optimisation and review management — addressing all three components of App Store visibility simultaneously. We research keyword opportunities using store-specific tools, optimise metadata for ranking and conversion, test creative variants to improve listing-to-install rates, and manage the review response and generation program that supports rating health.",
        "services_h2": "Our App Store Optimization Services",
        "services": [
            ("🔍", "Keyword Research & Strategy", "App Store-specific keyword research — search volume, difficulty, and relevance analysis for iOS (App Store Connect) and Android (Google Play Console) — identifying the highest-opportunity terms for your app's category and target user."),
            ("📝", "Metadata Optimisation", "App title, subtitle (iOS), short description (Android), keyword field (iOS), and long description optimisation — structured for keyword coverage and conversion, within each platform's character limits and content guidelines."),
            ("🖼️", "Creative Optimisation", "Screenshot design and sequence optimisation, preview video strategy, app icon testing — A/B tested through App Store Connect and Google Play experiments to improve listing-to-install conversion rate."),
            ("⭐", "Review & Rating Management", "In-app review request timing optimisation (using native request APIs), review response management, and rating health monitoring — building the social proof that drives both conversion and algorithmic favour."),
            ("📊", "ASO Analytics & Reporting", "Store analytics interpretation — impression-to-page view, page view-to-install conversion tracking, keyword ranking movement, and competitive positioning — with monthly reports mapping ASO performance to organic install growth."),
            ("🌐", "Localisation for International Markets", "App Store metadata localisation for target international markets — keyword research in local languages, screenshot adaptation, and description localisation that expands organic reach beyond English-language search."),
        ],
        "process": [
            ("🔍", "ASO Audit & Research", "Full audit of current metadata, keyword rankings, store page creative, and review health. Keyword research for primary and secondary terms. Competitive analysis of top 10 ranked apps in your category."),
            ("📝", "Metadata & Creative Update", "Optimised metadata delivered for both platforms, screenshot redesign concepts, and App Store Connect/Play Console update — deployed with store review submission."),
            ("🧪", "A/B Testing", "Creative variant testing through native platform A/B tools — testing screenshot sequences, app icons, and preview video hooks to identify the highest-converting listing configuration."),
            ("📈", "Monitor & Expand", "Monthly keyword ranking tracking, install attribution review, review health monitoring, and iterative metadata updates as competitive landscape and algorithm signals evolve."),
        ],
        "price_from": "$1,500",
        "price_note": "per month — includes both iOS and Android optimisation, creative assets, and review management",
        "faqs": [
            ("What's the difference between ASO and SEO?", "ASO (App Store Optimization) is the app store equivalent of SEO — optimising your app's discoverability within the App Store and Google Play Store search algorithms. Both disciplines involve keyword research, metadata optimisation, and conversion optimisation, but the platforms, signals, and tools are entirely different. App store algorithms weight title keywords heavily, penalise low ratings, and respond to install velocity — signals that don't exist in web SEO."),
            ("How long does it take for ASO changes to take effect?", "Keyword ranking changes typically become visible 2–4 weeks after a metadata update on both iOS and Android platforms, as store crawlers index and reassess your listing. Creative changes (screenshot A/B tests) show conversion impact within the test period set in App Store Connect (usually 7–28 days). Review rating improvements depend on the velocity of new reviews — typically 60–90 days for meaningful rating movement."),
            ("Does ASO work for both the App Store (iOS) and Google Play (Android)?", "Yes — Lumo optimises for both platforms simultaneously, but with platform-specific strategies. iOS keyword optimisation uses the dedicated keyword field (100 characters) not visible to users, while Android optimises description text for keywords. iOS A/B testing uses App Store Connect's native testing feature; Android uses Google Play Experiments. Both platforms have different ranking algorithm weights and content policies."),
            ("How important are reviews and ratings for ASO?", "Critical. App Store and Play Store algorithms use rating and review signals in ranking — a 4.7★ app ranks higher than a 3.8★ app for the same keywords, all else equal. Reviews also affect conversion: 79% of users check ratings before downloading. Lumo optimises review generation by timing in-app native review request prompts at high-satisfaction moments, and manages responses to all reviews for brand reputation and algorithmic signals."),
            ("Can ASO reduce our reliance on paid user acquisition?", "Yes — and this is the primary commercial case for ASO investment. Paid acquisition costs are increasing across all platforms (Apple Search Ads, Google UAC, Meta). Well-executed ASO creates a growing organic install base that reduces your cost per acquisition over time. Apps in competitive categories that invest in ASO typically achieve 30–50% of their installs from organic search — significantly reducing the paid acquisition budget required to hit growth targets."),
        ],
        "cta_h2": "Ready to Grow Your App's Organic Installs?",
        "cta_sub": "Get a free ASO audit — we'll review your current keyword rankings, metadata quality, store page conversion rate, and review health, then show you the organic install opportunity for your app.",
        "schema_service_name": "App Store Optimization (ASO) Services",
        "schema_service_desc": "App Store Optimization for iOS and Android — keyword research, metadata optimisation, creative A/B testing, and review management to drive organic app installs.",
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
    nav{{position:sticky;top:0;z-index:900;background:rgba(13,13,20,.92);backdrop-filter:blur(12px);border-bottom:1px solid var(--border)}}
    .nav-inner{{max-width:1180px;margin:0 auto;padding:0 24px;height:68px;display:flex;align-items:center;justify-content:space-between}}
    .nav-logo{{font-family:'Berkshire Swash',serif;font-size:1.45rem;background:linear-gradient(135deg,var(--primary),var(--accent));-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text}}
    .nav-links{{display:flex;gap:32px;list-style:none}}
    .nav-links a{{font-size:.9rem;font-weight:500;color:var(--muted);transition:color .2s}}
    .nav-links a:hover,.nav-links a.active{{color:#fff}}
    .nav-cta .btn-lime{{background:var(--primary);color:#000;font-weight:700;font-size:.85rem;padding:10px 22px;border-radius:8px;transition:opacity .2s}}
    .nav-cta .btn-lime:hover{{opacity:.85}}
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
    .stats{{background:var(--surface);border-top:1px solid var(--border);border-bottom:1px solid var(--border);padding:48px 24px}}
    .stats-inner{{max-width:900px;margin:0 auto;display:grid;grid-template-columns:repeat(3,1fr);gap:32px;text-align:center}}
    .stat-num{{font-family:'Syne',sans-serif;font-size:2.4rem;font-weight:800;color:var(--primary)}}
    .stat-lbl{{font-size:.85rem;color:var(--muted);margin-top:6px}}
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
    .services{{padding:96px 24px;background:var(--surface)}}
    .services-inner{{max-width:1100px;margin:0 auto}}
    .section-header{{text-align:center;margin-bottom:56px}}
    .svc-grid{{display:grid;grid-template-columns:repeat(3,1fr);gap:24px}}
    .svc-card{{background:var(--bg);border:1px solid var(--border);border-radius:16px;padding:28px;transition:border-color .2s}}
    .svc-card:hover{{border-color:var(--primary)}}
    .svc-icon{{font-size:2rem;margin-bottom:16px}}
    .svc-card h3{{font-family:'Syne',sans-serif;font-size:1rem;font-weight:700;margin-bottom:10px}}
    .svc-card p{{font-size:.88rem;color:var(--muted);line-height:1.65}}
    .process{{padding:96px 24px}}
    .process-inner{{max-width:1100px;margin:0 auto}}
    .step-grid{{display:grid;grid-template-columns:repeat(4,1fr);gap:24px;margin-top:56px}}
    .step-card{{background:var(--surface);border:1px solid var(--border);border-radius:16px;padding:28px}}
    .step-num{{font-family:'Syne',sans-serif;font-size:2rem;font-weight:800;color:var(--primary);opacity:.4;line-height:1}}
    .step-icon{{font-size:1.6rem;margin:12px 0}}
    .step-card h3{{font-family:'Syne',sans-serif;font-size:.95rem;font-weight:700;margin-bottom:8px}}
    .step-card p{{font-size:.85rem;color:var(--muted);line-height:1.65}}
    .pricing{{padding:96px 24px;background:var(--surface)}}
    .pricing-inner{{max-width:520px;margin:0 auto;text-align:center}}
    .pricing-box{{background:var(--bg);border:1px solid var(--border);border-radius:20px;padding:48px 40px;margin-top:40px}}
    .price-from{{font-size:.85rem;color:var(--muted);margin-bottom:8px}}
    .price-val{{font-family:'Syne',sans-serif;font-size:3rem;font-weight:800;color:var(--primary)}}
    .price-note{{font-size:.85rem;color:var(--muted);margin-top:8px;margin-bottom:32px}}
    .faq{{padding:96px 24px}}
    .faq-inner{{max-width:760px;margin:0 auto}}
    .faq-list{{margin-top:48px;display:flex;flex-direction:column;gap:12px}}
    .faq-item{{background:var(--surface);border:1px solid var(--border);border-radius:12px;overflow:hidden}}
    .faq-q{{width:100%;background:none;border:none;color:var(--text);font-family:'Inter',sans-serif;font-size:.95rem;font-weight:600;padding:20px 24px;text-align:left;cursor:pointer;display:flex;justify-content:space-between;align-items:center;gap:16px}}
    .faq-chevron{{font-size:1.4rem;color:var(--primary);transition:transform .3s;flex-shrink:0}}
    .faq-q[aria-expanded="true"] .faq-chevron{{transform:rotate(90deg)}}
    .faq-a{{max-height:0;overflow:hidden;transition:max-height .35s ease}}
    .faq-a p{{padding:0 24px 20px;color:var(--muted);font-size:.9rem;line-height:1.7}}
    .cta-band{{padding:96px 24px;background:radial-gradient(ellipse 70% 60% at 50% 50%,rgba(124,58,237,.25) 0%,transparent 70%);text-align:center}}
    .cta-band h2{{font-family:'Syne',sans-serif;font-size:clamp(1.6rem,3vw,2.4rem);font-weight:800;margin-bottom:16px}}
    .cta-band p{{color:var(--muted);max-width:560px;margin:0 auto 40px}}
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
    .social-links{{display:flex;gap:12px;margin-top:16px}}
    .social-links a{{width:34px;height:34px;border:1px solid var(--border);border-radius:8px;display:flex;align-items:center;justify-content:center;transition:border-color .2s;flex-shrink:0}}
    .social-links a:hover{{border-color:var(--primary)}}
    .social-links svg{{width:16px;height:16px;fill:var(--muted)}}
    @media(max-width:900px){{.why-inner{{grid-template-columns:1fr}}.svc-grid{{grid-template-columns:repeat(2,1fr)}}.step-grid{{grid-template-columns:repeat(2,1fr)}}.footer-top{{grid-template-columns:1fr 1fr}}}}
    @media(max-width:600px){{.stats-inner{{grid-template-columns:1fr}}.svc-grid{{grid-template-columns:1fr}}.step-grid{{grid-template-columns:1fr}}.nav-links{{display:none}}.footer-top{{grid-template-columns:1fr}}}}
  </style>
</head>
<body>

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

<section class="stats">
  <div class="stats-inner">
    <div><div class="stat-num">{d["stat1_num"]}</div><div class="stat-lbl">{d["stat1_lbl"]}</div></div>
    <div><div class="stat-num">{d["stat2_num"]}</div><div class="stat-lbl">{d["stat2_lbl"]}</div></div>
    <div><div class="stat-num">{d["stat3_num"]}</div><div class="stat-lbl">{d["stat3_lbl"]}</div></div>
  </div>
</section>

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
        <li>AI-powered insights layer on every engagement</li>
        <li>Transparent monthly performance reports</li>
        <li>GEO optimisation built into every strategy</li>
        <li>No lock-in contracts — performance keeps you here</li>
      </ul>
    </div>
  </div>
</section>

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

<section class="faq">
  <div class="faq-inner">
    <div class="section-label" style="text-align:center">FAQ</div>
    <h2 class="section-title" style="text-align:center">Frequently Asked Questions</h2>
    <div class="faq-list">
{faq_html}
    </div>
  </div>
</section>

<section class="cta-band">
  <h2>{d["cta_h2"]}</h2>
  <p>{d["cta_sub"]}</p>
  <a href="../contact.html" class="btn-primary">Book a Free Strategy Call</a>
</section>

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
          <li><a href="../services/enterprise-seo.html">Enterprise SEO</a></li>
          <li><a href="../services/b2b-seo.html">B2B SEO</a></li>
          <li><a href="../services/franchise-seo.html">Franchise SEO</a></li>
          <li><a href="../services/international-seo.html">International SEO</a></li>
          <li><a href="../services/app-store-optimization.html">ASO</a></li>
          <li><a href="../services/technical-seo.html">Technical SEO</a></li>
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
