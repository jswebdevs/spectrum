import os

DIR = '/home/newadmin/Projects/Spectrum/plain-html'

PRE_HERO = """    <link rel="preload" as="image" href="assets/img/banner_img_03.webp" type="image/webp" fetchpriority="high">
"""


def get_head(title, description, canonical_slug, og_image="assets/img/banner_img_01.jpg"):
    canonical_url = f"https://spectrum.com.bd/{canonical_slug}"
    # Homepage only: the hero banner is the mobile and desktop LCP image
    hero_preload = PRE_HERO if canonical_slug == "index.html" else ""
    og_image_url = f"https://spectrum.com.bd/{og_image}" if not og_image.startswith("http") else og_image
    return f"""    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{title}</title>
    <meta name="description" content="{description}">
    <meta name="robots" content="index, follow">
    <link rel="canonical" href="{canonical_url}">

    <!-- Open Graph / Facebook -->
    <meta property="og:type" content="website">
    <meta property="og:site_name" content="Spectrum IT Solutions Ltd.">
    <meta property="og:title" content="{title}">
    <meta property="og:description" content="{description}">
    <meta property="og:url" content="{canonical_url}">
    <meta property="og:image" content="{og_image_url}">
    <meta property="og:image:width" content="1200">
    <meta property="og:image:height" content="630">
    <meta property="og:locale" content="en_US">

    <!-- Twitter Cards -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:site" content="@SpectrumITSolutions">
    <meta name="twitter:title" content="{title}">
    <meta name="twitter:description" content="{description}">
    <meta name="twitter:image" content="{og_image_url}">

    <link rel="shortcut icon" type="image/x-icon" href="assets/img/favicon.png">
    <link rel="icon" type="image/png" href="assets/img/favicon.png">
    <link rel="ard" href=".well-known/ard.json">
    <!-- Resource Hints & Preloads -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link rel="preconnect" href="https://cdnjs.cloudflare.com" crossorigin>
{hero_preload}    <!-- Google Fonts & FontAwesome -->
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700&display=swap" media="print" onload="this.media='all'">
    <noscript><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700&display=swap"></noscript>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css" media="print" onload="this.media='all'">
    <noscript><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css"></noscript>
    <!-- Bootstrap & Site Styles -->
    <link rel="stylesheet" href="assets/css/bootstrap.min.css">
    <link rel="stylesheet" href="assets/css/style.min.css">
    <link rel="stylesheet" href="assets/css/responsive-fixes.min.css?v=20261103b">
    <!-- Structured Data (JSON-LD Organization & WebPage) -->
    <script type="application/ld+json">
    [
      {{
        "@context": "https://schema.org",
        "@type": "Organization",
        "name": "Spectrum IT Solutions Ltd.",
        "url": "https://spectrum.com.bd/",
        "logo": "https://spectrum.com.bd/assets/img/logo.png",
        "telephone": "+8801615900004",
        "email": "contact@spectrum.com.bd",
        "address": {{
          "@type": "PostalAddress",
          "streetAddress": "52/1, New Eskaton Road (Hasan Holdings Ltd., 12th Floor)",
          "addressLocality": "Dhaka",
          "postalCode": "1000",
          "addressCountry": "BD"
        }},
        "sameAs": [
          "https://www.facebook.com/myspectrumit",
          "https://www.linkedin.com/company/spectrum-it-solutions-limited",
          "https://www.youtube.com/@SpectrumITSolutionsbdLtd"
        ]
      }},
      {{
        "@context": "https://schema.org",
        "@type": "WebPage",
        "name": "{title}",
        "description": "{description}",
        "url": "{canonical_url}",
        "isPartOf": {{
          "@type": "WebSite",
          "name": "Spectrum IT Solutions Ltd.",
          "url": "https://spectrum.com.bd/"
        }}
      }}
    ]
    </script>"""

COMMON_HEAD = """    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="shortcut icon" type="image/x-icon" href="assets/img/favicon.png">
    <link rel="icon" type="image/png" href="assets/img/favicon.png">
    <link rel="ard" href=".well-known/ard.json">
    <!-- Resource Hints & Preloads -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link rel="preconnect" href="https://cdnjs.cloudflare.com" crossorigin>
    <!-- Google Fonts & FontAwesome -->
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700&display=swap" media="print" onload="this.media='all'">
    <noscript><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700&display=swap"></noscript>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css" media="print" onload="this.media='all'">
    <noscript><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css"></noscript>
    <!-- Bootstrap & Site Styles -->
    <link rel="stylesheet" href="assets/css/bootstrap.min.css">
    <link rel="stylesheet" href="assets/css/style.min.css">
    <link rel="stylesheet" href="assets/css/responsive-fixes.min.css?v=20261103b">
    <!-- Structured Data (JSON-LD) -->
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "Organization",
      "name": "Spectrum IT Solutions Ltd.",
      "url": "https://spectrum.com.bd/",
      "logo": "https://spectrum.com.bd/assets/img/logo.png",
      "telephone": "+8801615900004",
      "email": "contact@spectrum.com.bd",
      "address": {
        "@type": "PostalAddress",
        "streetAddress": "52/1, New Eskaton Road (Hasan Holdings Ltd., 12th Floor)",
        "addressLocality": "Dhaka",
        "postalCode": "1000",
        "addressCountry": "BD"
      },
      "sameAs": [
        "https://www.facebook.com/myspectrumit",
        "https://www.linkedin.com/company/spectrum-it-solutions-limited",
        "https://www.youtube.com/@SpectrumITSolutionsbdLtd"
      ]
    }
    </script>"""

COMMON_TOP_BAR = """    <!-- Start Top bar -->
    <div class="container-fluid bg-dark pt-2 pb-2 top_bar">
        <div class="container text-light d-flex justify-content-between align-items-center">
            <div class="top_social d-flex align-items-center">
                <a class="text-light me-3" href="https://www.facebook.com/myspectrumit" target="_blank" rel="noopener" aria-label="Spectrum Facebook"><i class="fab fa-facebook-f fa-sm fa-fw"></i></a>
                <a class="text-light me-3" href="https://www.linkedin.com/company/spectrum-it-solutions-limited" target="_blank" rel="noopener" aria-label="Spectrum LinkedIn"><i class="fab fa-linkedin fa-sm fa-fw"></i></a>
                <a class="text-light" href="https://www.youtube.com/@SpectrumITSolutionsbdLtd" target="_blank" rel="noopener" aria-label="Spectrum YouTube"><i class="fab fa-youtube fa-sm fa-fw"></i></a>
            </div>
            <div class="top_email d-flex align-items-center">
                <a class="top_email_badge text-decoration-none" href="mailto:contact@spectrum.com.bd">
                    <i class="fa fa-envelope"></i>
                    <span>contact@spectrum.com.bd</span>
                </a>
            </div>
        </div> 
    </div>
    <!-- Close Top bar -->"""

def get_navbar(active_page=''):
    def is_active(p):
        return ' active' if p == active_page else ''

    return f"""    <!-- Header -->
    <nav class="navbar navbar-expand-lg navbar-light shadow sticky-top pt-3 pb-3">
        <div class="container d-flex align-items-center justify-content-between">
            <div class="d-flex align-items-center">
                <div class="logo">
                    <a class="navbar-brand text-success align-self-center m-0 p-0" href="index.html">
                        <img src="assets/img/logo.png" width="165" height="60" alt="Spectrum IT Solutions Logo">
                    </a>
                </div>
                <div class="iso d-none d-lg-flex align-items-center ms-3">
                    <img src="assets/img/ISO_9001.png" width="70" height="75" alt="ISO 9001:2015" class="me-1">
                    <img src="assets/img/ISO_27001.png" width="70" height="75" alt="ISO 27001:2013">
                </div>
            </div>

            <button class="navbar-toggler d-lg-none border-0 ms-auto collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#templatemo_main_nav" aria-controls="templatemo_main_nav" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>

            <div class="collapse navbar-collapse flex-fill d-lg-flex justify-content-lg-between" id="templatemo_main_nav">
                <div class="flex-fill">
                    <ul class="nav navbar-nav d-flex menu_list justify-content-center">
                        <li class="nav-item">
                            <a class="nav-link{is_active('about')}" href="about_us.html">About Us</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link{is_active('services')}" href="services.html">Services</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link{is_active('products')}" href="products.html">Products</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link{is_active('projects')}" href="projects.html">Projects</a>
                        </li>
                        <li class="nav-item dropdown">
                            <a class="nav-link dropdown-toggle{is_active('case-study')}" href="case-study.html" id="caseStudyDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                                Case Study
                            </a>
                            <ul class="dropdown-menu shadow-sm" aria-labelledby="caseStudyDropdown">
                                <li><a class="dropdown-item" href="case-study.html"><i class="fas fa-layer-group me-2 text-warning"></i> All Case Studies</a></li>
                                <li><hr class="dropdown-divider my-1"></li>
                                <li><a class="dropdown-item" target="_blank" rel="noopener" href="https://digital.tcbsheba.com/"><i class="fas fa-id-card me-2 text-success"></i> Digital Transformation of TCB</a></li>
                                <li><a class="dropdown-item" target="_blank" rel="noopener" href="http://www.ecourt.gov.bd/"><i class="fas fa-gavel me-2 text-primary"></i> Industrial e-Court BD</a></li>
                                <li><a class="dropdown-item" target="_blank" rel="noopener" href="https://licence.gov.bd/"><i class="fas fa-file-contract me-2 text-info"></i> National e-Licensing Portal</a></li>
                            </ul>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link{is_active('contact')}" href="contact.html">Contact</a>
                        </li>
                    </ul>
                </div>
                
                <div class="ms-lg-3">
                    <div class="free_con d-flex align-items-center">
                        <i class="fa fa-phone-alt mx-2 text-warning"></i>
                        <div>
                            <span>Free Consultant</span><br>
                            <a href="tel:+8801615900004" style="color: inherit; text-decoration: none;"><strong>+8801615900004</strong></a>
                        </div>
                    </div>
                </div>

                <div class="d-lg-none text-center pt-3 pb-2 border-top mt-3">
                    <img src="assets/img/ISO_9001.png" alt="ISO 9001:2015" class="me-2" style="height: 28px;" loading="lazy">
                    <img src="assets/img/ISO_27001.png" alt="ISO 27001:2013" style="height: 28px;" loading="lazy">
                </div>
            </div>
        </div>
    </nav>"""

COMMON_FOOTER = """    <!-- Footer start -->
    <div class="footer-wrapper">
        <div class="container">
            <div class="row">
                <div class="col-lg-3 col-sm-6 mb-4 footer-col-about">
                    <div class="footer-about">
                        <a href="index.html"><img src="assets/img/logo.png" width="165" height="60" class="img-fluid mb-3" alt="Spectrum IT Solutions Logo" loading="lazy"></a>
                        <p>We are a software development company delivering splendid business IT Solutions and related services to customers home &amp; abroad.</p>
                        <div class="mt-3 footer-social-icons">
                            <a class="text-light" href="https://www.facebook.com/myspectrumit" target="_blank" rel="noopener" aria-label="Spectrum Facebook"><i class="fab fa-facebook-f"></i></a>
                            <a class="text-light" href="https://www.linkedin.com/company/spectrum-it-solutions-limited" target="_blank" rel="noopener" aria-label="Spectrum LinkedIn"><i class="fab fa-linkedin"></i></a>
                            <a class="text-light" href="https://www.youtube.com/@SpectrumITSolutionsbdLtd" target="_blank" rel="noopener" aria-label="Spectrum YouTube"><i class="fab fa-youtube"></i></a>
                        </div>
                    </div>
                    <a href="https://basis.org.bd/company-profile/21-04-024" target="_blank" rel="noopener"><img src="assets/img/basis_logo.png" width="214" height="54" class="img-fluid" style="padding-top: 30px; padding-bottom: 30px;" alt="BASIS Member" loading="lazy"></a>
                </div>

                <div class="col-lg-3 col-sm-6 mb-4">
                    <h3 class="text-white mb-3" style="font-size: 1.25rem;">Valuable Projects</h3>
                    <ul class="list-unstyled">
                        <li class="mb-2"><a href="https://licence.gov.bd/" target="_blank" rel="noopener" class="text-light text-decoration-none"><i class="fas fa-angle-right me-1 text-warning"></i> www.licence.gov.bd</a></li>
                        <li class="mb-2"><a href="https://ocd.org.bd/" target="_blank" rel="noopener" class="text-light text-decoration-none"><i class="fas fa-angle-right me-1 text-warning"></i> www.ocd.org.bd</a></li>
                        <li class="mb-2"><a href="http://www.tcbsheba.com/" target="_blank" rel="noopener" class="text-light text-decoration-none"><i class="fas fa-angle-right me-1 text-warning"></i> www.tcbsheba.com</a></li>
                        <li class="mb-2"><a href="http://www.ecourt.gov.bd/" target="_blank" rel="noopener" class="text-light text-decoration-none"><i class="fas fa-angle-right me-1 text-warning"></i> www.ecourt.gov.bd</a></li>
                        <li class="mb-2"><a href="https://novo.spectrum.com.bd/" target="_blank" rel="noopener" class="text-light text-decoration-none"><i class="fas fa-angle-right me-1 text-warning"></i> www.sobticket.com</a></li>
                    </ul>
                </div>

                <div class="col-lg-3 col-sm-6 mb-4">
                    <h3 class="text-white mb-3" style="font-size: 1.25rem;">Quick Link</h3>
                    <ul class="list-unstyled">
                        <li class="mb-2"><a href="Artificial_Intelligence.html" class="text-light text-decoration-none"><i class="fas fa-angle-right me-1 text-warning"></i> Artificial Intelligence</a></li>
                        <li class="mb-2"><a href="Digital_Identity_&_Security.html" class="text-light text-decoration-none"><i class="fas fa-angle-right me-1 text-warning"></i> Digital Identity &amp; Security</a></li>
                        <li class="mb-2"><a href="Smart_Card_Technologies.html" class="text-light text-decoration-none"><i class="fas fa-angle-right me-1 text-warning"></i> Smart Card Technologies</a></li>
                        <li class="mb-2"><a href="about_us.html" class="text-light text-decoration-none"><i class="fas fa-angle-right me-1 text-warning"></i> About Us</a></li>
                        <li class="mb-2"><a href="services.html" class="text-light text-decoration-none"><i class="fas fa-angle-right me-1 text-warning"></i> Our Services</a></li>
                        <li class="mb-2"><a href="products.html" class="text-light text-decoration-none"><i class="fas fa-angle-right me-1 text-warning"></i> Our Products</a></li>
                        <li class="mb-2"><a href="contact.html" class="text-light text-decoration-none"><i class="fas fa-angle-right me-1 text-warning"></i> Contact Us</a></li>
                    </ul>
                </div>

                <div class="col-lg-3 col-sm-6 mb-4 footer-col-contact">
                    <h3 class="text-white mb-3" style="font-size: 1.25rem;">Contact Us</h3>
                    <p class="text-light mb-2"><i class="fas fa-map-marker-alt me-2 text-warning"></i> 52/1, New Eskaton Road (Hasan Holdings Ltd., 12th Floor), Dhaka-1000, Bangladesh</p>
                    <p class="text-light mb-2"><i class="fas fa-envelope me-2 text-warning"></i> <a href="mailto:contact@spectrum.com.bd" class="text-light text-decoration-none">contact@spectrum.com.bd</a></p>
                    <p class="text-light mb-2"><i class="fas fa-phone-alt me-2 text-warning"></i> <a href="tel:+8801615900004" class="text-light text-decoration-none">+8801615900004</a></p>
                </div>
            </div>

            <!-- Copyright section with same background inside footer-wrapper -->
            <div class="footer-copyright">
                <p class="mb-0">Copyright &copy; 2026 <a href="index.html" style="color: #f26522; text-decoration: none;"><strong>Spectrum IT Solutions Ltd.</strong></a> All Rights Reserved.</p>
            </div>
        </div>
    </div>
    <!-- Footer end -->

    <!-- Scripts -->
    <script src="assets/js/bootstrap.bundle.min.js" defer></script>
    <script src="assets/js/custom.js" defer></script>"""
