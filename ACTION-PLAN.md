# SEO Action Plan — Lumo AI Agency
**Дата:** 2026-05-16 | **Health Score:** 62/100 | **Local SEO:** 30.6/100

---

## CRITICAL — Виправити негайно (цього тижня)

### 1. Замінити всі `href="*.html"` на clean URL
**Вплив:** Technical SEO, PageRank consolidation  
**Файли:** index.html, services.html, about.html, contact.html, pricing.html + шаблони service/local pages  
**Зміна:** `href="services.html"` → `href="/services"`, `href="about.html"` → `href="/about"`, `href="index.html"` → `href="/"`  
**Час:** 2-3 год (пошук і заміна по всіх файлах)

### 2. Виправити JSON-LD single quotes у всіх 38 blog-статтях
**Вплив:** FAQ та Article rich results відновляться; GEO score +8-10 балів  
**Дія:** Find & replace `': '` → `": "` у JSON-LD блоках blog/*/index.html  
**Час:** 30 хвилин (скрипт або bulk replace)

### 3. Вирішити проблему телефону +1 (647) — Toronto area code
**Вплив:** Local SEO, GBP verification, entity confidence у всіх AI platforms  
**Варіанти:**
- Отримати Austin DID number (512/737 area code) через Twilio або Google Voice
- Або прибрати telephone з LocalBusiness schema до вирішення
**Час:** 1 год (за наявності US number)

### 4. Видалити WebSite SearchAction (WordPress параметр на статичному сайті)
**Вплив:** Schema integrity  
**Дія:** Видалити блок `"potentialAction"` з WebSite schema в index.html  
**Час:** 5 хвилин

### 5. Noindex на design-system.html
**Дія:** Додати `<meta name="robots" content="noindex, nofollow">` в head  
**Час:** 5 хвилин

### 6. Стандартизувати назву до "Lumo AI Agency" скрізь
**Файли:** contact.html (schema publisher "Lumo Agency"), всі local pages (schema "Lumo")  
**Час:** 1-2 год (bulk replace)

---

## HIGH — Виправити протягом тижня

### 7. Додати named автора до blog-статей
**Вплив:** E-E-A-T Expertise signal, AI citation readiness  
**Дія:**
- Створити autor bio page (напр. `/team/alex-morgan/`)
- Змінити Article schema `author` з `@type: Organization` на `@type: Person` з ім'ям, URL, jobTitle
- Додати видиму byline під заголовком кожної статті  
**Час:** 3-4 год (шаблон + bulk update)

### 8. Виправити contact page
- Видалити "No real address or phone — contact form only" з meta description
- Додати видимий NAP: "600 Congress Ave, Austin, TX 78701 | Mon–Fri 9am–6pm"
- Додати Google Maps embed або link на Google Maps  
**Час:** 1 год

### 9. Додати blog URL до sitemap.xml
**Вплив:** Crawl budget, indexation speed  
**Дія:** Додати 39 URL (/blog/ + 38 статей) у sitemap з `changefreq: weekly`, `priority: 0.7`, `lastmod: 2026-05-15`  
**Час:** 1 год (або скрипт для автогенерації)

### 10. Стандартизувати trailing slash у sitemap
**Дія:** Вирішити — slash або без slash — і застосувати однаково до всіх ~481 URL  
- Services: `/services/seo` → `/services/seo/` (якщо Vercel serves з slash)
- Local: `/local/austin/ai-marketing-agency` → `/local/austin/ai-marketing-agency/`  
**Час:** 2 год (скрипт або bulk replace у sitemap.xml)

### 11. Виправити footer посилання на absolute paths
**Дія:** `href="local/austin/seo-agency/index.html"` → `href="/local/austin/seo-agency/"`  
**Час:** 2 год

### 12. Додати /industries/ до sitemap
**Дія:** Переконатися, що industries/index.html задеплоєний, додати URL до sitemap  
**Час:** 30 хвилин

### 13. Non-blocking Google Fonts loading (LCP fix)
**Вплив:** LCP -0.5-1.0s, особливо на mobile та slow connections  
**Дія:** Замінити `<link rel="stylesheet">` на preload pattern:
```html
<link rel="preload" as="style" href="https://fonts.googleapis.com/css2?family=Berkshire+Swash&family=Inter:wght@400;500;600;700;800;900&display=swap" onload="this.onload=null;this.rel='stylesheet'">
<noscript><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Berkshire+Swash&family=Inter:wght@400;500;600;700;800;900&display=swap"></noscript>
```
Прибрати `wght@300` — не використовується.  
**Час:** 30 хвилин

### 14. Зробити hero stats видимими на mobile
**Вплив:** Mobile conversion rate, trust signals  
**Дія:** Замість `display:none` на `.hero-visual` при 900px — показати condensed 2-stat row (300+ clients + 410% traffic)  
**Час:** 1-2 год (CSS + HTML)

---

## MEDIUM — Виправити протягом місяця

### 15. Виправити Schema: @id cross-linking, @type, AggregateRating
**Дія:**
- Додати `"@id"` до Organization та LocalBusiness blocks
- `"parentOrganization": {"@id": "..."}` у LocalBusiness
- Замінити `LocalBusiness` → `["LocalBusiness", "ProfessionalService"]`
- Додати `AggregateRating` до LocalBusiness (після появи verifiable reviews)
- Виправити `openingHours` → `openingHoursSpecification`
- Виправити `sameAs`: twitter.com → x.com; додати https://
- Видалити `WebPage` node якщо немає live schema tool  
**Час:** 2-3 год

### 16. Додати question-based H2 секцію на homepage
**Вплив:** AI Overview triggers, GEO score +8-12 балів  
**Дія:** Нова секція між Services та Testimonials з 3 питаннями:
- "What is an AI Marketing Agency?" (~150 words)
- "How Does AI-Powered SEO Differ from Traditional SEO?" (~150 words)
- "What ROI Can I Expect from AI Marketing?" (~150 words)  
**Час:** 3-4 год

### 17. Зробити FAQ visible на homepage
**Вплив:** Конверсія (видна відповідь на pricing питання), GEO  
**Дія:** Додати accordion секцію перед CTA band з 5 питань з FAQ schema (pricing, timeline, services, location, results)  
**Час:** 2-3 год

### 18. Диференціювати топ-5 local pages
**Вплив:** Doorway page risk mitigation, rankings  
**Міста:** Austin, New York, Los Angeles, Chicago, Houston  
**Мінімум на сторінку:**
- Унікальний intro параграф з city-specific даними
- Хоча б 1 local statistic або market data point
- Географічно коректний "Nearby cities" список
- City-specific CTA  
**Час:** 5-8 год (5 сторінок × 1-1.5 год)

### 19. Виправити LocalBusiness schema на local pages
**Дія:**
- `servedArea` → `areaServed`
- `name: "Lumo"` → `name: "Lumo AI Agency"`
- Прибрати false local address (addressLocality: "Chicago" + Austin phone)
- Додати `geo` coordinates для кожного міста  
**Час:** 2 год (bulk replace + city centroid data)

### 20. Виправити services.html title tag
**Поточний:** "All 105 AI Growth Services | Lumo AI Agency" (45 символів)  
**Рекомендований:** "AI Marketing Services — 105+ Solutions | Lumo AI Agency" (57 символів)  
**Час:** 5 хвилин

### 21. Розширити meta description homepage до 140+ символів
**Поточна:** 128 символів  
**Дія:** Додати value prop: "...Get a free proposal and see your custom growth forecast."  
**Час:** 10 хвилин

### 22. Додати pricing teaser на homepage
**Дія:** Рядок "Plans from $1,200/mo — see full pricing →" між Services та Why Lumo  
**Вплив:** CFO persona conversion, reduces bounce  
**Час:** 30 хвилин

### 23. Виправити CTA inconsistency
**Поточно:** "Get Started" (nav) / "Get Your Free Proposal" (hero) / "Get a Free Audit" (blog nav)  
**Дія:** Обрати одну мову і застосувати скрізь. Рекомендація: "Get Your Free Proposal"  
**Час:** 1 год (по всіх шаблонах)

### 24. Додати stat semantic pairing (DL/DT/DD)
**Вплив:** GEO — AI parsers зможуть правильно асоціювати "410%" з "Avg Traffic Growth"  
**Дія:** Замінити `<div class="hstat">` structure на `<dl>/<dt>/<dd>` у stats bar  
**Час:** 1 год

### 25. Додати `prefers-reduced-motion` для blob animations
```css
@media (prefers-reduced-motion: reduce) { .blob { animation: none; } }
```  
**Час:** 10 хвилин

---

## LOW — Backlog (коли буде час)

### 26. Додати третій-party proof на homepage
- Claim Clutch.co profile → отримати reviews → додати Clutch badge
- Claim G2 profile
- Якщо є Google Business Profile → додати Google Rating widget
- Оновити Organization `sameAs` з Clutch URL та G2 URL  
**Вплив:** Authority score, E-E-A-T, AI citation confidence  

### 27. Верифікувати та оптимізувати Google Business Profile
- Перевірити category (має бути "Marketing Agency")
- Верифікувати адресу 600 Congress Ave
- Додати GBP URL у homepage Organization sameAs
- Додати Maps embed на contact.html  
**Вплив:** #1 local pack ranking factor  

### 28. Додати named client logos або verifiable testimonials
- Попросити 1-2 клієнтів дозволити назвати компанію
- Або: "Trusted by companies in SaaS, E-commerce, Healthcare, Professional Services" label row  
**Вплив:** Experience E-E-A-T, conversion rate  

### 29. Додати "How We Work" process section (4 steps)
Audit → Strategy → Build → Scale  
**Вплив:** Consideration-stage conversion, "AI SEO agency" keyword intent  

### 30. Реалізувати IndexNow
- Зареєструватися на indexnow.org
- Додати API key файл у корінь
- Vercel GitHub Actions → IndexNow API call на deploy  

### 31. Виправити security headers у vercel.json
```json
{"key": "X-Frame-Options", "value": "SAMEORIGIN"},
{"key": "X-Content-Type-Options", "value": "nosniff"},
{"key": "Referrer-Policy", "value": "strict-origin-when-cross-origin"}
```

### 32. Додати Blog link у navbar
Homepage не має видимого шляху до blog контенту з навігації.  

### 33. Додати image sitemap для blog assets
Blog articles likely have featured images — image sitemap enables Google Image Search indexing.  

### 34. Виправити `<li>` у `<div>` у nearby cities sections
```html
<!-- Невалідно -->
<div class="nearby-grid"><li>...</li></div>
<!-- Правильно -->
<ul class="nearby-grid"><li>...</li></ul>
```

### 35. Розробити og-image.jpg та logo.png
- `og-image.jpg` referenced у meta/schema але існування не підтверджено
- Social sharing previews залежать від цього файлу
- Мінімум: 1200×630px для OG, 200×60px для logo

---

## Пріоритетний summary

| # | Дія | Severity | Зусилля | Вплив |
|---|---|---|---|---|
| 1 | href .html → clean URLs | Critical | 2h | Technical + PageRank |
| 2 | Blog JSON-LD single→double quotes | Critical | 30m | Rich results, GEO |
| 3 | Вирішити телефон (647) | Critical | 1h | Local SEO, Entity confidence |
| 4 | Видалити SearchAction | Critical | 5m | Schema integrity |
| 5 | Noindex design-system.html | Critical | 5m | Index cleanliness |
| 6 | Назва → "Lumo AI Agency" скрізь | Critical | 1h | NAP consistency |
| 7 | Named author на blog | High | 4h | E-E-A-T Expertise |
| 8 | Виправити contact page | High | 1h | Local SEO, Trust |
| 9 | Blog у sitemap | High | 1h | Crawl, Indexation |
| 10 | Trailing slash standardize | High | 2h | Technical |
| 11 | Non-blocking fonts | High | 30m | LCP |
| 12 | Hero stats на mobile | High | 2h | Mobile conversion |
| 13 | Question-based H2 section | Medium | 4h | GEO, AI Overviews |
| 14 | FAQ visible accordion | Medium | 3h | GEO, Conversion |
| 15 | Диференціювати local pages | Medium | 8h | Doorway page risk |

**Прогноз після критичних + high фіксів:** Health Score: 62 → ~76/100 | Local SEO: 30.6 → ~52/100
