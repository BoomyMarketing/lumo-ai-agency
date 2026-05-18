#!/usr/bin/env python3
"""Wave 3 — Batch 2:
   programmatic-advertising, influencer-marketing, amazon-marketing,
   bing-ads, landing-pages-funnels
"""
import os, json

BASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "services")
os.makedirs(BASE, exist_ok=True)

SERVICES = {

    "programmatic-advertising": {
        "title_tag":  "Programmatic Advertising Agency | AI-Powered Display & Video | Lumo AI",
        "meta_desc":  "Programmatic advertising management from Lumo AI Agency. DSP buying, audience targeting, display, video, and CTV ads delivered with AI precision across 500B+ impressions. Free strategy call.",
        "canonical":  "https://lumoaiagency.com/services/programmatic-advertising",
        "og_title":   "Programmatic Advertising | Lumo AI Agency",
        "og_desc":    "AI-powered programmatic advertising — display, video, CTV, and audio ads delivered to exactly the right audience at exactly the right time. Free programmatic audit.",
        "h1_html":    "Programmatic Advertising <span class=\"hl-lime\">Powered by AI</span>, Not Guesswork",
        "badge":      "Programmatic Ad Specialists",
        "lead":       "Programmatic advertising buys 91% of all US digital display ads. Done right, it delivers your message to exactly the right person at the right moment — automatically, at scale. Lumo manages your programmatic strategy from DSP selection to creative optimisation.",
        "stat1_num": "91%",  "stat1_lbl": "Of US digital display is now programmatic",
        "stat2_num": "4.1x", "stat2_lbl": "Average ROAS for Lumo programmatic campaigns",
        "stat3_num": "500B+","stat3_lbl": "Impression opportunities accessed via DSP",
        "why_h2": "Why Programmatic Advertising Outperforms Traditional Display",
        "why_p1": "Traditional display advertising means buying space on specific websites at fixed prices — blind to whether your audience is actually there. Programmatic advertising flips the model: you buy audiences, not placements. AI algorithms bid in real time on individual impressions across thousands of sites, serving your ad only when the right person is present.",
        "why_p2": "The result is dramatically higher relevance and lower cost-per-acquisition. Programmatic campaigns can target by demographics, intent signals, browsing history, location, device, time of day, and hundreds of other data points simultaneously — with automatic optimisation that improves performance as the campaign learns.",
        "why_p3": "Lumo adds an AI layer on top of programmatic's native intelligence. Our audience modelling, creative rotation algorithms, and attribution tooling compound programmatic's efficiency — delivering better CPMs, higher engagement rates, and clearer ROI attribution than agencies relying on standard DSP defaults.",
        "services_h2": "Our Programmatic Advertising Services",
        "services": [
            ("🖥️", "Display Advertising", "Banner, rich media, and responsive display ads delivered across the open web via premium DSPs — with audience targeting that reaches your ideal customer wherever they browse."),
            ("🎬", "Programmatic Video", "Pre-roll, mid-roll, outstream, and in-banner video ads served programmatically across YouTube's programmatic inventory, premium publisher video, and news environments."),
            ("📺", "Connected TV (CTV) & OTT", "Unskippable 15–30 second ads served on streaming platforms — Hulu, Peacock, Tubi, and premium CTV inventory — targeting cord-cutters and streaming audiences by household."),
            ("🎯", "Audience Targeting & DMP", "First-party data activation, lookalike audience modelling, intent-based targeting, and contextual segments — building audience strategies that reach high-value prospects at scale."),
            ("🔄", "Retargeting & Sequential Messaging", "Dynamic retargeting that serves personalised ads based on specific site pages visited, products viewed, or funnel stage — with sequential creative that tells a story across multiple touchpoints."),
            ("📊", "Attribution & Reporting", "Cross-channel attribution connecting programmatic impressions to conversions, view-through analytics, frequency management, and brand safety monitoring with monthly ROI reports."),
        ],
        "process": [
            ("🎯", "Audience Strategy", "Define target audience segments, select DSP platforms, configure brand safety parameters, and map campaign objectives to bidding strategies and KPIs."),
            ("🎨", "Creative & Inventory", "Develop ad creative across sizes and formats, set up brand safety blocklists, configure viewability standards, and select premium inventory packages."),
            ("🚀", "Launch & Optimise", "Go live across DSPs with automated bidding, then apply daily optimisation — pausing underperforming placements, scaling winners, rotating creative to prevent fatigue."),
            ("📊", "Report & Scale", "Weekly performance dashboards with impression, viewability, CTR, CPC, and conversion data — with budget reallocation recommendations as audience learnings accumulate."),
        ],
        "price_from": "$2,000",
        "price_note": "per month management fee — ad spend is separate (minimum $3,000/mo recommended)",
        "faqs": [
            ("What is programmatic advertising?", "Programmatic advertising is the automated buying and selling of digital ad inventory via real-time bidding (RTB) technology. Rather than negotiating fixed placements with individual publishers, programmatic algorithms bid on individual ad impressions in milliseconds — buying impressions from your target audience across thousands of websites simultaneously at optimised prices."),
            ("Which DSPs does Lumo use?", "Lumo works across major DSPs including The Trade Desk, DV360 (Google's Display & Video 360), Amazon DSP, and MediaMath — selecting the right platform based on your campaign objectives, target audience, and inventory requirements. We provide access to premium programmatic inventory without requiring minimum spend commitments on individual platforms."),
            ("What's the minimum budget for programmatic advertising?", "We recommend a minimum of $3,000/month in media spend for programmatic campaigns to generate statistically meaningful data for optimisation. Below this threshold, impression volume is too low to achieve reliable audience learning. Lumo's management fee starts at $2,000/month separately from ad spend."),
            ("How is programmatic different from Google Display Network?", "Google Display Network (GDN) is a walled-garden network — you can only reach people browsing Google-affiliated sites. Programmatic DSPs access the open web, including premium publishers that don't participate in GDN, plus CTV/OTT inventory, audio platforms, and digital-out-of-home. Programmatic also offers significantly more sophisticated audience targeting and bidding options."),
            ("How does Lumo ensure brand safety in programmatic?", "Lumo implements multi-layer brand safety: category exclusions (blocking adult, political, and sensitive content categories), domain blocklists (excluding known low-quality or brand-unsafe publishers), third-party verification through IAS or DoubleVerify, and viewability standards (minimum 70% in-view for 2+ seconds). Brand safety configuration is customised to each client's requirements."),
        ],
        "cta_h2": "Ready to Reach Your Audience Everywhere They Browse?",
        "cta_sub": "Get a free programmatic advertising strategy session — we'll map your audience segments, estimate reach and CPMs, and show you what a programmatic campaign looks like for your business.",
        "schema_service_name": "Programmatic Advertising Services",
        "schema_service_desc": "AI-powered programmatic advertising for US businesses — display, video, CTV, and retargeting campaigns via premium DSPs with audience-first targeting.",
    },

    "influencer-marketing": {
        "title_tag":  "Influencer Marketing Agency | Creator Campaigns That Convert | Lumo AI",
        "meta_desc":  "Influencer marketing management from Lumo AI Agency. Influencer discovery, vetting, campaign management, and performance tracking for US brands. Micro to mega — results-focused. Free strategy call.",
        "canonical":  "https://lumoaiagency.com/services/influencer-marketing",
        "og_title":   "Influencer Marketing Agency | Lumo AI Agency",
        "og_desc":    "Influencer campaigns that drive real sales — not just likes. Lumo finds, vets, and manages creators across Instagram, TikTok, YouTube, and podcasts. Performance-based tracking included.",
        "h1_html":    "Influencer Marketing That <span class=\"hl-lime\">Drives Sales</span>, Not Just Likes",
        "badge":      "Influencer Marketing Specialists",
        "lead":       "The influencer marketing industry hit $24B in 2025 — but most brands waste budget on vanity metrics. Lumo builds creator campaigns tied to real business outcomes: traffic, leads, and sales — with full performance tracking from post to purchase.",
        "stat1_num": "$24B",  "stat1_lbl": "Global influencer marketing industry (2025)",
        "stat2_num": "3.5x",  "stat2_lbl": "Higher engagement vs. brand-owned content",
        "stat3_num": "92%",   "stat3_lbl": "Of consumers trust creator recommendations",
        "why_h2": "Why Influencer Marketing Outperforms Traditional Advertising",
        "why_p1": "Ad blindness is real. Banner ads are ignored, pre-rolls are skipped, and sponsored posts in feeds blur into noise. But when a creator someone genuinely follows recommends a product in their authentic voice, it cuts through — because it doesn't feel like advertising. The trust a creator has built with their audience transfers to the brands they authentically endorse.",
        "why_p2": "The key word is 'authentically.' Most influencer campaigns fail because brands push scripted messaging that creators deliver inauthentically — and audiences immediately recognise it. Lumo builds creator briefs that give influencers creative freedom within your brand parameters, resulting in content that actually resonates and converts.",
        "why_p3": "Lumo adds AI-powered vetting and performance attribution that most influencer agencies lack. We analyse audience authenticity scores, engagement quality, follower demographics, and past campaign performance before any partnership — ensuring every creator we recommend has the audience you actually want to reach.",
        "services_h2": "Our Influencer Marketing Services",
        "services": [
            ("🔍", "Creator Discovery & Vetting", "Data-driven influencer identification — screening for audience authenticity, engagement quality, follower demographics, niche relevance, and brand safety before any outreach. We present only creators who pass our full vetting process."),
            ("📝", "Campaign Strategy & Briefing", "Campaign concept development, creator briefing documents, usage rights negotiation, FTC compliance guidance, and content approval workflows — ensuring on-brand execution without stifling creator voice."),
            ("🤝", "Creator Management", "End-to-end relationship management — contract negotiation, timeline management, deliverable tracking, and payment processing — so you focus on business outcomes while we handle logistics."),
            ("📊", "Performance Tracking & Attribution", "UTM-tracked links, promo codes, and pixel-based attribution connecting each creator's content directly to traffic, sign-ups, and sales — so you know exactly which partnerships are ROI-positive."),
            ("🎬", "Content Amplification", "Boost top-performing organic creator content via paid social (whitelisting) to extend reach beyond the creator's organic audience — combining authentic influencer trust with paid media scale."),
            ("♻️", "UGC Content Licensing", "License creator-produced content for use in your own paid ads, website, and email marketing — converting high-performing influencer content into evergreen brand assets."),
        ],
        "process": [
            ("🎯", "Strategy & Targeting", "Define campaign objectives, target audience, creator tier mix (nano/micro/macro/mega), platform selection, and KPIs — building a campaign architecture before any creator outreach."),
            ("🔍", "Discovery & Vetting", "Identify 20–50 qualified creator candidates per campaign, run full audience analysis, and present a shortlisted recommendation with data supporting each selection."),
            ("🚀", "Launch & Manage", "Execute contracts, deliver briefing documents, manage content review and approval, and publish on schedule — coordinating all creator logistics from one point of contact."),
            ("📊", "Measure & Report", "Post-campaign analysis: reach, engagement, click-through, conversion attribution, earned media value (EMV), and cost-per-acquisition — with a lessons-learned report for future campaign optimisation."),
        ],
        "price_from": "$2,500",
        "price_note": "per campaign — creator fees are separate and vary by tier and platform",
        "faqs": [
            ("What's the difference between micro and macro influencers?", "Micro-influencers (10K–100K followers) typically deliver higher engagement rates, more niche audiences, and lower cost-per-post than macro or mega influencers. Macro influencers (100K–1M) offer broader reach. Nano influencers (1K–10K) have the highest engagement rates but limited scale. Lumo recommends the right tier mix based on your campaign objectives — most brands see the best ROI from micro-influencer campaigns combined with paid whitelisting."),
            ("How do you ensure influencer content is FTC compliant?", "Lumo builds FTC compliance into every campaign brief — requiring clear disclosure language (#ad, #sponsored, or Paid Partnership labels), reviewing content before publication to verify disclosures are present, and documenting compliance for each partnership. We stay current with FTC guidelines updates and apply them to all campaigns proactively."),
            ("How do you measure influencer marketing ROI?", "Lumo uses UTM-tracked unique links and promo codes for each creator to directly attribute traffic, sign-ups, and purchases. We also track reach, impressions, engagement rate, earned media value (EMV), and cost-per-acquisition. For brand awareness campaigns, we track share of voice and sentiment in addition to direct conversion metrics."),
            ("Which platforms does Lumo run influencer campaigns on?", "Lumo manages influencer campaigns on Instagram (Feed, Reels, Stories), TikTok, YouTube (dedicated reviews and integrations), podcasts, and LinkedIn for B2B clients. Platform selection is driven by where your target audience is most active and receptive to creator recommendations."),
            ("How long does it take to launch an influencer campaign?", "A typical Lumo influencer campaign takes 3–4 weeks from kickoff to first content publication: 1 week for strategy and creator identification, 1 week for outreach and contracting, 1–2 weeks for content creation and review. Longer lead times may apply for campaigns requiring custom product samples or elaborate production."),
        ],
        "cta_h2": "Ready to Turn Creator Trust Into Your Sales?",
        "cta_sub": "Book a free influencer marketing strategy session — we'll map your target audience to creator opportunities and show you what a performance-tracked campaign looks like for your brand.",
        "schema_service_name": "Influencer Marketing Services",
        "schema_service_desc": "Influencer marketing campaigns for US brands — creator discovery, vetting, management, and performance attribution across Instagram, TikTok, YouTube, and podcasts.",
    },

    "amazon-marketing": {
        "title_tag":  "Amazon Marketing Agency | SEO + Ads for Sellers & Vendors | Lumo AI",
        "meta_desc":  "Amazon marketing from Lumo AI Agency — Amazon SEO, Sponsored Products, Sponsored Brands, DSP, and storefront optimization for sellers and vendors. Grow your Amazon revenue. Free audit.",
        "canonical":  "https://lumoaiagency.com/services/amazon-marketing",
        "og_title":   "Amazon Marketing Agency | Lumo AI Agency",
        "og_desc":    "Grow your Amazon revenue with SEO-optimised listings, Sponsored Products, Sponsored Brands, and Amazon DSP. Lumo manages your full Amazon marketing strategy. Free audit.",
        "h1_html":    "Amazon Marketing That <span class=\"hl-lime\">Grows Your Revenue</span> on the World's Biggest Marketplace",
        "badge":      "Amazon Marketing Specialists",
        "lead":       "Amazon is the #1 product search engine in the US — more product searches start on Amazon than on Google. Lumo builds complete Amazon marketing strategies: SEO-optimised listings, PPC campaigns, and brand storefronts that capture marketplace demand and convert it into revenue.",
        "stat1_num": "66%",  "stat1_lbl": "Of US product searches start on Amazon",
        "stat2_num": "3.7x", "stat2_lbl": "Average revenue growth for Lumo Amazon clients",
        "stat3_num": "380M", "stat3_lbl": "Active Amazon shoppers in the US",
        "why_h2": "Why Amazon Marketing Is a Separate Strategy From Google",
        "why_p1": "Amazon's A9/A10 search algorithm is fundamentally different from Google's. It prioritises conversion rate, sales velocity, and relevance — not backlinks or domain authority. A product with a poorly optimised title and thin bullet points will be buried in search results regardless of how strong your brand is elsewhere. Amazon SEO is its own discipline.",
        "why_p2": "Amazon's advertising platform — Sponsored Products, Sponsored Brands, and Sponsored Display — operates on a cost-per-click model with real-time auction dynamics. Without expert bid management and keyword strategy, ad spend can scale faster than revenue. Lumo's Amazon PPC management keeps ACoS (Advertising Cost of Sale) at efficient levels while scaling profitable campaigns.",
        "why_p3": "Lumo integrates Amazon marketing with your broader digital strategy. Brand-registered sellers benefit from A+ Content, Storefronts, and Brand Analytics — tools that improve conversion rates and provide competitive intelligence. We manage the full seller ecosystem so every element reinforces the others.",
        "services_h2": "Our Amazon Marketing Services",
        "services": [
            ("🔍", "Amazon SEO & Listing Optimisation", "Keyword research using Amazon-specific tools, title optimisation with primary keywords in the first 80 characters, bullet point copy, backend search terms, and A+ Content — built to rank and convert."),
            ("💰", "Sponsored Products Management", "Keyword and ASIN-targeted Sponsored Products campaigns with structured ad groups, match type strategy, negative keyword management, and bid optimisation — maintaining efficient ACoS while scaling revenue."),
            ("🏆", "Sponsored Brands & Display", "Sponsored Brands campaigns with custom headline copy and video — capturing brand searches and competitor traffic. Sponsored Display for remarketing site visitors and competitor ASIN shoppers."),
            ("🏪", "Amazon Storefront Design", "Custom Brand Store buildout with shoppable collections, brand story modules, and video — creating a brand destination within Amazon that increases basket size and repeat purchase."),
            ("📦", "Amazon DSP", "Amazon's Demand Side Platform for programmatic advertising — reaching Amazon shoppers on and off Amazon.com with first-party purchase data targeting unavailable anywhere else."),
            ("📊", "Amazon Analytics & Reporting", "Brand Analytics, Search Term Reports, ASIN performance tracking, and competitor share of voice monitoring — with monthly ACoS, TACoS, and revenue growth reporting."),
        ],
        "process": [
            ("🔎", "Account & Listing Audit", "Audit current listing quality, keyword rankings, ad account structure, ACoS by campaign, and competitor positioning — identifying the highest-impact opportunities first."),
            ("⚙️", "Optimise & Build", "Implement listing optimisations, restructure ad campaigns, launch A+ Content, and build or refresh the Brand Store — prioritised by estimated revenue impact."),
            ("🚀", "Scale Campaigns", "Once baseline campaigns are optimised and ACoS is efficient, scale budget into Sponsored Brands, video, and DSP to capture incrementally broader demand."),
            ("📊", "Report & Refine", "Weekly ad performance checks, monthly full-account reviews, and quarterly strategy adjustments based on seasonal trends and marketplace changes."),
        ],
        "price_from": "$1,800",
        "price_note": "per month management fee — Amazon ad spend is separate and goes directly to Amazon",
        "faqs": [
            ("What's the difference between Amazon SEO and Google SEO?", "Amazon SEO optimises product listings to rank in Amazon's internal search results — driven by conversion rate, sales velocity, relevance, and review signals. Google SEO optimises web pages for Google's algorithm. The keyword research approaches, ranking factors, and optimisation tactics are entirely different. Lumo treats Amazon SEO as a completely separate discipline with its own methodology."),
            ("What is ACoS and what's a good ACoS?", "ACoS (Advertising Cost of Sale) is the percentage of ad-attributed sales spent on advertising. A 'good' ACoS depends on your product margin — if your profit margin is 40%, an ACoS below 30% is profitable. Lumo targets ACoS levels based on your specific margin structure and growth phase — newer listings may justify higher ACoS to build sales velocity, while established products focus on efficiency."),
            ("Do you work with both FBA sellers and Vendors (1P)?", "Yes. Lumo works with both third-party (3P) FBA sellers using Seller Central and first-party (1P) vendors using Vendor Central. Each has different advertising tools, pricing dynamics, and optimisation levers — we adapt our strategy to your specific seller type and business model."),
            ("How quickly can I expect to see results from Amazon SEO?", "Listing optimisation improvements typically affect search ranking within 1–2 weeks as Amazon's algorithm processes the updated content. Sales velocity improvements follow within 2–4 weeks. Amazon PPC campaigns can generate incremental sales within the first week of launch, with ACoS efficiency improving over the first 30–60 days as negative keyword data accumulates."),
            ("Can Lumo help launch a new product on Amazon?", "Yes. Product launches require a specific strategy: aggressive initial PPC to build sales velocity, early review generation (via Amazon Vine or follow-up email), and listing optimisation before the first ad dollar is spent. Lumo builds launch plans that establish organic ranking quickly while maintaining controlled ACoS during the critical initial sales period."),
        ],
        "cta_h2": "Ready to Grow Your Amazon Revenue?",
        "cta_sub": "Get a free Amazon account audit — we'll review your listings, ad account structure, and competitor positioning and show you exactly where the growth opportunities are.",
        "schema_service_name": "Amazon Marketing Services",
        "schema_service_desc": "Amazon marketing for US sellers and vendors — listing SEO, Sponsored Products, Sponsored Brands, Amazon DSP, and storefront optimization to grow marketplace revenue.",
    },

    "bing-ads": {
        "title_tag":  "Bing Ads Management | Microsoft Advertising Agency | Lumo AI",
        "meta_desc":  "Microsoft Advertising (Bing Ads) management from Lumo AI Agency. Reach 63M searchers Google doesn't — at 30–40% lower CPCs. Expert Bing PPC management for US businesses. Free audit.",
        "canonical":  "https://lumoaiagency.com/services/bing-ads",
        "og_title":   "Bing Ads / Microsoft Advertising | Lumo AI Agency",
        "og_desc":    "Microsoft Advertising reaches 63M US searchers who don't use Google — at 30–40% lower CPCs. Lumo's Bing Ads management captures this overlooked traffic. Free audit.",
        "h1_html":    "Bing Ads That Reach <span class=\"hl-lime\">63 Million Searchers</span> Your Competitors Ignore",
        "badge":      "Microsoft Advertising Specialists",
        "lead":       "Microsoft Advertising (formerly Bing Ads) reaches 63 million US searchers who don't use Google — at 30–40% lower cost-per-click. Most businesses ignore Bing entirely, making it one of the highest-ROI untapped paid search opportunities available.",
        "stat1_num": "63M",   "stat1_lbl": "US searchers on Microsoft Search Network",
        "stat2_num": "35%",   "stat2_lbl": "Lower average CPC vs. Google Ads",
        "stat3_num": "38%",   "stat3_lbl": "Of Bing users have household income over $100K",
        "why_h2": "Why Microsoft Advertising Is the Overlooked Growth Channel",
        "why_p1": "The Microsoft Search Network (Bing, Yahoo, AOL, DuckDuckGo, and partner sites) accounts for over 30% of US desktop searches. Bing users skew older, wealthier, and more likely to be in professional or managerial roles — demographics that are highly valuable for B2B, financial services, home services, and premium consumer brands.",
        "why_p2": "Because most advertisers focus exclusively on Google, Bing Ads has significantly less competition — resulting in CPCs that are consistently 30–40% lower than equivalent Google campaigns. For businesses in competitive industries where Google CPC for core keywords runs $10–$30, Bing can deliver the same intent traffic at dramatically better economics.",
        "why_p3": "Microsoft Advertising also uniquely integrates with LinkedIn for B2B audience targeting — allowing you to target by job title, industry, and company size within search campaigns. This LinkedIn Professional Profile targeting capability exists nowhere else in paid search and makes Bing particularly powerful for B2B advertisers.",
        "services_h2": "Our Microsoft Advertising Services",
        "services": [
            ("🔍", "Bing Search Campaigns", "Keyword research, campaign structure, ad copy creation, and bid management for Microsoft Search — capturing high-intent queries at 30–40% lower CPCs than Google equivalents."),
            ("💼", "LinkedIn Audience Targeting", "Unique to Microsoft Advertising: target Bing Search ads by LinkedIn job title, company, industry, and seniority — the most precise B2B audience targeting available in any search platform."),
            ("🛒", "Microsoft Shopping Ads", "Product listing campaigns on Bing Shopping — reaching comparison shoppers on the Microsoft Search Network with lower competition and often lower CPCs than Google Shopping."),
            ("📱", "Microsoft Audience Network", "Native and display ads across MSN, Outlook.com, Microsoft Edge, and partner sites — reaching Microsoft's first-party audience with highly contextual targeting."),
            ("🔄", "Google Ads Import & Sync", "Import your existing Google Ads campaigns into Microsoft Advertising and adapt them for Bing's algorithm — the fastest way to extend your paid search reach to the Microsoft network."),
            ("📊", "Unified Reporting", "Cross-platform reporting combining Google Ads and Microsoft Advertising performance — showing total paid search reach, share of voice, and blended CPC/CPA across both networks."),
        ],
        "process": [
            ("🔎", "Audit & Import", "Audit your current Google Ads campaigns, import the best-performing campaigns into Microsoft Advertising, and adapt match types and bids for Bing's auction dynamics."),
            ("⚙️", "Optimise for Bing", "Adjust keyword match types, add Bing-specific negative keywords, configure LinkedIn audience layers for B2B campaigns, and set up Microsoft Audience Network targeting."),
            ("🚀", "Launch & Monitor", "Go live with initial bids and monitor search term reports, quality scores, and conversion data — applying Bing-specific optimisations that differ from Google best practices."),
            ("📊", "Report & Expand", "Monthly performance reports with Microsoft Advertising metrics alongside Google data — with recommendations for budget allocation between networks based on CPA and volume data."),
        ],
        "price_from": "$750",
        "price_note": "per month management fee — Microsoft Advertising spend is separate",
        "faqs": [
            ("Is Bing Ads worth it in 2026?", "Yes — especially for businesses in competitive Google Ads markets. Microsoft Advertising reaches 63M+ US searchers at 30–40% lower CPCs than Google, with less advertiser competition. B2B advertisers particularly benefit from LinkedIn Professional Profile targeting. For most businesses already running Google Ads, adding Bing is one of the highest-ROI expansion moves available."),
            ("How much does Bing Ads cost?", "Microsoft Advertising CPCs are typically 30–40% lower than equivalent Google Ads keywords. Minimum recommended spend is $500/month for meaningful data volume. Lumo's management fee starts at $750/month. For most clients, Bing is managed as an add-on alongside Google Ads rather than a standalone channel."),
            ("Can I import my Google Ads campaigns into Bing?", "Yes — Microsoft Advertising has a Google import tool that copies campaigns, ad groups, keywords, and ads from Google Ads. Lumo uses this as a starting point, then adapts the campaigns for Bing's algorithm differences: adjusting match types, modifying bids based on Bing's auction dynamics, and adding Bing-specific negative keywords and audience layers."),
            ("What's Microsoft Audience Network?", "Microsoft Audience Network (MSAN) is Microsoft's native advertising platform — showing ads on MSN.com, Outlook.com, Microsoft Edge, and partner sites. Unlike search ads, MSAN reaches users who aren't actively searching but match your target audience profile. It's similar to Google Display Network but with Microsoft's first-party data (including LinkedIn demographics) for targeting."),
            ("Does Lumo manage Bing Ads alongside Google Ads?", "Yes. Lumo manages both Google Ads and Microsoft Advertising for clients who want both, with unified reporting showing performance across both networks. This allows proper budget allocation based on CPA and volume data from each network, and ensures consistent messaging across both platforms."),
        ],
        "cta_h2": "Ready to Capture 30% More Search Traffic at Lower Cost?",
        "cta_sub": "Get a free Microsoft Advertising audit — we'll show you the search volume your business is missing on Bing and estimate your potential CPA vs. your current Google campaigns.",
        "schema_service_name": "Microsoft Advertising (Bing Ads) Management",
        "schema_service_desc": "Microsoft Advertising management for US businesses — Bing search campaigns, LinkedIn audience targeting, Microsoft Shopping, and Audience Network at 30–40% lower CPCs than Google.",
    },

    "landing-pages-funnels": {
        "title_tag":  "Landing Page Design & Sales Funnels | Conversion-Focused | Lumo AI",
        "meta_desc":  "Landing page design and sales funnel strategy from Lumo AI Agency. High-converting pages built for Google Ads, Meta Ads, and organic traffic. AI-optimised layouts. Free audit.",
        "canonical":  "https://lumoaiagency.com/services/landing-pages-funnels",
        "og_title":   "Landing Pages & Sales Funnels | Lumo AI Agency",
        "og_desc":    "High-converting landing pages and sales funnels designed by Lumo AI Agency. Built for paid ads, SEO, and email campaigns — with A/B testing and AI optimisation built in.",
        "h1_html":    "Landing Pages & Funnels That <span class=\"hl-lime\">Convert Traffic</span> Into Revenue",
        "badge":      "Conversion Design Specialists",
        "lead":       "Most businesses send paid traffic to their homepage — and lose 80% of it. Lumo designs conversion-focused landing pages and sales funnels that match message to intent, eliminate friction, and turn clicks into customers.",
        "stat1_num": "2.9x", "stat1_lbl": "Average CVR lift from dedicated landing pages",
        "stat2_num": "80%",  "stat2_lbl": "Of ad traffic is lost without dedicated landing pages",
        "stat3_num": "47%",  "stat3_lbl": "Average lead volume increase post-page rebuild",
        "why_h2": "Why Dedicated Landing Pages Are the Single Highest-ROI Conversion Fix",
        "why_p1": "When someone clicks your Google Ad for 'emergency plumber Austin' and lands on your homepage — with navigation, multiple CTAs, and no clear next step — most of them leave. A dedicated landing page that mirrors the ad's promise, eliminates distraction, and presents a single clear action can increase conversion rates by 2–5x with zero additional ad spend.",
        "why_p2": "The same principle applies across every traffic source. Email campaigns, social ads, SEO content, and organic social all convert dramatically better when they land users on pages purpose-built for that specific audience and intent. Generic destination pages waste the trust and intent you've earned getting the click.",
        "why_p3": "Lumo builds landing pages with AI-informed layout decisions — copy hierarchy, CTA placement, social proof positioning, and form length — based on conversion data across thousands of pages in similar industries. Every page launches with the best-known starting configuration, then improves through A/B testing.",
        "services_h2": "Our Landing Page & Funnel Services",
        "services": [
            ("🎯", "Conversion-Focused Page Design", "Purpose-built landing pages for each campaign and traffic source — with message-match to your ads, clear single CTAs, social proof positioning, and mobile-first layouts that load in under 2 seconds."),
            ("🔄", "Multi-Step Sales Funnels", "Lead generation funnels (optin → thank you), webinar funnels, e-commerce checkout funnels, and SaaS trial funnels — built with the right number of steps and friction level for your offer."),
            ("🧪", "A/B Testing", "Structured A/B tests on headlines, hero images, CTA copy, form length, and page layout — with statistical significance thresholds and clear test roadmaps that compound conversion gains over time."),
            ("📱", "Mobile Optimisation", "Mobile-first design with thumb-friendly CTAs, minimal form fields, click-to-call integration, and load times under 2 seconds on 4G — critical when 60%+ of paid traffic arrives on mobile."),
            ("⚡", "Page Speed Optimisation", "Core Web Vitals optimisation — LCP, CLS, and INP scores in the 'Good' range for every landing page, ensuring Google Ads Quality Scores stay high and users don't bounce from slow loads."),
            ("📊", "Conversion Tracking Setup", "Google Analytics 4, Google Ads conversion tracking, Meta Pixel, and heatmap tool implementation (Hotjar/Microsoft Clarity) — so every micro-conversion is measured and optimised."),
        ],
        "process": [
            ("🔎", "Audit & Strategy", "Analyse current landing pages, ad traffic, and conversion data — identifying the highest-impact pages to build or optimise first based on traffic volume and current conversion rate."),
            ("✏️", "Design & Build", "Create wireframes for approval, then develop high-fidelity pages in your CMS or standalone page builder — with copy, design, and technical implementation handled by Lumo's team."),
            ("🚀", "Launch & Track", "Deploy pages, implement full conversion tracking, configure heatmaps, and confirm all integrations (CRM, email, ad platforms) are firing correctly before driving traffic."),
            ("🧪", "Test & Optimise", "Run structured A/B tests with minimum 100 conversions per variant before declaring winners — applying learnings to compound conversion rate improvements across the entire funnel."),
        ],
        "price_from": "$1,500",
        "price_note": "per landing page build — funnel packages from $3,500; ongoing CRO retainers from $1,200/mo",
        "faqs": [
            ("What platform does Lumo build landing pages on?", "Lumo builds landing pages on the platform that best fits your existing tech stack and requirements: Webflow (recommended for design flexibility and CMS integration), Unbounce or Instapage (for rapid iteration and built-in A/B testing), WordPress with custom development, Shopify for e-commerce, or custom HTML/CSS for maximum performance. We recommend the right platform for your specific situation."),
            ("How long does it take to build a landing page?", "A standard landing page takes 5–7 business days from brief to launch: 1 day for brief and strategy, 2 days for wireframe and copy approval, 2 days for design and build, 1–2 days for QA and revisions. Complex multi-step funnels or pages requiring custom development may take 10–14 days. Lumo doesn't rush pages that aren't ready — a slow launch is better than a leaky one."),
            ("What makes a landing page high-converting?", "The most important conversion factors are: message-match (your page headline must mirror your ad copy exactly), a single clear CTA (one action, not six options), above-the-fold credibility (reviews, logos, stats visible before scrolling), friction reduction (short forms, clear privacy messaging), and page speed (under 2 seconds). Lumo builds these principles into every page from the first version."),
            ("Should I send all my ad traffic to one landing page?", "No — this is one of the most common conversion mistakes. Each ad campaign, ad group, and major keyword theme should ideally have its own dedicated landing page with matching headlines and relevant social proof. The more precisely a page matches the specific intent and language of the ad that drove the click, the higher it converts. Lumo builds page portfolios that match the structure of your ad account."),
            ("How do you measure landing page success?", "Lumo tracks conversion rate (primary metric), cost-per-conversion (for paid traffic), heatmap engagement (scroll depth, click maps), form abandonment rate, and page load time. We set conversion rate benchmarks based on your industry and traffic source, and report weekly during active A/B testing periods."),
        ],
        "cta_h2": "Ready to Convert More of the Traffic You're Already Getting?",
        "cta_sub": "Get a free landing page audit — we'll analyse your current pages, calculate how much conversion rate you're leaving on the table, and show you exactly what needs to change.",
        "schema_service_name": "Landing Page Design & Sales Funnel Services",
        "schema_service_desc": "Conversion-focused landing page design and sales funnel strategy for US businesses — A/B tested pages built for Google Ads, Meta Ads, SEO, and email campaigns.",
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
          <li><a href="../services/technical-seo.html">Technical SEO</a></li>
          <li><a href="../services/local-seo.html">Local SEO</a></li>
          <li><a href="../services/link-building.html">Link Building</a></li>
          <li><a href="../services/reputation-management.html">Reputation Mgmt</a></li>
          <li><a href="../services/programmatic-advertising.html">Programmatic Ads</a></li>
          <li><a href="../services/influencer-marketing.html">Influencer Mktg</a></li>
          <li><a href="../services/amazon-marketing.html">Amazon Marketing</a></li>
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

CSS = """    :root{--bg:#0D0D14;--bg-card:#13131F;--bg-dark:#09090F;--primary:#B3FF00;--secondary:#7C3AED;--accent:#00F5FF;--text:#F0F0FF;--muted:#6B7280;--border:rgba(179,255,0,0.15);--radius-sm:8px;--radius:14px;--radius-lg:20px;--transition:0.25s cubic-bezier(0.4,0,0.2,1);}
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
    @media(max-width:560px){.footer-top{grid-template-columns:1fr;gap:32px;}}"""

JS = """  const nav=document.getElementById('navbar');
  const st=document.getElementById('scroll-top');
  window.addEventListener('scroll',()=>{nav.classList.toggle('scrolled',window.scrollY>40);st.classList.toggle('visible',window.scrollY>300);});
  const hamburger=document.querySelector('.nav-hamburger');
  const mobileMenu=document.getElementById('mobile-menu');
  if(hamburger){hamburger.addEventListener('click',()=>{const open=mobileMenu.classList.toggle('open');hamburger.setAttribute('aria-expanded',open);});}
  st.addEventListener('click',()=>window.scrollTo({top:0,behavior:'smooth'}));
  document.querySelectorAll('.faq-q').forEach(q=>{q.addEventListener('click',()=>{q.parentElement.classList.toggle('open');});});"""


def build_page(slug, d):
    svc_cards = "".join(f"""      <div class="svc-card"><div class="svc-icon">{ic}</div><div class="svc-title">{t}</div><div class="svc-desc">{dc}</div></div>\n""" for ic,t,dc in d["services"])
    steps = "".join(f"""      <div class="step-card"><div class="step-num">{i:02d}</div><div class="step-icon">{ic}</div><div class="step-title">{t}</div><div class="step-desc">{dc}</div></div>\n""" for i,(ic,t,dc) in enumerate(d["process"],1))
    faq_html = ""
    schema_faqs = []
    for q,a in d["faqs"]:
        faq_html += f"""    <div class="faq-item"><div class="faq-q" role="button" tabindex="0"><span class="faq-q-text">{q}</span><span class="faq-icon"><svg width="12" height="12" viewBox="0 0 12 12" fill="none"><line x1="6" y1="0" x2="6" y2="12" stroke="currentColor" stroke-width="2"/><line x1="0" y1="6" x2="12" y2="6" stroke="currentColor" stroke-width="2"/></svg></span></div><div class="faq-a"><p>{a}</p></div></div>\n"""
        schema_faqs.append({"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}})
    schema = {"@context":"https://schema.org","@graph":[{"@type":"WebPage","@id":d["canonical"],"url":d["canonical"],"name":d["title_tag"],"description":d["meta_desc"],"breadcrumb":{"@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Home","item":"https://lumoaiagency.com/"},{"@type":"ListItem","position":2,"name":"Services","item":"https://lumoaiagency.com/services.html"},{"@type":"ListItem","position":3,"name":d["schema_service_name"],"item":d["canonical"]}]}},{"@type":"Service","name":d["schema_service_name"],"description":d["schema_service_desc"],"provider":{"@type":"LocalBusiness","name":"Lumo AI Agency","url":"https://lumoaiagency.com"},"areaServed":{"@type":"Country","name":"United States"}},{"@type":"FAQPage","mainEntity":schema_faqs}]}
    return f"""<!DOCTYPE html>
<html lang="en-US">
<head>
  <meta charset="UTF-8"/>
  <meta name="viewport" content="width=device-width,initial-scale=1.0"/>
  <meta name="description" content="{d['meta_desc']}"/>
  <meta name="robots" content="index,follow"/>
  <meta property="og:type" content="website"/>
  <meta property="og:title" content="{d['og_title']}"/>
  <meta property="og:description" content="{d['og_desc']}"/>
  <meta property="og:url" content="{d['canonical']}"/>
  <link rel="canonical" href="{d['canonical']}"/>
  <title>{d['title_tag']}</title>
  <link rel="preconnect" href="https://fonts.googleapis.com"/>
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin/>
  <link href="https://fonts.googleapis.com/css2?family=Berkshire+Swash&family=Inter:wght@400;500;600;700;900&family=Syne:wght@700;800&display=swap" rel="stylesheet"/>
  <script type="application/ld+json">{json.dumps(schema,ensure_ascii=False)}</script>
  <style>\n{CSS}\n  </style>
</head>
<body>
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
    <div class="nav-cta"><a href="../contact.html" class="btn btn-lime" style="padding:10px 22px;font-size:0.85rem;">Get Started</a></div>
    <button class="nav-hamburger" aria-label="Open menu" aria-expanded="false" aria-controls="mobile-menu"><span></span><span></span><span></span></button>
  </div>
  <div class="mobile-menu" id="mobile-menu" role="menu">
    <a href="../index.html" role="menuitem">Home</a>
    <a href="../services.html" role="menuitem">Services</a>
    <a href="../about.html" role="menuitem">About</a>
    <a href="../pricing.html" role="menuitem">Pricing</a>
    <a href="../contact.html" role="menuitem">Get Started</a>
  </div>
</nav>
<section class="page-hero">
  <div class="blob-wrap"><div class="blob blob-lime"></div><div class="blob blob-violet"></div></div>
  <div class="hero-noise"></div>
  <div class="container page-hero-inner">
    <nav class="breadcrumb" aria-label="Breadcrumb">
      <a href="../index.html">Home</a><span class="breadcrumb-sep">›</span>
      <a href="../services.html">Services</a><span class="breadcrumb-sep">›</span>
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
<section class="stats-strip" aria-label="Key metrics">
  <div class="stats-row">
    <div class="stat-item"><div class="stat-num">{d['stat1_num']}</div><div class="stat-label">{d['stat1_lbl']}</div></div>
    <div class="stat-item"><div class="stat-num">{d['stat2_num']}</div><div class="stat-label">{d['stat2_lbl']}</div></div>
    <div class="stat-item"><div class="stat-num">{d['stat3_num']}</div><div class="stat-label">{d['stat3_lbl']}</div></div>
  </div>
</section>
<section class="section-pad">
  <div class="container">
    <div class="why-grid">
      <div class="why-text">
        <div class="section-eyebrow">Why It Matters</div>
        <h2 class="section-h2">{d['why_h2']}</h2>
        <p>{d['why_p1']}</p><p>{d['why_p2']}</p><p>{d['why_p3']}</p>
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
<section class="section-pad process-bg">
  <div class="container">
    <div class="section-eyebrow">What We Do</div>
    <h2 class="section-h2">{d['services_h2']}</h2>
    <p class="section-sub">Every deliverable is tracked, reported, and tied to business outcomes — not just activity metrics.</p>
    <div class="svc-grid">
{svc_cards}    </div>
  </div>
</section>
<section class="section-pad">
  <div class="container">
    <div class="section-eyebrow">How We Work</div>
    <h2 class="section-h2">Our Process</h2>
    <p class="section-sub">A clear four-step process from first conversation to measurable results.</p>
    <div class="process-grid">
{steps}    </div>
  </div>
</section>
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
<section id="faq" class="section-pad">
  <div class="container">
    <div class="section-eyebrow">FAQ</div>
    <h2 class="section-h2" style="text-align:center;margin-bottom:48px;">Common Questions</h2>
    <div class="faq-wrap">
{faq_html}    </div>
  </div>
</section>
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
  <svg width="16" height="16" viewBox="0 0 16 16" fill="none"><path d="M8 12V4M4 8l4-4 4 4" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>
</button>
<script>{JS}</script>
</body>
</html>"""


for slug, data in SERVICES.items():
    html = build_page(slug, data)
    path = os.path.join(BASE, f"{slug}.html")
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Created: services/{slug}.html ({len(html):,} chars)")

print(f"\nDone. {len(SERVICES)} pages created.")
