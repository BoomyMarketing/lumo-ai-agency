#!/usr/bin/env python3
"""Backlog Batch 3:
   account-based-marketing, outbound-sales, cold-email-outreach,
   affiliate-marketing, white-label-marketing
"""
import os, json

BASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "services")
os.makedirs(BASE, exist_ok=True)

SERVICES = {

    "account-based-marketing": {
        "title_tag":  "Account-Based Marketing Agency | ABM Strategy & Execution | Lumo AI",
        "meta_desc":  "Account-based marketing services from Lumo AI Agency. ABM strategy, target account identification, multi-channel engagement, and pipeline attribution for B2B companies. Free ABM audit.",
        "canonical":  "https://lumoaiagency.com/services/account-based-marketing",
        "og_title":   "Account-Based Marketing Agency | Lumo AI Agency",
        "og_desc":    "Stop casting wide nets. ABM focuses your marketing on the accounts most likely to close — with personalised, multi-channel campaigns that align marketing and sales around your highest-value prospects.",
        "h1_html":    "Account-Based Marketing That <span class=\"hl-lime\">Targets the Accounts</span> Worth Winning",
        "badge":      "ABM Strategy Specialists",
        "lead":       "Account-based marketing treats high-value target accounts as markets of one — delivering personalised, coordinated campaigns across every channel your buyers use. B2B companies running ABM programs see 208% higher revenue from marketing compared to non-ABM approaches. Lumo builds end-to-end ABM programs that align marketing and sales around your most valuable opportunities.",
        "stat1_num": "208%", "stat1_lbl": "Higher revenue for companies using ABM vs. non-ABM marketing",
        "stat2_num": "87%",  "stat2_lbl": "Of B2B marketers say ABM outperforms other marketing investments",
        "stat3_num": "3x",   "stat3_lbl": "Higher deal size from ABM accounts vs. inbound-only approach",
        "why_h2": "Why ABM Beats Traditional B2B Marketing for High-Value Accounts",
        "why_p1": "Traditional B2B marketing casts wide nets — content marketing, SEO, webinars, and trade shows — hoping the right buyers find you. For most B2B companies, 80% of revenue comes from 20% of customers, yet most marketing budgets are spread evenly across all audience segments. ABM flips this allocation: concentrate your marketing investment on the accounts with the highest revenue potential, with campaigns personalised to the specific people making the buying decision.",
        "why_p2": "The sales and marketing alignment problem is where most B2B programs break down. Marketing generates leads that sales dismisses as unqualified. Sales complains about lead quality; marketing complains about follow-up. ABM eliminates this tension by starting with the accounts sales actually wants to win — building marketing programs around those specific targets rather than hoping inbound channels attract the right profile.",
        "why_p3": "Lumo's ABM programs combine target account identification (data-driven ICP scoring across your prospect universe), multi-channel engagement (coordinated LinkedIn, display retargeting, content, outbound email, and event strategies), and closed-loop attribution that measures marketing's contribution to pipeline and revenue at the account level. Marketing and sales share the same target list and the same success metrics.",
        "services_h2": "Our Account-Based Marketing Services",
        "services": [
            ("🎯", "Target Account Identification", "Data-driven ICP scoring to identify your highest-value target accounts — firmographic fit, intent data signals, technographic data, and account-level research to prioritise your top 100–500 accounts."),
            ("🗺️", "ABM Strategy & Playbook", "Tier-based ABM strategy (1:1 for top accounts, 1:few for clusters, 1:many for broader ICP) with campaign playbooks defining messaging, channels, cadence, and success metrics for each tier."),
            ("💼", "LinkedIn ABM Campaigns", "Company and contact-level LinkedIn targeting — Sponsored Content, Message Ads, and Lead Gen Forms targeted at specific job titles within target accounts — with personalised creative and offer by account segment."),
            ("🖥️", "Display Retargeting for Target Accounts", "IP-based and cookie-based display advertising serving personalised ads to individuals at target companies across the open web — maintaining brand visibility between direct outreach touchpoints."),
            ("📝", "Personalised Content & Outreach", "Account-specific content (landing pages, case studies, industry-relevant offers) and personalised email sequences coordinated with sales outreach — ensuring every touchpoint is relevant to the specific account's context."),
            ("📊", "Account-Level Attribution", "Pipeline and revenue attribution at the account level — tracking which marketing touchpoints influenced each account's progression through the funnel, with closed-loop reporting connecting ABM investment to won revenue."),
        ],
        "process": [
            ("🎯", "ICP & Account Selection", "Define ICP criteria, score your prospect universe, identify top target accounts by tier, conduct account-level research, and build account profiles for personalisation — agreed with sales before any campaign begins."),
            ("📋", "Strategy & Playbook", "ABM tier strategy, messaging architecture per account segment, channel selection, content and creative requirements, outreach cadence, and handoff protocols between marketing and sales."),
            ("🚀", "Campaign Execution", "Launch coordinated multi-channel campaigns — LinkedIn, display, email, and direct mail where applicable — with personalised content per account tier and daily monitoring for engagement signals."),
            ("📈", "Measure & Optimise", "Weekly account engagement scoring, pipeline influence reporting, account-level intent signal tracking, and monthly attribution review — optimising channel mix and messaging based on which approaches are moving accounts through the funnel."),
        ],
        "price_from": "$3,500",
        "price_note": "per month — ABM program scope and pricing scales with number of target accounts and channel complexity",
        "faqs": [
            ("How many target accounts do I need for ABM to be worthwhile?", "ABM programs are viable at almost any scale. 1:1 ABM (deeply personalised campaigns for your top 10–25 accounts) requires intensive resources but delivers the highest deal size impact. 1:few ABM (clustered campaigns for 50–200 accounts by industry or segment) is the most common entry point for mid-market B2B companies. 1:many ABM (programmatic ABM for 200–1,000+ accounts) is closer to targeted demand generation. Lumo recommends starting with 1:few for most clients and expanding as the program matures."),
            ("How is ABM different from regular B2B marketing?", "Traditional B2B marketing starts with channels (let's do content marketing, let's run LinkedIn ads) and hopes the right people find it. ABM starts with specific accounts (these are the 200 companies we want as customers) and builds campaigns specifically designed to engage the decision-makers at those companies. The sequence is reversed: accounts first, channels second. This also means ABM success is measured at the account level (pipeline influenced, accounts engaged) rather than at the lead level."),
            ("How do we identify which accounts to target?", "Lumo uses a combination of: firmographic data (company size, industry, revenue, location matching your best customer profile), technographic data (technologies the company uses that indicate fit), intent data (signals that specific companies are actively researching your category), and account-level engagement history (companies already visiting your website or engaging with your content). We combine these signals into a composite ICP score and prioritise accounts by expected revenue potential."),
            ("What's the minimum timeline to see ABM results?", "ABM works on longer timelines than demand generation because it targets enterprise accounts with multi-month sales cycles. Account awareness and engagement metrics are visible within 60–90 days. Pipeline influence (accounts progressing to opportunity stage with documented ABM touchpoints) typically appears at the 3–6 month mark. Closed revenue attributed to ABM campaigns is typically measured at the 6–12 month mark, matching your average sales cycle length."),
            ("How does ABM coordinate with our sales team?", "ABM requires tight sales-marketing alignment — which Lumo establishes in the strategy phase. This includes: a shared target account list agreed between marketing and sales, agreed definitions of what constitutes 'account engagement' that triggers a sales outreach, a handoff protocol defining which marketing signals prompt sales to reach out, and a joint review cadence (bi-weekly or monthly) where marketing and sales review account engagement data and adjust strategy together."),
        ],
        "cta_h2": "Ready to Focus Your Marketing on the Accounts Actually Worth Winning?",
        "cta_sub": "Get a free ABM audit — we'll assess your current ICP definition, target account list quality, and multi-channel readiness, then show you what a coordinated ABM program would look like for your top accounts.",
        "schema_service_name": "Account-Based Marketing Services",
        "schema_service_desc": "ABM strategy and execution for US B2B companies — target account identification, multi-channel engagement, personalised content, and account-level pipeline attribution.",
    },

    "outbound-sales": {
        "title_tag":  "Outbound Sales Agency | B2B Sales Development & Pipeline Building | Lumo AI",
        "meta_desc":  "Outbound sales services from Lumo AI Agency. SDR-as-a-service, prospect list building, multi-channel outbound sequences, and pipeline generation for US B2B companies. Free outbound audit.",
        "canonical":  "https://lumoaiagency.com/services/outbound-sales",
        "og_title":   "Outbound Sales Agency | Lumo AI Agency",
        "og_desc":    "Build pipeline without building a full sales team. Lumo's outbound sales programs — prospect research, multi-channel sequences, and meeting booking — generate qualified opportunities for B2B companies.",
        "h1_html":    "Outbound Sales That <span class=\"hl-lime\">Builds Pipeline</span> Before You Have a Sales Team",
        "badge":      "Outbound Sales Development Specialists",
        "lead":       "Most B2B companies wait for inbound leads to build pipeline — then wonder why growth is inconsistent. Outbound sales creates pipeline on demand: targeted prospect research, multi-channel outreach sequences, and meeting booking that puts qualified opportunities in front of your closers. Lumo's outbound programs work as a standalone SDR function or alongside your existing sales team.",
        "stat1_num": "80%",  "stat1_lbl": "Of B2B sales require 5+ touchpoints before a meeting is booked",
        "stat2_num": "3x",   "stat2_lbl": "More pipeline generated by multi-channel vs. cold email only",
        "stat3_num": "50%",  "stat3_lbl": "Of buyers prefer to be contacted proactively by vendors they fit",
        "why_h2": "Why Outbound Sales Is the Fastest Path to Predictable B2B Pipeline",
        "why_p1": "Inbound marketing builds pipeline over months and years — it's powerful but slow. Outbound sales can generate pipeline in weeks: identify the right prospects, deliver a compelling message across multiple channels, and book meetings with buyers who match your ICP. For early-stage companies, new market entry, and businesses launching new products, outbound is often the only reliable path to rapid pipeline generation.",
        "why_p2": "Most outbound programs fail because of one of three problems: a poorly defined ICP (reaching the wrong people), generic messaging (failing to give prospects a reason to respond), or single-channel execution (cold email only). Modern outbound requires multi-touch, multi-channel sequences — email, LinkedIn, phone, video — with personalisation that demonstrates you've done your research on the specific prospect.",
        "why_p3": "Lumo's outbound programs combine precise prospect identification, highly personalised messaging frameworks, and multi-channel sequence execution with performance measurement at every step. We track reply rate, meeting acceptance rate, and — critically — meeting-to-opportunity rate, ensuring the meetings booked are with prospects who can actually buy, not just prospects willing to take a call.",
        "services_h2": "Our Outbound Sales Services",
        "services": [
            ("🔍", "Prospect Research & List Building", "ICP-driven prospect list building — company identification by firmographic criteria, contact discovery for target job titles, data enrichment for personalisation, and list validation for deliverability and accuracy."),
            ("✍️", "Outbound Messaging Strategy", "Messaging framework development — value proposition, pain point mapping, objection handling, and multi-variant copy for cold email, LinkedIn, and phone — tested and refined against reply rate data."),
            ("📧", "Multi-Channel Sequence Execution", "Coordinated outbound sequences across cold email, LinkedIn connection and message, and phone — managed through sales engagement platforms (Outreach, Salesloft, Apollo) with automated follow-up and manual personalisation."),
            ("📅", "Meeting Booking & Handoff", "Calendar management, meeting confirmation, pre-meeting prospect research briefing, and CRM handoff to your closing team — ensuring meetings are well-prepared and prospects are correctly qualified before they reach sales."),
            ("🎯", "ICP Refinement & Segmentation", "Ongoing ICP analysis based on reply rate, meeting acceptance, and meeting-to-opportunity data — identifying which prospect segments, messaging, and value propositions are generating the highest-quality pipeline."),
            ("📊", "Pipeline & Performance Reporting", "Weekly activity reports (contacts touched, emails sent, LinkedIn connections, calls made), reply rate and meeting booking rate tracking, pipeline influence reporting, and monthly strategy review with sequence optimisation."),
        ],
        "process": [
            ("🎯", "ICP & Messaging", "Define ideal customer profile, identify addressable prospect universe, develop core value proposition and pain point messaging, create sequence scripts and variants — agreed before any outreach begins."),
            ("🏗️", "List & Tools Setup", "Prospect list build and validation, sales engagement platform configuration, email domain warmup and deliverability setup, LinkedIn account configuration, and CRM integration."),
            ("🚀", "Launch & Optimise", "Sequence launch with daily monitoring for replies, weekly reply rate analysis, A/B testing of subject lines and opening lines, and rapid iteration on low-performing sequence steps."),
            ("📈", "Scale & Report", "Scale volume on proven sequences, add new prospect segments, expand to new channels as performance data matures, and monthly review of pipeline generated vs. outbound investment."),
        ],
        "price_from": "$2,500",
        "price_note": "per month — includes prospect research, sequence management, and meeting booking (tech stack costs separate)",
        "faqs": [
            ("Is outbound sales the same as spam?", "No — done correctly, outbound is targeted, relevant, and personalised. Spam is mass unsolicited messages with no relevance to the recipient. Effective outbound contacts specifically identified prospects who match your ICP, with messages referencing their specific company context, recent news, or pain points relevant to their role. The distinction is relevance and personalisation — the same email sent to 10,000 random contacts is spam; the same message personalised to 50 carefully selected prospects is outbound."),
            ("How many meetings per month can outbound generate?", "Meeting volume depends on your ICP, message quality, and target market competitiveness. For most B2B outbound programs, a well-run sequence targeting a well-defined ICP generates 8–20 qualified meetings per month per 1,000 contacts touched. Lumo sets realistic meeting targets based on your specific market, average deal size, and acceptable cost-per-meeting — and optimises sequences aggressively in the first 60 days to hit those targets."),
            ("What's the difference between outbound sales and cold email?", "Cold email is one component of outbound sales — typically the first touchpoint in a multi-step sequence. Full outbound sales includes cold email, LinkedIn outreach and messaging, phone calls, personalised video, and direct mail in some cases. Multi-channel outbound significantly outperforms cold email alone — prospects who receive a LinkedIn connection request followed by an email followed by a personalised video respond at 3–5x the rate of cold email only campaigns."),
            ("Do you make cold calls as part of outbound programs?", "Lumo's outbound programs are primarily email and LinkedIn-led, with optional phone integration. We recommend phone as a mid-sequence touchpoint (after 2–3 email contacts) rather than a cold-call-first approach — prospects who've seen your email and LinkedIn message are significantly more receptive to a call than completely cold contacts. Phone is particularly effective for high-ACV enterprise deals where the additional touchpoint justifies the time investment."),
            ("How do you ensure outbound doesn't damage our brand?", "Brand protection starts with prospect selection — only contacting companies and roles that genuinely fit your ICP, and immediately removing contacts who reply negatively. Message quality is the second protection: relevant, personalised, and professional copy that doesn't make inflated promises or use manipulative pressure tactics. We also manage unsubscribe requests immediately and configure email infrastructure to prevent domain reputation damage."),
        ],
        "cta_h2": "Ready to Build Predictable Pipeline Without Waiting for Inbound?",
        "cta_sub": "Get a free outbound audit — we'll assess your ICP definition, current messaging, and prospect data quality, then show you what a targeted multi-channel outbound program would generate for your business.",
        "schema_service_name": "Outbound Sales Development Services",
        "schema_service_desc": "B2B outbound sales programs for US companies — prospect research, multi-channel sequences, meeting booking, and pipeline generation for B2B sales development.",
    },

    "cold-email-outreach": {
        "title_tag":  "Cold Email Outreach Agency | B2B Email Prospecting Services | Lumo AI",
        "meta_desc":  "Cold email outreach services from Lumo AI Agency. Prospect list building, deliverability infrastructure, personalised sequence writing, and reply management for US B2B companies. Free audit.",
        "canonical":  "https://lumoaiagency.com/services/cold-email-outreach",
        "og_title":   "Cold Email Outreach Agency | Lumo AI Agency",
        "og_desc":    "Cold email that lands in the primary inbox and gets replies. Lumo manages deliverability infrastructure, prospect research, personalised sequences, and reply handling for B2B companies.",
        "h1_html":    "Cold Email That <span class=\"hl-lime\">Lands, Gets Read</span>, and Books Meetings",
        "badge":      "Cold Email Outreach Specialists",
        "lead":       "Cold email remains the highest-ROI outbound channel for B2B — when done correctly. The majority of cold email programs fail on deliverability (landing in spam), relevance (generic copy that ignores the recipient's context), or follow-up (stopping after one email). Lumo builds cold email programs that land in the primary inbox, engage the right prospects, and generate meetings at scale.",
        "stat1_num": "91%", "stat1_lbl": "Of consumers check email daily — it's still the #1 channel",
        "stat2_num": "8",   "stat2_lbl": "Average touchpoints needed before a cold prospect responds",
        "stat3_num": "40x", "stat3_lbl": "Higher ROI for email vs. social media for B2B acquisition",
        "why_h2": "Why Most Cold Email Programs Fail (And How Lumo Fixes It)",
        "why_p1": "The first failure mode is deliverability. Most companies send cold email from their primary domain at high volume — triggering spam filters and damaging domain reputation. The result: emails landing in spam folders that prospects never see. Proper cold email infrastructure uses dedicated sending domains, warmed-up mailboxes, and technical configuration (SPF, DKIM, DMARC) that maintains inbox placement regardless of volume.",
        "why_p2": "The second failure mode is relevance. Generic cold emails — 'Hi [First Name], I saw you work at [Company] and wanted to reach out' — achieve reply rates below 1% because they offer no reason to respond. Effective cold email demonstrates specific research: a relevant trigger (recent funding, new hire, product launch), a pain point specific to the prospect's role, and a value proposition that maps directly to their context.",
        "why_p3": "Lumo manages the full cold email stack: technical deliverability infrastructure, ICP-driven prospect research, highly personalised sequence writing, A/B testing of subject lines and opening lines, and reply management. We optimise for reply rate and meeting booking rate — the metrics that connect email activity to pipeline — not vanity metrics like email opens, which are increasingly unreliable due to iOS privacy protections.",
        "services_h2": "Our Cold Email Outreach Services",
        "services": [
            ("🔧", "Deliverability Infrastructure", "Dedicated sending domain setup, DNS configuration (SPF, DKIM, DMARC), mailbox warmup, sending platform configuration (Instantly, Smartlead, Lemlist), and ongoing deliverability monitoring — ensuring consistent inbox placement."),
            ("🔍", "Prospect Research & List Building", "ICP-based prospect identification, contact data sourcing, email verification, personalisation data enrichment (LinkedIn, company news, role context), and list segmentation by persona and messaging approach."),
            ("✍️", "Sequence Writing & Testing", "Personalised cold email sequence copy — subject line variants, opening line personalisation, value proposition, social proof, and CTA — with A/B testing of key variables and iteration based on reply rate data."),
            ("📬", "Reply Management & Booking", "Inbox monitoring, reply categorisation (interested/not interested/bounce/wrong contact), personalised follow-up to positive replies, and meeting scheduling — ensuring no warm reply is missed or left without a timely response."),
            ("📊", "Performance Analytics", "Send volume, delivery rate, open rate, reply rate, and meeting booking rate tracking by sequence, persona, and message variant — with weekly reporting and monthly sequence optimisation based on performance data."),
            ("🔄", "Ongoing Campaign Management", "Continuous prospect list refresh, sequence refresh every 60–90 days to prevent template fatigue, new persona testing, and outreach expansion as proven sequences are scaled across broader prospect universes."),
        ],
        "process": [
            ("🏗️", "Infrastructure Setup", "Domain acquisition, DNS configuration, mailbox creation and warmup (3–4 weeks), sending platform configuration, and deliverability testing — achieving healthy sender reputation before any prospecting begins."),
            ("📋", "Research & Copy", "Prospect list build, personalisation data enrichment, sequence copy drafting with variants, and pre-send review — all completed before the first email is sent."),
            ("🚀", "Launch & Iterate", "Controlled send volume ramp, reply monitoring from day one, weekly A/B test analysis, rapid iteration on underperforming subject lines and opening lines, and reply handoff to sales or meeting booking."),
            ("📈", "Scale & Expand", "Increase volume on proven sequences, add new prospect segments, develop new sequence variants for different personas, and quarterly copy refresh to maintain reply rates as templates age."),
        ],
        "price_from": "$1,500",
        "price_note": "per month — includes infrastructure, research, sequence management, and reply handling",
        "faqs": [
            ("Is cold email legal?", "Yes — cold email to business contacts is legal in the US under CAN-SPAM (which applies to commercial email) when you include a physical address, an unsubscribe mechanism, and accurate sender information. GDPR applies to EU prospects; CASL applies to Canadian prospects — both have stricter consent requirements. Lumo configures cold email programs to comply with all applicable regulations and removes unsubscribe requests immediately. Never send cold email to consumer Gmail, Yahoo, or personal email addresses."),
            ("What reply rate should I expect from cold email?", "Industry benchmarks: a poorly run cold email program achieves 0.5–2% reply rate. A well-run program with personalisation and good deliverability achieves 3–8% reply rate. Best-in-class programs with highly personalised, trigger-based opening lines achieve 8–15% reply rate. Lumo targets 3–8% reply rate in the first 90 days, with improvement toward 8–12% as sequence data matures and we understand which personas and messages perform best."),
            ("How long does it take to set up cold email infrastructure?", "Domain registration and DNS configuration: 1–2 days. Mailbox warmup: 3–4 weeks (non-negotiable — skipping warmup causes immediate deliverability damage). Prospect list build and copy development: 1–2 weeks in parallel with warmup. First emails send in week 4–5 from kickoff. Lumo begins infrastructure setup and research simultaneously so the program is ready to launch as soon as mailboxes are warmed."),
            ("Why shouldn't I use my primary domain for cold email?", "Cold email sent at volume from your primary domain (yourcompany.com) risks damaging your primary domain's sender reputation if spam complaints occur. This can cause your transactional emails (receipts, onboarding, support) and marketing emails to start landing in spam — a serious business problem. Lumo uses dedicated cold email sending domains (youcompany-outreach.com, meetyourcompany.com) that are isolated from your primary domain's reputation."),
            ("How many emails per day can be sent safely?", "Per mailbox, safe sending volume is 30–50 emails per day — above this threshold, deliverability begins degrading. To scale volume, Lumo uses multiple warmed-up mailboxes across multiple sending domains, distributing volume across the infrastructure. A program using 5 mailboxes across 2 domains can safely send 150–250 emails per day while maintaining inbox placement."),
        ],
        "cta_h2": "Ready for Cold Email That Actually Lands and Gets Replies?",
        "cta_sub": "Get a free cold email audit — we'll test your current deliverability, review your sequence copy, and show you exactly what's preventing your emails from generating the reply rates your business needs.",
        "schema_service_name": "Cold Email Outreach Services",
        "schema_service_desc": "Cold email outreach for US B2B companies — deliverability infrastructure, prospect research, personalised sequence writing, and reply management for pipeline generation.",
    },

    "affiliate-marketing": {
        "title_tag":  "Affiliate Marketing Agency | Affiliate Program Management | Lumo AI",
        "meta_desc":  "Affiliate marketing services from Lumo AI Agency. Affiliate program setup, publisher recruitment, commission management, and fraud prevention for US e-commerce and SaaS brands. Free audit.",
        "canonical":  "https://lumoaiagency.com/services/affiliate-marketing",
        "og_title":   "Affiliate Marketing Agency | Lumo AI Agency",
        "og_desc":    "Pay only for results. Lumo builds and manages affiliate programs that recruit high-quality publishers, set performance-based commissions, and drive incremental revenue for US brands.",
        "h1_html":    "Affiliate Marketing That Pays <span class=\"hl-lime\">Only for Results</span>, Never for Reach",
        "badge":      "Affiliate Program Specialists",
        "lead":       "Affiliate marketing is the only digital channel where you pay exclusively for results — commissions on sales, leads, or conversions that your affiliate partners generate. Lumo builds and manages affiliate programs that recruit high-quality publishers, set competitive commission structures, and drive incremental revenue that your direct channels can't reach alone.",
        "stat1_num": "16%",  "stat1_lbl": "Of all US e-commerce orders are influenced by affiliate marketing",
        "stat2_num": "$17B", "stat2_lbl": "US affiliate marketing spend in 2024",
        "stat3_num": "12:1", "stat3_lbl": "Average ROI for managed affiliate programs",
        "why_h2": "Why Affiliate Marketing Is the Most Capital-Efficient Revenue Channel",
        "why_p1": "Every other digital marketing channel requires upfront spend regardless of results — Google Ads charges for clicks whether they convert or not, influencer campaigns charge flat fees whether they drive sales or not. Affiliate marketing inverts this model: you define the conversion event and the commission, and you only pay when that event occurs. This performance-based structure makes affiliate marketing uniquely capital-efficient, particularly for cash-flow-conscious businesses.",
        "why_p2": "The reach advantage is equally compelling. A well-managed affiliate program taps into publisher audiences that your direct marketing can't access — niche blogs, comparison sites, deal communities, email newsletters, and coupon platforms with established trust relationships with their readers. These publishers are motivated to promote you effectively because their income depends on your conversions. The aligned incentive structure is powerful.",
        "why_p3": "The challenge is program management. Unmanaged affiliate programs attract low-quality publishers who drive discount traffic, generate fraudulent conversions, or violate brand guidelines — delivering volume that looks good in reports but doesn't represent incremental revenue. Lumo builds programs with publisher quality standards, fraud detection, and brand compliance monitoring that protect your program's integrity while scaling genuine incremental revenue.",
        "services_h2": "Our Affiliate Marketing Services",
        "services": [
            ("🔧", "Affiliate Program Setup", "Affiliate network selection (ShareASale, CJ, Impact, Rakuten, or in-house), commission structure design, tracking implementation, creative asset library, and programme terms and brand guidelines — the infrastructure for a scalable affiliate program."),
            ("🤝", "Publisher Recruitment", "Targeted affiliate recruitment — identifying and onboarding publishers in your category (content sites, review sites, comparison engines, deal communities, email newsletters) with audiences that match your buyer profile."),
            ("⚙️", "Program Management", "Ongoing affiliate relationship management — commission payments, publisher communication, promotional calendar coordination, performance review, top-partner incentive programs, and underperformer management."),
            ("🛡️", "Fraud Prevention & Compliance", "Transaction-level fraud monitoring, coupon code misuse detection, brand compliance auditing, trademark bidding enforcement, and publisher policy violation management — protecting program integrity and incremental revenue quality."),
            ("📊", "Performance Analytics", "Publisher performance reporting, revenue attribution by partner type and traffic source, incrementality analysis (identifying genuinely new revenue vs. last-click cannibalization), and monthly program health reporting."),
            ("🚀", "Program Growth Strategy", "Tiered commission strategies, seasonal promotion planning, affiliate recruitment campaigns, content publisher development, and expansion into new affiliate verticals as the program matures."),
        ],
        "process": [
            ("🏗️", "Program Architecture", "Commission structure design, network selection, tracking setup, creative development, and publisher guidelines — building the foundation before any affiliate is recruited."),
            ("🤝", "Recruitment & Onboarding", "Publisher identification and outreach, application review, quality screening, onboarding, and initial promotional period support — building a quality publisher base in the first 60–90 days."),
            ("🔄", "Manage & Optimise", "Monthly publisher performance reviews, top-partner relationship development, underperformer communication, fraud monitoring, commission optimisation, and seasonal promotion planning."),
            ("📈", "Scale & Expand", "Expand into new publisher categories, develop tiered commission incentives for top performers, test new network placements, and incrementality analysis to identify genuine revenue contribution."),
        ],
        "price_from": "$1,500",
        "price_note": "per month management fee — affiliate network fees and publisher commissions are separate",
        "faqs": [
            ("Which affiliate networks does Lumo work with?", "Lumo manages programs on ShareASale, CJ Affiliate (Commission Junction), Impact, Rakuten Advertising, AvantLink, and FlexOffers — selecting the network based on your category, target publisher types, and existing publisher relationships. For SaaS companies, we also manage in-house affiliate programs built on PartnerStack or FirstPromoter. Network selection is a strategic decision made in the program architecture phase based on where your best publisher fits are."),
            ("What commission rate should I offer affiliates?", "Commission rates vary significantly by category: e-commerce products typically 5–15% of sale value; SaaS subscriptions typically 20–30% of first payment or 10–15% recurring; lead generation typically $20–$100 per lead depending on lead value. Competitiveness is the key variable — your commission needs to be attractive enough to motivate publishers to promote you over comparable programs. Lumo conducts competitive commission analysis as part of program architecture."),
            ("How do you prevent affiliate fraud?", "Affiliate fraud prevention includes: transaction-level monitoring for pattern anomalies (velocity spikes, unusual geographic clustering), coupon code misuse detection (ensuring your codes aren't posted on deal sites violating terms), return rate monitoring by affiliate (high returns can indicate fraudulent transaction generation), brand trademark bidding enforcement (preventing affiliates from bidding on your branded keywords), and publisher quality requirements during onboarding. Lumo uses both automated monitoring and manual review for high-volume affiliates."),
            ("Is affiliate marketing appropriate for SaaS companies?", "Yes — SaaS affiliate programs are highly effective when structured around recurring revenue. The typical SaaS affiliate commission model is either a one-time payment (100–200% of first month's subscription) or a recurring commission (10–30% of monthly payments for the life of the customer). Recurring commissions are particularly motivating for publishers with content audiences — the program pays them indefinitely for referred customers who retain. PartnerStack and FirstPromoter are the preferred platforms for SaaS affiliate programs."),
            ("How long does it take to see meaningful affiliate revenue?", "Affiliate program revenue builds over time as publisher count grows and existing publishers develop promotional content. A new program typically generates its first conversions in weeks from top publishers who promote immediately. Meaningful revenue (covering program management costs) typically appears at 3–6 months. Programs reach full performance at 12–18 months as content publishers' SEO-ranked content matures, comparison sites index the program, and top publishers develop annual promotional relationships."),
        ],
        "cta_h2": "Ready to Build a Revenue Channel That Only Costs You When It Converts?",
        "cta_sub": "Get a free affiliate program audit — we'll assess your current commission structure, publisher quality, and program health, then show you the incremental revenue opportunity in a well-managed affiliate program.",
        "schema_service_name": "Affiliate Marketing Program Management",
        "schema_service_desc": "Affiliate marketing program management for US brands — program setup, publisher recruitment, commission management, fraud prevention, and incremental revenue growth.",
    },

    "white-label-marketing": {
        "title_tag":  "White-Label Marketing Agency | Agency Reseller Services | Lumo AI",
        "meta_desc":  "White-label marketing services from Lumo AI Agency. SEO, paid media, content, and web development delivered under your brand. Scalable agency fulfilment with no client visibility into Lumo. Free consultation.",
        "canonical":  "https://lumoaiagency.com/services/white-label-marketing",
        "og_title":   "White-Label Marketing Agency | Lumo AI Agency",
        "og_desc":    "Deliver expert SEO, paid media, and content under your brand without hiring. Lumo's white-label fulfilment lets agencies scale services without headcount — all invisible to your clients.",
        "h1_html":    "White-Label Marketing <span class=\"hl-lime\">You Can Sell</span> Under Your Own Brand",
        "badge":      "White-Label Agency Partner",
        "lead":       "Agencies can't be experts at everything — but clients expect you to be. Lumo's white-label fulfilment delivers SEO, paid media, content, and web development services branded as your agency's own work. Your clients see your team. We handle the execution. You focus on growth and client relationships.",
        "stat1_num": "72%",  "stat1_lbl": "Of digital agencies use some form of white-label fulfilment",
        "stat2_num": "40%",  "stat2_lbl": "Average margin improvement for agencies using white-label",
        "stat3_num": "3x",   "stat3_lbl": "Faster service expansion with white-label vs. hiring",
        "why_h2": "Why Smart Agencies Use White-Label Fulfilment to Scale",
        "why_p1": "Hiring full-time specialists for every service you want to offer is expensive, slow, and risky — you need the revenue before you can justify the hire, but you need the hire to win the revenue. White-label fulfilment solves this bootstrapping problem: sell the service, fulfil it through Lumo at a margin, and use the cash flow to hire when volume justifies it. You expand service offerings without expanding payroll.",
        "why_p2": "Specialist quality is the second advantage. SEO, paid media, programmatic advertising, and technical web development require deep expertise that generalist agencies struggle to maintain across multiple disciplines simultaneously. Lumo's specialists focus on their craft full-time — the quality of work delivered under your brand exceeds what most agencies could produce in-house at equivalent cost, because we're not spreading specialists thin across unrelated service lines.",
        "why_p3": "Client relationship control remains entirely yours. Lumo operates completely behind the scenes — all deliverables are branded as your work, all communications go through you, and your clients have no visibility into the fulfilment relationship. Lumo signs NDAs as standard. You maintain the relationship, control the narrative, and build your agency's reputation on the work we deliver.",
        "services_h2": "Our White-Label Service Capabilities",
        "services": [
            ("🔍", "White-Label SEO", "Full SEO fulfilment under your brand — technical audits, on-page optimisation, content strategy, link building, and monthly reporting formatted to your agency's templates and delivered as your work product."),
            ("💰", "White-Label Paid Media", "Google Ads, Meta Ads, LinkedIn, and programmatic campaign management — strategy, campaign builds, ongoing optimisation, and reporting delivered as your agency's paid media service, invisible to clients."),
            ("📝", "White-Label Content Marketing", "Blog content, landing page copy, email sequences, and content strategy — written in your clients' brand voice, delivered to your editorial standards, and published through your workflow with no Lumo attribution."),
            ("🌐", "White-Label Web Development", "WordPress, Shopify, and custom website development delivered under your brand — from design to development to launch — with full project management and client communication routed through your team."),
            ("🤝", "Agency Partner Support", "Dedicated partner manager, white-label reporting templates, pitch deck support for new business, SLA-backed delivery timelines, and NDA-protected relationship — everything your agency needs for seamless client integration."),
            ("📊", "White-Label Reporting", "Client-facing report templates in your agency's branding — monthly performance reports, campaign dashboards, and executive summaries formatted to match your existing deliverable standards with no Lumo branding."),
        ],
        "process": [
            ("🤝", "Partner Onboarding", "Agency introduction, service scope agreement, NDA signing, reporting template setup, communication protocol definition, and client brief format alignment — establishing the fulfilment relationship before any client work begins."),
            ("📋", "Client Brief Intake", "Structured client brief intake through your agency — goals, budget, current performance, brand guidelines, and KPIs — which Lumo uses to build strategy and execution plans delivered back to you for client approval."),
            ("⚙️", "Fulfilment & Delivery", "Lumo executes the service, delivers all work product branded as your agency's output, and routes all communication through your team — maintaining complete client invisibility of the fulfilment relationship."),
            ("📊", "Report & Retain", "Monthly reporting in your branded templates, ongoing optimisation, and expansion recommendations delivered to you for relay to clients — supporting your client retention and upsell conversations with expert performance data."),
        ],
        "price_from": "$800",
        "price_note": "per client per month — pricing varies by service type and scope; volume discounts for 5+ clients",
        "faqs": [
            ("Will my clients know Lumo is involved?", "No — Lumo operates completely behind the scenes under NDA. All work is delivered under your agency's brand. Deliverables are formatted to your templates, communications come from your team, and Lumo's name never appears in any client-facing material. We're invisible by design."),
            ("What services can Lumo white-label?", "Lumo white-labels: SEO (technical, local, content, link building), paid media (Google Ads, Meta, LinkedIn, programmatic), content marketing (blog, landing pages, email), web development (WordPress, Shopify, custom), and reporting. Services are fulfilled by the same specialists who deliver Lumo's named services — your clients receive the same quality work."),
            ("How does billing work for white-label clients?", "Lumo bills your agency directly at wholesale rates — you bill your clients at whatever margin you choose. Lumo has no visibility into what you charge your clients. Typical agency margins on white-label fulfilment range from 30–60% above Lumo's wholesale pricing. We invoice monthly with 30-day payment terms."),
            ("What's the minimum commitment for white-label partnership?", "Lumo requires a 3-month minimum engagement per client to ensure quality service delivery — most SEO and paid media services require at least 90 days to demonstrate measurable results. There's no minimum number of clients — agencies can start with a single white-label client and scale from there. Volume pricing applies from 5+ simultaneous white-label clients."),
            ("How do you handle communication between Lumo and the end client?", "All client communication is routed through your agency. Your account manager or client success team relays briefs, approvals, and feedback to Lumo's fulfilment team. Lumo never contacts your clients directly. In practice, most agencies establish a structured weekly or bi-weekly check-in between the agency account manager and Lumo's fulfilment lead — keeping all parties aligned without client exposure."),
        ],
        "cta_h2": "Ready to Deliver Expert Services Under Your Brand Without Expanding Your Team?",
        "cta_sub": "Get a free white-label consultation — we'll walk through our service capabilities, pricing structure, and partnership model, and show you how agencies are using Lumo to scale revenue without scaling headcount.",
        "schema_service_name": "White-Label Marketing Services",
        "schema_service_desc": "White-label marketing fulfilment for US digital agencies — SEO, paid media, content, and web development delivered under your brand with complete client invisibility.",
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
        <li>AI-powered insights on every engagement</li>
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
          <li><a href="../services/lead-generation.html">Lead Generation</a></li>
          <li><a href="../services/account-based-marketing.html">ABM</a></li>
          <li><a href="../services/outbound-sales.html">Outbound Sales</a></li>
          <li><a href="../services/cold-email-outreach.html">Cold Email</a></li>
          <li><a href="../services/affiliate-marketing.html">Affiliate Marketing</a></li>
          <li><a href="../services/white-label-marketing.html">White-Label</a></li>
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
