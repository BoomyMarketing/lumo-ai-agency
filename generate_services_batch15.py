"""Batch 15 — Backlog Batch 10: amazon-store-management, amazon-fba, shopify-seo, woocommerce-marketing, shopping-feed-management"""
import json, os

SERVICES = {
    "amazon-store-management": {
        "title": "Amazon Store Management",
        "tagline": "End-to-end Amazon marketplace management — from listing to Buy Box to profit",
        "desc": "Amazon is the most competitive retail environment on earth — and most brands are leaving significant revenue on the table. We manage every aspect of your Amazon presence: listing optimization, A+ content, advertising, Buy Box strategy, inventory coordination, and performance monitoring — turning your Amazon channel into a reliable revenue engine.",
        "price": "$2,500/mo",
        "stat1": "$500B+",
        "stat1_label": "in annual Amazon marketplace sales",
        "stat2": "83%",
        "stat2_label": "of product searches now start on Amazon",
        "stat3": "Buy Box",
        "stat3_label": "wins drive 82% of all Amazon sales volume",
        "deliverables": [
            ("📝", "Listing Optimization", "Full listing optimization: keyword-rich titles (within Amazon's character limits), bullet points that sell, backend search terms, and descriptions — all researched with Helium 10 or Jungle Scout for maximum organic ranking."),
            ("🎨", "A+ Content & Brand Store", "Premium A+ Content (EBC) for all ASINs: comparison modules, lifestyle imagery, brand story sections, and feature callouts — increasing conversion rate by 3–10% on average. Brand Store design and optimization."),
            ("📦", "Inventory & Fulfillment Coordination", "Inventory planning and FBA replenishment alerts: monitoring stock levels, forecasting demand, and coordinating shipments to Amazon warehouses — preventing costly stockouts and excess inventory fees."),
            ("📣", "Amazon PPC Management", "Sponsored Products, Sponsored Brands, and Sponsored Display campaigns fully managed: keyword harvesting, negative keyword sculpting, bid optimization, and campaign structure designed for profitability."),
            ("🏆", "Buy Box Strategy", "Buy Box eligibility monitoring and optimization: pricing strategy, fulfillment method recommendations, seller metrics management, and competitive repricing guidance."),
            ("⭐", "Review Management & Velocity", "Compliant review acquisition strategy: follow-up sequences via Amazon's native tools, Vine enrollment for new products, and review monitoring with alert protocols for negative review response."),
            ("📊", "Performance Reporting", "Monthly reporting: organic rankings, PPC ACOS/TACOS, Buy Box percentage, conversion rate, and revenue by ASIN — with actionable recommendations for each metric."),
        ],
        "process": [
            ("🔍", "Account Audit", "Full audit of your Seller Central account: listing quality scores, PPC campaign structure, inventory health, Buy Box percentage, and review velocity — with a prioritized improvement plan."),
            ("📝", "Optimize & Build", "Listings fully optimized, A+ Content created, Brand Store built, PPC campaigns restructured. Review strategy activated. All changes documented."),
            ("📣", "Advertise & Scale", "PPC campaigns launched and managed. Organic rank tracked weekly. Buy Box percentage monitored. Inventory alerts configured."),
            ("📈", "Report & Iterate", "Monthly performance review: PPC optimization, listing refresh for seasonal keywords, inventory planning, and competitive landscape adjustments."),
        ],
        "faqs": [
            ("Do you work with Vendor Central or Seller Central?", "We primarily work with Seller Central (3P marketplace). Vendor Central (1P direct) management is available for brands with existing Vendor Central relationships."),
            ("Do you manage the advertising budget?", "Yes — we manage your Amazon PPC budget within the parameters you set. We provide weekly spend reporting and recommendations for budget allocation across campaign types."),
            ("Can you help us launch a new product on Amazon?", "Yes — product launch is a specific service we offer: pre-launch keyword research, listing build, launch PPC strategy, Vine enrollment, and initial review velocity optimization."),
            ("What categories do you specialize in?", "We work across most Amazon categories: home & kitchen, health & personal care, beauty, sports & outdoors, electronics accessories, pet supplies, and consumer goods. We assess fit during discovery."),
            ("How do you handle account health issues or suspensions?", "Account health monitoring is included in our management service. If account health drops, we address root cause immediately. For suspensions, we draft Plan of Action (POA) appeals and manage the reinstatement process."),
        ],
        "schema_service_desc": "Amazon store management — listing optimization, A+ content, PPC management, Buy Box strategy, inventory coordination, review management, and monthly reporting.",
    },
    "amazon-fba": {
        "title": "Amazon FBA Management",
        "tagline": "FBA operations, inventory strategy, and profitability optimization for Amazon sellers",
        "desc": "Fulfillment by Amazon gives you access to Prime shipping and Amazon's logistics network — but FBA profitability requires careful operational management. We handle the operational complexity of FBA: inventory planning, shipment creation, fee optimization, stranded inventory resolution, and profitability analysis — so you can focus on growing your brand.",
        "price": "$2,000/mo",
        "stat1": "73%",
        "stat1_label": "of Amazon third-party sellers use FBA",
        "stat2": "35%",
        "stat2_label": "average increase in sales velocity with Prime badge",
        "stat3": "$15B",
        "stat3_label": "paid annually by sellers in unnecessary FBA fees",
        "deliverables": [
            ("📦", "FBA Inventory Planning", "Demand forecasting and reorder point calculation for every ASIN: historical velocity analysis, seasonality adjustments, and lead time modeling — preventing stockouts and minimizing excess inventory storage fees."),
            ("🚚", "Shipment Creation & Management", "FBA shipment plan creation, box content uploads, carrier selection, and tracking management — ensuring shipments check in at Amazon warehouses correctly and on schedule."),
            ("💰", "FBA Fee Optimization", "FBA fee analysis by ASIN: identifying products with unfavorable fee-to-revenue ratios, recommending packaging dimension changes, and flagging candidates for FBM hybrid fulfillment."),
            ("🔍", "Stranded Inventory Management", "Weekly monitoring and resolution of stranded inventory — listings errors, ASIN issues, and suppressed listings that cause FBA inventory to sit unsold, accruing storage fees."),
            ("📊", "Profitability Analysis", "ASIN-level P&L: COGS, FBA fees, referral fees, PPC spend, and storage costs — giving you true net margin per unit to make informed pricing and sourcing decisions."),
            ("⚠️", "Reimbursement Claims", "Systematic FBA reimbursement claim filing for lost or damaged inventory, incorrect fee charges, and customer return discrepancies — recovering money Amazon owes you."),
            ("🔄", "Removal & Liquidation", "Excess inventory removal order management and liquidation strategy — balancing storage fee avoidance against liquidation recovery value."),
        ],
        "process": [
            ("🔍", "FBA Health Audit", "Full FBA account audit: fee analysis, inventory velocity, stranded inventory, reimbursement opportunities, and storage fee exposure — with a prioritized action plan."),
            ("⚙️", "Systems Setup", "Inventory tracking system configured, reorder point calculations established, shipment workflow documented, and reimbursement monitoring activated."),
            ("📦", "Ongoing Operations", "Weekly inventory monitoring, shipment creation, stranded inventory resolution, and reimbursement claim filing. Monthly profitability reporting by ASIN."),
            ("📈", "Optimize & Scale", "Quarterly fee structure review, packaging optimization recommendations, and sourcing guidance based on profitability data. Scaling recommendations for high-performing ASINs."),
        ],
        "faqs": [
            ("What's the difference between FBA management and Amazon Store Management?", "FBA Management focuses on the operational and financial side: inventory, logistics, fees, and profitability. Amazon Store Management covers listing optimization, advertising, and content. Many clients use both services together."),
            ("How much can we recover in FBA reimbursements?", "Most sellers have unclaimed reimbursements averaging 1–3% of annual FBA revenue. We audit 18 months of history and file all eligible claims systematically."),
            ("Do you handle international FBA (Canada, Europe)?", "Yes — we manage FBA operations for Amazon US, Canada, and European marketplaces. Each marketplace has different fee structures and logistics requirements we handle separately."),
            ("Can you help us decide which products to add to FBA?", "Yes — we calculate FBA profitability projections for new products before you commit to inventory, helping you make data-driven sourcing decisions."),
            ("What software do you use for inventory management?", "We use Inventory Lab, Sellerboard, or Jungle Scout Supply Chain depending on client preference and business scale. We can work within your existing toolset."),
        ],
        "schema_service_desc": "Amazon FBA management — inventory planning, shipment management, fee optimization, stranded inventory, profitability analysis, and reimbursement claims.",
    },
    "shopify-seo": {
        "title": "Shopify SEO",
        "tagline": "Technical and content SEO for Shopify stores — rank, convert, and scale",
        "desc": "Shopify SEO has unique technical challenges that generic SEO agencies miss — duplicate content from faceted navigation, canonical tag issues, bloated theme code, and structured data gaps. We fix the technical foundation and build the content and authority strategy that drives sustainable organic growth for your Shopify store.",
        "price": "$2,500/mo",
        "stat1": "43%",
        "stat1_label": "of e-commerce traffic comes from organic search",
        "stat2": "700%",
        "stat2_label": "higher ROI for organic vs. paid traffic over 12 months",
        "stat3": "15%",
        "stat3_label": "average Shopify stores lose traffic to duplicate content issues",
        "deliverables": [
            ("⚙️", "Shopify Technical SEO", "Full Shopify technical audit and remediation: canonical tag fixes, duplicate content from /collections/ and /products/ URLs, theme code optimization, image compression, pagination handling, and crawl budget management."),
            ("🔍", "Keyword Research & Architecture", "E-commerce keyword research: commercial intent keywords mapped to product and collection pages, informational keywords for blog content, and long-tail opportunities — with a URL structure plan aligned to Shopify's architecture."),
            ("📝", "Product & Collection Page Optimization", "On-page optimization for every priority product and collection page: unique titles, meta descriptions, heading hierarchy, schema markup (Product, Review, BreadcrumbList), and internal linking."),
            ("🏗️", "Schema Markup Implementation", "Full structured data implementation for e-commerce: Product schema with price, availability, and ratings, Organization schema, BreadcrumbList, and FAQ schema — via Shopify's JSON-LD or a structured data app."),
            ("📖", "Content Marketing for SEO", "Blog content strategy and production: buying guides, comparison articles, how-to content, and category-supporting articles — building topical authority for your product categories."),
            ("🔗", "Link Building", "E-commerce specific link building: product PR outreach, digital PR campaigns, supplier/partner links, and niche directory submissions — building domain authority in your product vertical."),
            ("📊", "Performance Reporting", "Monthly SEO reporting: organic traffic, keyword rankings by product/collection, conversion rate from organic, and revenue attributed to SEO — with actionable next steps."),
        ],
        "process": [
            ("🔍", "Shopify SEO Audit", "Comprehensive Shopify-specific SEO audit: technical issues, content gaps, keyword opportunities, and competitive analysis. Priority action list with estimated traffic impact."),
            ("⚙️", "Technical Remediation", "Technical fixes implemented: canonical tags, duplicate content, schema markup, page speed, and crawlability issues resolved. Changes documented and validated in Google Search Console."),
            ("📝", "Content & Optimization", "Product and collection pages optimized. Blog content strategy launched. Internal linking structure built. Schema markup verified."),
            ("📈", "Authority & Scale", "Link building campaigns activated. Keyword rankings tracked weekly. Content calendar executed. Monthly strategy review and roadmap adjustment."),
        ],
        "faqs": [
            ("What Shopify-specific SEO issues do you fix first?", "The most common high-impact issues are: duplicate content from /collections/ + /products/ URL variants, missing or incorrect canonical tags, unoptimized collection pages, and missing Product schema. We fix these in the first 30 days."),
            ("Can you work with our existing Shopify theme?", "Yes — we work within your existing theme via Shopify's theme editor, Liquid template edits, and JSON-LD script injection. We don't require a theme change unless the current theme has severe technical limitations."),
            ("How long until Shopify SEO shows results?", "Technical fixes show results within 4–8 weeks as Google recrawls. Content and authority building compounds over 6–12 months. E-commerce SEO is a long-term investment with exponential returns."),
            ("Do you handle SEO for Shopify apps?", "We optimize your site's SEO including how app-generated content (reviews, bundles, filters) impacts crawlability and indexation. We recommend and configure SEO-friendly settings for your existing apps."),
            ("Can you migrate us from another platform to Shopify without losing SEO?", "Yes — platform migrations are a specialized service. We manage the full redirect mapping, URL canonicalization, and Search Console migration to preserve organic rankings through the transition."),
        ],
        "schema_service_desc": "Shopify SEO — technical audit, duplicate content fixes, product page optimization, schema markup, content strategy, link building, and performance reporting.",
    },
    "woocommerce-marketing": {
        "title": "WooCommerce Marketing",
        "tagline": "Full-stack digital marketing for WooCommerce stores — SEO, ads, and email",
        "desc": "WooCommerce gives you maximum flexibility — but that flexibility means your marketing requires more custom configuration than any-other platform. We provide full-stack digital marketing for WooCommerce stores: technical SEO, Google Shopping, Meta Ads, email automation, and conversion rate optimization — all configured for WordPress and WooCommerce's unique environment.",
        "price": "$2,500/mo",
        "stat1": "28%",
        "stat1_label": "of all online stores run on WooCommerce",
        "stat2": "4.4%",
        "stat2_label": "average e-commerce conversion rate — we target 5%+",
        "stat3": "$4.20",
        "stat3_label": "average ROI for every $1 spent on email marketing",
        "deliverables": [
            ("⚙️", "WooCommerce Technical SEO", "WordPress/WooCommerce SEO via Yoast or Rank Math: product page optimization, category hierarchy, schema markup, page speed optimization (Core Web Vitals), and crawlability configuration."),
            ("🛒", "Google Shopping & Performance Max", "Product feed creation and optimization via Google Merchant Center, Shopping campaign management, and Performance Max campaigns — with feed-level optimization for title, description, and product type attributes."),
            ("📣", "Meta Ads for E-commerce", "Meta catalog sales campaigns, dynamic product ads (DPA), prospecting and retargeting campaigns — connected to your WooCommerce product catalog via Meta pixel and Conversions API."),
            ("📧", "Email Marketing Automation", "WooCommerce email automation via Klaviyo or Mailchimp: abandoned cart sequences, post-purchase flows, win-back campaigns, and browse abandonment — the highest-ROI e-commerce email flows."),
            ("🔄", "Cart Abandonment Recovery", "Multi-channel cart abandonment recovery: email sequence, retargeting ads, and SMS (optional) — systematically recovering 10–15% of abandoned carts."),
            ("📊", "WooCommerce Analytics", "GA4 e-commerce tracking for WooCommerce: purchase events, checkout funnel analysis, product performance reporting, and revenue attribution across channels."),
            ("🎯", "CRO & Landing Page Optimization", "Conversion rate optimization for product pages, category pages, and checkout: A/B testing, social proof integration, urgency elements, and checkout friction reduction."),
        ],
        "process": [
            ("🔍", "Audit & Strategy", "WooCommerce store audit: technical SEO, analytics tracking, ad account setup, and email automation gaps. Full-stack marketing strategy developed."),
            ("⚙️", "Foundation Build", "Technical SEO fixes, GA4 e-commerce tracking, product feed setup, ad campaigns built, and email automations configured. All tested before going live."),
            ("📣", "Launch & Optimize", "Campaigns launched, email flows activated, and SEO content publishing begins. Weekly monitoring across all channels from launch."),
            ("📈", "Scale & Report", "Monthly cross-channel reporting: organic traffic, ROAS, email revenue, and conversion rate. Budget shifted to highest-performing channels. Winning strategies scaled."),
        ],
        "faqs": [
            ("What plugins do you use for WooCommerce SEO?", "We work with Yoast SEO (most common) or Rank Math — configuring product schema, breadcrumbs, XML sitemaps, and all technical SEO settings. We recommend the plugin based on your existing setup."),
            ("Do you manage Google Merchant Center for us?", "Yes — Merchant Center setup, product feed management, feed optimization, and disapproval resolution are all included in our WooCommerce marketing service."),
            ("Can you integrate with our existing email platform?", "Yes — we integrate with Klaviyo, Mailchimp, ActiveCampaign, and most major email platforms. If you don't have one, we recommend Klaviyo for e-commerce and handle the full setup."),
            ("How is WooCommerce marketing different from Shopify marketing?", "WooCommerce runs on WordPress, giving more technical flexibility but requiring more custom configuration for tracking, feeds, and automation. The marketing strategy is similar — SEO, ads, email — but the technical implementation differs significantly."),
            ("Do you handle the WooCommerce hosting or site performance?", "We advise on hosting configuration and implement front-end performance optimizations (image compression, caching, lazy loading). Hosting migration or server management is outside our scope but we can recommend hosting partners."),
        ],
        "schema_service_desc": "WooCommerce marketing — technical SEO, Google Shopping, Meta Ads, email automation, cart abandonment recovery, analytics, and conversion rate optimization.",
    },
    "shopping-feed-management": {
        "title": "Shopping Feed Management",
        "tagline": "Optimized product feeds for Google Shopping, Meta, and marketplaces — more sales, lower CPC",
        "desc": "Your product feed is the foundation of your e-commerce advertising — if it's wrong, everything built on top of it underperforms. We audit, optimize, and continuously manage your product feeds across Google Shopping, Meta Catalog, Microsoft Shopping, and other channels — improving product visibility, click quality, and ROAS at the feed level.",
        "price": "$1,500/mo",
        "stat1": "85%",
        "stat1_label": "of shopping ad performance is driven by feed quality",
        "stat2": "30%",
        "stat2_label": "average CPC reduction with properly optimized product titles",
        "stat3": "2.4x",
        "stat3_label": "higher ROAS for stores with optimized vs. default feeds",
        "deliverables": [
            ("🔍", "Feed Audit & Diagnosis", "Complete product feed audit: disapproved products, policy violations, missing required attributes, low-quality titles, incorrect categorization, and missing GTIN/MPN — with a prioritized fix list and impact estimate."),
            ("📝", "Product Title Optimization", "Feed-level title optimization using keyword research and Google Shopping best practices: product type first, key attributes (brand, model, size, color, material) in priority order — driving higher impression share for relevant searches."),
            ("🏷️", "Attribute Enhancement", "Missing attribute population: GTIN, MPN, brand, color, size, material, age group, gender — using your product data and supplemental feeds to complete every required and recommended attribute."),
            ("📂", "Custom Label Strategy", "Custom label implementation for segmentation in Shopping campaigns: margin tiers, inventory levels, seasonality, sale items, and bestseller status — enabling granular bid strategy by product segment."),
            ("🔗", "Multi-Channel Feed Distribution", "Feed setup and management across: Google Shopping, Meta (Facebook/Instagram) Catalog, Microsoft/Bing Shopping, Pinterest Shopping, and TikTok Shopping — one optimized feed, distributed everywhere."),
            ("🔄", "Feed Monitoring & Maintenance", "Daily monitoring for new disapprovals, feed processing errors, and attribute changes. Automated alerts for critical issues. Monthly feed performance review with optimization priorities."),
            ("⚙️", "Feed Technology Management", "Feed management via DataFeedWatch, GoDataFeed, or Feedonomics — including feed rules, supplemental feed setup, and scheduled refresh configuration."),
        ],
        "process": [
            ("🔍", "Feed Audit", "Complete audit of current feed health across all connected channels: disapprovals, attribute coverage, title quality, and categorization accuracy. Gap analysis with impact prioritization."),
            ("⚙️", "Optimize & Rebuild", "Feed rules configured to optimize titles, populate missing attributes, apply custom labels, and fix categorization. Supplemental feeds built for data enrichment."),
            ("📡", "Distribute & Verify", "Optimized feed submitted to all channels. Merchant Center processing monitored. Disapproval rate tracked to zero. Custom label segments verified in campaign structure."),
            ("🔄", "Monitor & Maintain", "Daily disapproval monitoring, monthly performance review, and seasonal feed updates (holiday titles, promotional attributes). Feed rules updated as catalog evolves."),
        ],
        "faqs": [
            ("What's the most common feed problem you find?", "Poor product titles — most default feeds use internal product names that don't match how shoppers search. Optimizing titles to include the search terms buyers actually use is consistently the highest-impact feed improvement."),
            ("Do we need special software for feed management?", "We implement and manage a feed management tool (DataFeedWatch, GoDataFeed, or Feedonomics) on your behalf. The cost of the tool is typically included in the management fee or billed separately depending on catalog size."),
            ("Can you fix all our Google Merchant Center disapprovals?", "Yes — disapproval resolution is a core deliverable. Common causes (price mismatches, missing GTINs, policy violations, image issues) are systematically addressed with feed rules and product data corrections."),
            ("How often is the feed updated?", "Feed refresh frequency depends on your catalog update frequency. We configure scheduled refreshes — typically 2–4 times daily for price and inventory accuracy, with full attribute refreshes weekly."),
            ("Do you manage the Shopping campaigns themselves?", "Feed management is the data layer beneath Shopping campaigns. We can manage the campaigns through our Google Ads service, or deliver an optimized feed to your existing campaign manager."),
        ],
        "schema_service_desc": "Shopping feed management — feed audit, title optimization, attribute enhancement, custom labels, multi-channel distribution, and ongoing monitoring.",
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
            <li><a href="../services/ecommerce-seo.html">E-commerce SEO</a></li>
            <li><a href="../services/google-ads.html">Google Ads</a></li>
            <li><a href="../services/amazon-store-management.html">Amazon Management</a></li>
            <li><a href="../services/amazon-fba.html">Amazon FBA</a></li>
            <li><a href="../services/shopify-seo.html">Shopify SEO</a></li>
            <li><a href="../services/woocommerce-marketing.html">WooCommerce Marketing</a></li>
            <li><a href="../services/shopping-feed-management.html">Shopping Feeds</a></li>
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
            <li><a href="../industries/ecommerce-marketing/">E-commerce</a></li>
            <li><a href="../industries/saas-marketing/">SaaS</a></li>
            <li><a href="../industries/seo-for-lawyers/">Law Firms</a></li>
            <li><a href="../industries/healthcare-seo/">Healthcare</a></li>
            <li><a href="../industries/home-services-seo/">Home Services</a></li>
            <li><a href="../industries/seo-for-dentists/">Dentists</a></li>
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
