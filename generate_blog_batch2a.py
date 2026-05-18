import os

BASE_DIR = r"C:\Users\Инна\Desktop\projects\lumo-ai-agency"

NAV_HTML = """<nav id="navbar">
  <div class="nav-inner">
    <a href="/" class="nav-logo">Lumo<span>.</span></a>
    <ul class="nav-links">
      <li><a href="/services.html">Services</a></li>
      <li><a href="/about.html">About</a></li>
      <li><a href="/pricing.html">Pricing</a></li>
      <li><a href="/contact.html">Contact</a></li>
    </ul>
    <div class="nav-cta"><a href="/contact.html" class="btn btn-lime" style="padding:10px 22px;font-size:0.85rem;">Get a Free Audit</a></div>
    <button class="nav-hamburger" id="hamburger" aria-label="Open menu"><span></span><span></span><span></span></button>
  </div>
  <div class="mobile-menu" id="mobile-menu">
    <a href="/services.html">Services</a><a href="/about.html">About</a><a href="/pricing.html">Pricing</a><a href="/contact.html">Contact</a><a href="/contact.html">Get Started &rarr;</a>
  </div>
</nav>"""

FOOTER_HTML = """<footer>
  <div class="footer-inner">
    <div class="footer-top">
      <div class="footer-col">
        <div class="nav-logo" style="font-family:'Berkshire Swash',serif;font-size:1.5rem;color:var(--primary);margin-bottom:12px;">Lumo<span>.</span></div>
        <p style="font-size:0.85rem;color:var(--muted);line-height:1.7;max-width:220px;">Austin's AI-powered marketing agency helping brands grow with paid ads, SEO, and intelligent automation.</p>
      </div>
      <div class="footer-col">
        <h4>Services</h4>
        <ul>
          <li><a href="/services/seo.html">SEO</a></li>
          <li><a href="/services/geo.html">GEO / AI Search</a></li>
          <li><a href="/services/google-ads.html">Google Ads</a></li>
          <li><a href="/services/meta-ads.html">Meta Ads</a></li>
          <li><a href="/services/ai-automations.html">AI Automations</a></li>
          <li><a href="/services.html">All Services</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h4>Company</h4>
        <ul>
          <li><a href="/about.html">About</a></li>
          <li><a href="/pricing.html">Pricing</a></li>
          <li><a href="/contact.html">Contact</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h4>Legal</h4>
        <ul>
          <li><a href="/privacy-policy.html">Privacy Policy</a></li>
          <li><a href="/terms.html">Terms of Service</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <p>&copy; 2026 Lumo AI Agency. All rights reserved.</p>
      <div class="footer-badge"><span class="footer-badge-dot"></span>Serving clients across the US</div>
    </div>
  </div>
</footer>"""

CSS = """
:root{--bg:#0D0D14;--bg-card:#13131F;--bg-dark:#09090F;--primary:#B3FF00;--primary-dim:rgba(179,255,0,0.08);--secondary:#7C3AED;--accent:#00F5FF;--text:#F0F0FF;--muted:#6B7280;--border:rgba(179,255,0,0.15);--radius-sm:8px;--radius:14px;--radius-lg:20px;--transition:0.25s cubic-bezier(0.4,0,0.2,1);}
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0;}
html{scroll-behavior:smooth;-webkit-font-smoothing:antialiased;}
body{font-family:'Inter',system-ui,sans-serif;background:var(--bg);color:var(--text);overflow-x:hidden;line-height:1.6;}
h1,h2,h3,h4{line-height:1.15;}a{color:inherit;text-decoration:none;}ul{list-style:none;}button{font-family:inherit;cursor:pointer;border:none;background:none;}
.container{max-width:1180px;margin:0 auto;padding:0 24px;}
.btn{display:inline-flex;align-items:center;gap:8px;padding:14px 30px;border-radius:50px;font-weight:700;font-size:0.95rem;letter-spacing:0.02em;transition:var(--transition);white-space:nowrap;}
.btn-lime{background:var(--primary);color:#0D0D14;}.btn-lime:hover{background:#c8ff26;transform:translateY(-2px);box-shadow:0 8px 30px rgba(179,255,0,0.45);}
.btn-ghost{background:transparent;color:var(--text);border:1.5px solid rgba(240,240,255,0.2);}.btn-ghost:hover{border-color:var(--primary);color:var(--primary);transform:translateY(-2px);}
#navbar{position:fixed;top:0;left:0;right:0;z-index:900;background:rgba(13,13,20,0.85);backdrop-filter:blur(16px);border-bottom:1px solid rgba(179,255,0,0.06);transition:background 0.3s,border-color 0.3s;}
#navbar.scrolled{background:rgba(13,13,20,0.97);border-bottom-color:rgba(179,255,0,0.12);}
.nav-inner{display:flex;align-items:center;justify-content:space-between;height:68px;max-width:1180px;margin:0 auto;padding:0 24px;}
.nav-logo{font-family:'Berkshire Swash',serif;font-size:1.6rem;color:var(--primary);letter-spacing:-0.01em;text-shadow:0 0 20px rgba(179,255,0,0.4);}
.nav-links{display:flex;align-items:center;gap:36px;}
.nav-links a{font-size:0.88rem;font-weight:500;color:var(--muted);transition:color var(--transition);}
.nav-links a:hover{color:var(--primary);}
.nav-hamburger{display:none;flex-direction:column;gap:5px;padding:8px;}
.nav-hamburger span{display:block;width:24px;height:2px;background:var(--text);border-radius:2px;}
.mobile-menu{display:none;flex-direction:column;background:rgba(13,13,20,0.98);border-top:1px solid var(--border);padding:8px 24px 16px;}
.mobile-menu.open{display:flex;}
.mobile-menu a{padding:14px 0;border-bottom:1px solid rgba(255,255,255,0.05);color:var(--muted);font-size:0.95rem;transition:color var(--transition);}
.mobile-menu a:last-child{border-bottom:none;}
.mobile-menu a:hover{color:var(--primary);}
@media(max-width:768px){.nav-links,.nav-cta{display:none;}.nav-hamburger{display:flex;}}
.page-hero{padding:140px 0 60px;position:relative;overflow:hidden;}
.blob-wrap{position:absolute;inset:0;pointer-events:none;overflow:hidden;}
.blob{position:absolute;border-radius:50%;filter:blur(80px);}
.blob-lime{width:500px;height:500px;background:radial-gradient(circle,rgba(179,255,0,0.18) 0%,transparent 70%);top:-80px;left:-80px;animation:drift-a 18s ease-in-out infinite;}
.blob-violet{width:400px;height:400px;background:radial-gradient(circle,rgba(124,58,237,0.15) 0%,transparent 70%);bottom:0;right:-60px;animation:drift-b 22s ease-in-out infinite;}
@keyframes drift-a{0%,100%{transform:translate(0,0) scale(1);}50%{transform:translate(60px,50px) scale(1.08);}}
@keyframes drift-b{0%,100%{transform:translate(0,0) scale(1);}50%{transform:translate(-50px,-40px) scale(1.06);}}
.hero-noise{position:absolute;inset:0;background-image:linear-gradient(rgba(179,255,0,0.02) 1px,transparent 1px),linear-gradient(90deg,rgba(179,255,0,0.02) 1px,transparent 1px);background-size:60px 60px;pointer-events:none;}
.page-hero-inner{position:relative;z-index:2;}
.article-breadcrumb{font-size:0.78rem;color:var(--muted);margin-bottom:20px;display:flex;gap:8px;align-items:center;}
.article-breadcrumb a:hover{color:var(--primary);}
.article-meta{display:flex;gap:16px;align-items:center;margin-bottom:24px;flex-wrap:wrap;}
.article-cat{font-size:0.68rem;font-weight:700;letter-spacing:0.12em;text-transform:uppercase;padding:4px 12px;border-radius:50px;}
.cat-cyan{background:rgba(0,245,255,0.08);border:1px solid rgba(0,245,255,0.2);color:var(--accent);}
.cat-lime{background:rgba(179,255,0,0.08);border:1px solid rgba(179,255,0,0.25);color:var(--primary);}
.article-date,.article-mins{font-size:0.8rem;color:var(--muted);}
.article-body{max-width:740px;margin:0 auto;padding:60px 24px 100px;}
.article-body h2{font-family:'Berkshire Swash',serif;font-size:1.7rem;color:var(--text);margin:48px 0 16px;}
.article-body h3{font-size:1.1rem;font-weight:700;color:var(--text);margin:28px 0 10px;}
.article-body p{font-size:1rem;color:rgba(240,240,255,0.8);line-height:1.8;margin-bottom:18px;}
.article-body ul,.article-body ol{padding-left:24px;margin-bottom:18px;display:flex;flex-direction:column;gap:10px;}
.article-body li{font-size:1rem;color:rgba(240,240,255,0.8);line-height:1.7;}
.article-body strong{color:var(--text);font-weight:700;}
.callout{background:rgba(179,255,0,0.05);border:1px solid rgba(179,255,0,0.2);border-radius:14px;padding:24px 28px;margin:36px 0;}
.callout p{margin:0 0 12px;color:var(--text);font-weight:600;}
.callout a{color:var(--primary);font-weight:700;font-size:0.9rem;}
.faq-section{max-width:740px;margin:0 auto;padding:0 24px 60px;}
.faq-section h2{font-family:'Berkshire Swash',serif;font-size:1.7rem;margin-bottom:28px;}
.faq-item{border-bottom:1px solid rgba(255,255,255,0.07);padding:20px 0;}
.faq-q{font-weight:700;font-size:0.95rem;margin-bottom:10px;color:var(--text);}
.faq-a{font-size:0.9rem;color:var(--muted);line-height:1.7;}
.cta-band{background:var(--bg-dark);border-top:1px solid rgba(179,255,0,0.06);text-align:center;padding:100px 0;}
.cta-band h2{font-family:'Berkshire Swash',serif;font-size:clamp(2rem,4vw,3.2rem);margin-bottom:20px;}
.cta-band p{color:var(--muted);font-size:1rem;max-width:500px;margin:0 auto 36px;}
.cta-btns{display:flex;gap:14px;justify-content:center;flex-wrap:wrap;}
footer{background:var(--bg-dark);border-top:1px solid rgba(179,255,0,0.08);padding:60px 0 30px;}
.footer-inner{max-width:1180px;margin:0 auto;padding:0 24px;}
.footer-top{display:grid;grid-template-columns:1.4fr 1fr 1fr 1fr;gap:48px;margin-bottom:48px;}
.footer-col h4{font-size:0.78rem;font-weight:700;letter-spacing:0.1em;text-transform:uppercase;color:var(--text);margin-bottom:20px;}
.footer-col ul{display:flex;flex-direction:column;gap:10px;}
.footer-col a{font-size:0.85rem;color:var(--muted);transition:color 0.22s;}
.footer-col a:hover{color:var(--primary);}
.footer-bottom{border-top:1px solid rgba(255,255,255,0.06);padding-top:24px;display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:12px;}
.footer-bottom p{font-size:0.8rem;color:var(--muted);}
.footer-badge{display:inline-flex;align-items:center;gap:6px;font-size:0.75rem;color:var(--muted);background:rgba(179,255,0,0.05);border:1px solid rgba(179,255,0,0.12);padding:5px 12px;border-radius:50px;}
.footer-badge-dot{width:6px;height:6px;border-radius:50%;background:var(--primary);animation:blink 2s infinite;}
@keyframes blink{0%,100%{opacity:1;}50%{opacity:0.3;}}
@media(max-width:900px){.footer-top{grid-template-columns:1fr 1fr;}}
@media(max-width:560px){.footer-top{grid-template-columns:1fr;gap:32px;}.footer-bottom{flex-direction:column;text-align:center;}}
#scroll-top{position:fixed;bottom:30px;right:30px;width:46px;height:46px;border-radius:12px;background:var(--primary);color:#0D0D14;font-size:1.1rem;display:flex;align-items:center;justify-content:center;cursor:pointer;z-index:800;opacity:0;transform:translateY(10px);transition:opacity 0.3s,transform 0.3s;border:none;}
#scroll-top.visible{opacity:1;transform:translateY(0);}
#scroll-top:hover{box-shadow:0 0 20px rgba(179,255,0,0.5);}
"""

JS = """
<script>
(function(){
  var ham = document.getElementById('hamburger');
  var menu = document.getElementById('mobile-menu');
  if(ham && menu){
    ham.addEventListener('click', function(){
      menu.classList.toggle('open');
    });
  }
  var nav = document.getElementById('navbar');
  window.addEventListener('scroll', function(){
    if(window.scrollY > 40){ nav.classList.add('scrolled'); } else { nav.classList.remove('scrolled'); }
    var st = document.getElementById('scroll-top');
    if(st){ if(window.scrollY > 400){ st.classList.add('visible'); } else { st.classList.remove('visible'); } }
  });
  var st = document.getElementById('scroll-top');
  if(st){ st.addEventListener('click', function(){ window.scrollTo({top:0,behavior:'smooth'}); }); }
})();
</script>
"""

def build_page(title, meta_desc, slug, cat_label, cat_class, pub_date, read_mins,
               h1_html, lead, body_html, faqs, cta_service_slug, cta_service_name):
    faq_items = ""
    for q, a in faqs:
        faq_items += f"""
    <div class="faq-item">
      <div class="faq-q">{q}</div>
      <div class="faq-a">{a}</div>
    </div>"""

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8"/>
  <meta name="viewport" content="width=device-width,initial-scale=1"/>
  <title>{title} | Lumo AI Agency</title>
  <meta name="description" content="{meta_desc}"/>
  <link rel="canonical" href="https://lumoaiagency.com/blog/{slug}/"/>
  <link rel="preconnect" href="https://fonts.googleapis.com"/>
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin/>
  <link href="https://fonts.googleapis.com/css2?family=Berkshire+Swash&family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet"/>
  <style>{CSS}</style>
</head>
<body>

{NAV_HTML}

<section class="page-hero">
  <div class="blob-wrap">
    <div class="blob blob-lime"></div>
    <div class="blob blob-violet"></div>
    <div class="hero-noise"></div>
  </div>
  <div class="container page-hero-inner">
    <nav class="article-breadcrumb" aria-label="Breadcrumb">
      <a href="/">Home</a><span>/</span><a href="/blog/">Blog</a><span>/</span><span>{title}</span>
    </nav>
    <div class="article-meta">
      <span class="article-cat {cat_class}">{cat_label}</span>
      <span class="article-date">{pub_date}</span>
      <span class="article-mins">{read_mins} min read</span>
    </div>
    <h1 style="font-family:'Berkshire Swash',serif;font-size:clamp(2rem,4.5vw,3.2rem);max-width:820px;margin-bottom:24px;">{h1_html}</h1>
    <p style="font-size:1.1rem;color:rgba(240,240,255,0.7);max-width:680px;line-height:1.75;">{lead}</p>
  </div>
</section>

<article class="article-body">
{body_html}
</article>

<section class="faq-section">
  <h2>Frequently Asked Questions</h2>
  {faq_items}
</section>

<section class="cta-band">
  <div class="container">
    <h2>Ready to Scale with <span style="color:var(--primary);">{cta_service_name}?</span></h2>
    <p>Lumo AI Agency builds data-driven paid advertising campaigns that maximize your ROI. Let's find out what's possible for your business.</p>
    <div class="cta-btns">
      <a href="/contact.html" class="btn btn-lime">Get a Free Audit</a>
      <a href="/services/{cta_service_slug}.html" class="btn btn-ghost">Learn About {cta_service_name}</a>
    </div>
  </div>
</section>

{FOOTER_HTML}

<button id="scroll-top" aria-label="Back to top">&#8593;</button>

{JS}
</body>
</html>"""


# ─── ARTICLE DEFINITIONS ────────────────────────────────────────────────────

articles = []

# ── 1. google-ads-vs-meta-ads ──────────────────────────────────────────────
articles.append(dict(
    slug="google-ads-vs-meta-ads",
    title="Google Ads vs Meta Ads: Which Is Right for Your Business in 2026?",
    meta_desc="Google captures existing demand; Meta creates new demand. This fundamental difference drives budget allocation decisions. A complete comparison for 2026 covering ROI, use cases, and when to use both.",
    cat_label="Paid Advertising",
    cat_class="cat-cyan",
    pub_date="May 14, 2026",
    read_mins="9",
    h1_html='Google Ads vs Meta Ads: <span style="color:var(--accent);">Which Is Right for You?</span>',
    lead="The most expensive paid media mistake isn't choosing the wrong bidding strategy or targeting — it's choosing the wrong platform. Google and Meta operate on fundamentally different principles, and understanding that difference is worth thousands of dollars in better decisions.",
    cta_service_slug="google-ads",
    cta_service_name="Google Ads",
    body_html="""
<h2>The Fundamental Difference: Demand Capture vs Demand Creation</h2>
<p>At their core, Google Ads and Meta Ads solve different problems. Google is a <strong>demand capture platform</strong>. Someone types "emergency plumber Austin" into Google — that search represents crystallised, active intent. They need a plumber right now, and Google's job is to connect them with one. Your ad appears at the moment of maximum purchase intent.</p>
<p>Meta is a <strong>demand creation platform</strong>. You're reaching people who are scrolling Instagram or Facebook — they didn't open the app thinking about your product. They weren't planning to buy anything. Your ad needs to stop the scroll, create desire, and either convert immediately or plant a seed that leads to a future purchase.</p>
<p>This distinction has enormous implications for conversion rates. Google Search campaigns typically convert at 4–8% because you're catching buyers mid-decision. Meta campaigns often convert at 0.5–2% for cold audiences because you're interrupting people, not meeting them where their intent lives. That doesn't make Meta less valuable — it just means you can't evaluate the two on identical metrics.</p>
<p>The practical consequence: if you sell a product or service that people already search for, Google can acquire customers profitably at scale. If you're selling something people don't know they need, or something driven by visual aspiration and lifestyle, Meta's interruption model is often the only way to reach cold audiences efficiently.</p>

<h2>When Google Ads Wins</h2>
<p>Google Ads performs best when there is <strong>proven search demand</strong> for what you offer. If people are actively typing queries that match your solution, you're fishing in a pond full of buyers. Categories where Google consistently dominates on ROAS:</p>
<ul>
  <li><strong>High-intent service businesses</strong> — plumbers, electricians, HVAC, dentists, lawyers, accountants, locksmiths. These are people with urgent needs and credit cards ready. Google Local Services Ads and Search together can drive $10–$50 CPL for service businesses that compete well on reviews.</li>
  <li><strong>B2B with defined search categories</strong> — "CRM software for small business," "cloud accounting for nonprofits," "IT managed services Austin." If your buyers search for solutions, Google Search puts you in front of them at decision time.</li>
  <li><strong>Products with strong category search volume</strong> — Google Shopping Ads for e-commerce categories where shoppers browse with intent (office furniture, running shoes, supplements, kitchenware).</li>
  <li><strong>High-ticket considered purchases</strong> — home renovation, enterprise software, financial planning. Long search-to-close cycles are fine because the intent signal is still strong enough to outweigh the friction.</li>
</ul>
<p>The data point that seals the argument: across industries, <strong>Google Search Ads convert new visitors at 3–5x the rate of cold social traffic</strong>. The intent signal is doing the heavy conversion lifting before the user even reaches your landing page.</p>

<h2>When Meta Ads Wins</h2>
<p>Meta's 3.27 billion monthly active users and its unparalleled behavioral targeting dataset make it the go-to platform for demand creation. Where Meta consistently outperforms Google:</p>
<ul>
  <li><strong>Visual e-commerce products</strong> — fashion, home decor, beauty, food, lifestyle accessories. A stunning product photo or video in the feed can stop a scroll and trigger a purchase decision in under 30 seconds. Google can't replicate that visual interruption for products people weren't actively searching.</li>
  <li><strong>Impulse and aspirational purchases</strong> — products under $100 where the emotional appeal is strong and the purchase barrier is low. Meta's one-click checkout integrations have compressed the discovery-to-purchase cycle to minutes.</li>
  <li><strong>Audience building and remarketing</strong> — Meta's Pixel and Advantage+ audiences let you build huge warm audiences from website visitors, video viewers, and customer lists, then serve them progressively more targeted creative. This retargeting layer is often where Meta delivers its best ROAS.</li>
  <li><strong>Products people don't know they need yet</strong> — new categories, innovative gadgets, novel services. If search volume doesn't exist because awareness is low, Meta can create that awareness and build the search volume that Google will later capture.</li>
  <li><strong>B2C lifestyle brands</strong> — brands where identity and aspiration are central to the purchase decision. Following a brand on Instagram and seeing their story play out over weeks is a customer journey Google can't create.</li>
</ul>

<h2>The Full-Funnel Case for Using Both</h2>
<p>The most sophisticated paid media strategies use Google and Meta as <strong>complementary channels</strong>, not competing ones. The most common full-funnel pattern: Meta builds top-of-funnel awareness → the prospect searches Google later → Google Search or Shopping captures the purchase.</p>
<p>This creates a messy attribution problem that most advertisers underestimate. If you run Meta campaigns and later see a spike in Google Search branded traffic and direct conversions, that's frequently Meta's influence. Last-click attribution gives Google all the credit; Meta's contribution becomes invisible. The result is advertisers cutting Meta budgets that were actually driving significant downstream Google and direct revenue.</p>
<p>Smart attribution approaches for 2026 include: <strong>data-driven attribution in GA4</strong> (assigns fractional credit across touchpoints), <strong>Meta's own Conversions API</strong> data alongside Google's, and periodic <strong>incrementality tests</strong> (pause Meta for 2 weeks, measure if branded search drops). These methods consistently show Meta's contribution is 20–40% higher than last-click models suggest.</p>
<p>The practical implication: run both platforms if budget allows. Run a holdout test every 6 months to validate each channel's true incremental contribution. Don't cut a channel because last-click attribution undervalues it.</p>

<h2>Budget Allocation Framework</h2>
<p>Without knowing your specific business, margins, and data, here's a framework that has held up across dozens of accounts:</p>
<ul>
  <li><strong>Early stage (under $5k/month ad spend)</strong> — pick one platform based on your product type. If you're a service business with search demand: Google. If you're a visual e-commerce brand: Meta. Don't split a small budget; concentrate it where the core opportunity is.</li>
  <li><strong>Growth stage ($5k–$25k/month)</strong> — test both with a 70/30 split favouring your primary channel. Let each platform accumulate 60–90 days of data before judging. Focus the secondary channel on retargeting first, since warm audiences convert better and give you early wins.</li>
  <li><strong>Scale stage ($25k+/month)</strong> — operate full-funnel with proper attribution. Use Google for high-intent capture across Search and Shopping; use Meta for prospecting, creative testing, and retargeting sequences. Set platform-level ROAS targets based on data-driven attribution, not last-click.</li>
</ul>
<p>One final principle: <strong>the quality of your landing page and offer matters more than the platform</strong>. Switching from Google to Meta won't fix a 0.5% landing page conversion rate. Both platforms reward advertisers who convert efficiently — the algorithm gives better distribution to campaigns that prove their worth with conversion data. Optimise the post-click experience first; then scale on the platform that best matches your demand profile.</p>

<div class="callout">
  <p>Lumo AI Agency runs Google Ads campaigns that target the exact moment your customers are searching for your solution.</p>
  <a href="/services/google-ads.html">Explore our Google Ads service &rarr;</a>
</div>
""",
    faqs=[
        ("Can I run Google Ads and Meta Ads simultaneously on a limited budget?",
         "With budgets under $3,000/month, splitting between two platforms usually means neither gets enough data to optimise effectively. Pick the better fit for your product type, run it well for 60–90 days, and add the second platform once you're profitable on the first."),
        ("Which platform is better for local service businesses?",
         "Google is almost always the right starting point for local service businesses — plumbers, dentists, HVAC, attorneys, etc. Search intent is explicit and immediate. Google Local Services Ads with pay-per-lead billing often deliver the best CPL for local services. Add Meta retargeting later for brand-building."),
        ("How do I know if Meta or Google is actually driving my sales?",
         "Run a 2-week Meta spend pause and track branded Google Search impressions and direct conversions. If both drop significantly, Meta was creating demand that Google was capturing. Data-driven attribution in GA4 and Meta's Conversions API data together give the clearest cross-channel picture available without expensive incrementality infrastructure."),
    ]
))

# ── 2. performance-max-guide ───────────────────────────────────────────────
articles.append(dict(
    slug="performance-max-guide",
    title="Performance Max Campaigns: The Complete Setup and Optimization Guide",
    meta_desc="Performance Max uses Google's full inventory across Search, Display, YouTube, Shopping, and Maps. A complete guide to campaign structure, asset groups, audience signals, and ROAS optimization.",
    cat_label="Paid Advertising",
    cat_class="cat-cyan",
    pub_date="May 14, 2026",
    read_mins="10",
    h1_html='Performance Max: <span style="color:var(--accent);">Complete Setup &amp; Optimization Guide</span>',
    lead="Performance Max is Google's most capable campaign type and its least transparent. When configured correctly — right asset groups, audience signals, and budget controls — it consistently outperforms standalone campaigns. When configured poorly, it spends your budget on irrelevant placements with zero insight.",
    cta_service_slug="performance-max",
    cta_service_name="Performance Max",
    body_html="""
<h2>What Performance Max Actually Is</h2>
<p>Performance Max (PMax) is Google's AI-driven campaign type that serves ads across every Google-owned channel from a single campaign: <strong>Search, Display, YouTube, Shopping, Discover, Gmail, and Maps</strong>. Instead of managing separate campaigns for each channel, Google's machine learning decides where to serve your ads, which asset combinations to show, and how to bid — all in pursuit of your stated conversion goal.</p>
<p>The AI works on two axes simultaneously. First, <strong>goal-based bidding</strong>: Google's Smart Bidding predicts the probability that any given impression will result in your target conversion action, then bids accordingly in real time. Second, <strong>asset combination testing</strong>: Google automatically assembles headlines, descriptions, images, videos, and logos into ad creatives and tests which combinations perform best for each placement and audience.</p>
<p>The trade-off is transparency. Unlike Search campaigns where you see keyword-level performance, PMax gives limited placement-level and asset-level reporting. You're buying into Google's AI system — which in 2026 is genuinely powerful — but you're giving up granular control. Understanding that trade-off is the foundation of a good PMax strategy.</p>

<h2>Campaign Structure: One or Multiple PMax Campaigns?</h2>
<p>The question of how many PMax campaigns to run is one of the most consequential structural decisions, and the answer depends on your account type:</p>
<ul>
  <li><strong>E-commerce:</strong> Create separate PMax campaigns by <strong>product category or margin tier</strong>. A campaign that mixes high-margin accessories with low-margin commodities will have Google optimise toward conversion volume, often favouring the lower-margin items because they convert more frequently. Separate campaigns let you set different ROAS targets aligned with each category's actual margins.</li>
  <li><strong>Lead generation:</strong> Separate by <strong>service type</strong> if you offer multiple services with different CPL targets or conversion values. A law firm running campaigns for personal injury and estate planning simultaneously in one PMax campaign will confuse the AI's value optimisation.</li>
  <li><strong>Small budgets (under $3k/month):</strong> One campaign. The AI needs sufficient conversion volume to optimise effectively — splitting a small budget starves both campaigns of the data they need. Target 50+ conversions per campaign per month as a minimum threshold.</li>
</ul>
<p>Each campaign has its own budget, which means you can <strong>control spend isolation</strong> between product lines. This is critical for margin management: if your hero products and your low-margin products compete in the same budget pool, the algorithm will spend toward whichever drives easier conversions regardless of profitability.</p>

<h2>Asset Groups: The Most Important Setup Decision</h2>
<p>Asset groups are PMax's equivalent of ad groups — they contain the creative assets (headlines, descriptions, images, videos, logos) that Google assembles into ads. Think of each asset group as a <strong>creative theme</strong> aligned to a specific product, service, audience, or seasonal message.</p>
<p>The required assets per asset group: <strong>up to 15 headlines</strong> (at least 3 required), <strong>up to 5 descriptions</strong> (at least 2 required), <strong>up to 20 images</strong> (various aspect ratios), <strong>logos</strong>, and <strong>at least one video</strong> (Google will auto-generate a video if you don't provide one — and auto-generated videos are almost always worse than what you'd create).</p>
<p>Asset quality score (Excellent/Good/Low) is a signal of how varied and strong your assets are. A "Low" asset strength rating typically means you have too few headlines, they're too similar to each other, or your images are low-resolution. Improving from Low to Excellent has been shown to improve campaign performance by 12–20% in Google's own data — and our client experience corroborates this.</p>
<p>Structure asset groups around <strong>themes, not channel types</strong>. One asset group for "Running Shoes — Men" with images of men running, headlines about performance and fit, and product-specific descriptions. Another for "Running Shoes — Women" with appropriate creative variations. Don't put all products in one asset group; you'll get generic creative that speaks to no one specifically.</p>

<h2>Audience Signals: Guide the AI Without Limiting It</h2>
<p>Audience signals are one of the most misunderstood PMax features. They are <strong>hints to the AI about where to start looking</strong>, not hard targeting restrictions. Google will always serve beyond your audience signals if it believes other audiences will convert. This is by design — and often beneficial, as the AI frequently finds converting audiences you wouldn't have thought to target.</p>
<p>The hierarchy of effective audience signals, strongest to weakest:</p>
<ul>
  <li><strong>Customer match lists</strong> — your actual buyer data (email lists, CRM exports) is the highest-quality signal. Upload your existing customer list as the primary audience signal and Google will find similar people.</li>
  <li><strong>Website visitors</strong> — your existing site visitors, segmented by page type or recency where possible, give the AI a strong behavioural signal.</li>
  <li><strong>Similar segments</strong> — Google's own similar-to-converters lists are solid secondary signals, particularly for accounts without large customer lists.</li>
  <li><strong>Interest and in-market segments</strong> — use these as supplementary signals when customer data is limited, but don't over-rely on them; they're less predictive than first-party data.</li>
</ul>
<p>One important configuration note: <strong>do not add your customer list as a conversion exclusion</strong> unless you have a specific reason (e.g., you never want to advertise to existing customers). Many advertisers exclude their customer list from targeting, which removes your best lookalike seed from the AI's optimisation signal.</p>

<h2>Bidding Strategy and Budget Controls</h2>
<p>PMax supports two primary bidding strategies: <strong>Maximize Conversion Value</strong> (with or without a Target ROAS) and <strong>Maximize Conversions</strong> (with or without a Target CPA). For most e-commerce accounts, use Maximize Conversion Value with tROAS. For lead generation, use Maximize Conversions with tCPA.</p>
<p>The critical mistake with tROAS targets: <strong>setting them too high too early</strong>. If your historical ROAS is 4x and you set a 5x tROAS target from day one, Google will severely restrict delivery looking for those elusive high-value conversions, spending very little while the campaign starves for data. Instead: start at 80–90% of your historical average ROAS, let the campaign run for 4–6 weeks (minimum 50 conversions), then incrementally raise the target by 10–15% each time.</p>
<p>Budget pacing with PMax can be erratic in the first 2–3 weeks while the AI is in learning mode. Don't panic if daily spend is uneven. The algorithm catches up. However, if spend drops dramatically (below 50% of budget) after week 3 with good asset quality and reasonable tROAS targets, your targets are likely too aggressive.</p>

<h2>Optimization and Reporting</h2>
<p>PMax's limited reporting is a genuine challenge, but there are actionable levers. The <strong>asset group performance breakdown</strong> (available once you have sufficient conversion volume) shows which creative themes are driving results — use this to iterate, refreshing underperforming asset groups with new creative every 4–6 weeks.</p>
<p>The <strong>Search terms insight report</strong> (in Insights tab) shows categories of search terms your PMax ads matched, grouped by theme. While not keyword-level, it's essential for identifying wasted spend categories where you should add negative keywords. Note: negative keywords in PMax can only be applied at the campaign level via the Google Ads support team or through campaign settings — they don't work the same way as in Search campaigns.</p>
<p>Monthly optimization checklist: refresh lowest-performing assets, review search term categories for irrelevant themes, check audience insights for surprising converting segments, review campaign-level ROAS vs target and adjust by 10–15% if consistently above or below, and ensure your conversion actions are correctly weighted.</p>

<div class="callout">
  <p>Lumo AI Agency configures and manages Performance Max campaigns for e-commerce and lead generation clients — with full asset production and monthly optimization included.</p>
  <a href="/services/performance-max.html">See our Performance Max service &rarr;</a>
</div>
""",
    faqs=[
        ("Should I run Performance Max alongside my existing Search campaigns?",
         "Yes, in most cases. Search campaigns with exact and phrase match keywords will take priority over PMax for queries that match your keywords. Run both: Search for your core high-intent keywords with granular bid control, and PMax to capture additional inventory across all Google channels. Monitor for cannibalization in your Search terms report."),
        ("How long does Performance Max take to exit learning mode?",
         "PMax typically needs 4–6 weeks to fully exit learning mode and stabilise performance. During this period, avoid making significant changes (budget shifts over 20%, bid strategy changes, major asset additions) as each change resets the learning period. Plan to evaluate performance starting week 5–6, not week 2."),
        ("My Performance Max campaign has a low asset strength rating — does it matter?",
         "Yes, it matters meaningfully. Low asset strength usually means too few unique headlines, similar descriptions, or missing video assets. Google's data shows Excellent asset strength campaigns outperform Low by double digits. Add more varied headlines (covering different value propositions), add original video if missing, and ensure you have the full range of image aspect ratios (1:1, 4:5, 16:9, 1.91:1)."),
    ]
))

# ── 3. tiktok-ads-guide ───────────────────────────────────────────────────
articles.append(dict(
    slug="tiktok-ads-guide",
    title="TikTok Ads in 2026: Complete Setup Guide for B2C Brands",
    meta_desc="TikTok's algorithm rewards relevance over budget. How to structure TikTok ad campaigns, write creative briefs for UGC-style videos, choose the right formats, and find profitable CPAs for your brand.",
    cat_label="Paid Advertising",
    cat_class="cat-cyan",
    pub_date="May 14, 2026",
    read_mins="9",
    h1_html='TikTok Ads 2026: <span style="color:var(--accent);">Complete Guide for B2C Brands</span>',
    lead="TikTok Ads remain one of the highest-opportunity paid channels in 2026 — with CPMs 30–60% lower than Meta and an algorithm that distributes content by relevance, not just budget. But creative is everything: bad creative on TikTok burns budget faster than any other platform.",
    cta_service_slug="tiktok-ads",
    cta_service_name="TikTok Ads",
    body_html="""
<h2>TikTok Ad Formats Overview</h2>
<p>TikTok's ad inventory has expanded significantly and choosing the right format for your objective is the first structural decision. Here's how the formats break down by use case:</p>
<ul>
  <li><strong>In-Feed Ads</strong> — the workhorse format. Appear natively in the For You Page feed between organic content. Full-screen, sound-on, skippable after a few seconds. This is where the majority of TikTok ad budgets run. Works for all objectives from awareness to direct purchase.</li>
  <li><strong>Spark Ads</strong> — boost an existing organic TikTok post (yours or a creator's, with permission) as a paid ad. The key advantage: engagement (comments, likes, shares) accumulates on the original post, building social proof. When you have an organic video performing well, Sparking it typically outperforms running a separate In-Feed Ad.</li>
  <li><strong>TopView</strong> — the first ad shown when a user opens TikTok. Premium placement, premium CPMs. Best for major brand launches, product reveals, or time-sensitive campaigns where maximum reach matters more than cost efficiency.</li>
  <li><strong>Shopping Ads</strong> — catalog-connected ads that surface your product feed directly in TikTok. In 2026, TikTok Shop integration means users can complete purchases without leaving the app. For e-commerce brands with a product catalog, Shopping Ads are increasingly essential.</li>
  <li><strong>Brand Takeover and Branded Hashtag Challenges</strong> — large-budget awareness formats ($50k+ minimums) suited for enterprise campaigns. Not relevant for most mid-market brands.</li>
</ul>

<h2>Campaign Structure</h2>
<p>TikTok Ads Manager uses a three-level structure: Campaign (objective) → Ad Group (audience and placement) → Ad (creative). Getting the campaign objective right is foundational because it determines which conversion events TikTok optimizes for.</p>
<p>The three objective tiers and when to use them:</p>
<ul>
  <li><strong>Awareness</strong> (Reach, Video Views) — maximises impressions at lowest CPM. Use for brand launches, retargeting for brand recall, or warming up cold audiences before a conversion push.</li>
  <li><strong>Consideration</strong> (Traffic, Video Views at 6-second/2-second completion, Engagement, App Installs) — mid-funnel objectives that drive engaged interactions. Traffic campaigns to landing pages work when your funnel is long and you're building email lists. App Install campaigns for mobile apps.</li>
  <li><strong>Conversion</strong> (Website Conversions, Catalog Sales, Lead Generation) — the objective for direct-response e-commerce and lead gen. Requires TikTok Pixel or Events API installed and at least 50 conversion events per week per ad group for the algorithm to optimise effectively.</li>
</ul>
<p>A full-funnel TikTok structure for a growing e-commerce brand might look like: Conversion campaign for warm audiences (website visitors, customer lookalikes) + Awareness/Consideration campaigns for cold audiences using video-view objectives, then retarget video viewers with conversion-objective campaigns at a lower CPM than running straight cold conversion traffic.</p>

<h2>Creative Strategy: What Actually Works on TikTok</h2>
<p>TikTok's creative requirements are distinct from every other paid platform, and brands that bring polished TV-commercial aesthetics consistently underperform against brands making native-looking content. The principles that hold in 2026:</p>
<ul>
  <li><strong>Hook in the first 2 seconds.</strong> TikTok's skip rate is brutal. The opening frame needs an immediate pattern interrupt: a surprising statement, a bold visual, a question, or showing the "after" before explaining the "before." If your video starts with a logo or a brand intro, you've already lost most of the audience.</li>
  <li><strong>Look like organic content, not an ad.</strong> The best-performing TikTok ads are shot vertically on a phone, feel slightly imperfect, and match the aesthetic of organic TikToks. Overly produced creative signals "advertisement" to the algorithm and the viewer simultaneously.</li>
  <li><strong>UGC-style over polished production.</strong> User-generated content — someone filming themselves using the product, talking directly to camera, reacting genuinely — outperforms studio-shot ads at a ratio of roughly 3:1 on TikTok. This is partly algorithmic preference and partly the cultural expectation of TikTok users.</li>
  <li><strong>Product demonstration over lifestyle.</strong> Showing the product doing something specific and impressive converts better than aspirational lifestyle imagery. "Watch how this serum changed my skin in 14 days" outperforms "Feel beautiful, feel confident."</li>
  <li><strong>Creator partnerships vs in-house.</strong> Partnering with micro-creators (50k–500k followers) in your niche frequently produces the highest-performing creative at a manageable cost. Their audiences trust them; their content style is natively TikTok-appropriate. For Spark Ads, creator-originated content usually outperforms brand-originated even with identical ad spend.</li>
</ul>

<h2>Targeting on TikTok</h2>
<p>TikTok's targeting options are less granular than Meta's — you can't target by job title, relationship status, or the detailed behavioural categories that Meta has built over a decade. But for B2C brands, TikTok's targeting is effective enough, and the algorithm's organic distribution capability compensates for targeting limitations when creative is strong.</p>
<p>The targeting options available and how to use them:</p>
<ul>
  <li><strong>Interest targeting</strong> — broad categories (Beauty, Fitness, Gaming, Food). Use as a starting signal but don't over-restrict. TikTok's algorithm finds relevant users based on content engagement even within broad interest categories.</li>
  <li><strong>Behavioral targeting</strong> — users who've interacted with certain video types, followed certain creators, or engaged with specific hashtags. More precise than interests and underused by most advertisers.</li>
  <li><strong>Custom Audiences</strong> — customer email lists, website visitors (via Pixel), app event data. These are your highest-value targeting pools for retargeting and should anchor your conversion-objective campaigns.</li>
  <li><strong>Lookalike Audiences</strong> — TikTok's lookalikes from your customer list or pixel data. Quality improves significantly once your pixel has 1,000+ conversion events; before that, use broader interest targeting.</li>
</ul>
<p>A counterintuitive TikTok truth: <strong>broad targeting often outperforms narrow targeting</strong> when you have strong creative. TikTok's algorithm is exceptionally good at finding the right people within a large pool. Over-restricting targeting (narrow age range + specific interests + small geography) limits the algorithm's ability to optimise and frequently increases CPMs without improving conversion quality.</p>

<h2>Measuring and Scaling</h2>
<p>TikTok attribution defaults to a <strong>7-day click, 1-day view</strong> attribution window. This is more generous than many platforms, meaning some conversions TikTok claims credit for would have occurred anyway. Cross-reference TikTok's reported conversions with GA4 to understand true incrementality — typically, GA4 shows 30–50% fewer TikTok-attributed conversions than TikTok Ads Manager reports due to attribution window differences and cookie limitations.</p>
<p>TikTok conversions frequently appear as <strong>direct or social traffic in GA4</strong> rather than as paid social, because TikTok's in-app browser and app environment doesn't always pass UTM parameters correctly. Use the TikTok Events API (server-side) for more reliable conversion attribution back to TikTok Ads Manager, and append UTM parameters to all destination URLs.</p>
<p>Scaling on TikTok: when a creative is winning, <strong>duplicate the ad group</strong> rather than increasing the budget of the existing one. Budget increases of more than 20% in a single change typically reset the ad group's optimisation and cause performance to dip. Creative fatigue is the primary scaling limiter on TikTok — watch for CTR dropping 30%+ week-over-week and CPMs increasing as signals to refresh creative. Plan for a new creative batch every 3–4 weeks on active campaigns.</p>

<div class="callout">
  <p>Lumo AI Agency manages TikTok Ads campaigns end-to-end — creative strategy, UGC briefs, campaign setup, and weekly optimization.</p>
  <a href="/services/tiktok-ads.html">Explore our TikTok Ads service &rarr;</a>
</div>
""",
    faqs=[
        ("What budget do I need to start TikTok Ads?",
         "TikTok's campaign minimum is $50/day and ad group minimum is $20/day. For meaningful data and algorithm optimisation, plan for at least $3,000–$5,000/month. Below that, conversion-objective campaigns won't get the 50 weekly events needed to exit the learning phase. Start with Traffic or Video Views objectives if budget is limited, then layer in conversion campaigns once you understand your creative performance."),
        ("Do I need to make TikTok videos myself or can I hire creators?",
         "Both work, but creator-produced content typically outperforms brand-produced content in TikTok's environment. Consider partnering with 2–4 micro-creators (50k–200k followers) in your niche for initial creative testing. Their content tends to be natively formatted for TikTok, their audience trust lends credibility, and you can Spark their posts as paid ads if they perform organically."),
        ("How does TikTok Ads compare to Meta Ads for e-commerce?",
         "TikTok typically offers lower CPMs (30–60% cheaper than Meta in 2026), making it excellent for top-of-funnel awareness and video view campaigns. Meta's retargeting infrastructure and Advantage+ Shopping campaigns are often more efficient for direct conversion of warm audiences. Running both platforms with TikTok as awareness/discovery and Meta for retargeting is a strong full-funnel approach for e-commerce brands with $10k+/month budgets."),
    ]
))

# ── 4. linkedin-ads-guide ─────────────────────────────────────────────────
articles.append(dict(
    slug="linkedin-ads-guide",
    title="LinkedIn Ads for B2B: The Complete Pipeline Generation Guide",
    meta_desc="LinkedIn Ads are expensive per click and powerful per conversion for senior B2B buyers. Complete guide to campaign setup, targeting, formats, offer strategy, and measuring pipeline ROI.",
    cat_label="Paid Advertising",
    cat_class="cat-cyan",
    pub_date="May 14, 2026",
    read_mins="10",
    h1_html='LinkedIn Ads for B2B: <span style="color:var(--accent);">The Pipeline Generation Guide</span>',
    lead="LinkedIn's $15–$80 CPC makes most marketers flinch. Then they see the close rates. When you're reaching CFOs and VPs with a relevant offer, LinkedIn Ads consistently generate the highest-value pipeline of any paid channel — the math just requires patience and the right offer.",
    cta_service_slug="linkedin-ads",
    cta_service_name="LinkedIn Ads",
    body_html="""
<h2>Why LinkedIn Despite the High CPC</h2>
<p>The sticker shock is real. LinkedIn CPCs typically run $15–$80 depending on industry, seniority, and campaign type — compared to $1–$5 on Facebook or $2–$10 on Google Display. But the relevant comparison isn't CPC; it's <strong>cost per qualified pipeline opportunity</strong>.</p>
<p>A $40 CPC with a 10% landing page conversion rate and a 30% lead-to-opportunity rate produces a $1,333 cost per opportunity. For an enterprise software product with a $60,000 ACV, that's a phenomenal CAC. Compare this to Google Search, where a $5 CPC might yield lower-quality leads that convert to opportunities at 5%, producing a similar or worse cost per opportunity despite the lower CPC headline.</p>
<p>The reason LinkedIn's conversion quality justifies the cost: <strong>no other platform lets you simultaneously target by job title, company size, seniority, geography, and industry</strong>. On Facebook, you can target "Small Business Owner" — but that bucket includes every one-person Etsy shop alongside $10M revenue companies. On LinkedIn, you can target VP of Finance at companies with 500–5,000 employees in SaaS, who are 5+ years into their careers. That specificity is worth a premium.</p>
<p>The mental model shift that makes LinkedIn work: stop thinking cost-per-click and start thinking cost-per-ICP (ideal customer profile). If each lead that comes through LinkedIn is 3x more likely to be your ICP than a lead from other channels, a 3x higher CPC is break-even — and LinkedIn frequently delivers that quality differential.</p>

<h2>Campaign Types and When to Use Each</h2>
<p>LinkedIn Campaign Manager offers several ad formats, each suited to specific funnel stages and objectives:</p>
<ul>
  <li><strong>Sponsored Content</strong> — single image, carousel, or video ads in the LinkedIn feed. This is where the majority of LinkedIn budgets should run. Feed ads feel native, accommodate long copy (unlike most platforms), and work across the full funnel from awareness content to gated asset downloads.</li>
  <li><strong>Message Ads (formerly Sponsored InMail)</strong> — direct messages sent to LinkedIn inboxes. High open rates (30–50%) because they arrive in a dedicated notifications area. Best for high-specificity offers (personalised event invitations, tailored outreach to a precise audience segment). More expensive on a per-send basis but very effective for account-based approaches.</li>
  <li><strong>Lead Gen Forms</strong> — the most important LinkedIn-specific format for direct response. Opens a LinkedIn-native form (pre-filled with the user's LinkedIn data — name, title, company, email) when a user clicks your CTA. Eliminates the landing page friction step. Converts at 2–3x the rate of website conversion campaigns for most lead gen offers.</li>
  <li><strong>Document Ads</strong> — allows users to scroll through a multi-page PDF (research report, playbook, framework) in the feed before deciding to download. Excellent for long-form gated content where you want prospects to sample the value before committing their contact information.</li>
  <li><strong>Conversation Ads</strong> — branching message sequences in LinkedIn inbox with multiple CTA options. Useful for account-based marketing campaigns where you want to offer prospects a personalised path (book a demo vs. read a case study vs. attend a webinar).</li>
</ul>

<h2>Targeting: LinkedIn's Superpower</h2>
<p>LinkedIn's targeting is where the platform's B2B value is most concentrated. The nuances matter enormously:</p>
<ul>
  <li><strong>Job Title vs Job Function vs Seniority</strong> — Job Title targeting is intuitive but has an Achilles heel: people describe the same role differently ("Head of Growth," "Growth Marketing Manager," "Director of Acquisition"). Use Job Function + Seniority combinations for broader reach that doesn't miss people with non-standard titles. Use Job Title for highly specific roles where title language is standardised (e.g., "Chief Financial Officer").</li>
  <li><strong>Company Size + Industry</strong> — the backbone of most B2B targeting. Define your ICP's company size range (employees or revenue) and industry, then layer on seniority. This combination tends to give you a large enough audience to run efficiently while being meaningfully targeted.</li>
  <li><strong>Skills targeting</strong> — underused and often effective. If your ICP has specific technical skills listed on LinkedIn (Salesforce, AWS, Kubernetes), targeting by skill reaches people with proven expertise in your domain, often at lower competition than job title targeting.</li>
  <li><strong>Company Name targeting (ABM)</strong> — upload a list of target accounts (max 300,000 companies) and serve ads exclusively to employees at those companies. Essential for account-based marketing campaigns. Combine with seniority targeting to reach the decision-makers at your named accounts specifically.</li>
  <li><strong>Matched Audiences</strong> — retarget your website visitors (requires LinkedIn Insight Tag), upload customer or prospect lists for exclusion or targeting, build lookalike audiences from your converters. First-party data targeting on LinkedIn is consistently your highest-performing audience pool.</li>
</ul>

<h2>Offer and Creative Strategy for B2B</h2>
<p>The offer is the make-or-break variable in LinkedIn advertising. The mistake most B2B advertisers make: leading with a demo request to cold audiences who have never heard of your company. The same people who would never cold-call a stranger are willing to ask a stranger to book a 30-minute demo with their sales team.</p>
<p>The offer hierarchy for cold audiences, from highest to lowest friction:</p>
<ul>
  <li><strong>Research reports and original data</strong> — "2026 State of B2B SaaS Spending" — highest download rates because the value is clear and immediate. Gate with Lead Gen Forms.</li>
  <li><strong>Webinars and virtual events</strong> — lower friction than demos, delivers value, builds relationship. "How [Company Type] Cut CAC by 35% in Q1" is more compelling than a generic webinar.</li>
  <li><strong>Guides, frameworks, and templates</strong> — practical tools that help your ICP do their job. Credibility-building that positions you as the expert before the sales conversation.</li>
  <li><strong>Case studies</strong> — work best when highly specific to the prospect's industry and company size. "How a 200-person SaaS company reduced churn by 22%" outperforms generic customer stories.</li>
  <li><strong>Free audit or assessment</strong> — transitional offer between content and demo. Provides specific value (your expert looks at their setup) without the full sales-meeting commitment. Works well for warm audiences who've already engaged with content.</li>
  <li><strong>Product demo</strong> — reserve for warm audiences (website visitors, webinar attendees, content downloaders). Asking for a demo from cold audiences wastes your expensive LinkedIn clicks.</li>
</ul>
<p>On creative: <strong>professional doesn't mean boring</strong>. LinkedIn's feed has plenty of generic blue-and-white corporate imagery. Bold headlines, contrarian data points ("Most B2B sales teams are measuring the wrong KPIs"), and direct calls-out to specific roles ("If you manage paid media spend over $50k/month…") outperform generic brand imagery. Specificity signals relevance, and relevance drives clicks from the exact people you want.</p>

<h2>Lead Gen Forms vs Website Conversion</h2>
<p>This is one of the most common and consequential setup decisions in LinkedIn advertising. The data consistently shows:</p>
<ul>
  <li><strong>Lead Gen Forms deliver 2–3x more leads at 40–60% lower CPL</strong> because the pre-filled LinkedIn data eliminates the landing page drop-off (typically 70–85% of paid clicks never convert on landing pages).</li>
  <li><strong>But Lead Gen Form leads are lower quality</strong> on average — the friction reduction means less-engaged prospects also convert, and the automatic data fill means prospects sometimes submit without fully reading the offer details.</li>
</ul>
<p>The strategic answer: <strong>use Lead Gen Forms for top-of-funnel content offers</strong> (reports, guides, webinars) where volume matters and your sales team can qualify. <strong>Use website conversion campaigns for demo and consultation requests</strong> where the friction of visiting a landing page filters for higher intent, and the website experience itself builds credibility before the form submission.</p>

<h2>Budget, Bidding, and Scaling</h2>
<p>LinkedIn requires meaningful budget to gather actionable data. The practical minimums: <strong>$3,000/month</strong> to gather meaningful CPL data within 60–90 days. Below that, you'll have insufficient volume to make statistically sound optimisation decisions.</p>
<p>Bidding: start with <strong>Manual CPC bidding</strong> at the suggested bid to win competitive auctions and gather click data. Once you have 50+ conversions per campaign, transition to <strong>Automated Bidding with a Max CPA cap</strong>. LinkedIn's automated bidding system has improved substantially and typically reduces CPL by 15–25% over manual once it has sufficient conversion data.</p>
<p>Scaling on LinkedIn is primarily done through <strong>audience expansion</strong> (lookalike audiences from converters, broader seniority ranges, adjacent job function targeting) and <strong>creative testing at scale</strong> (run 3–5 creative variants per campaign, retire bottom performers after 2 weeks, always have a new creative ready to replace them). Budget increases over 20% in a single change tend to disrupt performance — scale budgets gradually, 15–20% per week when metrics support it.</p>

<div class="callout">
  <p>Lumo AI Agency builds LinkedIn Ads pipelines for B2B companies targeting enterprise buyers — from audience strategy to offer design to campaign execution.</p>
  <a href="/services/linkedin-ads.html">Explore our LinkedIn Ads service &rarr;</a>
</div>
""",
    faqs=[
        ("Is LinkedIn Ads worth it for SMBs or only enterprise?",
         "LinkedIn is most cost-effective when your deal size justifies the higher CPCs — typically $10,000+ ACV for SaaS or professional services, or high-ticket consulting engagements. For SMBs selling to small business owners with $2,000–$5,000 deal sizes, the CPC-to-LTV math often doesn't work. LinkedIn is best used to reach larger-company decision-makers; if your ICP is a small business owner, Meta or Google may offer better ROI."),
        ("How long does it take to see results from LinkedIn Ads?",
         "Budget for 60–90 days before drawing strong conclusions. LinkedIn's algorithm needs 2–4 weeks to exit learning mode, and B2B buying cycles mean leads from week 1 may not become opportunities until week 8–12. The mistake is optimising too early: changing targeting or offers after 2 weeks of data produces whiplash rather than improvement. Set a 90-day review cycle for major strategic decisions."),
        ("Should I exclude my current customers from LinkedIn targeting?",
         "Yes, always exclude current customer company names and email lists from prospecting campaigns. Serving acquisition ads to existing customers wastes budget and can create confusing messaging. Upload your customer domain list as an exclusion audience. Conversely, you can create a separate LinkedIn campaign targeting existing customers with expansion, upsell, or retention messaging — but keep it fully separate from your prospecting campaigns."),
    ]
))

# ── 5. retargeting-strategy ───────────────────────────────────────────────
articles.append(dict(
    slug="retargeting-strategy",
    title="Retargeting Strategy: How to Re-Engage the 97% Who Don't Convert",
    meta_desc="97% of visitors leave without converting. A multi-platform retargeting strategy brings them back — here's how to structure audiences, choose platforms, create effective sequences, and avoid ad fatigue.",
    cat_label="Paid Advertising",
    cat_class="cat-cyan",
    pub_date="May 14, 2026",
    read_mins="9",
    h1_html='Retargeting Strategy: <span style="color:var(--accent);">Re-Engage the 97% Who Don\'t Convert</span>',
    lead="The average website conversion rate is 2–3%. That means 97% of people who found your site, considered your offer, and left are now addressable through retargeting — and they convert at 10x the rate of cold audiences. The question isn't whether to retarget, it's how to structure it.",
    cta_service_slug="retargeting",
    cta_service_name="Retargeting",
    body_html="""
<h2>How Retargeting Works</h2>
<p>Retargeting works by placing a small piece of code (a pixel or tag) on your website that fires when a user visits. This tag drops a cookie in the user's browser and records the visit in the ad platform's database. When that user later browses other websites, watches YouTube, scrolls Instagram, or searches Google, the ad platform recognises them and serves your ad.</p>
<p>Each major platform has its own tracking mechanism: <strong>Meta Pixel</strong> (plus Conversions API for server-side), <strong>Google Tag</strong> (for Google Ads remarketing lists), <strong>LinkedIn Insight Tag</strong> (for LinkedIn website retargeting), and <strong>TikTok Pixel</strong>. Install all that are relevant to your advertising platforms as early as possible — audience pools build over time, and you can't retroactively add people who visited before the pixel was installed.</p>
<p>Privacy changes have meaningfully reduced retargeting effectiveness over the past few years. <strong>Apple's ITP</strong> limits cookie lifetime to 7 days on Safari (limiting the window for retargeting). <strong>iOS 14+ App Tracking Transparency</strong> requires user opt-in for tracking on iOS apps, reducing Meta's and other platforms' ability to track actions across apps and websites. <strong>Cookie consent tools</strong> (required under GDPR and increasingly under US state privacy laws) reduce the percentage of visitors who are tracked when they decline consent.</p>
<p>The practical impact: your retargeting audience pools are typically <strong>60–70% of what they would have been in 2020</strong>. First-party data (email lists, CRM data) has become far more valuable as a retargeting seed because it isn't affected by browser privacy changes — it works through customer list uploads and hashed email matching.</p>

<h2>Segmenting Your Retargeting Audiences by Intent</h2>
<p>Not all website visitors are equal. The most important structural decision in retargeting is <strong>segmenting your audience pools by behavioural intent signals</strong>, then serving different ads and offers to each segment. Running one giant "all visitors" retargeting campaign is leaving most of the value on the table.</p>
<ul>
  <li><strong>All visitors (last 30 days)</strong> — broadest pool, lowest average intent. Best for brand recall ads: lighter creative, social proof content, educational value. CPMs are typically low here. Don't oversell; most of this audience is still in early consideration.</li>
  <li><strong>Specific page visitors</strong> — people who visited a specific service page, product category, or pricing page. Significantly higher intent than general visitors. Serve ads referencing the specific thing they looked at. A visitor to your "Enterprise SEO" page should see ads about enterprise SEO, not your generic homepage messaging.</li>
  <li><strong>Video viewers (50%+ completion)</strong> — people who've demonstrated engagement with your content. Warmer than page visitors who bounced after 10 seconds. Serve more consideration-stage content: testimonials, detailed comparisons, specific case studies.</li>
  <li><strong>Email subscribers and CRM contacts</strong> — highest-quality first-party data audience. Upload customer and prospect lists and match via hashed email. These people are already in your funnel; serve them content that accelerates the purchase decision rather than re-introducing your brand.</li>
  <li><strong>Cart abandoners and form starters</strong> — the highest-intent non-converters. Someone who put items in a cart or started filling out a contact form and then left is very close to conversion. Serve urgency-creating ads: reminder of what they left, limited-time offer, social proof that removes final objections.</li>
</ul>

<h2>Platform Strategy</h2>
<p>Retargeting across multiple platforms simultaneously can feel like comprehensive coverage, but with limited budgets it fragments your audience pools too thinly to gather optimisation data. <strong>Prioritise platforms by where your customer actually spends time</strong>:</p>
<ul>
  <li><strong>Meta (Facebook and Instagram)</strong> — the largest reach for retargeting of any single platform. Dynamic Product Ads (DPA) automatically serve the exact product a visitor viewed, making them essential for e-commerce retargeting with catalogs. Meta's retargeting is best for B2C, e-commerce, and consumer services. Strong for cart abandoner recovery campaigns.</li>
  <li><strong>Google Display Network</strong> — CPMs are generally lower than Meta, and Display reaches users across millions of websites and apps (including YouTube). Less precise targeting but excellent for brand recall at scale. Particularly effective for B2B companies where buyers do research across many industry websites.</li>
  <li><strong>LinkedIn</strong> — for B2B companies, LinkedIn retargeting of pricing page and case study visitors is extremely high-value. Reaching a VP who visited your enterprise software pricing page with a case study from their industry converts at exceptional rates. CPMs are high, so reserve for your highest-intent B2B audience segments.</li>
  <li><strong>Programmatic retargeting</strong> — via DSPs (demand-side platforms) gives access to a wider inventory pool at potentially lower CPMs for large audience pools. Best suited for brands with 50,000+ monthly visitors where audience pool size supports programmatic buying.</li>
</ul>

<h2>Creative and Offer Strategy Per Segment</h2>
<p>The creative and offer you show each retargeting segment should match where they are in the decision process. Using the same ad for a cart abandoner and a one-time homepage visitor is a strategic error:</p>
<ul>
  <li><strong>Cold visitors (homepage, blog, early-stage content)</strong> — focus on building trust, not closing. Customer reviews, media logos ("As seen in"), statistics about results, educational content. The goal is to move them to the next consideration stage, not to generate an immediate conversion.</li>
  <li><strong>Product or service page visitors</strong> — serve creative that references what they looked at specifically. If Meta DPA is an option (e-commerce with catalog), let the algorithm serve the exact product. Otherwise, create audience-specific ads: "Still thinking about [service]? Here's what clients say."</li>
  <li><strong>Pricing page visitors</strong> — this audience has done enough research to look at pricing. They need final objection removal: strong testimonials, a specific ROI claim, a risk-reversal offer (free trial, money-back guarantee, free audit). Urgency messaging can work here if genuine (seasonal offer, limited spots).</li>
  <li><strong>Cart abandoners / form starters</strong> — direct, specific, action-oriented. "You left something behind." Show the exact product. Offer a small incentive if margin allows (free shipping, 10% off). Create urgency with stock messaging or a time-limited offer. This is the segment where every dollar of retargeting spend has the highest return.</li>
</ul>

<h2>Frequency Caps and Avoiding Ad Fatigue</h2>
<p>Retargeting's biggest failure mode is oversaturation — showing the same ads to the same small audience so frequently that they start generating negative sentiment rather than conversions. The symptoms are unmistakable: <strong>CPM increases</strong> (the platform charges more as your audience fatigues), <strong>CTR drops</strong> (people are tuning out your ads), and in worst cases, <strong>negative comments on your ads</strong> ("I'm seeing this everywhere, please stop.").</p>
<p>Recommended frequency caps by platform: <strong>Meta: 2–3 impressions per person per week</strong> for warm audiences; <strong>LinkedIn: 1–2 impressions per week</strong> for your typically small B2B retargeting pools; <strong>Google Display: 5–7 impressions per week</strong> due to lower CPMs and the expectation of more passive browsing exposure.</p>
<p>Creative refresh cadence is the most important lever for fighting fatigue: <strong>plan for new creative every 3–4 weeks</strong> for your most active retargeting audiences. This doesn't necessarily mean new concepts — different angles on the same offer (different testimonial, different visual, different headline) are sufficient to reset fatigue. Track your ad frequency metrics weekly, and flag any audience segment averaging above 3 impressions per week on Meta as a priority for immediate creative refresh or audience refresh.</p>
<p>Finally, always maintain <strong>conversion exclusion lists</strong>: exclude anyone who has converted in the past 30 days from your standard retargeting campaigns. Showing acquisition ads to recent buyers is wasteful and creates a negative brand experience. Converted buyers can be moved to separate post-purchase campaigns with upsell, referral, or loyalty messaging.</p>

<div class="callout">
  <p>Lumo AI Agency builds structured retargeting systems across Meta, Google, and LinkedIn — with audience segmentation, creative frameworks, and frequency management built in from day one.</p>
  <a href="/services/retargeting.html">Explore our Retargeting service &rarr;</a>
</div>
""",
    faqs=[
        ("How large does my retargeting audience need to be before it's worth running?",
         "Meta requires a minimum of 1,000 people in a custom audience to serve ads. Practically, you need 5,000+ monthly website visitors to build meaningful segmented retargeting pools. For smaller sites, email list uploads (customer match) can supplement thin pixel audiences. LinkedIn retargeting is viable with 300+ matched members, but 1,000+ is where performance becomes stable."),
        ("Does retargeting still work after iOS 14 and cookie changes?",
         "Yes, but audience pools are 30–40% smaller than pre-2021 baselines for browser-based tracking. The solution is first-party data: email list uploads and CRM matching are not affected by iOS privacy changes or cookie deprecation. Invest in growing your email list (and using it as a retargeting seed) and implement server-side tracking (Conversions API, GTM server-side) to recover conversion signal quality."),
        ("What's the right retargeting window — 7 days, 30 days, or 180 days?",
         "Use tiered windows based on your sales cycle length. For impulse e-commerce (under $100): 7–14 day windows with urgency creative. For considered purchases ($100–$1,000): 30–60 day windows. For B2B with long sales cycles: 90–180 day windows with educational content sequences. The longer the window, the less warm the audience — adjust creative and offer intensity accordingly."),
    ]
))

# ── 6. server-side-tracking-guide ─────────────────────────────────────────
articles.append(dict(
    slug="server-side-tracking-guide",
    title="Server-Side Tracking in 2026: Setup Guide for GA4 and Meta",
    meta_desc="iOS privacy changes and cookie deprecation are cutting 20–40% of your conversion data. Server-side tracking restores signal quality. How to implement GTM server-side, GA4 server events, and Meta Conversions API.",
    cat_label="Paid Advertising",
    cat_class="cat-cyan",
    pub_date="May 14, 2026",
    read_mins="10",
    h1_html='Server-Side Tracking 2026: <span style="color:var(--accent);">Restore Your Conversion Signal</span>',
    lead="If you're running Meta Ads without the Conversions API, or Google Ads without server-side conversion events, you're making budget decisions on 60-80% of your data. Studies show server-side tracking recovers 20-40% of conversion events that browser-side tags miss — events that determine how your campaigns are optimised.",
    cta_service_slug="conversion-tracking",
    cta_service_name="Conversion Tracking",
    body_html="""
<h2>Why Browser-Side Tracking Is Failing</h2>
<p>The tracking infrastructure that most advertising campaigns were built on — browser-based JavaScript tags that fire when a user completes an action — is being systematically dismantled by privacy technology. Understanding the specific mechanisms explains why server-side tracking has become essential rather than optional:</p>
<ul>
  <li><strong>Apple's Intelligent Tracking Prevention (ITP)</strong> — Safari (used by approximately 19% of global users but 30%+ in the US on mobile) limits the lifetime of JavaScript-set cookies to 7 days, and first-party cookies set via document.cookie to 7 days as well. This means any user who visits your site and converts more than 7 days later has their original traffic source attribution erased.</li>
  <li><strong>iOS 14+ App Tracking Transparency</strong> — Apple's ATT framework requires apps (including Facebook's) to explicitly ask users for permission to track their activity across apps and websites. Opt-in rates have settled at 25–35%. This means Meta has lost visibility into post-click conversions for 65–75% of iOS users who use the Facebook app, dramatically degrading campaign optimisation signals for iOS traffic.</li>
  <li><strong>Ad blockers</strong> — approximately 27% of US internet users run ad blockers in 2026. Many block not just display ads but also analytics and tracking pixels, including Google Tag and Meta Pixel. A user who converts after bypassing your ad blocker won't have that conversion registered by your browser-side tags.</li>
  <li><strong>Cookie consent tools</strong> — GDPR (EU), CCPA (California), and growing US state privacy legislation requires obtaining consent before setting non-essential tracking cookies. Users who decline consent (typically 15–40% of EU traffic) generate zero browser-side tracking data, even if they later convert.</li>
</ul>
<p>The cumulative effect: a typical e-commerce or SaaS website running only browser-side tracking is <strong>missing 20–40% of its actual conversion events</strong>. More critically, the conversions that are missed are systematically biased toward iOS Safari users — which skews performance data and mis-informs bidding algorithms that are optimising on incomplete conversion signals.</p>

<h2>How Server-Side Tracking Works</h2>
<p>Traditional browser-side tracking: user completes action on your website → JavaScript tag fires in the user's browser → tag sends event data directly to the ad platform (Meta, Google, etc.).</p>
<p>Server-side tracking breaks this chain at the browser: user completes action on your website → your server captures the event → your server sends the event data to ad platforms via their APIs. The browser is no longer the messenger. The key advantages:</p>
<ul>
  <li><strong>Not affected by ITP or Safari cookie limits</strong> — your server's HTTP requests aren't subject to browser cookie restrictions.</li>
  <li><strong>Not blocked by ad blockers</strong> — ad blockers target browser-side JavaScript; they can't intercept server-to-server API calls.</li>
  <li><strong>Richer data available</strong> — server-side events can include data that browsers can't access: server-confirmed purchase values, first-party customer IDs, hashed email and phone for identity matching (improving attribution rates).</li>
  <li><strong>Cookie lifetime control</strong> — set first-party cookies from your server (HTTP-only) to extend the attribution window beyond ITP's 7-day browser limit.</li>
</ul>
<p>The most common implementations in 2026: <strong>Google Tag Manager Server-Side Container</strong> (acts as the central hub, routing events to GA4 and Google Ads via server), <strong>Meta Conversions API</strong> (direct server-to-Meta API integration), and <strong>platform-specific SDKs and Measurement Protocols</strong> (GA4 Measurement Protocol, Snap Conversions API, TikTok Events API).</p>

<h2>Setting Up GTM Server-Side Container</h2>
<p>Google Tag Manager's server-side container acts as a proxy between your website and ad platforms. Your website sends events to the GTM server container, which then forwards them to GA4, Google Ads, Meta, and other platforms — all from your server, not the user's browser.</p>
<p>Step-by-step setup overview:</p>
<ul>
  <li><strong>Create the server container</strong> — in GTM, create a new container with the "Server" type. GTM will provision a server URL (ending in *.gtm-server.appspot.com by default) or let you provide a custom domain.</li>
  <li><strong>Deploy to Google Cloud</strong> — the recommended hosting is Google Cloud Run (serverless, scales to zero when not in use) or App Engine. Google Cloud provides a managed deployment option directly from GTM. Estimated cost: $30–$80/month for a site with 50,000–200,000 monthly visitors.</li>
  <li><strong>Configure clients</strong> — add the GA4 Client to your server container (handles incoming data from your GA4 web tag), and the Meta Client (handles forwarding to Meta's CAPI). Each client tells GTM which incoming event format to expect.</li>
  <li><strong>Update your web container</strong> — modify your existing GA4 Configuration Tag to send events to your server container URL (instead of directly to Google Analytics). This change routes all GA4 events through your server first.</li>
  <li><strong>Add platform tags in server container</strong> — add a GA4 Server Tag (forwards to Google Analytics), a Google Ads Conversion Tag (fires server-side conversion events), and a Meta Conversions API Tag (forwards to CAPI). Configure each with the appropriate API credentials.</li>
  <li><strong>Test with Preview mode</strong> — GTM's server-side preview mode shows you each incoming event and which tags fired. Test every conversion event type before publishing.</li>
</ul>

<h2>Meta Conversions API Implementation</h2>
<p>The Meta Conversions API (CAPI) is Meta's server-side event ingestion endpoint. It works alongside your Meta Pixel (browser-side) using a <strong>deduplication system</strong> that prevents the same conversion from being counted twice.</p>
<p>Critical implementation requirements:</p>
<ul>
  <li><strong>Get your CAPI access token</strong> — in Meta Events Manager, go to Settings → Conversions API → Generate access token. This token authenticates your server's requests to Meta's API.</li>
  <li><strong>Event deduplication</strong> — the most important technical requirement. When both browser Pixel and server CAPI fire for the same event, Meta will count it twice unless you implement deduplication. The mechanism: include an <code>event_id</code> parameter that is identical in both the browser Pixel event and the CAPI server event for the same user action. Meta deduplicates events with matching event_id within a 48-hour window.</li>
  <li><strong>Advanced matching</strong> — the more user data you include with CAPI events, the higher Meta's event match rate (EMQ score). Include hashed versions (SHA-256) of: email address, phone number, first and last name, city, state, zip, and country. A high EMQ score (7+) means Meta can attribute more conversions to the correct ad, improving campaign optimisation.</li>
  <li><strong>Key events to implement</strong> — at minimum: PageView, ViewContent (product/service page), AddToCart (e-commerce), InitiateCheckout, Purchase (with value and currency), Lead (for lead gen). Each event sent via CAPI should include user data, event_name, event_time, event_id, and action_source ("website").</li>
</ul>
<p>Event Match Quality (EMQ) is your north star metric for CAPI health. A score of 6–8 (out of 10) represents strong implementation; below 5 means your matching data is insufficient. Check EMQ in Meta Events Manager weekly until it stabilises above 6.</p>

<h2>GA4 Server-Side Events and Measurement Protocol</h2>
<p>GA4's Measurement Protocol allows you to send events directly to Google Analytics from your server, bypassing the browser entirely. This is separate from the GTM server-side implementation — both can be used together or independently depending on your technical setup.</p>
<p>When to use GA4 Measurement Protocol directly (vs GTM server-side): when you need to send events from back-end processes that have no user session context (e.g., delayed conversions, offline events, subscription renewals), or when your technical team prefers direct API integration over GTM's layer of abstraction.</p>
<p>Required parameters for a GA4 Measurement Protocol request: <strong>client_id</strong> (the GA4 client identifier, which you must store from the browser-side GA4 cookie — typically the _ga cookie value), <strong>events array</strong> (name and parameters of each event), <strong>measurement_id</strong> (your GA4 property's G-XXXXXXXX ID), and <strong>api_secret</strong> (generated in GA4 under Admin → Data Streams → Measurement Protocol API secrets).</p>
<p>Test server-side GA4 events using the <strong>DebugView in GA4</strong> (Admin → DebugView) by adding <code>debug_mode: 1</code> to your event parameters, or validate using the <strong>Realtime report</strong> for live event verification. Measurement Protocol events without a valid client_id won't appear in user-level reports — storing and passing the client_id correctly is the most common implementation error.</p>

<div class="callout">
  <p>Lumo AI Agency implements server-side tracking setups — GTM server containers, Meta CAPI, GA4 Measurement Protocol — that restore conversion data completeness and improve campaign performance.</p>
  <a href="/services/conversion-tracking.html">Explore our Conversion Tracking service &rarr;</a>
</div>
""",
    faqs=[
        ("Do I still need the Meta Pixel if I implement the Conversions API?",
         "Yes. The Pixel and CAPI should run simultaneously in a 'redundant' configuration with deduplication. The Pixel captures real-time browser-side events with session context (page URL, referrer, browser data). CAPI captures server-side events that survive iOS and ad blocker restrictions. Together, deduplicated via event_id, they provide the most complete event coverage. Removing the Pixel while running CAPI alone loses browser-context data that improves event quality."),
        ("How much does GTM server-side hosting cost?",
         "Google Cloud Run pricing for GTM server-side depends on traffic volume. For sites with 20,000–100,000 monthly visitors, expect $30–$60/month. For 100,000–500,000 monthly visitors, $60–$120/month. Google Cloud's free tier covers some usage, and Cloud Run scales to zero (no cost) when there are no requests. This cost is typically recovered many times over by improved campaign performance from better conversion data."),
        ("How do I know if my server-side tracking is working correctly?",
         "Three checks: (1) Meta Events Manager — check Event Match Quality score (target 6+) and compare CAPI-received events vs Pixel-received events for the same event types; the ratio should be close to 1:1 after deduplication. (2) GA4 DebugView — verify server-side events appear with correct parameters. (3) Compare total conversion event volume between your browser-only historical baseline and your server-side post-implementation period; you should see a 10–40% increase in captured events."),
    ]
))

# ── 7. google-shopping-guide ──────────────────────────────────────────────
articles.append(dict(
    slug="google-shopping-guide",
    title="Google Shopping Ads: Complete Campaign Setup and Optimization Guide 2026",
    meta_desc="Google Shopping is consistently the highest-ROAS paid channel for e-commerce. Step-by-step guide to product feed optimisation, campaign structure, bid strategy, negative keywords, and scaling.",
    cat_label="Paid Advertising",
    cat_class="cat-cyan",
    pub_date="May 14, 2026",
    read_mins="11",
    h1_html='Google Shopping Ads: <span style="color:var(--accent);">Complete Setup &amp; Optimization Guide</span>',
    lead="For e-commerce brands, Google Shopping Ads average 2–4x ROAS even before optimization — making them the most efficient paid channel for most product categories. But most brands run poorly structured campaigns and leave 40–60% of potential ROAS on the table through bad feed quality and campaign structure.",
    cta_service_slug="google-shopping",
    cta_service_name="Google Shopping",
    body_html="""
<h2>How Google Shopping Works</h2>
<p>Google Shopping operates fundamentally differently from Search advertising. In Search, you bid on keywords and write ad copy. In Shopping, your <strong>product feed in Google Merchant Center</strong> is the source of truth — it determines which queries your products are eligible to appear for, and the quality of your feed data determines how often and for which searches your products actually show up.</p>
<p>The Shopping auction combines three factors: <strong>your bid</strong>, <strong>product feed quality</strong> (how well your product data matches the user's query — title relevance, data completeness, GTIN accuracy), and <strong>landing page quality</strong> (relevance, page speed, pricing accuracy vs feed). Unlike Search, there are no keywords to bid on directly — Google's algorithm reads your product titles, descriptions, categories, and attributes to match products to search queries.</p>
<p>Shopping ads appear in multiple placements: <strong>SERP top and right rail</strong> (the image carousels at the top of Google search results), the <strong>Google Shopping tab</strong> (dedicated shopping search experience), <strong>Google Images</strong>, <strong>YouTube</strong> (for Performance Max campaigns), and <strong>Google partner sites</strong>. For e-commerce, Shopping typically drives higher ROAS than Search because the visual format (product image, price, store name) gives shoppers exactly the information they need to make a click decision — only motivated buyers click.</p>

<h2>Product Feed Optimisation (The Most Impactful Lever)</h2>
<p>Feed quality is the highest-leverage variable in Shopping Ads, yet most advertisers treat it as a one-time setup task rather than an ongoing optimisation priority. A well-optimised feed consistently outperforms a mediocre feed by 30–80% on impression share and ROAS for the same bid levels. Here's where the optimisation lives:</p>
<ul>
  <li><strong>Product titles</strong> — the single most important feed attribute. Google's algorithm reads titles like a Search ranking signal. The optimal title structure: <code>[Brand] + [Product Type] + [Key Differentiator] + [Size/Color/Variant]</code>. "Nike Air Max 270 Men's Running Shoe Navy Blue Size 10" beats "Air Max 270" in every competitive category. Front-load the most important terms — Google truncates titles in the ad unit and reads earlier terms as more significant.</li>
  <li><strong>Product descriptions</strong> — write 500–1,000 character descriptions that are keyword-rich and genuinely descriptive. Include secondary search terms that don't fit in the title (use case, material, compatibility, key benefits). Descriptions contribute to Google's understanding of your product even though they're not always displayed in the ad unit.</li>
  <li><strong>Product type taxonomy</strong> — use Google's Product Category taxonomy for campaign segmentation and bid management. A clear, specific product type (Apparel &amp; Accessories &gt; Shoes &gt; Athletic Shoes) helps Google match your products to the right queries and lets you structure campaigns and bids by category.</li>
  <li><strong>GTINs (Global Trade Item Numbers)</strong> — for branded products (products with a manufacturer's barcode/UPC), providing the correct GTIN significantly improves your shopping auction quality score. Google cross-references GTINs against its own product database to verify and enrich your product data. Missing GTINs on products where they exist is a common feed error that suppresses impressions.</li>
  <li><strong>Images</strong> — high-resolution (minimum 800x800px, ideally 1200x1200px or larger), clean background preferred for most categories (white background for apparel and accessories, lifestyle imagery works well for home goods and furniture). Google penalises watermarked images, promotional overlays, and low-resolution files. Image quality directly affects click-through rate once your ad appears.</li>
  <li><strong>Price accuracy</strong> — Google crawls your landing pages and compares prices to your feed. Discrepancies result in product disapproval. If you run promotions that change prices, ensure your feed updates within the same crawl cycle. Use Google's Merchant Center promotion features for sale pricing rather than manually updating base prices.</li>
</ul>

<h2>Campaign Structure</h2>
<p>Google Shopping campaign structure determines your bidding control and your ability to push budget toward your most profitable products. The foundational principle: <strong>products with different margins, conversion rates, and strategic priorities should not share campaigns or ad groups at the same bid level</strong>.</p>
<ul>
  <li><strong>Standard Shopping campaigns</strong> — the most controllable Shopping campaign type. Uses negative keywords to filter irrelevant queries, bids by product group (you can set different bids for different product categories, brands, custom labels, or individual items). Most granular control over which products appear for which queries.</li>
  <li><strong>Performance Max with Shopping feed</strong> — Google's replacement for Smart Shopping (which was deprecated). Provides Shopping distribution plus Display, YouTube, and Search via a single campaign. Higher automation, lower transparency. See our Performance Max guide for full PMax setup details.</li>
  <li><strong>Campaign priority settings</strong> — Standard Shopping campaigns have a Low/Medium/High priority setting that determines which campaign serves when a product is in multiple campaigns. Use this for query segmentation: run a High priority campaign for brand searches (at lower bids) that captures branded queries, while a Low priority campaign runs at higher bids for non-branded generic queries. Negative keywords in the High priority campaign exclude generic terms, ensuring they fall to the Low priority campaign.</li>
</ul>
<p>A proven structure for established e-commerce accounts: one campaign per major product category (e.g., separate campaigns for Shoes, Bags, Accessories), with product groups within each campaign segmented by brand or margin tier, and custom labels in the feed to flag best-sellers and high-margin items for higher bids.</p>

<h2>Bid Strategy and Budget</h2>
<p>Choosing the right bid strategy for your Shopping campaigns depends on conversion volume and account maturity:</p>
<ul>
  <li><strong>Manual CPC</strong> — maximum control, maximum management overhead. Set individual bids for each product group. Best for accounts with limited conversion data (under 30 conversions/month per campaign) where automated bidding has insufficient signal to optimise. Also useful for specific product lines where you want precise bid control that automation can't deliver.</li>
  <li><strong>Target ROAS (tROAS)</strong> — Google's Smart Bidding optimises every auction in real time toward your stated ROAS goal. Requires minimum 50 conversions per month per campaign for stable performance. The most effective strategy for established accounts with reliable conversion tracking.</li>
  <li><strong>Maximize Conversion Value</strong> — spends your budget to maximise total conversion value without a specific ROAS target. Good starting point when transitioning from manual bidding before you have enough data to set a reliable tROAS target.</li>
</ul>
<p>Setting your initial tROAS target: start at <strong>70–80% of your actual current ROAS</strong> to avoid over-constraining delivery. A common mistake is setting tROAS at your target (e.g., 400%) when your actual performance is running at 250% — the algorithm will severely limit delivery looking for those elusive high-ROAS conversions and you'll spend far below budget. Set a conservative initial target, let the campaign run for 4–6 weeks, then incrementally raise tROAS by 10–15% every 2 weeks as performance data builds.</p>

<h2>Negative Keywords: The Critical Difference</h2>
<p>Because Shopping campaigns don't use keywords — Google's algorithm matches products to queries automatically — negative keywords are your primary tool for preventing wasted spend on irrelevant searches. This is where Shopping campaigns most commonly fail.</p>
<p>The search terms report (available in Search Terms tab of your Shopping campaign) shows exactly which queries triggered your ads. Review it weekly for the first three months of a new campaign and add negatives aggressively. Categories of negatives to prioritise from day one:</p>
<ul>
  <li><strong>DIY and repair queries</strong> — "how to fix," "how to make," "tutorial," "instructions," "pattern" — information seekers who have no purchase intent</li>
  <li><strong>Wholesale and bulk queries</strong> — unless you actually sell wholesale, "wholesale," "bulk," "lot of," "for resale" queries attract the wrong buyers</li>
  <li><strong>Competitor brand names</strong> — unless you're running a deliberate conquesting strategy, traffic searching for a competitor's branded products converts poorly for your ads</li>
  <li><strong>Unrelated product categories</strong> — if you sell running shoes but appear for "dress shoes for wedding," that's wasted spend that a product-category-level negative would block</li>
  <li><strong>Free and cheap modifiers</strong> — "free," "cheapest," "used," "secondhand" — users using these modifiers have price sensitivity that likely doesn't match your positioning</li>
</ul>
<p>Establish a weekly search term review cadence for the first 90 days, then monthly once the account is stable. A mature Shopping account typically has hundreds of negative keywords that have been systematically added over time — this accumulated keyword hygiene is a significant competitive advantage that new competitors can't replicate quickly.</p>

<h2>Scaling Winning Products</h2>
<p>Once your Shopping campaigns are running profitably, scaling is a matter of identifying your highest-leverage products and systematically increasing their visibility. The process:</p>
<ul>
  <li><strong>Identify top performers</strong> — in your product group breakdown, sort by ROAS. Products consistently delivering ROAS at or above target with room to grow impression share are your scaling candidates. "Room to grow" means impression share below 60–70% — meaning you're winning only a portion of available auctions.</li>
  <li><strong>Isolate top performers in their own campaigns</strong> — move highest-ROAS products into dedicated campaigns with their own budgets. This prevents your budget from being shared with underperformers and lets you set more aggressive bids and budgets for your best products without diluting overall campaign ROAS.</li>
  <li><strong>Use product labels for bidding segmentation</strong> — add custom labels in your Merchant Center feed to tag products by performance tier: "bestseller," "high-margin," "seasonal," "new-arrival." These labels appear as filterable dimensions in your campaign product group view, making it easy to apply differentiated bid strategies without restructuring campaigns constantly.</li>
  <li><strong>Scale bids incrementally</strong> — increase bids on winning product groups by 10–15% per week. Larger increases trigger the algorithm to re-learn optimal bid levels, causing temporary performance dips. Slow, steady increases compound without disrupting the learning state of your Smart Bidding campaigns.</li>
</ul>
<p>One final principle that separates well-managed Shopping accounts from poorly managed ones: <strong>continuous feed improvement never stops</strong>. The feed is not a launch task; it's an ongoing competitive lever. Quarterly feed audits — checking title relevance against top search terms, image quality, data completeness scores in Merchant Center, and product disapproval rates — consistently yield incremental ROAS improvements that compound over time.</p>

<div class="callout">
  <p>Lumo AI Agency manages Google Shopping campaigns for e-commerce brands — including full feed optimisation, campaign structure, and weekly performance management.</p>
  <a href="/services/google-shopping.html">Explore our Google Shopping service &rarr;</a>
</div>
""",
    faqs=[
        ("Do I need Performance Max or can I use Standard Shopping campaigns?",
         "Both have a role. Standard Shopping gives you more control and transparency — you can see exactly which products serve which queries, manage bids by product group, and add keyword-level negatives. Performance Max delivers Shopping inventory plus all other Google channels with more automation. A common strategy: run Standard Shopping for your core categories with granular control, and test Performance Max for incremental reach. Don't replace Standard Shopping entirely with PMax until you have clear data that PMax outperforms."),
        ("How often should I update my product feed?",
         "At minimum, schedule a daily feed update to keep prices and inventory status current. Price discrepancies between your feed and landing page result in product disapprovals. For seasonal categories or frequent price changes, real-time feed updates via the Google Content API are worth implementing. Image and title/description optimisations can be done quarterly or in response to performance data from your search terms report."),
        ("My Shopping ads have high impressions but low clicks — what's wrong?",
         "Low CTR despite high impressions typically indicates one of three issues: (1) your price is uncompetitive compared to competitors showing in the same auction — Google Shopping is a price-comparison environment, and being 20%+ more expensive than alternatives dramatically reduces CTR; (2) your images are low quality, low contrast, or unclear compared to competitors; or (3) your titles are generic and don't communicate specific product value. Use Google Merchant Center's competitive visibility report to benchmark your prices against auction competitors."),
    ]
))


# ─── GENERATE FILES ──────────────────────────────────────────────────────────

total_bytes = 0
created_files = []

for art in articles:
    slug = art["slug"]
    out_dir = os.path.join(BASE_DIR, "blog", slug)
    os.makedirs(out_dir, exist_ok=True)

    html = build_page(
        title=art["title"],
        meta_desc=art["meta_desc"],
        slug=slug,
        cat_label=art["cat_label"],
        cat_class=art["cat_class"],
        pub_date=art["pub_date"],
        read_mins=art["read_mins"],
        h1_html=art["h1_html"],
        lead=art["lead"],
        body_html=art["body_html"],
        faqs=art["faqs"],
        cta_service_slug=art["cta_service_slug"],
        cta_service_name=art["cta_service_name"],
    )

    out_path = os.path.join(out_dir, "index.html")
    encoded = html.encode("utf-8")
    with open(out_path, "wb") as f:
        f.write(encoded)

    size = len(encoded)
    total_bytes += size
    created_files.append((out_path, size))
    print(f"  Created: blog/{slug}/index.html  ({size:,} bytes)")

print(f"\nDone. {len(created_files)} files, {total_bytes:,} total bytes.")
