#!/usr/bin/env python3
"""Backlog Batch 1:
   google-shopping, performance-max, pinterest-ads, snapchat-ads, twitter-ads
"""
import os, json

BASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "services")
os.makedirs(BASE, exist_ok=True)

SERVICES = {

    "google-shopping": {
        "title_tag":  "Google Shopping Ads Agency | Product Feed & PMax Management | Lumo AI",
        "meta_desc":  "Google Shopping management from Lumo AI Agency. Product feed optimisation, Smart Shopping, Performance Max, and Shopping campaign management for US e-commerce brands. Free shopping audit.",
        "canonical":  "https://lumoaiagency.com/services/google-shopping",
        "og_title":   "Google Shopping Ads Agency | Lumo AI Agency",
        "og_desc":    "Google Shopping campaigns that put your products in front of buyers ready to purchase. Lumo manages feed optimisation, bidding strategy, and Performance Max for US e-commerce brands.",
        "h1_html":    "Google Shopping Ads That <span class=\"hl-lime\">Put Your Products</span> in Front of Buyers",
        "badge":      "Google Shopping Specialists",
        "lead":       "Google Shopping ads appear at the top of search results with product image, price, and store name — capturing buyers at the moment of purchase intent. Lumo manages the full Google Shopping stack: product feed optimisation, campaign architecture, and bidding strategy for US e-commerce brands.",
        "stat1_num": "76%",  "stat1_lbl": "Of US consumers use Google to discover new products",
        "stat2_num": "30%",  "stat2_lbl": "Higher CTR for Shopping ads vs. text ads for product searches",
        "stat3_num": "4.2x", "stat3_lbl": "Average ROAS for Lumo-managed Google Shopping accounts",
        "why_h2": "Why Google Shopping Performance Starts With Your Product Feed",
        "why_p1": "Most e-commerce brands underperform on Google Shopping for the same reason: a low-quality product feed. Google's Shopping algorithm ranks products based on feed data — product title, description, category, attributes, and image quality — before campaign settings have any meaningful effect. A well-structured feed with keyword-rich titles and complete attribute data can double impressions without touching campaign bids.",
        "why_p2": "Campaign structure is the second major performance lever. The default Smart Shopping or broad Performance Max setup mixes high-margin products with low-margin SKUs, brand terms with non-brand queries, and bestsellers with dead inventory — optimising toward average rather than your most profitable segments. Granular campaign architecture separates these segments for independent budget allocation and bidding.",
        "why_p3": "Lumo treats Google Shopping as both a feed management and a paid media problem. We audit and rebuild product feeds for keyword richness, attribute completeness, and category accuracy — then build campaign structures that separate your product portfolio by margin, performance tier, and query intent. The result is a Shopping account that scales profitably rather than chasing blended ROAS averages.",
        "services_h2": "Our Google Shopping Services",
        "services": [
            ("📦", "Product Feed Optimisation", "Feed audit, title restructuring (keyword + attribute-forward format), description optimisation, Google taxonomy category mapping, attribute completion, and custom labels for campaign segmentation."),
            ("🛍️", "Shopping Campaign Architecture", "Segmented campaign structure by product category, margin tier, and performance history — with separate bidding for brand vs. non-brand shopping queries and priority-based campaign layering."),
            ("🚀", "Performance Max Management", "Google Performance Max campaign setup and ongoing optimisation — audience signal configuration, asset group management, product feed connection, and bid strategy tuning for e-commerce ROAS goals."),
            ("🎯", "Bidding Strategy & Optimisation", "Target ROAS bidding configuration, product-level bid adjustments, competitor monitoring, promotional period strategy, and daily optimisation to maximise conversion value within your ROAS targets."),
            ("🖼️", "Feed-Linked Creative Assets", "Performance Max lifestyle image and video asset creation linked to product categories — supplementing Shopping listings with brand imagery that improves display and YouTube placements within PMax."),
            ("📊", "Shopping Analytics & Reporting", "Impression share analysis, product performance reporting, auction insights vs. competitors, query-level performance mining, and monthly ROAS and revenue reporting with segment breakdowns."),
        ],
        "process": [
            ("🔍", "Feed & Account Audit", "Full product feed analysis, campaign structure review, query report mining, and competitive Shopping landscape audit — with a prioritised action plan for feed and campaign improvements."),
            ("🏗️", "Feed Rebuild & Campaign Setup", "Product feed restructuring in Merchant Center, campaign architecture build in Google Ads, bid strategy configuration, and conversion tracking verification — ready to launch within 2 weeks."),
            ("🚀", "Launch & Optimise", "Go live with initial bids, monitor impression share, ROAS, and conversion volume daily. Apply first optimisations in week 1 — negative keywords, bid adjustments, and underperforming product exclusions."),
            ("📈", "Scale & Expand", "Increase budgets on profitable segments, expand to new product categories, test Performance Max asset groups, and add seasonal budget uplift strategies as account performance data matures."),
        ],
        "price_from": "$1,200",
        "price_note": "per month management fee — ad spend is separate (minimum $3,000/mo recommended for Shopping)",
        "faqs": [
            ("What's the difference between Google Shopping and Performance Max?", "Google Shopping campaigns give you more control — you can see which search queries triggered your ads, set bid adjustments by device or time, and segment products into separate campaigns. Performance Max combines Shopping inventory with Google's other networks (Display, YouTube, Gmail, Discovery) and uses AI to optimise across all of them. PMax offers broader reach but less transparency. Lumo typically uses both together — Shopping campaigns for core ROAS performance, PMax for reach and new customer acquisition."),
            ("How important is the product feed for Shopping performance?", "Critical. The product feed is the foundation of Google Shopping — Google uses your feed data to match your products to search queries, rank your listing, and decide whether to show your ad at all. A product with an unoptimised title ('Blue Dress Size 12') performs significantly worse than one with a keyword-rich, attribute-forward title ('Women\'s Blue Midi Wrap Dress - Size 12 - Floral Print'). Feed quality is the most impactful improvement most Shopping accounts can make."),
            ("How do I qualify for Google Shopping?", "To run Google Shopping ads, you need: a Google Merchant Center account with your product feed submitted and approved, a Google Ads account linked to Merchant Center, a website with clear product pages and pricing, and compliance with Google's Shopping policies (no prohibited products, accurate pricing, clear return policy). Lumo handles Merchant Center setup and policy compliance as part of onboarding."),
            ("What ROAS can I expect from Google Shopping?", "Industry benchmark ROAS for Google Shopping varies significantly by category: apparel averages 3–4x, electronics 4–6x, home goods 3–5x. Lumo clients typically see 20–40% ROAS improvement over their baseline within 90 days through feed optimisation and campaign restructuring. We set ROAS targets based on your product margins rather than industry benchmarks — the right ROAS target for a 70% margin product differs from a 20% margin product."),
            ("Can you manage Shopping for Shopify, WooCommerce, or other platforms?", "Yes — Lumo manages Google Shopping for stores on any e-commerce platform. Feed generation is platform-specific: Shopify has a native Google Shopping channel app, WooCommerce uses Google Listings & Ads or third-party feed plugins, Magento uses DataFeedWatch or similar. We audit your current feed source, configure the cleanest data pipeline to Merchant Center, and manage ongoing feed health across your platform."),
        ],
        "cta_h2": "Ready to Get Your Products in Front of Buyers at the Moment of Purchase Intent?",
        "cta_sub": "Get a free Google Shopping audit — we'll analyse your product feed quality, campaign structure, and ROAS performance, then show you exactly what's holding back your Shopping revenue.",
        "schema_service_name": "Google Shopping Management Services",
        "schema_service_desc": "Google Shopping and Performance Max management for US e-commerce brands — product feed optimisation, campaign architecture, and ROAS-focused bidding strategy.",
    },

    "performance-max": {
        "title_tag":  "Performance Max Agency | Google PMax Campaign Management | Lumo AI",
        "meta_desc":  "Google Performance Max campaign management from Lumo AI Agency. PMax setup, audience signals, asset group optimisation, and ROAS management across Google's full ad inventory. Free PMax audit.",
        "canonical":  "https://lumoaiagency.com/services/performance-max",
        "og_title":   "Performance Max Agency | Lumo AI Agency",
        "og_desc":    "Performance Max campaigns run across every Google channel — Search, Shopping, Display, YouTube, Gmail, and Maps. Lumo manages PMax for US businesses with expert audience signals and asset optimisation.",
        "h1_html":    "Performance Max Campaigns That <span class=\"hl-lime\">Unlock Every</span> Google Channel",
        "badge":      "Performance Max Specialists",
        "lead":       "Google Performance Max is a single campaign type that runs across Search, Shopping, Display, YouTube, Gmail, and Google Maps simultaneously — using AI to find conversions wherever they're most available. Lumo manages PMax with the audience signals, asset quality, and optimisation expertise that separates high-performing accounts from wasted spend.",
        "stat1_num": "18%",  "stat1_lbl": "Average conversion increase from PMax vs. standard Shopping",
        "stat2_num": "6",    "stat2_lbl": "Google channels accessed through a single PMax campaign",
        "stat3_num": "3.8x", "stat3_lbl": "Average ROAS for Lumo Performance Max accounts",
        "why_h2": "Why Performance Max Requires Expert Management to Perform",
        "why_p1": "Performance Max hands Google's AI more control than any previous campaign type — choosing placements, audiences, bids, and creative combinations automatically. This is powerful when configured correctly, and catastrophic when it isn't. Without proper audience signals, Google enters a lengthy learning phase burning budget on irrelevant placements. Without quality assets, PMax serves low-converting creative. Without proper exclusions, brand spend cannibalises non-brand performance.",
        "why_p2": "The transparency problem is PMax's biggest challenge. Unlike Search campaigns where you can see every query, PMax provides limited search term visibility and no placement-level reporting. This means optimisation requires indirect signals — asset group performance, audience signal quality, and conversion data analysis — rather than the direct query mining available in standard campaigns. Agencies without PMax expertise often can't diagnose why performance fluctuates.",
        "why_p3": "Lumo's PMax management is built around the levers that actually matter: high-quality audience signals (first-party customer lists, high-intent website visitor segments), asset group architecture (separate groups by product category, audience, and funnel stage), creative quality (platform-native assets for each Google surface), and negative keyword lists (preventing PMax from misappropriating brand traffic).",
        "services_h2": "Our Performance Max Services",
        "services": [
            ("🎯", "Audience Signal Configuration", "First-party audience signal setup — customer match lists, high-value website visitor segments, in-market audiences, and custom intent segments — giving Google's AI the right starting signals for faster learning."),
            ("🖼️", "Asset Group Architecture", "Asset group design by product category, audience type, and funnel stage — with full creative asset sets (headlines, descriptions, images, logos, videos) for each group in correct dimensions and formats."),
            ("📝", "Creative Asset Production", "Performance Max creative production — responsive ad headlines and descriptions, lifestyle and product images in all required aspect ratios, and short-form video assets for YouTube and Discovery placements."),
            ("🛡️", "Brand & Exclusion Management", "Brand campaign separation to prevent PMax from cannibalising branded search traffic, negative keyword list maintenance, placement exclusions for low-quality display inventory, and audience exclusion for existing customers."),
            ("📊", "Performance Analysis & Optimisation", "Asset performance scoring, audience signal refinement, budget allocation between PMax and standard campaigns, conversion tracking audit, and weekly performance reporting with optimisation actions."),
            ("🔗", "Cross-Campaign Integration", "PMax coordination with existing Search, Shopping, and Display campaigns — ensuring PMax complements rather than cannibalises your campaign portfolio, with budget allocation across campaign types."),
        ],
        "process": [
            ("🔍", "Account & Strategy Audit", "Review existing campaign structure, conversion tracking accuracy, audience list quality, and current PMax configuration — identifying conflicts, gaps, and optimisation opportunities before any changes."),
            ("🏗️", "Build & Configure", "PMax campaign setup with audience signals, asset group architecture, creative assets, brand exclusions, and conversion goals — with staging review before going live."),
            ("🚀", "Launch & Learn", "Campaign launch with monitoring through the learning phase (typically 2–4 weeks), daily performance checks, and early adjustments to asset groups and signals as performance data emerges."),
            ("📈", "Optimise & Scale", "Post-learning optimisation — asset group refinement, audience signal updates, budget scaling on profitable segments, and ongoing creative refresh to prevent asset fatigue."),
        ],
        "price_from": "$1,500",
        "price_note": "per month management fee — ad spend is separate (minimum $3,000/mo for meaningful PMax data)",
        "faqs": [
            ("What's the learning phase for Performance Max and how long does it take?", "Google's PMax learning phase typically lasts 4–6 weeks. During this period, the algorithm tests audience, creative, and placement combinations to find what converts. Performance may fluctuate during learning — it's normal to see inconsistent results before the algorithm settles. Lumo configures campaigns to minimise learning phase duration: strong audience signals, complete creative asset sets, and accurate conversion tracking accelerate the learning process."),
            ("Can I run Performance Max alongside my existing Google Ads campaigns?", "Yes — PMax is designed to complement existing campaigns. Lumo establishes clear rules for campaign co-existence: Search campaigns for branded queries and high-intent exact match keywords, Shopping campaigns for product-level control, and PMax for incremental reach across Google's broader inventory. Without proper separation, PMax can cannibalise traffic from other campaigns — especially branded search — which is why exclusion management is critical."),
            ("Why can't I see which search queries are triggering my PMax ads?", "Google provides limited search term visibility in PMax by design — it's part of the trade-off between automation and transparency. Google does provide a partial search terms report showing queries that generated significant conversions, but not the full query data available in Search campaigns. Lumo supplements limited PMax visibility with Google Analytics 4 landing page analysis, audience performance data, and asset group reports to diagnose and improve performance."),
            ("Is Performance Max suitable for all business types?", "PMax works best for businesses with clear conversion events (purchases, lead form submissions, phone calls), sufficient conversion volume (50+ conversions/month recommended for smart bidding), and creative assets for multiple Google surfaces. It's most powerful for e-commerce (Shopping + Display + YouTube combination) and lead generation with good landing pages. Businesses with very narrow audiences, strict brand guidelines, or low conversion volume may benefit more from standard campaign types with more control."),
            ("How does Performance Max affect my Google Shopping campaigns?", "PMax and Shopping campaigns compete for the same Shopping inventory. Google's policy is that PMax takes priority over standard Shopping campaigns when both are eligible for the same query. Many advertisers have found Shopping campaigns receiving significantly less traffic after launching PMax. Lumo manages this by using campaign priority settings, product-level segmentation between PMax and Shopping, and budget allocation to ensure Shopping campaigns retain the control and transparency that PMax can't provide."),
        ],
        "cta_h2": "Ready to Unlock Google's Full Advertising Inventory Through Performance Max?",
        "cta_sub": "Get a free Performance Max audit — we'll review your current PMax configuration, audience signals, asset quality, and campaign co-existence strategy, then show you what's holding back your performance.",
        "schema_service_name": "Performance Max Campaign Management",
        "schema_service_desc": "Google Performance Max campaign management for US businesses — audience signals, asset group architecture, creative production, and ROAS optimisation across all Google channels.",
    },

    "pinterest-ads": {
        "title_tag":  "Pinterest Ads Agency | Pinterest Advertising for US Brands | Lumo AI",
        "meta_desc":  "Pinterest advertising management from Lumo AI Agency. Promoted Pins, Shopping ads, video Pins, and audience targeting for US consumer brands. Reach 465M monthly active users. Free audit.",
        "canonical":  "https://lumoaiagency.com/services/pinterest-ads",
        "og_title":   "Pinterest Ads Agency | Lumo AI Agency",
        "og_desc":    "Pinterest users plan purchases before they make them. Lumo builds Pinterest advertising programs that reach high-intent buyers at the discovery stage — when they're actively looking for what you sell.",
        "h1_html":    "Pinterest Ads That Reach Buyers <span class=\"hl-lime\">Before They Know</span> Where to Buy",
        "badge":      "Pinterest Advertising Specialists",
        "lead":       "Pinterest has 465 million monthly active users actively searching for inspiration — and 83% of weekly Pinners have made a purchase based on branded content. For consumer brands in fashion, home, beauty, food, and lifestyle, Pinterest is the highest-intent discovery channel available. Lumo builds Pinterest ad programs that convert discovery into revenue.",
        "stat1_num": "465M", "stat1_lbl": "Monthly active Pinterest users globally",
        "stat2_num": "83%",  "stat2_lbl": "Of weekly Pinners have made a purchase from brand content",
        "stat3_num": "2x",   "stat3_lbl": "Higher return on ad spend vs. social media benchmark",
        "why_h2": "Why Pinterest Is the Highest-Intent Discovery Platform for Consumer Brands",
        "why_p1": "Pinterest is fundamentally different from other social platforms because users arrive with intent — they're actively searching for ideas, planning purchases, and saving products they want to buy. Unlike Instagram or TikTok, where ads interrupt passive scrolling, Pinterest ads appear in the context of active product discovery. A user searching 'living room furniture ideas' is further along the purchase journey than anyone scrolling their Instagram feed.",
        "why_p2": "Pinterest's purchase timeline is also unique. Users on Pinterest plan purchases 14 days before other social platforms on average — meaning you're reaching them earlier, with less competition from last-minute advertisers. Seasonal campaigns for Christmas, Valentine's Day, back-to-school, and summer launches perform exceptionally on Pinterest because users start planning far in advance.",
        "why_p3": "Lumo builds Pinterest advertising programs for consumer brands that combine visual creative excellence with performance targeting. We manage keyword targeting (Pinterest has a robust search advertising component), audience targeting, shopping catalogue connections, and creative formats — from standard Promoted Pins to video, carousel, and shopping ads — delivering measurable ROAS, not just impressions.",
        "services_h2": "Our Pinterest Advertising Services",
        "services": [
            ("📌", "Promoted Pins Management", "Keyword and interest-targeted Promoted Pin campaigns — static image ads in search and home feed placements — with bid management, audience targeting, and creative testing for brand awareness and direct response goals."),
            ("🛍️", "Pinterest Shopping Ads", "Product catalogue connection and Shopping ad campaigns — dynamic product ads showing specific products to users based on browsing behaviour, search history, and interest signals, with direct checkout integration."),
            ("🎬", "Video Pin Advertising", "Promoted Video Pins for brand storytelling, product demonstrations, and tutorial content — leveraging Pinterest's video inventory for higher engagement rates and stronger consideration-stage impact."),
            ("🎯", "Audience Targeting & Retargeting", "Actalike audience creation from customer lists, website visitor retargeting, engagement retargeting, and interest/keyword targeting — building audience strategies that reach the right users at each stage of the discovery journey."),
            ("🎨", "Pinterest Creative Production", "Pinterest-native creative design — vertical and square formats, Pin copy optimised for Pinterest search, lifestyle imagery that fits editorial context, and seasonal creative calendars aligned with Pinterest's 45-day advance planning cycle."),
            ("📊", "Pinterest Analytics & Reporting", "Campaign performance reporting — impressions, saves, link clicks, outbound clicks, ROAS, and revenue attribution — with monthly Pinterest audience insights and competitive creative benchmarking."),
        ],
        "process": [
            ("🔍", "Audit & Strategy", "Pinterest account audit, competitor Pin analysis, target audience research, keyword opportunity assessment, and campaign strategy — identifying the highest-opportunity ad formats and targeting approaches for your brand."),
            ("🎨", "Creative & Catalogue Setup", "Pinterest-native creative production, product catalogue connection (for Shopping ads), Pin copy and keyword optimisation, and campaign structure build — ready to launch with full creative asset sets."),
            ("🚀", "Launch & Optimise", "Campaign launch with daily monitoring for first 14 days, bid adjustments based on impression and click performance, creative A/B testing, and audience signal refinement as data accumulates."),
            ("📈", "Scale & Seasonal", "Scale winning ad sets, develop seasonal campaign calendar (Pinterest's advance planning requirement), expand to new audience segments, and refresh creative quarterly to maintain Pin performance."),
        ],
        "price_from": "$1,000",
        "price_note": "per month management fee — ad spend is separate (minimum $1,500/mo recommended)",
        "faqs": [
            ("Is Pinterest advertising suitable for my brand?", "Pinterest works best for consumer brands in verticals with strong visual content: home & furniture, fashion & apparel, beauty & skincare, food & recipes, travel, weddings & events, fitness, baby & kids, and DIY/crafts. B2B brands and services businesses typically see lower Pinterest ROI because the platform's user base is primarily consumer-focused and discovery-driven. Lumo will give you an honest assessment of Pinterest's potential for your specific category before recommending it."),
            ("How does Pinterest advertising differ from Instagram advertising?", "Both are visual platforms, but the user mindset differs. Instagram users browse passively and encounter ads in their feed. Pinterest users actively search for ideas and products — Pinterest has a search engine at its core. This intent difference makes Pinterest more effective for discovery and consideration-stage campaigns. Pinterest ads also have a longer shelf life — Pins continue receiving organic impressions long after the paid campaign ends, creating compounding content value."),
            ("What image specs and formats work best for Pinterest ads?", "Pinterest's recommended format is vertical (2:3 aspect ratio, 1000×1500px) — vertical Pins take up more screen real estate on mobile and generate higher engagement. Video Pins should be 15–60 seconds in vertical format. Creative should feature minimal text overlay (Pinterest's algorithm deprioritises heavy text), high-quality lifestyle imagery over product-only shots, and bright, eye-catching colours that stand out in the feed. Lumo produces Pinterest-native creative as part of every campaign."),
            ("How do you track conversions from Pinterest advertising?", "Pinterest conversion tracking uses the Pinterest Tag (similar to Meta Pixel) placed on your website. The tag tracks page views, add-to-cart events, checkout initiations, and purchases — connecting Pinterest ad clicks to on-site conversions. For leads, we track form submissions and phone click events. Pinterest also provides a View-Through Attribution window for conversions that happen after a Pin impression without a click — important for awareness-stage campaigns."),
            ("What's the minimum budget for Pinterest advertising?", "We recommend a minimum of $1,500/month in ad spend for Pinterest advertising to generate sufficient data for meaningful optimisation. Pinterest campaigns typically have higher CPCs than Facebook but lower than Google Search — the platform's sweet spot is upper-to-mid funnel where cost-per-impression is competitive. Lumo manages campaigns from $1,500/month with awareness that lower budgets extend the learning timeline."),
        ],
        "cta_h2": "Ready to Reach Buyers Who Are Actively Planning to Purchase?",
        "cta_sub": "Get a free Pinterest advertising audit — we'll assess your current account setup, creative quality, and targeting strategy, then show you the opportunity for your brand on Pinterest's high-intent discovery platform.",
        "schema_service_name": "Pinterest Advertising Services",
        "schema_service_desc": "Pinterest advertising management for US consumer brands — Promoted Pins, Shopping ads, video Pins, and audience targeting across 465M monthly active users.",
    },

    "snapchat-ads": {
        "title_tag":  "Snapchat Ads Agency | Snapchat Advertising for US Brands | Lumo AI",
        "meta_desc":  "Snapchat advertising management from Lumo AI Agency. Snap Ads, Story Ads, Collection Ads, AR Lenses, and audience targeting for US brands reaching 18–34 audiences. Free Snapchat audit.",
        "canonical":  "https://lumoaiagency.com/services/snapchat-ads",
        "og_title":   "Snapchat Ads Agency | Lumo AI Agency",
        "og_desc":    "Snapchat reaches 75% of 13–34 year olds in the US. Lumo builds Snapchat advertising programs for brands targeting younger audiences — Snap Ads, Story Ads, and AR experiences that convert.",
        "h1_html":    "Snapchat Ads That Reach <span class=\"hl-lime\">75% of Millennials</span> & Gen Z in the US",
        "badge":      "Snapchat Advertising Specialists",
        "lead":       "Snapchat reaches 75% of 13–34 year olds in the United States daily — an audience that's increasingly unreachable through traditional digital channels. For brands targeting Millennials and Gen Z, Snapchat offers immersive ad formats, AR experiences, and vertical video inventory that drives both brand awareness and direct response conversions.",
        "stat1_num": "75%",  "stat1_lbl": "Of US 13–34 year olds reached by Snapchat daily",
        "stat2_num": "5B",   "stat2_lbl": "Snaps created every day — engaged, active users",
        "stat3_num": "34%",  "stat3_lbl": "Higher purchase intent from Snapchat vs. other social platforms",
        "why_h2": "Why Snapchat Is the Under-Utilised Channel for Youth-Demographic Brands",
        "why_p1": "While every brand is fighting for the same Meta and TikTok audiences, Snapchat remains comparatively underutilised by advertisers — creating a competitive opportunity. CPMs on Snapchat are frequently lower than equivalent Meta placements, while the audience quality for 18–34 demographics is comparable or superior. Brands that identify this gap before their competitors do win audience share at lower cost.",
        "why_p2": "Snapchat's ad environment is also more attention-forcing than most platforms. Snaps are full-screen, vertical, and sound-on by default — the user's entire screen is your canvas. Unlike feed ads that compete with surrounding content, Snap Ads are the content during consumption. This immersive environment creates higher brand recall and stronger emotional responses than banner or feed-interruption formats.",
        "why_p3": "Lumo builds Snapchat advertising programs that leverage the platform's unique strengths: vertical video creative produced for sound-on viewing, AR Lens campaigns for experiential engagement, Snap Star partnerships for creator amplification, and Pixel-based retargeting for direct response performance. We connect Snapchat campaigns to measurable business outcomes — leads, installs, purchases — rather than treating the platform as a pure awareness channel.",
        "services_h2": "Our Snapchat Advertising Services",
        "services": [
            ("📸", "Snap Ads Management", "Full-screen vertical video and static Snap Ads in Stories, Discover, and Spotlight — with audience targeting by age, interest, behaviour, and lookalike audiences, plus swipe-up conversion tracking."),
            ("📖", "Story Ads", "Branded Tiles in the Discover section — curated Story collections that let users engage with multiple Snaps in sequence, ideal for product launches, seasonal campaigns, and editorial brand storytelling."),
            ("🛍️", "Collection Ads", "Shoppable Collection Ads featuring a hero video or image with four tappable product tiles — connecting Snapchat creative to product catalogue for direct purchase intent and e-commerce conversion."),
            ("🎭", "AR Lens Campaigns", "Sponsored AR Lens creation and distribution — branded augmented reality experiences (face Lenses, world Lenses) that users engage with and share organically, extending campaign reach beyond paid placements."),
            ("🎯", "Audience Targeting & Retargeting", "Snap Pixel retargeting, customer list matching, lookalike audience creation, and first-party data activation — building targeting strategies that reach high-value prospects and re-engage past visitors."),
            ("📊", "Snapchat Analytics & Reporting", "Pixel event tracking, swipe-up rate analysis, story completion rates, purchase attribution, and monthly reporting connecting Snapchat investment to revenue, installs, or leads."),
        ],
        "process": [
            ("🔍", "Audience & Audit", "Assess target demographic Snapchat presence, competitive creative analysis, Snap Pixel setup verification, and audience strategy — determining the right ad formats and campaign objectives for your goals."),
            ("🎨", "Creative Production", "Vertical video creative production in Snapchat-native format (9:16, 1080×1920px), sound-on scripting, on-screen text overlay, and brand-to-CTA pacing optimised for 6–15 second Snap attention windows."),
            ("🚀", "Launch & Monitor", "Campaign launch with Snap Pixel conversion monitoring, swipe-up rate tracking, frequency management, and creative A/B testing in the first 30 days to identify top-performing creative."),
            ("📈", "Optimise & Scale", "Scale best-performing ad sets, expand audiences, refresh creative every 4–6 weeks to combat ad fatigue, and test new formats (Collection, AR Lens) as campaign performance data matures."),
        ],
        "price_from": "$1,200",
        "price_note": "per month management fee — ad spend is separate (minimum $2,000/mo recommended)",
        "faqs": [
            ("Is Snapchat advertising right for my brand?", "Snapchat is most effective for brands with a 13–34 target audience — fashion, beauty, gaming, entertainment, consumer tech, food & beverage, fitness, and mobile apps. It's less suitable for B2B, professional services, or brands targeting 45+ audiences. Lumo will assess your target demographic against Snapchat's audience composition before recommending the platform. If your audience is there, Snapchat often offers lower CPMs than Meta for equivalent 18–24 targeting."),
            ("What creative format performs best on Snapchat?", "Vertical video (9:16 aspect ratio) significantly outperforms horizontal or square formats on Snapchat. Creative should be designed for sound-on viewing, with key messaging communicated in the first 2 seconds before swipe-away. Motion, bright colours, on-screen text captions, and direct calls-to-action ('Swipe Up to Shop') consistently outperform polished, slow-burn brand storytelling. Snapchat's creative norms are more similar to UGC than traditional advertising."),
            ("How does Snapchat's attribution work?", "Snapchat attribution uses the Snap Pixel for web conversion tracking and Snap App Ads for mobile app install tracking. The default attribution window is 28-day click, 1-day view for purchases, and 28-day click, 28-day view for other events. Snap's attribution model includes both swipe-up (click) and view-through (impression) attribution — it's important to understand the difference when comparing Snapchat performance to other channels, as view-through attribution can inflate reported conversions."),
            ("Can Snapchat drive direct purchases or just awareness?", "Snapchat can drive direct-response conversions — purchases, app installs, lead form submissions, and sign-ups — through Snap Pixel tracking, Collection Ads with product tiles, and Dynamic Ads connected to your product catalogue. Direct response performance is strongest for impulse purchases, app installs, and e-commerce brands with strong visual products. Higher-consideration purchases typically use Snapchat for awareness and retarget converters on other platforms."),
            ("What are Snapchat's AR Lens ads and are they worth the cost?", "AR Lens ads are sponsored augmented reality experiences — filters users can apply to their face or environment and share as Snaps. Lenses have historically had very high engagement rates (users spend 10–15 seconds on average interacting with a Lens) and strong earned reach (shared Snaps extend beyond paid distribution). However, custom Lens production costs ($10,000–$50,000 for premium lenses) mean they're most viable for large-brand awareness campaigns rather than direct-response programmes."),
        ],
        "cta_h2": "Ready to Reach the Millennial and Gen Z Audiences Your Competitors Are Missing?",
        "cta_sub": "Get a free Snapchat advertising audit — we'll assess your target audience's Snapchat presence, review your creative readiness, and map a campaign strategy built for the platform's unique format.",
        "schema_service_name": "Snapchat Advertising Services",
        "schema_service_desc": "Snapchat advertising management for US brands — Snap Ads, Story Ads, Collection Ads, AR Lenses, and audience targeting for 13–34 year old audiences.",
    },

    "twitter-ads": {
        "title_tag":  "X (Twitter) Ads Agency | Twitter Advertising Management | Lumo AI",
        "meta_desc":  "X (Twitter) advertising management from Lumo AI Agency. Promoted tweets, X campaigns, audience targeting, and conversion tracking for US brands. Reach 259M daily active users. Free audit.",
        "canonical":  "https://lumoaiagency.com/services/twitter-ads",
        "og_title":   "X (Twitter) Ads Agency | Lumo AI Agency",
        "og_desc":    "X (Twitter) is where conversations happen in real time. Lumo builds X advertising programs for US brands — Promoted Posts, Follower campaigns, and Trend Takeovers that drive awareness and direct response.",
        "h1_html":    "X (Twitter) Ads That Join <span class=\"hl-lime\">the Conversation</span> Your Customers Are Having",
        "badge":      "X / Twitter Advertising Specialists",
        "lead":       "X (Twitter) has 259 million daily active users, with disproportionate presence of journalists, professionals, tech decision-makers, and cultural influencers who shape mainstream opinion. For brands targeting professional, urban, and tech-forward audiences, X advertising provides reach that doesn't exist on other platforms.",
        "stat1_num": "259M", "stat1_lbl": "Daily monetisable active users on X globally",
        "stat2_num": "40%",  "stat2_lbl": "Of X users make purchase decisions based on content seen on platform",
        "stat3_num": "26%",  "stat3_lbl": "Higher purchase intent for brands that advertise on X",
        "why_h2": "Why X Is the Platform for Brands That Want to Be Part of the Cultural Conversation",
        "why_p1": "X's advertising value is driven by who's on the platform, not just how many. X users index heavily toward higher income, higher education, professional roles, and early adoption of new products and ideas. A brand that establishes presence on X reaches the opinion leaders and decision-makers who influence the purchasing behaviour of much broader audiences — the ripple effect of X engagement extends far beyond the platform itself.",
        "why_p2": "X advertising also has timing advantages that no other platform can match. Real-time conversation targeting lets you run campaigns aligned with breaking news, live events, sports, cultural moments, and trending topics — putting your brand in the context of what's happening right now. Event-based advertising on X (sports finals, award shows, product announcements) delivers relevance that pre-scheduled campaigns on other platforms can't replicate.",
        "why_p3": "Lumo builds X advertising programs around X's specific strengths: professional audience targeting by job title, employer, and follower interests; real-time conversation targeting using keywords and trending topics; and direct response campaigns that leverage X's high-engagement, text-forward environment. Every campaign is measured against real business outcomes — leads, sign-ups, or website conversions — not follower counts.",
        "services_h2": "Our X (Twitter) Advertising Services",
        "services": [
            ("📢", "Promoted Post Campaigns", "Promoted Post campaigns targeting specific audience segments — expanding your content reach to relevant users who don't follow your account, with optimisation for engagement, click-through, or conversion objectives."),
            ("👥", "Follower Growth Campaigns", "Follower campaigns to build your X audience — targeting users who follow competitors, industry publications, or specific professional categories, growing a high-quality owned audience for organic distribution."),
            ("🔥", "Trend & Keyword Targeting", "Real-time keyword targeting that inserts your brand into live trending conversations and event moments — connecting your messaging to high-engagement topics as they unfold."),
            ("🎯", "Professional Audience Targeting", "Job title, employer, follower interest, and device targeting — reaching professional decision-makers, industry influencers, and high-income consumers with precision unavailable on most social platforms."),
            ("🔄", "Retargeting & Conversion", "X Pixel website retargeting, engagement retargeting (targeting users who engaged with your previous Promoted Posts), and conversion campaigns optimising for lead form submissions, app installs, or website purchases."),
            ("📊", "X Analytics & Reporting", "Impression, engagement, click-through, and conversion reporting with audience insight analysis — monthly reporting connecting X ad investment to measurable business outcomes and earned reach metrics."),
        ],
        "process": [
            ("🔍", "Audience & Platform Audit", "Assess target audience X presence, competitor brand analysis, X Pixel setup verification, and campaign objective definition — determining the right campaign types and targeting for your goals."),
            ("📝", "Creative & Copy Strategy", "X-native ad copy development (280-character constraint), creative image and video formats, hashtag strategy, and post timing recommendations for maximum organic amplification alongside paid reach."),
            ("🚀", "Launch & Monitor", "Campaign launch with daily engagement and conversion monitoring, audience refinement based on early performance data, creative testing, and real-time event opportunity identification."),
            ("📈", "Optimise & Scale", "Scale best-performing audience segments, develop editorial content calendar for organic amplification, test new campaign objectives, and identify high-engagement moments for budget uplift."),
        ],
        "price_from": "$1,000",
        "price_note": "per month management fee — ad spend is separate (minimum $1,500/mo recommended)",
        "faqs": [
            ("Is X (Twitter) advertising effective for lead generation?", "X is most effective for brand awareness and professional audience reach rather than bottom-funnel lead generation at high volume. X's Lead Generation Card (native lead form within the platform) performs well for professional services, SaaS, and B2B brands where the target buyer is a heavy X user — typically tech, media, finance, and marketing professionals. For e-commerce and consumer product direct response, other platforms typically deliver lower CPLs."),
            ("How has X changed since Elon Musk's acquisition?", "Since the acquisition in 2022, X has undergone significant changes: the verified badge system was restructured (blue checkmarks now available by subscription), the API pricing changed for developers and third-party tools, some brand safety features were modified, and overall ad revenue declined as some major advertisers paused spending. X has since rebuilt some brand safety tools and many advertisers have returned. Lumo monitors X's ad platform changes and adjusts campaign strategies accordingly."),
            ("What ad formats are available on X?", "X offers: Promoted Posts (standard feed ads), Promoted Video (video in feed), Carousel Ads (multi-image format), App Cards (for app installs), Lead Generation Cards (native lead forms), Website Buttons (CTA links to landing pages), and Trend Takeovers (branded promoted trending topics — premium/reservation buy). Follower Campaigns promote your account rather than a specific post. Lumo selects formats based on your campaign objective and budget."),
            ("How do you target professional audiences on X?", "X's professional targeting options include: follower lookalike targeting (targeting users who follow specific accounts — competitors, industry publications, your own followers), keyword targeting (users who tweeted or engaged with specific keywords), interest targeting (categorised by over 350 interest categories), and job title/employer targeting through partnership data. For B2B brands, follower lookalike targeting against competitor accounts and industry publications is the most precise option available."),
            ("What budget is recommended for X advertising?", "We recommend a minimum of $1,500/month in ad spend for X advertising to generate sufficient impression volume for meaningful performance data. X CPMs are generally lower than Facebook for professional audiences, but conversion rates are also typically lower — X is better evaluated on reach and engagement metrics for brand objectives, with direct response performance benchmarked against awareness-stage CPMs rather than bottom-funnel CPA targets."),
        ],
        "cta_h2": "Ready to Join the Conversations Your Customers Are Already Having?",
        "cta_sub": "Get a free X advertising audit — we'll assess your target audience's X presence, review your current account setup, and map a campaign strategy that connects your brand to the conversations that matter.",
        "schema_service_name": "X (Twitter) Advertising Services",
        "schema_service_desc": "X (Twitter) advertising management for US brands — Promoted Posts, audience targeting, keyword campaigns, and professional-audience reach across 259M daily active users.",
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
        <li>AI-powered insights on every campaign</li>
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
          <li><a href="../services/google-shopping.html">Google Shopping</a></li>
          <li><a href="../services/performance-max.html">Performance Max</a></li>
          <li><a href="../services/meta-ads.html">Meta Ads</a></li>
          <li><a href="../services/tiktok-ads.html">TikTok Ads</a></li>
          <li><a href="../services/linkedin-ads.html">LinkedIn Ads</a></li>
          <li><a href="../services/pinterest-ads.html">Pinterest Ads</a></li>
          <li><a href="../services/twitter-ads.html">X / Twitter Ads</a></li>
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
