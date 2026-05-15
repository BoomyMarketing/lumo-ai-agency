# SEO Full Audit Report — Lumo AI Agency
**URL:** https://lumoaiagency.com  
**Audit Date:** 2026-05-16  
**Scope:** Homepage + local files analysis (8 specialist agents)  
**Business Type:** AI Marketing Agency · Local Business (Austin TX) · Hybrid SAB

---

## Overall SEO Health Score: 62 / 100

| Category | Weight | Score | Weighted |
|---|---|---|---|
| Technical SEO | 22% | 71/100 | 15.6 |
| Content Quality (E-E-A-T) | 23% | 54/100 | 12.4 |
| On-Page SEO / SXO | 20% | 58/100 | 11.6 |
| Schema / Structured Data | 10% | 65/100 | 6.5 |
| Performance (CWV) | 10% | 72/100 | 7.2 |
| AI Search Readiness (GEO) | 10% | 71/100 | 7.1 |
| Images | 5% | 40/100 | 2.0 |
| **TOTAL** | | | **62.4 / 100** |

**Local SEO sub-score: 30.6 / 100** (critical — see Section 7)

---

## Top 5 Critical Issues

1. **Телефон +1 (647) — канадський код (Торонто), не Austin TX** — ламає Local SEO, E-E-A-T, GEO та entity confidence у всіх AI-платформах одночасно
2. **Внутрішні href посилання з `.html` розширенням** — `href="services.html"` в navbar/footer конфліктує з canonical URL без розширення → роздвоєння PageRank
3. **Назва бізнесу у трьох різних варіантах** — "Lumo AI Agency" / "Lumo Agency" / "Lumo" у різних schema-блоках → Google не може консолідувати entity
4. **Жодного named автора на жодній з 38 blog-статей** — Organization-type authorship = найсильніший сигнал AI-контенту batch-генерації
5. **Невалідний JSON-LD у blog-статтях** — single-quoted рядки замість double-quoted → structured data не обробляється Google; FAQ rich results недоступні

## Top 5 Quick Wins

1. Замінити всі `href="*.html"` на `/services`, `/about`, `/contact`, `/pricing`, `/` — 1 година, критичний технічний виправлення
2. Додати `<meta name="robots" content="noindex, nofollow">` у `design-system.html` — 5 хвилин
3. Видалити `potentialAction` SearchAction з WebSite schema — статичний сайт не має пошуку — 10 хвилин
4. Виправити всі single-quote → double-quote у JSON-LD блоках blog-статей — find & replace по всіх 38 файлах
5. Стандартизувати назву до "Lumo AI Agency" у всіх schema-блоках (homepage, contact, local pages) — 30 хвилин

---

## Section 1: Technical SEO — 71/100

### CRITICAL

**1. href атрибути з `.html` розширеннями (вся навігація)**
Navbar, footer та CTA-кнопки використовують `href="services.html"`, `href="about.html"`, `href="contact.html"` тощо. Vercel роздає ці файли як clean URL `/services`, `/about`, `/contact`. Google бачить два різних URL для тієї самої сторінки — canonical та href target. PageRank роздвоюється.

Рішення: Замінити всюди на кореневі відносні URL:
```html
<!-- Було -->
<a href="services.html">Services</a>
<!-- Має бути -->
<a href="/services">Services</a>
```

**2. design-system.html доступний для індексації**
Файл існує в корені без `<meta name="robots">`. Google може проіндексувати службову сторінку. Robots.txt її не блокує.

Рішення: `<meta name="robots" content="noindex, nofollow">` або `Disallow: /design-system.html` у robots.txt.

**3. Sitemap: URL-формат — trailing slash непослідовний**
- Services pages: `/services/seo` (без slash)
- Local pages: `/local/austin/ai-marketing-agency` (без slash)
- Blog pages: `/blog/what-is-geo/` (зі slash)
- Compare pages: `/compare/lumo-vs-webfx/` (зі slash)
- Industries 1-10: без slash; Industries 11-20: зі slash

Vercel робить 301 redirect між версіями, але канонічна форма у sitemap має відповідати формі у canonical тегах.

### HIGH

**4. WebSite SearchAction — неіснуючий ендпоінт**
```json
"target": "https://lumoaiagency.com/?s={search_term_string}"
```
WordPress-параметр пошуку на статичному HTML-сайті. Google тестуватиме цей endpoint; при 404 або redirect страждає довіра до всього schema-блоку.

**5. Blog URL відсутні у sitemap**
38 blog-статей та blog hub не фігурують у sitemap.xml. Індексація відбувається лише через internal links.

**6. Footer посилання — відносні без ведучого slash**
```html
<!-- Проблема — коректно лише з homepage -->
<a href="local/austin/seo-agency/index.html">
<!-- Правильно -->
<a href="/local/austin/seo-agency/">
```

### MEDIUM

**7. Title tag — services.html занадто короткий (45 символів)**
"All 105 AI Growth Services | Lumo AI Agency" — немає primary keyword "AI marketing" чи "Austin".
Рекомендація: "AI Marketing Services — 105+ Solutions | Lumo AI Agency" (~57 симв.)

**8. H1 не містить primary keyword**
"The AI Agency Austin Trusts" — brand-centric. "AI marketing agency" або "AI agency Austin" відсутні у H1.
Рекомендація: "Austin's AI Marketing Agency" + підзаголовок з деталями.

**9. Meta description homepage — 128 символів (нижче ідеалу 140-160)**
Можна розширити ще на 12-32 символи.

**10. IndexNow не реалізований**
Нові сторінки потрапляють до Bing тільки через sitemap crawl. Рекомендується: IndexNow API + Vercel GitHub Actions deploy hook.

### LOW / Інформаційно

- `lang="en-US"` на всіх сторінках — відмінно ✅
- `<meta name="viewport">` на всіх — відмінно ✅
- `robots: index, follow` явно прописано — відмінно ✅
- AI crawlers у robots.txt: GPTBot, ClaudeBot, OAI-SearchBot, Google-Extended, PerplexityBot, Applebot-Extended — відмінне покриття ✅
- Весь CSS inline — критичний CSS завжди inline — відмінно ✅
- SSR/статичний рендеринг — Google бачить повний HTML без JS ✅
- Security headers: перевірити `vercel.json` на X-Frame-Options, X-Content-Type-Options, Referrer-Policy

---

## Section 2: Content Quality / E-E-A-T — 54/100

### E-E-A-T Breakdown

| Фактор | Бал | Оцінка |
|---|---|---|
| Experience | 15/20 | Частково |
| Expertise | 14/25 | Слабко |
| Authoritativeness | 7/25 | Критично |
| Trustworthiness | 22/30 | Середньо |

### CRITICAL

**1. Жодного named автора на жодній зі статей**
Всі 38 blog-статей атрибутовані Organization ("Lumo AI Agency"), не Person. Це прямий сигнал AI batch-контенту. Per QRG September 2025 — Expertise score прагне до нуля без named human author.

**2. 5 ключових статистик повністю непідтверджені на сторінці**
| Заявка | Підтвердження |
|---|---|
| 300+ clients | Відсутнє |
| 410% avg organic traffic growth | Відсутнє (немає методології, періоду, базису) |
| 8.7x average ROAS | Відсутнє |
| $30M+ attributed revenue | Відсутнє |
| 200+ AI automations | Відсутнє |

Всі 5 є "unsubstantiated superlatives" за QRG + ризик FTC advertising compliance ("Austin's leading AI marketing agency").

**3. Невалідний JSON-LD у blog-статтях**
Single-quoted рядки у JSON-LD (`"description": 'Traditional agencies...'`) — невалідний JSON. Google's Rich Results Test не обробляє такий блок. FAQ та Article rich results недоступні для всіх 38 статей.

**4. Нуль third-party авторитетних сигналів**
Відсутні: press mentions, awards, Clutch/G2 badges, Google Partner badge, Meta Business Partner, media coverage (Inc., Forbes, Austin Business Journal). "Austin's leading" без будь-якого третього-party підтвердження.

### HIGH

**5. Testimonials — лише ініціали, без компаній**
Kevin R., Michelle B., David T. — "Co-Founder, SaaS startup". Без full name, company name, LinkedIn, фото. Quality Raters оцінюють як manufactured trust signals.

**6. Всі 38 blog-статей опубліковані в один день (2026-05-15)**
Strongest AI content batch-generation signal. Combination with batch Python scripts у git history = сильне зниження довіри до контенту.

**7. Meta description contact page: "No real address or phone — contact form only"**
Це direct admission, що NAP відсутній. Критично для Local SEO.

**8. "Meet the Team" → about.html — якщо там немає real named bios, E-E-A-T chain обривається**

### MEDIUM

- Homepage body copy ~520 words — мінімальний поріг
- "Why Lumo" section — 125 words для найважливішого E-E-A-T блоку
- CTA inconsistency: "Free Proposal" vs "Strategy Call" vs "Free Audit" (3 різні nav)
- Jargon без пояснень ("RAG pipelines", "entity optimization") для non-technical audience

### Top 5 E-E-A-T Fixes (ROI-пріоритет)

1. Виправити JSON-LD single→double quotes у всіх 38 статтях (find & replace)
2. Додати named author (хоча б одну особу: "Sarah Chen, Head of SEO") до всіх статей
3. Виправити/пояснити канадський телефон
4. Додати один named case study з metrics linked з homepage
5. Додати Clutch або Google Reviews widget (≥5 відгуків)

---

## Section 3: Schema / Structured Data — 65/100

### CRITICAL

**1. Телефон +16473701888 — Toronto area code 647, не Austin**
Присутній у Organization, LocalBusiness schema, footer HTML, всіх local pages. Austin використовує 512 та 737.

**2. Назва бізнесу — три варіанти**
- Homepage Organization: "Lumo AI Agency"
- Contact page publisher: "Lumo Agency"  
- Всі local pages: "Lumo"

**3. WebSite SearchAction → WordPress-параметр на статичному сайті**
Видалити `potentialAction` повністю або реалізувати site search.

### HIGH

**4. @id cross-linking між graph nodes відсутній**
Organization та LocalBusiness — два непов'язані entities. Google Knowledge Graph не може consolidate їх.

Рішення: додати `"@id": "https://lumoaiagency.com/#organization"` та `"@id": "https://lumoaiagency.com/#local-business"` + `"parentOrganization": {"@id": "..."}`.

**5. URL trailing slash — schema не збігається з canonical**
Canonical href: `https://lumoaiagency.com/` (зі slash)  
Schema url: `https://lumoaiagency.com` (без slash)

**6. SameAs — неканонічні hostname**
- `twitter.com` → має бути `x.com`
- Відсутні: Facebook, TikTok (обидва релевантні для marketing agency)

**7. LocalBusiness @type — занадто generic**
Замінити на `["LocalBusiness", "ProfessionalService"]`

### MEDIUM

**8. areaServed — тільки Country level**
Сайт має 303 local pages по містах. Додати top 6-7 міст:
```json
{"@type": "City", "name": "Austin"}, {"@type": "City", "name": "New York City"}, ...
```

**9. AggregateRating відсутній на homepage**
3 testimonials з specific numbers існують у HTML, але невидимі для structured data parsers.

**10. WebPage node на homepage відсутній**
Додати з `isPartOf`, `primaryImageOfPage`, `dateModified`.

**11. Service.provider на service pages використовує "Lumo Agency"**
Має бути "Lumo AI Agency" + `@id` reference.

**12. openingHours → deprecated, замінити на openingHoursSpecification**

### Рекомендований виправлений @graph (скорочено):
```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Organization",
      "@id": "https://lumoaiagency.com/#organization",
      "name": "Lumo AI Agency",
      "url": "https://lumoaiagency.com/",
      "sameAs": ["https://www.instagram.com/lumoaiagency", "https://x.com/lumoaiagency", "https://www.linkedin.com/company/lumoaiagency", "https://www.youtube.com/@lumoaiagency"]
    },
    {
      "@type": ["LocalBusiness", "ProfessionalService"],
      "@id": "https://lumoaiagency.com/#local-business",
      "name": "Lumo AI Agency",
      "parentOrganization": {"@id": "https://lumoaiagency.com/#organization"},
      "image": "https://lumoaiagency.com/og-image.jpg",
      "aggregateRating": {"@type": "AggregateRating", "ratingValue": "5.0", "reviewCount": "300"}
    }
  ]
}
```

---

## Section 4: Sitemap — Часткові проблеми

| Перевірка | Статус | Severity |
|---|---|---|
| URL count (~481 vs 596 очікуваних) | Розрив ~115 | Medium |
| Trailing slash непослідовний | FAIL | Medium |
| .html розширення відсутні | PASS ✅ | — |
| lastmod — реалістичні дати | PASS ✅ | — |
| Blog у sitemap | ВІДСУТНІЙ | High |
| Industries hub /industries/ у sitemap | ВІДСУТНІЙ | Medium |
| Robots.txt Sitemap декларація | PASS ✅ | — |
| Image sitemap | ВІДСУТНІЙ | Low |
| 360 local pages — doorway page risk | ПОПЕРЕДЖЕННЯ | High |

### Doorway Page Risk
303 local pages (20 міст × ~18 slug) — повністю ідентична структура з заміною лише назви міста. `local/austin/seo-agency/index.html` та `local/chicago/seo-agency/index.html` ідентичні рядок за рядком. Це class doorway page pattern. Пріоритет: диференціювати топ-5 міст (Austin, NY, LA, Chicago, Houston) реальним city-specific контентом.

---

## Section 5: Performance / Core Web Vitals — 72/100 (Оцінка B+)

| Метрика | Прогноз | Ризик |
|---|---|---|
| LCP | 1.5–2.8s | Google Fonts синхронне блокування |
| CLS | 0.02–0.08 | FOUT без size-adjust |
| INP | 50–120ms | Практично відсутній |

### CRITICAL: Google Fonts — синхронне блокування LCP

Поточний стан:
```html
<link href="https://fonts.googleapis.com/css2?family=Berkshire+Swash&family=Inter:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet" />
```

Рішення (non-blocking):
```html
<link rel="preload" as="style" href="https://fonts.googleapis.com/css2?family=Berkshire+Swash&family=Inter:wght@400;500;600;700;800;900&display=swap" onload="this.onload=null;this.rel='stylesheet'">
<noscript><link rel="stylesheet" href="https://fonts.googleapis.com/css2?..."></noscript>
```
Також видалити `wght@300` — не використовується в CSS.

### MEDIUM: Fallback font без size-adjust → FOUT → CLS

```css
@font-face {
  font-family: 'Berkshire Swash Fallback';
  src: local('Georgia');
  size-adjust: 105%;
  ascent-override: 90%;
}
```

### LOW

- Додати `@media (prefers-reduced-motion: reduce) { .blob { animation: none; } }`
- На мобільних зменшити `filter: blur(80px)` → `blur(40px)` для blob
- `meta viewport interactive-widget=resizes-content` для iOS CLS

### Позитивне ✅

- `will-change: transform` на всіх blob — GPU composited анімації
- `passive: true` на всіх scroll listeners — INP safe
- Весь CSS inline — нульовий render-blocking CSS
- Жодного `<img>` на сторінці — нульовий image payload

---

## Section 6: GEO / AI Search Readiness — 71/100

| Платформа | Оцінка | Головний блокер |
|---|---|---|
| Google AI Overviews | 64/100 | Немає question headings, немає AggregateRating, phone mismatch |
| ChatGPT | 72/100 | llms.txt є, FAQ schema сильний, немає named authors |
| Perplexity | 75/100 | Static HTML crawlable, llms.txt є, stats добре структуровані |
| Bing Copilot | 68/100 | LocalBusiness schema є, немає Review schema, phone mismatch |

### Позитивне ✅

- Всі major AI crawlers явно дозволені в robots.txt (GPTBot, ClaudeBot, PerplexityBot, Google-Extended, Applebot-Extended)
- `llms.txt` присутній — вище середнього по галузі
- FAQPage schema — 5 self-contained Q&A пар — найсильніший GEO актив сайту
- Static HTML — весь контент доступний без JS для AI crawlers
- Pricing in FAQ schema ($1,200/$3,000/$6,500) — citation-ready

### Gaps

**1. Stats semantically disconnected у DOM**
```html
<!-- Поточна структура — AI parser не може асоціювати 410% з Traffic Growth -->
<div class="hstat-num lime">410%</div>
<div class="hstat-label">Avg Traffic Growth</div>
```
Рішення: замінити на `<dl>/<dt>/<dd>` pairs для semantic pairing.

**2. Немає named humans на сайті**
Нуль named founders, authors, team members. AI системи сильно знижують citation confidence для контенту без людських expert-атрибуцій.

**3. Немає question-based H2/H3 headings**
Всі H2 декларативні ("AI-Powered Services for Modern Businesses"). Жоден не відповідає формату AI Overview trigger. Додати секцію з:
- "What is an AI Marketing Agency?"
- "How Does AI-Powered SEO Work?"
- "What Results Can I Expect from AI Marketing?"

**4. AggregateRating відсутній**
3 testimonials з числами існують у HTML але невидимі для structured data parsers.

---

## Section 7: Local SEO — 30.6/100 (КРИТИЧНО)

| Dimension | Вага | Бал | Зважений |
|---|---|---|---|
| GBP Signals | 25% | 12/100 | 3.0 |
| Reviews & Reputation | 20% | 28/100 | 5.6 |
| Local On-Page SEO | 20% | 52/100 | 10.4 |
| NAP Consistency | 15% | 45/100 | 6.8 |
| Local Schema | 10% | 38/100 | 3.8 |
| Local Link & Authority | 10% | 10/100 | 1.0 |
| **TOTAL** | | | **30.6 / 100** |

### CRITICAL

**1. Телефон (647) — Toronto area code**
Найважливіша проблема для Local SEO. Austin: 512 або 737. Canadian number на "Austin's leading agency" = Google Business Profile verification risk + local pack penalty.

**2. Contact page meta description: "No real address or phone — contact form only"**
Це буквальне визнання відсутності NAP Google. Потрібно негайно виправити.

**3. Назва бізнесу у 3 варіантах** (детально у Section 3)

**4. Doorway Pages — FAIL**
`local/austin/seo-agency/` та `local/chicago/seo-agency/` ідентичні рядок за рядком. 303 pages = significant algorithmic risk під March 2024 Helpful Content Update.

### HIGH

**5. GBP — нульова інтеграція**
- Немає Google Maps embed на жодній сторінці
- Немає GBP URL у `sameAs` array
- Немає Google Reviews widget
- Немає directions link

GBP signals = #1 local pack ranking factor (Whitespark 2026).

**6. AggregateRating на local pages без verifiable source**
4.9/127 reviews на local page schemas без посилання на review platform = schema policy risk.

**7. Повна адреса невидима на contact page**
600 Congress Ave має бути видимим текстом на contact.html.

**8. Non-Austin local pages мають Austin phone + addressLocality: "Chicago"**
False local address signal → GBP spam policy risk.

### MEDIUM

- `openingHours` → deprecated (використати `openingHoursSpecification`)
- `areaServed` на local pages використовує `servedArea` (невалідна property)
- Geo precision: 4 decimal places → 5+
- Немає Clutch, G2, Austin Chamber profiles
- Nearby cities sections географічно некоректні (Austin "nearby" = Albuquerque)

---

## Section 8: On-Page SEO / SXO — 58/100

### Page-Type Match Analysis

| Keyword | Intent | Page Type Match | Severity |
|---|---|---|---|
| "AI marketing agency Austin" | Local commercial | MEDIUM mismatch | Додати Austin-specific section |
| "AI marketing agency" | National commercial | ALIGNED ✅ | — |
| "Austin marketing agency" | Local general | ALIGNED ✅ | — |
| "AI SEO agency" | Specialized commercial | HIGH mismatch | Потрібна dedicated service page |

### CRITICAL: Hero stats приховані на мобільних

```css
@media (max-width: 900px) { .hero-visual { display: none; } }
```

4 ключові credibility metrics (300+, 410%, 8.7x, 200+) невидимі на mobile. Mobile = більшість first-touch трафіку.

### Відсутні секції (vs. competitor benchmark)

| Секція | Competitor Presence | Lumo | Пріоритет |
|---|---|---|---|
| Named client logo bar | Single Grain, NoGood, Thrive | ❌ | Critical |
| How We Work (process) | Keenfolks, NoGood | ❌ | High |
| Awards / Certifications | WebFX, Thrive | ❌ | High |
| Visible FAQ accordion | Most top-10 | ❌ | Medium |
| Industry tabs | Single Grain, NoGood | ❌ | Medium |
| Pricing teaser | NP Digital, NoGood | ❌ | Medium |
| Blog link in nav | Industry standard | ❌ | Low |

### Persona Scores

| Persona | Score | Головний Gap |
|---|---|---|
| Skeptical CFO | 38/100 | Немає pricing preview, немає ROI methodology |
| Comparison Shopper | 44/100 | Немає Clutch badge, named clients, competitor comparison hook |
| Local Austin Buyer | 52/100 | Немає map embed, немає office photo |
| AI-Curious Marketer | 56/100 | Немає process diagram, немає tech stack name |
| Ready-to-Buy | 62/100 | Немає inline form, CTA copy inconsistent |

---

## Section 9: Images — 40/100

- Жодного `<img>` тегу на homepage — нульовий image payload (перевага для performance)
- `og-image.jpg` referenced у meta але файл не підтверджений як існуючий
- `logo.png` у schema але файл не підтверджений
- Немає image sitemap
- Немає WebP/AVIF оптимізованих зображень (бо немає зображень взагалі)
- Відсутність реальних фото команди, офісу, clients — damage для E-E-A-T

---

## Limitations

- Немає Google API credentials → без CrUX field data (реальний LCP/CLS/INP)
- Немає Moz/Bing API → без live backlink profile
- Немає DataForSEO → без live SERP positions
- Немає GBP dashboard access → GBP status, category, review velocity невідомі
- Drift baseline відсутній → перший запуск, немає порівняння
- Local page content uniqueness: перевірено Austin vs Chicago; решта 301 pages не перевірялись індивідуально
