"""Batch 16 — Backlog Batch 11: social-commerce, product-photography, ai-consulting, chatgpt-optimization, ai-chatbot"""
import json, os

SERVICES = {
    "social-commerce": {
        "title": "Social Commerce",
        "tagline": "Sell directly on Instagram, TikTok Shop, Pinterest, and Facebook — social shopping done right",
        "desc": "Social commerce is the fastest-growing retail channel — consumers are buying without ever leaving their social apps. We build and manage your social commerce presence across Instagram Shop, TikTok Shop, Pinterest Shopping, and Facebook Shop: catalog setup, shoppable content strategy, live shopping, and full performance management.",
        "price": "$2,500/mo",
        "stat1": "$1.2T",
        "stat1_label": "projected global social commerce revenue by 2025",
        "stat2": "73%",
        "stat2_label": "of Gen Z discover and buy products via social media",
        "stat3": "3x",
        "stat3_label": "higher conversion rates for social shopping vs. traditional social ads",
        "deliverables": [
            ("🛍️", "Multi-Platform Shop Setup", "Complete shop setup across Instagram Shop, TikTok Shop, Facebook Shop, and Pinterest Shopping: catalog integration, product tagging, shop policies, and payment configuration."),
            ("📸", "Shoppable Content Strategy", "Content strategy and production coordination for shoppable posts, reels, and stories: product tagging, creative direction, and posting cadence optimized for each platform's shopping algorithm."),
            ("🎬", "TikTok Shop Management", "Full TikTok Shop management: product listing optimization, TikTok-specific content strategy, affiliate creator recruitment, and live shopping event coordination."),
            ("📌", "Pinterest Shopping", "Pinterest product pins, shoppable boards, catalog optimization, and shopping ads management — capturing high-purchase-intent Pinterest users actively planning purchases."),
            ("🤝", "Creator & Affiliate Commerce", "Social commerce affiliate program setup: recruiting creators to tag and sell your products, managing commission structures, and tracking affiliate-driven sales across platforms."),
            ("📊", "Social Commerce Analytics", "Unified reporting across all social commerce channels: revenue by platform, best-performing shoppable content, product-level conversion rates, and attribution analysis."),
            ("🔄", "Catalog Optimization", "Ongoing product catalog management: pricing accuracy, inventory sync, product description optimization for social discovery, and seasonal catalog updates."),
        ],
        "process": [
            ("🔍", "Platform Audit & Strategy", "We audit your existing social presence and e-commerce setup, identify the highest-opportunity platforms for your products and audience, and build a social commerce strategy."),
            ("⚙️", "Shop Setup & Catalog", "All shops set up and catalogs connected. Product listings optimized for each platform's discovery algorithm. Payment and policy configurations completed."),
            ("📸", "Content & Launch", "Shoppable content launched across platforms. Creator outreach initiated. TikTok Shop affiliate program activated. Live shopping events scheduled."),
            ("📈", "Optimize & Scale", "Monthly performance review: top-performing products and content identified, underperformers refreshed, budget shifted to highest-converting platforms."),
        ],
        "faqs": [
            ("Which social commerce platform should we start with?", "It depends on your product and audience. TikTok Shop for consumer products targeting 18–35 year olds. Instagram Shop for lifestyle and fashion brands. Pinterest Shopping for home, beauty, and craft products. We recommend a priority based on your audience data."),
            ("Do we need a Shopify or WooCommerce store to do social commerce?", "No — but integration is much easier with an existing e-commerce platform. We can connect your existing store catalog or build a standalone social commerce setup. Shopify has the best native integrations with most platforms."),
            ("What is TikTok Shop and should we be on it?", "TikTok Shop is TikTok's in-app marketplace with affiliate creator selling, live shopping, and shoppable videos. If your product targets under-35 consumers, TikTok Shop is one of the highest-growth channels available right now."),
            ("Do you produce the shoppable content?", "We provide content strategy and direction. Content production can be handled by your team, our performance creative service, or UGC creators we source. We coordinate the full workflow."),
            ("How do you track social commerce revenue?", "Each platform provides native sales reporting. We integrate this data into a unified dashboard alongside your e-commerce platform's order data — giving you accurate, deduplicated revenue attribution per channel."),
        ],
        "schema_service_desc": "Social commerce — Instagram Shop, TikTok Shop, Pinterest Shopping, Facebook Shop setup, shoppable content, creator affiliate programs, and performance analytics.",
    },
    "product-photography": {
        "title": "Product Photography",
        "tagline": "High-conversion product images for e-commerce, Amazon, and social media",
        "desc": "Product photography is the single highest-impact conversion factor in e-commerce — better images directly increase add-to-cart rates, reduce returns, and improve ad performance. We produce high-quality product photography: studio shots, lifestyle imagery, Amazon-compliant main images, and social media creative — all optimized for conversion.",
        "price": "$1,800",
        "stat1": "93%",
        "stat1_label": "of purchase decisions are influenced by product visuals",
        "stat2": "40%",
        "stat2_label": "average conversion increase with professional vs. DIY photos",
        "stat3": "22%",
        "stat3_label": "reduction in return rates with accurate, high-quality imagery",
        "deliverables": [
            ("📸", "Studio Product Photography", "Clean, white-background studio shots for every SKU: front, back, side, and detail angles — compliant with Amazon, Google Shopping, and major marketplace image requirements."),
            ("🏡", "Lifestyle Photography", "In-context lifestyle images showing your product in use: staged environments, models (if applicable), and scenes that communicate the product's value and aspirational use case."),
            ("🔍", "Detail & Feature Shots", "Close-up detail photography highlighting key product features, materials, textures, and quality — the images that answer the questions buyers have before they buy."),
            ("📐", "Image Optimization & Editing", "Professional post-processing: background removal, color correction, shadow effects, retouching, and resizing for every required platform format (2000x2000px for Amazon, 1:1 for Instagram, etc.)."),
            ("🎨", "Composite & Infographic Images", "Amazon A+ style composite images: product images with text callouts, feature highlights, size reference photos, and comparison visuals — increasing conversion on marketplace listings."),
            ("📱", "Social Media Creative", "Social-format images for Instagram, Facebook, Pinterest, and TikTok: lifestyle crops, story formats, and branded overlay variations for paid and organic social use."),
            ("📁", "Full Asset Package", "All images delivered in full resolution (RAW and edited), web-optimized JPG/PNG for all platform requirements, and organized by SKU in a shared cloud folder."),
        ],
        "process": [
            ("🔍", "Creative Brief", "We define the shot list, styling direction, lifestyle scenarios, and required formats for each SKU — aligning creative direction to your brand and platform requirements before any production begins."),
            ("🏗️", "Pre-Production", "Props sourced, studio booked (or on-location logistics coordinated), models arranged (if applicable), and product prepared. Shot list finalized and approved."),
            ("📸", "Photo Shoot", "Professional shoot executed by experienced product photographers with studio lighting, professional equipment, and quality control for every frame."),
            ("🎨", "Edit & Deliver", "Full post-production: culling, retouching, background removal, color correction, and format optimization. Assets delivered organized and labeled within 5–7 business days."),
        ],
        "faqs": [
            ("Do you shoot products at our location or at a studio?", "Both options are available. Studio shoots are done at our partner studios in Austin or major US cities. On-location lifestyle shoots can be arranged at client premises, rental spaces, or outdoor locations. We recommend based on your product and creative vision."),
            ("How many photos do we get per SKU?", "Standard package includes 8–12 edited images per SKU: 3–4 white background angles, 2–3 lifestyle shots, and 2–3 detail/feature shots. Custom shot lists can expand or contract this."),
            ("Are your images Amazon-compliant?", "Yes — studio shots are produced to Amazon's main image requirements: pure white background (RGB 255,255,255), product fills 85%+ of frame, no text overlays, and minimum 1000px longest side."),
            ("Can you photograph multiple SKUs or product lines?", "Yes — multi-SKU shoots are our most efficient format. We organize by product line, batch similar setup requirements, and optimize the shoot day to maximize SKU coverage."),
            ("Do you provide models?", "Yes — model talent can be arranged for appropriate categories (apparel, beauty, lifestyle accessories). Model fees are quoted separately based on usage rights and shoot duration."),
        ],
        "schema_service_desc": "Product photography — studio shots, lifestyle imagery, detail photos, Amazon-compliant images, composite infographics, social media creative, and full asset delivery.",
    },
    "ai-consulting": {
        "title": "AI Consulting",
        "tagline": "Strategic AI advisory for businesses ready to deploy AI for real competitive advantage",
        "desc": "AI is moving faster than most businesses can evaluate it — and the gap between companies that deploy AI strategically and those that experiment randomly is widening fast. We provide strategic AI consulting: identifying where AI creates real ROI in your specific business, evaluating the right tools and vendors, and building the roadmap to implement AI without wasted spend.",
        "price": "$5,000/mo",
        "stat1": "72%",
        "stat1_label": "of companies report AI has improved at least one business function",
        "stat2": "3.5x",
        "stat2_label": "higher ROI for companies with a defined AI strategy",
        "stat3": "$4.4T",
        "stat3_label": "potential annual value AI could add to the global economy",
        "deliverables": [
            ("🔍", "AI Opportunity Assessment", "A structured audit of your business operations, workflows, and data assets to identify where AI creates genuine ROI — prioritized by impact, feasibility, and build-vs-buy trade-offs."),
            ("🗺️", "AI Strategy & Roadmap", "A 12-month AI implementation roadmap: which use cases to pursue first, in what sequence, with what tools, and with what success metrics — grounded in your actual business model and resources."),
            ("🛠️", "AI Tool Evaluation & Selection", "Vendor-neutral evaluation of AI tools and platforms for your specific use cases: LLMs, automation tools, analytics AI, and vertical-specific solutions — with build-vs-buy analysis and cost modeling."),
            ("⚙️", "Proof of Concept Design", "Structured POC design for high-priority AI use cases: scope definition, data requirements, success criteria, and evaluation framework — so POCs generate real signal, not just demos."),
            ("👥", "AI Literacy & Team Training", "Executive and team-level AI literacy training: what AI can and can't do, how to work with AI tools effectively, and how to evaluate AI vendor claims critically."),
            ("🔐", "AI Risk & Governance", "AI governance framework: data privacy compliance, model bias evaluation, output quality controls, vendor contract review, and employee AI usage policies — managing risk as you scale AI adoption."),
            ("📊", "ROI Measurement Framework", "Metrics and measurement framework for every AI initiative: baseline establishment, KPI definition, and reporting cadence — ensuring AI investments are accountable."),
        ],
        "process": [
            ("🔍", "Discovery & Assessment", "We interview stakeholders across functions, audit current workflows and data assets, and identify AI opportunities with the highest potential impact and realistic implementation paths."),
            ("🗺️", "Strategy Development", "AI strategy and roadmap built from discovery findings. Tool recommendations with cost-benefit analysis. Governance framework drafted. Reviewed with leadership."),
            ("⚙️", "POC & Implementation Support", "First-priority use cases moved to POC. We advise on vendor selection, data preparation, and implementation approach — working alongside your technical team."),
            ("📈", "Measure & Evolve", "Ongoing monthly advisory: POC results review, roadmap adjustments, new AI capability assessment, and vendor performance evaluation."),
        ],
        "faqs": [
            ("We already use ChatGPT — do we need AI consulting?", "Using ChatGPT is not an AI strategy. Most businesses using ChatGPT are getting 10–20% of its potential value because they lack systematic integration, proper prompting frameworks, and custom use case development. We help you go from ad hoc to strategic."),
            ("How is AI consulting different from digital transformation consulting?", "AI consulting is specifically focused on identifying, evaluating, and implementing AI technologies — not general technology or process consulting. We stay current on the AI landscape (new models, tools, capabilities) in a way that generalist consultants don't."),
            ("Do you build AI tools yourself?", "We advise on strategy and tool selection; we don't build custom AI models or applications ourselves. For custom AI development, we partner with our AI Development service."),
            ("What industries do you have AI consulting experience in?", "We've advised on AI strategy for SaaS, e-commerce, professional services, healthcare-adjacent businesses, financial services, and marketing agencies. Each industry has different high-value AI use cases we've developed playbooks for."),
            ("How do you stay current on AI developments?", "Our team evaluates new AI tools and model releases weekly. We maintain relationships with key AI vendors and participate in enterprise AI communities. Our clients benefit from ongoing intelligence on what's new and what's ready for production use."),
        ],
        "schema_service_desc": "AI consulting — opportunity assessment, AI strategy and roadmap, tool evaluation, POC design, team training, governance framework, and ROI measurement.",
    },
    "chatgpt-optimization": {
        "title": "ChatGPT Optimization",
        "tagline": "Optimize your brand visibility in ChatGPT, Claude, Perplexity, and AI search engines",
        "desc": "AI search engines are now a primary discovery channel — and most brands are invisible in them. ChatGPT, Claude, Perplexity, and Google AI Overviews answer millions of brand and product queries daily, and the brands they cite are capturing significant organic traffic and trust signals. We optimize your digital presence specifically for AI engine visibility and citation.",
        "price": "$2,500/mo",
        "stat1": "1B+",
        "stat1_label": "monthly users across major AI assistants in 2024",
        "stat2": "58%",
        "stat2_label": "of AI search responses include direct brand citations",
        "stat3": "3x",
        "stat3_label": "higher brand consideration for companies cited in AI answers",
        "deliverables": [
            ("🤖", "AI Visibility Audit", "Comprehensive audit of your current AI engine visibility: how you appear (or don't) in ChatGPT, Claude, Perplexity, and Google AI Overviews for your key queries — with gap analysis and opportunity map."),
            ("📝", "AI-Citation Content Strategy", "Content strategy designed for AI citation: the formats, structures, and topics that AI engines extract and cite — including FAQ content, comparison content, statistical claims, and authoritative definitions."),
            ("🏗️", "Knowledge Graph Optimization", "Google Knowledge Panel management, Wikipedia/Wikidata optimization, and entity disambiguation — establishing clear brand entity signals that AI systems use to identify and correctly represent your brand."),
            ("📄", "llms.txt Implementation", "llms.txt file creation and optimization — the emerging standard for communicating brand information directly to AI crawlers, giving you direct control over how AI engines understand your brand."),
            ("🔗", "Authority Signal Building", "Building the authority signals AI systems trust: high-quality backlinks, brand mentions in authoritative publications, and structured data that communicates expertise and credibility."),
            ("📊", "AI Mention Monitoring", "Monthly monitoring of your brand mentions across major AI engines: tracking citation frequency, sentiment, accuracy, and competitive positioning in AI responses."),
            ("🔄", "Content Optimization & Refresh", "Ongoing optimization of existing content for AI citability: adding statistical claims, authoritative sources, FAQ structure, and clear factual statements that AI engines prefer to extract."),
        ],
        "process": [
            ("🔍", "AI Visibility Audit", "We query major AI engines with your key brand and category terms, map your current visibility, and identify the specific gaps causing you to be underrepresented in AI answers."),
            ("📝", "Strategy & Content Plan", "AI-citation content strategy developed. llms.txt implementation planned. Knowledge graph gaps identified. Authority building roadmap built."),
            ("⚙️", "Implement & Optimize", "Content produced, llms.txt deployed, Knowledge Panel claimed and optimized, and authority signal campaigns launched. Monitoring systems activated."),
            ("📊", "Monitor & Iterate", "Monthly AI mention monitoring report. Content refreshed based on citation performance. Strategy adjusted as AI engine algorithms evolve."),
        ],
        "faqs": [
            ("Is ChatGPT Optimization the same as SEO?", "Related but distinct. SEO optimizes for Google's traditional search algorithm — ranked links. ChatGPT Optimization (also called GEO — Generative Engine Optimization) optimizes for AI systems that synthesize answers rather than rank pages. Different signals, different content formats, overlapping but not identical."),
            ("How do you measure AI search visibility?", "We conduct structured query sampling across AI engines (ChatGPT, Claude, Perplexity, Google AI Overviews) for your key brand, product, and category queries — measuring citation frequency, sentiment, accuracy, and competitive share of voice."),
            ("Can you control what ChatGPT says about us?", "Directly, no — AI models generate responses from their training data and web retrieval. Indirectly, yes — by building the authoritative content, brand signals, and structured data that AI systems trust and cite, we influence how your brand is represented over time."),
            ("How quickly does AI visibility improve?", "Faster than traditional SEO for some signals (llms.txt, structured data), slower for others (brand authority, citation frequency). Typical clients see meaningful AI visibility improvement within 3–6 months."),
            ("Is this related to your GEO service?", "Yes — our GEO (Generative Engine Optimization) service covers AI visibility broadly. ChatGPT Optimization is the specific focus on ChatGPT, Claude, and Perplexity — complementary to our GEO service."),
        ],
        "schema_service_desc": "ChatGPT optimization — AI visibility audit, citation content strategy, llms.txt, Knowledge Graph optimization, authority signals, and AI mention monitoring.",
    },
    "ai-chatbot": {
        "title": "AI Chatbot Development",
        "tagline": "Custom AI chatbots that qualify leads, answer questions, and book meetings 24/7",
        "desc": "A well-built AI chatbot is your best sales development rep — available 24/7, never misses a lead, and handles the repetitive questions that drain your team's time. We design and build custom AI chatbots for lead qualification, customer support, appointment booking, and internal knowledge retrieval — trained on your specific business context and integrated with your existing tools.",
        "price": "$6,000",
        "stat1": "24/7",
        "stat1_label": "availability — no leads lost outside business hours",
        "stat2": "67%",
        "stat2_label": "of consumers prefer chatbots for quick queries",
        "stat3": "3x",
        "stat3_label": "more leads qualified per month vs. form-only websites",
        "deliverables": [
            ("🤖", "Chatbot Strategy & Design", "Chatbot scope definition: use cases, conversation flows, qualification logic, escalation rules, and integration requirements — designed before any development begins."),
            ("🧠", "AI Model Configuration", "LLM selection and configuration (GPT-4, Claude, or Gemini), system prompt engineering, knowledge base construction, and response quality optimization — trained on your products, services, FAQs, and brand voice."),
            ("💬", "Conversation Flow Development", "Custom conversation flow design: welcome messages, qualification sequences, objection handling scripts, appointment booking flows, and fallback handling — all tested for natural conversation quality."),
            ("🔗", "CRM & Calendar Integration", "Integration with your CRM (HubSpot, Salesforce, or Pipedrive) for lead capture, with Calendly or Google Calendar for appointment booking — so chatbot-qualified leads flow directly into your pipeline."),
            ("🎨", "UI & Website Embedding", "Custom chat widget design (matching your brand colors, fonts, and style), placement optimization (page-specific triggers, exit intent, scroll triggers), and mobile responsiveness."),
            ("📊", "Analytics & Conversation Tracking", "Chatbot performance dashboard: conversation volume, qualification rate, handoff rate, common questions, and pipeline attributed to chatbot conversations — full visibility into ROI."),
            ("🔄", "Training & Optimization", "30-day post-launch training period: monitoring real conversations, correcting mishandled queries, expanding the knowledge base, and improving qualification logic based on real user behavior."),
        ],
        "process": [
            ("🔍", "Discovery & Design", "We map your ideal conversation flows, define qualification criteria, identify knowledge base sources, and design the full chatbot architecture before any development begins."),
            ("🧠", "Build & Train", "AI model configured, knowledge base built, conversation flows developed, and integrations connected. Internal testing and QA across device types and use cases."),
            ("🚀", "Launch & Monitor", "Chatbot launched on your website with proper placement and triggers. Real conversation monitoring begins immediately. First-week issues addressed within 24 hours."),
            ("🔄", "Train & Optimize", "30-day intensive optimization: conversation review, knowledge base expansion, flow refinements, and integration debugging. Monthly optimization ongoing after launch."),
        ],
        "faqs": [
            ("What AI model do you use?", "We use GPT-4 (OpenAI), Claude (Anthropic), or Gemini depending on use case and client preference. We evaluate the best model for your specific chatbot requirements — response quality, cost, speed, and knowledge cutoff."),
            ("How is this different from a basic website chat widget?", "Basic chat widgets (Intercom, Drift) are conversation management tools — they don't understand natural language or reason through complex questions. Our AI chatbots use large language models that understand context, handle nuanced questions, and provide intelligent responses — not scripted menus."),
            ("Can the chatbot be trained on our specific products and processes?", "Yes — we build a custom knowledge base from your documentation, FAQs, product pages, pricing, and process guides. The chatbot answers questions specific to your business, not generic information."),
            ("What happens when the chatbot can't answer a question?", "We design graceful escalation protocols: the chatbot acknowledges the limitation, captures contact information, and routes to a human via email, Slack notification, or CRM task — ensuring no lead is lost."),
            ("Do you handle maintenance after launch?", "Yes — the initial quote includes a 30-day post-launch optimization period. Ongoing maintenance (knowledge base updates, model updates, new conversation flows) is available as a monthly retainer."),
        ],
        "schema_service_desc": "AI chatbot development — custom chatbot strategy, LLM configuration, conversation flows, CRM integration, appointment booking, analytics, and post-launch optimization.",
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
            <li><a href="../services/ai-consulting.html">AI Consulting</a></li>
            <li><a href="../services/ai-chatbot.html">AI Chatbot</a></li>
            <li><a href="../services/chatgpt-optimization.html">ChatGPT Optimization</a></li>
            <li><a href="../services/social-commerce.html">Social Commerce</a></li>
            <li><a href="../services/product-photography.html">Product Photography</a></li>
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
