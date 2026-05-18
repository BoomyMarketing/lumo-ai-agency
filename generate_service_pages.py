#!/usr/bin/env python3
"""Generate 5 new service pages for Lumo AI Agency."""
import os

BASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "services")

FOOTER = """<footer class="footer" role="contentinfo">
  <div class="footer-inner">
    <div class="footer-top">
      <div class="footer-brand">
        <a href="../index.html" class="footer-logo" aria-label="Lumo AI Agency home">Lumo<span>.</span></a>
        <p class="footer-tagline">Austin's AI-powered marketing agency. SEO, paid ads, AI automation &amp; web design built for the future.</p>
        <div class="footer-socials">
          <a href="https://instagram.com/lumoaiagency" class="social-link" target="_blank" rel="noopener noreferrer" aria-label="Lumo on Instagram">&#9679;</a>
          <a href="https://linkedin.com/company/lumoaiagency" class="social-link" target="_blank" rel="noopener noreferrer" aria-label="Lumo on LinkedIn">in</a>
          <a href="https://twitter.com/lumoaiagency" class="social-link" target="_blank" rel="noopener noreferrer" aria-label="Lumo on X">&#120143;</a>
        </div>
      </div>
      <div class="footer-col">
        <h4>Services</h4>
        <ul>
          <li><a href="../services/seo.html">SEO &amp; Content</a></li>
          <li><a href="../services/google-ads.html">Google Ads</a></li>
          <li><a href="../services/meta-ads.html">Meta Ads</a></li>
          <li><a href="../services/linkedin-ads.html">LinkedIn Ads</a></li>
          <li><a href="../services/tiktok-ads.html">TikTok Ads</a></li>
          <li><a href="../services/youtube-ads.html">YouTube Ads</a></li>
          <li><a href="../services/cro.html">CRO</a></li>
          <li><a href="../services/ecommerce-seo.html">E-commerce SEO</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h4>Top Locations</h4>
        <ul>
          <li><a href="../local/austin/seo-agency/index.html">SEO Agency Austin</a></li>
          <li><a href="../local/new-york/seo-agency/index.html">SEO Agency New York</a></li>
          <li><a href="../local/los-angeles/seo-agency/index.html">SEO Agency Los Angeles</a></li>
          <li><a href="../local/austin/google-ads-agency/index.html">Google Ads Austin</a></li>
          <li><a href="../local/chicago/seo-agency/index.html">SEO Agency Chicago</a></li>
          <li><a href="../local/houston/google-ads-agency/index.html">Google Ads Houston</a></li>
          <li><a href="../local/dallas/web-design-company/index.html">Web Design Dallas</a></li>
          <li><a href="../local/miami/social-media-agency/index.html">Social Media Miami</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h4>Company</h4>
        <ul>
          <li><a href="../about.html">About Us</a></li>
          <li><a href="../services.html">All Services</a></li>
          <li><a href="../pricing.html">Pricing</a></li>
          <li><a href="../contact.html">Contact</a></li>
        </ul>
        <h4 style="margin-top:24px">Contact</h4>
        <div class="footer-contact-item"><span class="fc-text"><a href="tel:+16473701888">(647) 370-1888</a></span></div>
        <div class="footer-contact-item"><span class="fc-text"><a href="mailto:hello@lumoaiagency.com">hello@lumoaiagency.com</a></span></div>
      </div>
    </div>
    <div class="footer-bottom">
      <span class="footer-copy">&copy; 2026 Lumo AI Agency. All rights reserved.</span>
      <div class="footer-bl">
        <a href="../privacy-policy.html">Privacy Policy</a>
        <a href="../terms.html">Terms of Service</a>
      </div>
    </div>
  </div>
</footer>"""

CSS_COMMON = """    :root{--bg:#0D0D14;--bg-card:#13131F;--bg-dark:#09090F;--primary:#B3FF00;--secondary:#7C3AED;--accent:#00F5FF;--text:#F0F0FF;--muted:#6B7280;--border:rgba(179,255,0,0.15);--glow-lime:0 0 30px rgba(179,255,0,0.35);--glow-violet:0 0 30px rgba(124,58,237,0.45);--radius-sm:8px;--radius:14px;--radius-lg:20px;--transition:0.25s cubic-bezier(0.4,0,0.2,1);}
    *,*::before,*::after{box-sizing:border-box;margin:0;padding:0;}
    html{scroll-behavior:smooth;-webkit-font-smoothing:antialiased;}
    body{font-family:'Inter',system-ui,sans-serif;background:var(--bg);color:var(--text);overflow-x:hidden;line-height:1.6;}
    h1,h2,h3,h4{font-family:'Syne',sans-serif;line-height:1.15;}
    a{color:inherit;text-decoration:none;}
    button{font-family:inherit;cursor:pointer;border:none;background:none;}
    ul{list-style:none;}
    .section-pad{padding:100px 0;}
    .container{max-width:1180px;margin:0 auto;padding:0 24px;}
    .btn{display:inline-flex;align-items:center;gap:8px;padding:14px 30px;border-radius:50px;font-weight:700;font-size:0.95rem;letter-spacing:0.02em;transition:var(--transition);white-space:nowrap;}
    .btn-lime{background:var(--primary);color:#0D0D14;}
    .btn-lime:hover{background:#c8ff26;transform:translateY(-2px);box-shadow:0 8px 30px rgba(179,255,0,0.45);}
    .btn-ghost{background:transparent;color:var(--text);border:1.5px solid rgba(240,240,255,0.2);}
    .btn-ghost:hover{border-color:var(--primary);color:var(--primary);transform:translateY(-2px);}
    #navbar{position:fixed;top:0;left:0;right:0;z-index:900;background:rgba(13,13,20,0.85);backdrop-filter:blur(16px);-webkit-backdrop-filter:blur(16px);border-bottom:1px solid rgba(179,255,0,0.06);transition:background 0.3s ease,border-color 0.3s ease;}
    #navbar.scrolled{background:rgba(13,13,20,0.97);border-bottom-color:rgba(179,255,0,0.12);}
    .nav-inner{display:flex;align-items:center;justify-content:space-between;height:68px;max-width:1180px;margin:0 auto;padding:0 24px;}
    .nav-logo{font-family:'Berkshire Swash',serif;font-size:1.6rem;color:var(--primary);letter-spacing:-0.01em;text-shadow:0 0 20px rgba(179,255,0,0.4);}
    .nav-links{display:flex;align-items:center;gap:36px;}
    .nav-links a{font-size:0.88rem;font-weight:500;color:var(--muted);transition:color var(--transition);letter-spacing:0.02em;}
    .nav-links a:hover,.nav-links a.active{color:var(--primary);}
    .nav-cta{display:flex;align-items:center;gap:16px;}
    .nav-hamburger{display:none;flex-direction:column;gap:5px;padding:8px;cursor:pointer;}
    .nav-hamburger span{display:block;width:24px;height:2px;background:var(--text);border-radius:2px;transition:var(--transition);}
    .mobile-menu{display:none;flex-direction:column;background:rgba(13,13,20,0.98);border-top:1px solid var(--border);padding:8px 24px 16px;}
    .mobile-menu.open{display:flex;}
    .mobile-menu a{padding:14px 0;border-bottom:1px solid rgba(255,255,255,0.05);color:var(--muted);font-size:0.95rem;font-weight:500;transition:color var(--transition);}
    .mobile-menu a:last-child{border-bottom:none;}
    .mobile-menu a:hover{color:var(--primary);}
    @media(max-width:768px){.nav-links,.nav-cta{display:none;}.nav-hamburger{display:flex;}}
    .page-hero{padding:140px 0 80px;position:relative;overflow:hidden;}
    .blob-wrap{position:absolute;inset:0;pointer-events:none;overflow:hidden;}
    .blob{position:absolute;border-radius:50%;filter:blur(80px);will-change:transform;}
    .blob-lime{width:500px;height:500px;background:radial-gradient(circle,rgba(179,255,0,0.18) 0%,transparent 70%);top:-80px;left:-80px;animation:drift-a 18s ease-in-out infinite;}
    .blob-violet{width:400px;height:400px;background:radial-gradient(circle,rgba(124,58,237,0.15) 0%,transparent 70%);bottom:0;right:-60px;animation:drift-b 22s ease-in-out infinite;}
    @keyframes drift-a{0%,100%{transform:translate(0,0) scale(1);}50%{transform:translate(60px,50px) scale(1.08);}}
    @keyframes drift-b{0%,100%{transform:translate(0,0) scale(1);}50%{transform:translate(-50px,-40px) scale(1.06);}}
    .hero-noise{position:absolute;inset:0;background-image:linear-gradient(rgba(179,255,0,0.02) 1px,transparent 1px),linear-gradient(90deg,rgba(179,255,0,0.02) 1px,transparent 1px);background-size:60px 60px;pointer-events:none;}
    .page-hero-inner{position:relative;z-index:2;}
    .breadcrumb{display:flex;align-items:center;gap:8px;font-size:0.8rem;color:var(--muted);margin-bottom:28px;}
    .breadcrumb a:hover{color:var(--primary);}
    .breadcrumb-sep{color:rgba(179,255,0,0.3);}
    .section-eyebrow{display:inline-flex;align-items:center;gap:8px;font-size:0.72rem;font-weight:700;letter-spacing:0.12em;text-transform:uppercase;color:var(--primary);margin-bottom:16px;}
    .section-eyebrow::before{content:'';display:block;width:24px;height:2px;background:var(--primary);border-radius:2px;}
    .section-h2{font-family:'Syne',sans-serif;font-size:clamp(2rem,4.5vw,3.2rem);color:var(--text);margin-bottom:16px;}
    .page-hero h1{font-family:'Syne',sans-serif;font-size:clamp(2.8rem,6vw,5rem);color:var(--text);line-height:1.08;margin-bottom:24px;}
    .page-hero h1 .hl-lime{color:var(--primary);text-shadow:0 0 30px rgba(179,255,0,0.45);}
    .page-hero p.lead{font-size:1.1rem;color:var(--muted);max-width:600px;margin-bottom:36px;}
    .hero-badge{display:inline-flex;align-items:center;gap:8px;padding:7px 16px;border:1px solid var(--primary);border-radius:50px;font-size:0.78rem;font-weight:600;color:var(--primary);letter-spacing:0.06em;text-transform:uppercase;background:rgba(179,255,0,0.06);margin-bottom:24px;}
    .stats-strip{background:var(--bg-dark);border-top:1px solid rgba(179,255,0,0.06);border-bottom:1px solid rgba(179,255,0,0.06);}
    .stats-row{display:grid;grid-template-columns:repeat(3,1fr);}
    .stat-item{padding:50px 40px;text-align:center;position:relative;}
    .stat-item:not(:last-child)::after{content:'';position:absolute;right:0;top:25%;bottom:25%;width:1px;background:rgba(179,255,0,0.08);}
    .stat-num{font-size:clamp(2.2rem,3.5vw,3rem);font-weight:900;color:var(--primary);line-height:1;text-shadow:0 0 20px rgba(179,255,0,0.3);}
    .stat-label{font-size:0.82rem;color:var(--muted);margin-top:8px;font-weight:500;}
    @media(max-width:600px){.stats-row{grid-template-columns:1fr;}.stat-item::after{display:none;}.stat-item{padding:32px 24px;}}
    .intro-grid{display:grid;grid-template-columns:1.2fr 1fr;gap:60px;align-items:start;}
    @media(max-width:900px){.intro-grid{grid-template-columns:1fr;gap:40px;}}
    .intro-text h2{font-family:'Syne',sans-serif;font-size:clamp(1.8rem,3.5vw,2.6rem);color:var(--text);margin-bottom:20px;}
    .intro-text p{color:var(--muted);font-size:0.95rem;line-height:1.8;margin-bottom:16px;}
    .deliverables-card{background:var(--bg-card);border:1px solid var(--border);border-radius:var(--radius-lg);padding:32px;}
    .deliverables-card h3{font-size:0.75rem;font-weight:700;letter-spacing:0.12em;text-transform:uppercase;color:var(--primary);margin-bottom:20px;}
    .deliverable-item{display:flex;align-items:flex-start;gap:12px;margin-bottom:14px;font-size:0.87rem;color:var(--text);}
    .del-check{width:20px;height:20px;border-radius:6px;background:rgba(179,255,0,0.1);border:1px solid rgba(179,255,0,0.3);display:flex;align-items:center;justify-content:center;flex-shrink:0;margin-top:1px;}
    .del-check svg{width:10px;height:10px;color:var(--primary);}
    #process{background:var(--bg-dark);}
    .process-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:20px;}
    @media(max-width:768px){.process-grid{grid-template-columns:1fr 1fr;}}
    @media(max-width:460px){.process-grid{grid-template-columns:1fr;}}
    .process-step{text-align:center;}
    .step-num{width:52px;height:52px;border-radius:50%;background:rgba(179,255,0,0.1);border:2px solid rgba(179,255,0,0.35);display:flex;align-items:center;justify-content:center;font-size:1rem;font-weight:800;color:var(--primary);margin:0 auto 20px;}
    .step-card{background:var(--bg-card);border:1px solid rgba(255,255,255,0.05);border-radius:var(--radius);padding:24px 20px;transition:border-color 0.28s,box-shadow 0.28s,transform 0.28s;}
    .process-step:hover .step-card{border-color:rgba(0,245,255,0.3);box-shadow:0 0 24px rgba(0,245,255,0.1);transform:translateY(-4px);}
    .step-icon{font-size:1.5rem;margin-bottom:12px;}
    .step-title{font-size:1rem;font-weight:700;color:var(--text);margin-bottom:8px;}
    .step-desc{font-size:0.82rem;color:var(--muted);line-height:1.6;}
    .pricing-teaser{background:var(--bg-card);border:1px solid var(--border);border-radius:var(--radius-lg);padding:40px;text-align:center;}
    .pricing-teaser h3{font-family:'Syne',sans-serif;font-size:1.8rem;color:var(--text);margin-bottom:12px;}
    .pricing-teaser p{color:var(--muted);font-size:0.92rem;margin-bottom:24px;}
    .price-display{font-size:clamp(2.5rem,4vw,3.5rem);font-weight:900;color:var(--primary);line-height:1;margin-bottom:6px;text-shadow:0 0 20px rgba(179,255,0,0.3);}
    #faq{background:var(--bg-dark);}
    .faq-list{display:flex;flex-direction:column;max-width:800px;margin:0 auto;}
    .faq-item{border-bottom:1px solid rgba(255,255,255,0.06);}
    .faq-item:first-child{border-top:1px solid rgba(255,255,255,0.06);}
    .faq-q{display:flex;justify-content:space-between;align-items:center;padding:22px 0;cursor:pointer;gap:16px;}
    .faq-q-text{font-size:0.98rem;font-weight:600;color:var(--text);}
    .faq-icon{width:28px;height:28px;border-radius:8px;background:rgba(179,255,0,0.08);border:1px solid rgba(179,255,0,0.2);display:flex;align-items:center;justify-content:center;flex-shrink:0;transition:transform 0.25s,background 0.25s;}
    .faq-item.open .faq-icon{transform:rotate(45deg);background:rgba(179,255,0,0.18);}
    .faq-a{max-height:0;overflow:hidden;transition:max-height 0.35s ease;}
    .faq-a p{font-size:0.9rem;color:var(--muted);line-height:1.75;padding-bottom:20px;}
    .faq-item.open .faq-a{max-height:400px;}
    .cta-band{background:linear-gradient(135deg,rgba(179,255,0,0.04) 0%,rgba(124,58,237,0.06) 100%);border-top:1px solid rgba(179,255,0,0.08);text-align:center;padding:100px 0;}
    .cta-band h2{font-family:'Syne',sans-serif;font-size:clamp(2rem,4vw,3.2rem);margin-bottom:20px;}
    .cta-band p{color:var(--muted);font-size:1rem;max-width:500px;margin:0 auto 36px;}
    .cta-btns{display:flex;gap:14px;justify-content:center;flex-wrap:wrap;}
    footer{background:var(--bg-dark);border-top:1px solid rgba(179,255,0,0.08);padding:60px 0 30px;}
    .footer-inner{max-width:1180px;margin:0 auto;padding:0 24px;}.footer-top{display:grid;grid-template-columns:1.4fr 1fr 1fr 1fr;gap:48px;margin-bottom:48px;}
    .footer-brand .footer-logo{font-family:'Berkshire Swash',serif;font-size:1.5rem;color:var(--primary);letter-spacing:-0.01em;text-shadow:0 0 20px rgba(179,255,0,0.4);display:inline-block;margin-bottom:16px;}
    .footer-tagline{font-size:0.85rem;color:var(--muted);line-height:1.7;margin-bottom:24px;}
    .footer-socials{display:flex;gap:10px;}
    .social-link{width:38px;height:38px;border-radius:10px;background:rgba(124,58,237,0.12);border:1px solid rgba(124,58,237,0.25);display:flex;align-items:center;justify-content:center;color:var(--secondary);font-size:0.9rem;font-weight:700;transition:background 0.25s,border-color 0.25s,transform 0.25s;}
    .social-link:hover{background:rgba(124,58,237,0.25);border-color:var(--secondary);transform:translateY(-3px);color:#fff;}
    .footer-col h4{font-size:0.78rem;font-weight:700;letter-spacing:0.1em;text-transform:uppercase;color:var(--text);margin-bottom:20px;}
    .footer-col ul{display:flex;flex-direction:column;gap:10px;}
    .footer-col a{font-size:0.85rem;color:var(--muted);transition:color 0.22s;}
    .footer-col a:hover{color:var(--primary);}
    .footer-contact-item{margin-bottom:8px;font-size:0.85rem;color:var(--muted);}
    .footer-contact-item a{color:var(--muted);transition:color 0.22s;}
    .footer-contact-item a:hover{color:var(--primary);}
    .footer-bottom{border-top:1px solid rgba(255,255,255,0.06);padding-top:24px;display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:12px;}
    .footer-bottom p,.footer-copy{font-size:0.8rem;color:var(--muted);}
    .footer-bottom a,.footer-bl a{color:var(--primary);font-size:0.8rem;}
    .footer-bl{display:flex;gap:24px;}
    @keyframes blink{0%,100%{opacity:1;}50%{opacity:0.3;}}
    @media(max-width:900px){.footer-top{grid-template-columns:1fr 1fr;}}
    @media(max-width:560px){.footer-top{grid-template-columns:1fr;gap:32px;}.footer-bottom{flex-direction:column;text-align:center;}.footer-bl{flex-direction:column;gap:10px;align-items:center;}}
    #scroll-top{position:fixed;bottom:30px;right:30px;width:46px;height:46px;border-radius:12px;background:var(--primary);color:#0D0D14;display:flex;align-items:center;justify-content:center;cursor:pointer;z-index:800;opacity:0;transform:translateY(10px);transition:opacity 0.3s,transform 0.3s,box-shadow 0.3s;border:none;}
    #scroll-top.visible{opacity:1;transform:translateY(0);}
    #scroll-top:hover{box-shadow:0 0 20px rgba(179,255,0,0.5);transform:translateY(-3px);}"""

JS_COMMON = """  const nav = document.getElementById('navbar');
  const hamburger = document.querySelector('.nav-hamburger');
  const mobileMenu = document.getElementById('mobile-menu');
  window.addEventListener('scroll', () => {
    nav.classList.toggle('scrolled', window.scrollY > 40);
    document.getElementById('scroll-top').classList.toggle('visible', window.scrollY > 300);
  });
  if (hamburger) {
    hamburger.addEventListener('click', () => {
      const open = mobileMenu.classList.toggle('open');
      hamburger.setAttribute('aria-expanded', open);
      mobileMenu.setAttribute('aria-hidden', !open);
    });
  }
  document.getElementById('scroll-top').addEventListener('click', () => window.scrollTo({top:0,behavior:'smooth'}));
  document.querySelectorAll('.faq-q').forEach(q => {
    q.addEventListener('click', () => {
      const item = q.parentElement;
      const open = item.classList.toggle('open');
      q.setAttribute('aria-expanded', open);
    });
    q.addEventListener('keydown', e => { if(e.key==='Enter'||e.key===' '){e.preventDefault();q.click();}});
  });"""

NAVBAR = """<header>
  <nav class="navbar" id="navbar" role="navigation" aria-label="Main navigation">
  <div class="nav-inner">
    <a href="../index.html" class="nav-logo" aria-label="Lumo AI Agency — Home">Lumo<span>.</span></a>
    <ul class="nav-links" role="menubar">
      <li role="none"><a href="../services.html" role="menuitem">Services</a></li>
      <li role="none"><a href="../about.html" role="menuitem">About</a></li>
      <li role="none"><a href="../pricing.html" role="menuitem">Pricing</a></li>
      <li role="none"><a href="../contact.html" role="menuitem">Contact</a></li>
    </ul>
    <div class="nav-cta"><a href="../contact.html" class="btn btn-lime" style="padding:10px 22px;font-size:0.85rem;">Get Started</a></div>
    <button class="nav-hamburger" aria-label="Open menu" aria-expanded="false" aria-controls="mobile-menu">
      <span></span><span></span><span></span>
    </button>
  </div>
  <div class="mobile-menu" id="mobile-menu" role="menu" aria-hidden="true">
    <a href="../services.html" role="menuitem">Services</a>
    <a href="../about.html" role="menuitem">About</a>
    <a href="../pricing.html" role="menuitem">Pricing</a>
    <a href="../contact.html" role="menuitem">Contact</a>
    <a href="../contact.html" role="menuitem">Get Started &rarr;</a>
  </div>
</nav>
</header>"""

def del_item(text):
    return f"""          <div class="deliverable-item"><div class="del-check"><svg viewBox="0 0 12 12" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M2 6l3 3 5-5"/></svg></div>{text}</div>"""

def faq_item(q, a):
    return f"""        <div class="faq-item">
          <div class="faq-q" tabindex="0" role="button" aria-expanded="false"><span class="faq-q-text">{q}</span><div class="faq-icon" aria-hidden="true"><svg width="12" height="12" viewBox="0 0 12 12" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M6 1v10M1 6h10"/></svg></div></div>
          <div class="faq-a"><p>{a}</p></div>
        </div>"""

def step(num, icon, title, desc):
    return f"""        <article class="process-step">
          <div class="step-num">{num}</div>
          <div class="step-card">
            <div class="step-icon">{icon}</div>
            <h3 class="step-title">{title}</h3>
            <p class="step-desc">{desc}</p>
          </div>
        </article>"""

def build_page(slug, title_tag, meta_desc, og_title, og_desc, canonical_path,
               schema_json, hero_badge, h1_html, lead,
               stat1, stat2, stat3,
               intro_h2, intro_ps, deliverables,
               process_title, steps,
               pricing_h3, price, pricing_p,
               faq_h2, faqs,
               cta_h2, cta_p, cta_btn_label):

    deliverables_html = "\n".join(del_item(d) for d in deliverables)
    steps_html = "\n".join(step(s[0], s[1], s[2], s[3]) for s in steps)
    faqs_html = "\n".join(faq_item(f[0], f[1]) for f in faqs)
    intro_ps_html = "\n".join(f"          <p>{p}</p>" for p in intro_ps)

    return f"""<!DOCTYPE html>
<html lang="en-US">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <meta name="description" content="{meta_desc}" />
  <meta name="robots" content="index, follow" />
  <meta name="author" content="Lumo Agency" />
  <meta property="og:type" content="website" />
  <meta property="og:title" content="{og_title}" />
  <meta property="og:description" content="{og_desc}" />
  <meta property="og:url" content="https://lumoaiagency.com/services/{canonical_path}" />
  <meta property="og:image" content="https://lumoaiagency.com/og-image.jpg" />
  <meta name="twitter:card" content="summary_large_image" />
  <link rel="canonical" href="https://lumoaiagency.com/services/{canonical_path}" />
  <title>{title_tag}</title>

  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Berkshire+Swash&family=Syne:wght@400;600;700;800&family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet" />

  <script type="application/ld+json">
  {schema_json}
  </script>

  <style>
{CSS_COMMON}
  </style>
</head>
<body>

{NAVBAR}

<main>
  <section class="page-hero" aria-label="{og_title}">
    <div class="blob-wrap" aria-hidden="true"><div class="blob blob-lime"></div><div class="blob blob-violet"></div></div>
    <div class="hero-noise" aria-hidden="true"></div>
    <div class="container page-hero-inner">
      <div class="hero-badge">{hero_badge}</div>
      <h1>{h1_html}</h1>
      <p class="lead">{lead}</p>
      <div style="display:flex;gap:14px;flex-wrap:wrap;">
        <a href="../contact.html" class="btn btn-lime">Get a Free Audit <svg width="16" height="16" viewBox="0 0 16 16" fill="none" aria-hidden="true"><path d="M3 8h10M9 4l4 4-4 4" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg></a>
        <a href="../pricing.html" class="btn btn-ghost">View Pricing</a>
      </div>
    </div>
  </section>

  <section class="stats-strip" aria-label="Key results">
    <div class="container">
      <div class="stats-row">
        <div class="stat-item"><div class="stat-num">{stat1[0]}</div><div class="stat-label">{stat1[1]}</div></div>
        <div class="stat-item"><div class="stat-num">{stat2[0]}</div><div class="stat-label">{stat2[1]}</div></div>
        <div class="stat-item"><div class="stat-num">{stat3[0]}</div><div class="stat-label">{stat3[1]}</div></div>
      </div>
    </div>
  </section>

  <section class="section-pad" id="intro" aria-labelledby="intro-h2">
    <div class="container">
      <div class="intro-grid">
        <div class="intro-text">
          <p class="section-eyebrow">What We Do</p>
          <h2 id="intro-h2">{intro_h2}</h2>
{intro_ps_html}
        </div>
        <div class="deliverables-card">
          <h3>What You Get</h3>
{deliverables_html}
        </div>
      </div>
    </div>
  </section>

  <section id="process" class="section-pad" aria-labelledby="process-h2">
    <div class="container">
      <div style="text-align:center;margin-bottom:60px;">
        <p class="section-eyebrow" style="justify-content:center;">How It Works</p>
        <h2 class="section-h2" id="process-h2">Our <span style="color:var(--primary);">{process_title}</span></h2>
      </div>
      <div class="process-grid">
{steps_html}
      </div>
    </div>
  </section>

  <section class="section-pad" id="pricing" aria-labelledby="pricing-h2">
    <div class="container" style="max-width:700px;">
      <div class="pricing-teaser">
        <p class="section-eyebrow" style="justify-content:center;">Transparent Pricing</p>
        <h3 id="pricing-h2">{pricing_h3}</h3>
        <div class="price-display">{price}<span style="font-size:1.2rem;font-weight:500;color:var(--muted);">/mo</span></div>
        <p>{pricing_p}</p>
        <div style="display:flex;gap:14px;justify-content:center;flex-wrap:wrap;margin-top:28px;">
          <a href="../contact.html" class="btn btn-lime">Get Free Audit</a>
          <a href="../pricing.html" class="btn btn-ghost">View All Plans</a>
        </div>
      </div>
    </div>
  </section>

  <section id="faq" class="section-pad" aria-labelledby="faq-h2">
    <div class="container">
      <div style="text-align:center;margin-bottom:60px;">
        <p class="section-eyebrow" style="justify-content:center;">Common Questions</p>
        <h2 class="section-h2" id="faq-h2">{faq_h2} <span style="color:var(--primary);">FAQ</span></h2>
      </div>
      <div class="faq-list">
{faqs_html}
      </div>
    </div>
  </section>

  <section class="cta-band" aria-label="Get started">
    <div class="container">
      <p class="section-eyebrow" style="justify-content:center;">Ready to Scale?</p>
      <h2>{cta_h2}</h2>
      <p>{cta_p}</p>
      <div class="cta-btns">
        <a href="../contact.html" class="btn btn-lime">{cta_btn_label} <svg width="16" height="16" viewBox="0 0 16 16" fill="none" aria-hidden="true"><path d="M3 8h10M9 4l4 4-4 4" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg></a>
        <a href="../pricing.html" class="btn btn-ghost">View Plans</a>
      </div>
    </div>
  </section>
</main>

{FOOTER}

<button id="scroll-top" aria-label="Scroll to top">
  <svg width="18" height="18" viewBox="0 0 18 18" fill="none" aria-hidden="true"><path d="M9 14V4M4 9l5-5 5 5" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>
</button>

<script>
{JS_COMMON}
</script>
</body>
</html>"""


# ─────────────────────────────────────────────
# 1. LINKEDIN ADS
# ─────────────────────────────────────────────
linkedin_schema = """{
    "@context": "https://schema.org",
    "@graph": [
      {
        "@type": "Service",
        "name": "LinkedIn Ads Management",
        "provider": {"@type": "Organization", "name": "Lumo Agency", "url": "https://lumoaiagency.com"},
        "description": "B2B-focused LinkedIn Ads management including Sponsored Content, Lead Gen Forms, and Message Ads for US businesses.",
        "areaServed": {"@type": "Country", "name": "United States"},
        "url": "https://lumoaiagency.com/services/linkedin-ads",
        "datePublished": "2026-05-13",
        "dateModified": "2026-05-13",
        "offers": {"@type": "Offer", "priceCurrency": "USD", "price": "1200", "priceSpecification": {"@type": "UnitPriceSpecification", "priceType": "monthly"}}
      },
      {
        "@type": "BreadcrumbList",
        "itemListElement": [
          {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://lumoaiagency.com/"},
          {"@type": "ListItem", "position": 2, "name": "Services", "item": "https://lumoaiagency.com/services"},
          {"@type": "ListItem", "position": 3, "name": "LinkedIn Ads", "item": "https://lumoaiagency.com/services/linkedin-ads"}
        ]
      },
      {
        "@type": "FAQPage",
        "mainEntity": [
          {"@type": "Question", "name": "What LinkedIn ad formats does Lumo manage?", "acceptedAnswer": {"@type": "Answer", "text": "We manage Sponsored Content (single image, carousel, video), Sponsored Messaging (Message Ads, Conversation Ads), Lead Gen Forms, Dynamic Ads, and Text Ads. The right mix depends on your funnel stage — we build a format strategy in your free audit session."}},
          {"@type": "Question", "name": "What B2B industries perform best on LinkedIn Ads?", "acceptedAnswer": {"@type": "Answer", "text": "LinkedIn Ads deliver the strongest ROI for SaaS, professional services, financial services, HR/recruiting, enterprise software, consulting, and B2B technology. If your target customer is a decision-maker at a mid-market or enterprise company, LinkedIn's targeting is unmatched."}},
          {"@type": "Question", "name": "What is a realistic CPL for LinkedIn Ads?", "acceptedAnswer": {"@type": "Answer", "text": "LinkedIn CPL typically ranges from $60–$200 depending on audience specificity, offer, and industry. While higher than Google Search, LinkedIn leads are often significantly more qualified — C-suite, VP, and Director-level decision-makers rather than anonymous search traffic."}},
          {"@type": "Question", "name": "Do you use LinkedIn Lead Gen Forms?", "acceptedAnswer": {"@type": "Answer", "text": "Yes, and we strongly recommend them for most B2B clients. Lead Gen Forms pre-fill contact data from LinkedIn profiles, removing the friction of landing page form completion and typically reducing CPL by 30–50% compared to standard click-through campaigns."}},
          {"@type": "Question", "name": "What minimum budget do you recommend for LinkedIn Ads?", "acceptedAnswer": {"@type": "Answer", "text": "We recommend a minimum daily budget of $100–$150 ($3,000–$4,500/mo ad spend) to generate meaningful data. LinkedIn's auction is competitive, and too-small budgets fail to exit the learning phase. Lumo's management fee is separate from ad spend."}}
        ]
      }
    ]
  }"""

linkedin = build_page(
    slug="linkedin-ads",
    title_tag="LinkedIn Ads Management — B2B Lead Generation | Lumo",
    meta_desc="Lumo manages LinkedIn Ads campaigns that reach C-suite decision-makers and generate high-quality B2B leads. Sponsored Content, Lead Gen Forms, and Message Ads. Starting at $1,200/mo.",
    og_title="LinkedIn Ads Management — B2B Lead Generation | Lumo Agency Austin TX",
    og_desc="AI-assisted LinkedIn Ads for B2B growth. Reach decision-makers with precision targeting, Lead Gen Forms, and Sponsored Content strategies that fill your pipeline.",
    canonical_path="linkedin-ads",
    schema_json=linkedin_schema,
    hero_badge="&#128188; B2B Paid Social",
    h1_html='LinkedIn Ads That<br/><span class="hl-lime">Fill Your B2B Pipeline</span>',
    lead="LinkedIn is the only platform where you can target decision-makers by job title, seniority, company size, and industry simultaneously. Lumo engineers LinkedIn Ads campaigns that reach the exact buyers your sales team wants — and convert them into qualified leads.",
    stat1=("4.2x", "Average pipeline ROI for LinkedIn Ads clients"),
    stat2=("$30M+", "B2B pipeline generated across client accounts"),
    stat3=("-41%", "Average CPL reduction after Lumo optimisation"),
    intro_h2="LinkedIn Ads Built for B2B Revenue, Not Impressions",
    intro_ps=[
        "Most B2B companies either avoid LinkedIn Ads because of the cost, or run them without a conversion-focused strategy and wonder why CPL is high. Lumo approaches LinkedIn Ads the way a revenue-obsessed operator would — with rigorous audience segmentation, offer testing, and attribution that connects every dollar spent to pipeline and closed revenue.",
        "Our LinkedIn Ads strategy starts with your ICP (Ideal Customer Profile). We build hyper-specific audience segments using job title, seniority, function, company size, industry, and LinkedIn Group membership — layered with retargeting audiences from your website and contact list uploads. The result is precise targeting that reaches decision-makers and minimizes wasted spend on irrelevant clicks.",
        "Creative is where most LinkedIn advertisers lose money. We run structured A/B tests across ad formats, hooks, visuals, and CTAs — identifying the messaging that resonates with your specific audience segment. For Lead Gen Form campaigns, we optimise the form fields and offer to maximize completion rates without sacrificing lead quality.",
        "Every LinkedIn campaign we manage is tracked end-to-end — from impression through to CRM opportunity and closed-won revenue. Lumo sets up LinkedIn Insight Tag, offline conversion imports, and CRM integrations so you have a complete picture of LinkedIn ROI, not just surface-level metrics.",
    ],
    deliverables=[
        "ICP audience research + segmentation strategy",
        "Sponsored Content + Lead Gen Form setup",
        "AI-assisted ad creative development and testing",
        "LinkedIn Insight Tag + conversion tracking",
        "CRM integration (HubSpot, Salesforce, GoHighLevel)",
        "Retargeting and lookalike audience configuration",
        "Weekly optimisation + monthly performance reporting",
    ],
    process_title="LinkedIn Ads Process",
    steps=[
        ("01", "&#128270;", "ICP + Audit", "We define your Ideal Customer Profile, audit existing campaigns if any, and map the audience segments and ad formats most likely to generate pipeline for your specific offer."),
        ("02", "&#127959;", "Build + Launch", "We build campaign architecture, develop ad creative, configure Lead Gen Forms, set up tracking, and launch with proper budget pacing to exit the learning phase efficiently."),
        ("03", "&#128202;", "Test + Optimise", "We run structured creative tests, refine audience segments, adjust bids, and iterate on form offers weekly — always moving toward lower CPL and higher lead quality."),
        ("04", "&#128640;", "Scale + Report", "Once core campaigns hit pipeline targets, we identify expansion opportunities — new audience segments, Message Ad sequences, and retargeting ladders that compound results over time."),
    ],
    pricing_h3="LinkedIn Ads Management",
    price="from $1,200",
    pricing_p="Management fee is separate from ad spend. We recommend a minimum monthly ad spend of $3,000–$4,500 to generate sufficient data for optimisation. Starter covers single-campaign management; Growth handles multi-audience funnels; Scale includes full LinkedIn + cross-channel paid strategy.",
    faq_h2="LinkedIn Ads",
    faqs=[
        ("What LinkedIn ad formats does Lumo manage?", "We manage Sponsored Content (single image, carousel, video), Sponsored Messaging (Message Ads, Conversation Ads), Lead Gen Forms, Dynamic Ads, and Text Ads. The right mix depends on your funnel stage — we build a format strategy in your free audit session."),
        ("What B2B industries perform best on LinkedIn Ads?", "LinkedIn Ads deliver the strongest ROI for SaaS, professional services, financial services, HR/recruiting, enterprise software, consulting, and B2B technology. If your target customer is a decision-maker at a mid-market or enterprise company, LinkedIn's targeting is unmatched."),
        ("What is a realistic CPL for LinkedIn Ads?", "LinkedIn CPL typically ranges from $60–$200 depending on audience specificity, offer, and industry. While higher than Google Search, LinkedIn leads are often significantly more qualified — C-suite, VP, and Director-level decision-makers rather than anonymous search traffic."),
        ("Do you use LinkedIn Lead Gen Forms?", "Yes, and we strongly recommend them for most B2B clients. Lead Gen Forms pre-fill contact data from LinkedIn profiles, removing the friction of landing page form completion and typically reducing CPL by 30–50% compared to standard click-through campaigns."),
        ("What minimum budget do you recommend for LinkedIn Ads?", "We recommend a minimum daily budget of $100–$150 ($3,000–$4,500/mo ad spend) to generate meaningful data. LinkedIn's auction is competitive, and too-small budgets fail to exit the learning phase. Lumo's management fee is separate from ad spend."),
    ],
    cta_h2='Fill Your Pipeline with <span style="color:var(--primary);">Qualified B2B Leads</span>',
    cta_p="Get a free LinkedIn Ads audit and a custom B2B lead generation strategy delivered within 48 hours.",
    cta_btn_label="Get Free LinkedIn Audit",
)

# ─────────────────────────────────────────────
# 2. TIKTOK ADS
# ─────────────────────────────────────────────
tiktok_schema = """{
    "@context": "https://schema.org",
    "@graph": [
      {
        "@type": "Service",
        "name": "TikTok Ads Management",
        "provider": {"@type": "Organization", "name": "Lumo Agency", "url": "https://lumoaiagency.com"},
        "description": "Performance TikTok Ads management including In-Feed Ads, TopView, Spark Ads, and creative strategy for US brands and e-commerce businesses.",
        "areaServed": {"@type": "Country", "name": "United States"},
        "url": "https://lumoaiagency.com/services/tiktok-ads",
        "datePublished": "2026-05-13",
        "dateModified": "2026-05-13",
        "offers": {"@type": "Offer", "priceCurrency": "USD", "price": "1200", "priceSpecification": {"@type": "UnitPriceSpecification", "priceType": "monthly"}}
      },
      {
        "@type": "BreadcrumbList",
        "itemListElement": [
          {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://lumoaiagency.com/"},
          {"@type": "ListItem", "position": 2, "name": "Services", "item": "https://lumoaiagency.com/services"},
          {"@type": "ListItem", "position": 3, "name": "TikTok Ads", "item": "https://lumoaiagency.com/services/tiktok-ads"}
        ]
      },
      {
        "@type": "FAQPage",
        "mainEntity": [
          {"@type": "Question", "name": "What types of TikTok ads does Lumo create?", "acceptedAnswer": {"@type": "Answer", "text": "We manage In-Feed Ads, Spark Ads (boosting organic content), TopView, Brand Takeover, and Collection Ads for e-commerce. Our creative team produces native-style video content that blends into the TikTok feed — because overly polished ads are the fastest way to get skipped."}},
          {"@type": "Question", "name": "Do I need to produce video content for TikTok Ads?", "acceptedAnswer": {"@type": "Answer", "text": "No. Lumo's creative team produces TikTok-native video content for your campaigns — including scripting, editing, and UGC-style production. We also work with your existing content, product footage, or can brief UGC creators to produce authentic ad material on your behalf."}},
          {"@type": "Question", "name": "Is TikTok Ads right for my business?", "acceptedAnswer": {"@type": "Answer", "text": "TikTok Ads work exceptionally well for e-commerce, consumer products, apps, food and beverage, beauty, fashion, fitness, and entertainment brands targeting 18–44 year olds. B2B and high-consideration purchase businesses typically see better ROI from LinkedIn or Google Search — we'll tell you honestly which platform suits your goals."}},
          {"@type": "Question", "name": "What ROAS can I expect from TikTok Ads?", "acceptedAnswer": {"@type": "Answer", "text": "E-commerce clients typically see 2–5x ROAS on TikTok, with standout creative achieving 8–12x. ROAS is highly creative-dependent on TikTok — the same offer with weak creative vs. strong native content can see 10x the performance difference. This is why creative strategy is at the core of Lumo's TikTok service."}},
          {"@type": "Question", "name": "How does Lumo approach TikTok creative?", "acceptedAnswer": {"@type": "Answer", "text": "We use a systematic creative testing framework — launching multiple hooks, formats, and offer angles simultaneously, then rapidly scaling the winning creative while pausing underperformers. We track thumb-stop rate, view-through rate, and conversion rate at every step to identify which creative variables drive performance."}}
        ]
      }
    ]
  }"""

tiktok = build_page(
    slug="tiktok-ads",
    title_tag="TikTok Ads Management — Creative Performance Advertising | Lumo",
    meta_desc="Lumo creates and manages TikTok Ads campaigns with native-style creative that converts. In-Feed Ads, Spark Ads, and e-commerce collection campaigns. Starting at $1,200/mo.",
    og_title="TikTok Ads Management — Creative Performance Advertising | Lumo Agency Austin TX",
    og_desc="Stop boosting random posts. Lumo engineers TikTok ad campaigns with scroll-stopping creative, systematic testing, and performance tracking that drives real revenue.",
    canonical_path="tiktok-ads",
    schema_json=tiktok_schema,
    hero_badge="&#127909; TikTok Performance",
    h1_html='TikTok Ads That<br/><span class="hl-lime">Stop the Scroll</span>',
    lead="TikTok's algorithm rewards creative quality over budget size — which means brands with the right content strategy can outperform brands spending 10x more. Lumo builds TikTok Ads campaigns grounded in native creative, systematic testing, and conversion data.",
    stat1=("3.8x", "Average ROAS across TikTok e-commerce clients"),
    stat2=("68%", "Lower CPM vs. Meta Ads on comparable audiences"),
    stat3=("12x", "Top creative ROAS achieved for e-commerce clients"),
    intro_h2="TikTok Ads Built for Creative Performance, Not Vanity Views",
    intro_ps=[
        "TikTok is the fastest-growing paid media channel for consumer brands — but most advertisers fail because they apply the same creative playbook they use for Facebook or Google. TikTok is a native content platform. Ads that look like ads get skipped. Ads that look like content get watched, shared, and purchased.",
        "Lumo's TikTok Ads strategy starts with creative intelligence — researching what content performs in your category, what hooks stop the scroll, and what offer structures convert on the platform. We then build a creative pipeline that produces and tests multiple concepts simultaneously, letting the algorithm tell us what works rather than guessing.",
        "Our campaign architecture covers the full TikTok funnel: awareness campaigns with broad targeting to identify resonant creative, retargeting campaigns to convert warm audiences, and Spark Ads to amplify your best organic content with paid distribution. We manage budgets dynamically, scaling spend behind proven creative and cutting waste fast.",
        "TikTok's pixel and events API give us the conversion data we need to optimize toward real business outcomes — not just views and engagements. We set up full-funnel tracking including server-side events so TikTok's algorithm has the cleanest possible signal for value-based bidding and ROAS optimization.",
    ],
    deliverables=[
        "TikTok Ads account setup and pixel configuration",
        "Native-style video creative production (scripting + editing)",
        "Multi-variant creative testing framework",
        "In-Feed, Spark Ads, and Collection ad setup",
        "Full-funnel audience segmentation + retargeting",
        "Server-side events API integration",
        "Weekly creative refresh + monthly performance reporting",
    ],
    process_title="TikTok Ads Process",
    steps=[
        ("01", "&#127916;", "Creative Research", "We audit your category's top-performing TikTok content, identify winning hooks and formats, and map a creative brief that sets the foundation for native-style ads that convert."),
        ("02", "&#127775;", "Produce + Launch", "We script, produce, and edit multiple creative variations — then launch with systematic A/B testing across hooks, offers, and formats to identify top performers fast."),
        ("03", "&#128202;", "Test + Scale", "We analyse thumb-stop rate, view-through rate, add-to-cart, and ROAS daily — cutting underperformers fast and scaling budget behind proven creative within the same billing cycle."),
        ("04", "&#9851;", "Refresh + Grow", "TikTok creative fatigues faster than other platforms. We maintain a rolling creative pipeline — refreshing winning formats and introducing new concepts monthly to sustain performance."),
    ],
    pricing_h3="TikTok Ads Management",
    price="from $1,200",
    pricing_p="Management fee covers strategy, creative direction, campaign management, and reporting. Video production is included in Growth and Scale plans. Recommended minimum ad spend is $2,000–$3,000/mo. Ad spend is paid directly to TikTok.",
    faq_h2="TikTok Ads",
    faqs=[
        ("What types of TikTok ads does Lumo create?", "We manage In-Feed Ads, Spark Ads (boosting organic content), TopView, Brand Takeover, and Collection Ads for e-commerce. Our creative team produces native-style video content that blends into the TikTok feed — because overly polished ads are the fastest way to get skipped."),
        ("Do I need to produce video content for TikTok Ads?", "No. Lumo's creative team produces TikTok-native video content for your campaigns — including scripting, editing, and UGC-style production. We also work with your existing content, product footage, or can brief UGC creators to produce authentic ad material on your behalf."),
        ("Is TikTok Ads right for my business?", "TikTok Ads work exceptionally well for e-commerce, consumer products, apps, food and beverage, beauty, fashion, fitness, and entertainment brands targeting 18–44 year olds. B2B and high-consideration purchase businesses typically see better ROI from LinkedIn or Google Search — we'll tell you honestly which platform suits your goals."),
        ("What ROAS can I expect from TikTok Ads?", "E-commerce clients typically see 2–5x ROAS on TikTok, with standout creative achieving 8–12x. ROAS is highly creative-dependent on TikTok — the same offer with weak creative vs. strong native content can see 10x the performance difference. This is why creative strategy is at the core of Lumo's TikTok service."),
        ("How does Lumo approach TikTok creative?", "We use a systematic creative testing framework — launching multiple hooks, formats, and offer angles simultaneously, then rapidly scaling the winning creative while pausing underperformers. We track thumb-stop rate, view-through rate, and conversion rate at every step to identify which creative variables drive performance."),
    ],
    cta_h2='Let\'s Build TikTok Ads That <span style="color:var(--primary);">Actually Convert</span>',
    cta_p="Get a free TikTok Ads strategy session and creative brief delivered within 48 hours.",
    cta_btn_label="Get Free TikTok Strategy",
)

# ─────────────────────────────────────────────
# 3. YOUTUBE ADS
# ─────────────────────────────────────────────
youtube_schema = """{
    "@context": "https://schema.org",
    "@graph": [
      {
        "@type": "Service",
        "name": "YouTube Ads Management",
        "provider": {"@type": "Organization", "name": "Lumo Agency", "url": "https://lumoaiagency.com"},
        "description": "YouTube advertising management including TrueView, bumper ads, and Performance Max video campaigns for US businesses seeking brand awareness and direct response results.",
        "areaServed": {"@type": "Country", "name": "United States"},
        "url": "https://lumoaiagency.com/services/youtube-ads",
        "datePublished": "2026-05-13",
        "dateModified": "2026-05-13",
        "offers": {"@type": "Offer", "priceCurrency": "USD", "price": "1200", "priceSpecification": {"@type": "UnitPriceSpecification", "priceType": "monthly"}}
      },
      {
        "@type": "BreadcrumbList",
        "itemListElement": [
          {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://lumoaiagency.com/"},
          {"@type": "ListItem", "position": 2, "name": "Services", "item": "https://lumoaiagency.com/services"},
          {"@type": "ListItem", "position": 3, "name": "YouTube Ads", "item": "https://lumoaiagency.com/services/youtube-ads"}
        ]
      },
      {
        "@type": "FAQPage",
        "mainEntity": [
          {"@type": "Question", "name": "What YouTube ad formats does Lumo manage?", "acceptedAnswer": {"@type": "Answer", "text": "We manage TrueView In-Stream (skippable), Non-Skippable In-Stream (15s), Bumper Ads (6s), In-Feed Video Ads (formerly Video Discovery), and YouTube via Performance Max campaigns. Format selection depends on your goal — awareness, consideration, or direct conversion."}},
          {"@type": "Question", "name": "Do I need a professionally produced video for YouTube Ads?", "acceptedAnswer": {"@type": "Answer", "text": "Not necessarily. While higher production quality helps for brand awareness campaigns, direct response YouTube Ads often perform strongly with authentic, talking-head style videos. Lumo will advise on production requirements based on your goals and budget — and can assist with scripting and editing for any format."}},
          {"@type": "Question", "name": "How does YouTube Ads fit into a full-funnel strategy?", "acceptedAnswer": {"@type": "Answer", "text": "YouTube is uniquely powerful at the awareness and consideration stages — reaching audiences who haven't searched for you yet and building brand affinity before they enter the purchase decision. Combined with Google Search ads that capture intent, YouTube creates a flywheel where your brand is the obvious choice when prospects are ready to buy."}},
          {"@type": "Question", "name": "What targeting options does YouTube offer?", "acceptedAnswer": {"@type": "Answer", "text": "YouTube offers demographic targeting, interest audiences, in-market audiences, custom intent audiences (people searching specific keywords), placement targeting (specific channels/videos), topic targeting, and remarketing to your website visitors. We layer these strategically to reach the right person at the right moment in their journey."}},
          {"@type": "Question", "name": "How do you measure YouTube Ads performance?", "acceptedAnswer": {"@type": "Answer", "text": "We track view-through rate (VTR), cost per view (CPV), brand lift metrics, and — critically — assisted conversions and view-through conversions that show YouTube's influence on downstream purchases. Many businesses undervalue YouTube because they only look at last-click attribution, missing the significant assist it provides to conversion campaigns."}}
        ]
      }
    ]
  }"""

youtube = build_page(
    slug="youtube-ads",
    title_tag="YouTube Ads Management — Video Advertising That Converts | Lumo",
    meta_desc="Lumo manages YouTube advertising campaigns that build brand authority and drive measurable ROI. TrueView, bumper ads, and Performance Max video strategy. Starting at $1,200/mo.",
    og_title="YouTube Ads Management — Video Advertising That Converts | Lumo Agency Austin TX",
    og_desc="YouTube is the world's second-largest search engine. Lumo builds video ad campaigns that reach your audience at every stage of the funnel — from awareness to conversion.",
    canonical_path="youtube-ads",
    schema_json=youtube_schema,
    hero_badge="&#127916; Video Advertising",
    h1_html='YouTube Ads That<br/><span class="hl-lime">Build Brands and Drive Revenue</span>',
    lead="YouTube reaches over 2.5 billion users monthly — and most advertisers are running the same generic pre-roll ads their competitors ran five years ago. Lumo builds YouTube Ads campaigns with strategic format selection, audience layering, and creative that earns attention before delivering a message.",
    stat1=("2.5B", "Monthly active YouTube users — the world's second-largest search engine"),
    stat2=("3x", "Higher purchase intent lift vs. linear TV advertising"),
    stat3=("$30M+", "Client revenue influenced by Lumo's video ad campaigns"),
    intro_h2="YouTube Advertising Built for the Full Funnel",
    intro_ps=[
        "YouTube is not just a branding channel — it's a direct response powerhouse when structured correctly. The brands winning on YouTube today use it as both a top-of-funnel awareness engine and a mid-funnel nurture channel that pre-sells prospects before they ever reach your landing page.",
        "Lumo's YouTube Ads strategy integrates with your broader Google ecosystem. We use custom intent audiences to reach people actively searching for keywords related to your product, then serve them targeted video ads that build authority before they click. The result is a warmed audience that converts at a fraction of the cost of cold traffic.",
        "Creative strategy is everything on YouTube. We apply a direct response framework to video scripting — opening with a hook designed to earn the first five seconds, establishing credibility quickly, presenting your offer clearly, and closing with a specific call to action. Every script is designed to work both with and without sound.",
        "Our YouTube campaigns run alongside your Google Search activity and are linked to the same conversion data — giving us a complete attribution picture. We track view-through conversions, assisted conversions, and brand search lift to quantify YouTube's full contribution to your revenue, not just its last-click value.",
    ],
    deliverables=[
        "YouTube campaign architecture + format strategy",
        "Custom intent + audience targeting setup",
        "Video ad scripting and creative direction",
        "TrueView, bumper, and non-skippable campaign builds",
        "Brand lift measurement setup",
        "Full-funnel attribution + Google Ads integration",
        "Monthly performance reporting + creative recommendations",
    ],
    process_title="YouTube Ads Process",
    steps=[
        ("01", "&#128270;", "Audit + Strategy", "We analyse your current video assets, audience opportunities, and competitive landscape to define a YouTube Ads strategy aligned to your specific funnel goals and budget."),
        ("02", "&#127917;", "Script + Produce", "We write direct-response video scripts, advise on production, and develop companion banner ads. For clients without existing video, we provide full production guidance or edit existing footage."),
        ("03", "&#127919;", "Target + Launch", "We build audience segments, set up conversion tracking, configure bidding strategy, and launch with structured testing across creatives, audiences, and formats."),
        ("04", "&#128200;", "Optimise + Scale", "We analyse VTR, CPV, assisted conversions, and brand search lift weekly — optimising audiences, creative, and budget allocation to maximise full-funnel impact."),
    ],
    pricing_h3="YouTube Ads Management",
    price="from $1,200",
    pricing_p="Management fee covers strategy, creative direction, campaign management, and reporting. Recommended minimum ad spend is $2,500–$5,000/mo for meaningful reach and optimisation data. Ad spend is paid directly to Google.",
    faq_h2="YouTube Ads",
    faqs=[
        ("What YouTube ad formats does Lumo manage?", "We manage TrueView In-Stream (skippable), Non-Skippable In-Stream (15s), Bumper Ads (6s), In-Feed Video Ads (formerly Video Discovery), and YouTube via Performance Max campaigns. Format selection depends on your goal — awareness, consideration, or direct conversion."),
        ("Do I need a professionally produced video for YouTube Ads?", "Not necessarily. While higher production quality helps for brand awareness campaigns, direct response YouTube Ads often perform strongly with authentic, talking-head style videos. Lumo will advise on production requirements based on your goals and budget — and can assist with scripting and editing for any format."),
        ("How does YouTube Ads fit into a full-funnel strategy?", "YouTube is uniquely powerful at the awareness and consideration stages — reaching audiences who haven't searched for you yet and building brand affinity before they enter the purchase decision. Combined with Google Search ads that capture intent, YouTube creates a flywheel where your brand is the obvious choice when prospects are ready to buy."),
        ("What targeting options does YouTube offer?", "YouTube offers demographic targeting, interest audiences, in-market audiences, custom intent audiences (people searching specific keywords), placement targeting (specific channels/videos), topic targeting, and remarketing to your website visitors. We layer these strategically to reach the right person at the right moment in their journey."),
        ("How do you measure YouTube Ads performance?", "We track view-through rate (VTR), cost per view (CPV), brand lift metrics, and — critically — assisted conversions and view-through conversions that show YouTube's influence on downstream purchases. Many businesses undervalue YouTube because they only look at last-click attribution, missing the significant assist it provides to conversion campaigns."),
    ],
    cta_h2='Put Your Brand in Front of <span style="color:var(--primary);">Millions on YouTube</span>',
    cta_p="Get a free YouTube Ads strategy session and video script framework within 48 hours.",
    cta_btn_label="Get Free Video Strategy",
)

# ─────────────────────────────────────────────
# 4. CRO
# ─────────────────────────────────────────────
cro_schema = """{
    "@context": "https://schema.org",
    "@graph": [
      {
        "@type": "Service",
        "name": "Conversion Rate Optimisation (CRO)",
        "provider": {"@type": "Organization", "name": "Lumo Agency", "url": "https://lumoaiagency.com"},
        "description": "Data-driven CRO services including A/B testing, landing page optimisation, UX analysis, and funnel improvement for US businesses.",
        "areaServed": {"@type": "Country", "name": "United States"},
        "url": "https://lumoaiagency.com/services/cro",
        "datePublished": "2026-05-13",
        "dateModified": "2026-05-13",
        "offers": {"@type": "Offer", "priceCurrency": "USD", "price": "1500", "priceSpecification": {"@type": "UnitPriceSpecification", "priceType": "monthly"}}
      },
      {
        "@type": "BreadcrumbList",
        "itemListElement": [
          {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://lumoaiagency.com/"},
          {"@type": "ListItem", "position": 2, "name": "Services", "item": "https://lumoaiagency.com/services"},
          {"@type": "ListItem", "position": 3, "name": "CRO", "item": "https://lumoaiagency.com/services/cro"}
        ]
      },
      {
        "@type": "FAQPage",
        "mainEntity": [
          {"@type": "Question", "name": "What does CRO include?", "acceptedAnswer": {"@type": "Answer", "text": "Lumo's CRO service covers heatmap and session recording analysis, funnel drop-off identification, landing page A/B testing, copywriting optimisation, form optimisation, page speed improvements, and mobile UX fixes. We prioritise tests by expected revenue impact, not complexity."}},
          {"@type": "Question", "name": "How long does CRO take to show results?", "acceptedAnswer": {"@type": "Answer", "text": "Initial quick wins — form simplification, CTA copy changes, page speed fixes — often show measurable uplift within 2–4 weeks. Full A/B test cycles typically run 3–6 weeks to reach statistical significance. Most clients see compounding conversion improvements over 3–6 months as multiple tests are completed."}},
          {"@type": "Question", "name": "What tools does Lumo use for CRO?", "acceptedAnswer": {"@type": "Answer", "text": "We use Hotjar or Microsoft Clarity for heatmaps and session recordings, Google Optimize or VWO for A/B testing, GA4 for funnel analysis, and Google PageSpeed Insights + Core Web Vitals data for performance diagnostics. Tool selection is adapted to your existing stack."}},
          {"@type": "Question", "name": "How much traffic do I need for CRO to work?", "acceptedAnswer": {"@type": "Answer", "text": "Meaningful A/B tests require at least 500–1,000 unique visitors per variant per week to reach statistical significance in a reasonable timeframe. For lower-traffic sites, we focus on qualitative methods — session recordings, user surveys, expert UX review — to generate high-confidence hypotheses without waiting for test significance."}},
          {"@type": "Question", "name": "Does CRO work for both e-commerce and lead generation?", "acceptedAnswer": {"@type": "Answer", "text": "Absolutely. For e-commerce, we optimise product pages, cart flow, checkout, and category pages to increase transaction rate and average order value. For lead generation, we optimise landing pages, contact forms, and lead magnets to increase form completion rates and lead quality simultaneously."}}
        ]
      }
    ]
  }"""

cro = build_page(
    slug="cro",
    title_tag="Conversion Rate Optimisation (CRO) — Turn More Visitors Into Customers | Lumo",
    meta_desc="Lumo's CRO service uses data, heatmaps, and A/B testing to increase your website's conversion rate — turning more existing traffic into leads and sales. Starting at $1,500/mo.",
    og_title="Conversion Rate Optimisation (CRO) — More Revenue From Existing Traffic | Lumo Agency Austin TX",
    og_desc="Stop spending more on ads. Lumo's CRO service uses A/B testing, heatmaps, and UX analysis to convert more of the traffic you already have into paying customers.",
    canonical_path="cro",
    schema_json=cro_schema,
    hero_badge="&#128200; Conversion Optimisation",
    h1_html='CRO That Turns<br/><span class="hl-lime">More Visitors Into Revenue</span>',
    lead="Doubling your conversion rate delivers the same revenue as doubling your traffic — at a fraction of the cost. Lumo's CRO service uses behavioural data, structured A/B testing, and UX expertise to systematically eliminate the friction points that are costing you leads and sales right now.",
    stat1=("+47%", "Average conversion rate improvement across CRO client engagements"),
    stat2=("3.2x", "Average revenue uplift per visitor within 6 months of CRO"),
    stat3=("$30M+", "Additional client revenue unlocked through conversion optimisation"),
    intro_h2="CRO Built on Data, Not Opinions",
    intro_ps=[
        "Most websites convert 1–3% of their visitors. The other 97–99% leave without taking action — and most businesses respond by spending more on ads to drive more traffic into a leaky funnel. CRO flips this equation: fix the funnel first, then scale traffic into a system that actually converts.",
        "Lumo's CRO process starts with a comprehensive data audit. We analyse your GA4 funnel data to identify exactly where visitors drop off, use heatmaps and session recordings to understand why, and conduct expert UX reviews to spot barriers that data alone doesn't reveal. Every hypothesis we test is grounded in evidence, not gut instinct.",
        "Our A/B testing framework runs structured experiments across landing pages, CTAs, headlines, forms, pricing pages, and checkout flows. We prioritise tests by expected revenue impact — high-traffic pages with meaningful drop-off rates come first. Every test runs to statistical significance before conclusions are drawn.",
        "CRO is not a one-time project — it's a continuous improvement system. Lumo maintains a rolling test backlog, so the moment one test concludes, the next is already queued. Over time, these compounding improvements create a website that converts dramatically better than it did 6 or 12 months ago.",
    ],
    deliverables=[
        "GA4 funnel analysis + drop-off mapping",
        "Heatmap and session recording analysis",
        "Expert UX and copywriting review",
        "A/B test hypothesis development and prioritisation",
        "Landing page variant design and implementation",
        "Form and checkout flow optimisation",
        "Monthly test results report + next-quarter roadmap",
    ],
    process_title="CRO Process",
    steps=[
        ("01", "&#128270;", "Data Audit", "We analyse your GA4 funnels, heatmaps, and session recordings to identify the highest-impact drop-off points — the specific moments where visitors abandon instead of converting."),
        ("02", "&#128161;", "Hypothesise + Prioritise", "We develop evidence-based hypotheses for each drop-off point and prioritise them by expected revenue impact — focusing effort where conversion gains matter most."),
        ("03", "&#129514;", "Test + Measure", "We build A/B test variants, implement them via testing software, and run experiments to statistical significance before drawing conclusions — no premature decisions."),
        ("04", "&#128640;", "Iterate + Compound", "Winning variants are implemented permanently. Losing tests inform new hypotheses. The cycle continues monthly, compounding conversion gains over time."),
    ],
    pricing_h3="Conversion Rate Optimisation",
    price="from $1,500",
    pricing_p="Pricing covers audit, hypothesis development, A/B test implementation, and monthly reporting. Testing tool licences (VWO, Optimizely) and heatmap tools (Hotjar, Clarity) are included in Growth and Scale plans. Starter covers 2 active tests per month; Scale runs unlimited parallel tests.",
    faq_h2="CRO",
    faqs=[
        ("What does CRO include?", "Lumo's CRO service covers heatmap and session recording analysis, funnel drop-off identification, landing page A/B testing, copywriting optimisation, form optimisation, page speed improvements, and mobile UX fixes. We prioritise tests by expected revenue impact, not complexity."),
        ("How long does CRO take to show results?", "Initial quick wins — form simplification, CTA copy changes, page speed fixes — often show measurable uplift within 2–4 weeks. Full A/B test cycles typically run 3–6 weeks to reach statistical significance. Most clients see compounding conversion improvements over 3–6 months as multiple tests are completed."),
        ("What tools does Lumo use for CRO?", "We use Hotjar or Microsoft Clarity for heatmaps and session recordings, Google Optimize or VWO for A/B testing, GA4 for funnel analysis, and Google PageSpeed Insights + Core Web Vitals data for performance diagnostics. Tool selection is adapted to your existing stack."),
        ("How much traffic do I need for CRO to work?", "Meaningful A/B tests require at least 500–1,000 unique visitors per variant per week to reach statistical significance in a reasonable timeframe. For lower-traffic sites, we focus on qualitative methods — session recordings, user surveys, expert UX review — to generate high-confidence hypotheses without waiting for test significance."),
        ("Does CRO work for both e-commerce and lead generation?", "Absolutely. For e-commerce, we optimise product pages, cart flow, checkout, and category pages to increase transaction rate and average order value. For lead generation, we optimise landing pages, contact forms, and lead magnets to increase form completion rates and lead quality simultaneously."),
    ],
    cta_h2='Convert More of the Traffic <span style="color:var(--primary);">You Already Have</span>',
    cta_p="Get a free CRO audit — we'll identify your top 3 conversion killers and estimate the revenue you're leaving on the table.",
    cta_btn_label="Get Free CRO Audit",
)

# ─────────────────────────────────────────────
# 5. ECOMMERCE SEO
# ─────────────────────────────────────────────
ecom_schema = """{
    "@context": "https://schema.org",
    "@graph": [
      {
        "@type": "Service",
        "name": "E-commerce SEO",
        "provider": {"@type": "Organization", "name": "Lumo Agency", "url": "https://lumoaiagency.com"},
        "description": "Specialist e-commerce SEO for Shopify, WooCommerce, and custom platforms — covering technical SEO, product schema, category optimisation, and organic revenue growth.",
        "areaServed": {"@type": "Country", "name": "United States"},
        "url": "https://lumoaiagency.com/services/ecommerce-seo",
        "datePublished": "2026-05-13",
        "dateModified": "2026-05-13",
        "offers": {"@type": "Offer", "priceCurrency": "USD", "price": "1500", "priceSpecification": {"@type": "UnitPriceSpecification", "priceType": "monthly"}}
      },
      {
        "@type": "BreadcrumbList",
        "itemListElement": [
          {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://lumoaiagency.com/"},
          {"@type": "ListItem", "position": 2, "name": "Services", "item": "https://lumoaiagency.com/services"},
          {"@type": "ListItem", "position": 3, "name": "E-commerce SEO", "item": "https://lumoaiagency.com/services/ecommerce-seo"}
        ]
      },
      {
        "@type": "FAQPage",
        "mainEntity": [
          {"@type": "Question", "name": "What e-commerce platforms does Lumo support?", "acceptedAnswer": {"@type": "Answer", "text": "We work with Shopify, WooCommerce, BigCommerce, Magento, and custom e-commerce builds. Each platform has unique SEO considerations — Shopify URL structures, WooCommerce canonical issues, and faceted navigation crawl bloat are common problems we fix routinely."}},
          {"@type": "Question", "name": "How is e-commerce SEO different from regular SEO?", "acceptedAnswer": {"@type": "Answer", "text": "E-commerce SEO involves unique challenges: thousands of product pages requiring individual optimisation, category page architecture, faceted navigation creating duplicate content and crawl waste, product schema (Product, Offer, AggregateRating), and managing seasonal inventory fluctuations without losing ranking authority. Lumo specialises in all of these."}},
          {"@type": "Question", "name": "How long does e-commerce SEO take to show results?", "acceptedAnswer": {"@type": "Answer", "text": "Technical fixes often show ranking improvements within 4–8 weeks. Category page optimisation typically shows meaningful organic traffic gains within 60–90 days. Building competitive authority for high-value product and category keywords takes 6–12 months of consistent content and link building."}},
          {"@type": "Question", "name": "Do you optimise product pages at scale?", "acceptedAnswer": {"@type": "Answer", "text": "Yes. For stores with hundreds or thousands of products, Lumo uses templated optimisation frameworks — standardising meta title and description patterns, implementing bulk schema generation, and creating product description templates that ensure consistent quality and uniqueness at scale without manual editing of every product."}},
          {"@type": "Question", "name": "Do you help with Google Shopping SEO?", "acceptedAnswer": {"@type": "Answer", "text": "Yes. Organic Google Shopping (free listings) is driven by your product feed quality and page optimisation. Lumo optimises your product data feed — titles, descriptions, GTINs, and attributes — alongside on-page product SEO to maximise visibility in both organic search and free Shopping listings."}}
        ]
      }
    ]
  }"""

ecommerce = build_page(
    slug="ecommerce-seo",
    title_tag="E-commerce SEO — Organic Revenue Growth for Online Stores | Lumo",
    meta_desc="Lumo's e-commerce SEO service drives organic revenue for Shopify, WooCommerce, and BigCommerce stores. Product schema, category optimisation, technical SEO at scale. Starting at $1,500/mo.",
    og_title="E-commerce SEO — Drive Organic Revenue for Your Online Store | Lumo Agency Austin TX",
    og_desc="Turn organic search into your highest-ROI acquisition channel. Lumo's e-commerce SEO specialists optimise product pages, category architecture, and technical foundations for sustained organic growth.",
    canonical_path="ecommerce-seo",
    schema_json=ecom_schema,
    hero_badge="&#128722; E-commerce Growth",
    h1_html='E-commerce SEO That<br/><span class="hl-lime">Drives Organic Revenue</span>',
    lead="Organic search is the highest-margin acquisition channel for e-commerce — no CPC, no ad spend, just compounding traffic that grows as your authority builds. Lumo's e-commerce SEO specialists build the technical foundations, category architecture, and content strategy that turn Google into your most profitable sales channel.",
    stat1=("+183%", "Average organic revenue increase within 12 months for e-commerce clients"),
    stat2=("$30M+", "Organic e-commerce revenue generated across client stores"),
    stat3=("-64%", "Average reduction in organic cost-per-acquisition vs. paid channels"),
    intro_h2="E-commerce SEO Built for Revenue, Not Just Rankings",
    intro_ps=[
        "Most e-commerce stores leave enormous organic revenue on the table. Thin product descriptions, duplicate content from faceted navigation, unoptimised category pages, missing product schema, and slow load times all compound into a site that Google can't rank — even for keywords your competitors rank for with weaker products.",
        "Lumo's e-commerce SEO process starts with a comprehensive technical audit. We identify crawl waste from duplicate URLs, canonicalisation errors, orphaned pages, and pagination issues — then fix the foundation before investing in content. Technical problems are the silent killer of e-commerce organic performance.",
        "Category pages are the highest-value SEO asset in most e-commerce stores, yet most stores treat them as pure navigation. Lumo optimises category pages with strategic H1s, unique introductory copy, internal linking structures, and schema markup that signals topical relevance to Google — often producing the largest organic traffic gains in the first 90 days.",
        "At scale, product page SEO requires a systems approach. We build optimisation templates, automated schema generation, and meta title/description frameworks that ensure hundreds or thousands of product pages are individually optimised without requiring manual attention to every SKU.",
    ],
    deliverables=[
        "Full technical SEO audit + crawl issue remediation",
        "Category page optimisation (copy, structure, schema)",
        "Product page template optimisation at scale",
        "Product schema (Product, Offer, AggregateRating)",
        "Faceted navigation and canonical strategy",
        "Internal linking architecture redesign",
        "Monthly organic revenue reporting + roadmap",
    ],
    process_title="E-commerce SEO Process",
    steps=[
        ("01", "&#128269;", "Technical Audit", "We crawl your entire store, identify duplicate content, canonical errors, crawl waste, and Core Web Vitals issues — building a prioritised remediation plan based on organic revenue impact."),
        ("02", "&#127760;", "Architecture + Schema", "We restructure category URLs if needed, implement Product and BreadcrumbList schema, fix faceted navigation, and set up canonical rules to prevent Google indexing thousands of duplicate filter pages."),
        ("03", "&#128221;", "Content + Optimisation", "We optimise category page copy, build product description frameworks, develop blog content targeting high-intent buyer keywords, and implement internal linking that passes authority to revenue-driving pages."),
        ("04", "&#128200;", "Scale + Compound", "We build link equity through digital PR and supplier/brand citation strategies, monitor ranking progression monthly, and iterate content strategy based on what's ranking and what needs more authority."),
    ],
    pricing_h3="E-commerce SEO",
    price="from $1,500",
    pricing_p="Pricing covers technical audit, on-page optimisation, content strategy, and monthly reporting. Store size significantly affects scope — we provide custom pricing for stores with 500+ SKUs or complex platform configurations. All plans include monthly organic revenue reporting.",
    faq_h2="E-commerce SEO",
    faqs=[
        ("What e-commerce platforms does Lumo support?", "We work with Shopify, WooCommerce, BigCommerce, Magento, and custom e-commerce builds. Each platform has unique SEO considerations — Shopify URL structures, WooCommerce canonical issues, and faceted navigation crawl bloat are common problems we fix routinely."),
        ("How is e-commerce SEO different from regular SEO?", "E-commerce SEO involves unique challenges: thousands of product pages requiring individual optimisation, category page architecture, faceted navigation creating duplicate content and crawl waste, product schema (Product, Offer, AggregateRating), and managing seasonal inventory fluctuations without losing ranking authority. Lumo specialises in all of these."),
        ("How long does e-commerce SEO take to show results?", "Technical fixes often show ranking improvements within 4–8 weeks. Category page optimisation typically shows meaningful organic traffic gains within 60–90 days. Building competitive authority for high-value product and category keywords takes 6–12 months of consistent content and link building."),
        ("Do you optimise product pages at scale?", "Yes. For stores with hundreds or thousands of products, Lumo uses templated optimisation frameworks — standardising meta title and description patterns, implementing bulk schema generation, and creating product description templates that ensure consistent quality and uniqueness at scale without manual editing of every product."),
        ("Do you help with Google Shopping SEO?", "Yes. Organic Google Shopping (free listings) is driven by your product feed quality and page optimisation. Lumo optimises your product data feed — titles, descriptions, GTINs, and attributes — alongside on-page product SEO to maximise visibility in both organic search and free Shopping listings."),
    ],
    cta_h2='Make Organic Search Your <span style="color:var(--primary);">Most Profitable Sales Channel</span>',
    cta_p="Get a free e-commerce SEO audit — we'll identify your top revenue leaks and show you exactly what it takes to fix them.",
    cta_btn_label="Get Free E-commerce Audit",
)

# Write all files
pages = {
    "linkedin-ads.html": linkedin,
    "tiktok-ads.html":   tiktok,
    "youtube-ads.html":  youtube,
    "cro.html":          cro,
    "ecommerce-seo.html": ecommerce,
}

for filename, html in pages.items():
    path = os.path.join(BASE, filename)
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Created: services/{filename} ({len(html):,} chars)")

print("Done.")
