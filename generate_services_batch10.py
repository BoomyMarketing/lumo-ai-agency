"""Batch 10 — Backlog Batch 5: mobile-app-development, logo-design, graphic-design, social-media-design, pitch-deck-design"""
import json, os

SERVICES = {
    "mobile-app-development": {
        "title": "Mobile App Development",
        "tagline": "Native and cross-platform mobile apps built for growth — iOS & Android",
        "desc": "We design and develop high-performance mobile apps for iOS and Android — from MVP to enterprise-grade. Our apps are built for speed, scalability, and conversion using React Native, Flutter, or native Swift/Kotlin, with full backend integration, App Store submission, and post-launch support.",
        "price": "$8,000",
        "stat1": "6.8B",
        "stat1_label": "smartphone users worldwide",
        "stat2": "90%",
        "stat2_label": "of mobile time spent in apps",
        "stat3": "$935B",
        "stat3_label": "projected mobile app revenue by 2026",
        "deliverables": [
            ("📱", "iOS & Android Development", "Native or cross-platform development using React Native or Flutter — a single codebase delivering near-native performance on both platforms."),
            ("🎨", "UI/UX Design", "Human-centered design following Apple HIG and Material Design guidelines — wireframes, prototypes, and pixel-perfect UI for every screen."),
            ("⚙️", "Backend & API Integration", "REST or GraphQL API development, database design, authentication (OAuth, biometrics), push notifications, and third-party service integrations."),
            ("🔐", "Security & Compliance", "End-to-end encryption, secure data storage, GDPR/CCPA compliance, and App Store privacy label documentation."),
            ("🧪", "QA & Device Testing", "Manual and automated testing across 30+ device/OS combinations — functional, performance, regression, and accessibility testing."),
            ("🚀", "App Store Submission", "Full App Store Connect and Google Play Console submission — including screenshots, descriptions, privacy policies, and review response support."),
            ("🔄", "Post-Launch Support", "30-day bug warranty, crash monitoring (Sentry/Firebase Crashlytics), and ongoing maintenance plans for updates and OS compatibility."),
        ],
        "process": [
            ("🔍", "Discovery & Architecture", "We define feature scope, user flows, technical architecture, and third-party integrations. We deliver a detailed spec before any code is written."),
            ("🎨", "Design Sprint", "We design every screen in Figma — wireframes first, then high-fidelity mockups — and build an interactive prototype for your review and approval."),
            ("⚙️", "Development & QA", "Agile sprints with weekly demos. Backend and frontend developed in parallel. Automated testing runs on every commit; manual QA before each release."),
            ("🚀", "Launch & Scale", "We submit to both app stores, monitor reviews and crash reports, and provide a roadmap for v2 features based on user analytics and feedback."),
        ],
        "faqs": [
            ("Should I build native or cross-platform?", "For most startups and growth-stage businesses, React Native or Flutter delivers 80–90% of native performance at significantly lower cost. We recommend native (Swift/Kotlin) only for apps requiring deep hardware integration or maximum performance, like AR/VR or real-time video."),
            ("How long does a mobile app take to build?", "An MVP with core features typically takes 10–16 weeks. A full-featured app with complex backend and integrations can take 20–30 weeks. We provide a detailed timeline after discovery."),
            ("Do you handle both iOS and Android?", "Yes — we deliver both platforms simultaneously using cross-platform frameworks. For native builds, we have dedicated iOS and Android engineers."),
            ("What happens after launch?", "We include 30-day bug warranty. We also offer monthly maintenance plans covering OS updates, security patches, and minor feature additions."),
            ("Can you rebuild or modernize an existing app?", "Yes — we handle full app modernizations, including platform migrations (e.g., Objective-C to Swift), UI/UX redesigns, and backend refactors for legacy apps."),
        ],
        "schema_service_desc": "Mobile app development for iOS and Android — React Native, Flutter, native Swift/Kotlin, UI/UX design, backend integration, App Store submission, and post-launch support.",
    },
    "logo-design": {
        "title": "Logo Design",
        "tagline": "Memorable logos that capture your brand identity and stand the test of time",
        "desc": "Your logo is the cornerstone of your brand identity. We design logos that are distinctive, scalable, and strategically built — from initial concept exploration to final files delivered in every format you need. No templates, no stock icons — original designs crafted for your business.",
        "price": "$800",
        "stat1": "7s",
        "stat1_label": "to form a first impression of your brand",
        "stat2": "80%",
        "stat2_label": "brand recognition increase with consistent logo use",
        "stat3": "100%",
        "stat3_label": "original — no templates or stock icons",
        "deliverables": [
            ("✏️", "Brand Discovery & Moodboard", "We research your industry, competitors, and target audience to build a visual direction — color palette, typography style, and reference moodboard for alignment before design begins."),
            ("🎨", "3 Original Concepts", "Three distinct logo concepts — each with a unique design direction, typeface, and visual concept — presented with context explaining the strategic rationale."),
            ("🔄", "2 Rounds of Revisions", "Two full revision rounds on your chosen concept to refine colors, spacing, typography weight, and any other elements until the logo is exactly right."),
            ("📁", "Complete File Package", "Final logo delivered in SVG, PNG (transparent background), PDF (vector), and JPG — in color, reversed (white), and black versions for all use cases."),
            ("📋", "Brand Usage Guide", "One-page brand guide covering logo clear space rules, minimum size, color codes (HEX, RGB, CMYK, Pantone), and correct/incorrect usage examples."),
            ("🖼️", "Mockup Presentations", "Realistic mockup previews showing your logo on business cards, signage, website header, social media profiles, and branded merchandise."),
            ("©️", "Full IP Transfer", "All rights to the final logo transferred to you in writing — you own the design completely. Source files included for future use with any designer."),
        ],
        "process": [
            ("🔍", "Brand Discovery", "We conduct a brand questionnaire covering your values, audience, competitors, and aesthetic preferences. We build a moodboard for visual alignment before any design work begins."),
            ("✏️", "Concept Development", "Our designers explore 5–8 rough directions, distill them to the 3 strongest, and present them with strategic context explaining why each fits your brand positioning."),
            ("🔄", "Refine & Perfect", "You choose your preferred direction and we refine it through up to 2 revision rounds — adjusting color, proportion, weight, and typography until you're 100% satisfied."),
            ("📁", "Final Delivery", "We prepare and deliver the complete file package, brand usage guide, and all mockups. Source files and IP transfer documentation are included."),
        ],
        "faqs": [
            ("How many logo concepts will I see?", "You receive 3 fully developed logo concepts. Each concept represents a distinct design direction — not minor variations. You choose the one to move forward with."),
            ("What file formats are included?", "You receive SVG (scalable vector), PNG (transparent background, multiple sizes), PDF (print-ready vector), and JPG. All versions include color, white, and black variants."),
            ("Do you have experience in my industry?", "We've designed logos across SaaS, healthcare, finance, retail, food & beverage, professional services, and more. Our discovery process adapts to any industry's visual conventions and audience expectations."),
            ("What if I don't like any of the concepts?", "This is rare — our discovery process typically surfaces strong direction before design begins. If none of the 3 concepts resonate, we provide an additional concept round at a reduced rate."),
            ("Can you redesign my existing logo?", "Yes — we offer logo refinement (modernizing an existing logo while preserving equity) or full redesign. We'll recommend the right approach based on your current logo's strengths and weaknesses."),
        ],
        "schema_service_desc": "Professional logo design — 3 original concepts, 2 revision rounds, complete file package (SVG, PNG, PDF), brand usage guide, and full IP transfer.",
    },
    "graphic-design": {
        "title": "Graphic Design",
        "tagline": "On-brand visuals for every channel — from ads to presentations to print",
        "desc": "Consistent, professional graphic design builds brand trust and drives conversion. We provide on-demand graphic design for digital ads, social media content, email templates, print collateral, presentations, and more — all aligned to your brand identity and optimized for each channel.",
        "price": "$1,500/mo",
        "stat1": "94%",
        "stat1_label": "of first impressions are design-related",
        "stat2": "3x",
        "stat2_label": "more engagement for branded visual content",
        "stat3": "60s",
        "stat3_label": "average time users spend on a well-designed page",
        "deliverables": [
            ("📱", "Social Media Graphics", "Branded templates and custom graphics for Instagram, LinkedIn, Facebook, and X — posts, stories, reels covers, and profile assets."),
            ("🎯", "Digital Ad Creative", "Static and animated ad creatives for Google Display, Meta Ads, LinkedIn Ads, and programmatic — in all required sizes and formats."),
            ("📧", "Email Design Templates", "Custom HTML email templates for newsletters, promotional campaigns, onboarding sequences, and transactional emails — coded for all major email clients."),
            ("📄", "Print Collateral", "Business cards, brochures, flyers, banners, trade show materials, and direct mail — designed to print-ready specifications with bleed and crop marks."),
            ("📊", "Presentations & Decks", "Branded PowerPoint and Google Slides templates, investor decks, sales presentations, and webinar slides — designed to communicate and persuade."),
            ("🖼️", "Infographics", "Data-driven and editorial infographics that simplify complex information into shareable visual content for web, social, and press use."),
            ("🔄", "Brand Asset Management", "Organization of all design assets in a shared library — logos, colors, fonts, templates, and icons — for consistent use across your team."),
        ],
        "process": [
            ("🔍", "Brand Intake & Asset Audit", "We review your existing brand guidelines, asset library, and design history to establish a baseline and identify gaps or inconsistencies."),
            ("📋", "Monthly Brief & Prioritization", "At the start of each month, we agree on the design deliverables priority list — balancing campaign needs, deadlines, and strategic initiatives."),
            ("🎨", "Design & Collaboration", "Designs are delivered via shared Figma workspace. You review, comment, and request revisions directly in the tool — streamlined feedback loop."),
            ("📁", "Delivery & Handoff", "Production-ready files delivered in all required formats. We maintain a version-controlled asset library so nothing is ever lost."),
        ],
        "faqs": [
            ("What's included in the monthly retainer?", "The retainer covers a defined number of design hours (typically 20–40 hours/month). We agree on deliverables at the start of each month based on your campaigns and priorities. Rush requests can be accommodated within the monthly allocation."),
            ("Do you work in our brand guidelines?", "Yes — we follow your existing brand guidelines precisely. If guidelines don't exist, we can document them as part of our engagement."),
            ("What design tools do you use?", "We work in Figma (primary), Adobe Creative Suite (Photoshop, Illustrator, InDesign), and Canva if needed. All source files are delivered in your preferred format."),
            ("How fast can you turn around designs?", "Standard turnaround is 2–3 business days for simple assets, 3–5 days for complex designs. Rush 24-hour turnarounds are available for critical campaign assets."),
            ("Do you create animated graphics?", "Yes — we create GIF animations, HTML5 banner ads (for Google Display), and Lottie animations for web use. Video-based motion graphics are available as an add-on."),
        ],
        "schema_service_desc": "Graphic design retainer — social media graphics, digital ad creative, email templates, print collateral, presentations, and infographics on monthly retainer.",
    },
    "social-media-design": {
        "title": "Social Media Design",
        "tagline": "Scroll-stopping visuals that build brand equity and drive engagement",
        "desc": "Social media is a visual medium — and inconsistent, generic visuals destroy brand credibility. We design a cohesive social media visual system for your brand: custom templates, feed aesthetics, story formats, and campaign-specific creative that stops the scroll and communicates your brand personality.",
        "price": "$1,200/mo",
        "stat1": "4.8B",
        "stat1_label": "active social media users worldwide",
        "stat2": "6x",
        "stat2_label": "higher conversion with consistent visual branding",
        "stat3": "65%",
        "stat3_label": "of people are visual learners — visuals drive decisions",
        "deliverables": [
            ("🎨", "Social Media Visual System", "A complete visual design system for your brand's social presence — color palette, typography, graphic elements, image treatment style, and layout grid for each platform."),
            ("📐", "Custom Template Library", "20–40 branded Canva or Figma templates covering post types: educational carousels, product spotlights, testimonials, announcements, events, and behind-the-scenes."),
            ("📱", "Platform-Specific Formats", "Correctly sized and optimized designs for Instagram (1:1, 4:5, 9:16), LinkedIn (1.91:1, 1:1), Facebook (1:1, 16:9), X (16:9), TikTok (9:16), and Pinterest (2:3)."),
            ("✨", "Campaign Creative Packages", "Custom-designed graphics for product launches, seasonal campaigns, promotions, and events — aligned to campaign goals and brand visual identity."),
            ("📊", "Carousel & Story Design", "Multi-slide carousel designs with narrative flow, branded story sequences, and highlight cover icons for Instagram and Facebook."),
            ("🎬", "Static Ad Creative", "High-performing static ad creative designed for paid social campaigns — optimized for thumb-stop power, clear value proposition, and platform ad specs."),
            ("📅", "Monthly Content Calendar Design", "Design coordination with your content team — we receive the content calendar and produce matching visual assets on a defined delivery schedule."),
        ],
        "process": [
            ("🔍", "Brand & Platform Audit", "We analyze your current social presence, identify inconsistencies, review top-performing competitors, and document what visual elements resonate with your target audience."),
            ("🎨", "Visual System Development", "We develop your social media visual identity — a dedicated design system separate from (but aligned to) your main brand guidelines, built for social media's unique constraints."),
            ("📐", "Template Library Build", "We create your full template library in Canva or Figma — ready to use by your team or us. Each template is editable and labeled clearly."),
            ("🔄", "Ongoing Production", "Monthly design production aligned to your content calendar. Weekly delivery batches with revision rounds. Quarterly visual refresh to keep the aesthetic fresh."),
        ],
        "faqs": [
            ("Do you design for all social platforms?", "Yes — we design for Instagram, LinkedIn, Facebook, X (Twitter), TikTok, Pinterest, and YouTube channel art. We prioritize platforms based on your audience and business goals."),
            ("Can our team use the templates you create?", "Absolutely. All templates are delivered in Canva or Figma — whichever your team prefers. We provide a brief training session to ensure your team can update templates independently."),
            ("Do you also write the captions?", "Our social media design service covers visual design only. We can pair it with our Content Marketing or Social Media Management service if you need copy and strategy as well."),
            ("How many designs do we get per month?", "The retainer includes 20–30 individual design assets per month (posts, stories, carousels). We agree on the split based on your content calendar at the start of each month."),
            ("Can you match an aesthetic we show you?", "Yes — show us reference accounts or mood boards and we'll align your visual system to that direction while ensuring it reflects your unique brand identity."),
        ],
        "schema_service_desc": "Social media design — visual system development, custom template library, platform-specific formats, campaign creative, and ongoing monthly design production.",
    },
    "pitch-deck-design": {
        "title": "Pitch Deck Design",
        "tagline": "Investor-ready pitch decks that tell your story and close rounds",
        "desc": "A great pitch deck can be the difference between a term sheet and a pass. We design compelling, investor-ready pitch decks — structuring your narrative, visualizing your data, and presenting your business in the clearest and most persuasive way possible. Built for seed through Series B fundraising.",
        "price": "$2,500",
        "stat1": "$300B+",
        "stat1_label": "raised globally by startups annually",
        "stat2": "3min",
        "stat2_label": "average time investors spend reviewing a deck",
        "stat3": "10–15",
        "stat3_label": "slides — the optimal pitch deck length",
        "deliverables": [
            ("📊", "Narrative & Structure Consulting", "We workshop your story with you — problem, solution, market, product, traction, team, ask — and structure your narrative for maximum investor clarity and emotional pull."),
            ("🎨", "Custom Visual Design", "Bespoke slide design — not a template. Every slide is designed to guide investor attention, communicate clearly, and reflect your brand's visual identity and ambition."),
            ("📈", "Data Visualization", "Charts, graphs, market maps, and financial projections designed for clarity — we make your data tell a story rather than just display numbers."),
            ("🖼️", "Competitive Positioning Maps", "Magic quadrant-style competitive landscape maps, comparison tables, and positioning matrices that clearly establish your differentiated position."),
            ("📝", "Speaker Notes", "Concise speaker notes for every slide — ensuring you can deliver the pitch confidently without reading from the deck."),
            ("🖥️", "Multiple Format Delivery", "Delivered in PowerPoint (.pptx), Google Slides (shared link), and PDF — plus a PDF teaser version (5–7 slides) optimized for email pitching before meetings."),
            ("🔄", "2 Revision Rounds", "Two full revision rounds post-initial delivery — covering content changes, data updates, and design refinements until the deck is exactly right."),
        ],
        "process": [
            ("🔍", "Narrative Workshop", "We conduct a 60–90 minute strategy session to extract your story, understand your round goals, define your ideal investor archetype, and map the key narrative beats."),
            ("📋", "Content Outline & Approval", "We draft the deck outline — slide titles, key points, data needed per slide — and present it for your review before any design begins."),
            ("🎨", "Design & Build", "We design and build all slides, integrating your data, visuals, and narrative. A draft is delivered within 5–7 business days for your initial review."),
            ("🔄", "Refine & Finalize", "Two revision rounds to tighten messaging, update data, and perfect the visual execution. Final files delivered in all formats with speaker notes."),
        ],
        "faqs": [
            ("How many slides should a pitch deck have?", "10–15 slides is the sweet spot for a seed to Series B deck. We cover: problem, solution, market size, product, business model, traction, team, roadmap, competitive landscape, and the ask."),
            ("Do you help with the content, or just design?", "Both. We consult on narrative structure and slide content strategy — not just design. You'll leave with a stronger story, not just prettier slides."),
            ("How long does a pitch deck take?", "From kickoff to final delivery: 7–10 business days. Rush turnaround (5 business days) is available at an additional fee."),
            ("Can you update an existing deck?", "Yes — we offer redesigns of existing decks. We'll restructure narrative and completely rebuild the visual design. Pricing for redesigns is the same as a new deck."),
            ("Do you have experience with specific industries?", "We've built decks for SaaS, fintech, healthtech, consumer, marketplace, and deep tech startups — and understand what investors in each category want to see."),
        ],
        "schema_service_desc": "Pitch deck design — narrative consulting, custom slide design, data visualization, competitive maps, PowerPoint/Google Slides/PDF delivery, and 2 revision rounds.",
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
            <li><a href="../services/mobile-app-development.html">Mobile App Dev</a></li>
            <li><a href="../services/logo-design.html">Logo Design</a></li>
            <li><a href="../services/graphic-design.html">Graphic Design</a></li>
            <li><a href="../services/social-media-design.html">Social Media Design</a></li>
            <li><a href="../services/pitch-deck-design.html">Pitch Deck Design</a></li>
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
                "provider": {
                    "@type": "Organization",
                    "name": "Lumo AI Agency",
                    "url": "https://lumoaiagency.com",
                },
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
    /* NAV */
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
    /* HERO */
    .hero{{padding:140px 24px 80px;text-align:center;background:radial-gradient(ellipse 80% 60% at 50% 0%,rgba(124,58,237,.15),transparent)}}
    .hero-eyebrow{{display:inline-block;background:rgba(179,255,0,.1);color:var(--primary);border:1px solid rgba(179,255,0,.3);border-radius:100px;padding:6px 18px;font-size:.85rem;font-weight:600;margin-bottom:24px}}
    .hero h1{{font-family:'Syne',sans-serif;font-size:clamp(2.2rem,5vw,3.6rem);font-weight:800;line-height:1.1;margin-bottom:20px}}
    .hero h1 span{{color:var(--primary)}}
    .hero-sub{{font-size:1.1rem;color:var(--muted);max-width:620px;margin:0 auto 36px}}
    .hero-actions{{display:flex;gap:16px;justify-content:center;flex-wrap:wrap}}
    .btn-primary{{background:var(--primary);color:#0D0D14;padding:14px 32px;border-radius:10px;font-weight:700;font-size:1rem;transition:opacity .2s}}.btn-primary:hover{{opacity:.85}}
    .btn-secondary{{border:1px solid var(--border);color:#fff;padding:14px 32px;border-radius:10px;font-weight:600;font-size:1rem;transition:border-color .2s}}.btn-secondary:hover{{border-color:var(--primary)}}
    /* STATS */
    .stats-strip{{background:var(--surface);border-top:1px solid var(--border);border-bottom:1px solid var(--border);padding:40px 24px}}
    .stats-inner{{max-width:900px;margin:0 auto;display:grid;grid-template-columns:repeat(3,1fr);gap:24px;text-align:center}}
    .stat-val{{font-family:'Syne',sans-serif;font-size:2.4rem;font-weight:800;color:var(--primary)}}
    .stat-lbl{{font-size:.85rem;color:var(--muted);margin-top:4px}}
    /* SECTIONS */
    section{{padding:80px 24px}}
    .section-inner{{max-width:1180px;margin:0 auto}}
    .section-label{{font-size:.8rem;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--primary);margin-bottom:12px}}
    .section-title{{font-family:'Syne',sans-serif;font-size:clamp(1.8rem,3.5vw,2.6rem);font-weight:800;margin-bottom:16px}}
    .section-sub{{color:var(--muted);max-width:640px;margin-bottom:48px}}
    /* SERVICES GRID */
    .services-grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:24px}}
    .service-card{{background:var(--surface);border:1px solid var(--border);border-radius:16px;padding:28px;transition:border-color .2s}}.service-card:hover{{border-color:rgba(179,255,0,.35)}}
    .service-icon{{font-size:2rem;margin-bottom:14px}}
    .service-card h3{{font-family:'Syne',sans-serif;font-size:1.15rem;font-weight:700;margin-bottom:8px}}
    .service-card p{{color:var(--muted);font-size:.9rem;line-height:1.6}}
    /* PROCESS */
    .process-grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:24px}}
    .process-step{{background:var(--surface);border:1px solid var(--border);border-radius:16px;padding:28px;position:relative}}
    .step-number{{font-family:'Syne',sans-serif;font-size:2.5rem;font-weight:800;color:rgba(179,255,0,.15);position:absolute;top:20px;right:20px}}
    .step-icon{{font-size:1.8rem;margin-bottom:12px}}
    .process-step h3{{font-family:'Syne',sans-serif;font-size:1.05rem;font-weight:700;margin-bottom:8px}}
    .process-step p{{color:var(--muted);font-size:.88rem;line-height:1.6}}
    /* PRICING */
    .pricing-box{{background:var(--surface);border:1px solid rgba(179,255,0,.3);border-radius:20px;padding:48px;max-width:600px;margin:0 auto;text-align:center}}
    .price-label{{font-size:.85rem;color:var(--muted);margin-bottom:8px}}
    .price-val{{font-family:'Syne',sans-serif;font-size:3rem;font-weight:800;color:var(--primary);margin-bottom:8px}}
    .price-note{{font-size:.9rem;color:var(--muted);margin-bottom:32px}}
    /* FAQ */
    .faq-list{{max-width:780px;margin:0 auto;display:flex;flex-direction:column;gap:12px}}
    .faq-item{{background:var(--surface);border:1px solid var(--border);border-radius:12px;overflow:hidden}}
    .faq-q{{width:100%;background:none;border:none;color:#fff;font-family:'Inter',sans-serif;font-size:1rem;font-weight:600;text-align:left;padding:20px 24px;cursor:pointer;display:flex;justify-content:space-between;align-items:center;gap:12px}}
    .faq-arrow{{color:var(--primary);transition:transform .3s;flex-shrink:0}}
    .faq-q[aria-expanded="true"] .faq-arrow{{transform:rotate(180deg)}}
    .faq-a{{max-height:0;overflow:hidden;transition:max-height .3s ease}}
    .faq-a p{{padding:0 24px 20px;color:var(--muted);font-size:.95rem;line-height:1.7}}
    /* CTA */
    .cta-section{{background:linear-gradient(135deg,rgba(124,58,237,.2),rgba(179,255,0,.08));border-top:1px solid var(--border);border-bottom:1px solid var(--border);text-align:center;padding:80px 24px}}
    .cta-section h2{{font-family:'Syne',sans-serif;font-size:clamp(1.8rem,3.5vw,2.8rem);font-weight:800;margin-bottom:16px}}
    .cta-section p{{color:var(--muted);margin-bottom:36px;max-width:540px;margin-left:auto;margin-right:auto}}
    /* FOOTER */
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
