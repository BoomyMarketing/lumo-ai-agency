"""Batch 12 — Backlog Batch 7: ugc-marketing, brand-storytelling, appointment-setting, referral-marketing, listings-management"""
import json, os

SERVICES = {
    "ugc-marketing": {
        "title": "UGC Marketing",
        "tagline": "Authentic user-generated content that drives trust and conversions at scale",
        "desc": "User-generated content outperforms branded content on every platform — because people trust people, not brands. We build and manage systematic UGC programs: sourcing authentic creators, managing production, and deploying content across your paid and organic channels to drive measurable conversion lifts.",
        "price": "$2,500/mo",
        "stat1": "79%",
        "stat1_label": "of people say UGC influences purchase decisions",
        "stat2": "4x",
        "stat2_label": "higher click-through rates vs. branded creative",
        "stat3": "29%",
        "stat3_label": "higher web conversions with UGC on product pages",
        "deliverables": [
            ("🔍", "Creator Sourcing & Vetting", "We identify and vet UGC creators matched to your product, audience demographics, and content style — prioritizing creators with genuine product affinity over follower count."),
            ("📋", "Creative Briefs & Direction", "Detailed creative briefs for every creator: talking points, visual requirements, platform specs, brand dos/don'ts, and CTA guidance — ensuring on-brand output without stifling authenticity."),
            ("🎬", "Content Production Management", "End-to-end production management: creator coordination, revision rounds, content approval workflow, and rights acquisition for paid media usage."),
            ("📱", "Platform Deployment", "Optimized deployment across Meta Ads (as Collaborative Ads or dark posts), TikTok Spark Ads, Instagram organic, and product pages — with platform-specific formatting for each placement."),
            ("🧪", "A/B Testing & Optimization", "Systematic testing of UGC creative: comparing hooks, formats, creator demographics, and content styles — feeding learnings back into brief development for continuous improvement."),
            ("⚖️", "Rights Management", "Usage rights documentation for all content — covering paid media usage, duration, platforms, and territory — protecting you from IP disputes."),
            ("📊", "Performance Reporting", "Monthly reporting on UGC creative performance: CTR, CPM, conversion rate, ROAS, and engagement — with creator-level and format-level breakdowns."),
        ],
        "process": [
            ("🔍", "Strategy & Creator Match", "We define your UGC content strategy, identify creator personas, and source 5–15 matched creators from our vetted network or via targeted outreach."),
            ("📋", "Brief & Onboard", "Creative briefs developed for each creator. Creators briefed, products shipped, and production timelines confirmed. Approval workflow established."),
            ("🎬", "Produce & Deploy", "Content reviewed, approved, and deployed across channels. Paid ads launched with UGC creative; organic posts scheduled. Rights documentation completed."),
            ("📈", "Test & Scale", "Performance data analyzed weekly. Top-performing UGC creative scaled; underperformers replaced. New briefs developed based on winning content patterns."),
        ],
        "faqs": [
            ("Do the creators need to have large followings?", "No — UGC is about authenticity, not reach. We prioritize creators with 500–10K followers who have genuine product interest and high engagement rates. Large-following influencers are a different service."),
            ("Do we keep the content rights?", "Yes — all content produced under our UGC program includes full usage rights for paid media, organic posting, and website use for a defined period (typically 12 months, renewable)."),
            ("How many UGC videos do we get per month?", "Standard retainer includes 10–20 UGC assets per month (videos and statics). Volume scales with your budget and testing velocity."),
            ("Can we use UGC in our paid ads?", "Absolutely — that's often where it performs best. We format all content for Meta dark posts, TikTok Spark Ads, and other paid placements with proper usage rights documentation."),
            ("What if the content doesn't match our brand?", "Our detailed creative briefs and approval process catch misaligned content before it's finalized. If a creator consistently misses the brief, we replace them at no additional cost."),
        ],
        "schema_service_desc": "UGC marketing — creator sourcing, creative briefs, production management, paid media deployment, A/B testing, rights management, and performance reporting.",
    },
    "brand-storytelling": {
        "title": "Brand Storytelling",
        "tagline": "Narrative strategy that builds emotional connection and long-term brand equity",
        "desc": "Brand storytelling is the difference between a company people buy from and one they believe in. We develop your brand narrative — the origin story, mission, values, and customer transformation stories — and translate it into content across every channel, building the emotional connection that makes your marketing work harder.",
        "price": "$3,500/mo",
        "stat1": "5x",
        "stat1_label": "more persuasive than facts alone — stories activate emotion",
        "stat2": "64%",
        "stat2_label": "of consumers buy based on shared brand values",
        "stat3": "22x",
        "stat3_label": "more memorable than facts when delivered as a story",
        "deliverables": [
            ("📖", "Brand Narrative Development", "We excavate your brand's authentic story — founders, origin, mission, and the problem you exist to solve — and articulate it in a compelling narrative framework that guides all content."),
            ("🎯", "Messaging Architecture", "A tiered messaging system: brand-level story, audience-specific value propositions, product/service narratives, and proof point libraries — ensuring consistency across every touchpoint."),
            ("✍️", "Signature Content Pieces", "Long-form brand storytelling content: founder essays, mission manifestos, customer transformation case studies, and origin stories — for website, press, and social use."),
            ("📱", "Social Storytelling", "Ongoing social media content that tells your brand story in episodic format — building narrative threads across posts, stories, and series that keep audiences engaged over time."),
            ("🎬", "Video Story Scripts", "Scripts for brand video content: origin story videos, customer testimonial narratives, team culture videos, and cause/mission content — ready for production."),
            ("📰", "PR Narrative Package", "Compelling company narrative and story angles prepared for press outreach — making it easy for journalists and podcasters to understand and tell your story accurately."),
            ("🔄", "Story Audit & Refresh", "Quarterly audit of your brand story's consistency across website, social, ads, and sales materials — with a gap analysis and recommendations for alignment."),
        ],
        "process": [
            ("🔍", "Story Discovery", "Deep-dive interviews with founders, team members, and customers to uncover the authentic human story behind your brand — the real origin, the real mission, the real transformation."),
            ("📖", "Narrative Architecture", "We build your brand narrative framework: core story, messaging hierarchy, character archetypes, and content themes — the strategic foundation for all storytelling."),
            ("✍️", "Content Production", "Signature content pieces produced and delivered: brand story, messaging guide, and first content series. Review and refinement rounds included."),
            ("🔄", "Ongoing Storytelling", "Monthly content production: social narratives, blog stories, video scripts, and campaign content — all building on the established brand narrative foundation."),
        ],
        "faqs": [
            ("What if our brand story isn't very exciting?", "Every brand has a compelling story — most just haven't found the right angle yet. Our discovery process consistently surfaces authentic elements that resonate: the problem the founder couldn't stop thinking about, the customer who changed everything, the near-failure that clarified the mission."),
            ("How is brand storytelling different from content marketing?", "Content marketing informs; brand storytelling connects. Content answers questions — storytelling creates belief. Both work together: storytelling gives your content emotional resonance and brand differentiation that makes people choose you over equally qualified competitors."),
            ("How long does it take to develop the brand narrative?", "The initial brand narrative framework and messaging architecture is delivered within 3–4 weeks. Signature content pieces (founder story, customer stories) are delivered in weeks 4–6."),
            ("Will this affect our existing marketing?", "Yes — intentionally. The brand narrative becomes the foundation that makes all your existing marketing more consistent and more effective. We help you retrofit the narrative across existing channels without disrupting active campaigns."),
            ("Do you handle distribution of the story content?", "We produce the content; distribution is coordinated with your marketing team or through our other services (social media, PR, blog writing). We provide a distribution strategy as part of the engagement."),
        ],
        "schema_service_desc": "Brand storytelling — narrative development, messaging architecture, signature content, social storytelling, video scripts, PR narrative package, and ongoing story production.",
    },
    "appointment-setting": {
        "title": "Appointment Setting",
        "tagline": "Qualified sales meetings delivered to your calendar — consistently",
        "desc": "We fill your sales team's calendar with qualified meetings — targeting your ideal accounts, personalizing outreach at scale, and handling the multi-touch follow-up sequence that turns cold prospects into booked calls. Our appointment setters work as an extension of your team, using your brand voice and following your qualification criteria.",
        "price": "$3,000/mo",
        "stat1": "80%",
        "stat1_label": "of sales require 5+ follow-up touches to book",
        "stat2": "22%",
        "stat2_label": "average meeting show rate improvement with our nurture sequences",
        "stat3": "6–12",
        "stat3_label": "qualified meetings booked per month on average",
        "deliverables": [
            ("🎯", "ICP & Target List Building", "We define your ideal customer profile (ICP) and build a targeted prospecting list from LinkedIn Sales Navigator, Apollo, ZoomInfo, and other sources — verified emails and direct contact info."),
            ("✍️", "Personalized Outreach Sequences", "Multi-touch outreach sequences across email, LinkedIn, and phone — personalized at the company and contact level, not generic templates. We write sequences in your brand voice."),
            ("📧", "Email Infrastructure Setup", "Properly warmed sending domains, SPF/DKIM/DMARC configuration, and deliverability monitoring — ensuring your outreach lands in the inbox, not spam."),
            ("📞", "Follow-Up & Objection Handling", "Persistent follow-up sequences with objection-handling messaging — addressing common hesitations (timing, budget, existing solution) to convert skeptical prospects into booked meetings."),
            ("📅", "Calendar Management", "Meeting scheduling directly into your team's calendar via Calendly or your CRM — with automated reminders and pre-meeting brief packets for your sales reps."),
            ("🔄", "Show Rate Optimization", "Post-booking nurture sequences to reduce no-shows: reminder emails, pre-meeting resources, and meeting confirmation protocols that keep your calendar full."),
            ("📊", "Pipeline Reporting", "Weekly reporting on contacts prospected, sequence open and reply rates, meetings booked, show rates, and qualified opportunity count — full funnel visibility."),
        ],
        "process": [
            ("🔍", "ICP Definition & Setup", "We interview your sales team, review your best customers, and define your ICP precisely. Email infrastructure configured. CRM integration established. Sequence copy drafted and approved."),
            ("📋", "List Build & Launch", "Target list built to ICP specifications. Sequences launched with initial batch of 200–500 prospects. Deliverability monitored from day one."),
            ("📞", "Prospect & Follow Up", "Daily outreach, follow-up management, and response handling. Interested prospects moved to meeting scheduling; unqualified leads flagged and removed."),
            ("📈", "Optimize & Scale", "Weekly performance review: what's converting, what's not. Sequence copy, targeting, and messaging refined weekly based on reply data. Scale what's working."),
        ],
        "faqs": [
            ("How many meetings can we expect per month?", "Volume depends on your ICP size, offer strength, and market conditions. Our clients typically see 6–12 qualified meetings per month by month 2–3. We set realistic expectations upfront based on your target market."),
            ("Do your setters work under our brand or yours?", "All outreach goes under your brand — your domain, your email signature, your LinkedIn. We are an invisible extension of your team. Prospects interact with 'your company', not with us."),
            ("What CRM do you work with?", "We work with HubSpot, Salesforce, Pipedrive, Close, and most major CRMs. If you don't have a CRM, we can set up a lightweight tracking system."),
            ("How do you qualify leads before booking?", "Your qualification criteria are built into the outreach sequence and pre-meeting questionnaire. We only book meetings that meet your defined requirements (company size, budget, decision-maker title, etc.)."),
            ("What's the difference between appointment setting and SDR outsourcing?", "Appointment setting focuses purely on booking qualified meetings. Full SDR outsourcing includes more discovery and early-stage selling. We recommend which model fits your sales cycle based on your ACV and product complexity."),
        ],
        "schema_service_desc": "Appointment setting — ICP list building, personalized outreach sequences, email infrastructure, follow-up management, calendar booking, and pipeline reporting.",
    },
    "referral-marketing": {
        "title": "Referral Marketing",
        "tagline": "Turn customers into your best sales channel with systematic referral programs",
        "desc": "Referred customers close faster, spend more, and churn less — yet most businesses leave this channel completely unmanaged. We design, implement, and optimize referral programs that systematically convert your happiest customers into a reliable pipeline source — with the right incentive structure, automation, and tracking to make it scale.",
        "price": "$1,800/mo",
        "stat1": "92%",
        "stat1_label": "of consumers trust referrals from people they know",
        "stat2": "16%",
        "stat2_label": "higher LTV for referred customers vs. other channels",
        "stat3": "3–5x",
        "stat3_label": "higher conversion rate for referred leads",
        "deliverables": [
            ("🎯", "Referral Program Strategy", "We design your referral program from the ground up: incentive structure (cash, credit, gift, recognition), referral mechanics, eligibility criteria, and program positioning in your customer journey."),
            ("⚙️", "Program Setup & Automation", "Full technical implementation using ReferralHero, Referral Factory, or custom-built solutions — with automated tracking, reward fulfillment triggers, and CRM integration."),
            ("📧", "Customer Activation Campaigns", "Email and in-app campaigns to activate your existing customer base as referrers — timed to high-satisfaction moments (post-purchase, milestone, renewal) for maximum participation."),
            ("🎨", "Referral Asset Creation", "Everything referrers need: shareable links, pre-written social copy, email templates, and referral cards — reducing friction and making sharing effortless."),
            ("📊", "Tracking & Attribution", "End-to-end referral tracking: who referred whom, conversion status, reward fulfillment, and program ROI — with clean attribution to distinguish referral from other channels."),
            ("🔄", "Program Optimization", "Monthly A/B testing of incentive types, activation timing, and messaging — continuously improving participation rate and referral conversion rate."),
            ("🏆", "Referrer Recognition Program", "Tiered recognition for top referrers: leaderboards, milestone rewards, and VIP status — gamifying the program to sustain long-term engagement."),
        ],
        "process": [
            ("🔍", "Program Design", "We audit your customer base, identify high-satisfaction segments, benchmark competitor programs, and design an incentive structure optimized for your product and price point."),
            ("⚙️", "Build & Integrate", "Technical implementation, CRM integration, tracking setup, and reward fulfillment automation. Customer-facing referral assets designed and copy written."),
            ("📧", "Launch & Activate", "Activation campaign to your existing customer base. Referral program introduced at key customer journey touchpoints. Show rate monitored from day one."),
            ("📈", "Optimize & Scale", "Monthly performance review: participation rate, referral conversion, CAC, and ROI. Incentive and messaging tested for improvement. Top referrers identified and nurtured."),
        ],
        "faqs": [
            ("What incentive structure works best?", "It depends on your product and customer profile. Cash rewards work well for high-ticket B2B. Account credit works for SaaS. Gift rewards work for consumer products. We recommend the structure based on your economics and test alternatives."),
            ("Do we need special software?", "We implement using existing platforms (ReferralHero, Referral Factory, or your CRM's native tools) or build custom solutions if needed. We handle the technical setup."),
            ("How long until we see referrals coming in?", "Most programs see first referrals within 2–4 weeks of launch if there's an engaged customer base. Volume builds over 3–6 months as the program becomes part of your customer culture."),
            ("Can we run a referral program in B2B?", "Yes — B2B referral programs often outperform B2C because professional trust is higher and deal values justify larger incentives. The mechanics differ (incentive type, activation timing) but the principle is the same."),
            ("What if our customers don't participate?", "Low participation usually signals one of three things: wrong incentive, wrong timing, or insufficient activation effort. We diagnose the issue and iterate. Initial activation campaigns consistently move participation from 0% to 5–15% of the customer base."),
        ],
        "schema_service_desc": "Referral marketing — program design, technical setup, customer activation campaigns, referral assets, tracking, and ongoing optimization.",
    },
    "listings-management": {
        "title": "Listings Management",
        "tagline": "Accurate business listings across 70+ directories — no inconsistencies, no lost traffic",
        "desc": "Inconsistent NAP (Name, Address, Phone) data across online directories directly hurts your local search rankings and costs you customers. We audit, correct, and maintain your business listings across 70+ platforms — Google Business Profile, Yelp, Apple Maps, Bing Places, and industry-specific directories — ensuring perfect consistency and maximum local visibility.",
        "price": "$500/mo",
        "stat1": "73%",
        "stat1_label": "of consumers lose trust in businesses with inaccurate listings",
        "stat2": "70+",
        "stat2_label": "directories managed in our listings network",
        "stat3": "4x",
        "stat3_label": "more likely to be considered reputable with consistent listings",
        "deliverables": [
            ("🔍", "Full Listings Audit", "A complete audit of your current listings across 70+ directories — identifying missing listings, NAP inconsistencies, duplicate entries, incorrect categories, and outdated information."),
            ("✅", "Listings Creation & Correction", "We create missing listings and correct all inaccurate data: business name, address, phone number, website URL, hours, categories, and service descriptions — across every platform."),
            ("📍", "Google Business Profile Management", "Ongoing GBP management: photo uploads, post publishing, Q&A monitoring, attribute updates, and service area management — the most important listing for local search."),
            ("🏪", "Apple Maps & Bing Places", "Full setup and ongoing management of Apple Maps Connect and Bing Places — capturing search traffic from non-Google search engines and iOS native map searches."),
            ("📂", "Industry-Specific Directories", "Management of industry-relevant directories: Healthgrades (healthcare), Avvo (legal), Houzz (home services), TripAdvisor (hospitality), and others specific to your vertical."),
            ("🔄", "Duplicate Suppression", "Identification and suppression of duplicate listings that confuse search engines and split review equity — a common issue for businesses that have moved or rebranded."),
            ("📊", "Monthly Listings Report", "Monthly report showing listing accuracy score, new listings added, corrections made, and GBP performance metrics (views, clicks, direction requests, calls)."),
        ],
        "process": [
            ("🔍", "Audit & Benchmark", "We run your business through our listings audit tool, generating a complete accuracy report across 70+ directories. We identify every inconsistency and prioritize fixes by impact."),
            ("✅", "Correct & Create", "Corrections submitted to all major platforms. New listings created where absent. Data synced through our listings distribution network for rapid propagation."),
            ("📍", "GBP Optimization", "Google Business Profile fully optimized: all attributes completed, photos uploaded, posts published, and Q&A seeded — maximizing your local pack visibility."),
            ("🔄", "Monitor & Maintain", "Monthly monitoring for data drift (directories sometimes revert to old data), new duplicate detection, review monitoring, and GBP post publishing."),
        ],
        "faqs": [
            ("Why do my listings have wrong information?", "Data aggregators like Data Axle and Neustar Localeze distribute business data to hundreds of directories. If their records are outdated, incorrect data propagates everywhere. We correct the data at source and at every directory level."),
            ("How long does it take to fix listings?", "Major platforms (Google, Yelp, Apple Maps) update within 1–2 weeks. The full network of 70+ directories typically stabilizes within 4–8 weeks as data propagates through the aggregator network."),
            ("Do you manage Google Business Profile reviews?", "Our listings management service monitors reviews and alerts you to new reviews. Active review response is included in our Reputation Management or Review Management services."),
            ("What if we have multiple locations?", "Multi-location listings management is available at a per-location rate. We manage the full network consistently, with location-specific data for each branch."),
            ("Is this a one-time fix or ongoing?", "Ongoing management is essential. Directory data drifts constantly — platforms update records from aggregators, users suggest edits, and Google makes automated changes. Monthly monitoring prevents regression."),
        ],
        "schema_service_desc": "Listings management — full directory audit, NAP correction across 70+ platforms, Google Business Profile management, Apple Maps, Bing Places, and monthly monitoring.",
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
            <li><a href="../services/ugc-marketing.html">UGC Marketing</a></li>
            <li><a href="../services/brand-storytelling.html">Brand Storytelling</a></li>
            <li><a href="../services/appointment-setting.html">Appointment Setting</a></li>
            <li><a href="../services/referral-marketing.html">Referral Marketing</a></li>
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
