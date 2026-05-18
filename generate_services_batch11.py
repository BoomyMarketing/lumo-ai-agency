"""Batch 11 — Backlog Batch 6: blog-writing, video-marketing, infographic-design, performance-creative, podcast-marketing"""
import json, os

SERVICES = {
    "blog-writing": {
        "title": "Blog Writing",
        "tagline": "SEO-optimized blog content that ranks, educates, and converts",
        "desc": "We produce high-quality, SEO-driven blog content that builds topical authority, attracts organic traffic, and moves readers through your funnel. Every article is researched, strategically structured, and written by subject-matter experts — then optimized for target keywords, internal linking, and conversion before publication.",
        "price": "$2,000/mo",
        "stat1": "77%",
        "stat1_label": "of internet users regularly read blog content",
        "stat2": "6x",
        "stat2_label": "more leads for companies that blog consistently",
        "stat3": "434%",
        "stat3_label": "more indexed pages for sites with active blogs",
        "deliverables": [
            ("🔍", "Keyword & Topic Research", "We identify high-value keywords and content gaps using SEMrush and Ahrefs — mapping every article to a target keyword cluster with defined search intent and realistic ranking potential."),
            ("✍️", "Expert Article Writing", "Long-form articles (1,500–3,500 words) written by industry-specialized writers with genuine subject-matter expertise — not generalist copywriters or AI-only output."),
            ("📐", "SEO Optimization", "On-page optimization for every post: target keyword placement, semantic LSI terms, meta title and description, header hierarchy, image alt text, and internal link recommendations."),
            ("🔗", "Internal Linking Strategy", "Strategic internal links woven into each post — connecting to relevant service pages, related articles, and conversion pages to distribute link equity and reduce bounce rate."),
            ("🎨", "Content Formatting & Design", "Reader-friendly formatting: clear H2/H3 hierarchy, bullet points, callout boxes, stat highlights, and visual break suggestions for your design team or CMS."),
            ("📊", "Performance Tracking", "Monthly reporting on organic traffic, keyword rankings, and engagement for every published post — with recommendations for refreshing underperforming content."),
            ("📅", "Editorial Calendar", "A 3-month rolling editorial calendar aligned to your marketing campaigns, seasonal trends, and content funnel stage — so you always know what's coming."),
        ],
        "process": [
            ("🔍", "Content Audit & Strategy", "We audit your existing content, identify keyword gaps, and build a content strategy aligned to your SEO goals and buyer journey — before writing a single word."),
            ("📋", "Brief & Outline Approval", "Every article starts with a detailed brief: target keyword, search intent, outline, key points, and internal link targets. You approve before writing begins."),
            ("✍️", "Writing & Optimization", "Our writers produce the draft; our SEO team optimizes it. You receive a polished, formatted article with all SEO elements in place — ready to publish."),
            ("📈", "Publish, Track & Iterate", "We track rankings and traffic for every post and flag opportunities to update, expand, or consolidate content to maximize long-term organic performance."),
        ],
        "faqs": [
            ("How many articles do we get per month?", "The standard retainer includes 4–8 articles per month depending on length and complexity. We agree on the mix upfront based on your content strategy priorities."),
            ("Do you write in our brand voice?", "Yes — we conduct a voice and tone intake session at the start of the engagement and develop a style guide that all writers follow. Existing content is reviewed to match your established voice."),
            ("Is the content AI-generated?", "We use AI tools for research assistance and initial drafts, but every article is written and substantially edited by human subject-matter experts. We do not publish raw AI output."),
            ("How long until we see results?", "Blog SEO is a 3–6 month investment. New content typically begins ranking within 3–4 months for medium-competition keywords. High-competition keywords may take 6–12 months."),
            ("Can you write for technical or specialized industries?", "Yes — we have writers with backgrounds in SaaS, fintech, healthcare, legal, e-commerce, and B2B technology. We match writers to industries based on expertise."),
        ],
        "schema_service_desc": "Blog writing service — SEO-optimized articles, keyword research, expert writers, on-page optimization, editorial calendar, and monthly performance tracking.",
    },
    "video-marketing": {
        "title": "Video Marketing",
        "tagline": "Video content strategy that engages audiences and drives measurable ROI",
        "desc": "Video is the highest-engagement content format across every platform — and most brands still treat it as an afterthought. We build end-to-end video marketing programs: strategy, scripting, production coordination, editing, platform optimization, and distribution. From YouTube long-form to TikTok shorts to LinkedIn thought leadership, we turn video into a growth channel.",
        "price": "$3,500/mo",
        "stat1": "91%",
        "stat1_label": "of consumers want to see more brand video content",
        "stat2": "2x",
        "stat2_label": "higher conversion rates with video on landing pages",
        "stat3": "88%",
        "stat3_label": "more time spent on pages with video content",
        "deliverables": [
            ("🎬", "Video Content Strategy", "A platform-specific video strategy aligned to your funnel — mapping content types (awareness, education, conversion, retention) to the right platforms, formats, and distribution cadence."),
            ("📝", "Script & Storyboard", "Professional scriptwriting and storyboarding for every video — structured for viewer retention, SEO (YouTube), and platform-specific best practices."),
            ("🎞️", "Video Production Coordination", "We coordinate filming logistics, talent briefing, b-roll direction, and on-camera coaching — whether you have an in-house team or need our production partners."),
            ("✂️", "Editing & Post-Production", "Professional video editing with motion graphics, captions, brand intros/outros, color grading, and audio mixing — optimized for each platform's technical requirements."),
            ("📱", "Multi-Platform Reformatting", "Each video reformatted for every target platform: YouTube (16:9), TikTok/Reels/Shorts (9:16), LinkedIn (1:1), and website embed — all with platform-specific optimization."),
            ("🔍", "YouTube SEO", "Full YouTube optimization: keyword-researched titles, descriptions, tags, chapters, end screens, cards, and thumbnail A/B testing to maximize views and subscriber growth."),
            ("📊", "Analytics & Reporting", "Monthly reporting on views, watch time, click-through rate, subscriber growth, and video-attributed conversions — with recommendations for improving performance."),
        ],
        "process": [
            ("🔍", "Strategy & Audit", "We audit your current video presence, benchmark competitors, and build a platform-specific video strategy with content pillars, posting cadence, and production workflow."),
            ("📝", "Script & Pre-Production", "Scripts and storyboards developed for approval before any production begins. We handle talent briefs, shot lists, and location coordination."),
            ("🎬", "Production & Post", "Filming coordination and professional post-production: editing, motion graphics, captions, and platform-specific formatting. Delivered on schedule."),
            ("📈", "Distribute & Optimize", "Strategic publishing across platforms with full metadata optimization. We monitor performance and iterate on content strategy based on what's driving views and conversions."),
        ],
        "faqs": [
            ("Do you handle filming or just editing?", "We offer both. For clients with in-house teams, we provide strategy, scripting, and post-production. For clients needing full production, we coordinate our network of videographers and production crews across the US."),
            ("How many videos do we get per month?", "The retainer typically covers 4–8 videos per month depending on length and production complexity. We agree on the content mix (long-form, short-form, testimonials, ads) based on your strategy."),
            ("Which platforms do you focus on?", "We prioritize based on your audience: YouTube for long-form and search, TikTok/Reels for awareness and reach, LinkedIn for B2B thought leadership. We advise on the best platform mix for your goals."),
            ("Do you create video ads as well as organic content?", "Yes — we produce both organic video content and paid video ad creative. Paid video ads follow a different structure (hook, value prop, CTA) and we optimize them for platform ad policies."),
            ("Can you work with existing footage we have?", "Absolutely. We can edit and repurpose existing raw footage, interviews, webinar recordings, or event content into polished videos optimized for each platform."),
        ],
        "schema_service_desc": "Video marketing service — content strategy, scriptwriting, production coordination, editing, YouTube SEO, multi-platform distribution, and performance analytics.",
    },
    "infographic-design": {
        "title": "Infographic Design",
        "tagline": "Data-driven infographics that earn links, shares, and traffic",
        "desc": "Infographics are one of the highest-ROI content formats for link building, social sharing, and simplifying complex information. We research, design, and distribute data-driven infographics that your audience actually wants to share — generating backlinks, social engagement, and brand awareness at scale.",
        "price": "$1,500",
        "stat1": "3x",
        "stat1_label": "more engagement than text-only content",
        "stat2": "94%",
        "stat2_label": "more views for content with compelling visuals",
        "stat3": "40x",
        "stat3_label": "more likely to be shared on social media vs. plain text",
        "deliverables": [
            ("🔍", "Research & Data Sourcing", "We identify compelling data points, statistics, and insights from credible primary sources — government data, academic research, industry reports — and fact-check everything before design begins."),
            ("📐", "Concept & Structure", "We develop the narrative structure and visual hierarchy: what story the infographic tells, how data flows, where the eye goes first, and how to guide readers to the key insight."),
            ("🎨", "Custom Infographic Design", "100% custom design — no templates. Fully branded to your visual identity with consistent typography, color palette, icons, and illustrations."),
            ("📏", "Multiple Format Delivery", "Delivered in full-width web version (800px wide), tall vertical (Pinterest/social-optimized), square format, and print-ready PDF — all in SVG and PNG."),
            ("📝", "Companion Blog Post", "A 500–800 word blog post that contextualizes the infographic, embeds it, and is SEO-optimized for related keywords — driving organic discovery."),
            ("🔗", "Embed Code Creation", "A ready-to-use embed code for publishers and bloggers to feature your infographic on their sites — complete with attribution link back to your domain for passive link building."),
            ("📣", "Outreach Asset Package", "A curated outreach target list (journalists, bloggers, industry publications) and a pitch email template optimized for infographic placement and link acquisition."),
        ],
        "process": [
            ("🔍", "Data & Concept Development", "We research primary data sources and develop 2–3 concept directions — each with a different angle on the topic. You select the direction to move forward."),
            ("📐", "Structure & Wireframe", "We wireframe the infographic — showing the data flow, visual hierarchy, and narrative structure — before any final design work begins."),
            ("🎨", "Design & Refinement", "Full infographic designed to brand standards, delivered for your review. One round of revisions included to refine data presentation, colors, or content."),
            ("📣", "Delivery & Distribution", "Final files and embed code delivered. Companion blog post published. Outreach list and pitch template provided for your link building campaign."),
        ],
        "faqs": [
            ("What types of infographics do you create?", "We create statistical infographics (data visualization), process infographics (step-by-step guides), comparison infographics (vs. tables), timeline infographics, geographic infographics (maps), and list-style infographics. We recommend the format based on your data and goals."),
            ("Can you create an infographic from our data?", "Yes — if you have proprietary data (survey results, customer data, internal research), we can visualize it. Proprietary data infographics often earn the most links since the data isn't available elsewhere."),
            ("How long does an infographic take?", "From brief to final delivery: 7–10 business days. Rush production (5 business days) is available at an additional fee."),
            ("Do you handle the link building outreach?", "We provide the outreach asset package (target list + pitch template). Active outreach execution is available as an add-on or through our Link Building service."),
            ("Can you animate the infographic?", "Yes — we offer animated infographic versions (GIF or HTML5) optimized for social media and web use. Animation is quoted separately based on complexity."),
        ],
        "schema_service_desc": "Infographic design — data research, custom design, multiple format delivery, companion blog post, embed code, and outreach package for link building.",
    },
    "performance-creative": {
        "title": "Performance Creative",
        "tagline": "Ad creative engineered for clicks, conversions, and ROAS — not just aesthetics",
        "desc": "Most agencies separate creative and media buying — and both suffer for it. Our performance creative team designs ad creative with the media buying strategy baked in: thumb-stopping hooks, clear value propositions, and CTAs designed for the specific platform, audience, and funnel stage. We test, learn, and iterate at scale.",
        "price": "$2,500/mo",
        "stat1": "70%",
        "stat1_label": "of campaign performance is determined by creative quality",
        "stat2": "3–5x",
        "stat2_label": "ROAS improvement from systematic creative testing",
        "stat3": "14",
        "stat3_label": "creative variations tested per month on average",
        "deliverables": [
            ("🎯", "Creative Strategy & Brief", "A data-driven creative strategy built on audience research, competitive creative analysis, and performance data from your existing campaigns — identifying the angles, hooks, and formats most likely to perform."),
            ("🖼️", "Static Ad Creative", "High-converting static image ads for Meta, Google Display, LinkedIn, and programmatic — designed with proven direct-response principles: strong visual hook, benefit-led headline, clear CTA."),
            ("🎬", "Video Ad Creative", "Short-form video ads (6–30 seconds) optimized for scroll-stop performance: pattern-interrupt openers, rapid value delivery, and platform-native formats (Reels, TikTok, YouTube pre-roll)."),
            ("📝", "Ad Copy Variants", "Multiple copy variants per creative — testing different hooks, headlines, CTAs, and value proposition angles — giving your media buyer meaningful variables to test systematically."),
            ("🔄", "Creative Testing Framework", "A structured A/B and multivariate testing framework: what to test, in what order, with what budget thresholds, and how to interpret results to inform the next creative iteration."),
            ("📊", "Performance Analysis", "Bi-weekly creative performance reporting: CTR, CPM, CPC, conversion rate, and ROAS by creative — with clear recommendations on what to scale, pause, or iterate."),
            ("⚡", "Rapid Iteration Cycles", "Bi-weekly creative refresh cycles so your ads don't fatigue. We produce new variants based on performance data — not guesswork — keeping your account fresh and performing."),
        ],
        "process": [
            ("🔍", "Creative Audit & Research", "We audit your existing creative, analyze competitor ads, and review your campaign data to identify what's working, what isn't, and what we should test first."),
            ("📋", "Strategy & Brief", "We develop a 90-day creative roadmap: priority angles, ad formats, testing sequence, and production schedule. You review and approve the strategy before production begins."),
            ("🎨", "Production & Launch", "Creative designed, copy written, and assets delivered in all required sizes and formats. We coordinate directly with your media buyer or manage the account ourselves."),
            ("📈", "Analyze & Iterate", "Performance data reviewed bi-weekly. Winning creatives scaled; underperformers paused. New variants developed based on learnings — continuous improvement baked into the retainer."),
        ],
        "faqs": [
            ("Do you also run the ads, or just make the creative?", "We specialize in creative production and strategy. We can deliver assets to your in-house media buyer or partner agency, or we can manage the full campaign if you use our paid advertising services."),
            ("How many creative assets do we get per month?", "The retainer includes 10–20 individual creative assets per month (a mix of static, video, and copy variants). Volume is calibrated to your testing velocity and budget."),
            ("What platforms do you design for?", "Meta (Facebook/Instagram), TikTok, LinkedIn, YouTube, Google Display, and programmatic. Each platform has specific sizing, format, and content guidelines we follow precisely."),
            ("How do you measure creative performance?", "We track thumb-stop rate (3-second video views), CTR, CPM, CPC, ROAS, and creative-level conversion rate. We provide a bi-weekly dashboard breaking down performance by creative variant."),
            ("What if our creatives aren't performing?", "Underperformance is a data signal, not a failure. We analyze why (audience mismatch, wrong hook, offer clarity) and pivot the creative strategy accordingly. Our retainer is built around iteration."),
        ],
        "schema_service_desc": "Performance creative service — ad creative strategy, static and video ad production, copy variants, creative testing framework, and bi-weekly performance optimization.",
    },
    "podcast-marketing": {
        "title": "Podcast Marketing",
        "tagline": "Podcast launch, production, and growth strategy for B2B and consumer brands",
        "desc": "Podcasts are one of the most powerful trust-building channels available — 80% of listeners finish episodes they start. We help brands launch, produce, and grow podcasts that build genuine audience relationships, establish thought leadership, and generate qualified pipeline. From concept to episode to distribution, we handle everything.",
        "price": "$2,500/mo",
        "stat1": "80%",
        "stat1_label": "of podcast listeners hear every episode they start",
        "stat2": "54%",
        "stat2_label": "of podcast listeners more likely to buy from advertisers",
        "stat3": "464M",
        "stat3_label": "podcast listeners globally in 2023",
        "deliverables": [
            ("🎙️", "Podcast Strategy & Format", "We define your podcast concept, target audience, episode format (interview, solo, narrative, panel), episode length, publishing cadence, and positioning relative to competing shows in your category."),
            ("🎚️", "Audio Production & Editing", "Professional audio editing for every episode: noise removal, EQ and compression, music intro/outro, chapter markers, and export in all required formats (MP3, AAC) for every major platform."),
            ("📝", "Show Notes & Transcripts", "SEO-optimized show notes for every episode — guest bios, key takeaways, resource links, and timestamps — plus full episode transcripts for accessibility and search indexing."),
            ("📣", "Multi-Platform Distribution", "Automated distribution to Spotify, Apple Podcasts, Google Podcasts, Amazon Music, Stitcher, and 10+ additional platforms via your RSS feed — so every episode appears everywhere simultaneously."),
            ("🎬", "Video Podcast Repurposing", "Episode repurposed into: full-length YouTube video, 3–5 short clips (Reels/TikTok/Shorts), audiogram for social media, and pull-quote graphics — maximizing reach from each recording."),
            ("📈", "Growth Strategy", "Guest booking strategy (for interview shows), listener acquisition campaigns, cross-promotion partnerships, podcast SEO, and Spotify/Apple Podcasts profile optimization."),
            ("📊", "Analytics & Reporting", "Monthly reporting on downloads, listener retention, episode performance, and platform growth — with episode-level recommendations to improve content and audience engagement."),
        ],
        "process": [
            ("🔍", "Concept & Launch Planning", "We define your show concept, target listener persona, competitive positioning, and production workflow. We handle RSS setup, hosting configuration, and platform submission."),
            ("🎙️", "Production & Launch", "First 3 episodes produced simultaneously for a strong launch (Apple Podcasts ranks shows higher with multiple episodes). We coordinate recording logistics and complete all post-production."),
            ("📣", "Distribution & Promotion", "Launch promotion across your existing channels, listener acquisition campaigns, and outreach to relevant podcast communities and directories for placement and cross-promotion."),
            ("📈", "Grow & Optimize", "Ongoing production, guest booking, listener growth campaigns, and performance optimization. Monthly strategy reviews to refine content based on what's resonating with your audience."),
        ],
        "faqs": [
            ("Do I need any recording equipment?", "For remote interview shows, a quality USB microphone ($100–200) and a quiet recording space is sufficient. We recommend specific equipment based on your budget. For in-studio production, we can coordinate local production resources."),
            ("How many episodes per month?", "Most B2B podcasts publish 2–4 episodes per month. We'll recommend a cadence based on your content goals and internal capacity for guest sourcing or solo recording."),
            ("How long until the podcast starts generating leads?", "Podcasts are a long-term authority channel. Most shows see meaningful listener growth by month 3–6. Pipeline attribution typically appears at 6–12 months as the audience builds trust and acts."),
            ("Can you help book podcast guests?", "Yes — guest booking is included in our growth strategy. We identify relevant guests based on your target audience and handle outreach, scheduling, and pre-interview briefing."),
            ("Can you start a podcast if we have no audience?", "Absolutely. Many of our most successful podcast clients started with zero listeners. We build the audience through distribution optimization, SEO, cross-promotion, and your existing email and social channels."),
        ],
        "schema_service_desc": "Podcast marketing — strategy, audio production, show notes, multi-platform distribution, video repurposing, listener growth campaigns, and monthly analytics.",
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
            <li><a href="../services/blog-writing.html">Blog Writing</a></li>
            <li><a href="../services/video-marketing.html">Video Marketing</a></li>
            <li><a href="../services/performance-creative.html">Performance Creative</a></li>
            <li><a href="../services/podcast-marketing.html">Podcast Marketing</a></li>
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
