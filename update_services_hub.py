"""Regenerate services.html with all 105 service pages organized into 9 categories."""

CATEGORIES = [
    {
        "id": "ai-services",
        "label": "AI-First Services",
        "cat_class": "cat-ai",
        "h2": 'The AI <span class="hl-lime">Core Stack</span>',
        "sub": "These are the services that separate Lumo from every other agency — built on real machine learning, not marketing language.",
        "color": "lime",
        "services": [
            ("🤖", "AI Automations",       "End-to-end workflow automation using n8n, Make, Zapier, and custom Python pipelines. We eliminate manual tasks and build self-healing systems that scale.",                                   "90% reduction in manual ops time",    "ss-lime", "ai-automations"),
            ("⚙️", "AI Development",       "Custom LLM applications, RAG pipelines, AI agents, and model fine-tuning. We build production-grade AI systems tailored to your exact business logic.",                                   "Production-grade in 4–8 weeks",       "ss-lime", "ai-development"),
            ("🎙️", "Voice AI",             "Intelligent voice agents for inbound calls, appointment booking, lead qualification, and customer support — available 24/7 and indistinguishable from human agents.",                    "24/7 coverage, $0 overtime",          "ss-violet","voice-ai"),
            ("📤", "AI Outbound",          "Hyper-personalized outbound sequences powered by AI research, intent signals, and automated follow-up. Cold to closed in fewer touchpoints.",                                             "3x reply rates vs. manual outreach",  "ss-cyan",  "ai-outbound"),
            ("🌐", "GEO (AI SEO)",         "Generative Engine Optimization — get your brand cited by ChatGPT, Perplexity, and Google AI Overviews. The future of search visibility.",                                                "Cited in AI answers in 90 days",      "ss-lime",  "geo"),
            ("📦", "SaaS Products",        "We design and build AI-powered SaaS tools — from internal platforms to full white-label products. Stripe-integrated, launch-ready, and built on modern stack.",                          "MVP to launch in 6–10 weeks",         "ss-violet","saas-products"),
            ("🧠", "AI Consulting",        "Strategic AI advisory for businesses ready to deploy AI for real competitive advantage — from opportunity assessment to roadmap and vendor selection.",                                   "3.5x higher ROI with AI strategy",    "ss-lime",  "ai-consulting"),
            ("🤖", "AI Chatbot",           "Custom AI chatbots that qualify leads, answer questions, and book meetings 24/7 — trained on your business context and integrated with your CRM.",                                       "3x more leads vs. form-only sites",   "ss-cyan",  "ai-chatbot"),
            ("💬", "ChatGPT Optimization", "Optimize your brand visibility in ChatGPT, Claude, Perplexity, and AI search engines — where a billion users now discover brands and products.",                                         "58% of AI responses cite brands",     "ss-violet","chatgpt-optimization"),
            ("📝", "AI Content Strategy",  "AI-powered content creation at scale — SEO-optimized, on-brand, and human-edited. 10x your content output without 10x the headcount.",                                                 "10x content speed, same quality",     "ss-lime",  "ai-content"),
            ("🎨", "AI Ad Creative",       "AI-generated and human-refined ad creative that scales testing and maximizes ROAS — more variations, faster learning, better performance.",                                              "3.2x ROAS improvement with testing",  "ss-cyan",  "ai-ad-creative"),
            ("⚡", "Workflow Automation",  "Business process automation that eliminates manual work and scales your operations — using Zapier, Make, n8n, and native platform integrations.",                                        "40% of work tasks can be automated",  "ss-violet","workflow-automation"),
        ],
    },
    {
        "id": "seo-services",
        "label": "SEO & Organic Growth",
        "cat_class": "cat-marketing",
        "h2": 'SEO That <span class="hl-violet">Compounds</span>',
        "sub": "Technical foundations, content authority, and link equity — every SEO service engineered for sustainable organic growth.",
        "color": "violet",
        "services": [
            ("🔍", "SEO",                    "Technical SEO, AI-assisted content strategy, and authority link building — engineered to earn #1 rankings that compound over time.",                                                    "+280% avg. organic traffic",          "ss-lime",  "seo"),
            ("⚙️", "Technical SEO",          "Full technical audit and remediation: Core Web Vitals, crawlability, indexability, schema, site architecture, and page speed — the foundation all other SEO is built on.",            "Fixes that recover lost rankings",    "ss-violet","technical-seo"),
            ("📍", "Local SEO",              "Google Business Profile, local citations, and map pack optimization for businesses that need customers in their city — not just their industry.",                                       "#1 map pack ranking in 90 days",      "ss-cyan",  "local-seo"),
            ("🛒", "E-commerce SEO",         "Shopify, WooCommerce, and BigCommerce SEO — product schema, category pages, and AI content for maximum organic product visibility.",                                                   "+183% avg. organic revenue",          "ss-lime",  "ecommerce-seo"),
            ("🏢", "Enterprise SEO",         "Large-scale SEO programs for enterprise sites: multi-site management, advanced crawl budget, international SEO, and C-suite reporting.",                                               "Managed at site-wide scale",          "ss-violet","enterprise-seo"),
            ("🏪", "Franchise SEO",          "Unified SEO strategy for franchise networks — brand consistency, local relevance, and ranking at the national and location level simultaneously.",                                     "Rank nationally + locally",           "ss-cyan",  "franchise-seo"),
            ("💼", "B2B SEO",               "Pipeline-focused SEO for B2B companies: buyer-intent keyword targeting, gated content strategy, and thought leadership that drives qualified demo requests.",                          "3x pipeline growth in 12 months",     "ss-lime",  "b2b-seo"),
            ("🌍", "International SEO",      "Multi-language, multi-region SEO: hreflang, international site architecture, localization strategy, and country-specific ranking campaigns.",                                          "Rank in 10+ countries simultaneously","ss-violet","international-seo"),
            ("📱", "App Store Optimization", "iOS App Store and Google Play ranking optimization — keyword research, metadata, visual assets, and review strategy that drives organic app installs.",                                "+167% organic app installs",          "ss-cyan",  "app-store-optimization"),
            ("🔗", "Link Building",          "White-hat link acquisition: digital PR, niche edits, content-led outreach, and resource link building — earning backlinks that move rankings.",                                        "Domain authority growth in 6 months", "ss-lime",  "link-building"),
            ("🛍️", "Shopify SEO",           "Shopify-specific technical SEO: canonical tags, duplicate content, product page optimization, and schema markup that drives organic store revenue.",                                   "+43% organic traffic to stores",      "ss-violet","shopify-seo"),
        ],
    },
    {
        "id": "paid-advertising",
        "label": "Paid Advertising",
        "cat_class": "cat-marketing",
        "h2": 'Paid Media That <span class="hl-violet">Performs</span>',
        "sub": "Every ad platform managed with AI bidding, advanced tracking, and creative testing — from Google to TikTok to Connected TV.",
        "color": "violet",
        "services": [
            ("📈", "Google Ads",              "Search, Performance Max, and YouTube campaigns managed with AI bidding, advanced conversion tracking, and daily optimization routines.",                                                 "7.2x average ROAS",                   "ss-violet","google-ads"),
            ("📱", "Meta Ads",               "Facebook and Instagram ad systems built for scale — creative testing frameworks, pixel architecture, and AI-powered audience segmentation.",                                             "6.8x average ROAS",                   "ss-cyan",  "meta-ads"),
            ("💡", "PPC Management",         "Full-funnel paid media management across Google, Bing, and display networks — with AI-driven bid management and weekly performance reports.",                                            "30% lower CPL on average",            "ss-lime",  "ppc"),
            ("💼", "LinkedIn Ads",           "B2B pipeline generation via LinkedIn's professional targeting — Lead Gen Forms, ICP audience layers, and AI-optimized bidding for decision-maker leads.",                               "CPL $60–$200 for enterprise buyers",  "ss-violet","linkedin-ads"),
            ("🎵", "TikTok Ads",            "Native creative campaigns that convert — UGC-style video, TopView, and AI-powered creative testing to find your winning content formula fast.",                                          "2–5x ROAS on proven creative",        "ss-lime",  "tiktok-ads"),
            ("▶️", "YouTube Ads",           "Full-funnel YouTube campaigns — TrueView, bumpers, and non-skippable ads with custom intent audiences and AI-assisted script optimization.",                                             "Full-funnel from awareness to close", "ss-cyan",  "youtube-ads"),
            ("🔵", "Bing Ads",              "Microsoft Ads management — capturing the 30% of search volume Google misses, at lower CPCs and with less advertiser competition.",                                                       "30% lower CPC than Google avg.",      "ss-violet","bing-ads"),
            ("🛒", "Google Shopping",       "Product feed optimization and Shopping campaign management — more product visibility, better ROAS, and lower CPC across every category.",                                                "2.4x ROAS with optimized feeds",      "ss-lime",  "google-shopping"),
            ("🚀", "Performance Max",       "AI-powered Performance Max campaigns built for profitability — asset groups, audience signals, and budget controls that let Google's AI work for you.",                                  "Full Google inventory in one campaign","ss-cyan",  "performance-max"),
            ("📌", "Pinterest Ads",         "High-intent shopping and discovery ads on Pinterest — capturing buyers in the research and planning phase before they search on Google.",                                                "2x longer purchase consideration",    "ss-violet","pinterest-ads"),
            ("👻", "Snapchat Ads",          "Mobile-first Snap ads targeting Gen Z and Millennial audiences — AR lenses, Story ads, and Snap-native creative that drives app installs and purchases.",                               "86% of users aged 13–34",             "ss-lime",  "snapchat-ads"),
            ("🐦", "Twitter/X Ads",        "X (Twitter) ad campaigns for brand awareness, follower growth, and website traffic — targeting by interest, keyword, and follower lookalikes.",                                          "Engage 350M+ monthly active users",   "ss-cyan",  "twitter-ads"),
            ("📡", "Programmatic Ads",      "Data-driven display and video advertising across thousands of publisher sites — using DMP audience targeting, contextual signals, and real-time bidding.",                               "Reach your ICP across the web",       "ss-violet","programmatic-advertising"),
            ("🎯", "Retargeting",           "Multi-channel retargeting campaigns that re-engage visitors who didn't convert — Meta, Google Display, LinkedIn, and programmatic working in concert.",                                  "10x more likely to convert vs. cold", "ss-lime",  "retargeting"),
            ("📺", "Connected TV Ads",      "CTV and OTT advertising on Hulu, Roku, Peacock, and streaming apps — reaching cord-cutters with unskippable video where they actually watch content.",                                  "147M US households reachable via CTV","ss-cyan",  "connected-tv-advertising"),
            ("🍎", "Apple Search Ads",      "App Store search advertising on iOS — keyword-targeted ads that appear when users search the App Store, driving high-intent app installs.",                                              "65% of downloads come from search",   "ss-violet","apple-search-ads"),
            ("🎵", "Audio Advertising",     "Programmatic audio ads on Spotify, Pandora, and podcast networks — reaching engaged listeners when they can't scroll past your message.",                                               "182M US podcast listeners in 2023",   "ss-lime",  "audio-advertising"),
            ("🏬", "Walmart Advertising",   "Walmart Connect search and display ads — sponsored products and brand placements that capture Walmart.com's 120M monthly shoppers.",                                                     "Walmart: 120M monthly shoppers",      "ss-cyan",  "walmart-advertising"),
            ("📻", "Google Local Services", "Google Local Services Ads for service businesses — pay-per-lead, Google Guaranteed badge, and top-of-search placement for local service queries.",                                       "Pay per lead, not per click",         "ss-violet","google-local-services-ads"),
        ],
    },
    {
        "id": "content-creative",
        "label": "Content & Creative",
        "cat_class": "cat-ai",
        "h2": 'Content That <span class="hl-lime">Converts</span>',
        "sub": "From blog articles to video production to UGC — content strategy and creative production that builds authority and drives revenue.",
        "color": "lime",
        "services": [
            ("📝", "Content Marketing",    "AI-augmented content strategy, long-form SEO articles, thought leadership, and brand storytelling — all crafted to rank and resonate.",                                                "3x lead volume increase",              "ss-lime",  "content-marketing"),
            ("✍️", "Blog Writing",         "SEO-optimized blog content researched and written by subject-matter experts — building topical authority and organic traffic that compounds.",                                         "6x more leads for active bloggers",    "ss-violet","blog-writing"),
            ("🎬", "Video Marketing",      "End-to-end video content strategy: scripting, production coordination, editing, YouTube SEO, and multi-platform distribution for maximum reach.",                                      "+88% time on page with video",         "ss-cyan",  "video-marketing"),
            ("🎞️", "Video Production",    "Professional video production for brand films, product demos, testimonials, and social content — scripted, filmed, and edited by our production team.",                               "3x engagement vs. static content",     "ss-lime",  "video-production"),
            ("📊", "Infographic Design",   "Data-driven infographics that earn backlinks, get shared, and simplify complex ideas — research, design, and outreach package included.",                                              "40x more shared than plain text",      "ss-violet","infographic-design"),
            ("🎯", "Performance Creative", "Ad creative engineered for ROAS — static, video, and copy variants designed for systematic testing with media buying strategy built in.",                                              "70% of ad results driven by creative", "ss-cyan",  "performance-creative"),
            ("🎙️", "Podcast Marketing",   "Podcast launch, production, and growth strategy — audio editing, show notes, multi-platform distribution, and listener acquisition campaigns.",                                        "80% of listeners finish episodes",     "ss-lime",  "podcast-marketing"),
            ("📱", "UGC Marketing",        "Authentic user-generated content sourced, directed, and deployed across paid and organic channels — 4x higher CTR than branded creative.",                                            "79% of buyers trust UGC over ads",     "ss-violet","ugc-marketing"),
            ("📖", "Brand Storytelling",   "Narrative strategy and content that builds emotional connection — founder story, messaging architecture, customer transformation, and social storytelling.",                            "22x more memorable than facts alone",  "ss-cyan",  "brand-storytelling"),
            ("✏️", "Copywriting",          "Conversion-focused copy for websites, landing pages, ads, and email — written by direct-response specialists who understand persuasion and your audience.",                            "Clear copy doubles conversion rates",  "ss-lime",  "copywriting"),
            ("🎨", "Branding",             "Visual brand identity systems — logo, color palette, typography, brand guidelines, and collateral designed for consistency and recognition across channels.",                           "Brand consistency = 3.5x revenue",     "ss-violet","branding"),
            ("🤳", "Influencer Marketing", "Influencer partnerships for brand awareness and conversions — creator sourcing, campaign management, and performance tracking across Instagram, TikTok, and YouTube.",                "Influencer content = 11x higher ROI",  "ss-cyan",  "influencer-marketing"),
            ("📸", "Product Photography",  "High-conversion product photography for e-commerce, Amazon, and social media — studio shots, lifestyle imagery, and composite infographics.",                                         "93% of purchases influenced by visuals","ss-lime",  "product-photography"),
            ("📲", "Social Media",         "AI-assisted content creation, scheduling, and community management across LinkedIn, Instagram, X, and TikTok — with performance analytics.",                                          "4x organic reach increase",            "ss-violet","social-media"),
        ],
    },
    {
        "id": "ecommerce-services",
        "label": "E-commerce",
        "cat_class": "cat-dev",
        "h2": 'E-commerce That <span class="hl-cyan">Scales</span>',
        "sub": "Every channel, every marketplace, every platform — full-stack e-commerce marketing and operations for stores that want to grow.",
        "color": "cyan",
        "services": [
            ("🛒", "Amazon Marketing",         "Full Amazon channel management — listing optimization, A+ content, Sponsored Ads, and Brand Store design for maximum marketplace visibility.",               "83% of product searches start on Amazon","ss-lime",  "amazon-marketing"),
            ("📦", "Amazon Store Management",  "End-to-end Amazon management: listing optimization, A+ content, PPC, Buy Box strategy, inventory, and review velocity for marketplace growth.",             "Buy Box wins = 82% of all sales",        "ss-violet","amazon-store-management"),
            ("🏭", "Amazon FBA",              "FBA operations: inventory planning, shipment management, fee optimization, stranded inventory resolution, and profitability analysis by ASIN.",              "$15B paid in unnecessary FBA fees/yr",   "ss-cyan",  "amazon-fba"),
            ("🛍️", "Shopify Development",     "Conversion-optimized Shopify stores — custom theme development, app integrations, checkout optimization, and performance-first builds.",                    "+190% avg. conversion rate lift",        "ss-lime",  "shopify-development"),
            ("🔍", "Shopify SEO",             "Shopify-specific SEO: canonical fixes, duplicate content, product page optimization, and schema — driving sustainable organic revenue.",                    "+43% organic traffic to stores",         "ss-violet","shopify-seo"),
            ("🟣", "WooCommerce Marketing",   "Full-stack marketing for WooCommerce stores — SEO, Google Shopping, Meta Ads, and email automation configured for WordPress and WooCommerce.",              "28% of all online stores use WooCommerce","ss-cyan", "woocommerce-marketing"),
            ("📡", "Shopping Feed Management","Product feed optimization across Google Shopping, Meta, and marketplaces — better titles, attributes, and custom labels for higher ROAS.",                  "2.4x ROAS with optimized feeds",         "ss-lime",  "shopping-feed-management"),
            ("🛍️", "Social Commerce",        "Sell directly on Instagram Shop, TikTok Shop, Pinterest, and Facebook — catalog setup, shoppable content, and live shopping management.",                   "$1.2T in social commerce sales by 2025", "ss-violet","social-commerce"),
            ("🖥️", "Ecommerce Web Design",   "High-converting e-commerce websites — mobile-first, sub-2s load times, integrated with your marketing stack, and built for conversion.",                    "+190% avg. conversion rate lift",        "ss-cyan",  "ecommerce-web-design"),
            ("🏪", "Listings Management",     "Business listings accuracy across 70+ directories — Google, Yelp, Apple Maps, and industry directories — eliminating NAP inconsistencies that hurt rankings.", "73% lose trust over inaccurate listings","ss-lime", "listings-management"),
        ],
    },
    {
        "id": "lead-gen",
        "label": "Lead Generation & Sales",
        "cat_class": "cat-marketing",
        "h2": 'Pipeline Built to <span class="hl-violet">Convert</span>',
        "sub": "From cold outreach to warm referrals — systematic lead generation programs that fill your pipeline with qualified, sales-ready opportunities.",
        "color": "violet",
        "services": [
            ("🎯", "Lead Generation",           "Multi-channel lead generation programs — search, social, and content working together to consistently fill your pipeline with qualified prospects.",                                  "CPL reduction of 33% on average",     "ss-lime",  "lead-generation"),
            ("📤", "Outbound Sales",            "Fully managed outbound sales programs — target list building, personalized sequences, and follow-up management that books qualified meetings.",                                     "80% of sales need 5+ follow-ups",     "ss-violet","outbound-sales"),
            ("📧", "Cold Email Outreach",       "Cold email campaigns built for deliverability and reply rates — domain infrastructure, personalized sequences, and A/B tested messaging.",                                          "3x reply rates vs. industry avg.",    "ss-cyan",  "cold-email-outreach"),
            ("📅", "Appointment Setting",       "Qualified sales meetings booked directly to your calendar — ICP targeting, multi-touch sequences, and show-rate optimization by our outreach team.",                               "6–12 qualified meetings/mo avg.",     "ss-lime",  "appointment-setting"),
            ("🏢", "Account-Based Marketing",  "ABM programs targeting your highest-value accounts — personalized content, coordinated multi-channel outreach, and account-level analytics.",                                        "200% higher deal values vs. inbound", "ss-violet","account-based-marketing"),
            ("🤝", "Referral Marketing",        "Systematic referral programs that turn customers into your best sales channel — incentive design, automation, and program management.",                                              "3–5x higher conversion for referrals","ss-cyan",  "referral-marketing"),
            ("🌱", "Lead Nurture",              "Multi-channel nurture sequences that move cold leads to sales-ready opportunities — email, retargeting, and behavioral triggers working together.",                                 "50% more sales-ready leads with nurture","ss-lime","lead-nurture"),
            ("🔄", "Sales Funnel Automation",  "Automated sales funnels that capture, nurture, and convert leads without manual follow-up — built in your marketing automation platform.",                                           "5x revenue for mature automation",    "ss-violet","sales-funnel-automation"),
            ("🔗", "Affiliate Marketing",       "Affiliate program setup and management — recruiter affiliates, commission structure, tracking, and compliance for performance-based partner revenue.",                              "Affiliate marketing = 15% of revenue", "ss-cyan", "affiliate-marketing"),
        ],
    },
    {
        "id": "design-dev",
        "label": "Design & Development",
        "cat_class": "cat-dev",
        "h2": 'Built to <span class="hl-cyan">Convert</span>',
        "sub": "Design and development services engineered for performance — from websites and apps to logos and landing pages.",
        "color": "cyan",
        "services": [
            ("🖥️", "Web Design & Dev",         "Conversion-engineered websites and web apps — sub-2s load times, mobile-first, CRM-integrated, and built to scale.",                                                                "+190% avg. conversion rate lift",     "ss-cyan",  "web-design"),
            ("🧪", "CRO",                       "A/B testing, heatmap analysis, GA4 funnel diagnostics, and landing page optimization — systematic conversion improvement that compounds.",                                           "+47% avg. CVR improvement",           "ss-lime",  "cro"),
            ("📝", "WordPress Development",     "Custom WordPress development — bespoke themes, plugin development, WooCommerce integration, and performance optimization for content-heavy sites.",                                   "44% of all websites run WordPress",   "ss-violet","wordpress-development"),
            ("🔧", "Website Maintenance",       "Ongoing website maintenance — security updates, backups, uptime monitoring, content updates, and performance optimization. Your site, always healthy.",                               "99.9% uptime guarantee",              "ss-cyan",  "website-maintenance"),
            ("🔄", "Website Redesign",          "Strategic website redesigns that improve conversion, modernize design, and fix technical debt — without losing your organic search rankings.",                                        "+190% conversion rate after redesign","ss-lime",  "website-redesign"),
            ("📱", "Mobile App Development",    "Native and cross-platform mobile apps for iOS and Android — React Native or Flutter, full backend integration, and App Store submission.",                                            "6.8B smartphone users worldwide",     "ss-violet","mobile-app-development"),
            ("✏️", "Logo Design",               "Memorable logos designed to last — 3 original concepts, 2 revision rounds, complete file package (SVG, PNG, PDF), and full IP transfer.",                                            "7 seconds to form a brand impression","ss-cyan",  "logo-design"),
            ("🎨", "Graphic Design",            "On-brand visual design for every channel — social media graphics, digital ad creative, email templates, print collateral, and presentations.",                                        "94% of first impressions design-related","ss-lime","graphic-design"),
            ("📱", "Social Media Design",       "Scroll-stopping social media visual systems — custom template libraries, platform-specific formats, and campaign creative for every platform.",                                       "6x conversion with consistent branding","ss-violet","social-media-design"),
            ("📊", "Pitch Deck Design",         "Investor-ready pitch decks — narrative consulting, custom slide design, data visualization, and delivery in PowerPoint, Google Slides, and PDF.",                                   "3 min: avg. investor review time",    "ss-cyan",  "pitch-deck-design"),
            ("♿", "ADA Compliance",            "WCAG 2.1 AA compliance for your website — accessibility audit, remediation, and ongoing monitoring to avoid ADA lawsuits and serve all users.",                                      "26% of adults have a disability",     "ss-lime",  "ada-compliance"),
            ("⚡", "Website Speed Optimization","Core Web Vitals optimization — LCP, CLS, and INP improvements that improve rankings, reduce bounce rate, and increase conversions.",                                                  "1s delay = 7% conversion drop",       "ss-violet","website-speed-optimization"),
        ],
    },
    {
        "id": "analytics-strategy",
        "label": "Analytics & Strategy",
        "cat_class": "cat-ai",
        "h2": 'Decisions Backed by <span class="hl-lime">Data</span>',
        "sub": "From attribution modeling to competitive intelligence — the analytical foundation that makes every marketing dollar more accountable.",
        "color": "lime",
        "services": [
            ("📊", "Marketing Analytics",      "Full-funnel data visibility — tracking setup, data integration, custom dashboards, and monthly performance reviews that drive better decisions.",                                    "5x ROI for data-driven marketers",    "ss-lime",  "marketing-analytics"),
            ("🎯", "Conversion Tracking",      "Bulletproof cross-channel conversion tracking — server-side tracking, GA4 events, and Conversions API for every ad platform. No more lost data.",                                  "40% of conversions lost without SSGT","ss-violet","conversion-tracking"),
            ("🗺️", "Marketing Attribution",   "Multi-touch attribution modeling that reveals which channels truly drive revenue — beyond last-click, toward accurate budget allocation.",                                            "23% budget freed with right attribution","ss-cyan","marketing-attribution"),
            ("🔍", "Competitor Analysis",      "Deep competitive intelligence — SEO, paid advertising, content, positioning, and pricing — mapped into a 90-day action plan.",                                                       "90% of Fortune 500 use CI",           "ss-lime",  "competitor-analysis"),
            ("📋", "Marketing Strategy",       "Data-driven marketing strategy: customer research, ICP definition, channel mix, budget modeling, and 12-month roadmap — built on real data.",                                       "3x higher ROI with documented strategy","ss-violet","marketing-strategy"),
            ("🔗", "Revenue Operations",       "RevOps: aligning sales, marketing, and CS around a unified revenue engine — CRM architecture, pipeline, forecasting, and workflow automation.",                                     "19% faster revenue growth with RevOps","ss-cyan",  "revenue-operations"),
            ("🧪", "A/B Testing",              "Systematic experimentation that compounds conversion gains — test roadmap, heatmap analysis, variant design, and statistically rigorous analysis.",                                  "1.5–3x CVR after 12 months of testing","ss-lime", "ab-testing"),
            ("✨", "Website Personalization",  "Dynamic website experiences tailored to each visitor segment — more relevance, more conversions, and measurable lift tracked by segment.",                                            "2.5x higher CVR with personalization", "ss-violet","website-personalization"),
        ],
    },
    {
        "id": "marketing-ops",
        "label": "Marketing Operations & Automation",
        "cat_class": "cat-marketing",
        "h2": 'Operations That <span class="hl-violet">Scale</span>',
        "sub": "CRM setup, email automation, marketing operations, and multi-location systems that let your team do more without growing headcount.",
        "color": "violet",
        "services": [
            ("✉️", "Email Marketing",            "AI-personalized email sequences, list segmentation, deliverability optimization, and behavioral triggers that convert subscribers into customers.",                                 "45% open rates (2x industry avg)",   "ss-violet","email-marketing"),
            ("📱", "SMS Marketing",              "SMS marketing campaigns and automation — promotional messages, abandoned cart recovery, and appointment reminders with 98% open rates.",                                           "98% SMS open rate vs. 20% email",    "ss-lime",  "sms-marketing"),
            ("⚙️", "Marketing Automation",       "Marketing automation programs that nurture leads, trigger campaigns by behavior, and score prospects — turning your CRM into a revenue machine.",                                  "5x revenue for automation-mature orgs","ss-cyan",  "marketing-automation"),
            ("🗃️", "CRM Setup",                 "CRM implementation, data migration, workflow automation, and team training — configured to your actual sales process, not a generic template.",                                    "29% sales productivity increase",    "ss-lime",  "crm-setup"),
            ("🏢", "Franchise Marketing",        "Scalable marketing systems for franchise networks — centralized strategy, templated local execution, and multi-location reporting.",                                               "2.3x growth with central marketing", "ss-violet","franchise-marketing"),
            ("🗺️", "Multi-Location Marketing",  "Unified digital marketing for businesses with 2–200+ locations — local SEO, geo-targeted ads, and centralized performance reporting.",                                             "46% of Google searches have local intent","ss-cyan","multi-location-marketing"),
            ("📣", "Reputation Management",      "Online reputation strategy — monitoring, response protocols, review generation, and recovery playbooks across Google, Yelp, and review platforms.",                               "88% trust online reviews as much as referrals","ss-lime","reputation-management"),
            ("⭐", "Review Management",          "Systematic review generation and management — compliant review requests, response workflows, and reputation monitoring across all platforms.",                                      "91% read reviews before buying",     "ss-violet","review-management"),
            ("🌐", "White-Label Marketing",      "White-label marketing services for agencies — our services delivered under your brand, with agency-grade quality and zero overhead.",                                              "Expand service offerings in 30 days", "ss-cyan",  "white-label-marketing"),
            ("📍", "Google Business Profile",    "Google Business Profile setup, optimization, and ongoing management — posts, photos, Q&A, and attributes that drive calls, direction requests, and website visits.",              "97% of consumers research locally",  "ss-lime",  "google-business-profile"),
        ],
    },
]

HERO_SECTION = """  <section class="page-hero" aria-label="Lumo Services">
    <div class="blob-wrap" aria-hidden="true"><div class="blob blob-lime"></div><div class="blob blob-violet"></div></div>
    <div class="hero-noise" aria-hidden="true"></div>
    <div class="container page-hero-inner">
      <p class="section-eyebrow">What We Build</p>
      <h1>105 Growth Services,<br/><span class="hl-lime">One Agency</span></h1>
      <p class="lead">From AI automations and custom LLM development to SEO, paid ads, e-commerce, and brand design — every service engineered to compound your growth.</p>
      <div style="display:flex;gap:14px;flex-wrap:wrap;">
        <a href="/contact.html" class="btn btn-lime">Get Free Proposal <svg width="16" height="16" viewBox="0 0 16 16" fill="none" aria-hidden="true"><path d="M3 8h10M9 4l4 4-4 4" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg></a>
        <a href="/pricing.html" class="btn btn-ghost">View Pricing</a>
      </div>
    </div>
  </section>"""

INDUSTRY_SECTION = """  <section class="services-section" id="industries" aria-labelledby="ind-h2">
    <div class="container">
      <div class="category-label cat-ai">By Industry</div>
      <h2 class="section-h2" id="ind-h2">Specialist Marketing for <span class="hl-lime">Your Industry</span></h2>
      <p class="section-sub">Generic agency playbooks don't work. Every industry has unique search behaviour, compliance requirements, and conversion dynamics — we build strategies that reflect that.</p>
      <div class="services-grid">
        <article class="svc-card lime"><div class="svc-icon si-lime">⚖️</div><h3 class="svc-title">Law Firms &amp; Lawyers</h3><p class="svc-desc">E-E-A-T-focused SEO, local map pack rankings, and compliant content marketing that fills your consultation calendar with high-value clients.</p><a href="/industries/seo-for-lawyers/" class="svc-link">Learn more →</a></article>
        <article class="svc-card violet"><div class="svc-icon si-violet">🦷</div><h3 class="svc-title">Dentists &amp; Dental Clinics</h3><p class="svc-desc">Local SEO, Google Maps, and review strategy that puts your practice in the top 3 map results for 'dentist near me' — booking more new patients every week.</p><a href="/industries/seo-for-dentists/" class="svc-link">Learn more →</a></article>
        <article class="svc-card cyan"><div class="svc-icon si-cyan">🏠</div><h3 class="svc-title">Real Estate &amp; Realtors</h3><p class="svc-desc">Hyperlocal SEO, Google Ads, and neighbourhood content that generates a consistent flow of qualified buyer and seller leads from organic and paid search.</p><a href="/industries/digital-marketing-for-real-estate/" class="svc-link">Learn more →</a></article>
        <article class="svc-card lime"><div class="svc-icon si-lime">🍽️</div><h3 class="svc-title">Restaurants &amp; Food</h3><p class="svc-desc">Google Maps rankings, review management, and social media content that drives consistent foot traffic and fills tables for dine-in and delivery.</p><a href="/industries/restaurant-marketing/" class="svc-link">Learn more →</a></article>
        <article class="svc-card violet"><div class="svc-icon si-violet">🏥</div><h3 class="svc-title">Healthcare &amp; Medical</h3><p class="svc-desc">HIPAA-aware patient acquisition SEO — ranking your practice for specialty and condition searches that attract new patients actively looking for care.</p><a href="/industries/healthcare-seo/" class="svc-link">Learn more →</a></article>
        <article class="svc-card cyan"><div class="svc-icon si-cyan">🛍️</div><h3 class="svc-title">E-commerce &amp; Retail</h3><p class="svc-desc">Shopify SEO, Google Shopping, Meta Ads, and CRO for online stores — driving sustainable organic revenue growth that compounds month over month.</p><a href="/industries/ecommerce-marketing/" class="svc-link">Learn more →</a></article>
        <article class="svc-card lime"><div class="svc-icon si-lime">💻</div><h3 class="svc-title">SaaS &amp; Tech Startups</h3><p class="svc-desc">Pipeline-focused SEO, LinkedIn Ads, and comparison content designed for the SaaS acquisition model — from top-of-funnel awareness to demo bookings.</p><a href="/industries/saas-marketing/" class="svc-link">Learn more →</a></article>
        <article class="svc-card violet"><div class="svc-icon si-violet">🔧</div><h3 class="svc-title">Home Services</h3><p class="svc-desc">Local SEO, Google Local Services Ads, and review generation for HVAC, plumbing, roofing, and home services — booking more jobs from Google every week.</p><a href="/industries/home-services-seo/" class="svc-link">Learn more →</a></article>
        <article class="svc-card cyan"><div class="svc-icon si-cyan">💰</div><h3 class="svc-title">Financial Services</h3><p class="svc-desc">Compliance-aware SEO and content marketing for financial advisors, insurance agencies, mortgage brokers, and fintech — building trust and qualified lead flow.</p><a href="/industries/financial-services-marketing/" class="svc-link">Learn more →</a></article>
        <article class="svc-card lime"><div class="svc-icon si-lime">🚗</div><h3 class="svc-title">Automotive</h3><p class="svc-desc">Dealership SEO, Google Vehicle Listing Ads, and local marketing for auto repair shops and automotive businesses — driving showroom visits and service bookings.</p><a href="/industries/automotive-seo/" class="svc-link">Learn more →</a></article>
      </div>
    </div>
  </section>"""

CTA_SECTION = """  <section class="cta-band" aria-labelledby="cta-h2">
    <div class="container">
      <p class="section-eyebrow" style="justify-content:center;">Ready to Scale?</p>
      <h2 id="cta-h2">Deploy AI. <span style="color:var(--primary);">Grow Faster.</span></h2>
      <p>Book a free strategy call and we'll show you exactly which services will move the needle for your business — with projected ROI.</p>
      <div class="cta-btns">
        <a href="/contact.html" class="btn btn-lime">Get Free Proposal <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14M12 5l7 7-7 7"/></svg></a>
        <a href="/pricing.html" class="btn btn-ghost">View Pricing</a>
      </div>
    </div>
  </section>"""

def build_service_card(color, icon, title, desc, stat, stat_class, slug):
    si_class = f"si-{color}"
    card_color = color
    return f"""        <article class="svc-card {card_color}">
          <div class="svc-icon {si_class}">{icon}</div>
          <h3 class="svc-title">{title}</h3>
          <p class="svc-desc">{desc}</p>
          <span class="svc-stat {stat_class}">{stat}</span>
          <a href="/services/{slug}.html" class="svc-link">Learn more →</a>
        </article>"""

def build_section(cat):
    cards = ""
    for svc in cat["services"]:
        icon, title, desc, stat, stat_class, slug = svc
        cards += "\n" + build_service_card(cat["color"], icon, title, desc, stat, stat_class, slug)
    return f"""  <section class="services-section" id="{cat['id']}" aria-labelledby="{cat['id']}-h2">
    <div class="container">
      <div class="category-label {cat['cat_class']}">{cat['label']}</div>
      <h2 class="section-h2" id="{cat['id']}-h2">{cat['h2']}</h2>
      <p class="section-sub">{cat['sub']}</p>
      <div class="services-grid">{cards}
      </div>
    </div>
  </section>"""

# Read the existing file to preserve head, nav, and footer
with open("services.html", "r", encoding="utf-8") as f:
    original = f.read()

# Extract head section (up to and including <body>)
head_end = original.index("<main>")
head = original[:head_end]

# Extract footer+script section
footer_start = original.index("<footer")
footer = original[footer_start:]

# Update title and description in head
head = head.replace(
    '<title>AI Growth Services — All 19 Services | Lumo Agency</title>',
    '<title>All 105 AI Growth Services | Lumo AI Agency</title>'
)
head = head.replace(
    'content="Lumo\'s full suite of 19 AI-powered growth services',
    'content="Lumo\'s full suite of 105 AI-powered growth services'
)
head = head.replace(
    'content="19 AI-powered services to grow your business',
    'content="105 AI-powered services to grow your business'
)
head = head.replace(
    '"description": "All 19 AI-powered growth services offered by Lumo Agency."',
    '"description": "All 105 AI-powered growth services offered by Lumo AI Agency."'
)
head = head.replace(
    '"dateModified": "2026-05-13"',
    '"dateModified": "2026-05-14"'
)

# Build new main section
main_parts = ["<main>", HERO_SECTION]
for cat in CATEGORIES:
    main_parts.append(build_section(cat))
main_parts.append(INDUSTRY_SECTION)
main_parts.append(CTA_SECTION)
main_parts.append("</main>")
main_html = "\n\n".join(main_parts)

# Combine all parts
new_html = head + "\n" + main_html + "\n\n" + footer

with open("services.html", "w", encoding="utf-8") as f:
    f.write(new_html)

# Count services
total = sum(len(c["services"]) for c in CATEGORIES)
print(f"Done. {total} service cards across {len(CATEGORIES)} categories.")
print(f"File size: {len(new_html):,} chars")
