#!/usr/bin/env python3
"""Wave 3 — Batch 4:
   wordpress-development, shopify-development, website-maintenance,
   copywriting, review-management
"""
import os, json

BASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "services")
os.makedirs(BASE, exist_ok=True)

SERVICES = {

    "wordpress-development": {
        "title_tag":  "WordPress Development Agency | Custom WP Sites & Plugins | Lumo AI",
        "meta_desc":  "WordPress development services from Lumo AI Agency. Custom themes, plugin development, WooCommerce, performance optimisation, and SEO-ready builds. Free site audit.",
        "canonical":  "https://lumoaiagency.com/services/wordpress-development",
        "og_title":   "WordPress Development Agency | Lumo AI Agency",
        "og_desc":    "Custom WordPress development built for speed, SEO, and conversions. Lumo builds WP sites, themes, and plugins with performance and growth baked in from the first line of code.",
        "h1_html":    "WordPress Development Built for <span class=\"hl-lime\">Speed, SEO</span> & Conversions",
        "badge":      "WordPress Development Specialists",
        "lead":       "WordPress powers 43% of the web — but most WP sites are slow, insecure, and technically broken for SEO. Lumo builds custom WordPress sites that are fast by default, structured for search visibility, and designed to convert visitors into customers from day one.",
        "stat1_num": "43%",  "stat1_lbl": "Of the entire web runs on WordPress",
        "stat2_num": "3s",   "stat2_lbl": "Load time that causes 53% of mobile users to abandon",
        "stat3_num": "200%", "stat3_lbl": "Faster load times achieved through Lumo WP optimisation",
        "why_h2": "Why Most WordPress Sites Underperform (And How Lumo Fixes It)",
        "why_p1": "Most WordPress sites are built by developers who prioritise visual appeal over technical performance. The result: heavy page builders, unoptimised images, too many plugins, and no consideration for Core Web Vitals. Google's ranking signals now include page experience metrics directly — a slow WordPress site is a site that won't rank, regardless of how good the content is.",
        "why_p2": "Security is the second failure mode. A default WordPress installation with an off-the-shelf theme and generic plugins is a target. Lumo implements hardened WordPress configurations, regular security scanning, and update management as part of every build — ensuring your site doesn't become a liability.",
        "why_p3": "Lumo approaches WordPress development as a marketing infrastructure project, not a web design project. Every build includes technical SEO foundations (schema, canonical tags, XML sitemaps, structured URL architecture), performance optimisation for Core Web Vitals, conversion-oriented design, and integration with your marketing stack — so the site generates revenue, not just traffic.",
        "services_h2": "Our WordPress Development Services",
        "services": [
            ("🎨", "Custom Theme Development", "Bespoke WordPress themes built from scratch — no page builders, no bloated frameworks. Hand-coded HTML, CSS, and PHP for maximum performance, SEO control, and design precision to your brand spec."),
            ("🔌", "Plugin Development", "Custom WordPress plugin development for functionality your business requires — booking systems, membership portals, custom post types, API integrations, and workflow automations that off-the-shelf plugins can't provide."),
            ("🛒", "WooCommerce Development", "WooCommerce store builds and customisation — product catalogue architecture, custom checkout flows, payment gateway integration, inventory management, and performance optimisation for e-commerce conversion rates."),
            ("⚡", "Speed & Performance Optimisation", "Core Web Vitals optimisation — image compression, lazy loading, server-side caching, CDN configuration, database optimisation, and code minification. We target sub-2s load times on mobile."),
            ("🔒", "Security Hardening & Maintenance", "WordPress security configuration — login protection, malware scanning, file integrity monitoring, plugin vetting, and regular updates. Monthly maintenance plans include update management and uptime monitoring."),
            ("🔄", "Migration & Redesign", "Migration from any CMS to WordPress, theme redesigns preserving SEO equity (301 redirects, sitemap submission, Search Console verification), and plugin replacements — with zero downtime transitions."),
        ],
        "process": [
            ("📋", "Discovery & Architecture", "Define site goals, audit current performance, map URL structure, plan content architecture, specify technical requirements, and agree on design direction before any development begins."),
            ("🏗️", "Development & Build", "Custom theme and plugin development with performance and SEO requirements built in — iterative staging builds with client review at each milestone before production deployment."),
            ("🚀", "Launch & Optimise", "Pre-launch checklist: Core Web Vitals audit, SEO technical review, security scan, form testing, analytics verification — then go live with monitoring in place for the first 30 days."),
            ("🔧", "Maintenance & Growth", "Ongoing monthly maintenance: plugin updates, security scanning, performance monitoring, and feature additions as your business grows and marketing requirements evolve."),
        ],
        "price_from": "$3,500",
        "price_note": "for a custom WordPress build — WooCommerce and complex builds from $6,500",
        "faqs": [
            ("Do you use page builders like Elementor or Divi?", "No. Lumo builds custom WordPress themes with hand-written code rather than page builders. Page builders generate excessive markup, load unnecessary JavaScript, and make it harder to control Core Web Vitals. Custom-coded themes are faster, more maintainable, and give us precise control over every element that affects SEO and performance."),
            ("How long does a WordPress development project take?", "A standard informational WordPress site takes 4–6 weeks from kickoff to launch. A WooCommerce store with custom functionality takes 8–12 weeks. Complex multi-site builds or custom plugin development projects are quoted separately based on scope. Timeline includes design review rounds and staging environment testing."),
            ("Will my site be SEO-ready out of the box?", "Yes. Every Lumo WordPress build includes: clean URL structure, XML sitemap, schema markup, canonical tags, Open Graph meta tags, optimised heading hierarchy, image alt text management, and integration with a lightweight SEO plugin for ongoing management. We don't launch sites that aren't technically optimised for search."),
            ("What happens after the site launches?", "Lumo offers monthly maintenance plans that cover plugin updates, WordPress core updates, security scanning, performance monitoring, and up to 2 hours of content or feature changes per month. This keeps your site secure, fast, and supported as WordPress evolves. Development-only clients can also purchase ad-hoc support hours."),
            ("Can you redesign our existing WordPress site without hurting SEO?", "Yes — we specialise in WordPress redesigns that preserve and improve SEO equity. This includes URL structure mapping and 301 redirect implementation, Search Console property verification, sitemap resubmission, and crawl error monitoring post-launch. We treat SEO preservation as a core project requirement, not an afterthought."),
        ],
        "cta_h2": "Ready for a WordPress Site That Actually Performs?",
        "cta_sub": "Get a free WordPress site audit — we'll assess your current performance, Core Web Vitals, and technical SEO, then show you exactly what a faster, better-converting site looks like.",
        "schema_service_name": "WordPress Development Services",
        "schema_service_desc": "Custom WordPress development for US businesses — themes, plugins, WooCommerce, performance optimisation, and SEO-ready builds designed to convert.",
    },

    "shopify-development": {
        "title_tag":  "Shopify Development Agency | Custom Stores & Theme Builds | Lumo AI",
        "meta_desc":  "Shopify development services from Lumo AI Agency. Custom theme development, app integration, store migration, Shopify Plus builds, and conversion rate optimisation. Free Shopify audit.",
        "canonical":  "https://lumoaiagency.com/services/shopify-development",
        "og_title":   "Shopify Development Agency | Lumo AI Agency",
        "og_desc":    "Custom Shopify stores built to convert. Lumo develops bespoke Shopify themes, app integrations, and Plus builds — with CRO and SEO baked in from the first line of code.",
        "h1_html":    "Shopify Development That <span class=\"hl-lime\">Converts Browsers</span> Into Buyers",
        "badge":      "Shopify Development Specialists",
        "lead":       "Shopify powers 4.6 million stores — but 98% of visitors leave without buying. Lumo builds custom Shopify themes and store experiences designed around the psychology of purchase: fast-loading, conversion-optimised, SEO-ready stores that turn traffic into revenue.",
        "stat1_num": "4.6M",  "stat1_lbl": "Active Shopify stores in the US",
        "stat2_num": "2-4%",  "stat2_lbl": "Average e-commerce conversion rate (Lumo targets 3–6%)",
        "stat3_num": "$1.75T","stat3_lbl": "In global e-commerce GMV facilitated by Shopify (2024)",
        "why_h2": "Why Your Shopify Theme Is Costing You Sales",
        "why_p1": "Most Shopify stores use off-the-shelf themes that were designed to look good in a demo environment, not to convert your specific audience. Generic themes apply average design decisions — and average doesn't win in competitive e-commerce. Your product pages, collection pages, cart experience, and checkout flow should be engineered around your customer's behaviour, not a theme developer's aesthetic preferences.",
        "why_p2": "Shopify's native SEO capabilities are also limited by default. Without custom development, most stores have duplicate content issues (collection vs. product URL conflicts), missing structured data, unoptimised category page architectures, and poor internal linking. These are technical deficits that cap organic traffic potential regardless of how much you spend on content.",
        "why_p3": "Lumo builds Shopify stores with conversion rate and SEO performance as primary design constraints. Every decision — layout, page speed, trust signal placement, cart flow, product photography specifications, upsell mechanics — is made with data-informed conversion principles. The result is a store that looks great and performs commercially.",
        "services_h2": "Our Shopify Development Services",
        "services": [
            ("🎨", "Custom Theme Development", "Bespoke Shopify themes — not Dawn or other stock themes with minor modifications. Fully custom Liquid templates built to your brand specification with performance, CRO, and SEO requirements embedded in the code."),
            ("🛍️", "Store Setup & Configuration", "New Shopify store configuration — product catalogue architecture, collection hierarchy, navigation structure, payment gateway setup, shipping configuration, tax settings, and initial SEO foundations."),
            ("📱", "Shopify Plus Development", "Enterprise Shopify Plus builds with custom checkout extensions, Scripts for B2B pricing, Flow automation, Launchpad for sale events, and multi-storefront configurations for international markets."),
            ("🔗", "App Integration & Development", "Third-party app integration and custom app development — subscription apps, loyalty programs, review platforms, ERP connections, CRM sync, and custom functionality beyond what the Shopify App Store provides."),
            ("🔄", "Platform Migration", "Migration from WooCommerce, Magento, BigCommerce, or other platforms to Shopify — with product data migration, redirect mapping, SEO equity preservation, and customer account migration."),
            ("⚡", "Speed & CRO Optimisation", "Shopify store performance audit and optimisation — image compression, lazy loading, app audit (removing speed-killing apps), LCP improvement, and A/B testing of product page and checkout elements."),
        ],
        "process": [
            ("🔍", "Discovery & Strategy", "Audit current store performance and conversion funnel. Define target customer journey, design requirements, technical integrations, and success metrics before any development begins."),
            ("🎨", "Design & Development", "Custom design mockups for key page templates, followed by Liquid theme development on a development store — with staging review at each milestone before production build."),
            ("🚀", "Launch & Verify", "Pre-launch QA: cross-browser testing, mobile responsiveness, checkout flow test, GA4 e-commerce tracking verification, Google Search Console setup, and Core Web Vitals audit before go-live."),
            ("📈", "Optimise & Scale", "Post-launch CRO testing — A/B experiments on product pages, checkout flow, and upsell mechanics — plus ongoing development support as your catalogue and app requirements grow."),
        ],
        "price_from": "$4,000",
        "price_note": "for a custom Shopify theme build — Shopify Plus builds from $8,000",
        "faqs": [
            ("Do you use Shopify's free themes or build custom?", "Lumo builds fully custom Shopify themes using Liquid templating. We don't modify stock themes like Dawn — custom builds give us full control over page speed, conversion elements, and SEO structure. If your budget requires a theme-based approach, we'll recommend the best performing base themes and apply targeted customisations rather than generic modifications."),
            ("What's the difference between Shopify and Shopify Plus?", "Shopify Plus is Shopify's enterprise tier, designed for high-volume merchants. It adds custom checkout extensions (Scripts), advanced B2B pricing and wholesale portals, Flow automation, Launchpad for scheduled campaigns, and dedicated support. It's recommended for stores doing $1M+ annually or with complex B2B or international requirements. Lumo develops for both tiers."),
            ("How long does a Shopify development project take?", "A custom Shopify theme build takes 5–8 weeks. A full new store build with custom apps and integrations takes 8–12 weeks. A platform migration project from WooCommerce or Magento takes 6–10 weeks depending on catalogue size and redirect complexity. Timelines include design review and staging environment testing rounds."),
            ("Can you improve the performance of our existing Shopify store?", "Yes — Shopify performance optimisation is a standalone service. We audit your current theme code, installed apps (each adds JavaScript overhead), image delivery, and liquid rendering performance. Most stores can achieve 30–50% improvement in LCP and overall speed scores through targeted optimisation without a full rebuild."),
            ("Do you provide ongoing support after launch?", "Yes. Lumo offers Shopify retainer support covering theme updates, new feature development, app integrations, and CRO testing — priced per hour or as a monthly retainer based on your development volume. We also offer Shopify Plus clients dedicated development support as part of ongoing marketing engagement packages."),
        ],
        "cta_h2": "Ready to Build a Shopify Store That Actually Converts?",
        "cta_sub": "Get a free Shopify audit — we'll review your current theme, page speed, conversion flow, and SEO foundations, then show you what a higher-converting store looks like for your brand.",
        "schema_service_name": "Shopify Development Services",
        "schema_service_desc": "Custom Shopify development for US e-commerce brands — bespoke themes, Shopify Plus builds, app integrations, and conversion-optimised store experiences.",
    },

    "website-maintenance": {
        "title_tag":  "Website Maintenance Services | Ongoing Support & Updates | Lumo AI",
        "meta_desc":  "Website maintenance services from Lumo AI Agency. Ongoing support, security updates, performance monitoring, content updates, and technical health management. Plans from $300/mo.",
        "canonical":  "https://lumoaiagency.com/services/website-maintenance",
        "og_title":   "Website Maintenance Services | Lumo AI Agency",
        "og_desc":    "Keep your website fast, secure, and performing. Lumo's website maintenance plans cover security updates, performance monitoring, content changes, and technical health management.",
        "h1_html":    "Website Maintenance That Keeps Your Site <span class=\"hl-lime\">Fast, Secure</span> & Growing",
        "badge":      "Website Maintenance Specialists",
        "lead":       "A website that isn't maintained is a website that's actively degrading. Security vulnerabilities accumulate, plugins break, performance regresses, and broken links multiply — costing you traffic, conversions, and brand credibility. Lumo's maintenance plans keep your site in peak condition without burdening your team.",
        "stat1_num": "30k",  "stat1_lbl": "Websites hacked every day due to outdated software",
        "stat2_num": "88%",  "stat2_lbl": "Of users won't return after a bad website experience",
        "stat3_num": "1s",   "stat3_lbl": "Page load delay reduces conversions by 7%",
        "why_h2": "Why Website Maintenance Is a Revenue Decision, Not a Cost",
        "why_p1": "Most businesses treat website maintenance as an afterthought — something to deal with when something breaks. But by the time something visibly breaks, the damage is often already done: Google has crawled and indexed broken pages, security vulnerabilities have been exploited, or Core Web Vitals have declined enough to affect rankings. Proactive maintenance prevents these events rather than responding to them.",
        "why_p2": "The cumulative cost of neglect compounds. A WordPress plugin vulnerability left unpatched for 30 days is a meaningful security risk. A Core Web Vitals regression caused by a new plugin or content change impacts your ranking position. A broken checkout form or lead capture form costs you every lead it fails to submit. Regular maintenance catches these before they become incidents.",
        "why_p3": "Lumo's maintenance plans go beyond 'updates applied.' We monitor uptime, performance metrics, and security posture continuously — alerting on anomalies before they become user-facing problems. Monthly reporting shows you exactly what was done and what's on the horizon, so you always know the health of your digital infrastructure.",
        "services_h2": "Our Website Maintenance Services",
        "services": [
            ("🔒", "Security Updates & Monitoring", "Plugin and CMS core updates, malware scanning, file integrity monitoring, SSL certificate management, and vulnerability patching — keeping your site protected against the 30,000+ daily attacks targeting CMS vulnerabilities."),
            ("⚡", "Performance Monitoring & Optimisation", "Monthly Core Web Vitals checks, page speed monitoring, image optimisation audits, and proactive fixes for performance regressions caused by content changes, new plugins, or server configuration drift."),
            ("📝", "Content & Page Updates", "Text changes, image swaps, new page creation, blog post publishing, team member updates, pricing changes — up to a defined monthly hours allowance so your site stays current without requiring developer involvement."),
            ("🔍", "SEO Health Monitoring", "Monthly crawl to detect broken links, redirect errors, missing meta tags, duplicate content issues, and new indexation problems — with fixes applied before issues compound into ranking losses."),
            ("📊", "Analytics & Reporting", "Monthly site health report covering uptime, speed metrics, security status, changes made, and a dashboard summary of organic traffic, lead volume, and Core Web Vitals — so you always know what's happening."),
            ("🆘", "Emergency Support", "Priority response for site outages, hacked sites, broken functionality, or urgent fixes — with committed response times depending on plan tier. Emergency response outside normal maintenance scope is included in premium plans."),
        ],
        "process": [
            ("🔍", "Site Audit", "Full technical audit of your current site — security posture, plugin versions, performance benchmarks, broken links, and SEO health — establishing the baseline and identifying immediate fixes required."),
            ("🔧", "Onboarding & Setup", "Access provisioning, monitoring tool configuration, backup scheduling, security hardening, and documentation of your site's architecture and any custom code that requires special handling."),
            ("🔄", "Monthly Maintenance Cycle", "Scheduled monthly maintenance window: security updates applied, performance checks run, content updates completed, SEO health scan reviewed, and monthly report delivered."),
            ("📈", "Continuous Improvement", "Quarterly strategy review identifying opportunities to improve performance, conversion rate, or technical SEO based on accumulated monitoring data and your evolving business needs."),
        ],
        "price_from": "$300",
        "price_note": "per month for standard maintenance — premium plans with priority support from $600/mo",
        "faqs": [
            ("What CMS platforms does Lumo maintain?", "Lumo provides maintenance for WordPress (including WooCommerce), Shopify (theme and app management), Webflow, and custom HTML/CSS/JS sites. The scope of maintenance varies by platform — WordPress requires the most active security management, while Shopify and Webflow have fewer security risks but still benefit from performance monitoring and content management support."),
            ("What's the difference between maintenance plans?", "Standard plans cover security updates, monthly performance checks, up to 2 hours of content changes, and monthly reporting. Premium plans add priority support response times, up to 5 hours of content and development changes, quarterly strategy reviews, and emergency response coverage. We'll recommend the right tier based on your site's complexity and how frequently you need content updates."),
            ("How do website backups work?", "Lumo configures automated daily backups stored off-server (not just on your hosting provider). Backups include database and file system. In the event of a security incident or failed update, we can restore to any backup point within the last 30 days. Backup frequency increases to multiple daily backups for e-commerce sites where order data is business-critical."),
            ("What happens if something breaks between maintenance windows?", "All Lumo maintenance clients have access to support for unexpected issues between scheduled maintenance windows. Standard plan clients receive 48-hour response for non-critical issues. Premium plan clients receive same-day response. For complete site outages, all plans include emergency response within 4 hours during business hours."),
            ("Can I upgrade or cancel my maintenance plan?", "Yes — maintenance plans are monthly rolling with 30 days notice to cancel or downgrade. Upgrade is effective immediately. We don't require annual contracts for standard maintenance — you stay because the service is valuable, not because you're locked in."),
        ],
        "cta_h2": "Ready to Stop Worrying About Your Website?",
        "cta_sub": "Get a free website health audit — we'll assess your current security posture, performance scores, and maintenance gaps, and recommend the right plan to keep your site protected and performing.",
        "schema_service_name": "Website Maintenance Services",
        "schema_service_desc": "Ongoing website maintenance for US businesses — security updates, performance monitoring, content management, SEO health monitoring, and emergency support.",
    },

    "copywriting": {
        "title_tag":  "Copywriting Agency | Conversion-Focused Copy That Sells | Lumo AI",
        "meta_desc":  "Copywriting services from Lumo AI Agency. Website copy, landing pages, email sequences, ad copy, and sales pages — written for conversion and optimised for SEO. Free copy audit.",
        "canonical":  "https://lumoaiagency.com/services/copywriting",
        "og_title":   "Copywriting Agency | Lumo AI Agency",
        "og_desc":    "Copy that converts — not just reads well. Lumo writes website copy, landing pages, email sequences, and ad creative built around your audience's psychology and your conversion goals.",
        "h1_html":    "Copywriting That <span class=\"hl-lime\">Converts Readers</span> Into Customers",
        "badge":      "Conversion Copywriting Specialists",
        "lead":       "Most copy fails because it's written for the brand, not the buyer. Lumo writes conversion-focused copy — website pages, landing pages, email sequences, and ad creative — built around your customer's psychology, designed to answer their objections, and structured to drive the next action.",
        "stat1_num": "80%", "stat1_lbl": "Of visitors read only the headline — copy structure is everything",
        "stat2_num": "7x",  "stat2_lbl": "More leads from copy that addresses specific buyer pain points",
        "stat3_num": "30%", "stat3_lbl": "Average lift in conversion rate from professional copywriting",
        "why_h2": "Why Most Business Copy Fails to Convert",
        "why_p1": "Most businesses write copy about themselves: what they do, how long they've been operating, their mission statement, their team's credentials. Buyers don't care about any of that — at least not at first. They care about their problem, whether you understand it, and whether you can solve it better than the alternatives. Copy that starts with the customer's reality outperforms company-first copy on every metric.",
        "why_p2": "Structure matters as much as content. The order in which information is presented, the hierarchy of headlines, the placement of social proof, the specificity of the offer, the friction in the call-to-action — these structural decisions determine whether someone reads to the end or bounces. Conversion copywriting is a discipline, not creative writing with a button at the bottom.",
        "why_p3": "Lumo's copywriters combine direct response discipline with SEO requirements and brand voice consistency. Every piece of copy is researched — customer interviews, competitor analysis, review mining — before a word is written. We write to a defined conversion goal and test headline and CTA variants to improve results over time.",
        "services_h2": "Our Copywriting Services",
        "services": [
            ("🌐", "Website Copywriting", "Full website copy — homepage, about, services, and contact pages — written to your customer's decision journey with clear value propositions, objection handling, and conversion-oriented CTAs throughout."),
            ("📄", "Landing Page Copy", "High-converting landing page copy for paid traffic, lead magnets, and product launches — with headline testing variants, benefit-focused body copy, social proof integration, and friction-minimising CTAs."),
            ("📧", "Email Copywriting", "Email sequence copy for nurture campaigns, welcome series, promotional campaigns, and re-engagement flows — written for open rate, click rate, and conversion with platform-specific formatting."),
            ("📢", "Ad Copy", "Paid ad copy for Google Search, Meta, LinkedIn, and TikTok — headline variants, description copy, and creative scripts calibrated to platform character limits and audience psychology at each funnel stage."),
            ("💼", "Sales Page Copy", "Long-form sales page copy for products, services, and courses — full problem/solution narrative, feature/benefit stacks, testimonial placement, FAQ objection handling, and multi-point CTA structure."),
            ("🔍", "SEO Blog Writing", "SEO-optimised blog content targeting specific keywords — researched, structured with proper heading hierarchy, internally linked, and written for both search visibility and genuine audience value."),
        ],
        "process": [
            ("🔍", "Research & Discovery", "Customer research (interviews, reviews, competitor analysis), audience pain point mapping, competitive positioning analysis, and brand voice definition before any copy is drafted."),
            ("📝", "Strategy & Outline", "Conversion goal definition, message hierarchy, key proof points, objection list, and structural outline — agreed before full copy is written to avoid expensive revision cycles."),
            ("✍️", "Draft & Refine", "First draft delivered for review, followed by two rounds of revisions based on client feedback — with rationale provided for copy choices so edits are informed rather than subjective."),
            ("🧪", "Test & Optimise", "For landing pages and email: A/B testing of headline variants and CTAs, with performance data fed back into copy refinements over the first 90 days post-launch."),
        ],
        "price_from": "$800",
        "price_note": "per page for website or landing page copy — email sequences from $1,500 for a 5-email flow",
        "faqs": [
            ("What industries does Lumo write copy for?", "Lumo writes copy for SaaS, professional services (legal, financial, consulting), e-commerce, healthcare, home services, B2B technology, and marketing agencies. We specialise in industries where the sale requires trust-building — high-consideration purchases where copy needs to do real persuasion work, not just describe features."),
            ("What's the difference between copywriting and content writing?", "Copywriting is writing with a direct conversion goal — a specific action you want the reader to take (buy, sign up, request a quote). Content writing (blogs, guides, articles) is written to build authority, attract organic traffic, and provide value — with conversion as a secondary goal. Lumo does both, but treats them as different disciplines with different success metrics."),
            ("Do you include SEO in website copy?", "Yes — Lumo's website and landing page copy includes primary keyword integration, natural semantic keyword variation, optimised heading structure, and meta title and description copy. SEO requirements are balanced against conversion requirements — we never stuff keywords at the expense of readability and persuasion."),
            ("How many revisions are included?", "All Lumo copy projects include two rounds of revisions at no additional cost. Revisions should be consolidated — one set of feedback per round rather than incremental changes. Copy is revised based on strategic rationale, not subjective preference — we'll discuss feedback before implementing changes that we believe will reduce conversion effectiveness."),
            ("Can you match our existing brand voice?", "Yes — brand voice matching is part of our discovery process. We analyse existing copy (website, email, social) to extract voice attributes, and provide a voice and tone brief for review before drafting. If you don't have a defined brand voice, we develop one as part of the project. Consistency across all copy is a priority."),
        ],
        "cta_h2": "Ready for Copy That Actually Converts?",
        "cta_sub": "Get a free copy audit — we'll review your highest-traffic pages, identify conversion gaps and messaging weaknesses, and show you the specific copy changes that would improve your results.",
        "schema_service_name": "Copywriting Services",
        "schema_service_desc": "Conversion-focused copywriting for US businesses — website copy, landing pages, email sequences, ad copy, and sales pages built to drive action.",
    },

    "review-management": {
        "title_tag":  "Review Management Agency | Generate & Respond to Reviews | Lumo AI",
        "meta_desc":  "Review management services from Lumo AI Agency. Google review generation, review response management, reputation monitoring, and negative review mitigation for US businesses. Free audit.",
        "canonical":  "https://lumoaiagency.com/services/review-management",
        "og_title":   "Review Management Agency | Lumo AI Agency",
        "og_desc":    "93% of consumers read reviews before buying. Lumo's review management programs generate authentic Google reviews, manage responses, and protect your online reputation proactively.",
        "h1_html":    "Review Management That <span class=\"hl-lime\">Builds Trust</span> & Wins More Customers",
        "badge":      "Review & Reputation Specialists",
        "lead":       "93% of consumers read online reviews before making a purchase — and your star rating is visible in search results before they even visit your site. Lumo builds systematic review generation programs that grow your rating, manage responses, and protect your reputation across Google, Yelp, and industry-specific platforms.",
        "stat1_num": "93%", "stat1_lbl": "Of consumers read reviews before purchasing",
        "stat2_num": "31%", "stat2_lbl": "More spending by customers of businesses with excellent reviews",
        "stat3_num": "4.0+","stat3_lbl": "Minimum star rating 57% of consumers require before choosing",
        "why_h2": "Why Your Review Profile Is a Revenue Asset",
        "why_p1": "Online reviews have become the default trust signal for consumer decisions. When someone Googles your business name — or searches for the service you provide — your star rating and review count appear in the knowledge panel, local pack, and Google Business Profile before they reach your website. A low rating or sparse review count loses you customers before you ever get a chance to pitch them.",
        "why_p2": "The challenge is that review generation happens by default — not in your favour. Unhappy customers are 3x more likely to leave a review than satisfied ones without prompting. The businesses with the highest ratings are those that have systematically asked happy customers to share their experience, not those with the fewest complaints.",
        "why_p3": "Lumo builds review management programs that shift this asymmetry. We implement ethical, compliant review request workflows triggered at the moment of highest customer satisfaction — through email, SMS, or QR code — with personalised messaging that makes leaving a review easy. We also manage responses to every review, positive and negative, to demonstrate active engagement and mitigate damage from critical feedback.",
        "services_h2": "Our Review Management Services",
        "services": [
            ("⭐", "Review Generation Campaigns", "Systematic review request programs — email and SMS sequences triggered at post-service or post-purchase satisfaction peaks, with platform-specific direct links and personalised messaging that drives completion."),
            ("💬", "Review Response Management", "Professional, brand-consistent responses to every Google, Yelp, and platform review — positive reviews thanked personally, negative reviews addressed constructively with empathy and resolution offers."),
            ("🔍", "Reputation Monitoring", "Real-time monitoring across Google, Yelp, Facebook, TripAdvisor, G2, Capterra, and industry-specific platforms — alerting you within hours of new reviews so responses are timely and issues don't compound."),
            ("🛡️", "Negative Review Mitigation", "Strategic response protocols for negative reviews — addressing root cause, demonstrating resolution, and when appropriate, working with platforms on review policy violations for fake or spam reviews."),
            ("📊", "Review Analytics & Reporting", "Monthly report covering review count growth, average rating trend, platform distribution, sentiment analysis, and response rate — with benchmarking against local competitors and industry averages."),
            ("🏪", "Google Business Profile Optimisation", "GBP setup and optimisation — business information completeness, category selection, photo management, post scheduling, and Q&A management — the full profile that hosts your reviews and affects local ranking."),
        ],
        "process": [
            ("🔍", "Audit & Baseline", "Audit existing reviews across all platforms, assess rating health, identify review gaps versus competitors, and document current GBP optimisation status — establishing the baseline before any program launches."),
            ("🏗️", "Program Design & Setup", "Design review request workflow, configure automation platform, set up monitoring alerts, build response templates by scenario, and launch GBP optimisation — program ready within 2 weeks."),
            ("🚀", "Launch & Monitor", "Activate review request campaigns, begin monitoring, and start responding to all new reviews within 24 hours. Track rating movement and completion rates weekly during the first 60 days."),
            ("📈", "Optimise & Report", "Monthly performance review, request message A/B testing, platform strategy adjustments based on where your customers are most active, and competitive benchmarking to track relative reputation position."),
        ],
        "price_from": "$600",
        "price_note": "per month — includes review generation, response management, and monthly reporting",
        "faqs": [
            ("Is it legal to ask customers for reviews?", "Yes — asking customers to leave reviews is completely legitimate and encouraged by Google. What's prohibited is incentivising reviews (offering discounts or gifts in exchange for reviews), creating fake reviews, or suppressing negative reviews by only sending review requests to customers you know are happy. Lumo builds compliant programs that ask all customers for honest feedback — which is what generates trust."),
            ("Which review platforms do you manage?", "Lumo monitors and manages responses across Google Business Profile, Yelp, Facebook, TripAdvisor, G2, Capterra, Trustpilot, BBB, Healthgrades, Avvo, Houzz, Angi, and other industry-specific platforms. The platforms prioritised for active review generation depend on which ones Google displays prominently for your business type and location."),
            ("How quickly can we see improvement in our rating?", "For businesses with an active customer base, a well-run review generation program can generate 10–30+ new Google reviews per month, with measurable rating improvement within 60–90 days. The rate depends on your review request volume, current customer satisfaction levels, and your completion rate on review requests (typically 15–25% completion from email, 20–35% from SMS)."),
            ("What do you do about fake or unfair negative reviews?", "Lumo responds professionally to all negative reviews with empathy and resolution offers — this response is often more important to future readers than the review itself. For reviews that violate Google's policies (fake reviews, conflict of interest, spam), we can flag them for Google review with documented rationale. Google does remove policy-violating reviews, but the process takes time and isn't guaranteed."),
            ("Does review management work for multi-location businesses?", "Yes — multi-location review management is one of Lumo's specialities. We manage review profiles for each location separately, ensuring each GBP is optimised, responses are location-specific, and review generation programs reference the correct location. Rating benchmarking is done at both the brand level and individual location level."),
        ],
        "cta_h2": "Ready to Turn Your Customer Satisfaction Into More Customers?",
        "cta_sub": "Get a free reputation audit — we'll assess your current review profile across all platforms, compare you to local competitors, and show you exactly how much business your ratings are winning or losing.",
        "schema_service_name": "Review Management Services",
        "schema_service_desc": "Review generation and reputation management for US businesses — Google review campaigns, response management, reputation monitoring, and negative review mitigation.",
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
          <li><a href="../services/technical-seo.html">Technical SEO</a></li>
          <li><a href="../services/local-seo.html">Local SEO</a></li>
          <li><a href="../services/link-building.html">Link Building</a></li>
          <li><a href="../services/marketing-automation.html">Marketing Automation</a></li>
          <li><a href="../services/copywriting.html">Copywriting</a></li>
          <li><a href="../services/review-management.html">Review Management</a></li>
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
