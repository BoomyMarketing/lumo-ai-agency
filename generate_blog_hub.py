"""
generate_blog_hub.py
Generates blog/index.html — the Lumo AI Agency blog listing hub page.
Run: python generate_blog_hub.py
"""

import os
from collections import OrderedDict

# ---------------------------------------------------------------------------
# ARTICLES list  (slug, category, cat_class, title, excerpt, date_str, read_mins)
# cat_class: "cat-ai" (lime), "cat-marketing" (violet), "cat-dev" (cyan)
# ---------------------------------------------------------------------------
ARTICLES = [
    # AI & GEO (6)
    ("what-is-geo", "AI & GEO", "cat-ai", "What Is GEO (Generative Engine Optimization)?", "GEO is the practice of making your brand visible in ChatGPT, Perplexity, and Google AI Overviews. Here's how it works and why it matters more than traditional SEO in 2026.", "May 15, 2026", 10),
    ("how-to-get-cited-in-ai-search", "AI & GEO", "cat-ai", "How to Get Your Brand Cited in ChatGPT and AI Search", "Most brands are invisible in AI-generated answers. Here's a practical framework for earning citations in ChatGPT, Perplexity, and Google AI Overviews.", "May 15, 2026", 9),
    ("ai-marketing-automations", "AI & GEO", "cat-ai", "10 AI Marketing Automations Every Business Should Build", "These 10 automation workflows eliminate repetitive marketing work, reduce costs, and scale your pipeline — without hiring more people.", "May 15, 2026", 11),
    ("voice-ai-for-business", "AI & GEO", "cat-ai", "Voice AI for Business: How AI Phone Agents Work in 2026", "AI phone agents now handle inbound calls, qualify leads, and book appointments around the clock. Here's what voice AI can and can't do.", "May 15, 2026", 8),
    ("chatgpt-vs-perplexity-vs-google", "AI & GEO", "cat-ai", "ChatGPT vs Perplexity vs Google AI Overviews: Marketer's Guide", "Three AI search platforms, three different algorithms, three different optimization strategies. Here's what you need to do to appear in all three.", "May 15, 2026", 9),
    ("ai-agency-vs-traditional", "AI & GEO", "cat-ai", "AI Marketing Agency vs Traditional Agency: The Real Difference", "Traditional agencies swap headcount for deliverables. AI agencies build systems that compound. An honest breakdown of the differences and trade-offs.", "May 15, 2026", 7),

    # SEO (7)
    ("technical-seo-checklist", "SEO", "cat-marketing", "Technical SEO Checklist 2026: 47 Checks to Audit Your Site", "A comprehensive technical SEO audit covers crawlability, indexability, Core Web Vitals, schema, and site architecture. Use this checklist to find and fix issues.", "May 15, 2026", 14),
    ("how-long-does-seo-take", "SEO", "cat-marketing", "How Long Does SEO Take? A Data-Driven Answer", "The honest answer is 4–12 months — but the range depends on domain age, competition, and execution quality. Here's what to expect at each stage.", "May 15, 2026", 7),
    ("ecommerce-seo-guide", "SEO", "cat-marketing", "E-commerce SEO Guide 2026: Shopify, WooCommerce & BigCommerce", "E-commerce SEO has unique challenges: duplicate content, thin product pages, and category cannibalisation. Here's how to solve all of them.", "May 15, 2026", 13),
    ("local-seo-guide", "SEO", "cat-marketing", "Local SEO Playbook 2026: How to Rank #1 in Google Maps", "Ranking in the local map pack requires a different playbook. Complete local SEO strategy: Google Business Profile, citations, reviews, and on-page localisation.", "May 15, 2026", 12),
    ("link-building-guide", "SEO", "cat-marketing", "Link Building in 2026: What Works and What Gets You Penalized", "The link building tactics that worked in 2020 are either commoditised or dangerous in 2026. Here's what's actually earning high-authority backlinks.", "May 15, 2026", 11),
    ("core-web-vitals-guide", "SEO", "cat-marketing", "Core Web Vitals 2026: LCP, CLS & INP Explained", "What LCP, CLS, and INP mean, how they're measured, what scores you need to rank, and the fastest ways to fix each metric.", "May 15, 2026", 10),
    ("b2b-seo-guide", "SEO", "cat-marketing", "B2B SEO Guide: How to Generate Pipeline with Search Marketing", "B2B buyers research extensively before talking to sales. How to build an SEO strategy that captures buyer intent and converts searches into demos.", "May 15, 2026", 11),

    # Paid Advertising (7)
    ("google-ads-vs-meta-ads", "Paid Ads", "cat-dev", "Google Ads vs Meta Ads: Which Is Right for Your Business?", "Google captures demand; Meta creates it. Understanding this fundamental difference is the key to allocating paid media budget intelligently.", "May 15, 2026", 9),
    ("performance-max-guide", "Paid Ads", "cat-dev", "Performance Max: Complete Setup and Optimization Guide", "Performance Max campaigns use Google's full inventory. Done right, exceptional ROAS. Done wrong, budget burn with no insight. Here's how to do it right.", "May 15, 2026", 12),
    ("tiktok-ads-guide", "Paid Ads", "cat-dev", "TikTok Ads in 2026: Complete Setup Guide for B2C Brands", "TikTok's algorithm rewards relevance over budget. How to structure creative testing and find the ad formats that drive the lowest CPAs.", "May 15, 2026", 11),
    ("linkedin-ads-guide", "Paid Ads", "cat-dev", "LinkedIn Ads for B2B: The Complete Pipeline Generation Guide", "LinkedIn is the most expensive ad platform per click — and the most effective for senior decision-makers. How to generate qualified pipeline, not just clicks.", "May 15, 2026", 12),
    ("retargeting-strategy", "Paid Ads", "cat-dev", "Retargeting Strategy: Re-Engage the 97% Who Don't Convert", "97% of visitors leave without converting. Retargeting brings them back — but only if your sequence is structured correctly.", "May 15, 2026", 9),
    ("server-side-tracking-guide", "Paid Ads", "cat-dev", "Server-Side Tracking in 2026: Setup Guide for GA4 and Meta", "Third-party cookies are dying. Server-side tracking restores signal loss — here's how to implement it for GA4 and Meta Pixel.", "May 15, 2026", 11),
    ("google-shopping-guide", "Paid Ads", "cat-dev", "Google Shopping Ads: Complete Campaign Setup Guide 2026", "Google Shopping is the highest-ROAS paid channel for e-commerce — when structured correctly. Step-by-step guide to campaign structure and feed optimisation.", "May 15, 2026", 12),

    # Content & Creative (4)
    ("content-marketing-roi", "Content", "cat-marketing", "Content Marketing ROI: How to Measure What Actually Matters", "Most teams track content metrics that feel good but don't reflect pipeline impact. How to measure content in a way that ties directly to revenue.", "May 15, 2026", 8),
    ("content-cluster-strategy", "Content", "cat-marketing", "Content Cluster Strategy: How to Build Topical Authority", "Topical authority is now the primary driver of organic growth. How to build and execute a content cluster strategy that dominates your subject area.", "May 15, 2026", 10),
    ("ugc-marketing-guide", "Content", "cat-marketing", "UGC Marketing Guide: Scale Authentic Content for Paid Ads", "User-generated content outperforms branded creative in almost every paid channel. How to source, direct, and deploy UGC at scale.", "May 15, 2026", 9),
    ("email-marketing-guide", "Content", "cat-marketing", "Email Marketing in 2026: How to Get 45%+ Open Rates", "Email is still the highest-ROI marketing channel — but only when deliverability, subject lines, and segmentation are working correctly.", "May 15, 2026", 11),

    # CRO & Analytics (4)
    ("ab-testing-guide", "CRO", "cat-ai", "A/B Testing Guide: 15 Experiments Every Website Should Run", "Most A/B tests fail — not because CRO doesn't work, but because teams test the wrong things. A prioritised framework for tests that consistently improve CVR.", "May 15, 2026", 10),
    ("landing-page-optimization", "CRO", "cat-ai", "Landing Page Optimization: 11 Elements That Move CVR", "A high-converting landing page isn't designed — it's engineered. 11 specific elements with proven impact on conversion rate, ranked by impact.", "May 15, 2026", 9),
    ("marketing-attribution-guide", "CRO", "cat-ai", "Marketing Attribution Models: Find Your True Revenue Drivers", "Last-click attribution is lying to you. How to move to multi-touch attribution and allocate budget based on true revenue contribution.", "May 15, 2026", 10),
    ("marketing-kpis", "CRO", "cat-ai", "Marketing KPIs: 25 Metrics That Actually Predict Revenue Growth", "Most dashboards measure activity, not impact. The 25 metrics that correlate most strongly with revenue, organised by funnel stage.", "May 15, 2026", 11),

    # E-commerce (2)
    ("amazon-seo-guide", "E-commerce", "cat-dev", "Amazon SEO Guide 2026: Rank Products and Win the Buy Box", "Amazon's A10 algorithm ranks listings differently from Google. How to optimise product listings, build review velocity, and dominate organic and paid Amazon results.", "May 15, 2026", 12),
    ("shopify-vs-woocommerce-seo", "E-commerce", "cat-dev", "Shopify vs WooCommerce for SEO: Which Platform Wins in 2026?", "Both platforms can rank well but have fundamentally different SEO strengths. An honest comparison to choose or migrate to the right platform.", "May 15, 2026", 10),

    # Lead Gen & Sales (2)
    ("cold-email-guide", "Lead Gen", "cat-marketing", "Cold Email in 2026: Technical Setup for Inbox Delivery", "Cold email deliverability is harder than ever — but getting it right is a significant competitive advantage. Complete technical infrastructure and sequence strategy.", "May 15, 2026", 11),
    ("outbound-sales-sequence", "Lead Gen", "cat-marketing", "Outbound Sales Sequences: 7 Frameworks That Book Meetings", "The best outbound sequences aren't the longest — they're the most relevant. 7 sequence frameworks matched to different ICPs and deal sizes.", "May 15, 2026", 10),

    # Strategy & Operations (6)
    ("competitor-analysis-framework", "Strategy", "cat-ai", "Competitor Analysis Framework for Digital Marketing", "Understanding what competitors are doing in search, paid, and content is the fastest way to find growth opportunities. A systematic framework.", "May 15, 2026", 9),
    ("revenue-operations-guide", "Strategy", "cat-ai", "RevOps: What Revenue Operations Is and Why It Drives Faster Growth", "RevOps aligns sales, marketing, and CS around a single revenue engine. What it means in practice and how to implement it.", "May 15, 2026", 9),
    ("how-to-choose-marketing-agency", "Strategy", "cat-ai", "How to Choose a Digital Marketing Agency in 2026", "Most agency evaluation processes are backwards — they measure outputs rather than fit and systems. A framework for selecting an agency that delivers.", "May 15, 2026", 8),
    ("marketing-budget-allocation", "Strategy", "cat-ai", "Marketing Budget Allocation: How to Split Your Budget Across Channels", "Budget allocation is the most consequential marketing decision — and most businesses do it based on convention rather than data.", "May 15, 2026", 8),
    ("crm-setup-guide", "Strategy", "cat-ai", "CRM Setup Guide: Build a Revenue Engine, Not a Contact List", "A poorly configured CRM creates friction for sales and obscures pipeline. How to set it up correctly from the start.", "May 15, 2026", 10),
    ("ai-consulting-what-to-expect", "Strategy", "cat-ai", "AI Consulting: What to Expect, What It Costs, How to Choose", "AI consulting ranges from a $5k opportunity assessment to a $500k multi-year implementation. How to scope, evaluate vendors, and avoid common mistakes.", "May 15, 2026", 9),
]

# ---------------------------------------------------------------------------
# Helper: group articles by category, preserving insertion order
# ---------------------------------------------------------------------------
def group_by_category(articles):
    groups = OrderedDict()
    for art in articles:
        cat = art[1]
        if cat not in groups:
            groups[cat] = []
        groups[cat].append(art)
    return groups

# ---------------------------------------------------------------------------
# Category metadata: display label, accent class, section id
# ---------------------------------------------------------------------------
CAT_META = {
    "AI & GEO":   {"label": "AI & GEO",            "cat_class": "cat-ai",        "id": "ai-geo"},
    "SEO":        {"label": "SEO",                  "cat_class": "cat-marketing", "id": "seo"},
    "Paid Ads":   {"label": "Paid Advertising",     "cat_class": "cat-dev",       "id": "paid-ads"},
    "Content":    {"label": "Content & Creative",   "cat_class": "cat-marketing", "id": "content"},
    "CRO":        {"label": "CRO & Analytics",      "cat_class": "cat-ai",        "id": "cro"},
    "E-commerce": {"label": "E-commerce",           "cat_class": "cat-dev",       "id": "ecommerce"},
    "Lead Gen":   {"label": "Lead Gen & Sales",     "cat_class": "cat-marketing", "id": "lead-gen"},
    "Strategy":   {"label": "Strategy & Operations","cat_class": "cat-ai",        "id": "strategy"},
}

# Map cat_class -> hover border/shadow colours
HOVER_COLOURS = {
    "cat-ai":        ("rgba(179,255,0,0.35)",  "rgba(179,255,0,0.1)"),
    "cat-marketing": ("rgba(124,58,237,0.45)", "rgba(124,58,237,0.15)"),
    "cat-dev":       ("rgba(0,245,255,0.35)",  "rgba(0,245,255,0.1)"),
}

# ---------------------------------------------------------------------------
# Card renderer
# ---------------------------------------------------------------------------
def render_card(slug, category, cat_class, title, excerpt, date_str, read_mins):
    return f"""        <article class="article-card {cat_class}">
          <span class="article-cat-pill {cat_class}">{category}</span>
          <h3 class="article-title">{title}</h3>
          <p class="article-excerpt">{excerpt}</p>
          <div class="article-footer">
            <div class="article-meta">{date_str} &middot; {read_mins} min read</div>
            <a href="/blog/{slug}/" class="read-link">Read Guide &rarr;</a>
          </div>
        </article>"""

# ---------------------------------------------------------------------------
# Section renderer
# ---------------------------------------------------------------------------
def render_section(cat_name, articles, first=False):
    meta = CAT_META[cat_name]
    label = meta["label"]
    cat_class = meta["cat_class"]
    sec_id = meta["id"]
    count = len(articles)
    border_top = "" if first else ' style="border-top:1px solid rgba(255,255,255,0.04);"'
    cards = "\n".join(render_card(*a) for a in articles)
    return f"""
  <section class="blog-section section-pad" id="{sec_id}" aria-labelledby="h2-{sec_id}"{border_top}>
    <div class="container">
      <div class="category-label {cat_class}">{label} &mdash; {count} guides</div>
      <h2 class="section-h2" id="h2-{sec_id}">{label}</h2>
      <div class="blog-grid">
{cards}
      </div>
    </div>
  </section>"""

# ---------------------------------------------------------------------------
# JSON-LD schema for CollectionPage
# ---------------------------------------------------------------------------
def build_schema(articles):
    items = []
    for i, (slug, cat, cat_class, title, excerpt, date_str, mins) in enumerate(articles, 1):
        items.append(
            f'    {{"@type":"ListItem","position":{i},"name":"{title}","url":"https://lumoaiagency.com/blog/{slug}/"}}'
        )
    items_str = ",\n".join(items)
    return f"""{{
  "@context": "https://schema.org",
  "@type": "CollectionPage",
  "name": "Lumo Blog — AI, SEO & Growth Marketing Insights",
  "url": "https://lumoaiagency.com/blog/",
  "description": "38 in-depth guides on AI, SEO, paid media, and growth strategy from the team at Lumo AI Agency.",
  "datePublished": "2026-05-15",
  "dateModified": "2026-05-15",
  "publisher": {{
    "@type": "Organization",
    "name": "Lumo AI Agency",
    "url": "https://lumoaiagency.com"
  }},
  "breadcrumb": {{
    "@type": "BreadcrumbList",
    "itemListElement": [
      {{"@type":"ListItem","position":1,"name":"Home","item":"https://lumoaiagency.com/"}},
      {{"@type":"ListItem","position":2,"name":"Blog","item":"https://lumoaiagency.com/blog/"}}
    ]
  }},
  "mainEntity": {{
    "@type": "ItemList",
    "numberOfItems": {len(articles)},
    "itemListElement": [
{items_str}
    ]
  }}
}}"""

# ---------------------------------------------------------------------------
# Full page builder
# ---------------------------------------------------------------------------
def build_html(articles):
    groups = group_by_category(articles)
    total = len(articles)

    # Build sections
    sections = []
    for i, (cat_name, arts) in enumerate(groups.items()):
        sections.append(render_section(cat_name, arts, first=(i == 0)))
    sections_html = "\n".join(sections)

    schema = build_schema(articles)

    # TOC nav links for jump-to-section bar
    toc_links = " &nbsp;|&nbsp; ".join(
        f'<a href="#{CAT_META[c]["id"]}">{CAT_META[c]["label"]}</a>'
        for c in groups.keys()
    )

    html = f"""<!DOCTYPE html>
<html lang="en-US">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <meta name="description" content="38 in-depth guides on AI, SEO, paid media, and growth strategy — written by the team at Lumo AI Agency, Austin TX." />
  <meta name="robots" content="index, follow" />
  <meta name="author" content="Lumo AI Agency" />
  <meta property="og:type" content="website" />
  <meta property="og:title" content="Lumo Blog — AI, SEO &amp; Growth Marketing Insights | Lumo AI Agency" />
  <meta property="og:description" content="38 in-depth guides on AI, SEO, paid media, and growth strategy from the team at Lumo AI Agency." />
  <meta property="og:url" content="https://lumoaiagency.com/blog/" />
  <meta property="og:image" content="https://lumoaiagency.com/og-image.jpg" />
  <meta name="twitter:card" content="summary_large_image" />
  <link rel="canonical" href="https://lumoaiagency.com/blog/" />
  <title>Lumo Blog &mdash; AI, SEO &amp; Growth Marketing Insights | Lumo AI Agency</title>

  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Berkshire+Swash&family=Inter:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet" />

  <script type="application/ld+json">
  {schema}
  </script>

  <style>
    :root {{
      --bg:#0D0D14;--bg-card:#13131F;--bg-dark:#09090F;--primary:#B3FF00;--primary-dim:rgba(179,255,0,0.08);--secondary:#7C3AED;--accent:#00F5FF;--text:#F0F0FF;--muted:#6B7280;--border:rgba(179,255,0,0.15);--glow-lime:0 0 30px rgba(179,255,0,0.35);--glow-violet:0 0 30px rgba(124,58,237,0.45);--radius-sm:8px;--radius:14px;--radius-lg:20px;--transition:0.25s cubic-bezier(0.4,0,0.2,1);
    }}
    *,*::before,*::after{{box-sizing:border-box;margin:0;padding:0;}}
    html{{scroll-behavior:smooth;-webkit-font-smoothing:antialiased;}}
    body{{font-family:'Inter',system-ui,sans-serif;background:var(--bg);color:var(--text);overflow-x:hidden;line-height:1.6;}}
    h1,h2,h3,h4{{line-height:1.15;}}
    a{{color:inherit;text-decoration:none;}}
    img{{max-width:100%;height:auto;display:block;}}
    button{{font-family:inherit;cursor:pointer;border:none;background:none;}}
    ul{{list-style:none;}}
    .section-pad{{padding:100px 0;}}
    .container{{max-width:1180px;margin:0 auto;padding:0 24px;}}
    .btn{{display:inline-flex;align-items:center;gap:8px;padding:14px 30px;border-radius:50px;font-weight:700;font-size:0.95rem;letter-spacing:0.02em;transition:var(--transition);position:relative;overflow:hidden;white-space:nowrap;}}
    .btn-lime{{background:var(--primary);color:#0D0D14;}}
    .btn-lime:hover{{background:#c8ff26;transform:translateY(-2px);box-shadow:0 8px 30px rgba(179,255,0,0.45);}}
    .btn-ghost{{background:transparent;color:var(--text);border:1.5px solid rgba(240,240,255,0.2);}}
    .btn-ghost:hover{{border-color:var(--primary);color:var(--primary);transform:translateY(-2px);}}

    /* ---- Navbar ---- */
    #navbar{{position:fixed;top:0;left:0;right:0;z-index:900;background:rgba(13,13,20,0.85);backdrop-filter:blur(16px);-webkit-backdrop-filter:blur(16px);border-bottom:1px solid rgba(179,255,0,0.06);transition:background 0.3s ease,border-color 0.3s ease;}}
    #navbar.scrolled{{background:rgba(13,13,20,0.97);border-bottom-color:rgba(179,255,0,0.12);}}
    .nav-inner{{display:flex;align-items:center;justify-content:space-between;height:68px;max-width:1180px;margin:0 auto;padding:0 24px;}}
    .nav-logo{{font-family:'Berkshire Swash',serif;font-size:1.6rem;color:var(--primary);letter-spacing:-0.01em;text-shadow:0 0 20px rgba(179,255,0,0.4);}}
    .nav-links{{display:flex;align-items:center;gap:36px;}}
    .nav-links a{{font-size:0.88rem;font-weight:500;color:var(--muted);transition:color var(--transition);letter-spacing:0.02em;}}
    .nav-links a:hover,.nav-links a.active{{color:var(--primary);}}
    .nav-cta{{display:flex;align-items:center;gap:16px;}}
    .nav-hamburger{{display:none;flex-direction:column;gap:5px;padding:8px;cursor:pointer;}}
    .nav-hamburger span{{display:block;width:24px;height:2px;background:var(--text);border-radius:2px;transition:var(--transition);}}
    .mobile-menu{{display:none;flex-direction:column;gap:0;background:rgba(13,13,20,0.98);border-top:1px solid var(--border);padding:8px 24px 16px;}}
    .mobile-menu.open{{display:flex;}}
    .mobile-menu a{{padding:14px 0;border-bottom:1px solid rgba(255,255,255,0.05);color:var(--muted);font-size:0.95rem;font-weight:500;transition:color var(--transition);}}
    .mobile-menu a:last-child{{border-bottom:none;}}
    .mobile-menu a:hover{{color:var(--primary);}}
    @media(max-width:768px){{.nav-links,.nav-cta{{display:none;}}.nav-hamburger{{display:flex;}}}}

    /* ---- Hero ---- */
    .page-hero{{padding:140px 0 80px;position:relative;overflow:hidden;}}
    .blob-wrap{{position:absolute;inset:0;pointer-events:none;overflow:hidden;}}
    .blob{{position:absolute;border-radius:50%;filter:blur(80px);will-change:transform;}}
    .blob-lime{{width:500px;height:500px;background:radial-gradient(circle,rgba(179,255,0,0.18) 0%,transparent 70%);top:-80px;left:-80px;animation:drift-a 18s ease-in-out infinite;}}
    .blob-violet{{width:400px;height:400px;background:radial-gradient(circle,rgba(124,58,237,0.15) 0%,transparent 70%);bottom:0;right:-60px;animation:drift-b 22s ease-in-out infinite;}}
    .blob-cyan{{width:340px;height:340px;background:radial-gradient(circle,rgba(0,245,255,0.1) 0%,transparent 70%);top:50%;left:50%;transform:translate(-50%,-50%);animation:drift-a 26s ease-in-out infinite reverse;}}
    @keyframes drift-a{{0%,100%{{transform:translate(0,0) scale(1);}}50%{{transform:translate(60px,50px) scale(1.08);}}}}
    @keyframes drift-b{{0%,100%{{transform:translate(0,0) scale(1);}}50%{{transform:translate(-50px,-40px) scale(1.06);}}}}
    .hero-noise{{position:absolute;inset:0;background-image:linear-gradient(rgba(179,255,0,0.02) 1px,transparent 1px),linear-gradient(90deg,rgba(179,255,0,0.02) 1px,transparent 1px);background-size:60px 60px;pointer-events:none;}}
    .page-hero-inner{{position:relative;z-index:2;}}
    .section-eyebrow{{display:inline-flex;align-items:center;gap:8px;font-size:0.72rem;font-weight:700;letter-spacing:0.12em;text-transform:uppercase;color:var(--primary);margin-bottom:16px;}}
    .section-eyebrow::before{{content:'';display:block;width:24px;height:2px;background:var(--primary);border-radius:2px;}}
    .section-h2{{font-family:'Berkshire Swash',serif;font-size:clamp(2rem,4.5vw,3.4rem);color:var(--text);margin-bottom:16px;}}
    .section-h2 .hl-lime{{color:var(--primary);}}
    .section-h2 .hl-violet{{color:var(--secondary);}}
    .section-h2 .hl-cyan{{color:var(--accent);}}
    .section-sub{{font-size:1.05rem;color:var(--muted);max-width:520px;margin-bottom:60px;}}
    .page-hero h1{{font-family:'Berkshire Swash',serif;font-size:clamp(2.8rem,6vw,5rem);color:var(--text);line-height:1.08;margin-bottom:24px;}}
    .page-hero h1 .hl-lime{{color:var(--primary);text-shadow:0 0 30px rgba(179,255,0,0.45);}}
    .page-hero h1 .hl-violet{{color:var(--secondary);}}
    .page-hero h1 .hl-cyan{{color:var(--accent);}}
    .page-hero p.lead{{font-size:1.15rem;color:var(--muted);max-width:640px;margin-bottom:40px;}}

    /* ---- Hero stats strip ---- */
    .hero-stats{{display:flex;gap:40px;flex-wrap:wrap;margin-top:48px;padding-top:40px;border-top:1px solid rgba(255,255,255,0.06);}}
    .hero-stat-item{{display:flex;flex-direction:column;gap:4px;}}
    .hero-stat-num{{font-size:1.8rem;font-weight:800;color:var(--primary);line-height:1;}}
    .hero-stat-label{{font-size:0.78rem;color:var(--muted);text-transform:uppercase;letter-spacing:0.08em;}}

    /* ---- TOC jump bar ---- */
    .toc-bar{{background:var(--bg-card);border-bottom:1px solid rgba(255,255,255,0.05);padding:14px 0;position:sticky;top:68px;z-index:800;overflow-x:auto;white-space:nowrap;}}
    .toc-bar-inner{{max-width:1180px;margin:0 auto;padding:0 24px;display:flex;gap:6px;align-items:center;flex-wrap:nowrap;}}
    .toc-bar-inner a{{font-size:0.78rem;font-weight:600;color:var(--muted);padding:5px 12px;border-radius:50px;border:1px solid transparent;transition:all 0.22s;letter-spacing:0.03em;}}
    .toc-bar-inner a:hover{{color:var(--primary);border-color:rgba(179,255,0,0.25);background:rgba(179,255,0,0.05);}}
    .toc-sep{{color:rgba(255,255,255,0.12);font-size:0.75rem;}}

    /* ---- Category label pill (section heading) ---- */
    .category-label{{font-size:0.7rem;font-weight:700;letter-spacing:0.14em;text-transform:uppercase;padding:4px 12px;border-radius:50px;margin-bottom:24px;display:inline-block;}}
    .cat-ai{{background:rgba(179,255,0,0.08);border:1px solid rgba(179,255,0,0.25);color:var(--primary);}}
    .cat-marketing{{background:rgba(124,58,237,0.1);border:1px solid rgba(124,58,237,0.3);color:var(--secondary);}}
    .cat-dev{{background:rgba(0,245,255,0.08);border:1px solid rgba(0,245,255,0.2);color:var(--accent);}}

    /* ---- Blog section ---- */
    .blog-section{{padding:80px 0;}}
    .blog-section+.blog-section{{border-top:1px solid rgba(255,255,255,0.04);}}

    /* ---- Blog grid ---- */
    .blog-grid{{display:grid;grid-template-columns:repeat(3,1fr);gap:20px;}}
    @media(max-width:900px){{.blog-grid{{grid-template-columns:1fr 1fr;}}}}
    @media(max-width:560px){{.blog-grid{{grid-template-columns:1fr;}}}}

    /* ---- Article card ---- */
    .article-card{{background:var(--bg-card);border:1px solid rgba(255,255,255,0.05);border-radius:var(--radius-lg);padding:28px;display:flex;flex-direction:column;gap:14px;transition:transform 0.28s ease,border-color 0.28s ease,box-shadow 0.28s ease;}}
    .article-card.cat-ai:hover{{border-color:rgba(179,255,0,0.35);box-shadow:0 0 36px rgba(179,255,0,0.1);transform:translateY(-4px);}}
    .article-card.cat-marketing:hover{{border-color:rgba(124,58,237,0.45);box-shadow:0 0 36px rgba(124,58,237,0.15);transform:translateY(-4px);}}
    .article-card.cat-dev:hover{{border-color:rgba(0,245,255,0.35);box-shadow:0 0 36px rgba(0,245,255,0.1);transform:translateY(-4px);}}

    /* ---- Article cat pill ---- */
    .article-cat-pill{{font-size:0.68rem;font-weight:700;letter-spacing:0.12em;text-transform:uppercase;padding:3px 10px;border-radius:50px;display:inline-block;align-self:flex-start;}}

    /* ---- Article title ---- */
    .article-title{{font-size:1.05rem;font-weight:700;color:var(--text);line-height:1.3;flex-shrink:0;}}

    /* ---- Article excerpt ---- */
    .article-excerpt{{font-size:0.86rem;color:var(--muted);line-height:1.65;flex:1;}}

    /* ---- Article footer row ---- */
    .article-footer{{display:flex;align-items:center;justify-content:space-between;gap:8px;flex-wrap:wrap;margin-top:auto;padding-top:4px;border-top:1px solid rgba(255,255,255,0.05);}}
    .article-meta{{font-size:0.75rem;color:var(--muted);}}
    .read-link{{font-size:0.82rem;font-weight:600;color:var(--primary);display:inline-flex;align-items:center;gap:4px;transition:gap 0.2s,color 0.2s;white-space:nowrap;}}
    .read-link:hover{{gap:8px;color:#c8ff26;}}

    /* ---- CTA band ---- */
    .cta-band{{background:var(--bg-dark);border-top:1px solid rgba(179,255,0,0.06);text-align:center;padding:100px 0;}}
    .cta-band h2{{font-family:'Berkshire Swash',serif;font-size:clamp(2rem,4vw,3.2rem);margin-bottom:20px;}}
    .cta-band p{{color:var(--muted);font-size:1rem;max-width:500px;margin:0 auto 36px;}}
    .cta-btns{{display:flex;gap:14px;justify-content:center;flex-wrap:wrap;}}

    /* ---- Footer ---- */
    footer{{background:var(--bg-dark);border-top:1px solid rgba(179,255,0,0.08);padding:60px 0 30px;}}
    .footer-inner{{max-width:1180px;margin:0 auto;padding:0 24px;}}
    .footer-top{{display:grid;grid-template-columns:1.4fr 1fr 1fr 1fr;gap:48px;margin-bottom:48px;}}
    .footer-brand .nav-logo{{margin-bottom:16px;display:block;}}
    .footer-brand p{{font-size:0.85rem;color:var(--muted);line-height:1.7;margin-bottom:24px;}}
    .social-links{{display:flex;gap:10px;}}
    .social-link{{width:38px;height:38px;border-radius:10px;background:rgba(124,58,237,0.12);border:1px solid rgba(124,58,237,0.25);display:flex;align-items:center;justify-content:center;color:var(--secondary);font-size:0.9rem;transition:background 0.25s,border-color 0.25s,transform 0.25s,box-shadow 0.25s;}}
    .social-link:hover{{background:rgba(124,58,237,0.25);border-color:var(--secondary);transform:translateY(-3px);box-shadow:var(--glow-violet);color:#fff;}}
    .footer-col h4{{font-size:0.78rem;font-weight:700;letter-spacing:0.1em;text-transform:uppercase;color:var(--text);margin-bottom:20px;}}
    .footer-col ul{{display:flex;flex-direction:column;gap:10px;}}
    .footer-col a{{font-size:0.85rem;color:var(--muted);transition:color 0.22s;}}
    .footer-col a:hover{{color:var(--primary);}}
    .footer-bottom{{border-top:1px solid rgba(255,255,255,0.06);padding-top:24px;display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:12px;}}
    .footer-bottom p,.footer-copy{{font-size:0.8rem;color:var(--muted);}}
    .footer-bottom a,.footer-bl a{{color:var(--primary);font-size:0.8rem;margin-left:16px;}}
    .footer-bl a:first-child{{margin-left:0;}}
    .footer-badge{{display:inline-flex;align-items:center;gap:6px;font-size:0.75rem;color:var(--muted);background:rgba(179,255,0,0.05);border:1px solid rgba(179,255,0,0.12);padding:5px 12px;border-radius:50px;}}
    .footer-badge-dot{{width:6px;height:6px;border-radius:50%;background:var(--primary);box-shadow:0 0 6px rgba(179,255,0,0.8);animation:blink 2s infinite;}}
    @keyframes blink{{0%,100%{{opacity:1;}}50%{{opacity:0.3;}}}}
    @media(max-width:900px){{.footer-top{{grid-template-columns:1fr 1fr;}}}}
    @media(max-width:560px){{.footer-top{{grid-template-columns:1fr;gap:32px;}}.footer-bottom{{flex-direction:column;text-align:center;}}}}

    /* ---- Scroll-to-top ---- */
    #scroll-top{{position:fixed;bottom:30px;right:30px;width:46px;height:46px;border-radius:12px;background:var(--primary);color:#0D0D14;font-size:1.1rem;display:flex;align-items:center;justify-content:center;cursor:pointer;z-index:800;opacity:0;transform:translateY(10px);transition:opacity 0.3s,transform 0.3s,box-shadow 0.3s;border:none;}}
    #scroll-top.visible{{opacity:1;transform:translateY(0);}}
    #scroll-top:hover{{box-shadow:0 0 20px rgba(179,255,0,0.5);transform:translateY(-3px);}}
  </style>
</head>
<body>

<header>
  <nav id="navbar" role="navigation" aria-label="Main navigation">
    <div class="nav-inner">
      <a href="/" class="nav-logo" aria-label="Lumo AI Agency — Home">Lumo<span>.</span></a>
      <ul class="nav-links" role="menubar">
        <li role="none"><a href="/services.html" role="menuitem">Services</a></li>
        <li role="none"><a href="/about.html" role="menuitem">About</a></li>
        <li role="none"><a href="/pricing.html" role="menuitem">Pricing</a></li>
        <li role="none"><a href="/contact.html" role="menuitem">Contact</a></li>
      </ul>
      <div class="nav-cta"><a href="/contact.html" class="btn btn-lime" style="padding:10px 22px;font-size:0.85rem;">Get Started</a></div>
      <button class="nav-hamburger" id="hamburger" aria-label="Open menu" aria-expanded="false" aria-controls="mobile-menu">
        <span></span><span></span><span></span>
      </button>
    </div>
    <div class="mobile-menu" id="mobile-menu" role="menu" aria-hidden="true">
      <a href="/services.html" role="menuitem">Services</a>
      <a href="/about.html" role="menuitem">About</a>
      <a href="/pricing.html" role="menuitem">Pricing</a>
      <a href="/contact.html" role="menuitem">Contact</a>
      <a href="/contact.html" role="menuitem">Get Started &rarr;</a>
    </div>
  </nav>
</header>

<main>

  <!-- HERO -->
  <section class="page-hero" aria-label="Lumo Blog">
    <div class="blob-wrap" aria-hidden="true">
      <div class="blob blob-lime"></div>
      <div class="blob blob-violet"></div>
      <div class="blob blob-cyan"></div>
    </div>
    <div class="hero-noise" aria-hidden="true"></div>
    <div class="container page-hero-inner">
      <p class="section-eyebrow">Lumo Blog</p>
      <h1>AI &amp; Marketing<br/><span class="hl-lime">Insights</span></h1>
      <p class="lead">{total} in-depth guides on AI, SEO, paid media, and growth strategy &mdash; from the team at Lumo AI Agency.</p>
      <div style="display:flex;gap:14px;flex-wrap:wrap;">
        <a href="/contact.html" class="btn btn-lime">Get Free Proposal <svg width="16" height="16" viewBox="0 0 16 16" fill="none" aria-hidden="true"><path d="M3 8h10M9 4l4 4-4 4" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg></a>
        <a href="/services.html" class="btn btn-ghost">Our Services</a>
      </div>
      <div class="hero-stats">
        <div class="hero-stat-item">
          <span class="hero-stat-num">{total}</span>
          <span class="hero-stat-label">In-Depth Guides</span>
        </div>
        <div class="hero-stat-item">
          <span class="hero-stat-num">{len(groups)}</span>
          <span class="hero-stat-label">Topic Categories</span>
        </div>
        <div class="hero-stat-item">
          <span class="hero-stat-num">~{sum(a[6] for a in articles)}</span>
          <span class="hero-stat-label">Total Reading Minutes</span>
        </div>
      </div>
    </div>
  </section>

  <!-- TOC jump bar -->
  <nav class="toc-bar" aria-label="Jump to section">
    <div class="toc-bar-inner">
      {"<span class='toc-sep'>|</span>".join(f'<a href="#{CAT_META[c]["id"]}">{CAT_META[c]["label"]}</a>' for c in groups.keys())}
    </div>
  </nav>

{sections_html}

  <!-- CTA BAND -->
  <section class="cta-band" aria-labelledby="cta-h2">
    <div class="container">
      <p class="section-eyebrow" style="justify-content:center;">Ready to Scale?</p>
      <h2 id="cta-h2">Deploy AI. <span style="color:var(--primary);">Grow Faster.</span></h2>
      <p>Book a free strategy call and we&rsquo;ll show you exactly which services will move the needle for your business &mdash; with projected ROI.</p>
      <div class="cta-btns">
        <a href="/contact.html" class="btn btn-lime">Get Free Proposal <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14M12 5l7 7-7 7"/></svg></a>
        <a href="/pricing.html" class="btn btn-ghost">View Pricing</a>
      </div>
    </div>
  </section>

</main>

<footer role="contentinfo">
  <div class="footer-inner">
    <div class="footer-top">
      <div class="footer-brand">
        <a href="/" class="nav-logo footer-logo" aria-label="Lumo AI Agency home">Lumo<span>.</span></a>
        <p>Austin&rsquo;s AI-powered marketing agency. SEO, paid ads, AI automation &amp; web design built for the future.</p>
        <div class="social-links">
          <a href="https://instagram.com/lumoaiagency" class="social-link" target="_blank" rel="noopener noreferrer" aria-label="Lumo on Instagram">&#9679;</a>
          <a href="https://linkedin.com/company/lumoaiagency" class="social-link" target="_blank" rel="noopener noreferrer" aria-label="Lumo on LinkedIn">in</a>
          <a href="https://twitter.com/lumoaiagency" class="social-link" target="_blank" rel="noopener noreferrer" aria-label="Lumo on X">&#120143;</a>
        </div>
      </div>
      <div class="footer-col">
        <h4>Services</h4>
        <ul>
          <li><a href="/services/seo.html">SEO &amp; Content</a></li>
          <li><a href="/services/google-ads.html">Google Ads</a></li>
          <li><a href="/services/meta-ads.html">Meta Ads</a></li>
          <li><a href="/services/linkedin-ads.html">LinkedIn Ads</a></li>
          <li><a href="/services/tiktok-ads.html">TikTok Ads</a></li>
          <li><a href="/services/ecommerce-seo.html">E-commerce SEO</a></li>
          <li><a href="/services/cro.html">CRO</a></li>
          <li><a href="/services/web-design.html">Web Design</a></li>
          <li><a href="/services/ai-development.html">AI Development</a></li>
          <li><a href="/services/ai-automations.html">AI Automations</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h4>Top Locations</h4>
        <ul>
          <li><a href="/local/austin/seo-agency/">SEO Agency Austin</a></li>
          <li><a href="/local/new-york/seo-agency/">SEO Agency New York</a></li>
          <li><a href="/local/los-angeles/seo-agency/">SEO Agency Los Angeles</a></li>
          <li><a href="/local/austin/google-ads-agency/">Google Ads Austin</a></li>
          <li><a href="/local/austin/ai-automation-agency/">AI Agency Austin</a></li>
          <li><a href="/local/chicago/seo-agency/">SEO Agency Chicago</a></li>
          <li><a href="/local/houston/seo-agency/">SEO Agency Houston</a></li>
          <li><a href="/local/dallas/seo-agency/">SEO Agency Dallas</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h4>Company</h4>
        <ul>
          <li><a href="/about.html">About Us</a></li>
          <li><a href="/services.html">All Services</a></li>
          <li><a href="/pricing.html">Pricing</a></li>
          <li><a href="/blog/">Blog</a></li>
          <li><a href="/contact.html">Contact</a></li>
        </ul>
        <h4 style="margin-top:24px">Contact</h4>
        <div><a href="tel:+16473701888" style="font-size:0.85rem;color:var(--muted);">(647) 370-1888</a></div>
        <div style="margin-top:8px"><a href="mailto:hello@lumoaiagency.com" style="font-size:0.85rem;color:var(--muted);">hello@lumoaiagency.com</a></div>
      </div>
    </div>
    <div class="footer-bottom">
      <span class="footer-copy">&copy; 2026 Lumo AI Agency. All rights reserved.</span>
      <div class="footer-bl">
        <a href="/privacy-policy.html">Privacy Policy</a>
        <a href="/terms.html">Terms of Service</a>
        <a href="/cookie-policy.html">Cookie Policy</a>
      </div>
    </div>
  </div>
</footer>

<button id="scroll-top" aria-label="Scroll back to top">
  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 19V5M5 12l7-7 7 7"/></svg>
</button>

<script>
(function(){{
  var navbar=document.getElementById('navbar');
  var hamburger=document.getElementById('hamburger');
  var mobileMenu=document.getElementById('mobile-menu');
  var menuOpen=false;
  window.addEventListener('scroll',function(){{navbar.classList.toggle('scrolled',window.scrollY>20);}},{{passive:true}});
  hamburger.addEventListener('click',function(){{menuOpen=!menuOpen;mobileMenu.classList.toggle('open',menuOpen);hamburger.setAttribute('aria-expanded',String(menuOpen));mobileMenu.setAttribute('aria-hidden',String(!menuOpen));}});
  mobileMenu.querySelectorAll('a').forEach(function(link){{link.addEventListener('click',function(){{menuOpen=false;mobileMenu.classList.remove('open');hamburger.setAttribute('aria-expanded','false');mobileMenu.setAttribute('aria-hidden','true');}});}});
  var scrollTopBtn=document.getElementById('scroll-top');
  window.addEventListener('scroll',function(){{scrollTopBtn.classList.toggle('visible',window.scrollY>400);}},{{passive:true}});
  scrollTopBtn.addEventListener('click',function(){{window.scrollTo({{top:0,behavior:'smooth'}});}});
}})();
</script>
</body>
</html>"""
    return html

# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    blog_dir = os.path.join(script_dir, "blog")
    os.makedirs(blog_dir, exist_ok=True)

    output_path = os.path.join(blog_dir, "index.html")
    html = build_html(ARTICLES)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html)

    file_size = os.path.getsize(output_path)
    print(f"Written: {output_path}")
    print(f"File size: {file_size:,} bytes")
    print(f"Article cards rendered: {len(ARTICLES)}")
    print(f"Categories: {len(group_by_category(ARTICLES))}")

if __name__ == "__main__":
    main()
