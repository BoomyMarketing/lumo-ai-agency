#!/usr/bin/env python3
"""Generate 10 industry vertical pages under /industries/{slug}/index.html."""
import os, json

BASE = os.path.dirname(os.path.abspath(__file__))

# ---------------------------------------------------------------------------
# INDUSTRY DATA
# ---------------------------------------------------------------------------
INDUSTRIES = {
    "seo-for-lawyers": {
        "label":      "Law Firms & Lawyers",
        "slug":       "seo-for-lawyers",
        "icon":       "⚖️",
        "title_tag":  "SEO for Law Firms & Lawyers | Lumo AI Agency Austin TX",
        "meta_desc":  "Specialist SEO and digital marketing for law firms across the US. Lumo AI Agency helps attorneys rank on Google, appear in AI search, and generate high-value client leads. Book a free strategy call.",
        "og_title":   "SEO for Law Firms | Lumo AI Agency",
        "og_desc":    "Law firm SEO that fills your consultation calendar — technical SEO, local SEO, content authority, and AI search visibility. Results-focused. Free audit.",
        "h1":         "SEO for Law Firms & <span class=\"hl-lime\">Lawyers</span>",
        "hero_badge": "Legal Industry Specialists",
        "hero_sub":   "Rank on Google and get cited in AI search — so the right clients find you before they find your competitors.",
        "stat1_num": "4.1x", "stat1_lbl": "Average ROI for law firm SEO clients",
        "stat2_num": "68%",  "stat2_lbl": "Of legal searches start on Google",
        "stat3_num": "90d",  "stat3_lbl": "Avg. time to first page-one rankings",
        "why_h2":    "Why Law Firms Need Specialist SEO in 2026",
        "why_p1":    "Legal services is one of the most competitive search landscapes in the United States. Potential clients type 'divorce attorney near me' or 'personal injury lawyer Austin' into Google and make high-stakes decisions based on what appears on the first page. If your firm is not visible, you are invisible to the majority of the market.",
        "why_p2":    "Generic SEO agencies treat law firms like any other business. Lumo understands the compliance constraints, E-E-A-T requirements, and local search dynamics specific to legal marketing. We build authority the right way — through genuine expertise signals, local citations, and content that demonstrates real legal knowledge.",
        "why_p3":    "AI-powered search is changing legal discovery too. ChatGPT, Perplexity, and Google AI Overviews are increasingly answering legal questions — and citing specific law firms as resources. Lumo integrates GEO (Generative Engine Optimisation) into every legal SEO strategy so your firm gets cited in AI answers, not just blue-link results.",
        "services_h2": "Our SEO Services for Law Firms",
        "services": [
            ("🏛️", "Local SEO & Google Business", "Dominate the local map pack for searches like 'attorney near me' and practice-area queries in your city. Includes GBP optimisation, local citation building, and review strategy."),
            ("📝", "Legal Content Marketing", "Long-form practice area pages, FAQ content, and legal guides written to demonstrate genuine expertise and satisfy Google's E-E-A-T standards for YMYL (Your Money Your Life) content."),
            ("🔧", "Technical SEO Audit", "Site speed, mobile optimisation, structured data for attorneys (LegalService schema), crawlability, and indexation — all optimised for Google's quality signals."),
            ("🔗", "Authority Link Building", "High-quality backlinks from legal directories (Avvo, FindLaw, Martindale), bar association pages, local news, and authoritative legal publications."),
            ("🤖", "AI Search Visibility (GEO)", "Optimise your firm's content to be cited in ChatGPT, Perplexity, and Google AI Overviews when users ask legal questions in your practice areas."),
            ("📊", "Rank Tracking & Reporting", "Monthly reports on keyword rankings, organic traffic, lead volume, and call tracking — with transparent attribution from search to signed client."),
        ],
        "challenges_h2": "Legal SEO Challenges We Solve",
        "challenges": [
            ("YMYL Scrutiny", "Google applies its highest E-E-A-T standards to legal content — requiring demonstrated expertise, authoritative sources, and trustworthy credentials. Lumo structures your content to pass these quality signals."),
            ("Bar Advertising Rules", "Legal advertising is governed by state bar rules that restrict certain claims. Lumo's legal marketing team understands these constraints and writes compliant content that still converts."),
            ("Hyper-Local Competition", "Legal searches are intensely local. We build geo-targeted landing pages, practice-area pages with city modifiers, and local structured data to dominate your target markets."),
            ("Review Generation", "Google reviews are critical for legal local SEO. Lumo implements ethical review generation systems that increase your firm's review count and rating while complying with bar rules."),
        ],
        "faqs": [
            ("How long does SEO take for a law firm?", "Most law firms see meaningful ranking improvements within 60–90 days for lower-competition practice areas, and 4–6 months for highly competitive terms like 'personal injury attorney' or 'divorce lawyer.' Lumo tracks progress weekly so you always see momentum."),
            ("What practice areas does Lumo specialise in for legal SEO?", "Lumo works with personal injury, family law, criminal defence, immigration, estate planning, business law, and employment law firms. Each practice area has unique keyword landscapes and content requirements — we build strategies tailored to your specific practice mix."),
            ("How much does law firm SEO cost?", "Lumo's law firm SEO packages start at $2,000/mo for single-location practices and scale based on competition level, number of practice areas, and target geography. Most law firm clients see full ROI within 3–4 months. Book a free audit for a tailored quote."),
            ("Can SEO help my law firm compete with large legal directories like Avvo and FindLaw?", "Yes — local SEO is the most effective way to outrank aggregator directories for geo-specific searches. While Avvo may rank for 'attorneys nationwide,' you can outrank them for 'personal injury attorney in [your city]' — which is where your highest-value clients are searching."),
            ("Does Lumo handle both SEO and Google Ads for law firms?", "Yes. Lumo manages both organic SEO and Google Local Services Ads (LSAs) and Google Search Ads for law firms. We coordinate the strategies so organic and paid reinforce each other — improving Quality Scores and lowering overall cost-per-lead."),
            ("How does Lumo measure SEO success for law firms?", "Beyond rankings, Lumo tracks organic traffic, contact form submissions, phone calls (with call tracking), consultation bookings, and signed client attribution where possible. We report on metrics that connect directly to revenue — not just vanity traffic numbers."),
        ],
        "cta_h2": "Ready to Fill Your Consultation Calendar?",
        "cta_sub": "Book a free legal SEO audit — we'll analyse your current rankings, competitor gaps, and show you exactly what it takes to dominate search in your practice area.",
        "related_service": "../services/seo.html",
        "related_label":   "SEO Services",
    },
    "seo-for-dentists": {
        "label":      "Dentists & Dental Clinics",
        "slug":       "seo-for-dentists",
        "icon":       "🦷",
        "title_tag":  "SEO for Dentists & Dental Clinics | Lumo AI Agency Austin TX",
        "meta_desc":  "Specialist dental SEO that fills your appointment book — local rankings, Google Business Profile optimisation, and AI search visibility for dental practices across the US. Free audit.",
        "og_title":   "SEO for Dentists | Lumo AI Agency",
        "og_desc":    "Dental practice SEO that books more new patients — local SEO, Google Maps, and AI search for dentists. Results-focused. Free audit.",
        "h1":         "SEO for Dentists & <span class=\"hl-lime\">Dental Clinics</span>",
        "hero_badge": "Dental Industry Specialists",
        "hero_sub":   "Get found by new patients searching for a dentist near them — on Google, Maps, and AI search tools.",
        "stat1_num": "77%",  "stat1_lbl": "Of patients search online before booking a dentist",
        "stat2_num": "3.8x", "stat2_lbl": "Average new-patient ROI for dental SEO",
        "stat3_num": "60d",  "stat3_lbl": "Avg. time to top-3 Google Maps ranking",
        "why_h2":    "Why Dental Practices Need Specialist SEO",
        "why_p1":    "Over 77% of patients search online before choosing a dentist. When someone types 'dentist near me' or 'teeth whitening Austin TX,' the practices that appear in the top three Google Map Pack results capture the overwhelming majority of clicks — and new patient bookings.",
        "why_p2":    "Dental SEO requires a specific combination of local SEO, healthcare-compliant content, and technical optimisation that generic agencies rarely understand. Lumo builds dental SEO strategies that work within HIPAA-aware marketing guidelines while maximising your local search visibility.",
        "why_p3":    "Patients increasingly use AI tools to find and compare dental practices. Lumo's GEO optimisation ensures your practice is cited in AI-generated answers for queries like 'best cosmetic dentist in [city]' — capturing patients at the research stage before they even search on Google.",
        "services_h2": "Our SEO Services for Dental Practices",
        "services": [
            ("📍", "Local SEO & Map Pack", "Rank in the top 3 of Google Maps for 'dentist near me' and procedure-specific searches in your target area. Includes GBP management, local citation building, and geo-targeted landing pages."),
            ("📝", "Dental Content Strategy", "Service pages for every procedure (implants, Invisalign, cosmetic dentistry, emergency dental), FAQ content, and blog articles that attract patients at every stage of the search journey."),
            ("⭐", "Review Management", "Systematic review generation to build your star rating on Google, Healthgrades, Zocdoc, and Yelp — the platforms that drive the most new patient decisions."),
            ("🔧", "Technical SEO", "Site speed, mobile optimisation, dental schema markup (Dentist, MedicalBusiness), and structured data that enable rich results in Google Search."),
            ("🤖", "AI Search Visibility", "Appear in Google AI Overviews and ChatGPT when patients ask 'best dentist for implants' or 'affordable Invisalign near me' — capturing high-intent patients early."),
            ("📊", "New Patient Reporting", "Monthly reports tracking rankings, organic traffic, phone calls, appointment form submissions, and new patient attribution from search channels."),
        ],
        "challenges_h2": "Dental SEO Challenges We Solve",
        "challenges": [
            ("'Near Me' Competition", "Dental searches are hyper-local and intensely competitive. Lumo's local SEO strategy builds the citation authority and GBP signals needed to rank in the map pack for your highest-value procedures."),
            ("Multiple Locations", "Multi-location dental groups need separate, optimised local presences for each practice. Lumo builds individual location pages and GBP profiles that rank independently without cannibalising each other."),
            ("Negative Reviews", "A single negative review can cost a dental practice dozens of new patients. Lumo implements proactive review generation systems to build review volume and dilute isolated negative feedback."),
            ("Procedure-Specific Pages", "Patients search for specific procedures — 'dental implants near me' converts differently than 'dentist.' Lumo creates optimised landing pages for every high-value procedure you offer."),
        ],
        "faqs": [
            ("How long does SEO take for a dental practice?", "Dental practices in moderately competitive markets typically see top-3 Google Maps rankings within 60–90 days, and first-page Google Search rankings for procedure-specific terms within 3–4 months. Highly competitive markets (multiple DSOs) may take 4–6 months."),
            ("What's more important for dental SEO — Google Maps or organic search?", "Both matter, but Google Maps (the local pack) drives the most new patient calls for dental practices. Lumo optimises both channels simultaneously — most new patients click a map listing first, then visit the website before calling. Both touchpoints must be strong."),
            ("How much does dental SEO cost?", "Lumo's dental SEO packages start at $1,500/mo for single-location practices and scale up for multi-location groups. Most dental clients see positive ROI within 60–90 days as new patient bookings increase. Book a free audit for a tailored quote."),
            ("Can SEO help a new dental practice get patients quickly?", "Yes, though a new practice typically takes 3–4 months to build the authority needed for competitive rankings. Lumo accelerates this with targeted Google Business Profile optimisation, local citation building, and a content strategy that captures lower-competition long-tail searches early."),
            ("Does Lumo manage Google Ads for dental practices as well?", "Yes. Lumo manages Google Local Services Ads (LSAs) and Google Search Ads for dental practices alongside organic SEO. LSAs are particularly effective for dentists — they display above organic results and charge per lead rather than per click."),
            ("How does Lumo generate more Google reviews for my dental practice?", "Lumo implements post-appointment review request systems — automated email and SMS sequences sent shortly after visits, with a direct link to your Google review page. This ethical, compliant approach typically triples review velocity within 60 days."),
        ],
        "cta_h2": "Ready to Book More New Patients?",
        "cta_sub": "Get a free dental SEO audit — we'll show you your current map pack position, how you compare to nearby competitors, and what it takes to reach the top 3.",
        "related_service": "../services/seo.html",
        "related_label":   "SEO Services",
    },
    "digital-marketing-for-real-estate": {
        "label":      "Real Estate & Realtors",
        "slug":       "digital-marketing-for-real-estate",
        "icon":       "🏠",
        "title_tag":  "Digital Marketing for Real Estate Agents & Brokerages | Lumo AI Agency",
        "meta_desc":  "Digital marketing and SEO for real estate agents, teams, and brokerages. Lumo generates high-quality buyer and seller leads through organic search, paid ads, and AI search visibility. Free audit.",
        "og_title":   "Real Estate Digital Marketing | Lumo AI Agency",
        "og_desc":    "Real estate SEO and paid ads that generate buyer and seller leads — not just website traffic. Lumo serves agents, teams, and brokerages across the US.",
        "h1":         "Digital Marketing for <span class=\"hl-lime\">Real Estate</span> Agents & Brokerages",
        "hero_badge": "Real Estate Marketing Specialists",
        "hero_sub":   "Generate a consistent flow of buyer and seller leads through Google, paid ads, and AI search — predictably, month after month.",
        "stat1_num": "92%",  "stat1_lbl": "Of home buyers search online during their process",
        "stat2_num": "5.2x", "stat2_lbl": "Average lead ROI for real estate SEO clients",
        "stat3_num": "45d",  "stat3_lbl": "Avg. time to first qualified organic leads",
        "why_h2":    "Why Real Estate Professionals Need Specialist Digital Marketing",
        "why_p1":    "Over 92% of home buyers and sellers use the internet during their real estate journey — and most begin with a Google search. Agents and brokerages that rank on the first page for searches like 'homes for sale in Austin TX' or 'top realtor in Denver' capture leads that never need to be cold-called.",
        "why_p2":    "Real estate digital marketing requires a unique combination of hyperlocal SEO, IDX integration expertise, and an understanding of buyer and seller intent at each stage of the transaction cycle. Lumo builds strategies specifically engineered for the real estate sales cycle.",
        "why_p3":    "With AI tools increasingly answering real estate questions ('what are home prices in Austin right now?' 'best realtor in Seattle'), Lumo's GEO optimisation ensures your brand is cited as an authoritative local resource in AI-generated search results — an early-mover advantage that is still available in most markets.",
        "services_h2": "Our Digital Marketing Services for Real Estate",
        "services": [
            ("🗺️", "Hyperlocal SEO", "Rank for neighbourhood, city, and suburb-level searches: 'homes for sale in [area]', 'top realtor [city]', 'condos near [landmark]'. We build geo-targeted content and landing pages for every market you serve."),
            ("📢", "Google & Meta Ads", "High-intent Google Search campaigns for buyer and seller keywords, plus Meta Ads for listing promotion, neighbourhood guides, and brand awareness — all tracked to leads and appointments."),
            ("🏘️", "Neighbourhood Content", "Authoritative neighbourhood guides, market report pages, and local area content that rank for research-phase queries and establish your expertise in specific submarkets."),
            ("📱", "Social Media & Listings", "Property listing promotion, market update content, and community-focused posts for Instagram, Facebook, and LinkedIn — designed to build local following and generate referrals."),
            ("🤖", "AI Search Visibility", "Get cited in ChatGPT and Perplexity when buyers ask 'best neighbourhoods in [city]' or 'what is the real estate market like in [area]' — positioning your brand as the go-to local expert."),
            ("📊", "Lead Attribution Reporting", "Track every lead from first search to signed contract. Lumo connects Google Analytics, call tracking, and your CRM so you know exactly which marketing activities generate your best leads."),
        ],
        "challenges_h2": "Real Estate Marketing Challenges We Solve",
        "challenges": [
            ("Zillow / Realtor.com Competition", "Major portals dominate broad searches. Lumo focuses on hyper-local and long-tail searches where individual agents and boutique brokerages can outrank Zillow — and where buyer intent is highest."),
            ("Lead Quality vs. Quantity", "Many real estate marketing agencies chase traffic volume. Lumo focuses on qualified buyer and seller intent — building campaigns and content that attract people who are actually in the market, not just browsing."),
            ("Seasonal Market Fluctuations", "Real estate search volume varies significantly by season. Lumo builds content strategies and ad campaigns that capitalise on peak periods while maintaining lead flow year-round."),
            ("IDX Integration SEO", "IDX property search tools often create SEO problems (duplicate content, crawl issues, thin pages). Lumo audits and optimises your IDX implementation to prevent search performance issues."),
        ],
        "faqs": [
            ("What digital marketing works best for real estate agents?", "For individual agents and small teams, local SEO combined with Google Local Services Ads generates the highest-quality leads at the lowest cost. For brokerages with larger budgets, we layer in Meta Ads for listing promotion and brand building. Lumo recommends the right mix based on your budget and market."),
            ("How long does SEO take for a real estate agent or brokerage?", "Most real estate SEO campaigns show meaningful traffic and lead improvements within 60–90 days for neighbourhood-level searches, and 4–6 months for competitive city-wide terms. Lumo tracks keyword rankings, traffic, and lead quality weekly so you always see clear progress."),
            ("Can Lumo help me compete with Zillow and Realtor.com?", "You won't beat Zillow for 'homes for sale' nationally — but you absolutely can outrank them for local, specific searches like 'homes for sale in [specific neighbourhood]' or 'best real estate agent in [your city].' These hyperlocal searches convert at far higher rates than broad portal traffic."),
            ("How much does real estate digital marketing cost?", "Lumo's real estate packages start at $1,500/mo for individual agents and scale for teams and brokerages. Most clients see positive ROI within 60 days as qualified leads start flowing from organic and paid channels. Book a free audit for a tailored recommendation."),
            ("Does Lumo run Facebook and Instagram ads for real estate listings?", "Yes. Meta Ads are highly effective for real estate listing promotion, open house announcements, and building local brand awareness. Lumo manages Facebook and Instagram campaigns alongside Google Ads and SEO as part of an integrated real estate marketing strategy."),
            ("Can Lumo help with both buyer and seller lead generation?", "Yes. Buyer and seller intent requires different landing pages, content, and ad strategies. Lumo builds separate funnels for each — from 'homes for sale' and neighbourhood content for buyers, to 'how much is my home worth' and market report content for sellers."),
        ],
        "cta_h2": "Ready to Generate More Buyer & Seller Leads?",
        "cta_sub": "Book a free real estate marketing audit — we'll review your current online presence, identify your top lead generation opportunities, and show you what a winning strategy looks like for your market.",
        "related_service": "../services/seo.html",
        "related_label":   "SEO & Digital Marketing",
    },
    "restaurant-marketing": {
        "label":      "Restaurants & Food Businesses",
        "slug":       "restaurant-marketing",
        "icon":       "🍽️",
        "title_tag":  "Digital Marketing for Restaurants | Lumo AI Agency Austin TX",
        "meta_desc":  "Restaurant digital marketing that fills tables — local SEO, Google Maps, social media, and AI search visibility for restaurants, cafes, bars, and food businesses across the US. Free audit.",
        "og_title":   "Restaurant Digital Marketing | Lumo AI Agency",
        "og_desc":    "Get more diners through local SEO, Google Maps, social media, and AI search. Lumo serves restaurants, cafes, bars, and food businesses across the US.",
        "h1":         "Digital Marketing for <span class=\"hl-lime\">Restaurants</span> & Food Businesses",
        "hero_badge": "Restaurant Marketing Specialists",
        "hero_sub":   "Fill more tables, drive more orders, and build a loyal local following — with restaurant marketing built around how diners actually search and decide.",
        "stat1_num": "86%",  "stat1_lbl": "Of diners look up a restaurant online before visiting",
        "stat2_num": "3.4x", "stat2_lbl": "Average increase in reservations for SEO clients",
        "stat3_num": "30d",  "stat3_lbl": "Avg. time to improved Google Maps visibility",
        "why_h2":    "Why Restaurants Need Specialist Digital Marketing",
        "why_p1":    "86% of diners check a restaurant online before visiting — and the majority make their decision based on Google Maps, star ratings, and photos. A restaurant that does not appear in the top three map results for 'restaurants near me' or '[cuisine] in [city]' is invisible to most potential customers.",
        "why_p2":    "Restaurant marketing requires a unique blend of local SEO, reputation management, social media content, and food-photography-driven visual presence. Lumo builds restaurant marketing strategies that work across all the channels diners use — from Google to Instagram to AI search tools.",
        "why_p3":    "AI search is transforming how diners discover restaurants. When someone asks ChatGPT 'best Italian restaurant in Austin' or Google AI Overviews surfaces dining recommendations, Lumo's GEO optimisation ensures your restaurant is featured — not your competitors.",
        "services_h2": "Our Digital Marketing Services for Restaurants",
        "services": [
            ("📍", "Local SEO & Google Maps", "Rank in the top 3 for 'restaurants near me,' cuisine-specific searches, and occasion-based queries ('best date night restaurant Austin'). Includes GBP management and local citation building."),
            ("⭐", "Review Strategy & Management", "Build and maintain a 4.5+ star rating on Google, Yelp, and TripAdvisor — the platforms that drive the most diner decisions. Includes review response management and ethical review generation."),
            ("📱", "Social Media Marketing", "Scroll-stopping food photography, behind-the-scenes content, event promotion, and community engagement on Instagram and Facebook — building a loyal local following that fills tables week after week."),
            ("📢", "Google & Meta Ads", "Targeted ads for new restaurant launches, special events, seasonal promotions, and delivery campaigns — reaching diners in your area when they're deciding where to eat."),
            ("🤖", "AI Search Visibility", "Appear in AI-generated dining recommendations on ChatGPT, Perplexity, and Google AI Overviews for cuisine-type and occasion searches in your market."),
            ("📊", "Performance Reporting", "Monthly reports tracking visibility, reservation volume, phone calls, website traffic, and social engagement — giving you a clear picture of marketing ROI."),
        ],
        "challenges_h2": "Restaurant Marketing Challenges We Solve",
        "challenges": [
            ("Negative Reviews", "A 3.2-star rating can halve a restaurant's foot traffic. Lumo implements proactive review generation systems that build volume and improve average ratings, with real-time alerts for negative reviews requiring response."),
            ("Standing Out in a Crowded Market", "Every city block has multiple dining options. Lumo builds distinct brand positioning and targeted SEO content that highlights your unique offering — cuisine, atmosphere, occasion fit — to the right audience at the right time."),
            ("Online Ordering & Delivery", "Third-party delivery platforms eat into margins. Lumo builds direct-order SEO strategies that rank your own website for delivery searches, reducing dependence on Uber Eats and DoorDash commissions."),
            ("Event & Seasonal Promotion", "Holidays, private events, and seasonal menus require timely marketing. Lumo builds campaign calendars that promote your restaurant's highest-margin occasions with paid ads, email, and social media."),
        ],
        "faqs": [
            ("What's the most effective digital marketing for restaurants?", "Google Maps / local SEO is typically the highest ROI channel for restaurants — it drives the most new customer foot traffic at the lowest cost. Review management and Instagram are also critical. Lumo builds integrated strategies that optimise all three simultaneously."),
            ("How long does it take for restaurant SEO to show results?", "Restaurants in most US cities see improved Google Maps visibility within 30–60 days of Lumo's local SEO work. Organic search improvements for cuisine and occasion-specific keywords typically appear within 60–90 days."),
            ("How much does restaurant digital marketing cost?", "Lumo's restaurant marketing packages start at $1,200/mo for local SEO and review management. Full-service packages including social media and paid ads start at $2,500/mo. Book a free audit for a tailored recommendation based on your location and goals."),
            ("Can Lumo help a new restaurant build an online presence quickly?", "Yes. For new restaurant openings, Lumo prioritises rapid GBP setup and verification, local citation building, launch-focused social media content, and Google Ads to drive awareness before organic rankings build. Most new restaurant clients are generating walk-in traffic from Google within 30 days."),
            ("Does Lumo manage social media for restaurants?", "Yes. Lumo manages Instagram, Facebook, and TikTok for restaurants — from content strategy and food photography direction to posting, community management, and paid promotion. Social media is one of the highest-impact channels for restaurant brand building and event promotion."),
            ("How does Lumo handle negative Yelp and Google reviews?", "Lumo monitors reviews across all major platforms in real time and responds to negative reviews within 24 hours using brand-appropriate, professional language. Simultaneously, we implement review generation systems that build positive review volume — improving your overall rating over time."),
        ],
        "cta_h2": "Ready to Fill More Tables?",
        "cta_sub": "Book a free restaurant marketing audit — we'll analyse your Google Maps ranking, review profile, and social presence and show you the top opportunities to drive more diners.",
        "related_service": "../services/seo.html",
        "related_label":   "SEO & Local Marketing",
    },
    "healthcare-seo": {
        "label":      "Healthcare & Medical Practices",
        "slug":       "healthcare-seo",
        "icon":       "🏥",
        "title_tag":  "SEO & Digital Marketing for Healthcare & Medical Practices | Lumo AI Agency",
        "meta_desc":  "Healthcare SEO that drives patient acquisition — HIPAA-aware digital marketing for medical practices, clinics, specialists, and healthcare groups across the US. Free audit.",
        "og_title":   "Healthcare SEO | Lumo AI Agency",
        "og_desc":    "Patient acquisition SEO for doctors, specialists, clinics, and healthcare groups. HIPAA-aware digital marketing that fills your schedule. Free audit.",
        "h1":         "SEO & Digital Marketing for <span class=\"hl-lime\">Healthcare</span> Practices",
        "hero_badge": "Healthcare Marketing Specialists",
        "hero_sub":   "Attract more patients through Google, AI search, and local discovery — with marketing that respects healthcare compliance requirements.",
        "stat1_num": "80%",  "stat1_lbl": "Of patients search online before choosing a provider",
        "stat2_num": "4.3x", "stat2_lbl": "Average patient acquisition ROI for healthcare SEO",
        "stat3_num": "90d",  "stat3_lbl": "Avg. time to measurable new patient growth",
        "why_h2":    "Why Healthcare Practices Need Specialist SEO",
        "why_p1":    "Over 80% of patients search online before choosing a healthcare provider. Whether they are looking for a specialist, a primary care physician, or an urgent care clinic, the practices that appear at the top of Google — and in AI-generated health answers — capture the majority of new patient bookings.",
        "why_p2":    "Healthcare SEO is categorised as YMYL (Your Money Your Life) by Google, meaning it is subject to the strictest E-E-A-T (Experience, Expertise, Authoritativeness, Trustworthiness) requirements of any industry. Lumo builds healthcare content that meets these standards — demonstrating real medical credibility that Google rewards with rankings.",
        "why_p3":    "Patients are increasingly asking AI tools health questions and seeking provider recommendations. Lumo's GEO strategy ensures your practice is cited in AI-generated health searches — positioning your providers as trusted local experts before the patient ever visits your website.",
        "services_h2": "Our SEO Services for Healthcare Practices",
        "services": [
            ("📍", "Local SEO & Patient Acquisition", "Rank in Google Maps and organic results for 'doctor near me,' specialty-specific searches, and condition-related queries in your service area."),
            ("📝", "Medical Content Marketing", "Condition pages, treatment guides, and FAQ content written to meet Google's E-E-A-T standards for healthcare — demonstrating genuine clinical expertise without crossing into medical advice liability."),
            ("⭐", "Patient Review Strategy", "Build and maintain strong ratings on Google, Healthgrades, Zocdoc, and Vitals — the platforms that drive the most new patient decisions."),
            ("🔧", "Technical Healthcare SEO", "HIPAA-aware site architecture, medical schema markup (Physician, MedicalClinic), and technical optimisation that satisfies both Google's quality signals and compliance requirements."),
            ("🤖", "AI Health Search Visibility", "Appear in Google AI Overviews and ChatGPT health answers when patients research conditions and providers in your specialty — building brand awareness before they book."),
            ("📊", "New Patient Reporting", "Track new patient acquisition from search, phone calls, and online booking — with clear attribution connecting your marketing investment to filled appointment slots."),
        ],
        "challenges_h2": "Healthcare SEO Challenges We Solve",
        "challenges": [
            ("YMYL E-E-A-T Requirements", "Healthcare content must demonstrate genuine medical expertise, cite authoritative sources, and be reviewed by qualified providers. Lumo structures your content workflow to meet these demanding quality standards."),
            ("HIPAA Marketing Compliance", "Healthcare marketing must navigate HIPAA restrictions on patient data in advertising. Lumo implements compliant tracking, consent-based analytics, and advertising practices that protect patient privacy."),
            ("Specialist Visibility", "Specialists in competitive markets — orthopedics, dermatology, oncology — face intense search competition. Lumo builds condition-specific and procedure-specific SEO that reaches patients researching their specific diagnosis."),
            ("Provider Reputation Management", "Physician online reputation directly impacts patient choice. Lumo monitors and builds provider profiles on Healthgrades, Vitals, and Google to ensure your providers are represented accurately and positively."),
        ],
        "faqs": [
            ("How long does healthcare SEO take to generate new patients?", "Most healthcare practices see meaningful new patient growth from organic search within 90–120 days. Highly competitive specialties in major metro areas may take 4–6 months to reach top-3 rankings. Lumo tracks leads and appointments weekly so progress is always visible."),
            ("Is healthcare SEO HIPAA compliant?", "Yes. Lumo's healthcare digital marketing is built with HIPAA compliance as a core requirement — we use privacy-compliant analytics, do not retarget based on health conditions without proper consent, and advise on advertising platform policies specific to healthcare."),
            ("What types of healthcare practices does Lumo work with?", "Lumo works with primary care practices, medical specialists (orthopaedics, dermatology, cardiology, etc.), urgent care groups, dental practices, mental health providers, physical therapy clinics, and multi-location health systems. Each practice type has distinct SEO requirements that Lumo addresses specifically."),
            ("How much does healthcare SEO cost?", "Lumo's healthcare SEO packages start at $2,000/mo for single-location practices and scale for multi-location groups and health systems. Book a free audit for a tailored recommendation. Most clients see positive ROI within 60–90 days as new patient bookings increase."),
            ("Can SEO help my practice attract patients for specific conditions or procedures?", "Absolutely. Condition-specific and procedure-specific SEO is one of the most effective healthcare marketing strategies. Lumo builds dedicated landing pages for your highest-value services — 'hip replacement specialist near me,' 'Botox clinic Austin TX,' 'anxiety therapy online' — that rank for high-intent patient searches."),
            ("Does Lumo manage Google Ads for healthcare practices?", "Yes. Lumo manages Google Search Ads and Google Local Services Ads for healthcare practices, coordinated with organic SEO. Healthcare advertising has specific Google policies (no before/after images, no personal health condition targeting) that Lumo navigates expertly."),
        ],
        "cta_h2": "Ready to Attract More Patients?",
        "cta_sub": "Book a free healthcare SEO audit — we'll review your current search visibility, competitor rankings, and patient acquisition opportunities specific to your specialty and market.",
        "related_service": "../services/seo.html",
        "related_label":   "SEO Services",
    },
    "ecommerce-marketing": {
        "label":      "E-commerce & Online Retail",
        "slug":       "ecommerce-marketing",
        "icon":       "🛍️",
        "title_tag":  "E-commerce Marketing Agency | Shopify SEO & Paid Ads | Lumo AI Agency",
        "meta_desc":  "E-commerce marketing that drives organic revenue — Shopify SEO, Google Shopping, Meta Ads, and CRO for online stores. Lumo AI Agency. Average +183% organic revenue. Free audit.",
        "og_title":   "E-commerce Marketing | Lumo AI Agency",
        "og_desc":    "Shopify SEO, Google Shopping, Meta Ads, and CRO for e-commerce brands. Lumo drives +183% average organic revenue for online stores. Free audit.",
        "h1":         "E-commerce Marketing for <span class=\"hl-lime\">Online Retail</span> Brands",
        "hero_badge": "E-commerce Growth Specialists",
        "hero_sub":   "Grow your online store's organic traffic, Google Shopping presence, and conversion rate — with e-commerce marketing built for sustainable revenue growth.",
        "stat1_num": "+183%", "stat1_lbl": "Average organic revenue growth for e-com clients",
        "stat2_num": "6.8x",  "stat2_lbl": "Average ROAS on Google Shopping campaigns",
        "stat3_num": "+47%",  "stat3_lbl": "Average conversion rate improvement via CRO",
        "why_h2":    "Why E-commerce Brands Need Specialist Marketing",
        "why_p1":    "E-commerce is one of the most competitive digital landscapes online — and one of the most rewarding for brands that get their marketing right. Organic product discovery, Google Shopping visibility, and a well-optimised conversion funnel can compound revenue growth far beyond what paid ads alone can achieve.",
        "why_p2":    "E-commerce SEO is fundamentally different from service business SEO. Product schema, category page architecture, faceted navigation, crawl budget management, and product-specific keyword research all require specialist knowledge. Lumo's e-commerce team understands Shopify, WooCommerce, and BigCommerce at a platform level — not just generically.",
        "why_p3":    "AI-powered shopping discovery is growing rapidly. Products and brands are increasingly recommended in ChatGPT shopping queries and Google AI Overviews. Lumo's GEO and structured data strategy ensures your products appear in AI-driven commerce discovery — an emerging channel most e-commerce brands are not yet optimising for.",
        "services_h2": "Our Marketing Services for E-commerce Brands",
        "services": [
            ("🔍", "E-commerce SEO", "Category page optimisation, product schema, technical crawl fixes, faceted navigation, and content strategy — driving sustainable organic traffic growth that compounds month over month."),
            ("🛒", "Google Shopping & PMax", "Performance Max and Standard Shopping campaigns optimised for ROAS — with product feed management, bidding strategy, and audience signal optimisation specific to your catalogue."),
            ("📱", "Meta & TikTok Ads", "Dynamic product ads, retargeting campaigns, and prospecting on Facebook, Instagram, and TikTok — with creative testing frameworks designed for e-commerce conversion."),
            ("🧪", "Conversion Rate Optimisation", "A/B testing for product pages, PDPs, cart, and checkout — systematically fixing the friction points that cause visitors to abandon without purchasing."),
            ("✉️", "Email & SMS Marketing", "Abandoned cart sequences, post-purchase flows, win-back campaigns, and promotional calendars — automated revenue from your existing customer base."),
            ("📊", "Revenue Attribution", "Multi-touch attribution connecting your marketing channels to actual orders — so you know exactly which campaigns are driving revenue, not just traffic."),
        ],
        "challenges_h2": "E-commerce Marketing Challenges We Solve",
        "challenges": [
            ("Product Duplicate Content", "E-commerce platforms generate thousands of near-duplicate URLs from product variants, filters, and sorting. Lumo implements canonical tags, robots directives, and parameter handling to keep your SEO clean at scale."),
            ("Cart Abandonment", "The average e-commerce cart abandonment rate is 70%. Lumo combines CRO (checkout UX fixes), email/SMS automation (abandonment recovery), and retargeting ads to systematically recover lost revenue."),
            ("Amazon Competition", "Competing with Amazon on Google requires a specialist approach — targeting category, comparison, and informational searches where brand-specific stores can outrank marketplace listings."),
            ("Rising Ad Costs", "Meta and Google CPC costs increase year-over-year. Lumo reduces dependence on paid traffic by building organic SEO and email marketing channels that generate revenue without per-click costs."),
        ],
        "faqs": [
            ("What e-commerce platforms does Lumo work with?", "Lumo specialises in Shopify (including Shopify Plus), WooCommerce, and BigCommerce. We understand the SEO quirks, theme structures, and app ecosystems of each platform and build strategies that work with them rather than against them."),
            ("How long does e-commerce SEO take to show revenue impact?", "Most e-commerce clients see meaningful organic traffic growth within 3–4 months and measurable revenue impact within 4–6 months. Lumo tracks keyword rankings, organic sessions, and most importantly organic revenue weekly so ROI is always visible."),
            ("How much does e-commerce marketing cost?", "Lumo's e-commerce packages start at $2,000/mo for SEO, scaling based on catalogue size and competitive intensity. Full-service packages including paid ads and CRO start at $4,000/mo. Book a free audit for a tailored recommendation."),
            ("Can Lumo help with both Shopify SEO and Google Shopping?", "Yes — Lumo manages both as a coordinated strategy. We optimise your product schema and category pages for organic search, while building Google Shopping campaigns that target high-commercial-intent queries your organic rankings may not yet cover."),
            ("What's the biggest e-commerce SEO mistake Lumo sees?", "The most common issue is ignoring category pages. Most e-commerce brands focus SEO effort on product pages, but category pages are where the highest search volume keywords live — 'women's running shoes,' 'standing desks under $500.' Optimising category pages for both content and technical SEO typically drives the largest traffic gains."),
            ("Does Lumo offer CRO for e-commerce stores?", "Yes. Lumo's e-commerce CRO programme focuses on the highest-impact conversion points: product page layout and photography, add-to-cart friction, checkout flow, and post-purchase upsells. We run structured A/B tests using statistical significance to implement only changes that genuinely improve conversion rate."),
        ],
        "cta_h2": "Ready to Grow Your Online Store Revenue?",
        "cta_sub": "Book a free e-commerce marketing audit — we'll analyse your store's SEO health, Google Shopping setup, conversion rate, and show you the highest-impact growth opportunities.",
        "related_service": "../services/ecommerce-seo.html",
        "related_label":   "E-commerce SEO",
    },
    "saas-marketing": {
        "label":      "SaaS & Tech Startups",
        "slug":       "saas-marketing",
        "icon":       "💻",
        "title_tag":  "Digital Marketing for SaaS & Tech Startups | Lumo AI Agency Austin TX",
        "meta_desc":  "SaaS marketing agency — SEO, content, paid ads, and AI-powered growth for software companies and tech startups. Lumo drives pipeline, trials, and demo requests. Free audit.",
        "og_title":   "SaaS & Tech Startup Marketing | Lumo AI Agency",
        "og_desc":    "Pipeline-focused marketing for SaaS and tech companies — SEO, Google Ads, LinkedIn Ads, content strategy, and AI search visibility. Lumo AI Agency. Free audit.",
        "h1":         "Digital Marketing for <span class=\"hl-lime\">SaaS</span> & Tech Startups",
        "hero_badge": "SaaS Growth Specialists",
        "hero_sub":   "Drive signups, trial starts, and demo bookings with marketing built for the SaaS acquisition model — from top-of-funnel awareness to bottom-of-funnel conversion.",
        "stat1_num": "3.7x", "stat1_lbl": "Average pipeline increase for SaaS SEO clients",
        "stat2_num": "4.2x", "stat2_lbl": "Average ROI on LinkedIn Ads for B2B SaaS",
        "stat3_num": "90d",  "stat3_lbl": "Avg. time to measurable pipeline impact",
        "why_h2":    "Why SaaS Companies Need Specialist Digital Marketing",
        "why_p1":    "SaaS marketing is different from any other industry. You are selling a product that requires prospect education, a free trial or demo conversion step, and often a 30–90 day sales cycle. Generic marketing agencies optimise for leads — SaaS marketing must be optimised for pipeline quality, trial-to-paid conversion, and payback period.",
        "why_p2":    "Lumo's SaaS marketing approach is built around the unique metrics that matter to software businesses: CAC, LTV, MRR, churn, and NPS — not just traffic and form fills. We build SEO and content strategies designed around your entire acquisition funnel, from awareness to activation.",
        "why_p3":    "AI-powered software discovery is growing rapidly. Buyers ask ChatGPT 'what is the best CRM for small business?' or 'top project management tools for agencies' — and Lumo's GEO strategy ensures your product is featured in those AI-generated comparisons and recommendations.",
        "services_h2": "Our Marketing Services for SaaS Companies",
        "services": [
            ("🔍", "SaaS SEO & Content", "Problem-aware, solution-aware, and product-aware content strategy across the full funnel — from educational blog content to high-converting comparison pages and use-case landing pages."),
            ("💼", "LinkedIn Ads", "Precise B2B targeting by job title, company size, and industry — reaching the decision-makers who buy your SaaS product with Lead Gen Forms and sponsored content designed for software buyers."),
            ("📢", "Google Ads & PPC", "High-intent search campaigns targeting software-specific keywords, competitor comparison terms, and category-level searches — capturing buyers who are actively evaluating solutions."),
            ("🤖", "AI Search Visibility (GEO)", "Get your product recommended in ChatGPT, Perplexity, and Google AI Overviews when buyers ask for software recommendations in your category — an emerging channel that most SaaS companies are not yet optimising."),
            ("📝", "Comparison & Alternative Pages", "'/product-name-alternatives' and '/us-vs-competitor' pages that rank for high-intent comparison searches and capture buyers evaluating multiple tools."),
            ("📊", "Pipeline & MRR Reporting", "Marketing analytics tied directly to trial starts, demo requests, and MRR impact — connecting every channel to the metrics your investors and board actually care about."),
        ],
        "challenges_h2": "SaaS Marketing Challenges We Solve",
        "challenges": [
            ("Long Sales Cycles", "SaaS buying decisions take weeks or months. Lumo builds multi-touch nurture content, retargeting sequences, and email automation that keeps your brand top-of-mind throughout the evaluation period."),
            ("Product-Led vs. Sales-Led Growth", "PLG companies need to optimise for self-serve trial conversion; SLG companies need demo pipeline. Lumo builds marketing strategies aligned with your specific growth motion and conversion architecture."),
            ("Category Education", "New SaaS categories require educating the market before selling. Lumo builds top-of-funnel content that defines the problem your product solves and establishes your brand as the category leader."),
            ("Competitor Comparison Traffic", "Buyers actively search 'best [category] software' and '[competitor] alternatives.' Lumo builds structured comparison content that captures this high-intent traffic and converts it to trials and demos."),
        ],
        "faqs": [
            ("What SaaS marketing channels does Lumo recommend?", "The right mix depends on your ICP, deal size, and growth stage. Early-stage SaaS benefits most from SEO content and LinkedIn Ads. Mid-stage companies typically add Google Ads and retargeting. Enterprise SaaS with high deal values gets maximum ROI from LinkedIn Ads and ABM strategies. Lumo recommends the optimal channel mix in your free audit."),
            ("How long does SaaS SEO take to drive pipeline?", "SaaS SEO typically starts driving meaningful organic traffic within 60–90 days and measurable pipeline within 90–120 days. Comparison and alternative pages targeting competitor search terms often rank faster and convert at higher rates than category keywords."),
            ("Can Lumo help with both PLG and SLG SaaS models?", "Yes. Lumo builds distinct strategies for product-led growth (optimising self-serve trial conversion, onboarding content, and expansion SEO) and sales-led growth (demo pipeline, enterprise content, ABM). We've worked with SaaS companies across both models."),
            ("How much does SaaS marketing cost?", "Lumo's SaaS marketing packages start at $2,500/mo for content and SEO, scaling based on channel mix and campaign scope. Full-service packages including paid ads start at $4,500/mo. Book a free audit for a tailored recommendation."),
            ("Does Lumo create AI software recommendation content?", "Yes. GEO for SaaS is a growing speciality — we create content specifically designed to be cited in AI tool comparison queries. This includes structured product descriptions, feature comparison tables, and use-case content formatted for how AI models synthesise software recommendations."),
            ("Can Lumo help a SaaS startup with limited marketing budget?", "Yes. For early-stage SaaS with limited budget, Lumo focuses on highest-ROI activities first: SEO content targeting competitor alternatives and category keywords, LinkedIn Ads for ICP targeting, and conversion optimisation of your trial signup or demo booking flow. We build a roadmap to scale as MRR grows."),
        ],
        "cta_h2": "Ready to Accelerate Your SaaS Pipeline?",
        "cta_sub": "Book a free SaaS marketing audit — we'll analyse your current acquisition funnel, identify your top-of-funnel gaps, and show you the fastest path to predictable pipeline growth.",
        "related_service": "../services/ai-development.html",
        "related_label":   "AI Development",
    },
    "home-services-seo": {
        "label":      "Home Services Businesses",
        "slug":       "home-services-seo",
        "icon":       "🔧",
        "title_tag":  "SEO & Digital Marketing for Home Services Businesses | Lumo AI Agency",
        "meta_desc":  "Home services SEO that books more jobs — local SEO, Google Maps, and Google Local Services Ads for HVAC, plumbing, roofing, electrical, landscaping, and home service businesses. Free audit.",
        "og_title":   "Home Services SEO | Lumo AI Agency",
        "og_desc":    "Book more HVAC, plumbing, roofing, and home service jobs with local SEO and Google Local Services Ads. Lumo AI Agency. Measurable results. Free audit.",
        "h1":         "SEO for <span class=\"hl-lime\">Home Services</span> Businesses",
        "hero_badge": "Home Services Marketing Specialists",
        "hero_sub":   "Book more jobs with local SEO, Google Maps, and Google Local Services Ads — marketing built for HVAC, plumbing, roofing, electrical, and all home services.",
        "stat1_num": "97%",  "stat1_lbl": "Of service searches happen on mobile",
        "stat2_num": "4.5x", "stat2_lbl": "Average new job ROI for home services SEO",
        "stat3_num": "30d",  "stat3_lbl": "Avg. time to increased local lead volume",
        "why_h2":    "Why Home Services Companies Need Specialist Local SEO",
        "why_p1":    "When a homeowner needs HVAC repair, emergency plumbing, or a new roof, they search Google immediately — and call one of the top three results. Over 97% of home service searches happen on mobile, and the vast majority of calls go to businesses in the Google Maps Pack or Local Services Ads.",
        "why_p2":    "Home services local SEO requires a specific combination of Google Business Profile management, local citation building, service area page strategy, and review generation that is very different from e-commerce or B2B SEO. Lumo specialises in the exact signals that move home service companies up in local search.",
        "why_p3":    "AI tools are increasingly being used to find service providers. When someone asks ChatGPT 'best HVAC company in Austin' or 'who do I call for emergency plumbing near me,' Lumo's GEO strategy ensures your business is recommended — a powerful new lead source most home service companies are not yet capturing.",
        "services_h2": "Our Digital Marketing Services for Home Services",
        "services": [
            ("📍", "Local SEO & Map Pack", "Rank in the top 3 Google Maps results for your service area's highest-value searches — 'HVAC repair near me,' 'emergency plumber [city],' 'roof replacement [area].' The map pack drives the majority of home service leads."),
            ("🏆", "Google Local Services Ads", "LSAs appear above all organic results and Google Ads — and you only pay per qualified lead call. Lumo manages your LSA profile, bid strategy, and lead verification for maximum ROI."),
            ("📢", "Google Search Ads", "High-intent PPC campaigns for emergency and high-value services — reaching homeowners at the exact moment of need with ads targeting urgent service keywords."),
            ("🌐", "Service Area Page SEO", "Individual optimised landing pages for every city, town, and zip code you serve — so you rank for '[service] in [neighbourhood]' searches across your entire service territory."),
            ("⭐", "Review Generation", "Automated post-service review requests that build your Google and Yelp rating — driving more calls from the social proof signals homeowners rely on to choose a service company."),
            ("📊", "Lead Tracking & ROI Reporting", "Call tracking and lead attribution that connects every phone call to the marketing channel that drove it — so you know exactly which investments are booking jobs."),
        ],
        "challenges_h2": "Home Services Marketing Challenges We Solve",
        "challenges": [
            ("Seasonal Demand Fluctuations", "HVAC, landscaping, and roofing businesses face extreme seasonal peaks and valleys. Lumo builds marketing calendars that front-load acquisition before peak season and maintain lead flow during slower periods."),
            ("Large Service Territories", "Service area businesses covering multiple cities need individual local presence in each market. Lumo builds service area page strategies that create genuine local SEO footprint across your full territory."),
            ("Emergency vs. Planned Services", "Emergency calls (burst pipe, no AC in summer) need different marketing than planned services (annual HVAC maintenance, kitchen remodel). Lumo builds separate campaigns optimised for each intent type."),
            ("Lead Quality", "Many lead generation services deliver low-quality or shared leads. Lumo's organic SEO and LSA strategies generate exclusive, inbound leads from homeowners who found your business directly — typically higher intent and higher conversion rate."),
        ],
        "faqs": [
            ("What's the most effective marketing for home services businesses?", "Google Local Services Ads combined with local SEO (Google Maps) generate the highest ROI for most home service businesses. LSAs appear at the very top of Google for service searches and charge per qualified lead. Lumo manages both channels together for maximum visibility and lead volume."),
            ("How quickly can home services SEO generate leads?", "Google Local Services Ads can generate leads within days of approval. Local SEO improvements (GBP, citations, on-page) typically show increased lead volume within 30–60 days. Full map pack ranking improvements take 60–90 days in most markets."),
            ("How much does home services marketing cost?", "Lumo's home services packages start at $1,200/mo for local SEO and GBP management. Full-service packages including Google Ads and LSAs start at $2,500/mo plus ad spend. Book a free audit for a tailored recommendation."),
            ("Does Lumo work with franchise or multi-location home service companies?", "Yes. Lumo manages multi-location SEO and paid media for home service franchises — building individual local presences for each location without cannibalising group-level brand searches. We have experience with national franchise systems across HVAC, plumbing, cleaning, and landscaping."),
            ("How important are Google reviews for home services businesses?", "Extremely important. Google reviews are one of the top ranking factors for the local map pack, and star rating directly impacts call-through rate — a business with 4.8 stars gets significantly more calls than a 3.9-star competitor in the same position. Lumo's review generation system typically doubles review velocity within 60 days."),
            ("Can Lumo help with ServiceTitan or Jobber integration for marketing?", "Yes. Lumo integrates with field service management platforms including ServiceTitan, Jobber, and HouseCall Pro for automated post-job review requests and closed-loop lead attribution. This connects your marketing data to actual job completions for accurate ROI measurement."),
        ],
        "cta_h2": "Ready to Book More Jobs?",
        "cta_sub": "Book a free home services marketing audit — we'll check your Google Maps ranking, LSA setup, and review profile and show you the fastest path to more inbound leads.",
        "related_service": "../services/seo.html",
        "related_label":   "Local SEO",
    },
    "financial-services-marketing": {
        "label":      "Financial Services",
        "slug":       "financial-services-marketing",
        "icon":       "💰",
        "title_tag":  "Digital Marketing for Financial Services | Lumo AI Agency Austin TX",
        "meta_desc":  "Compliant digital marketing for financial advisors, wealth managers, insurance agencies, mortgage brokers, and fintech companies. SEO, paid ads, and AI search visibility. Free audit.",
        "og_title":   "Financial Services Digital Marketing | Lumo AI Agency",
        "og_desc":    "Compliance-aware SEO and digital marketing for financial advisors, fintech, insurance, and mortgage professionals. Lumo AI Agency. Free audit.",
        "h1":         "Digital Marketing for <span class=\"hl-lime\">Financial Services</span>",
        "hero_badge": "Financial Industry Marketing Specialists",
        "hero_sub":   "Grow your AUM, book more appointments, and establish digital authority — with financial marketing built to meet compliance requirements and drive qualified leads.",
        "stat1_num": "74%",  "stat1_lbl": "Of financial clients research online before engaging",
        "stat2_num": "3.9x", "stat2_lbl": "Average lead ROI for financial SEO clients",
        "stat3_num": "120d", "stat3_lbl": "Avg. time to significant organic lead growth",
        "why_h2":    "Why Financial Services Firms Need Specialist Digital Marketing",
        "why_p1":    "Over 74% of financial services clients search online before engaging an advisor, broker, or financial firm. High-net-worth individuals researching wealth management, small business owners looking for commercial insurance, and homebuyers comparing mortgage rates all begin their search on Google — and trust the firms that appear at the top.",
        "why_p2":    "Financial services marketing is tightly regulated. FINRA, SEC, FTC, and state insurance regulations govern what can be said, how performance must be disclosed, and what testimonials are permissible. Lumo's financial marketing team builds compliant content and advertising strategies that generate leads without triggering regulatory issues.",
        "why_p3":    "AI-driven finance discovery is growing rapidly — users ask ChatGPT 'best financial advisor for small business owners' or 'how do I choose a mortgage broker.' Lumo's GEO strategy positions your firm as a cited expert in AI-generated financial guidance, building brand awareness at the top of the research funnel.",
        "services_h2": "Our Marketing Services for Financial Services",
        "services": [
            ("🔍", "Financial Services SEO", "Rank for high-intent financial searches — 'financial advisor near me,' 'best mortgage broker [city],' 'small business insurance [state]' — with compliant content that meets E-E-A-T standards for YMYL financial topics."),
            ("📝", "Compliant Content Marketing", "Educational content, financial guides, and market commentary that demonstrates genuine expertise, meets regulatory disclosure requirements, and builds the trust that high-value financial clients need before engaging."),
            ("💼", "LinkedIn Ads for Financial Services", "B2B and high-net-worth targeting on LinkedIn — reaching business owners, executives, and professionals who match your ideal client profile with compliant lead generation campaigns."),
            ("📢", "Google Ads (FINRA/FTC Compliant)", "Search campaigns targeting financial service keywords, managed within advertising compliance frameworks — including proper disclaimers, performance disclosure standards, and approved messaging."),
            ("🤖", "AI Financial Search Visibility", "Appear in AI-generated financial guidance when prospects research advisors, products, or financial strategies — establishing your firm's authority before the prospect ever visits your website."),
            ("📊", "Lead Quality Reporting", "Attribution tracking connecting marketing channels to appointments booked, AUM conversations initiated, and new client acquisition — so you measure marketing ROI in the metrics that matter to your practice."),
        ],
        "challenges_h2": "Financial Marketing Challenges We Solve",
        "challenges": [
            ("Regulatory Compliance", "FINRA, SEC, insurance commissioner, and state regulations restrict financial advertising in specific ways. Lumo's financial marketing team navigates these constraints to produce compliant campaigns that still convert."),
            ("Trust & Credibility Building", "Financial relationships require significant trust. Lumo builds digital credibility through authoritative content, consistent review management, thought leadership, and E-E-A-T signals that demonstrate genuine expertise."),
            ("Long Consideration Cycles", "Financial decisions take weeks or months. Lumo builds nurture content, email sequences, and retargeting strategies that maintain engagement through the long consideration period between first search and first meeting."),
            ("Niche Audience Targeting", "Financial firms often serve specific niches — dentists, business owners, retirees. Lumo builds highly targeted paid media and SEO strategies that reach your exact ideal client profile efficiently."),
        ],
        "faqs": [
            ("What financial services does Lumo work with?", "Lumo works with independent financial advisors (RIAs and IARs), wealth management firms, insurance agencies, mortgage brokers, fintech companies, accounting firms, and credit unions. Each sector has distinct compliance requirements and search behaviour that Lumo addresses specifically."),
            ("How does Lumo ensure financial marketing compliance?", "Lumo's financial content undergoes compliance review including required disclosures, past performance disclaimers, testimonial regulations, and advertising standards specific to your registration type (SEC-registered, FINRA broker-dealer, state-licensed insurance). We work with your compliance team to ensure every asset is approved before publishing."),
            ("How long does financial services SEO take?", "Financial SEO for YMYL content requires building substantial E-E-A-T signals — typically 4–6 months to achieve strong rankings for competitive financial keywords. However, local financial advisor searches (e.g., 'fee-only advisor Austin TX') often rank within 60–90 days. Lumo tracks leads and appointments to show ROI throughout the campaign."),
            ("How much does financial services digital marketing cost?", "Lumo's financial services packages start at $2,500/mo given the compliance complexity and content quality requirements. Full-service packages including paid media start at $4,500/mo. Book a free audit for a tailored recommendation based on your AUM targets and client acquisition goals."),
            ("Can Lumo help fintech companies with marketing?", "Yes. Lumo works with fintech companies on product marketing SEO, SaaS-style acquisition content, and B2B LinkedIn campaigns targeting financial institutions. Fintech marketing combines financial services compliance knowledge with SaaS growth marketing expertise — a combination Lumo offers."),
            ("Does Lumo generate qualified leads or just website traffic?", "Lead quality is our primary focus for financial services clients. We optimise for high-intent searches, qualified audience targeting, and conversion pathways (appointment bookings, consultation requests, newsletter signups) that connect to your actual business development pipeline — not just vanity traffic."),
        ],
        "cta_h2": "Ready to Grow Your Financial Practice?",
        "cta_sub": "Book a free financial services marketing audit — we'll review your current digital presence, competitive landscape, and show you the highest-impact, compliance-safe growth opportunities.",
        "related_service": "../services/seo.html",
        "related_label":   "SEO Services",
    },
    "automotive-seo": {
        "label":      "Automotive Businesses",
        "slug":       "automotive-seo",
        "icon":       "🚗",
        "title_tag":  "SEO & Digital Marketing for Automotive Businesses | Lumo AI Agency",
        "meta_desc":  "Automotive SEO and digital marketing for car dealerships, auto repair shops, detailing businesses, and automotive service providers. Local SEO, paid ads, and AI search visibility. Free audit.",
        "og_title":   "Automotive SEO & Marketing | Lumo AI Agency",
        "og_desc":    "Drive more showroom visits, service bookings, and car sales with automotive SEO, Google Ads, and local marketing. Lumo AI Agency. Free audit.",
        "h1":         "SEO & Digital Marketing for <span class=\"hl-lime\">Automotive</span> Businesses",
        "hero_badge": "Automotive Industry Marketing Specialists",
        "hero_sub":   "Drive more showroom visits, service appointments, and vehicle sales with digital marketing built specifically for the automotive industry.",
        "stat1_num": "95%",  "stat1_lbl": "Of car buyers research online before visiting a dealer",
        "stat2_num": "4.0x", "stat2_lbl": "Average lead ROI for automotive SEO clients",
        "stat3_num": "60d",  "stat3_lbl": "Avg. time to increased organic lead volume",
        "why_h2":    "Why Automotive Businesses Need Specialist Digital Marketing",
        "why_p1":    "Over 95% of car buyers conduct online research before setting foot in a dealership — and the majority start with a Google search. Whether they are searching 'used trucks near me,' 'Toyota dealership Austin,' or 'best auto repair shop in Phoenix,' the businesses that appear at the top of those results win the walk-ins and phone calls.",
        "why_p2":    "Automotive digital marketing requires understanding search intent at different stages of the buying and service journey — from early research ('2025 Honda Accord vs Camry') to near-purchase ('Honda Accord for sale near me') to service ('oil change near me'). Each stage requires different content, landing pages, and conversion strategies.",
        "why_p3":    "AI tools are rapidly influencing automotive purchase decisions. Buyers ask ChatGPT for vehicle recommendations, compare models, and seek local dealership recommendations. Lumo's GEO strategy ensures your dealership or service business is mentioned in AI-generated automotive research — an early-mover advantage in this space.",
        "services_h2": "Our Digital Marketing Services for Automotive",
        "services": [
            ("📍", "Local SEO & Google Maps", "Rank for 'dealerships near me,' 'auto repair near me,' and make/model-specific searches in your local market. Includes GBP management, dealership schema, and local citation optimisation."),
            ("📢", "Google & Meta Ads", "Vehicle inventory ads, service special promotions, and new model launch campaigns — with audience targeting, dynamic ads, and CRM integration for automotive marketing compliance."),
            ("🌐", "Inventory & Service Page SEO", "Optimised vehicle inventory pages, make/model landing pages, and service department pages — structured for both search engines and car-buying intent."),
            ("🤖", "AI Automotive Search Visibility", "Get cited in AI-generated car buying guides and service recommendations for your make/model speciality and local market — appearing in research-stage queries before buyers visit Google."),
            ("⭐", "Dealer Review Management", "Build and maintain strong Google, DealerRater, and Cars.com ratings — the social proof signals that convert online researchers into showroom visits."),
            ("📊", "Showroom & Lead Attribution", "Track form submissions, phone calls, and chat leads back to specific marketing channels — giving you clear automotive marketing ROI beyond just website traffic."),
        ],
        "challenges_h2": "Automotive Marketing Challenges We Solve",
        "challenges": [
            ("Inventory Turnover & Dynamic Pages", "Automotive inventory changes constantly, creating SEO challenges with pages appearing and disappearing. Lumo implements strategies that build stable category and model authority regardless of specific inventory changes."),
            ("OEM Digital Advertising Restrictions", "Franchise dealerships operate under OEM co-op advertising rules that restrict campaign messaging and require specific compliance. Lumo works within OEM frameworks to maximise your visibility within approved guidelines."),
            ("Service Department SEO", "Most dealerships focus digital marketing on vehicle sales but underinvest in service department marketing. Lumo builds service-specific SEO and paid campaigns that drive high-margin, recurring service revenue."),
            ("Price Transparency Expectations", "Today's car buyer arrives at the dealership more informed than ever. Lumo builds content strategies that meet buyers where they are in their research — building trust rather than fighting information asymmetry."),
        ],
        "faqs": [
            ("What automotive businesses does Lumo work with?", "Lumo works with new and used car dealerships (franchise and independent), auto repair shops, detailing businesses, tire shops, auto parts retailers, car rental companies, and automotive service franchises. Each business type has distinct digital marketing needs that Lumo addresses with specialist strategies."),
            ("How long does automotive SEO take?", "Auto repair and service businesses typically see improved local visibility within 30–60 days. Dealership SEO for competitive make/model searches takes 3–5 months to achieve strong first-page rankings in most metro markets. Lumo tracks calls, leads, and showroom visits weekly to show continuous ROI."),
            ("How much does automotive digital marketing cost?", "Lumo's automotive packages start at $1,500/mo for local SEO and GBP management for auto repair and service businesses. Dealership full-service packages including paid media start at $3,500/mo plus ad spend. Book a free audit for a tailored recommendation."),
            ("Can Lumo manage Google Vehicle Inventory Ads for dealerships?", "Yes. Lumo manages Google Vehicle Listing Ads (VLAs) and Performance Max for automotive campaigns — connecting your DMS inventory feed to Google for dynamic vehicle advertising that showcases your current stock to in-market shoppers."),
            ("Does Lumo work with both franchise dealerships and independent dealers?", "Yes. Lumo works with both franchise dealers (navigating OEM co-op compliance and brand standards) and independent dealers (with more flexibility in messaging and campaign structure). Each client receives a strategy aligned with their specific situation."),
            ("How does Lumo measure automotive marketing ROI?", "Lumo tracks phone calls (with recording and lead classification), contact form submissions, chat leads, inventory page views, and where possible, in-store visit attribution through Google Ads. We connect this data to your CRM or DMS to show which marketing channels are actually selling cars and booking service appointments."),
        ],
        "cta_h2": "Ready to Drive More Showroom Visits & Service Bookings?",
        "cta_sub": "Book a free automotive marketing audit — we'll review your local search rankings, Google Business Profile, and competitive landscape and show you exactly where the growth opportunities are.",
        "related_service": "../services/seo.html",
        "related_label":   "SEO Services",
    },

    # ---- WAVE 2: 10 NEW VERTICALS ----

    "fitness-gym-marketing": {
        "label":      "Fitness Centers & Gyms",
        "slug":       "fitness-gym-marketing",
        "icon":       "💪",
        "title_tag":  "Digital Marketing for Fitness Centers & Gyms | Lumo AI Agency",
        "meta_desc":  "AI-powered digital marketing for gyms, fitness studios, and personal trainers across the US. Grow memberships with SEO, Google Ads, and social media. Free strategy call.",
        "og_title":   "Fitness & Gym Marketing | Lumo AI Agency",
        "og_desc":    "Grow gym memberships with targeted digital marketing — local SEO, Google Ads, Meta Ads, and AI search visibility for fitness businesses. Free audit.",
        "h1":         "Digital Marketing for <span class=\"hl-lime\">Fitness Centers & Gyms</span>",
        "hero_badge": "Fitness Industry Specialists",
        "hero_sub":   "Fill your gym floor and class schedules — with SEO, social ads, and AI search visibility built for fitness businesses.",
        "stat1_num": "3.6x", "stat1_lbl": "Average membership ROI for gym SEO clients",
        "stat2_num": "71%",  "stat2_lbl": "Of gym searches happen on mobile devices",
        "stat3_num": "45d",  "stat3_lbl": "Avg. time to first new-member attribution",
        "why_h2":    "Why Fitness Businesses Need Specialist Digital Marketing",
        "why_p1":    "The fitness industry is intensely local and seasonally competitive — January surges, summer lulls, and back-to-school spikes drive wildly different demand patterns. Gym owners who rely on walk-ins and word-of-mouth leave the majority of high-intent searchers to competitors who show up on Google.",
        "why_p2":    "Lumo builds digital marketing strategies tailored to the fitness acquisition funnel — from 'gym near me' and 'personal trainer Austin' to retargeting sequences that convert free-trial visitors into paying members. We understand the lifetime value of a gym member and build campaigns that maximise it.",
        "why_p3":    "AI search is reshaping fitness discovery too. When someone asks ChatGPT 'best CrossFit gym in Dallas' or 'affordable yoga studio near me,' the gyms cited in the answer win without a click. Lumo integrates GEO optimisation so your studio is named in AI-generated fitness recommendations.",
        "services_h2": "Our Marketing Services for Fitness Businesses",
        "services": [
            ("📍", "Local SEO & Google Maps", "Dominate 'gym near me,' 'fitness center [city],' and class-specific searches. Includes Google Business Profile optimisation, local citations, and review generation."),
            ("📱", "Social Media Ads", "Meta and TikTok ad campaigns targeting local audiences with compelling creative — free trials, class promos, and transformation stories that drive sign-ups."),
            ("🤖", "AI Search Visibility (GEO)", "Get cited in ChatGPT, Perplexity, and Google AI Overviews when users search for fitness options in your city — capturing high-intent prospects early."),
            ("📧", "Email & SMS Automation", "Automated sequences for free-trial follow-ups, membership renewals, class booking reminders, and re-engagement campaigns for churned members."),
            ("🔍", "Google Ads", "Search and Performance Max campaigns targeting gym-related intent keywords in your service area, with landing pages optimised for free-trial sign-ups."),
            ("📊", "Membership Analytics", "Track leads, free-trial conversions, membership sign-ups, and churn — with attribution data that shows which channels are actually growing your gym."),
        ],
        "challenges_h2": "Fitness Marketing Challenges We Solve",
        "challenges": [
            ("Seasonal Demand Swings", "January brings a rush; February brings churn. Lumo builds year-round content and ad strategies that smooth revenue curves and attract members who stay."),
            ("Multi-Format Complexity", "Whether you run a traditional gym, CrossFit box, yoga studio, or boutique fitness studio, Lumo tailors messaging to your specific format and target demographic."),
            ("High Member Acquisition Cost", "Generic digital ads waste budget on low-intent traffic. Lumo's hyper-local targeting and conversion-optimised landing pages drive down cost-per-member to sustainable levels."),
            ("Competing with National Chains", "Planet Fitness and Equinox have massive ad budgets. Lumo helps independent gyms win on local SEO, community storytelling, and niche positioning that chains can't replicate."),
        ],
        "faqs": [
            ("What digital marketing works best for gyms?", "Local SEO (Google Maps) and social media ads (Meta/TikTok) are the highest-ROI channels for most fitness businesses. Google Maps captures high-intent searchers actively looking for a gym; social ads build brand awareness and drive free-trial sign-ups among your target demographic. Lumo typically recommends starting with both in parallel."),
            ("How long does it take to see results from gym marketing?", "Google Maps rankings typically improve within 30–60 days. Social ad campaigns can generate free-trial leads within the first week of launch. SEO for competitive keyword terms takes 3–4 months. Lumo tracks weekly metrics so you see progress continuously."),
            ("How much does gym digital marketing cost?", "Lumo's fitness marketing packages start at $1,200/mo for local SEO and GBP management. Full-service packages including paid social and Google Ads start at $2,500/mo plus ad spend. Most fitness clients see positive ROI within 60 days."),
            ("Can Lumo help a new gym get its first 100 members?", "Yes — new gym launches are a specialty. Lumo uses a pre-launch local SEO and social media strategy, grand opening ad campaigns, and a referral-optimised landing page to build your founding member base before opening day."),
            ("Does social media marketing actually bring gym members?", "Yes, when done correctly. Transformation photos, class highlight videos, trainer profiles, and limited-time offer ads consistently drive free-trial sign-ups for fitness businesses. Lumo creates and manages this content end-to-end, including creative production briefs."),
            ("How does Lumo measure gym marketing ROI?", "Lumo tracks free-trial sign-ups, paid membership conversions, cost-per-member, and member lifetime value. We integrate with your gym management software (Mindbody, Glofox, ClubReady) where possible to connect marketing spend directly to revenue outcomes."),
        ],
        "cta_h2": "Ready to Fill Your Gym & Classes?",
        "cta_sub": "Book a free fitness marketing audit — we'll analyse your local rankings, social presence, and competitor landscape and show you the fastest path to new member growth.",
        "related_service": "../services/social-media.html",
        "related_label":   "Social Media Marketing",
    },

    "construction-marketing": {
        "label":      "Construction & Contractors",
        "slug":       "construction-marketing",
        "icon":       "🏗️",
        "title_tag":  "Digital Marketing for Construction & Contractors | Lumo AI Agency",
        "meta_desc":  "SEO, Google Ads, and lead generation for general contractors, builders, and construction companies across the US. Lumo AI Agency fills your project pipeline. Free audit.",
        "og_title":   "Construction & Contractor Marketing | Lumo AI Agency",
        "og_desc":    "Generate a steady flow of qualified construction leads with SEO, Google Local Services Ads, and AI search visibility. Results-focused. Free strategy call.",
        "h1":         "Digital Marketing for <span class=\"hl-lime\">Construction & Contractors</span>",
        "hero_badge": "Construction Industry Specialists",
        "hero_sub":   "Fill your project pipeline year-round — with local SEO, Google Ads, and AI-powered lead generation for contractors.",
        "stat1_num": "4.3x", "stat1_lbl": "Average project-lead ROI for contractor SEO",
        "stat2_num": "82%",  "stat2_lbl": "Of homeowners search online before hiring a contractor",
        "stat3_num": "60d",  "stat3_lbl": "Avg. time to first page-one local rankings",
        "why_h2":    "Why Contractors Need Specialist Digital Marketing",
        "why_p1":    "Over 82% of homeowners and commercial property owners research contractors online before making a hire. When someone searches 'general contractor near me' or 'home addition contractor Austin,' they hire from the first three results the vast majority of the time. If your business doesn't rank there, you're invisible to your hottest prospects.",
        "why_p2":    "Construction marketing has unique challenges: project cycles are long, average contract values are high, and trust signals (reviews, portfolio, licensing) drive purchase decisions more than in most industries. Lumo builds contractor marketing strategies that showcase your credentials and generate qualified project inquiries — not just website traffic.",
        "why_p3":    "AI search is increasingly influencing contractor selection. Homeowners ask ChatGPT 'best roofing contractor in Houston' or 'kitchen remodel contractor near me' before opening Google. Lumo's GEO optimisation ensures your business is cited in these AI-generated recommendations.",
        "services_h2": "Our Marketing Services for Contractors",
        "services": [
            ("📍", "Local SEO & Google Maps", "Rank in the top 3 of Google Maps for your trade and service area. Includes GBP optimisation, local citations, and portfolio content that builds trust before first contact."),
            ("⚡", "Google Local Services Ads", "LSAs display above all other search results and charge per lead — not per click. Lumo manages your LSA campaigns to maximise verified leads at the lowest cost per project inquiry."),
            ("📝", "Service & Project Pages", "Dedicated pages for each trade (kitchen remodeling, roof replacement, commercial build-out) with location modifiers, project photo galleries, and conversion-optimised layouts."),
            ("⭐", "Review Generation", "A systematic process to increase your Google, Houzz, and HomeAdvisor reviews — the trust signals that convert visitors into project leads."),
            ("🤖", "AI Search Visibility (GEO)", "Get cited in ChatGPT and Google AI Overviews when homeowners ask for contractor recommendations in your market — capturing high-intent prospects before they search."),
            ("📊", "Lead Tracking & Attribution", "Full-funnel tracking from first search to signed contract — including call recording, form submissions, and CRM integration."),
        ],
        "challenges_h2": "Contractor Marketing Challenges We Solve",
        "challenges": [
            ("Feast-or-Famine Pipeline", "Many contractors swing between overwhelmed and idle. Lumo builds a consistent inbound lead system that fills your calendar without relying on referrals or seasonal surges."),
            ("High Cost-Per-Lead", "Lead aggregators like HomeAdvisor charge high fees for shared leads. Lumo builds owned channels (SEO, LSAs) that deliver exclusive, lower-cost leads directly to you."),
            ("Trust & Credential Signals", "Construction is a high-trust purchase. Lumo builds your digital credibility with portfolio galleries, license verification schema, and review strategy that converts skeptical prospects."),
            ("Geographic Targeting", "Most contractors serve a specific radius. Lumo targets your exact service area — city and suburb by suburb — so you don't waste budget on leads outside your zone."),
        ],
        "faqs": [
            ("What's the best way to get more construction leads online?", "Google Local Services Ads (LSAs) and local SEO are the highest-ROI channels for most contractors. LSAs generate immediate leads; local SEO builds long-term organic lead flow. Lumo typically recommends running both simultaneously — LSAs for quick wins while SEO builds momentum."),
            ("How long does SEO take for a construction company?", "Contractors in moderately competitive markets typically see first-page rankings for service-area searches within 60–90 days. Highly competitive metro markets may take 4–6 months. Google Business Profile improvements (map pack rankings) often show results faster — within 30–60 days."),
            ("How much does contractor digital marketing cost?", "Lumo's contractor packages start at $1,500/mo for local SEO and GBP management. Full-service packages including Google Ads start at $2,500/mo plus ad spend. Average project value for most contractors means a single closed job covers months of marketing cost."),
            ("Should I use HomeAdvisor or build my own SEO?", "HomeAdvisor provides shared leads at high per-lead costs. Lumo's SEO and LSA strategy generates exclusive leads that cost significantly less over time and don't require competing with 4 other contractors for the same homeowner. Most clients who switch from lead aggregators see immediate cost-per-lead reduction."),
            ("How important are Google reviews for contractors?", "Critical. Reviews are the #1 trust signal homeowners use when choosing a contractor. Lumo implements a systematic review request process that typically triples your review velocity within 60 days — improving both rankings and conversion rates."),
            ("Can Lumo help with both residential and commercial construction marketing?", "Yes. Residential and commercial construction have different buyers, different search behaviors, and different content requirements. Lumo builds separate strategies and landing pages for each market segment, targeting the right keywords and decision-makers for each."),
        ],
        "cta_h2": "Ready to Fill Your Project Pipeline?",
        "cta_sub": "Book a free contractor marketing audit — we'll analyse your local rankings, competitor presence, and lead generation gaps and show you exactly what it takes to win more projects.",
        "related_service": "../services/seo.html",
        "related_label":   "SEO Services",
    },

    "education-marketing": {
        "label":      "Schools & Education Services",
        "slug":       "education-marketing",
        "icon":       "🎓",
        "title_tag":  "Digital Marketing for Schools & Education Services | Lumo AI Agency",
        "meta_desc":  "SEO and digital marketing for private schools, tutoring centers, online courses, and education companies across the US. Grow enrollment with Lumo AI Agency. Free audit.",
        "og_title":   "Education Marketing | Lumo AI Agency",
        "og_desc":    "Grow student enrollment with AI-powered digital marketing — SEO, Google Ads, and content strategy for schools and education businesses. Free strategy call.",
        "h1":         "Digital Marketing for <span class=\"hl-lime\">Schools & Education Services</span>",
        "hero_badge": "Education Industry Specialists",
        "hero_sub":   "Grow enrollment and course sign-ups with SEO, Google Ads, and AI search visibility built for education businesses.",
        "stat1_num": "3.9x", "stat1_lbl": "Average enrollment ROI for education SEO clients",
        "stat2_num": "76%",  "stat2_lbl": "Of parents research schools online before enrolling",
        "stat3_num": "90d",  "stat3_lbl": "Avg. time to measurable enrollment growth",
        "why_h2":    "Why Education Businesses Need Specialist Digital Marketing",
        "why_p1":    "The education market has fundamentally shifted online. Whether parents are searching for a private school, tutoring center, test prep service, or online course, they research extensively on Google before making enrollment decisions. Education businesses that don't appear prominently in search lose prospective students to competitors who do.",
        "why_p2":    "Education marketing requires a nuanced approach: parents and students have different search behaviors, enrollment decisions take time and involve multiple touchpoints, and trust signals (accreditation, outcomes, testimonials) are paramount. Lumo builds education marketing strategies that address each stage of the enrollment journey.",
        "why_p3":    "AI-powered search is transforming how families discover education options. When a parent asks Google's AI Overview 'best private schools in Austin' or ChatGPT 'top tutoring services near me,' the providers cited in the answer dominate. Lumo integrates GEO optimisation to ensure your institution is included in these recommendations.",
        "services_h2": "Our Marketing Services for Education Businesses",
        "services": [
            ("🔍", "Local SEO & Maps", "Rank for 'tutoring center near me,' 'private school [city],' and program-specific searches in your target area. Includes GBP management and local citation building."),
            ("📝", "Enrollment Content Strategy", "Program pages, outcome-focused case studies, faculty profiles, and FAQ content that answers the questions parents ask before enrolling — building trust before first contact."),
            ("🎯", "Google Ads for Enrollment", "Search campaigns targeting high-intent keywords in your enrollment area, with landing pages optimised for tour bookings, information requests, and application starts."),
            ("🤖", "AI Search Visibility (GEO)", "Get cited in ChatGPT, Perplexity, and Google AI Overviews when parents search for education options — capturing research-stage prospects before they visit competitor sites."),
            ("📧", "Lead Nurture Sequences", "Automated email and SMS sequences that move prospective families from inquiry to enrollment decision — with content tailored to each stage of the decision process."),
            ("📊", "Enrollment Analytics", "Track inquiry-to-enrollment conversion rates, cost-per-enrolled-student, and marketing channel attribution across all campaigns."),
        ],
        "challenges_h2": "Education Marketing Challenges We Solve",
        "challenges": [
            ("Long Decision Cycles", "Enrollment decisions take weeks or months. Lumo builds nurture sequences and remarketing campaigns that keep your institution top-of-mind throughout the research process."),
            ("Parent vs. Student Audiences", "Parents and students search differently and prioritise different factors. Lumo creates separate messaging tracks for each audience persona, ensuring relevant content reaches the right decision-maker."),
            ("Outcome Differentiation", "Every school claims great outcomes. Lumo helps you quantify and communicate your unique results with specific data points, alumni stories, and placement statistics that stand out from generic claims."),
            ("Seasonality", "Education has intense seasonal enrollment windows. Lumo builds year-round content strategies and ramps paid campaigns strategically around open enrollment and application deadlines."),
        ],
        "faqs": [
            ("What digital marketing works best for private schools?", "Local SEO combined with Google Ads and a strong content strategy is the most effective combination for private schools. Local SEO captures parents actively searching for schools; Google Ads ensures visibility during enrollment season; content marketing builds trust over the research period."),
            ("How can a tutoring center get more students online?", "Google Maps optimisation and Google Ads targeting 'tutoring near me' and subject-specific searches are the fastest path to new student inquiries for tutoring centers. Social media (especially Facebook for reaching parents) and email nurture sequences convert inquiries into enrolled students."),
            ("How much does education digital marketing cost?", "Lumo's education marketing packages start at $1,500/mo for local SEO and content strategy. Full-service packages including Google Ads start at $2,500/mo plus ad spend. Most education clients recover investment from a handful of new enrollments."),
            ("How long does it take to see enrollment growth from SEO?", "Local SEO improvements typically take 60–90 days to show meaningful ranking changes. Enrollment impact (more inquiries and tour bookings) is usually visible within 90–120 days. Google Ads can generate inquiries within the first week of launch."),
            ("Does Lumo work with online education companies?", "Yes. Lumo works with both location-based education businesses and online course creators, online tutoring platforms, and e-learning companies. Online education requires different SEO and paid acquisition strategies — national keyword targeting, content clusters, and conversion-optimised sales funnels."),
            ("How does Lumo handle COPPA compliance for education marketing?", "Lumo does not target advertising to children under 13 and follows COPPA guidelines in all campaigns for education clients. All paid campaigns are targeted at parent and adult-student audiences. We build compliant data collection forms and consent mechanisms for all education clients."),
        ],
        "cta_h2": "Ready to Grow Your Enrollment?",
        "cta_sub": "Book a free education marketing audit — we'll analyse your current search visibility, competitor presence, and enrollment funnel and identify the fastest path to new student growth.",
        "related_service": "../services/content-marketing.html",
        "related_label":   "Content Marketing",
    },

    "beauty-salon-marketing": {
        "label":      "Beauty Salons & Spas",
        "slug":       "beauty-salon-marketing",
        "icon":       "💅",
        "title_tag":  "Digital Marketing for Beauty Salons & Spas | Lumo AI Agency",
        "meta_desc":  "SEO, Google Maps, and social media marketing for hair salons, beauty spas, and esthetic clinics across the US. Fill your appointment book with Lumo AI Agency. Free audit.",
        "og_title":   "Beauty Salon & Spa Marketing | Lumo AI Agency",
        "og_desc":    "Fill your chair and treatment room with AI-powered marketing — local SEO, Instagram Ads, and Google Maps for salons and spas. Free strategy call.",
        "h1":         "Digital Marketing for <span class=\"hl-lime\">Beauty Salons & Spas</span>",
        "hero_badge": "Beauty Industry Specialists",
        "hero_sub":   "Fill your appointment book and grow your clientele — with local SEO, social ads, and AI search visibility built for salons and spas.",
        "stat1_num": "3.4x", "stat1_lbl": "Average booking ROI for salon SEO clients",
        "stat2_num": "85%",  "stat2_lbl": "Of beauty clients find new salons via Google or Instagram",
        "stat3_num": "30d",  "stat3_lbl": "Avg. time to first new-client attributions",
        "why_h2":    "Why Salons & Spas Need Specialist Digital Marketing",
        "why_p1":    "Beauty services are intensely discovery-driven — clients explore Instagram, Google Maps, and Google Search when looking for a new hairstylist, esthetician, or nail tech. The salons and spas that appear across these channels consistently win new clients while those relying solely on referrals plateau.",
        "why_p2":    "Lumo builds beauty business marketing strategies that work across the full client acquisition funnel: Google Maps for high-intent local searches, Instagram and TikTok ads for visual discovery, and automated booking integrations that turn interest into appointments. We understand that chair occupancy and repeat visit frequency are the core metrics that matter.",
        "why_p3":    "AI search is changing how clients find beauty services too. When someone asks ChatGPT 'best hair color salon in Nashville' or Google's AI Overview 'top-rated spa near me,' the businesses cited win high-value clients without a click. Lumo integrates GEO optimisation into every beauty marketing strategy.",
        "services_h2": "Our Marketing Services for Salons & Spas",
        "services": [
            ("📍", "Local SEO & Google Maps", "Rank in the top 3 of Google Maps for 'salon near me,' 'hair color specialist [city],' and service-specific searches. Includes GBP optimisation, photo strategy, and review generation."),
            ("📱", "Instagram & TikTok Ads", "Visually compelling ad campaigns showcasing your work — before/after content, stylist reels, and seasonal promotions that drive booking link clicks from your target demographic."),
            ("📅", "Online Booking Optimisation", "Landing pages and CTAs connected to your booking platform (Fresha, Vagaro, Square, Booksy) to reduce friction from search to scheduled appointment."),
            ("⭐", "Review Generation & Reputation", "Systematic review generation on Google and Yelp — building the star rating and review volume that converts first-time browsers into booked clients."),
            ("🤖", "AI Search Visibility (GEO)", "Get cited in ChatGPT and Google AI Overviews when users search for salon and spa recommendations in your city — capturing high-intent clients at the research stage."),
            ("📊", "Booking Attribution", "Track which marketing channels are driving bookings — with integration to your salon management software and month-over-month new vs. returning client reporting."),
        ],
        "challenges_h2": "Beauty Marketing Challenges We Solve",
        "challenges": [
            ("Client Churn & Retention", "The beauty industry has high client churn. Lumo builds automated retention sequences — rebooking reminders, loyalty promotions, and seasonal outreach — to increase visit frequency and lifetime value."),
            ("Stylist Attribution", "When a star stylist leaves, clients follow. Lumo builds salon-level brand equity online so client loyalty attaches to the business, not just individual team members."),
            ("Seasonal Demand Peaks", "Prom, wedding season, and holidays create demand spikes. Lumo runs targeted campaigns timed to these windows to capture seasonal demand before competitors claim it."),
            ("Standing Out on Instagram", "Every salon has an Instagram. Lumo's social strategy combines ad targeting with content coaching to build an account that actually converts followers into booked appointments."),
        ],
        "faqs": [
            ("What digital marketing works best for salons?", "Google Maps (local SEO) and Instagram/TikTok ads are the highest-impact channels for salons. Google Maps captures clients actively searching for a new salon; Instagram and TikTok drive discovery among clients who aren't searching yet but respond to beautiful visual content. Lumo builds both in parallel for maximum growth."),
            ("How do I get more Google reviews for my salon?", "Lumo implements a post-appointment review request sequence — an automated text or email sent within hours of checkout with a direct link to your Google review page. This ethical process typically triples your review velocity within 30 days."),
            ("How much does salon digital marketing cost?", "Lumo's beauty business packages start at $900/mo for Google Maps optimisation and review management. Full-service packages including paid social start at $1,800/mo plus ad spend. Most salon clients see new-client bookings from the first month."),
            ("Can Lumo help a new salon get its first clients quickly?", "Yes. Lumo launches new salons with a Google Business Profile optimisation blitz, targeted Instagram ad campaign, and a grand-opening offer that generates bookings within the first two weeks. We also set up your booking integration so discovery converts to appointments without friction."),
            ("Does social media marketing really drive salon bookings?", "Yes — when the creative is strong. Before/after transformations, stylist-personality reels, and time-limited offer ads consistently drive appointment bookings for beauty businesses. Lumo handles creative strategy and ad management end-to-end."),
            ("How does Lumo measure beauty marketing success?", "Lumo tracks new client bookings, cost-per-new-client, repeat visit rate, and average client lifetime value. We integrate with your booking platform (Vagaro, Fresha, Square, etc.) to connect marketing spend directly to booked and completed appointments."),
        ],
        "cta_h2": "Ready to Fill Your Appointment Book?",
        "cta_sub": "Book a free beauty marketing audit — we'll analyse your Google Maps ranking, social presence, and booking funnel and identify the fastest path to new client growth.",
        "related_service": "../services/social-media.html",
        "related_label":   "Social Media Marketing",
    },

    "insurance-marketing": {
        "label":      "Insurance Agencies",
        "slug":       "insurance-marketing",
        "icon":       "🛡️",
        "title_tag":  "Digital Marketing for Insurance Agencies | Lumo AI Agency",
        "meta_desc":  "SEO, Google Ads, and lead generation for insurance agents and agencies across the US. Lumo AI Agency grows your book of business with AI-powered marketing. Free audit.",
        "og_title":   "Insurance Agency Marketing | Lumo AI Agency",
        "og_desc":    "Grow your insurance book of business with SEO, Google Ads, and AI search visibility. Results-focused digital marketing for agents and agencies. Free strategy call.",
        "h1":         "Digital Marketing for <span class=\"hl-lime\">Insurance Agencies</span>",
        "hero_badge": "Insurance Industry Specialists",
        "hero_sub":   "Grow your book of business with SEO, Google Local Services Ads, and AI-powered lead generation for insurance agents.",
        "stat1_num": "4.5x", "stat1_lbl": "Average policy-lead ROI for insurance SEO",
        "stat2_num": "73%",  "stat2_lbl": "Of insurance buyers research online before purchasing",
        "stat3_num": "60d",  "stat3_lbl": "Avg. time to first incremental policy leads",
        "why_h2":    "Why Insurance Agencies Need Specialist Digital Marketing",
        "why_p1":    "Insurance is one of the most competitive pay-per-click markets in the world — dominated by comparison sites and national carriers with massive budgets. Independent agents and regional agencies who rely solely on paid ads compete against near-unlimited spending. The smarter strategy is owning organic search and local visibility.",
        "why_p2":    "Lumo builds insurance marketing strategies that compound over time: local SEO that ranks your agency for 'insurance agent near me,' content authority that positions you as the trusted expert for specific product lines, and Google Local Services Ads that generate verified leads at cost-efficient rates.",
        "why_p3":    "AI search is transforming insurance discovery. When someone asks ChatGPT 'best home insurance agent in Denver' or Perplexity 'auto insurance options for new drivers,' the agencies cited in the answer capture high-intent prospects before they ever visit a comparison site. Lumo integrates GEO optimisation into every insurance marketing strategy.",
        "services_h2": "Our Marketing Services for Insurance Agencies",
        "services": [
            ("📍", "Local SEO & Google Maps", "Rank for 'insurance agent near me,' 'homeowners insurance [city],' and product-specific searches in your market. Includes GBP management and local citation building."),
            ("⚡", "Google Local Services Ads", "LSAs for insurance display above all other search results and charge per verified lead. Lumo manages your LSA campaigns to maximise policy inquiries at the lowest cost per lead."),
            ("📝", "Insurance Content Authority", "Product-specific landing pages (home, auto, life, commercial) with clear, compliant content that answers the questions buyers ask — building trust and ranking for long-tail policy searches."),
            ("🤖", "AI Search Visibility (GEO)", "Get cited in ChatGPT and Google AI Overviews when buyers research insurance options in your coverage area — capturing high-intent leads at the earliest research stage."),
            ("📧", "Lead Nurture & CRM Integration", "Automated follow-up sequences for quote requests and inquiries — integrated with your CRM or agency management system to ensure no lead falls through the cracks."),
            ("📊", "Lead Tracking & Attribution", "Full-funnel reporting from first search to bound policy — including call recording, form submission tracking, and cost-per-bound-policy analytics."),
        ],
        "challenges_h2": "Insurance Marketing Challenges We Solve",
        "challenges": [
            ("National Carrier Competition", "Geico, State Farm, and Progressive dominate generic insurance searches. Lumo helps independent agents win on local SEO and niche product expertise that national carriers can't match."),
            ("SERP Dominated by Aggregators", "Comparison sites like PolicyGenius claim top positions for generic searches. Lumo targets longer-tail, local intent queries where independent agents can rank — and where buyers are closer to a decision."),
            ("Compliance Constraints", "Insurance marketing has strict state-specific compliance requirements. Lumo's insurance marketing team understands these constraints and creates compliant content that still drives conversions."),
            ("Long Purchase Cycles", "Insurance buyers often research for weeks. Lumo builds remarketing sequences and email nurture campaigns that stay front-of-mind throughout the decision process and convert comparison shoppers into clients."),
        ],
        "faqs": [
            ("What digital marketing works best for insurance agents?", "Google Local Services Ads and local SEO are the highest-ROI channels for independent insurance agents. LSAs generate immediate verified leads; local SEO builds sustainable organic lead flow over time. Content marketing targeting specific policy questions is also effective for establishing expertise authority."),
            ("How much does insurance digital marketing cost?", "Lumo's insurance agency packages start at $1,500/mo for local SEO and GBP management. Full-service packages including Google Ads start at $2,500/mo plus ad spend. LSA costs vary by product line and market — Lumo provides a tailored cost estimate in your free audit."),
            ("Can SEO compete with insurance comparison sites?", "For local and specific-product searches, yes. Lumo targets queries like 'independent insurance agent [city]' and '[product type] insurance [city]' where comparison aggregators don't have location-specific authority. These searches convert at higher rates because the buyer wants a local relationship, not just a price comparison."),
            ("How long does insurance SEO take to show results?", "Local SEO improvements for insurance agencies typically appear within 60–90 days. Product-specific content rankings take 3–5 months depending on competition. Google Local Services Ads can generate leads within the first week of launch."),
            ("Does Lumo work with captive agents and independent agencies?", "Yes. Lumo works with captive agents (State Farm, Allstate, Farmers) within carrier marketing guidelines and independent agencies with full flexibility. Each situation has different constraints and opportunities — we tailor strategies accordingly."),
            ("How does Lumo handle compliance in insurance marketing?", "Lumo's insurance content follows state insurance department guidelines and avoids prohibited claims (guaranteed rates, specific comparisons without disclosure, etc.). All content is reviewed for compliance before publication. We stay current with regulatory changes that affect insurance marketing."),
        ],
        "cta_h2": "Ready to Grow Your Book of Business?",
        "cta_sub": "Book a free insurance agency marketing audit — we'll analyse your local rankings, competitor presence, and lead generation gaps and show you the fastest path to new policy growth.",
        "related_service": "../services/google-ads.html",
        "related_label":   "Google Ads",
    },

    "nonprofit-marketing": {
        "label":      "Nonprofits & Charities",
        "slug":       "nonprofit-marketing",
        "icon":       "❤️",
        "title_tag":  "Digital Marketing for Nonprofits & Charities | Lumo AI Agency",
        "meta_desc":  "SEO, Google Ad Grants, and digital marketing for nonprofits and charities across the US. Lumo AI Agency grows your donor base and community reach. Free strategy call.",
        "og_title":   "Nonprofit Digital Marketing | Lumo AI Agency",
        "og_desc":    "Grow donations, volunteers, and community impact with AI-powered nonprofit marketing — Google Ad Grants, SEO, and email automation. Free strategy call.",
        "h1":         "Digital Marketing for <span class=\"hl-lime\">Nonprofits & Charities</span>",
        "hero_badge": "Nonprofit Sector Specialists",
        "hero_sub":   "Grow your donor base, volunteer pool, and community reach — with Google Ad Grants, SEO, and digital fundraising built for nonprofits.",
        "stat1_num": "$10K",  "stat1_lbl": "Free Google Ads budget available via Ad Grants",
        "stat2_num": "3.2x",  "stat2_lbl": "Average donor acquisition ROI for nonprofit SEO",
        "stat3_num": "90d",   "stat3_lbl": "Avg. time to first measurable donor growth",
        "why_h2":    "Why Nonprofits Need Specialist Digital Marketing",
        "why_p1":    "Nonprofits face a unique challenge: connecting with donors, volunteers, and beneficiaries without the marketing budgets of commercial businesses. Google's Ad Grants program offers up to $10,000/month in free search advertising to eligible nonprofits — but most organisations fail to fully utilise this benefit due to campaign complexity.",
        "why_p2":    "Lumo builds nonprofit digital marketing strategies that maximise every dollar of budget, including full Google Ad Grants management, SEO that attracts mission-aligned donors, and email automation that converts one-time donors into recurring supporters. We understand the unique messaging requirements of mission-driven organisations.",
        "why_p3":    "AI search is changing how donors discover causes. When someone asks ChatGPT 'best food bank in Chicago to donate to' or 'animal rescue volunteer opportunities near me,' the organisations cited in the answer win high-intent supporters. Lumo integrates GEO optimisation to ensure your nonprofit is included in these recommendations.",
        "services_h2": "Our Marketing Services for Nonprofits",
        "services": [
            ("💰", "Google Ad Grants Management", "Full management of your nonprofit's $10,000/month Google Ad Grants account — keyword strategy, ad creation, conversion tracking, and compliance with Google's grant requirements."),
            ("🔍", "SEO for Cause Discovery", "Rank for mission-specific searches ('food bank near me,' '[cause] nonprofit [city]') and donor-intent queries ('where to donate [cause] in [city]') — connecting you with people actively looking to support your cause."),
            ("📧", "Donor Email Automation", "Welcome sequences, recurring gift upgrade campaigns, impact reporting emails, and year-end fundraising sequences that maximise donor lifetime value and retention."),
            ("📱", "Social Media & Campaign Content", "Mission storytelling, impact photography direction, campaign content, and Meta ad campaigns for fundraising events and seasonal giving campaigns."),
            ("🤖", "AI Search Visibility (GEO)", "Get cited in ChatGPT and Perplexity when people search for giving opportunities or volunteer programs in your cause area — capturing mission-aligned supporters at the moment of intent."),
            ("📊", "Fundraising Analytics", "Track donor acquisition cost, average gift size, donor retention rate, and total fundraising revenue attributed to digital channels — with reporting tied to your fundraising platform."),
        ],
        "challenges_h2": "Nonprofit Marketing Challenges We Solve",
        "challenges": [
            ("Budget Constraints", "Nonprofits can't outspend commercial competitors for keywords. Lumo maximises the Google Ad Grants program and focuses SEO strategy on mission-specific queries where nonprofits can win organically."),
            ("Donor Retention", "One-time donors rarely become recurring supporters without follow-up. Lumo builds automated nurture sequences that educate new donors on impact and consistently upgrade one-time gifts to monthly commitments."),
            ("Volunteer Recruitment", "Finding dedicated volunteers requires targeted outreach beyond your current network. Lumo builds content and social campaigns that attract mission-aligned volunteers searching for opportunities online."),
            ("Trust & Transparency", "Donors want to know their money creates impact. Lumo builds trust through impact storytelling, transparent reporting content, and credibility signals that convert skeptical first-time visitors into donors."),
        ],
        "faqs": [
            ("How can a nonprofit use Google Ad Grants?", "Google Ad Grants provides up to $10,000/month in free Google Search advertising to eligible 501(c)(3) nonprofits. Lumo manages your Ad Grants account end-to-end — from initial application support to ongoing campaign management — ensuring you utilise the full grant while complying with Google's requirements."),
            ("What digital marketing works best for nonprofits?", "Google Ad Grants and SEO are the highest-ROI digital channels for most nonprofits. Ad Grants deliver immediate search visibility at no cost; SEO builds long-term organic reach. Email marketing is the highest-ROI channel for donor retention and upgrade campaigns."),
            ("How much does nonprofit digital marketing cost?", "Lumo's nonprofit packages start at $800/mo for Google Ad Grants management and basic SEO — recognising the budget constraints of the sector. Full-service fundraising marketing packages start at $1,800/mo. Many nonprofits see immediate net-positive ROI from Ad Grants alone."),
            ("Can digital marketing increase recurring donors?", "Yes. Lumo's donor lifecycle email sequences consistently increase recurring gift rates by 30–60% within 90 days. We build upgrade journeys that move one-time donors to monthly commitments using impact storytelling and clear ask strategies."),
            ("Does Lumo work with small nonprofits?", "Yes. Lumo works with nonprofits of all sizes — from community foundations with small budgets to national charities. We tailor scope and investment to what makes sense for your organisation's size and growth stage."),
            ("How does Lumo measure nonprofit marketing success?", "Lumo tracks donor acquisition (new donors from digital channels), average gift size, recurring gift conversion rate, cost-per-new-donor, and total digital fundraising revenue. We integrate with your fundraising platform (Bloomerang, DonorPerfect, Salesforce NPSP) to connect marketing spend to fundraising outcomes."),
        ],
        "cta_h2": "Ready to Grow Your Mission's Reach?",
        "cta_sub": "Book a free nonprofit marketing strategy call — we'll review your Google Ad Grants eligibility, current digital presence, and show you how to maximise your mission's online impact.",
        "related_service": "../services/google-ads.html",
        "related_label":   "Google Ads",
    },

    "senior-care-marketing": {
        "label":      "Senior Care & Assisted Living",
        "slug":       "senior-care-marketing",
        "icon":       "🏠",
        "title_tag":  "Digital Marketing for Senior Care & Assisted Living | Lumo AI Agency",
        "meta_desc":  "SEO, Google Ads, and lead generation for senior care, assisted living, and home health agencies across the US. Fill your facility census with Lumo AI Agency. Free audit.",
        "og_title":   "Senior Care & Assisted Living Marketing | Lumo AI Agency",
        "og_desc":    "Fill your senior care facility census with AI-powered marketing — local SEO, Google Ads, and content strategy for assisted living and home health. Free strategy call.",
        "h1":         "Digital Marketing for <span class=\"hl-lime\">Senior Care & Assisted Living</span>",
        "hero_badge": "Senior Care Industry Specialists",
        "hero_sub":   "Fill your census and grow your referral pipeline — with SEO, Google Ads, and AI search visibility built for senior care providers.",
        "stat1_num": "4.1x", "stat1_lbl": "Average resident-lead ROI for senior care SEO",
        "stat2_num": "79%",  "stat2_lbl": "Of senior care decisions start with online research",
        "stat3_num": "60d",  "stat3_lbl": "Avg. time to census-impacting lead increase",
        "why_h2":    "Why Senior Care Providers Need Specialist Digital Marketing",
        "why_p1":    "Adult children searching for senior care options for a parent conduct extensive online research before making placement decisions. When they search 'assisted living near me' or 'memory care facilities in Austin,' the communities that appear at the top of Google — with strong reviews and informative websites — win the inquiry and ultimately the resident.",
        "why_p2":    "Senior care marketing requires sensitivity, deep empathy in messaging, and compliance with healthcare marketing guidelines. Lumo builds senior care digital strategies that speak to the emotional complexity of placement decisions while driving the lead volume your community needs to maintain census.",
        "why_p3":    "AI search is transforming how families research senior care. When an adult child asks ChatGPT 'best assisted living in Phoenix for someone with dementia' or Perplexity 'home health care agencies near me,' the providers cited in the answer receive high-intent inquiries. Lumo integrates GEO optimisation into every senior care marketing strategy.",
        "services_h2": "Our Marketing Services for Senior Care Providers",
        "services": [
            ("📍", "Local SEO & Google Maps", "Rank for 'assisted living near me,' 'memory care [city],' and home health searches in your service area. Includes GBP management, local citations, and review generation."),
            ("📝", "Empathetic Content Strategy", "Community pages, care level guides, family resources, and FAQ content that addresses the questions families ask during the placement research process — building trust at every stage."),
            ("🎯", "Google Ads Lead Generation", "Search and display campaigns targeting high-intent senior care keywords, with landing pages optimised for tour requests and information inquiries from adult children."),
            ("🤖", "AI Search Visibility (GEO)", "Get cited in ChatGPT and Google AI Overviews when families research senior care options in your market — capturing high-intent inquiries before families visit competitor sites."),
            ("📧", "Lead Nurture Automation", "Multi-touch email and SMS sequences that follow up with tour inquiries, nurture families through the 60–120 day decision cycle, and facilitate waitlist management."),
            ("📊", "Census Analytics", "Track tour bookings, move-in conversions, cost-per-resident, and digital channel attribution — connecting marketing spend to census outcomes.",),
        ],
        "challenges_h2": "Senior Care Marketing Challenges We Solve",
        "challenges": [
            ("Long Decision Cycles", "Senior placement decisions take 60–120 days on average. Lumo builds nurture sequences that stay front-of-mind throughout the process and convert researching families into tour bookings."),
            ("Referral Source Diversification", "Over-reliance on hospital and physician referrals creates census vulnerability. Lumo builds direct-to-family digital channels that generate inquiries independent of referral relationships."),
            ("Emotional Sensitivity in Messaging", "Senior care content must balance empathy with information. Lumo's content team understands the emotional weight of placement decisions and writes copy that families respond to positively."),
            ("Multi-Care-Level Marketing", "Communities offering independent living, assisted living, and memory care need separate marketing strategies for each care level. Lumo creates distinct content tracks and landing pages for each."),
        ],
        "faqs": [
            ("What digital marketing works best for assisted living communities?", "Local SEO and Google Ads targeting adult children (primary decision-makers) are the most effective channels for assisted living. SEO builds sustainable organic inquiry flow; Google Ads fills inquiry gaps immediately. Review management is also critical — families heavily weight Google and A Place for Mom reviews."),
            ("How long does senior care SEO take to show results?", "Local SEO improvements for senior care providers typically appear within 60–90 days. Inquiry impact (more tour bookings) usually follows within 90–120 days. Google Ads can generate tour inquiries within the first week of launch."),
            ("How much does senior care digital marketing cost?", "Lumo's senior care packages start at $1,800/mo for local SEO, content strategy, and GBP management. Full-service packages including Google Ads start at $3,000/mo plus ad spend. A single additional resident placement typically pays back months of marketing investment."),
            ("Can digital marketing replace senior care referral sources?", "Digital marketing should complement referral sources, not replace them. Lumo builds direct-to-family digital channels that diversify your inquiry pipeline and reduce dependence on any single referral source — creating census resilience."),
            ("How does Lumo handle HIPAA compliance in senior care marketing?", "Lumo does not collect or process Protected Health Information (PHI) in marketing campaigns. All contact forms collect general inquiry information only. We use HIPAA-compliant email platforms for lead nurture and avoid retargeting pixels on care-record-adjacent pages."),
            ("Does Lumo work with home health agencies as well as facilities?", "Yes. Lumo works with in-home care agencies, adult day programs, skilled nursing facilities, independent living communities, assisted living, and memory care communities. Each care type has different search intent and buyer journeys — we build strategies tailored to your specific care model."),
        ],
        "cta_h2": "Ready to Fill Your Community Census?",
        "cta_sub": "Book a free senior care marketing audit — we'll analyse your local rankings, review profile, and competitor presence and identify the fastest path to more family inquiries and tour bookings.",
        "related_service": "../services/seo.html",
        "related_label":   "SEO Services",
    },

    "pet-services-marketing": {
        "label":      "Veterinarians & Pet Services",
        "slug":       "pet-services-marketing",
        "icon":       "🐾",
        "title_tag":  "Digital Marketing for Veterinarians & Pet Services | Lumo AI Agency",
        "meta_desc":  "SEO, Google Maps, and digital marketing for veterinary clinics, pet groomers, boarding facilities, and pet stores across the US. Grow your client base with Lumo AI Agency. Free audit.",
        "og_title":   "Veterinarian & Pet Services Marketing | Lumo AI Agency",
        "og_desc":    "Grow your veterinary practice or pet business with local SEO, Google Ads, and social media marketing. Results-focused. Free strategy call.",
        "h1":         "Digital Marketing for <span class=\"hl-lime\">Veterinarians & Pet Services</span>",
        "hero_badge": "Pet Industry Specialists",
        "hero_sub":   "Attract more pet owners to your vet practice, grooming salon, or boarding facility — with local SEO and digital marketing built for pet businesses.",
        "stat1_num": "3.5x", "stat1_lbl": "Average client-acquisition ROI for vet SEO",
        "stat2_num": "72%",  "stat2_lbl": "Of pet owners search online when finding a new vet",
        "stat3_num": "45d",  "stat3_lbl": "Avg. time to first new-client increase",
        "why_h2":    "Why Pet Businesses Need Specialist Digital Marketing",
        "why_p1":    "Pet ownership is at an all-time high in the US — over 66% of households own a pet, and pet owners spend more on veterinary and grooming services than ever before. When a new pet owner moves to the area or a current pet owner looks for a specialist, the first step is almost always Google. The practices and businesses that appear prominently in local search win those clients.",
        "why_p2":    "Veterinary and pet service marketing has unique considerations: healthcare compliance for vet practices, the emotional attachment of pet owners to their animals, and intensely local search intent for grooming, boarding, and daycare services. Lumo builds marketing strategies calibrated to the specific business model and client psychology of each pet industry segment.",
        "why_p3":    "AI-powered search is also changing pet service discovery. When someone asks ChatGPT 'best vet near me for large dogs' or 'dog boarding with webcams in Seattle,' the businesses cited win high-value clients. Lumo integrates GEO optimisation to ensure your pet business is included in AI-generated recommendations.",
        "services_h2": "Our Marketing Services for Pet Businesses",
        "services": [
            ("📍", "Local SEO & Google Maps", "Rank for 'vet near me,' 'dog groomer [city],' 'pet boarding [city],' and specialty searches in your service area. Includes GBP management, photo strategy, and review generation."),
            ("📝", "Service & Specialty Pages", "Individual pages for each service (wellness exams, dental cleanings, grooming packages, boarding, daycare) with conversion-optimised layouts and clear calls-to-action."),
            ("⭐", "Review Generation", "Systematic review generation on Google, Yelp, and veterinarian-specific platforms — the trust signals that convert browsing pet owners into booked appointments."),
            ("📱", "Social Media Marketing", "Pet-friendly social content — patient spotlights (with owner permission), team introductions, care tips, and seasonal promotions that build community and drive referrals."),
            ("🤖", "AI Search Visibility (GEO)", "Get cited in ChatGPT and Google AI Overviews when pet owners search for veterinary and pet care recommendations — capturing high-intent clients early."),
            ("📊", "Client Attribution Reporting", "Track new client acquisition by channel, appointment type conversion rates, and client lifetime value — with integration to your practice management software."),
        ],
        "challenges_h2": "Pet Business Marketing Challenges We Solve",
        "challenges": [
            ("High Client Lifetime Value", "A loyal pet client is worth thousands over their pet's lifetime. Lumo builds acquisition strategies that target the highest-LTV client segments — multi-pet households, young families with new pets."),
            ("'Near Me' Competition", "Pet searches are hyper-local. Lumo's local SEO strategy builds the citation authority and GBP signals needed to rank in the map pack for your highest-value services."),
            ("Specialty Differentiation", "Exotic animal care, feline-only practices, or fear-free certified clinics have valuable differentiation that generic marketing misses. Lumo builds specialty-specific content that attracts clients specifically seeking your expertise."),
            ("Emergency & After-Hours Capture", "Pet emergencies drive high-urgency searches. Lumo ensures you rank for emergency and after-hours queries in your area and that your GBP hours and emergency protocols are clearly communicated."),
        ],
        "faqs": [
            ("What digital marketing works best for veterinary practices?", "Local SEO (Google Maps) and Google Ads are the highest-ROI channels for veterinary practices. Maps captures pet owners searching for a new vet; Google Ads ensures visibility for new-patient acquisition campaigns. Review management is equally important — star rating is a primary selection factor."),
            ("How long does vet SEO take to show results?", "Local SEO improvements for veterinary practices typically appear within 45–60 days. New client attribution (more appointment bookings from organic) usually shows within 60–90 days. Google Ads can generate new client appointments within the first week of launch."),
            ("How much does pet business digital marketing cost?", "Lumo's pet business packages start at $1,200/mo for local SEO and GBP management. Full-service packages including Google Ads start at $2,200/mo plus ad spend. Most vet practices recover investment from 3–5 new regular clients."),
            ("Can digital marketing help a grooming or boarding business?", "Yes. Grooming and boarding are even more locally-driven than veterinary care — most searches are highly local intent. Google Maps ranking, positive reviews, and targeted social media ads (particularly Instagram and Facebook for reaching local dog owners) are highly effective for these businesses."),
            ("Does Lumo work with specialty veterinary practices?", "Yes. Lumo works with general practice, emergency veterinary hospitals, feline specialty practices, exotic animal clinics, veterinary dermatology, oncology, and internal medicine specialists. Each specialty has distinct search intent and client acquisition strategies — we tailor accordingly."),
            ("How does Lumo handle VCPR and veterinary marketing compliance?", "Lumo's veterinary content follows AVMA and state veterinary board guidelines — avoiding specific diagnostic claims, prohibited treatment guarantees, and other marketing restrictions. All content is reviewed for compliance before publication."),
        ],
        "cta_h2": "Ready to Grow Your Pet Client Base?",
        "cta_sub": "Book a free pet business marketing audit — we'll analyse your local search rankings, Google Maps presence, and competitor landscape and identify the fastest path to new client growth.",
        "related_service": "../services/seo.html",
        "related_label":   "SEO Services",
    },

    "retail-seo": {
        "label":      "Retail & Brick-and-Mortar Stores",
        "slug":       "retail-seo",
        "icon":       "🛍️",
        "title_tag":  "SEO & Digital Marketing for Retail Stores | Lumo AI Agency",
        "meta_desc":  "Local SEO, Google Shopping, and digital marketing for retail stores and boutiques across the US. Drive foot traffic and online sales with Lumo AI Agency. Free audit.",
        "og_title":   "Retail Store SEO & Marketing | Lumo AI Agency",
        "og_desc":    "Drive foot traffic and online sales with local SEO, Google Shopping Ads, and AI search visibility for retail businesses. Free strategy call.",
        "h1":         "SEO & Digital Marketing for <span class=\"hl-lime\">Retail Stores</span>",
        "hero_badge": "Retail Industry Specialists",
        "hero_sub":   "Drive more foot traffic and online sales with local SEO, Google Shopping, and AI search visibility built for retail businesses.",
        "stat1_num": "3.8x", "stat1_lbl": "Average foot-traffic ROI for retail SEO clients",
        "stat2_num": "88%",  "stat2_lbl": "Of shoppers research locally online before visiting a store",
        "stat3_num": "45d",  "stat3_lbl": "Avg. time to first foot-traffic increase",
        "why_h2":    "Why Retail Stores Need Specialist Digital Marketing",
        "why_p1":    "Over 88% of shoppers research locally online before visiting a brick-and-mortar store. When someone searches 'running shoe store near me' or 'vintage furniture shop Austin,' the stores that appear in Google Maps and the top of search results drive the foot traffic. Retailers that aren't visible in local search are missing the majority of available customer intent.",
        "why_p2":    "Retail digital marketing requires a unique combination of local SEO, Google Business Profile management, Google Shopping Ads, and inventory-connected digital advertising. Lumo builds retail marketing strategies that capture in-store intent, drive foot traffic, and — where applicable — grow your online sales channel simultaneously.",
        "why_p3":    "AI search is reshaping retail discovery. When a shopper asks ChatGPT 'best independent bookstore in Portland' or Google's AI Overview 'where to buy [product] near me,' the stores cited in the answer win walk-in customers. Lumo integrates GEO optimisation into every retail marketing strategy.",
        "services_h2": "Our Marketing Services for Retail Businesses",
        "services": [
            ("📍", "Local SEO & Google Maps", "Rank for '[product category] store near me' and product-specific searches in your area. Includes GBP management, local citation building, store hours optimisation, and product keyword targeting."),
            ("🛒", "Google Shopping & Product Ads", "Performance Max and Shopping campaigns that connect your product inventory to Google Search — showing your products to in-market shoppers before they visit a competitor."),
            ("📝", "Product & Category Content", "SEO-optimised product pages, category descriptions, and buying guides that rank for product research queries and convert search traffic into in-store visits or online orders."),
            ("📱", "Social Media & Visual Commerce", "Instagram Shopping, Facebook catalog ads, and TikTok product content that drives discovery among local shoppers — with direct links to purchase or store visit."),
            ("🤖", "AI Search Visibility (GEO)", "Get cited in ChatGPT and Google AI Overviews when shoppers search for products or stores in your category — capturing high-intent customers before they choose a destination."),
            ("📊", "Foot Traffic & Sales Attribution", "Track online-to-offline conversion — Google store visit conversions, GBP direction requests, call tracking, and online order attribution — connecting digital spend to real sales."),
        ],
        "challenges_h2": "Retail Marketing Challenges We Solve",
        "challenges": [
            ("Competing with Amazon & Big Box", "Independents can't out-spend national chains on generic searches. Lumo focuses on local intent, product specificity, and community brand storytelling where independent retailers have genuine competitive advantages."),
            ("Online-to-Offline Attribution", "Measuring which digital spend drives foot traffic is notoriously hard. Lumo uses Google store visit conversions, direction request tracking, and call attribution to connect your digital investment to in-store revenue."),
            ("Seasonal Inventory Fluctuations", "Retail demand swings with seasons and trends. Lumo builds dynamic ad strategies that align with your inventory levels and seasonal demand patterns — scaling up before peak periods."),
            ("Multi-Channel Complexity", "Managing a physical store plus an e-commerce site plus social commerce is complex. Lumo builds integrated marketing strategies that present consistent messaging and inventory across all channels."),
        ],
        "faqs": [
            ("What digital marketing works best for retail stores?", "Google Business Profile (Maps) optimisation is the single highest-impact channel for brick-and-mortar retail — it captures shoppers with immediate intent. Google Shopping Ads are next for product-focused retailers. Social media (Instagram, TikTok) drives discovery for fashion, home goods, and lifestyle retail."),
            ("How does local SEO drive foot traffic to retail stores?", "Local SEO ensures your store appears in the top 3 Google Maps results when nearby shoppers search for your product category. Lumo optimises your GBP with accurate hours, product photos, Q&A, and consistent local citations — the signals that determine map pack ranking and shopper selection."),
            ("How much does retail digital marketing cost?", "Lumo's retail packages start at $1,200/mo for local SEO and GBP management. Full-service packages including Google Shopping and social ads start at $2,500/mo plus ad spend. Most retail clients see positive ROI within 45–60 days."),
            ("Can Lumo help a new retail store get customers quickly?", "Yes. Lumo launches new retail businesses with a Google Business Profile optimisation blitz (same-day), Google Ads campaign targeting local shoppers, and a social launch campaign — generating store visitors within the first weeks of opening."),
            ("Does Lumo manage Google Shopping Ads for retail?", "Yes. Lumo manages Google Shopping, Performance Max, and standard search campaigns for retail clients — including product feed management, bidding strategy, and landing page optimisation to maximise return on ad spend."),
            ("How does Lumo handle multi-location retail marketing?", "Multi-location retailers need individual local presences for each location alongside consistent brand messaging. Lumo manages separate GBP profiles, local SEO strategies, and geo-targeted ad campaigns for each location — while maintaining brand coherence across all markets."),
        ],
        "cta_h2": "Ready to Drive More Foot Traffic & Sales?",
        "cta_sub": "Book a free retail marketing audit — we'll analyse your local search rankings, Google Shopping presence, and competitor visibility and identify the fastest path to more customers and sales.",
        "related_service": "../services/google-ads.html",
        "related_label":   "Google Ads",
    },

    "hospitality-marketing": {
        "label":      "Hotels & Hospitality",
        "slug":       "hospitality-marketing",
        "icon":       "🏨",
        "title_tag":  "Digital Marketing for Hotels & Hospitality | Lumo AI Agency",
        "meta_desc":  "SEO, Google Hotel Ads, and digital marketing for hotels, vacation rentals, and hospitality businesses across the US. Grow direct bookings with Lumo AI Agency. Free audit.",
        "og_title":   "Hotel & Hospitality Marketing | Lumo AI Agency",
        "og_desc":    "Grow direct bookings and reduce OTA dependency with SEO, Google Hotel Ads, and AI search visibility for hotels and hospitality businesses. Free strategy call.",
        "h1":         "Digital Marketing for <span class=\"hl-lime\">Hotels & Hospitality</span>",
        "hero_badge": "Hospitality Industry Specialists",
        "hero_sub":   "Grow direct bookings and reduce OTA commission costs with SEO, Google Hotel Ads, and AI search visibility built for hospitality businesses.",
        "stat1_num": "4.2x", "stat1_lbl": "Average direct-booking ROI for hotel SEO",
        "stat2_num": "65%",  "stat2_lbl": "Of hotel searches begin on Google",
        "stat3_num": "30d",  "stat3_lbl": "Avg. time to first direct booking increase",
        "why_h2":    "Why Hospitality Businesses Need Specialist Digital Marketing",
        "why_p1":    "Over 65% of hotel searches begin on Google — but most of those searchers end up booking through Expedia, Booking.com, or Hotels.com, costing properties 15–25% in OTA commission on every booking. The hospitality businesses that invest in direct booking strategies through SEO and Google Hotel Ads recapture that margin and build direct guest relationships.",
        "why_p2":    "Hospitality marketing has unique complexity: rate parity issues, OTA competitive dynamics, seasonal demand management, and the critical role of review platforms (TripAdvisor, Google) in booking decisions. Lumo builds hotel marketing strategies that drive direct bookings, manage online reputation, and maximise revenue per available room (RevPAR).",
        "why_p3":    "AI travel assistants are transforming hospitality discovery. When a traveler asks ChatGPT 'best boutique hotel in Austin for a weekend trip' or Perplexity 'hotels near [attraction],' the properties cited win high-value direct bookings. Lumo integrates GEO optimisation to ensure your property is included in AI-generated travel recommendations.",
        "services_h2": "Our Marketing Services for Hospitality Businesses",
        "services": [
            ("🔍", "Hotel SEO & Local Visibility", "Rank for 'hotels in [city],' '[neighborhood] hotel,' and experience-specific searches. Includes GBP management, travel schema markup, and content strategy that captures travelers at the research stage."),
            ("🏨", "Google Hotel Ads", "Direct booking campaigns through Google Hotel Ads — displaying your rates alongside OTA competitors and driving commission-free reservations through your direct booking engine."),
            ("⭐", "Review Management & TripAdvisor", "Systematic review generation on Google, TripAdvisor, and Booking.com — and professional response management that demonstrates exceptional guest service to prospective visitors."),
            ("📝", "Experience & Destination Content", "Local experience guides, seasonal content, and event-driven articles that attract travelers researching destinations — building authority and organic traffic from non-branded queries."),
            ("🤖", "AI Travel Search Visibility (GEO)", "Get cited in ChatGPT, Perplexity, and Google AI Overviews when travelers research your destination — capturing high-intent guests before they reach OTA booking pages."),
            ("📊", "Direct Booking Analytics", "Track direct vs. OTA booking ratio, cost-per-direct-booking, RevPAR impact, and channel attribution — connecting marketing investment to revenue outcomes.",),
        ],
        "challenges_h2": "Hospitality Marketing Challenges We Solve",
        "challenges": [
            ("OTA Commission Dependency", "Expedia and Booking.com charge 15–25% per booking. Lumo's direct booking strategy — SEO, Google Hotel Ads, email loyalty — reduces OTA dependency and recaptures margin on every booking."),
            ("Seasonal Demand Management", "Hospitality has extreme seasonal variance. Lumo builds dynamic content and campaign strategies that maximise RevPAR in peak periods and drive occupancy in shoulder seasons."),
            ("Review Platform Dominance", "TripAdvisor and Google reviews drive an outsized share of booking decisions. Lumo builds systematic review generation and response processes that improve your rating and convert more browsers to bookers."),
            ("Competing with Brand Hotels", "Independent and boutique properties can't out-advertise Marriott or Hilton. Lumo focuses on the differentiation, local experience content, and niche audience targeting where independent properties win."),
        ],
        "faqs": [
            ("How can hotels reduce OTA dependence?", "The most effective strategy is a combination of Google Hotel Ads (which drive direct bookings at lower commission than OTAs), SEO that captures destination-intent searches, and a loyalty email program that converts first-time OTA guests into direct repeat bookers. Lumo builds all three channels as an integrated strategy."),
            ("What is Google Hotel Ads and how does it work?", "Google Hotel Ads displays your property's rates directly in Google Search and Google Maps alongside OTA competitors, with a 'Book Direct' link to your own booking engine. You pay only when a guest completes a booking — at commission rates typically lower than OTAs. Lumo manages the full Hotel Ads setup and optimisation."),
            ("How much does hotel digital marketing cost?", "Lumo's hotel marketing packages start at $2,000/mo for local SEO, GBP management, and review strategy. Full-service packages including Google Hotel Ads start at $3,500/mo plus ad spend. A single percentage point shift from OTA to direct bookings typically pays back the full marketing investment."),
            ("How long does hotel SEO take to show results?", "Google Business Profile improvements often show results within 30 days. Organic search ranking changes typically appear within 60–90 days. Direct booking growth from SEO is usually measurable within 90–120 days. Google Hotel Ads can drive direct bookings from the first week of launch."),
            ("Does Lumo work with vacation rentals and Airbnb hosts?", "Yes. Lumo works with vacation rental managers and multi-property Airbnb operators who want to build direct booking channels independent of Airbnb and Vrbo. We build branded websites, Google Hotel Ads campaigns, and SEO strategies that drive commission-free direct reservations."),
            ("How does Lumo manage TripAdvisor and review platforms for hotels?", "Lumo implements post-stay review request sequences, professional response templates for both positive and negative reviews, and ongoing review monitoring. We also optimise your TripAdvisor listing for algorithm ranking — maximising visibility in the TripAdvisor index alongside Google."),
        ],
        "cta_h2": "Ready to Grow Direct Bookings?",
        "cta_sub": "Book a free hospitality marketing audit — we'll analyse your direct booking ratio, OTA performance, local search rankings, and show you exactly how to recapture margin from OTA commissions.",
        "related_service": "../services/google-ads.html",
        "related_label":   "Google Ads",
    },
}

# ---------------------------------------------------------------------------
# SHARED ASSETS (2 levels deep: industries/{slug}/index.html → ../../)
# ---------------------------------------------------------------------------
CSS = """
    :root {
      --bg:#0D0D14;--bg-card:#13131F;--bg-dark:#09090F;--primary:#B3FF00;
      --primary-dim:rgba(179,255,0,0.08);--secondary:#7C3AED;--accent:#00F5FF;
      --text:#F0F0FF;--muted:#6B7280;--border:rgba(179,255,0,0.15);
      --glow-lime:0 0 30px rgba(179,255,0,0.35);--radius-sm:8px;
      --radius:14px;--radius-lg:20px;--transition:0.25s cubic-bezier(0.4,0,0.2,1);
    }
    *,*::before,*::after{box-sizing:border-box;margin:0;padding:0;}
    html{scroll-behavior:smooth;-webkit-font-smoothing:antialiased;}
    body{font-family:'Inter',system-ui,sans-serif;background:var(--bg);color:var(--text);overflow-x:hidden;line-height:1.6;}
    h1,h2,h3,h4{line-height:1.15;}
    a{color:inherit;text-decoration:none;}
    img{max-width:100%;height:auto;display:block;}
    button{font-family:inherit;cursor:pointer;border:none;background:none;}
    ul{list-style:none;}
    .container{max-width:1180px;margin:0 auto;padding:0 24px;}
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
    .nav-cta{display:flex;align-items:center;gap:16px;}
    .nav-hamburger{display:none;flex-direction:column;gap:5px;padding:8px;}
    .nav-hamburger span{display:block;width:24px;height:2px;background:var(--text);border-radius:2px;transition:var(--transition);}
    .mobile-menu{display:none;flex-direction:column;gap:0;background:rgba(13,13,20,0.98);border-top:1px solid var(--border);padding:8px 24px 16px;}
    .mobile-menu.open{display:flex;}
    .mobile-menu a{padding:14px 0;border-bottom:1px solid rgba(255,255,255,0.05);color:var(--muted);font-size:0.95rem;font-weight:500;transition:color var(--transition);}
    .mobile-menu a:last-child{border-bottom:none;}
    .mobile-menu a:hover{color:var(--primary);}
    @media(max-width:768px){.nav-links,.nav-cta{display:none;}.nav-hamburger{display:flex;}}
    /* Hero */
    .page-hero{padding:140px 0 80px;position:relative;overflow:hidden;}
    .blob-wrap{position:absolute;inset:0;pointer-events:none;overflow:hidden;}
    .blob{position:absolute;border-radius:50%;filter:blur(80px);}
    .blob-lime{width:500px;height:500px;background:radial-gradient(circle,rgba(179,255,0,0.18) 0%,transparent 70%);top:-80px;left:-80px;animation:drift-a 18s ease-in-out infinite;}
    .blob-violet{width:400px;height:400px;background:radial-gradient(circle,rgba(124,58,237,0.15) 0%,transparent 70%);bottom:0;right:-60px;animation:drift-b 22s ease-in-out infinite;}
    @keyframes drift-a{0%,100%{transform:translate(0,0) scale(1);}50%{transform:translate(60px,50px) scale(1.08);}}
    @keyframes drift-b{0%,100%{transform:translate(0,0) scale(1);}50%{transform:translate(-50px,-40px) scale(1.06);}}
    .hero-noise{position:absolute;inset:0;background-image:linear-gradient(rgba(179,255,0,0.02) 1px,transparent 1px),linear-gradient(90deg,rgba(179,255,0,0.02) 1px,transparent 1px);background-size:60px 60px;pointer-events:none;}
    .hero-inner{position:relative;z-index:2;}
    .hero-badge{display:inline-flex;align-items:center;gap:8px;font-size:0.72rem;font-weight:700;letter-spacing:0.12em;text-transform:uppercase;color:var(--primary);background:rgba(179,255,0,0.08);border:1px solid rgba(179,255,0,0.2);padding:6px 14px;border-radius:50px;margin-bottom:24px;}
    .breadcrumb{display:flex;align-items:center;gap:8px;font-size:0.8rem;color:var(--muted);margin-bottom:20px;}
    .breadcrumb a:hover{color:var(--primary);}
    .breadcrumb-sep{color:rgba(179,255,0,0.3);}
    .page-hero h1{font-family:'Berkshire Swash',serif;font-size:clamp(2.4rem,5vw,4.2rem);color:var(--text);line-height:1.08;margin-bottom:20px;}
    .hl-lime{color:var(--primary);text-shadow:0 0 30px rgba(179,255,0,0.45);}
    .hl-violet{color:var(--secondary);}
    .hl-cyan{color:var(--accent);}
    .hero-sub{font-size:1.1rem;color:var(--muted);max-width:580px;margin-bottom:36px;line-height:1.7;}
    .hero-btns{display:flex;gap:14px;flex-wrap:wrap;}
    /* Stats strip */
    .stats-strip{background:var(--bg-dark);border-top:1px solid rgba(179,255,0,0.06);border-bottom:1px solid rgba(179,255,0,0.06);}
    .stats-row{display:grid;grid-template-columns:repeat(3,1fr);}
    .stat-item{padding:44px 36px;text-align:center;position:relative;}
    .stat-item:not(:last-child)::after{content:'';position:absolute;right:0;top:25%;bottom:25%;width:1px;background:rgba(179,255,0,0.08);}
    .stat-num{font-size:clamp(2rem,3.5vw,2.8rem);font-weight:900;color:var(--primary);line-height:1;text-shadow:0 0 20px rgba(179,255,0,0.3);}
    .stat-label{font-size:0.8rem;color:var(--muted);margin-top:8px;line-height:1.5;}
    @media(max-width:600px){.stats-row{grid-template-columns:1fr;}.stat-item:not(:last-child)::after{display:none;}}
    /* Section commons */
    .section-pad{padding:90px 0;}
    .section-eyebrow{display:inline-flex;align-items:center;gap:8px;font-size:0.72rem;font-weight:700;letter-spacing:0.12em;text-transform:uppercase;color:var(--primary);margin-bottom:16px;}
    .section-eyebrow::before{content:'';display:block;width:24px;height:2px;background:var(--primary);border-radius:2px;}
    .section-h2{font-family:'Berkshire Swash',serif;font-size:clamp(1.9rem,4vw,3rem);color:var(--text);margin-bottom:16px;}
    .section-sub{font-size:1rem;color:var(--muted);max-width:540px;margin-bottom:50px;line-height:1.7;}
    /* Why section */
    .why-grid{display:grid;grid-template-columns:1fr 1fr;gap:60px;align-items:start;}
    .why-text p{color:var(--muted);line-height:1.8;margin-bottom:18px;font-size:0.97rem;}
    .why-aside{background:var(--bg-card);border:1px solid var(--border);border-radius:var(--radius-lg);padding:36px;}
    .why-aside h3{font-family:'Berkshire Swash',serif;font-size:1.2rem;color:var(--primary);margin-bottom:20px;}
    .aside-list li{display:flex;align-items:flex-start;gap:12px;padding:12px 0;border-bottom:1px solid rgba(255,255,255,0.05);}
    .aside-list li:last-child{border-bottom:none;}
    .aside-check{width:20px;height:20px;border-radius:50%;background:rgba(179,255,0,0.12);border:1px solid rgba(179,255,0,0.3);display:flex;align-items:center;justify-content:center;flex-shrink:0;margin-top:1px;color:var(--primary);font-size:0.7rem;}
    .aside-text{font-size:0.88rem;color:var(--muted);line-height:1.6;}
    @media(max-width:768px){.why-grid{grid-template-columns:1fr;}}
    /* Services grid */
    .svc-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:20px;}
    .svc-card{background:var(--bg-card);border:1px solid rgba(255,255,255,0.05);border-radius:var(--radius-lg);padding:30px;display:flex;flex-direction:column;gap:12px;transition:transform 0.28s,border-color 0.28s,box-shadow 0.28s;}
    .svc-card:hover{border-color:rgba(179,255,0,0.3);box-shadow:0 0 30px rgba(179,255,0,0.08);transform:translateY(-4px);}
    .svc-icon{font-size:1.6rem;margin-bottom:4px;}
    .svc-card h3{font-size:1rem;font-weight:700;color:var(--text);}
    .svc-card p{font-size:0.85rem;color:var(--muted);line-height:1.65;flex:1;}
    @media(max-width:900px){.svc-grid{grid-template-columns:1fr 1fr;}}
    @media(max-width:560px){.svc-grid{grid-template-columns:1fr;}}
    /* Challenges */
    .challenges-section{background:var(--bg-dark);border-top:1px solid rgba(255,255,255,0.04);border-bottom:1px solid rgba(255,255,255,0.04);}
    .challenges-grid{display:grid;grid-template-columns:1fr 1fr;gap:24px;}
    .challenge-card{background:var(--bg-card);border:1px solid rgba(255,255,255,0.05);border-radius:var(--radius);padding:28px;border-left:3px solid var(--primary);}
    .challenge-card h3{font-size:0.95rem;font-weight:700;color:var(--text);margin-bottom:10px;}
    .challenge-card p{font-size:0.85rem;color:var(--muted);line-height:1.65;}
    @media(max-width:640px){.challenges-grid{grid-template-columns:1fr;}}
    /* FAQ */
    .faq-section{background:var(--bg);}
    .faq-wrap{max-width:740px;margin:0 auto;}
    .faq-item{border-bottom:1px solid rgba(179,255,0,0.08);}
    .faq-q{width:100%;text-align:left;padding:22px 0;font-size:0.97rem;font-weight:600;color:var(--text);display:flex;justify-content:space-between;align-items:center;gap:16px;cursor:pointer;background:none;border:none;font-family:inherit;}
    .faq-q .faq-arrow{width:20px;height:20px;border-radius:50%;background:rgba(179,255,0,0.08);border:1px solid rgba(179,255,0,0.2);display:flex;align-items:center;justify-content:center;flex-shrink:0;transition:transform 0.3s,background 0.3s;color:var(--primary);font-size:0.7rem;}
    .faq-item.open .faq-arrow{transform:rotate(180deg);background:rgba(179,255,0,0.15);}
    .faq-a{max-height:0;overflow:hidden;transition:max-height 0.35s ease;}
    .faq-a p{font-size:0.9rem;color:var(--muted);line-height:1.75;padding-bottom:20px;}
    .faq-item.open .faq-a{max-height:300px;}
    /* CTA Band */
    .cta-band{background:var(--bg-dark);border-top:1px solid rgba(179,255,0,0.06);text-align:center;padding:100px 0;}
    .cta-band h2{font-family:'Berkshire Swash',serif;font-size:clamp(1.9rem,4vw,3.1rem);margin-bottom:18px;}
    .cta-band p{color:var(--muted);font-size:1rem;max-width:500px;margin:0 auto 34px;}
    .cta-btns{display:flex;gap:14px;justify-content:center;flex-wrap:wrap;}
    /* Footer */
    footer{background:var(--bg-dark);border-top:1px solid rgba(179,255,0,0.08);padding:60px 0 30px;}
    .footer-inner{max-width:1180px;margin:0 auto;padding:0 24px;}
    .footer-top{display:grid;grid-template-columns:1.4fr 1fr 1fr 1fr;gap:48px;margin-bottom:48px;}
    .footer-logo{font-family:'Berkshire Swash',serif;font-size:1.5rem;color:var(--primary);display:block;margin-bottom:14px;text-shadow:0 0 20px rgba(179,255,0,0.4);}
    .footer-top p{font-size:0.85rem;color:var(--muted);line-height:1.7;margin-bottom:20px;}
    .footer-col h4{font-size:0.78rem;font-weight:700;letter-spacing:0.1em;text-transform:uppercase;color:var(--text);margin-bottom:18px;}
    .footer-col ul{display:flex;flex-direction:column;gap:10px;}
    .footer-col a{font-size:0.85rem;color:var(--muted);transition:color 0.22s;}
    .footer-col a:hover{color:var(--primary);}
    .footer-bottom{border-top:1px solid rgba(255,255,255,0.06);padding-top:22px;display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:12px;}
    .footer-bottom p,.footer-bottom a{font-size:0.8rem;color:var(--muted);}
    .footer-bottom a:hover{color:var(--primary);}
    .footer-bl{display:flex;gap:20px;}
    @media(max-width:900px){.footer-top{grid-template-columns:1fr 1fr;}}
    @media(max-width:560px){.footer-top{grid-template-columns:1fr;gap:28px;}.footer-bottom{flex-direction:column;text-align:center;}}
    #scroll-top{position:fixed;bottom:30px;right:30px;width:46px;height:46px;border-radius:12px;background:var(--primary);color:#0D0D14;display:flex;align-items:center;justify-content:center;cursor:pointer;z-index:800;opacity:0;transform:translateY(10px);transition:opacity 0.3s,transform 0.3s;border:none;}
    #scroll-top.visible{opacity:1;transform:translateY(0);}
    #scroll-top:hover{box-shadow:0 0 20px rgba(179,255,0,0.5);transform:translateY(-3px);}
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


def build_page(ind):
    slug     = ind["slug"]
    label    = ind["label"]
    canon    = f"https://lumoaiagency.com/industries/{slug}"

    svc_schema = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "WebPage",
                "name": ind["title_tag"],
                "description": ind["meta_desc"],
                "url": canon,
                "datePublished": "2026-05-13",
                "dateModified": "2026-05-13",
                "breadcrumb": {
                    "@type": "BreadcrumbList",
                    "itemListElement": [
                        {"@type":"ListItem","position":1,"name":"Home","item":"https://lumoaiagency.com"},
                        {"@type":"ListItem","position":2,"name":"Industries","item":"https://lumoaiagency.com/industries"},
                        {"@type":"ListItem","position":3,"name":label,"item":canon},
                    ]
                }
            },
            build_faq_schema(ind["faqs"])
        ]
    }

    services_html = ""
    for icon, title, desc in ind["services"]:
        services_html += f"""        <div class="svc-card">
          <div class="svc-icon">{icon}</div>
          <h3>{title}</h3>
          <p>{desc}</p>
        </div>\n"""

    challenges_html = ""
    for title, desc in ind["challenges"]:
        challenges_html += f"""        <div class="challenge-card">
          <h3>{title}</h3>
          <p>{desc}</p>
        </div>\n"""

    faqs_html = ""
    for i, (q, a) in enumerate(ind["faqs"]):
        faqs_html += f"""      <div class="faq-item">
        <button class="faq-q" aria-expanded="false">
          {q}
          <span class="faq-arrow" aria-hidden="true">▼</span>
        </button>
        <div class="faq-a" id="faq-{i}"><p>{a}</p></div>
      </div>\n"""

    # "Why" aside list — derive from services titles
    aside_items = "".join(
        f'<li class="aside-list" style="display:flex;align-items:flex-start;gap:12px;padding:11px 0;border-bottom:1px solid rgba(255,255,255,0.05);">'
        f'<span class="aside-check">✓</span>'
        f'<span class="aside-text">{title}</span></li>\n'
        for _, title, _ in ind["services"]
    )

    html = f"""<!DOCTYPE html>
<html lang="en-US">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <meta name="robots" content="index, follow" />
  <meta name="description" content="{ind['meta_desc']}" />
  <meta property="og:title" content="{ind['og_title']}" />
  <meta property="og:description" content="{ind['og_desc']}" />
  <meta property="og:url" content="{canon}" />
  <meta property="og:type" content="website" />
  <meta property="og:image" content="https://lumoaiagency.com/og-image.jpg" />
  <meta name="twitter:card" content="summary_large_image" />
  <link rel="canonical" href="{canon}" />
  <title>{ind['title_tag']}</title>

  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Berkshire+Swash&family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet" />

  <script type="application/ld+json">
{json.dumps(svc_schema, ensure_ascii=False, indent=2)}
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
  <section class="page-hero" aria-label="Hero">
    <div class="blob-wrap" aria-hidden="true"><div class="blob blob-lime"></div><div class="blob blob-violet"></div></div>
    <div class="hero-noise" aria-hidden="true"></div>
    <div class="container hero-inner">
      <nav class="breadcrumb" aria-label="Breadcrumb">
        <a href="../../index.html">Home</a>
        <span class="breadcrumb-sep" aria-hidden="true">›</span>
        <a href="../../services.html">Industries</a>
        <span class="breadcrumb-sep" aria-hidden="true">›</span>
        <span>{label}</span>
      </nav>
      <div class="hero-badge">{ind['icon']} {ind['hero_badge']}</div>
      <h1>{ind['h1']}</h1>
      <p class="hero-sub">{ind['hero_sub']}</p>
      <div class="hero-btns">
        <a href="../../contact.html" class="btn btn-lime">Get Free Audit <svg width="16" height="16" viewBox="0 0 16 16" fill="none" aria-hidden="true"><path d="M3 8h10M9 4l4 4-4 4" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg></a>
        <a href="../../pricing.html" class="btn btn-ghost">View Pricing</a>
      </div>
    </div>
  </section>

  <!-- STATS -->
  <section class="stats-strip" aria-label="Key stats">
    <div class="stats-row">
      <div class="stat-item"><div class="stat-num">{ind['stat1_num']}</div><div class="stat-label">{ind['stat1_lbl']}</div></div>
      <div class="stat-item"><div class="stat-num">{ind['stat2_num']}</div><div class="stat-label">{ind['stat2_lbl']}</div></div>
      <div class="stat-item"><div class="stat-num">{ind['stat3_num']}</div><div class="stat-label">{ind['stat3_lbl']}</div></div>
    </div>
  </section>

  <!-- WHY -->
  <section class="section-pad" aria-labelledby="why-h2">
    <div class="container">
      <div class="why-grid">
        <div class="why-text">
          <p class="section-eyebrow">Why It Matters</p>
          <h2 class="section-h2" id="why-h2">{ind['why_h2']}</h2>
          <p>{ind['why_p1']}</p>
          <p>{ind['why_p2']}</p>
          <p>{ind['why_p3']}</p>
        </div>
        <div class="why-aside">
          <h3>What We Deliver</h3>
          <ul style="list-style:none;padding:0;margin:0;">
{aside_items}          </ul>
        </div>
      </div>
    </div>
  </section>

  <!-- SERVICES -->
  <section class="section-pad" style="background:var(--bg-dark);border-top:1px solid rgba(255,255,255,0.04);" aria-labelledby="svc-h2">
    <div class="container">
      <p class="section-eyebrow">What We Do</p>
      <h2 class="section-h2" id="svc-h2">{ind['services_h2']}</h2>
      <p class="section-sub">Every engagement is tailored to your industry's specific competitive dynamics, compliance needs, and customer behaviour.</p>
      <div class="svc-grid">
{services_html}      </div>
    </div>
  </section>

  <!-- CHALLENGES -->
  <section class="section-pad challenges-section" aria-labelledby="chal-h2">
    <div class="container">
      <p class="section-eyebrow">Specialist Knowledge</p>
      <h2 class="section-h2" id="chal-h2">{ind['challenges_h2']}</h2>
      <p class="section-sub">Industry-specific marketing challenges require industry-specific solutions — not generic agency playbooks.</p>
      <div class="challenges-grid">
{challenges_html}      </div>
    </div>
  </section>

  <!-- FAQ -->
  <section class="section-pad faq-section" aria-labelledby="faq-h2">
    <div class="container">
      <div style="text-align:center;margin-bottom:48px;">
        <p class="section-eyebrow" style="justify-content:center;">FAQ</p>
        <h2 class="section-h2" id="faq-h2">Common Questions about Marketing for <span class="hl-lime">{label}</span></h2>
      </div>
      <div class="faq-wrap">
{faqs_html}      </div>
    </div>
  </section>

  <!-- CTA -->
  <section class="cta-band" aria-labelledby="cta-h2">
    <div class="container">
      <p class="section-eyebrow" style="justify-content:center;">Ready to Grow?</p>
      <h2 id="cta-h2">{ind['cta_h2']}</h2>
      <p>{ind['cta_sub']}</p>
      <div class="cta-btns">
        <a href="../../contact.html" class="btn btn-lime">Book Free Audit <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14M12 5l7 7-7 7"/></svg></a>
        <a href="{ind['related_service']}" class="btn btn-ghost">See {ind['related_label']}</a>
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
          <li><a href="../../services/tiktok-ads.html">TikTok Ads</a></li>
          <li><a href="../../services/youtube-ads.html">YouTube Ads</a></li>
          <li><a href="../../services/ecommerce-seo.html">E-commerce SEO</a></li>
          <li><a href="../../services/cro.html">CRO</a></li>
          <li><a href="../../services/ai-automations.html">AI Automations</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h4>Industries</h4>
        <ul>
          <li><a href="../../industries/seo-for-lawyers/">Law Firms</a></li>
          <li><a href="../../industries/seo-for-dentists/">Dentists</a></li>
          <li><a href="../../industries/digital-marketing-for-real-estate/">Real Estate</a></li>
          <li><a href="../../industries/restaurant-marketing/">Restaurants</a></li>
          <li><a href="../../industries/healthcare-seo/">Healthcare</a></li>
          <li><a href="../../industries/saas-marketing/">SaaS & Tech</a></li>
          <li><a href="../../industries/ecommerce-marketing/">E-commerce</a></li>
          <li><a href="../../industries/home-services-seo/">Home Services</a></li>
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
        <h4 style="margin-top:22px;">Contact</h4>
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
    for slug, ind in INDUSTRIES.items():
        out_dir = os.path.join(BASE, "industries", slug)
        os.makedirs(out_dir, exist_ok=True)
        html = build_page(ind)
        with open(os.path.join(out_dir, "index.html"), "w", encoding="utf-8") as f:
            f.write(html)
        print(f"Created: industries/{slug}/index.html ({len(html):,} chars)")
    print(f"Done. {len(INDUSTRIES)} pages created.")


if __name__ == "__main__":
    main()
