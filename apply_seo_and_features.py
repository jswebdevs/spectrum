import os
import re

SITE_SCRIPT = '/home/newadmin/Projects/Spectrum/plain-html/generate_site.py'

with open(SITE_SCRIPT, 'r', encoding='utf-8') as f:
    code = f.read()

# 1. Update imports
old_import = "from update_all_pages import COMMON_HEAD, COMMON_TOP_BAR, get_navbar, COMMON_FOOTER"
new_import = "from update_all_pages import get_head, COMMON_HEAD, COMMON_TOP_BAR, get_navbar, COMMON_FOOTER"
assert old_import in code, "Could not find import statement"
code = code.replace(old_import, new_import, 1)

# 2. Update Index Head
old_index_head = """<head>
    <title>Spectrum IT Solutions: Software Company in Bangladesh</title>
    <meta name="description" content="Spectrum IT Solutions Ltd. is a leading Dhaka-based software company delivering digital identity, biometric infrastructure, smart cards, AI systems, and national enterprise solutions.">
    <link rel="canonical" href="index.html">
{COMMON_HEAD}
</head>"""

new_index_head = """<head>
{get_head(
    title="Spectrum IT Solutions: Software Company in Bangladesh",
    description="Spectrum IT Solutions Ltd. is a leading Dhaka-based software company delivering digital identity, biometric infrastructure, smart cards, AI systems, and national enterprise solutions.",
    canonical_slug="index.html",
    og_image="assets/img/banner_img_01.jpg"
)}
</head>"""
assert old_index_head in code, "Could not find old_index_head"
code = code.replace(old_index_head, new_index_head, 1)

# 3. Update Services Head
old_services_head = """<head>
    <title>IT and Software Services in Bangladesh | Spectrum</title>
    <meta name="description" content="Explore Spectrum's comprehensive IT services including digital identity, biometric infrastructure, smart cards, AI systems, ERP, cybersecurity, and smart city solutions.">
    <link rel="canonical" href="services.html">
{COMMON_HEAD}
</head>"""

new_services_head = """<head>
{get_head(
    title="IT and Software Services in Bangladesh | Spectrum IT Solutions Ltd.",
    description="Explore Spectrum's comprehensive IT services including digital identity, biometric infrastructure, smart cards, AI systems, ERP, cybersecurity, and smart city solutions.",
    canonical_slug="services.html",
    og_image="assets/img/Our_Services_3.jpg"
)}
</head>"""
assert old_services_head in code, "Could not find old_services_head"
code = code.replace(old_services_head, new_services_head, 1)

# 4. Update Projects Head
old_projects_head = """<head>
    <title>National &amp; Enterprise Projects | Spectrum IT Solutions Ltd.</title>
    <meta name="description" content="Discover major public and enterprise projects delivered by Spectrum IT Solutions: TCB Smart Family Card (10M+ families), Industrial e-Court BD, National e-Licensing, and smart card platforms.">
    <link rel="canonical" href="projects.html">
{COMMON_HEAD}
</head>"""

new_projects_head = """<head>
{get_head(
    title="National &amp; Enterprise Projects | Spectrum IT Solutions Ltd.",
    description="Discover major public and enterprise projects delivered by Spectrum IT Solutions: TCB Smart Family Card (10M+ families), Industrial e-Court BD, National e-Licensing, and smart card platforms.",
    canonical_slug="projects.html",
    og_image="assets/img/project_1.png"
)}
</head>"""
assert old_projects_head in code, "Could not find old_projects_head"
code = code.replace(old_projects_head, new_projects_head, 1)

# 5. Update Case Study Head
old_cs_head = """<head>
    <title>Enterprise Case Studies | National Scale Deployments | Spectrum IT Solutions Ltd.</title>
    <meta name="description" content="Explore real-world case studies of sovereign-scale systems engineered by Spectrum IT Solutions: TCB Smart Family Card (10M+ families), Industrial e-Court BD, National e-Licensing, and smart card platforms.">
    <link rel="canonical" href="case-study.html">
{COMMON_HEAD}
</head>"""

new_cs_head = """<head>
{get_head(
    title="Enterprise Case Studies | National Scale Deployments | Spectrum IT Solutions Ltd.",
    description="Explore real-world case studies of sovereign-scale systems engineered by Spectrum IT Solutions: TCB Smart Family Card (10M+ families), Industrial e-Court BD, National e-Licensing, and smart card platforms.",
    canonical_slug="case-study.html",
    og_image="assets/img/project_1.png"
)}
</head>"""
assert old_cs_head in code, "Could not find old_cs_head"
code = code.replace(old_cs_head, new_cs_head, 1)

# 6. Update DIS Head
old_dis_head = """<head>
    <title>Digital Identity and Security | Spectrum IT Solutions</title>
    <meta name="description" content="Digital Identity &amp; Security solutions by Spectrum IT Solutions Ltd., featuring national biometric deduplication, KYC engines, and automated ID verification.">
    <link rel="canonical" href="Digital_Identity_&_Security.html">
{COMMON_HEAD}
</head>"""

new_dis_head = """<head>
{get_head(
    title="Digital Identity and Security | Spectrum IT Solutions",
    description="Digital Identity & Security solutions by Spectrum IT Solutions Ltd., featuring national biometric deduplication, KYC engines, and automated ID verification.",
    canonical_slug="Digital_Identity_&_Security.html",
    og_image="assets/img/Digital-Identity-&-Security.jpg"
)}
</head>"""
assert old_dis_head in code, "Could not find old_dis_head"
code = code.replace(old_dis_head, new_dis_head, 1)

# 7. Update Contact Head
old_contact_head = """<head>
    <title>Contact Spectrum IT Solutions, Dhaka</title>
    <meta name="description" content="Contact Spectrum IT Solutions Ltd. in Dhaka, Bangladesh for sovereign digital identity, smart card personalization, biometric systems, and enterprise software engineering.">
    <link rel="canonical" href="contact.html">
{COMMON_HEAD}
</head>"""

new_contact_head = """<head>
{get_head(
    title="Contact Corporate Headquarters | Spectrum IT Solutions Ltd.",
    description="Contact Spectrum IT Solutions Ltd. in Dhaka, Bangladesh for sovereign digital identity, smart card personalization, biometric systems, and enterprise software engineering.",
    canonical_slug="contact.html",
    og_image="assets/img/contact_img.png"
)}
</head>"""
assert old_contact_head in code, "Could not find old_contact_head"
code = code.replace(old_contact_head, new_contact_head, 1)

# 8. Update AI Head
old_ai_head = """<head>
    <title>Artificial Intelligence Solutions | Spectrum IT Solutions</title>
    <meta name="description" content="Artificial Intelligence and machine learning engineering by Spectrum IT Solutions: computer vision, automated document parsing, and enterprise cognitive systems.">
    <link rel="canonical" href="Artificial_Intelligence.html">
{COMMON_HEAD}
</head>"""

new_ai_head = """<head>
{get_head(
    title="Artificial Intelligence Solutions | Spectrum IT Solutions",
    description="Artificial Intelligence and machine learning engineering by Spectrum IT Solutions: computer vision, automated document parsing, and enterprise cognitive systems.",
    canonical_slug="Artificial_Intelligence.html",
    og_image="assets/img/Artificial_Intelligence.png"
)}
</head>"""
assert old_ai_head in code, "Could not find old_ai_head"
code = code.replace(old_ai_head, new_ai_head, 1)

# 9. Update About Head
old_about_head = """<head>
    <title>About Spectrum IT Solutions Ltd., Dhaka | Executive Leadership &amp; History</title>
    <meta name="description" content="Discover Spectrum IT Solutions Ltd. - Over 12+ years delivering sovereign digital transformation, biometric identity, and mission-critical software engineering. Meet our Chairman Kabir Ahmed Bhuiyan.">
    <link rel="canonical" href="about_us.html">
{COMMON_HEAD}
</head>"""

new_about_head = """<head>
{get_head(
    title="About Spectrum IT Solutions Ltd., Dhaka | Executive Leadership &amp; History",
    description="Discover Spectrum IT Solutions Ltd. - Over 12+ years delivering sovereign digital transformation, biometric identity, and mission-critical software engineering. Meet our Chairman Kabir Ahmed Bhuiyan.",
    canonical_slug="about_us.html",
    og_image="assets/img/chairman_Sir.png"
)}
</head>"""
assert old_about_head in code, "Could not find old_about_head"
code = code.replace(old_about_head, new_about_head, 1)

# 10. Update Products Head
old_products_head = """<head>
    <title>Enterprise Products | Hardware &amp; Software Solutions | Spectrum IT Solutions Ltd.</title>
    <meta name="description" content="Discover Spectrum IT Solutions enterprise products: Smart Card Printers, Biometric Terminals, Access Control, Kiosks, CCTV, GPS Trackers, ERP, and e-KYC.">
    <link rel="canonical" href="products.html">
{COMMON_HEAD}
</head>"""

new_products_head = """<head>
{get_head(
    title="Enterprise Products | Hardware &amp; Software Solutions | Spectrum IT Solutions Ltd.",
    description="Discover Spectrum IT Solutions enterprise products: Smart Card Printers, Biometric Terminals, Access Control, Kiosks, CCTV, GPS Trackers, ERP, and e-KYC platforms.",
    canonical_slug="products.html",
    og_image="assets/img/sm-card-about.png"
)}
</head>"""
assert old_products_head in code, "Could not find old_products_head"
code = code.replace(old_products_head, new_products_head, 1)

# 11. Update SCT Head
old_sct_head = """<head>
    <title>Smart Card Technologies | Spectrum IT Solutions</title>
    <meta name="description" content="Turnkey smart card personalization, dual-interface chip encoding, laser engraving, and automated kiosk platforms by Spectrum IT Solutions.">
    <link rel="canonical" href="Smart_Card_Technologies.html">
{COMMON_HEAD}
</head>"""

new_sct_head = """<head>
{get_head(
    title="Smart Card Technologies &amp; Personalization | Spectrum IT Solutions",
    description="Turnkey smart card personalization, dual-interface chip encoding, laser engraving, and automated kiosk platforms by Spectrum IT Solutions.",
    canonical_slug="Smart_Card_Technologies.html",
    og_image="assets/img/banner_img_03.jpg"
)}
</head>"""
assert old_sct_head in code, "Could not find old_sct_head"
code = code.replace(old_sct_head, new_sct_head, 1)

# 12. Add Category Filter & reveal classes to projects.html
old_projects_row = """        <div class="row g-4">
            <!-- Project 1: TCB Smart Family Card (FLAGSHIP) -->
            <div class="col-lg-4 col-md-6">"""

new_projects_row = """        <!-- Interactive Category Filter Tabs -->
        <div class="filter-nav-wrap mb-5">
            <button class="filter-btn active" data-filter="all">
                <i class="fas fa-layer-group"></i> All Deployments <span class="badge-count">6</span>
            </button>
            <button class="filter-btn" data-filter="identity">
                <i class="fas fa-id-card"></i> Digital Identity &amp; Smart Cards <span class="badge-count">2</span>
            </button>
            <button class="filter-btn" data-filter="governance">
                <i class="fas fa-balance-scale"></i> E-Governance &amp; Judicial <span class="badge-count">2</span>
            </button>
            <button class="filter-btn" data-filter="portal">
                <i class="fas fa-ticket-alt"></i> Verification &amp; E-Ticketing <span class="badge-count">2</span>
            </button>
        </div>

        <div class="row g-4">
            <!-- Project 1: TCB Smart Family Card (FLAGSHIP) -->
            <div class="col-lg-4 col-md-6 filter-item reveal-on-scroll" data-category="identity">"""

assert old_projects_row in code, "Could not find old_projects_row"
code = code.replace(old_projects_row, new_projects_row, 1)

# Replace other project cards in projects.html
code = code.replace(
    '<!-- Project 2: Industrial e-Court Bangladesh -->\n            <div class="col-lg-4 col-md-6">',
    '<!-- Project 2: Industrial e-Court Bangladesh -->\n            <div class="col-lg-4 col-md-6 filter-item reveal-on-scroll" data-category="governance">',
    1
)

code = code.replace(
    '<!-- Project 3: Automated Smart Card & License Issuance Platform -->\n            <div class="col-lg-4 col-md-6">',
    '<!-- Project 3: Automated Smart Card & License Issuance Platform -->\n            <div class="col-lg-4 col-md-6 filter-item reveal-on-scroll" data-category="identity">',
    1
)

code = code.replace(
    '<!-- Project 4: National e-Licensing Platform -->\n            <div class="col-lg-4 col-md-6">',
    '<!-- Project 4: National e-Licensing Platform -->\n            <div class="col-lg-4 col-md-6 filter-item reveal-on-scroll" data-category="governance">',
    1
)

code = code.replace(
    '<!-- Project 5: OCD Online Verification Portal -->\n            <div class="col-lg-4 col-md-6">',
    '<!-- Project 5: OCD Online Verification Portal -->\n            <div class="col-lg-4 col-md-6 filter-item reveal-on-scroll" data-category="portal">',
    1
)

code = code.replace(
    '<!-- Project 6: Novo Theatre Automated e-Ticketing -->\n            <div class="col-lg-4 col-md-6">',
    '<!-- Project 6: Novo Theatre Automated e-Ticketing -->\n            <div class="col-lg-4 col-md-6 filter-item reveal-on-scroll" data-category="portal">',
    1
)

# 13. Add Category Filter & reveal classes to products.html
old_prod_sec1 = """    <!-- SECTION 1: TURNKEY HARDWARE & SPECIALIZED SYSTEMS (8 CORE PRODUCTS) -->
    <div class="container py-5">
        <div class="text-center mb-5">
            <span class="badge px-3 py-2 rounded-pill fw-semibold mb-2" style="background: rgba(242, 101, 34, 0.1); color: #f26522; border: 1px solid rgba(242, 101, 34, 0.25); font-size: 13px;">Turnkey Hardware Systems</span>
            <h2 class="header_two" style="color: #2e3760; font-size: 36px; font-weight: 700;">Hardware &amp; <span style="color: #f26522;">Specialized Devices</span></h2>
            <p class="text-muted mx-auto" style="max-width: 680px; font-size: 15px;">Industrial-grade, ruggedized hardware solutions deployed across national governance platforms, financial institutions, and enterprise facilities.</p>
        </div>

        <div class="row g-4">
            <!-- Product 1: Smart Card & Printer -->
            <div class="col-lg-3 col-md-6 col-sm-6">"""

new_prod_sec1 = """    <!-- SECTION 1: TURNKEY HARDWARE & SPECIALIZED SYSTEMS (8 CORE PRODUCTS) -->
    <div class="container py-5 filter-section">
        <!-- Interactive Category Filter Tabs -->
        <div class="filter-nav-wrap mb-5">
            <button class="filter-btn active" data-filter="all">
                <i class="fas fa-cubes"></i> All Solutions <span class="badge-count">12</span>
            </button>
            <button class="filter-btn" data-filter="hardware">
                <i class="fas fa-microchip"></i> Hardware &amp; Specialized Devices <span class="badge-count">8</span>
            </button>
            <button class="filter-btn" data-filter="software">
                <i class="fas fa-laptop-code"></i> Enterprise Software Suites <span class="badge-count">4</span>
            </button>
        </div>

        <div class="text-center mb-5">
            <span class="badge px-3 py-2 rounded-pill fw-semibold mb-2" style="background: rgba(242, 101, 34, 0.1); color: #f26522; border: 1px solid rgba(242, 101, 34, 0.25); font-size: 13px;">Turnkey Hardware Systems</span>
            <h2 class="header_two" style="color: #2e3760; font-size: 36px; font-weight: 700;">Hardware &amp; <span style="color: #f26522;">Specialized Devices</span></h2>
            <p class="text-muted mx-auto" style="max-width: 680px; font-size: 15px;">Industrial-grade, ruggedized hardware solutions deployed across national governance platforms, financial institutions, and enterprise facilities.</p>
        </div>

        <div class="row g-4">
            <!-- Product 1: Smart Card & Printer -->
            <div class="col-lg-3 col-md-6 col-sm-6 filter-item reveal-on-scroll" data-category="hardware">"""

assert old_prod_sec1 in code, "Could not find old_prod_sec1"
code = code.replace(old_prod_sec1, new_prod_sec1, 1)

# Replace hardware products 2-8
for i, name in [
    (2, "Time Attendance Systems"),
    (3, "Access Control Solutions"),
    (4, "Digital Signage"),
    (5, "Self-Service Kiosk"),
    (6, "Biometric Devices"),
    (7, "CCTV & Surveillance Cameras"),
    (8, "GPS & IoT Tracker")
]:
    old_p = f'<!-- Product {i}: {name} -->\n            <div class="col-lg-3 col-md-6 col-sm-6">'
    new_p = f'<!-- Product {i}: {name} -->\n            <div class="col-lg-3 col-md-6 col-sm-6 filter-item reveal-on-scroll" data-category="hardware">'
    assert old_p in code, f"Could not find product {i}"
    code = code.replace(old_p, new_p, 1)

# Section 2 of products
old_prod_sec2 = """    <!-- SECTION 2: ENTERPRISE SOFTWARE SUITES -->
    <div class="container-fluid py-5" style="background: #f8fafc; border-top: 1px solid #e2e8f0; border-bottom: 1px solid #e2e8f0;">
        <div class="container">
            <div class="text-center mb-5">
                <span class="badge px-3 py-2 rounded-pill fw-semibold mb-2" style="background: rgba(30, 126, 52, 0.1); color: #1e7e34; border: 1px solid rgba(30, 126, 52, 0.25); font-size: 13px;">Software Platforms</span>
                <h2 class="header_two" style="color: #2e3760; font-size: 36px; font-weight: 700;">Enterprise <span style="color: #f26522;">Software Suites</span></h2>
                <p class="text-muted mx-auto" style="max-width: 680px; font-size: 15px;">Battle-tested digital platforms designed for high-concurrency public service delivery, corporate operations, and national identity ecosystems.</p>
            </div>

            <div class="row g-4">
                <!-- Suite 1: Spectrum Enterprise ERP -->
                <div class="col-lg-3 col-md-6 col-sm-6">"""

new_prod_sec2 = """    <!-- SECTION 2: ENTERPRISE SOFTWARE SUITES -->
    <div class="container-fluid py-5 filter-section" style="background: #f8fafc; border-top: 1px solid #e2e8f0; border-bottom: 1px solid #e2e8f0;">
        <div class="container">
            <div class="text-center mb-5">
                <span class="badge px-3 py-2 rounded-pill fw-semibold mb-2" style="background: rgba(30, 126, 52, 0.1); color: #1e7e34; border: 1px solid rgba(30, 126, 52, 0.25); font-size: 13px;">Software Platforms</span>
                <h2 class="header_two" style="color: #2e3760; font-size: 36px; font-weight: 700;">Enterprise <span style="color: #f26522;">Software Suites</span></h2>
                <p class="text-muted mx-auto" style="max-width: 680px; font-size: 15px;">Battle-tested digital platforms designed for high-concurrency public service delivery, corporate operations, and national identity ecosystems.</p>
            </div>

            <div class="row g-4">
                <!-- Suite 1: Spectrum Enterprise ERP -->
                <div class="col-lg-3 col-md-6 col-sm-6 filter-item reveal-on-scroll" data-category="software">"""

assert old_prod_sec2 in code, "Could not find old_prod_sec2"
code = code.replace(old_prod_sec2, new_prod_sec2, 1)

# Replace suites 2-4
for i, name in [
    (2, "Spectrum e-KYC Suite"),
    (3, "Smart City & IoT Platform"),
    (4, "AI Computer Vision Suite")
]:
    old_s = f'<!-- Suite {i}: {name} -->\n                <div class="col-lg-3 col-md-6 col-sm-6">'
    new_s = f'<!-- Suite {i}: {name} -->\n                <div class="col-lg-3 col-md-6 col-sm-6 filter-item reveal-on-scroll" data-category="software">'
    assert old_s in code, f"Could not find suite {i}"
    code = code.replace(old_s, new_s, 1)

# Update internal slugs in products.html
code = code.replace('href="sct.html" class="button">read more</a>', 'href="Smart_Card_Technologies.html" class="button">read more</a>')
code = code.replace('href="dis.html" class="button">read more</a>', 'href="Digital_Identity_&_Security.html" class="button">read more</a>')
code = code.replace('href="ai.html" class="button">read more</a>', 'href="Artificial_Intelligence.html" class="button">read more</a>')

# 14. Add 404 generation right before sitemap
error_404_block = '''
# 10. GENERATE 404.HTML (BRANDED ERROR PAGE)
error_404_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
{get_head(
    title="404 - Page Not Found | Spectrum IT Solutions Ltd.",
    description="The requested page could not be found. Return to Spectrum IT Solutions homepage or explore our enterprise solutions.",
    canonical_slug="404.html",
    og_image="assets/img/banner_img_01.jpg"
)}
</head>
<body>
{COMMON_TOP_BAR}
{get_navbar()}

    <!-- Page Hero Banner -->
    <div class="page-hero-banner">
        <div class="container position-relative text-center">
            <div class="breadcrumb-pill">
                <a href="index.html"><i class="fas fa-home me-1"></i> Home</a>
                <span class="opacity-50">/</span>
                <span style="color: #f26522; font-weight: 600;">404 Error</span>
            </div>
            <h1>404 <span>Not Found</span></h1>
            <p class="hero-desc">
                The resource or endpoint you requested is not available on this sovereign server.
            </p>
        </div>
    </div>

    <!-- 404 Main Section -->
    <div class="container error-page-section">
        <div class="error-code-badge reveal-on-scroll">404</div>
        <h2 class="error-title reveal-on-scroll">Page Not Found</h2>
        <p class="error-desc reveal-on-scroll">
            We couldn't locate the page you're searching for. The URL might have been typed incorrectly, the file moved, or the resource renamed during our system upgrade.
        </p>

        <!-- Quick Navigation Cards -->
        <div class="error-quick-links reveal-on-scroll">
            <h5 class="fw-bold mb-3" style="color: #2e3760;">Popular Destinations</h5>
            <div class="row g-3 justify-content-center text-start">
                <div class="col-md-4 col-sm-6">
                    <a href="index.html" class="d-flex align-items-center p-3 rounded text-decoration-none" style="background: #f8fafc; border: 1px solid #e2e8f0; transition: all 0.2s ease;">
                        <i class="fas fa-home text-warning fa-lg me-3"></i>
                        <div>
                            <div class="fw-bold text-dark" style="font-size: 14px;">Homepage</div>
                            <small class="text-muted" style="font-size: 12px;">Company overview</small>
                        </div>
                    </a>
                </div>
                <div class="col-md-4 col-sm-6">
                    <a href="Artificial_Intelligence.html" class="d-flex align-items-center p-3 rounded text-decoration-none" style="background: #f8fafc; border: 1px solid #e2e8f0; transition: all 0.2s ease;">
                        <i class="fas fa-brain text-success fa-lg me-3"></i>
                        <div>
                            <div class="fw-bold text-dark" style="font-size: 14px;">Artificial Intelligence</div>
                            <small class="text-muted" style="font-size: 12px;">Computer vision &amp; OCR</small>
                        </div>
                    </a>
                </div>
                <div class="col-md-4 col-sm-6">
                    <a href="Digital_Identity_&_Security.html" class="d-flex align-items-center p-3 rounded text-decoration-none" style="background: #f8fafc; border: 1px solid #e2e8f0; transition: all 0.2s ease;">
                        <i class="fas fa-fingerprint text-primary fa-lg me-3"></i>
                        <div>
                            <div class="fw-bold text-dark" style="font-size: 14px;">Digital Identity</div>
                            <small class="text-muted" style="font-size: 12px;">Biometrics &amp; trust</small>
                        </div>
                    </a>
                </div>
                <div class="col-md-4 col-sm-6">
                    <a href="Smart_Card_Technologies.html" class="d-flex align-items-center p-3 rounded text-decoration-none" style="background: #f8fafc; border: 1px solid #e2e8f0; transition: all 0.2s ease;">
                        <i class="fas fa-id-card text-warning fa-lg me-3"></i>
                        <div>
                            <div class="fw-bold text-dark" style="font-size: 14px;">Smart Cards</div>
                            <small class="text-muted" style="font-size: 12px;">Chip encoding &amp; kiosks</small>
                        </div>
                    </a>
                </div>
                <div class="col-md-4 col-sm-6">
                    <a href="services.html" class="d-flex align-items-center p-3 rounded text-decoration-none" style="background: #f8fafc; border: 1px solid #e2e8f0; transition: all 0.2s ease;">
                        <i class="fas fa-cogs text-info fa-lg me-3"></i>
                        <div>
                            <div class="fw-bold text-dark" style="font-size: 14px;">Our Services</div>
                            <small class="text-muted" style="font-size: 12px;">Enterprise engineering</small>
                        </div>
                    </a>
                </div>
                <div class="col-md-4 col-sm-6">
                    <a href="contact.html" class="d-flex align-items-center p-3 rounded text-decoration-none" style="background: #f8fafc; border: 1px solid #e2e8f0; transition: all 0.2s ease;">
                        <i class="fas fa-headset text-danger fa-lg me-3"></i>
                        <div>
                            <div class="fw-bold text-dark" style="font-size: 14px;">Contact Us</div>
                            <small class="text-muted" style="font-size: 12px;">Dhaka headquarters</small>
                        </div>
                    </a>
                </div>
            </div>
        </div>

        <div class="d-flex justify-content-center align-items-center flex-wrap gap-3 reveal-on-scroll">
            <a href="index.html" class="cta-primary-btn">
                <i class="fas fa-home me-2"></i> Return to Homepage
            </a>
            <a href="contact.html" class="cta-secondary-btn">
                <i class="fas fa-paper-plane me-2"></i> Contact Support
            </a>
        </div>
    </div>

{COMMON_FOOTER}
</body>
</html>"""

with open(os.path.join(DIR, '404.html'), 'w', encoding='utf-8') as f:
    f.write(error_404_content)
print("404.html created.")
'''

old_sitemap_marker = "# 10. GENERATE SITEMAP.XML & ROBOTS.TXT & LLMS.TXT (Audit #8, #113)"
new_sitemap_marker = "# 11. GENERATE SITEMAP.XML & ROBOTS.TXT & LLMS.TXT (Audit #8, #113)"
assert old_sitemap_marker in code, "Could not find old_sitemap_marker"
code = code.replace(old_sitemap_marker, error_404_block + "\n" + new_sitemap_marker, 1)

# 15. Add .reveal-on-scroll to key cards across pages
# In contact page: accreditation-card
code = code.replace(
    '<div class="col-lg-3 col-sm-6">\n                        <div class="accreditation-card">',
    '<div class="col-lg-3 col-sm-6">\n                        <div class="accreditation-card reveal-on-scroll">'
)

with open(SITE_SCRIPT, 'w', encoding='utf-8') as f:
    f.write(code)

print("generate_site.py successfully updated with complete SEO, category filters, scroll-reveal, and 404 page!")
