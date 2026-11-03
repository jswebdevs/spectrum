import os
import shutil

DIR = '/home/newadmin/Projects/Spectrum/plain-html'

from update_all_pages import get_head, COMMON_HEAD, COMMON_TOP_BAR, get_navbar, COMMON_FOOTER

# 1. GENERATE INDEX.HTML (HOMEPAGE)
index_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
{get_head(
    title="Spectrum IT Solutions: Software Company in Bangladesh",
    description="Spectrum IT Solutions Ltd. is a leading Dhaka-based software company delivering digital identity, biometric infrastructure, smart cards, AI systems, and national enterprise solutions.",
    canonical_slug="index.html",
    og_image="assets/img/banner_img_01.jpg"
)}
</head>
<body>
    <a class="visually-hidden-focusable" href="#main-content">Skip to main content</a>
{COMMON_TOP_BAR}
{get_navbar('home')}

    <main id="main-content">
    <!-- Start Banner / Hero Slider -->
    <div id="template-mo-zay-hero-carousel" class="carousel slide" data-bs-ride="false" data-bs-interval="false">
        <!-- Carousel Indicators -->
        <div class="carousel-indicators">
            <button type="button" data-bs-target="#template-mo-zay-hero-carousel" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1: Digital Identity"></button>
            <button type="button" data-bs-target="#template-mo-zay-hero-carousel" data-bs-slide-to="1" aria-label="Slide 2: Blockchain Technology"></button>
            <button type="button" data-bs-target="#template-mo-zay-hero-carousel" data-bs-slide-to="2" aria-label="Slide 3: Artificial Intelligence"></button>
            <button type="button" data-bs-target="#template-mo-zay-hero-carousel" data-bs-slide-to="3" aria-label="Slide 4: Smart Card Technologies"></button>
            <button type="button" data-bs-target="#template-mo-zay-hero-carousel" data-bs-slide-to="4" aria-label="Slide 5: Software &amp; IT Solutions"></button>
        </div>

        <div class="carousel-inner">
            <!-- Slide 1: Digital Identity (banner_img_03.webp) -->
            <div class="carousel-item active sld-slide sld-slide-1">
                <picture class="hero-bg-picture">
                    <img src="assets/img/banner_img_03.webp" alt="Digital Identity" class="hero-bg-img" loading="lazy" decoding="async">
                </picture>
                <div class="container h-100">
                    <div class="row h-100 align-items-center">
                        <div class="col-lg-6 col-md-7 hero_text">
                            <p class="header_two mb-1">Secure and Seamless Future with</p>
                            <h1 class="header_thr">Digital Identity</h1>
                            <p>Digital Identity enables secure, verified access to services, protecting user data and simplifying online interactions globally.</p>
                            <div class="hero_icons d-flex align-items-center my-3">
                                <span class="hero_icon d-inline-flex align-items-center"><img src="assets/img/icon_leadership.png" width="28" height="42" style="height: 22px; width: auto;" class="me-2" alt="" aria-hidden="true"> LEADERSHIP WORK</span>
                                <span class="hero_icon d-inline-flex align-items-center"><img src="assets/img/icon_qwork.png" width="39" height="38" style="height: 22px; width: auto;" class="me-2" alt="" aria-hidden="true"> QUALITY WORK</span>
                            </div>
                            <div class="hero_buttons d-flex align-items-center mt-4">
                                <a href="Digital_Identity_&_Security.html" class="hero_button" aria-label="Explore Digital Identity and Security solutions">Explore Solution</a>
                                <a href="https://www.youtube.com/@SpectrumITSolutionsbdLtd" target="_blank" rel="noopener" class="hero_watch_button d-inline-flex align-items-center" aria-label="Watch video about Digital Identity on YouTube"><img src="assets/img/icon_video.png" width="38" height="38" class="me-2" alt="" aria-hidden="true"> Watch Video</a>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Slide 2: Blockchain Technology (banner_img_05.webp) -->
            <div class="carousel-item sld-slide sld-slide-2">
                <picture class="hero-bg-picture">
                    <img src="assets/img/banner_img_05.webp" alt="Blockchain Technology" class="hero-bg-img" loading="lazy" decoding="async">
                </picture>
                <div class="container h-100">
                    <div class="row h-100 align-items-center">
                        <div class="col-lg-6 col-md-7 hero_text">
                            <p class="header_two mb-1">Future of Digital Trust Lies in</p>
                            <h1 class="header_thr">Blockchain Technology</h1>
                            <p>Blockchain Technology ensures secure, transparent, and tamper-proof data exchange through decentralized networks.</p>
                            <div class="hero_icons d-flex align-items-center my-3">
                                <span class="hero_icon d-inline-flex align-items-center"><img src="assets/img/icon_leadership.png" width="28" height="42" style="height: 22px; width: auto;" class="me-2" alt="" aria-hidden="true"> LEADERSHIP WORK</span>
                                <span class="hero_icon d-inline-flex align-items-center"><img src="assets/img/icon_qwork.png" width="39" height="38" style="height: 22px; width: auto;" class="me-2" alt="" aria-hidden="true"> QUALITY WORK</span>
                            </div>
                            <div class="hero_buttons d-flex align-items-center mt-4">
                                <a href="services.html" class="hero_button" aria-label="Explore Blockchain Technology implementations">Explore Solution</a>
                                <a href="https://www.youtube.com/@SpectrumITSolutionsbdLtd" target="_blank" rel="noopener" class="hero_watch_button d-inline-flex align-items-center" aria-label="Watch video about Blockchain Technology on YouTube"><img src="assets/img/icon_video.png" width="38" height="38" class="me-2" alt="" aria-hidden="true"> Watch Video</a>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Slide 3: Artificial Intelligence (banner_img_01.webp) -->
            <div class="carousel-item sld-slide sld-slide-3">
                <picture class="hero-bg-picture">
                    <img src="assets/img/banner_img_01.webp" alt="Artificial Intelligence" class="hero-bg-img" loading="lazy" decoding="async">
                </picture>
                <div class="container h-100">
                    <div class="row h-100 align-items-center">
                        <div class="col-lg-6 col-md-7 hero_text">
                            <p class="header_two mb-1">Revolutionizing Your World with</p>
                            <h1 class="header_thr">Artificial Intelligence</h1>
                            <p>Transforming Industries, Enhancing Human Capabilities, Automating Tasks, and Shaping the Future of Technology.</p>
                            <div class="hero_icons d-flex align-items-center my-3">
                                <span class="hero_icon d-inline-flex align-items-center"><img src="assets/img/icon_leadership.png" width="28" height="42" style="height: 22px; width: auto;" class="me-2" alt="" aria-hidden="true"> LEADERSHIP WORK</span>
                                <span class="hero_icon d-inline-flex align-items-center"><img src="assets/img/icon_qwork.png" width="39" height="38" style="height: 22px; width: auto;" class="me-2" alt="" aria-hidden="true"> QUALITY WORK</span>
                            </div>
                            <div class="hero_buttons d-flex align-items-center mt-4">
                                <a href="Artificial_Intelligence.html" class="hero_button" aria-label="Explore Artificial Intelligence services">Explore Solution</a>
                                <a href="https://www.youtube.com/@SpectrumITSolutionsbdLtd" target="_blank" rel="noopener" class="hero_watch_button d-inline-flex align-items-center" aria-label="Watch video about Artificial Intelligence on YouTube"><img src="assets/img/icon_video.png" width="38" height="38" class="me-2" alt="" aria-hidden="true"> Watch Video</a>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Slide 4: Smart Card Technologies (banner_img_04.webp) -->
            <div class="carousel-item sld-slide sld-slide-4">
                <picture class="hero-bg-picture">
                    <img src="assets/img/banner_img_04.webp" alt="Smart Card Technologies" class="hero-bg-img" loading="lazy" decoding="async">
                </picture>
                <div class="container h-100">
                    <div class="row h-100 align-items-center">
                        <div class="col-lg-6 col-md-7 hero_text">
                            <p class="header_two mb-1">Secure Personal Identification with</p>
                            <h1 class="header_thr">Smart Card Technologies</h1>
                            <p>Smart cards store data securely for identification and authentication, powering national citizen registry and ID programs.</p>
                            <div class="hero_icons d-flex align-items-center my-3">
                                <span class="hero_icon d-inline-flex align-items-center"><img src="assets/img/icon_leadership.png" width="28" height="42" style="height: 22px; width: auto;" class="me-2" alt="" aria-hidden="true"> LEADERSHIP WORK</span>
                                <span class="hero_icon d-inline-flex align-items-center"><img src="assets/img/icon_qwork.png" width="39" height="38" style="height: 22px; width: auto;" class="me-2" alt="" aria-hidden="true"> QUALITY WORK</span>
                            </div>
                            <div class="hero_buttons d-flex align-items-center mt-4">
                                <a href="Smart_Card_Technologies.html" class="hero_button" aria-label="Explore Smart Card Technologies">Explore Solution</a>
                                <a href="https://www.youtube.com/@SpectrumITSolutionsbdLtd" target="_blank" rel="noopener" class="hero_watch_button d-inline-flex align-items-center" aria-label="Watch video about Smart Card Technologies on YouTube"><img src="assets/img/icon_video.png" width="38" height="38" class="me-2" alt="" aria-hidden="true"> Watch Video</a>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Slide 5: Software & IT Solutions (banner_img_02.webp) -->
            <div class="carousel-item sld-slide sld-slide-5">
                <picture class="hero-bg-picture">
                    <img src="assets/img/banner_img_02.webp" alt="Software and IT Solutions" class="hero-bg-img" loading="lazy" decoding="async">
                </picture>
                <div class="container h-100">
                    <div class="row h-100 align-items-center">
                        <div class="col-lg-6 col-md-7 hero_text">
                            <p class="header_two mb-1">Leading Software &amp; IT Services</p>
                            <h1 class="header_thr">IT Solutions</h1>
                            <p>We are a software development company delivering splendid business IT Solutions and related services to customers home &amp; abroad.</p>
                            <div class="hero_icons d-flex align-items-center my-3">
                                <span class="hero_icon d-inline-flex align-items-center"><img src="assets/img/icon_leadership.png" width="28" height="42" style="height: 22px; width: auto;" class="me-2" alt="" aria-hidden="true"> LEADERSHIP WORK</span>
                                <span class="hero_icon d-inline-flex align-items-center"><img src="assets/img/icon_qwork.png" width="39" height="38" style="height: 22px; width: auto;" class="me-2" alt="" aria-hidden="true"> QUALITY WORK</span>
                            </div>
                            <div class="hero_buttons d-flex align-items-center mt-4">
                                <a href="services.html" class="hero_button" aria-label="Explore Software and IT Solutions">Explore Solution</a>
                                <a href="https://www.youtube.com/@SpectrumITSolutionsbdLtd" target="_blank" rel="noopener" class="hero_watch_button d-inline-flex align-items-center" aria-label="Watch video about Software and IT Solutions on YouTube"><img src="assets/img/icon_video.png" width="38" height="38" class="me-2" alt="" aria-hidden="true"> Watch Video</a>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <a class="carousel-control-prev text-decoration-none" href="#template-mo-zay-hero-carousel" role="button" data-bs-slide="prev" aria-label="Previous Slide">
            <i class="fas fa-chevron-left" aria-hidden="true"></i>
            <span class="visually-hidden">Previous</span>
        </a>
        <a class="carousel-control-next text-decoration-none" href="#template-mo-zay-hero-carousel" role="button" data-bs-slide="next" aria-label="Next Slide">
            <i class="fas fa-chevron-right" aria-hidden="true"></i>
            <span class="visually-hidden">Next</span>
        </a>
    </div>
    <!-- End Banner / Hero Slider -->

    <!-- About Section -->
    <div class="about py-5">
        <div class="container">
            <div class="row align-items-center">
                <div class="col-lg-6">
                    <div class="about_image text-center">
                        <picture><source srcset="assets/img/about_us_2.webp" type="image/webp"><img src="assets/img/about_us_2.png" width="594" height="563" class="img-fluid" alt="About Spectrum IT Solutions" loading="lazy" decoding="async" style="border-radius: 12px; aspect-ratio: 594/563;"></picture>
                    </div>
                </div>
                <div class="col-lg-6">
                    <div class="about_text">
                        <h2 class="header_two" style="color: #2e3760;">About Spectrum</h2>
                        <h3 class="header_one mb-4" style="color: #c2410c;">Innovating Technology for National Progress</h3>
                        <p class="text-muted" style="line-height: 1.8;">
                            Spectrum IT Solutions Ltd. is a premier Dhaka-based software and IT services company established with a clear mandate to build resilient, sovereign digital solutions. We engineer complex architectures for government ministries, regulatory authorities, and leading enterprises.
                        </p>
                        
                        <!-- Verified Statistics Counter (Audit #327: consistent 12+ years) -->
                        <div class="row pt-3 pb-4">
                            <div class="col-6 col-md-3 mb-3">
                                <div class="counter">
                                    <h3 class="mb-0 fw-bold">12+</h3>
                                    <span>Years Experience</span>
                                </div>
                            </div>
                            <div class="col-6 col-md-3 mb-3">
                                <div class="counter">
                                    <h3 class="mb-0 fw-bold">10M+</h3>
                                    <span>Citizens Served</span>
                                </div>
                            </div>
                            <div class="col-6 col-md-3 mb-3">
                                <div class="counter">
                                    <h3 class="mb-0 fw-bold">50+</h3>
                                    <span>Enterprise Projects</span>
                                </div>
                            </div>
                            <div class="col-6 col-md-3 mb-3">
                                <div class="counter">
                                    <h3 class="mb-0 fw-bold">100%</h3>
                                    <span>Quality Verified</span>
                                </div>
                            </div>
                        </div>

                        <div class="read-more-homepage">
                            <a href="about_us.html" class="button" aria-label="Read more about Spectrum IT Solutions Ltd. and company profile">Read More About Us</a>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- Core Services Overview (Digital Identity is Card #1 at First) -->
    <div class="services py-5">
        <div class="container">
            <div class="text-center mb-5">
                <h2 class="text-white">Our Core Services</h2>
                <p class="text-light">Discover our specialized engineering capabilities across identity, hardware, and sovereign software.</p>
            </div>
            
            <div class="row pt-4">
                <!-- Card 1: Digital Identity & Security (KEPT AT FIRST) -->
                <div class="col-lg-4 col-md-6 mb-4">
                    <div class="services-item p-4 d-flex flex-column justify-content-between h-100" style="border: 2px solid #c2410c; background: #fff;">
                        <div>
                            <img src="assets/img/icon_Digital_Identity_Security.png" width="101" height="101" alt="Digital Identity &amp; Security" class="mb-3">
                            <h3 class="fw-bold" style="font-size: 1.25rem;">Digital Identity &amp; Security</h3>
                            <p class="text-muted">High-security biometric identity management, KYC infrastructure, national family cards, and verification engines.</p>
                        </div>
                        <div class="pt-3 text-center">
                            <a href="Digital_Identity_&_Security.html" class="button" aria-label="Explore Digital Identity and Security solutions">Explore Solutions</a>
                        </div>
                    </div>
                </div>

                <!-- Card 2: Smart Card Technologies -->
                <div class="col-lg-4 col-md-6 mb-4">
                    <div class="services-item p-4 d-flex flex-column justify-content-between h-100" style="background: #fff;">
                        <div>
                            <img src="assets/img/icon_Smart_Card_Technologies.png" width="101" height="101" alt="Smart Card Technologies" class="mb-3">
                            <h3 class="fw-bold" style="font-size: 1.25rem;">Smart Card Technologies</h3>
                            <p class="text-muted">Turnkey contact and contactless chip card issuance, encoding, laser personalization, and reader ecosystems.</p>
                        </div>
                        <div class="pt-3 text-center">
                            <a href="Smart_Card_Technologies.html" class="button" aria-label="Explore Smart Card Technologies">Explore Solutions</a>
                        </div>
                    </div>
                </div>

                <!-- Card 3: Artificial Intelligence -->
                <div class="col-lg-4 col-md-6 mb-4">
                    <div class="services-item p-4 d-flex flex-column justify-content-between h-100" style="background: #fff;">
                        <div>
                            <img src="assets/img/icon_Artificial_Intelligence.png" width="101" height="101" alt="Artificial Intelligence" class="mb-3">
                            <h3 class="fw-bold" style="font-size: 1.25rem;">Artificial Intelligence</h3>
                            <p class="text-muted">Machine learning models, facial recognition, computer vision, and cognitive document automation for enterprise scale.</p>
                        </div>
                        <div class="pt-3 text-center">
                            <a href="Artificial_Intelligence.html" class="button" aria-label="Explore Artificial Intelligence services">Explore Solutions</a>
                        </div>
                    </div>
                </div>

                <!-- Card 4: Biometric Technologies -->
                <div class="col-lg-4 col-md-6 mb-4">
                    <div class="services-item p-4 d-flex flex-column justify-content-between h-100" style="background: #fff;">
                        <div>
                            <img src="assets/img/icon_Biometric_Technologiest.png" width="101" height="101" alt="Biometric Technologies" class="mb-3">
                            <h3 class="fw-bold" style="font-size: 1.25rem;">Biometric Technologies</h3>
                            <p class="text-muted">AFIS/ABIS integration, iris scanning, fingerprint identification, and multi-modal biometric authentication.</p>
                        </div>
                        <div class="pt-3 text-center">
                            <a href="Digital_Identity_&_Security.html" class="button" aria-label="Explore Biometric Technologies">Explore Solutions</a>
                        </div>
                    </div>
                </div>

                <!-- Card 5: Smart Access Control -->
                <div class="col-lg-4 col-md-6 mb-4">
                    <div class="services-item p-4 d-flex flex-column justify-content-between h-100" style="background: #fff;">
                        <div>
                            <img src="assets/img/icon_Smart_Access_Control.png" width="101" height="101" alt="Smart Access Control" class="mb-3">
                            <h3 class="fw-bold" style="font-size: 1.25rem;">Smart Access Control</h3>
                            <p class="text-muted">Turnstiles, flap barriers, RFID gateways, and biometric access management systems for high-security facilities.</p>
                        </div>
                        <div class="pt-3 text-center">
                            <a href="Digital_Identity_&_Security.html" class="button" aria-label="Explore Smart Access Control systems">Explore Solutions</a>
                        </div>
                    </div>
                </div>

                <!-- Card 6: View All Services -->
                <div class="col-lg-4 col-md-6 mb-4">
                    <div class="services-item_all p-4 d-flex flex-column justify-content-center align-items-center text-center h-100">
                        <p class="text-white mb-2" style="padding-top: 0;">Explore All Capabilities</p>
                        <h3 class="text-white fw-bold mb-4" style="font-size: 1.25rem;">12+ Engineering Services</h3>
                        <a href="services.html" class="btn btn-light fw-bold px-4 py-2" style="border-radius: 8px; color: #9a3412;" aria-label="View all 12+ engineering services">View All Services</a>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- Featured Projects & Case Studies (TCB Smart Family Card is Project #1) -->
    <div class="portfolio py-5">
        <div class="container">
            <div class="text-center mb-5">
                <h2>Featured Projects &amp; Case Studies</h2>
                <p>Proven track record of engineering national-scale mission-critical infrastructure.</p>
            </div>
            
            <div class="row pt-4">
                <!-- Project 1: TCB Smart Family Card (FIRST) -->
                <div class="col-lg-3 col-md-6 mb-4 reveal-on-scroll">
                    <div class="portfolio_image bg-white p-3 shadow-sm h-100 d-flex flex-column justify-content-between text-center align-items-center" style="border-radius: 12px; border: 1px solid #dee2e6;">
                        <div class="w-100 text-center">
                            <picture class="mx-auto d-block"><source srcset="assets/img/project_1.webp" type="image/webp"><img src="assets/img/project_1.png" width="600" height="535" alt="TCB Smart Family Card Project" class="img-fluid mb-3 mx-auto d-block" loading="lazy" decoding="async" style="border-radius: 8px; aspect-ratio: 600/535;"></picture>
                            <div class="mb-2"><span class="badge bg-success">Digital Identity</span></div>
                            <h3 class="fw-bold mb-2 text-center" style="font-size: 1.15rem;">TCB Smart Family Card</h3>
                            <p class="text-muted text-center mx-auto" style="font-size: 13px; line-height: 1.6;">Automated beneficiary identification platform managing over 10M citizen family records nationwide.</p>
                        </div>
                        <div class="pt-2 text-center w-100">
                            <a href="case-study.html#tcb" class="button btn-sm d-inline-block" aria-label="View case study on TCB Smart Family Card">View Case Study</a>
                        </div>
                    </div>
                </div>

                <!-- Project 2: Industrial e-Court BD -->
                <div class="col-lg-3 col-md-6 mb-4 reveal-on-scroll">
                    <div class="portfolio_image bg-white p-3 shadow-sm h-100 d-flex flex-column justify-content-between text-center align-items-center" style="border-radius: 12px; border: 1px solid #dee2e6;">
                        <div class="w-100 text-center">
                            <picture class="mx-auto d-block"><source srcset="assets/img/project_2.webp" type="image/webp"><img src="assets/img/project_2.png" width="299" height="256" alt="Industrial e-Court Bangladesh" class="img-fluid mb-3 mx-auto d-block" loading="lazy" decoding="async" style="border-radius: 8px; aspect-ratio: 299/256;"></picture>
                            <div class="mb-2"><span class="badge bg-primary">Enterprise Software</span></div>
                            <h3 class="fw-bold mb-2 text-center" style="font-size: 1.15rem;">Industrial e-Court BD</h3>
                            <p class="text-muted text-center mx-auto" style="font-size: 13px; line-height: 1.6;">Full digital judiciary automation, electronic case filing, cause list management, and summons tracking.</p>
                        </div>
                        <div class="pt-2 text-center w-100">
                            <a href="case-study.html#ecourt" class="button btn-sm d-inline-block" aria-label="View case study on Industrial e-Court Bangladesh">View Case Study</a>
                        </div>
                    </div>
                </div>

                <!-- Project 3: Smart Card Transport -->
                <div class="col-lg-3 col-md-6 mb-4 reveal-on-scroll">
                    <div class="portfolio_image bg-white p-3 shadow-sm h-100 d-flex flex-column justify-content-between text-center align-items-center" style="border-radius: 12px; border: 1px solid #dee2e6;">
                        <div class="w-100 text-center">
                            <picture class="mx-auto d-block"><source srcset="assets/img/project_3.webp" type="image/webp"><img src="assets/img/project_3.png" width="305" height="261" alt="Smart Card Issuance Platform" class="img-fluid mb-3 mx-auto d-block" loading="lazy" decoding="async" style="border-radius: 8px; aspect-ratio: 305/261;"></picture>
                            <div class="mb-2"><span class="badge bg-warning text-dark">Smart Card</span></div>
                            <h3 class="fw-bold mb-2 text-center" style="font-size: 1.15rem;">Smart Card Platform</h3>
                            <p class="text-muted text-center mx-auto" style="font-size: 13px; line-height: 1.6;">Automated laser engraving and dual-interface smart card personalization architecture.</p>
                        </div>
                        <div class="pt-2 text-center w-100">
                            <a href="case-study.html#smartcard" class="button btn-sm d-inline-block" aria-label="View case study on Smart Card Platform">View Case Study</a>
                        </div>
                    </div>
                </div>

                <!-- Project 4: National e-Licensing -->
                <div class="col-lg-3 col-md-6 mb-4 reveal-on-scroll">
                    <div class="portfolio_image bg-white p-3 shadow-sm h-100 d-flex flex-column justify-content-between text-center align-items-center" style="border-radius: 12px; border: 1px solid #dee2e6;">
                        <div class="w-100 text-center">
                            <picture class="mx-auto d-block"><source srcset="assets/img/project_4.webp" type="image/webp"><img src="assets/img/project_4.png" width="309" height="266" alt="National e-Licensing System" class="img-fluid mb-3 mx-auto d-block" loading="lazy" decoding="async" style="border-radius: 8px; aspect-ratio: 309/266;"></picture>
                            <div class="mb-2"><span class="badge bg-info text-dark">Government System</span></div>
                            <h3 class="fw-bold mb-2 text-center" style="font-size: 1.15rem;">National e-Licensing</h3>
                            <p class="text-muted text-center mx-auto" style="font-size: 13px; line-height: 1.6;">Paperless digital regulatory portal with payment gateway and automated certificate generation.</p>
                        </div>
                        <div class="pt-2 text-center w-100">
                            <a href="case-study.html#licence" class="button btn-sm d-inline-block" aria-label="View case study on National e-Licensing Portal">View Case Study</a>
                        </div>
                    </div>
                </div>
            </div>

            <div class="text-center mt-4">
                <a href="projects.html" class="button" aria-label="Explore all sovereign enterprise projects and deployments">Explore All Projects</a>
            </div>
        </div>
    </div>

    <!-- Working Process & Standards -->
    <div class="working py-5">
        <div class="container">
            <div class="row align-items-center">
                <div class="col-lg-6">
                    <div class="working_process">
                        <h2 class="header_two" style="color: #2e3760;">Quality &amp; Standards</h2>
                        <h3 class="header_one mb-4" style="color: #c2410c;">Certified Software Engineering</h3>
                        <p class="text-muted">
                            We adhere to international best practices in software architecture, cybersecurity, and data protection.
                        </p>
                        <div class="steps">
                            <div class="steps_each pb-3">
                                <h3 class="fw-bold" style="font-size: 1.15rem;"><i class="fas fa-check-circle text-success me-2" aria-hidden="true"></i> ISO 9001:2015 Certified</h3>
                                <p class="text-muted">Rigorous quality management systems ensuring consistent delivery and client satisfaction.</p>
                            </div>
                            <div class="steps_each pb-3">
                                <h3 class="fw-bold" style="font-size: 1.15rem;"><i class="fas fa-shield-alt text-success me-2" aria-hidden="true"></i> ISO 27001:2013 Certified</h3>
                                <p class="text-muted">Bank-grade information security management protecting sensitive national data assets.</p>
                            </div>
                            <div class="steps_each pb-3">
                                <h3 class="fw-bold" style="font-size: 1.15rem;"><i class="fas fa-award text-success me-2" aria-hidden="true"></i> BASIS Registered Member</h3>
                                <p class="text-muted">Active member of Bangladesh Association of Software and Information Services (Company ID: 21-04-024).</p>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="col-lg-6 text-center d-none d-lg-block">
                    <picture><source srcset="assets/img/working_process_2.webp" type="image/webp"><img src="assets/img/working_process_2.png" width="533" height="531" alt="Certified Working Process" class="img-fluid" loading="lazy" decoding="async" style="border-radius: 12px; aspect-ratio: 533/531;"></picture>
                </div>
            </div>
        </div>
    </div>

    <!-- Valued Clients & Partners -->
    <div class="client py-5 bg-light">
        <div class="container">
            <div class="text-center mb-5">
                <h2>Our Valued Clients &amp; Partners</h2>
                <p>Trusted by premier government agencies and top corporate institutions across Bangladesh.</p>
            </div>
            <div class="row g-4 text-center justify-content-center align-items-center">
                <div class="col-6 col-md-4">
                    <div class="client_image">
                        <img src="assets/img/vlc_01.jpg" width="192" height="136" alt="Bangladesh Election Commission / Government Partner" class="img-fluid" loading="lazy" decoding="async" style="aspect-ratio: 192/136;">
                    </div>
                </div>
                <div class="col-6 col-md-4">
                    <div class="client_image">
                        <img src="assets/img/vlc_02.jpg" width="192" height="136" alt="TCB Ministry of Commerce Client" class="img-fluid" loading="lazy" decoding="async" style="aspect-ratio: 192/136;">
                    </div>
                </div>
                <div class="col-6 col-md-4">
                    <div class="client_image">
                        <img src="assets/img/vlc_03.jpg" width="192" height="136" alt="Judiciary e-Court Partner" class="img-fluid" loading="lazy" decoding="async" style="aspect-ratio: 192/136;">
                    </div>
                </div>
                <div class="col-6 col-md-4">
                    <div class="client_image">
                        <img src="assets/img/vlc_04.jpg" width="192" height="136" alt="National Governance Partner" class="img-fluid" loading="lazy" decoding="async" style="aspect-ratio: 192/136;">
                    </div>
                </div>
                <div class="col-6 col-md-4">
                    <div class="client_image">
                        <img src="assets/img/vlc_05.jpg" width="192" height="136" alt="Commercial Enterprise Partner" class="img-fluid" loading="lazy" decoding="async" style="aspect-ratio: 192/136;">
                    </div>
                </div>
                <div class="col-6 col-md-4">
                    <div class="client_image">
                        <img src="assets/img/vlc_06.jpg" width="192" height="136" alt="Banking &amp; Financial Partner" class="img-fluid" loading="lazy" decoding="async" style="aspect-ratio: 192/136;">
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- SECTION: CALL TO ACTION -->
    <div class="container-fluid py-5 cta-banner-section">
        <div class="container text-center py-4 position-relative" style="z-index: 2;">
            <span class="badge px-3 py-2 rounded-pill fw-semibold mb-3" style="background: rgba(242, 101, 34, 0.2); color: #c2410c; border: 1px solid rgba(242, 101, 34, 0.4); font-size: 13px;">Sovereign Digital Infrastructure</span>
            <h2 class="display-6 fw-bold text-white mb-3">Ready to Transform Your Digital Infrastructure?</h2>
            <p class="text-light opacity-75 mx-auto mb-4" style="max-width: 650px; font-size: 16px; line-height: 1.7;">
                Spectrum IT Solutions delivers turnkey sovereign identity, smart card architectures, and high-assurance software engineering.
            </p>
            <div class="d-flex justify-content-center align-items-center flex-wrap gap-3 pt-2">
                <a href="contact.html" class="cta-primary-btn" aria-label="Contact Engineering for project consultation">
                    <i class="fas fa-paper-plane me-2" aria-hidden="true"></i> Contact Engineering
                </a>
                <a href="tel:+8801615900004" class="cta-secondary-btn" aria-label="Call Spectrum IT Solutions at +8801615900004">
                    <i class="fas fa-phone-alt me-2 text-warning" aria-hidden="true"></i> +8801615900004
                </a>
            </div>
        </div>
    </div>
    </main>

{COMMON_FOOTER}
</body>
</html>"""

with open(os.path.join(DIR, 'index.html'), 'w', encoding='utf-8') as f:
    f.write(index_content)
print("index.html created successfully.")


# 2. GENERATE SERVICES.HTML
services_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
{get_head(
    title="IT and Software Services in Bangladesh | Spectrum IT Solutions Ltd.",
    description="Explore Spectrum's comprehensive IT services including digital identity, biometric infrastructure, smart cards, AI systems, ERP, cybersecurity, and smart city solutions.",
    canonical_slug="services.html",
    og_image="assets/img/Our_Services_3.jpg"
)}
</head>
<body>
{COMMON_TOP_BAR}
{get_navbar('services')}

    <!-- Page Hero Banner -->
    <div class="page-hero-banner">
        <div class="container position-relative text-center">
            <div class="breadcrumb-pill">
                <a href="index.html"><i class="fas fa-home me-1"></i> Home</a>
                <span class="opacity-50">/</span>
                <span style="color: #f26522; font-weight: 600;">Services</span>
            </div>
            <h1>Our <span>Services</span></h1>
            <p class="hero-desc">
                We support and accompany our clients in a solution-focused manner &mdash; ranging from conceptual design and sovereign identity architectures through to nationwide deployment and 24/7 mission-critical operations.
            </p>
            <div class="hero-features">
                <span class="hero-feature-item">
                    <i class="fas fa-fingerprint" style="color: #f26522;"></i> Digital Identity &amp; Biometrics
                </span>
                <span class="hero-feature-item">
                    <i class="fas fa-id-card" style="color: #4ade80;"></i> Smart Card Technologies
                </span>
                <span class="hero-feature-item">
                    <i class="fas fa-brain" style="color: #38bdf8;"></i> Artificial Intelligence
                </span>
                <span class="hero-feature-item">
                    <i class="fas fa-shield-alt" style="color: #fbbf24;"></i> Sovereign Cyber Security
                </span>
            </div>
        </div>
    </div>

    <!-- Start Services Grid -->
    <div class="container py-5">
        <div class="row">
            <!-- Card 1: Digital Identity & Security (KEPT AT FIRST) -->
            <div class="col-lg-4 col-md-6 mb-4">
                <div class="services-item_pg p-4 h-100 d-flex flex-column justify-content-between shadow-sm bg-white" style="border-radius: 12px; border: 1px solid #dee2e6;">
                    <div>
                        <div class="text-center mb-3">
                            <img src="assets/img/icon_Digital_Identity_Security.png" alt="Digital Identity &amp; Security">
                        </div>
                        <h4 class="fw-bold mb-3" style="color: #f26522;">Digital Identity &amp; Security</h4>
                        <p class="text-muted" style="font-size: 14px; line-height: 1.6;">
                            Comprehensive national identity verification, biometric registry, and family card platforms. Engineered with end-to-end cryptographic safeguards and multi-factor validation.
                        </p>
                    </div>
                    <div class="pt-3 text-center">
                        <a href="Digital_Identity_&_Security.html" class="button">read more</a>
                    </div>
                </div>
            </div>

            <!-- Card 2: Smart Card Technologies -->
            <div class="col-lg-4 col-md-6 mb-4">
                <div class="services-item_pg p-4 h-100 d-flex flex-column justify-content-between shadow-sm bg-white" style="border-radius: 12px; border: 1px solid #dee2e6;">
                    <div>
                        <div class="text-center mb-3">
                            <img src="assets/img/icon_Smart_Card_Technologies.png" alt="Smart Card Technologies">
                        </div>
                        <h4 class="fw-bold mb-3" style="color: #f26522;">Smart Card Technologies</h4>
                        <p class="text-muted" style="font-size: 14px; line-height: 1.6;">
                            Turnkey contact and contactless smart card issuance platforms, secure chip personalization, laser engraving, cryptographic keys, and automated self-service kiosks.
                        </p>
                    </div>
                    <div class="pt-3 text-center">
                        <a href="Smart_Card_Technologies.html" class="button">read more</a>
                    </div>
                </div>
            </div>

            <!-- Card 3: Artificial Intelligence -->
            <div class="col-lg-4 col-md-6 mb-4">
                <div class="services-item_pg p-4 h-100 d-flex flex-column justify-content-between shadow-sm bg-white" style="border-radius: 12px; border: 1px solid #dee2e6;">
                    <div>
                        <div class="text-center mb-3">
                            <img src="assets/img/icon_Artificial_Intelligence.png" alt="Artificial Intelligence">
                        </div>
                        <h4 class="fw-bold mb-3" style="color: #f26522;">Artificial Intelligence</h4>
                        <p class="text-muted" style="font-size: 14px; line-height: 1.6;">
                            Computer vision, facial recognition, automated cognitive document parsing, predictive models, and machine learning architectures custom-trained for sovereign requirements.
                        </p>
                    </div>
                    <div class="pt-3 text-center">
                        <a href="Artificial_Intelligence.html" class="button">read more</a>
                    </div>
                </div>
            </div>

            <!-- Card 4: Biometric Technologies -->
            <div class="col-lg-4 col-md-6 mb-4">
                <div class="services-item_pg p-4 h-100 d-flex flex-column justify-content-between shadow-sm bg-white" style="border-radius: 12px; border: 1px solid #dee2e6;">
                    <div>
                        <div class="text-center mb-3">
                            <img src="assets/img/icon_Biometric_Technologiest.png" alt="Biometric Technologies">
                        </div>
                        <h4 class="fw-bold mb-3" style="color: #f26522;">Biometric Technologies</h4>
                        <p class="text-muted" style="font-size: 14px; line-height: 1.6;">
                            Automated Fingerprint &amp; Iris Identification Systems (AFIS/ABIS), multi-modal biometric sensors, and high-throughput real-time identity deduplication matching engines.
                        </p>
                    </div>
                    <div class="pt-3 text-center">
                        <a href="Digital_Identity_&_Security.html" class="button">read more</a>
                    </div>
                </div>
            </div>

            <!-- Card 5: Smart Access Control -->
            <div class="col-lg-4 col-md-6 mb-4">
                <div class="services-item_pg p-4 h-100 d-flex flex-column justify-content-between shadow-sm bg-white" style="border-radius: 12px; border: 1px solid #dee2e6;">
                    <div>
                        <div class="text-center mb-3">
                            <img src="assets/img/icon_Smart_Access_Control.png" alt="Smart Access Control">
                        </div>
                        <h4 class="fw-bold mb-3" style="color: #f26522;">Smart Access Control</h4>
                        <p class="text-muted" style="font-size: 14px; line-height: 1.6;">
                            High-security entry management integrating optical flap barriers, full-height turnstiles, UHF RFID, and biometric readers for ministries and enterprise headquarters.
                        </p>
                    </div>
                    <div class="pt-3 text-center">
                        <a href="Digital_Identity_&_Security.html" class="button">read more</a>
                    </div>
                </div>
            </div>

            <!-- Card 6: Cyber Security -->
            <div class="col-lg-4 col-md-6 mb-4">
                <div class="services-item_pg p-4 h-100 d-flex flex-column justify-content-between shadow-sm bg-white" style="border-radius: 12px; border: 1px solid #dee2e6;">
                    <div>
                        <div class="text-center mb-3">
                            <img src="assets/img/icon_Cyber_Security.png" alt="Cyber Security">
                        </div>
                        <h4 class="fw-bold mb-3" style="color: #f26522;">Cyber Security</h4>
                        <p class="text-muted" style="font-size: 14px; line-height: 1.6;">
                            Vulnerability assessment, penetration testing, security operations, ISO 27001 advisory, and cryptographic defense protecting mission-critical government networks.
                        </p>
                    </div>
                    <div class="pt-3 text-center">
                        <a href="Digital_Identity_&_Security.html" class="button">read more</a>
                    </div>
                </div>
            </div>

            <!-- Card 7: ERP Solutions -->
            <div class="col-lg-4 col-md-6 mb-4">
                <div class="services-item_pg p-4 h-100 d-flex flex-column justify-content-between shadow-sm bg-white" style="border-radius: 12px; border: 1px solid #dee2e6;">
                    <div>
                        <div class="text-center mb-3">
                            <img src="assets/img/icon_ERP.png" alt="Enterprise Resource Planning">
                        </div>
                        <h4 class="fw-bold mb-3" style="color: #f26522;">ERP Solutions</h4>
                        <p class="text-muted" style="font-size: 14px; line-height: 1.6;">
                            Comprehensive enterprise resource planning covering financials, procurement, human resources, inventory, and cross-departmental digitized operational workflows.
                        </p>
                    </div>
                    <div class="pt-3 text-center">
                        <a href="products.html" class="button">read more</a>
                    </div>
                </div>
            </div>

            <!-- Card 8: Smart City Solutions -->
            <div class="col-lg-4 col-md-6 mb-4">
                <div class="services-item_pg p-4 h-100 d-flex flex-column justify-content-between shadow-sm bg-white" style="border-radius: 12px; border: 1px solid #dee2e6;">
                    <div>
                        <div class="text-center mb-3">
                            <img src="assets/img/icon_Smart_City_Solutions.png" alt="Smart City Solutions">
                        </div>
                        <h4 class="fw-bold mb-3" style="color: #f26522;">Smart City Solutions</h4>
                        <p class="text-muted" style="font-size: 14px; line-height: 1.6;">
                            Intelligent municipal traffic surveillance, sensor networks, centralized control rooms, automated toll collection, and citizen utility integration portals.
                        </p>
                    </div>
                    <div class="pt-3 text-center">
                        <a href="projects.html" class="button">read more</a>
                    </div>
                </div>
            </div>

            <!-- Card 9: Time Attendance -->
            <div class="col-lg-4 col-md-6 mb-4">
                <div class="services-item_pg p-4 h-100 d-flex flex-column justify-content-between shadow-sm bg-white" style="border-radius: 12px; border: 1px solid #dee2e6;">
                    <div>
                        <div class="text-center mb-3">
                            <img src="assets/img/icon_Time_Attendance.png" alt="Time Attendance Systems">
                        </div>
                        <h4 class="fw-bold mb-3" style="color: #f26522;">Time Attendance Systems</h4>
                        <p class="text-muted" style="font-size: 14px; line-height: 1.6;">
                            Cloud-synchronized employee attendance monitoring, roster management, shift tracking, and automated payroll software integration with biometric hardware.
                        </p>
                    </div>
                    <div class="pt-3 text-center">
                        <a href="Smart_Card_Technologies.html" class="button">read more</a>
                    </div>
                </div>
            </div>

            <!-- Card 10: Kiosk Solutions -->
            <div class="col-lg-4 col-md-6 mb-4">
                <div class="services-item_pg p-4 h-100 d-flex flex-column justify-content-between shadow-sm bg-white" style="border-radius: 12px; border: 1px solid #dee2e6;">
                    <div>
                        <div class="text-center mb-3">
                            <img src="assets/img/icon_Kiosk.png" alt="Kiosk Solutions">
                        </div>
                        <h4 class="fw-bold mb-3" style="color: #f26522;">Self-Service Kiosks</h4>
                        <p class="text-muted" style="font-size: 14px; line-height: 1.6;">
                            Rugged interactive kiosks for automated bill payment, digital certificate printing, queue management, and sovereign public service delivery.
                        </p>
                    </div>
                    <div class="pt-3 text-center">
                        <a href="Smart_Card_Technologies.html" class="button">read more</a>
                    </div>
                </div>
            </div>

            <!-- Card 11: Tracking Solutions -->
            <div class="col-lg-4 col-md-6 mb-4">
                <div class="services-item_pg p-4 h-100 d-flex flex-column justify-content-between shadow-sm bg-white" style="border-radius: 12px; border: 1px solid #dee2e6;">
                    <div>
                        <div class="text-center mb-3">
                            <img src="assets/img/icon_Tracking.png" alt="Asset &amp; Vehicle Tracking">
                        </div>
                        <h4 class="fw-bold mb-3" style="color: #f26522;">Tracking Solutions</h4>
                        <p class="text-muted" style="font-size: 14px; line-height: 1.6;">
                            Real-time GPS vehicle tracking, geofencing, fuel monitoring, refrigerated supply chain telematics, and heavy equipment management.
                        </p>
                    </div>
                    <div class="pt-3 text-center">
                        <a href="Smart_Card_Technologies.html" class="button">read more</a>
                    </div>
                </div>
            </div>

            <!-- Card 12: Business Security System -->
            <div class="col-lg-4 col-md-6 mb-4">
                <div class="services-item_pg p-4 h-100 d-flex flex-column justify-content-between shadow-sm bg-white" style="border-radius: 12px; border: 1px solid #dee2e6;">
                    <div>
                        <div class="text-center mb-3">
                            <img src="assets/img/icon_Business_Security_System.png" alt="Business Security System">
                        </div>
                        <h4 class="fw-bold mb-3" style="color: #f26522;">Business Security System</h4>
                        <p class="text-muted" style="font-size: 14px; line-height: 1.6;">
                            Integrated IP video surveillance, CCTV telemetry, alarm automation, server room environmental monitoring, and perimeter defense systems.
                        </p>
                    </div>
                    <div class="pt-3 text-center">
                        <a href="Digital_Identity_&_Security.html" class="button">read more</a>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- SECTION: CALL TO ACTION -->
    <div class="container-fluid py-5 cta-banner-section">
        <div class="container text-center py-4 position-relative" style="z-index: 2;">
            <span class="badge px-3 py-2 rounded-pill fw-semibold mb-3" style="background: rgba(242, 101, 34, 0.2); color: #f26522; border: 1px solid rgba(242, 101, 34, 0.4); font-size: 13px;">Enterprise Consultation</span>
            <h2 class="display-6 fw-bold text-white mb-3">Need Architectural Consultation for Sovereign Systems?</h2>
            <p class="text-light opacity-75 mx-auto mb-4" style="max-width: 650px; font-size: 16px; line-height: 1.7;">
                From digital identity and smart card personalization to AI automation, our senior solutions architects are ready to assist.
            </p>
            <div class="d-flex justify-content-center align-items-center flex-wrap gap-3 pt-2">
                <a href="contact.html" class="cta-primary-btn">
                    <i class="fas fa-paper-plane me-2"></i> Contact Engineering
                </a>
                <a href="tel:+8801615900004" class="cta-secondary-btn">
                    <i class="fas fa-phone-alt me-2 text-warning"></i> +8801615900004
                </a>
            </div>
        </div>
    </div>

{COMMON_FOOTER}
</body>
</html>"""

with open(os.path.join(DIR, 'services.html'), 'w', encoding='utf-8') as f:
    f.write(services_content)
with open(os.path.join(DIR, 'Services.html'), 'w', encoding='utf-8') as f:
    f.write(services_content)
print("services.html & Services.html updated.")


# 3. GENERATE PROJECTS.HTML
projects_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
{get_head(
    title="National &amp; Enterprise Projects | Spectrum IT Solutions Ltd.",
    description="Discover major public and enterprise projects delivered by Spectrum IT Solutions: TCB Smart Family Card (10M+ families), Industrial e-Court BD, National e-Licensing, and smart card platforms.",
    canonical_slug="projects.html",
    og_image="assets/img/project_1.png"
)}
</head>
<body>
{COMMON_TOP_BAR}
{get_navbar('projects')}

    <!-- Page Hero Banner -->
    <div class="page-hero-banner">
        <div class="container position-relative text-center">
            <div class="breadcrumb-pill">
                <a href="index.html"><i class="fas fa-home me-1"></i> Home</a>
                <span class="opacity-50">/</span>
                <span style="color: #f26522; font-weight: 600;">Projects</span>
            </div>
            <h1>Our <span>Projects</span></h1>
            <p class="hero-desc">
                A proven track record of delivering resilient, high-assurance digital platforms, biometric governance systems, and mission-critical public infrastructure for Bangladesh and global clients.
            </p>
            <div class="hero-features">
                <span class="hero-feature-item">
                    <i class="fas fa-id-card" style="color: #4ade80;"></i> 10M+ Citizen Beneficiaries
                </span>
                <span class="hero-feature-item">
                    <i class="fas fa-balance-scale" style="color: #f26522;"></i> Judicial Automation
                </span>
                <span class="hero-feature-item">
                    <i class="fas fa-file-contract" style="color: #38bdf8;"></i> National e-Licensing
                </span>
                <span class="hero-feature-item">
                    <i class="fas fa-ticket-alt" style="color: #fbbf24;"></i> Automated e-Ticketing
                </span>
                <span class="hero-feature-item">
                    <i class="fas fa-shield-alt" style="color: #a78bfa;"></i> Sovereign Security
                </span>
            </div>
        </div>
    </div>

    <!-- SECTION 1: DELIVERED PROJECTS GRID -->
    <div class="container py-5">
        <div class="text-center mb-4 mx-auto" style="max-width: 800px;">
            <span class="badge px-3 py-2 rounded-pill fw-semibold mb-2 d-inline-block text-center" style="background: rgba(242, 101, 34, 0.1); color: #f26522; border: 1px solid rgba(242, 101, 34, 0.25); font-size: 13px;">Proven Deployments</span>
            <h2 class="header_two text-center" style="color: #2e3760; font-size: 36px; font-weight: 700; text-align: center !important;">Delivered Public &amp; <span style="color: #f26522;">Enterprise Systems</span></h2>
            <p class="text-muted mx-auto text-center mb-4" style="max-width: 680px; font-size: 15px; text-align: center !important; line-height: 1.7;">Nationwide digital transformation initiatives delivering tangible socio-economic impact across government ministries and public service departments.</p>

            <!-- Interactive Category Filter Tabs (2-Line Table-Cell Grid on Mobile, Single Line on Desktop) -->
            <div class="filter-nav-wrap filter-nav-grid-2x2">
                <button class="filter-btn active" data-filter="all">
                    <i class="fas fa-layer-group"></i> All <span class="badge-count">6</span>
                </button>
                <button class="filter-btn" data-filter="identity">
                    <i class="fas fa-id-card"></i> Identity &amp; Cards <span class="badge-count">2</span>
                </button>
                <button class="filter-btn" data-filter="governance">
                    <i class="fas fa-balance-scale"></i> Governance <span class="badge-count">2</span>
                </button>
                <button class="filter-btn" data-filter="portal">
                    <i class="fas fa-ticket-alt"></i> E-Ticketing <span class="badge-count">2</span>
                </button>
            </div>
        </div>

        <div class="row g-4">
            <!-- Project 1: TCB Smart Family Card (FLAGSHIP) -->
            <div class="col-lg-4 col-md-6 filter-item reveal-on-scroll" data-category="identity">
                <div class="project-card-modern" style="border: 2px solid #f26522;">
                    <div>
                        <div class="project-icon-wrap">
                            <img src="assets/img/icon_Digital_Identity_Security.png" alt="TCB Smart Family Card">
                        </div>
                        <div class="text-center">
                            <span class="project-badge-pill">Digital Identity &amp; Safety Net</span>
                            <span class="project-client-name"><i class="fas fa-building me-1"></i> Trading Corporation of Bangladesh (TCB)</span>
                        </div>
                        <h4 class="text-center">TCB Smart Family Card</h4>
                        <p class="text-center">Nationwide digital beneficiary platform issuing biometric smart family cards to 10+ million households, eliminating ghost claimants and streamlining subsidized food distribution.</p>
                        <div class="project-tech-tags">
                            <span>Digital Identity</span>
                            <span>Smart Card OS</span>
                            <span>POS Matching</span>
                            <span>Biometric Verification</span>
                        </div>
                    </div>
                    <div class="pt-3 d-flex justify-content-center align-items-center gap-2 flex-wrap">
                        <a href="case-study.html#tcb" class="button">Read Case Study</a>
                        <a href="https://digital.tcbsheba.com/" target="_blank" rel="noopener" class="project-btn-portal"><i class="fas fa-external-link-alt me-1 text-primary"></i> Live Portal</a>
                    </div>
                </div>
            </div>

            <!-- Project 2: Industrial e-Court Bangladesh -->
            <div class="col-lg-4 col-md-6 filter-item reveal-on-scroll" data-category="governance">
                <div class="project-card-modern">
                    <div>
                        <div class="project-icon-wrap">
                            <img src="assets/img/icon_ERP.png" alt="Industrial e-Court System">
                        </div>
                        <div class="text-center">
                            <span class="project-badge-pill">Judicial Automation</span>
                            <span class="project-client-name"><i class="fas fa-building me-1"></i> Judiciary &amp; Ministry of Law</span>
                        </div>
                        <h4 class="text-center">Industrial e-Court BD</h4>
                        <p class="text-center">Pioneering digital judicial workflow platform for Bangladesh Labour Courts, automating case filing, daily cause list publishing, digital summonses, and real-time case tracking.</p>
                        <div class="project-tech-tags">
                            <span>Workflow Automation</span>
                            <span>PKI Security</span>
                            <span>Daily Cause Lists</span>
                            <span>SMS Gateway</span>
                        </div>
                    </div>
                    <div class="pt-3 d-flex justify-content-center align-items-center gap-2 flex-wrap">
                        <a href="case-study.html#ecourt" class="button">Read Case Study</a>
                        <a href="http://www.ecourt.gov.bd/" target="_blank" rel="noopener" class="project-btn-portal"><i class="fas fa-external-link-alt me-1 text-primary"></i> Live Portal</a>
                    </div>
                </div>
            </div>

            <!-- Project 3: Automated Smart Card & License Issuance Platform -->
            <div class="col-lg-4 col-md-6 filter-item reveal-on-scroll" data-category="identity">
                <div class="project-card-modern">
                    <div>
                        <div class="project-icon-wrap">
                            <img src="assets/img/icon_Smart_Card_Technologies.png" alt="Smart Card Issuance">
                        </div>
                        <div class="text-center">
                            <span class="project-badge-pill">Smart Card Architecture</span>
                            <span class="project-client-name"><i class="fas fa-building me-1"></i> National Transport Authorities</span>
                        </div>
                        <h4 class="text-center">Smart Card &amp; License Issuance</h4>
                        <p class="text-center">High-throughput dual-interface ISO 7816/14443 contactless smart card personalization architecture featuring laser engraving, cryptographic verification, and kiosk printing.</p>
                        <div class="project-tech-tags">
                            <span>ISO 7816 / 14443</span>
                            <span>Laser Engraving</span>
                            <span>Cryptographic Keys</span>
                            <span>Handheld Scanners</span>
                        </div>
                    </div>
                    <div class="pt-3 d-flex justify-content-center align-items-center gap-2 flex-wrap">
                        <a href="case-study.html#smartcard" class="button">Read Case Study</a>
                        <a href="sct.html" class="project-btn-portal"><i class="fas fa-microchip me-1 text-warning"></i> Card Tech</a>
                    </div>
                </div>
            </div>

            <!-- Project 4: National e-Licensing Platform -->
            <div class="col-lg-4 col-md-6 filter-item reveal-on-scroll" data-category="governance">
                <div class="project-card-modern">
                    <div>
                        <div class="project-icon-wrap">
                            <img src="assets/img/icon_eSign_Solutions.png" alt="National e-Licensing">
                        </div>
                        <div class="text-center">
                            <span class="project-badge-pill">Regulatory Single-Window</span>
                            <span class="project-client-name"><i class="fas fa-building me-1"></i> Government Regulatory Agencies</span>
                        </div>
                        <h4 class="text-center">National e-Licensing Portal</h4>
                        <p class="text-center">Single-window regulatory portal for license issuance, renewals, digital fee payment processing, and automated verification across multiple state departments.</p>
                        <div class="project-tech-tags">
                            <span>Single-Window</span>
                            <span>Payment Gateways</span>
                            <span>Instant Verification</span>
                            <span>Audit Trail</span>
                        </div>
                    </div>
                    <div class="pt-3 d-flex justify-content-center align-items-center gap-2 flex-wrap">
                        <a href="case-study.html#licence" class="button">Read Case Study</a>
                        <a href="https://licence.gov.bd/" target="_blank" rel="noopener" class="project-btn-portal"><i class="fas fa-external-link-alt me-1 text-primary"></i> Live Portal</a>
                    </div>
                </div>
            </div>

            <!-- Project 5: OCD Online Verification Portal -->
            <div class="col-lg-4 col-md-6 filter-item reveal-on-scroll" data-category="portal">
                <div class="project-card-modern">
                    <div>
                        <div class="project-icon-wrap">
                            <img src="assets/img/icon_Cyber_Security.png" alt="OCD Portal">
                        </div>
                        <div class="text-center">
                            <span class="project-badge-pill">Certificate Security</span>
                            <span class="project-client-name"><i class="fas fa-building me-1"></i> Chief Controller of Imports &amp; Exports</span>
                        </div>
                        <h4 class="text-center">OCD Verification Portal</h4>
                        <p class="text-center">Instant online certificate verification and authentic document management infrastructure with QR verification, PKI digital signatures, and anti-fraud encryption.</p>
                        <div class="project-tech-tags">
                            <span>QR Code Auth</span>
                            <span>PKI Signatures</span>
                            <span>Anti-Tamper Certs</span>
                            <span>Instant Lookup API</span>
                        </div>
                    </div>
                    <div class="pt-3 d-flex justify-content-center align-items-center gap-2 flex-wrap">
                        <a href="case-study.html#ocd" class="button">Read Case Study</a>
                        <a href="https://ocd.org.bd/" target="_blank" rel="noopener" class="project-btn-portal"><i class="fas fa-external-link-alt me-1 text-primary"></i> Live Portal</a>
                    </div>
                </div>
            </div>

            <!-- Project 6: Novo Theatre Automated e-Ticketing -->
            <div class="col-lg-4 col-md-6 filter-item reveal-on-scroll" data-category="portal">
                <div class="project-card-modern">
                    <div>
                        <div class="project-icon-wrap">
                            <img src="assets/img/icon_Smart_Access_Control.png" alt="Novo Theatre Ticketing">
                        </div>
                        <div class="text-center">
                            <span class="project-badge-pill">Smart Access &amp; Ticketing</span>
                            <span class="project-client-name"><i class="fas fa-building me-1"></i> BSM Novo Theatre</span>
                        </div>
                        <h4 class="text-center">Novo Theatre e-Ticketing</h4>
                        <p class="text-center">Turnkey online booking, ticket reservation, and automated turnstile barcode access system for Bangabandhu Sheikh Mujibur Rahman Novo Theatre.</p>
                        <div class="project-tech-tags">
                            <span>Online Reservation</span>
                            <span>Seating Engine</span>
                            <span>Barcode Gates</span>
                            <span>Financial Reconciliation</span>
                        </div>
                    </div>
                    <div class="pt-3 d-flex justify-content-center align-items-center gap-2 flex-wrap">
                        <a href="case-study.html" class="button">Read Details</a>
                        <a href="https://novo.spectrum.com.bd/" target="_blank" rel="noopener" class="project-btn-portal"><i class="fas fa-external-link-alt me-1 text-primary"></i> Live Portal</a>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- SECTION 2: NATIONWIDE IMPACT METRICS -->
    <div class="container-fluid py-5" style="background: #f8fafc; border-top: 1px solid #e2e8f0; border-bottom: 1px solid #e2e8f0;">
        <div class="container text-center">
            <div class="text-center mb-5 mx-auto" style="max-width: 750px;">
                <span class="badge px-3 py-2 rounded-pill fw-semibold mb-2 d-inline-block text-center" style="background: rgba(30, 126, 52, 0.1); color: #1e7e34; border: 1px solid rgba(30, 126, 52, 0.25); font-size: 13px;">Measurable Impact</span>
                <h2 class="header_two text-center" style="color: #2e3760; font-size: 36px; font-weight: 700; text-align: center !important;">National Scale &amp; <span style="color: #f26522;">Operational Milestones</span></h2>
                <p class="text-muted mx-auto text-center mb-0" style="max-width: 680px; font-size: 15px; text-align: center !important; line-height: 1.7;">Transforming government efficiency and citizen services with dependable digital infrastructure.</p>
            </div>

            <div class="row g-4 justify-content-center">
                <div class="col-lg-3 col-sm-6 text-center">
                    <div class="counter-stat-card text-center">
                        <img src="assets/img/icon_1.png" alt="Beneficiaries Verified">
                        <div class="text-center w-100">
                            <h3 class="text-center">10M+</h3>
                            <span class="text-center">Citizens Verified</span>
                        </div>
                    </div>
                </div>
                <div class="col-lg-3 col-sm-6 text-center">
                    <div class="counter-stat-card text-center">
                        <img src="assets/img/icon_2.png" alt="Districts Covered">
                        <div class="text-center w-100">
                            <h3 class="text-center">64</h3>
                            <span class="text-center">Districts Covered</span>
                        </div>
                    </div>
                </div>
                <div class="col-lg-3 col-sm-6 text-center">
                    <div class="counter-stat-card text-center">
                        <img src="assets/img/icon_3.png" alt="Platform Uptime">
                        <div class="text-center w-100">
                            <h3 class="text-center">99.98%</h3>
                            <span class="text-center">System Uptime SLA</span>
                        </div>
                    </div>
                </div>
                <div class="col-lg-3 col-sm-6 text-center">
                    <div class="counter-stat-card text-center">
                        <img src="assets/img/icon_4.png" alt="Zero Counterfeit">
                        <div class="text-center w-100">
                            <h3 class="text-center">100%</h3>
                            <span class="text-center">Sovereign Security</span>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- SECTION 3: CALL TO ACTION -->
    <div class="container-fluid py-5 cta-banner-section">
        <div class="container text-center py-4 position-relative" style="z-index: 2;">
            <span class="badge px-3 py-2 rounded-pill fw-semibold mb-3" style="background: rgba(242, 101, 34, 0.2); color: #f26522; border: 1px solid rgba(242, 101, 34, 0.4); font-size: 13px;">Have a Mission-Critical National Project?</span>
            <h2 class="display-6 fw-bold text-white mb-3">Partner with Bangladesh&rsquo;s Leading Sovereign IT Firm</h2>
            <p class="text-light opacity-75 mx-auto mb-4" style="max-width: 650px; font-size: 16px; line-height: 1.7;">
                Our solutions architects help government agencies and enterprise organizations design, build, and deploy secure software systems with zero downtime.
            </p>
            <div class="d-flex justify-content-center align-items-center flex-wrap gap-3 pt-2">
                <a href="contact.html" class="cta-primary-btn">
                    <i class="fas fa-paper-plane me-2"></i> Contact Engineering
                </a>
                <a href="tel:+8801615900004" class="cta-secondary-btn">
                    <i class="fas fa-phone-alt me-2 text-warning"></i> +8801615900004
                </a>
            </div>
        </div>
    </div>

{COMMON_FOOTER}
</body>
</html>"""

with open(os.path.join(DIR, 'projects.html'), 'w', encoding='utf-8') as f:
    f.write(projects_content)
with open(os.path.join(DIR, 'Projects.html'), 'w', encoding='utf-8') as f:
    f.write(projects_content)
print("projects.html & Projects.html updated.")

# 4. GENERATE CASE-STUDY.HTML
case_study_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
{get_head(
    title="Enterprise Case Studies | National Scale Deployments | Spectrum IT Solutions Ltd.",
    description="Explore real-world case studies of sovereign-scale systems engineered by Spectrum IT Solutions: TCB Smart Family Card (10M+ families), Industrial e-Court BD, National e-Licensing, and smart card platforms.",
    canonical_slug="case-study.html",
    og_image="assets/img/project_1.png"
)}
</head>
<body>
{COMMON_TOP_BAR}
{get_navbar('case-study')}

    <!-- Page Hero Banner -->
    <div class="page-hero-banner">
        <div class="container position-relative text-center">
            <div class="breadcrumb-pill">
                <a href="index.html"><i class="fas fa-home me-1"></i> Home</a>
                <span class="opacity-50">/</span>
                <span style="color: #f26522; font-weight: 600;">Case Studies</span>
            </div>
            <h1>Enterprise <span>Case Studies</span></h1>
            <p class="hero-desc">
                Real-world execution of sovereign-grade software architectures, nationwide biometric identity platforms, and mission-critical public infrastructure for Bangladesh.
            </p>
            <div class="hero-features">
                <span class="hero-feature-item">
                    <i class="fas fa-id-card" style="color: #4ade80;"></i> 10M+ Citizen Safety Net
                </span>
                <span class="hero-feature-item">
                    <i class="fas fa-balance-scale" style="color: #f26522;"></i> Judicial e-Court BD
                </span>
                <span class="hero-feature-item">
                    <i class="fas fa-id-badge" style="color: #38bdf8;"></i> Automated Smart Card CPMS
                </span>
                <span class="hero-feature-item">
                    <i class="fas fa-file-signature" style="color: #fbbf24;"></i> National e-Licensing
                </span>
            </div>
        </div>
    </div>

    <!-- Case Studies Container -->
    <div class="container py-5">
        <div class="text-center mb-5 mx-auto" style="max-width: 750px;">
            <span class="badge px-3 py-2 rounded-pill fw-semibold mb-2 d-inline-block text-center" style="background: rgba(242, 101, 34, 0.1); color: #f26522; border: 1px solid rgba(242, 101, 34, 0.25); font-size: 13px;">Flagship Implementations</span>
            <h2 class="header_two text-center" style="color: #2e3760; font-size: 36px; font-weight: 700; text-align: center !important;">Proven Results Across <span style="color: #f26522;">National Platforms</span></h2>
            <p class="text-muted mx-auto text-center" style="max-width: 680px; font-size: 15px; text-align: center !important; line-height: 1.7;">In-depth analysis of high-impact platforms engineered to solve complex operational, security, and scalability bottlenecks.</p>
        </div>

        <!-- Case Study 1: TCB Smart Family Card -->
        <div id="tcb" class="case-study-card-modern">
            <div class="row g-0 align-items-center">
                <div class="col-lg-5">
                    <div class="case-study-img-wrap">
                        <img src="assets/img/project_1.png" alt="TCB Smart Family Card Case Study" class="img-fluid">
                        <div class="text-center mt-3">
                            <span class="badge rounded-pill px-3 py-1 text-white fw-semibold" style="background: #1e7e34; font-size: 12px;"><i class="fas fa-check-circle me-1"></i> 10M+ Households Enrolled</span>
                        </div>
                    </div>
                </div>
                <div class="col-lg-7">
                    <div class="case-study-body">
                        <span class="case-study-badge">Digital Identity &amp; Social Safety Net</span>
                        <h3 class="case-study-title">TCB Smart Family Card Platform</h3>
                        <div class="case-study-client">
                            <i class="fas fa-building text-warning"></i>
                            <span><strong>Client:</strong> Trading Corporation of Bangladesh (Ministry of Commerce)</span>
                        </div>
                        
                        <div class="case-study-section-title"><i class="fas fa-exclamation-circle text-danger"></i> The Challenge</div>
                        <p class="case-study-text">
                            Distributing essential subsidized commodities to over 10 million vulnerable families across all 64 districts suffered from manual coupon counterfeiting, duplicate records, and lack of real-time distribution tracking.
                        </p>

                        <div class="case-study-section-title"><i class="fas fa-cogs text-primary"></i> The Spectrum Architecture</div>
                        <p class="case-study-text">
                            Engineered a cloud-native biometric beneficiary management system with National ID (NID) deduplication. The system pairs encrypted QR smart family cards with offline/online point-of-sale Android validation apps deployed across 10,000+ licensed dealers.
                        </p>

                        <div class="case-study-section-title"><i class="fas fa-chart-line text-success"></i> Measurable Impact</div>
                        <ul class="case-study-impact-list">
                            <li><i class="fas fa-check-circle"></i> 10,000,000+ verified beneficiary families enrolled into a deduplicated sovereign database.</li>
                            <li><i class="fas fa-check-circle"></i> Over 57 million citizens benefit directly from transparent, tamper-proof food subsidy distribution.</li>
                            <li><i class="fas fa-check-circle"></i> 99.8% elimination of duplicate claims through real-time inventory reconciliation.</li>
                        </ul>

                        <div class="case-study-tech-pills">
                            <span>NID Biometric Deduplication</span>
                            <span>Encrypted QR Card OS</span>
                            <span>POS Terminal Verification</span>
                            <span>High-Concurrency Cloud</span>
                        </div>

                        <div class="pt-3 text-center d-flex justify-content-center align-items-center gap-3 flex-wrap">
                            <a href="https://digital.tcbsheba.com/" target="_blank" rel="noopener" class="button">Visit Live System</a>
                            <a href="contact.html" class="project-btn-portal"><i class="fas fa-paper-plane me-1 text-warning"></i> Inquire About Architecture</a>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Case Study 2: Industrial e-Court Bangladesh -->
        <div id="ecourt" class="case-study-card-modern">
            <div class="row g-0 align-items-center">
                <div class="col-lg-5">
                    <div class="case-study-img-wrap">
                        <img src="assets/img/project_2.png" alt="Industrial e-Court Bangladesh" class="img-fluid">
                        <div class="text-center mt-3">
                            <span class="badge rounded-pill px-3 py-1 text-white fw-semibold" style="background: #2e3760; font-size: 12px;"><i class="fas fa-gavel me-1"></i> Paperless Judicial Workflow</span>
                        </div>
                    </div>
                </div>
                <div class="col-lg-7">
                    <div class="case-study-body">
                        <span class="case-study-badge" style="color: #2e3760; background: rgba(46, 55, 96, 0.08); border-color: rgba(46, 55, 96, 0.2);">Judiciary &amp; Legal Workflow Automation</span>
                        <h3 class="case-study-title">Industrial e-Court Bangladesh</h3>
                        <div class="case-study-client">
                            <i class="fas fa-building text-warning"></i>
                            <span><strong>Client:</strong> Ministry of Labour &amp; Employment / Labour Courts of Bangladesh</span>
                        </div>

                        <div class="case-study-section-title"><i class="fas fa-exclamation-circle text-danger"></i> The Challenge</div>
                        <p class="case-study-text">
                            Subordinate labour courts were overwhelmed by physical paper dockets, manual case scheduling, delayed physical summons delivery, and the inability of factory workers to track hearing dates remotely.
                        </p>

                        <div class="case-study-section-title"><i class="fas fa-cogs text-primary"></i> The Spectrum Architecture</div>
                        <p class="case-study-text">
                            Developed a sovereign e-Judiciary case management platform that digitizes electronic case filing, automated daily cause-list publishing, digital judge's bench access, tamper-evident case logs, and SMS alert notification gateways.
                        </p>

                        <div class="case-study-section-title"><i class="fas fa-chart-line text-success"></i> Measurable Impact</div>
                        <ul class="case-study-impact-list">
                            <li><i class="fas fa-check-circle"></i> 85% reduction in case scheduling delays with instant online cause list publication.</li>
                            <li><i class="fas fa-check-circle"></i> Complete paperless case tracking for litigants and attorneys across all Labour Court benches.</li>
                            <li><i class="fas fa-check-circle"></i> Digital transmission of bail orders and hearing notices with cryptographic audit trails.</li>
                        </ul>

                        <div class="case-study-tech-pills">
                            <span>Judicial Workflow Engine</span>
                            <span>PKI Security</span>
                            <span>Automated Cause Lists</span>
                            <span>Litigant SMS Gateway</span>
                        </div>

                        <div class="pt-3 text-center d-flex justify-content-center align-items-center gap-3 flex-wrap">
                            <a href="http://www.ecourt.gov.bd/" target="_blank" rel="noopener" class="button">Visit e-Court Portal</a>
                            <a href="contact.html" class="project-btn-portal"><i class="fas fa-paper-plane me-1 text-warning"></i> Inquire About Architecture</a>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Case Study 3: Automated Smart Card Issuance Platform -->
        <div id="smartcard" class="case-study-card-modern">
            <div class="row g-0 align-items-center">
                <div class="col-lg-5">
                    <div class="case-study-img-wrap">
                        <img src="assets/img/project_3.png" alt="Smart Card Issuance Architecture" class="img-fluid">
                        <div class="text-center mt-3">
                            <span class="badge rounded-pill px-3 py-1 text-dark fw-semibold" style="background: #ffc107; font-size: 12px;"><i class="fas fa-microchip me-1"></i> ISO 7816 / 14443 Type A/B</span>
                        </div>
                    </div>
                </div>
                <div class="col-lg-7">
                    <div class="case-study-body">
                        <span class="case-study-badge" style="color: #b45309; background: rgba(245, 158, 11, 0.1); border-color: rgba(245, 158, 11, 0.25);">High-Security Hardware &amp; Personalization</span>
                        <h3 class="case-study-title">Automated Smart Card Issuance Platform</h3>
                        <div class="case-study-client">
                            <i class="fas fa-building text-warning"></i>
                            <span><strong>Client:</strong> National Transport &amp; Licensing Authorities</span>
                        </div>

                        <div class="case-study-section-title"><i class="fas fa-exclamation-circle text-danger"></i> The Challenge</div>
                        <p class="case-study-text">
                            High volume issuance of counterfeit-proof driving licenses and transit smart cards required stringent personalization throughput, cryptographic key injection, and tamper-resistant security features.
                        </p>

                        <div class="case-study-section-title"><i class="fas fa-cogs text-primary"></i> The Spectrum Architecture</div>
                        <p class="case-study-text">
                            Architected a centralized Smart Card Personalization Management System (CPMS) integrated with automated laser engraving machines, dual-interface chip programmers, and hardware security modules (HSM) for biometric match-on-card.
                        </p>

                        <div class="case-study-section-title"><i class="fas fa-chart-line text-success"></i> Measurable Impact</div>
                        <ul class="case-study-impact-list">
                            <li><i class="fas fa-check-circle"></i> High-speed card personalization throughput exceeding 15,000 smart cards per day.</li>
                            <li><i class="fas fa-check-circle"></i> Zero counterfeit incidents on issued cryptographic contactless smart cards.</li>
                            <li><i class="fas fa-check-circle"></i> Instant offline authentication by law enforcement using ruggedized handheld scanners.</li>
                        </ul>

                        <div class="case-study-tech-pills">
                            <span>Laser Engraving</span>
                            <span>HSM Key Management</span>
                            <span>Biometric Match-on-Card</span>
                            <span>Handheld Field Validation</span>
                        </div>

                        <div class="pt-3 text-center d-flex justify-content-center align-items-center gap-3 flex-wrap">
                            <a href="Smart_Card_Technologies.html" class="button">Explore Smart Card Tech</a>
                            <a href="contact.html" class="project-btn-portal"><i class="fas fa-paper-plane me-1 text-warning"></i> Inquire About Architecture</a>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Case Study 4: National e-Licensing Platform -->
        <div id="licence" class="case-study-card-modern">
            <div class="row g-0 align-items-center">
                <div class="col-lg-5">
                    <div class="case-study-img-wrap">
                        <img src="assets/img/project_4.png" alt="National e-Licensing" class="img-fluid">
                        <div class="text-center mt-3">
                            <span class="badge rounded-pill px-3 py-1 text-white fw-semibold" style="background: #0284c7; font-size: 12px;"><i class="fas fa-stamp me-1"></i> Single-Window Regulatory Portal</span>
                        </div>
                    </div>
                </div>
                <div class="col-lg-7">
                    <div class="case-study-body">
                        <span class="case-study-badge" style="color: #0369a1; background: rgba(2, 132, 199, 0.1); border-color: rgba(2, 132, 199, 0.25);">Government Regulatory Infrastructure</span>
                        <h3 class="case-study-title">National e-Licensing Platform</h3>
                        <div class="case-study-client">
                            <i class="fas fa-building text-warning"></i>
                            <span><strong>Client:</strong> State Regulatory Authorities &amp; Ministries</span>
                        </div>

                        <div class="case-study-section-title"><i class="fas fa-exclamation-circle text-danger"></i> The Challenge</div>
                        <p class="case-study-text">
                            Eliminating multi-week bureaucratic bottlenecks, manual paper submissions, in-person document scrutiny, and opaque payment tracking for nationwide commercial licenses and import-export permits.
                        </p>

                        <div class="case-study-section-title"><i class="fas fa-cogs text-primary"></i> The Spectrum Architecture</div>
                        <p class="case-study-text">
                            Delivered an integrated single-window web portal supporting electronic document uploads, rule-based automated scrutiny routing, electronic approval signatures, payment gateway integrations, and digitally signed QR-verifiable certificates.
                        </p>

                        <div class="case-study-section-title"><i class="fas fa-chart-line text-success"></i> Measurable Impact</div>
                        <ul class="case-study-impact-list">
                            <li><i class="fas fa-check-circle"></i> License application turnaround time dropped from 21 days to under 48 hours.</li>
                            <li><i class="fas fa-check-circle"></i> Over 100,000 commercial licenses issued with instant QR verification.</li>
                            <li><i class="fas fa-check-circle"></i> Seamless electronic revenue collection directly integrated with Bangladesh Bank e-challan.</li>
                        </ul>

                        <div class="case-study-tech-pills">
                            <span>Single-Window e-Gov</span>
                            <span>Digital Signature PKI</span>
                            <span>e-Challan Integration</span>
                            <span>Instant QR Authentication</span>
                        </div>

                        <div class="pt-3 text-center d-flex justify-content-center align-items-center gap-3 flex-wrap">
                            <a href="https://licence.gov.bd/" target="_blank" rel="noopener" class="button">Visit e-Licensing Portal</a>
                            <a href="contact.html" class="project-btn-portal"><i class="fas fa-paper-plane me-1 text-warning"></i> Inquire About Architecture</a>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- SECTION 2: ENGINEERING PRINCIPLES -->
    <div class="container-fluid py-5" style="background: #f8fafc; border-top: 1px solid #e2e8f0; border-bottom: 1px solid #e2e8f0;">
        <div class="container text-center">
            <div class="text-center mb-5 mx-auto" style="max-width: 750px;">
                <span class="badge px-3 py-2 rounded-pill fw-semibold mb-2 d-inline-block text-center" style="background: rgba(30, 126, 52, 0.1); color: #1e7e34; border: 1px solid rgba(30, 126, 52, 0.25); font-size: 13px;">Architecture Standards</span>
                <h2 class="header_two text-center" style="color: #2e3760; font-size: 36px; font-weight: 700; text-align: center !important;">How Spectrum Builds for <span style="color: #f26522;">National Scale</span></h2>
                <p class="text-muted mx-auto text-center mb-0" style="max-width: 680px; font-size: 15px; text-align: center !important; line-height: 1.7;">Four core technical pillars underpinning our delivered sovereign solutions.</p>
            </div>

            <div class="row g-4 justify-content-center">
                <div class="col-lg-3 col-sm-6 text-center">
                    <div class="counter-stat-card text-center">
                        <img src="assets/img/icon_ERP.png" alt="High Concurrency">
                        <div class="text-center w-100">
                            <h3 class="text-center" style="font-size: 22px;">High Concurrency</h3>
                            <span class="text-center">Elastic microservices tested for 50,000+ requests/sec</span>
                        </div>
                    </div>
                </div>
                <div class="col-lg-3 col-sm-6 text-center">
                    <div class="counter-stat-card text-center">
                        <img src="assets/img/icon_Digital_Identity_Security.png" alt="Biometrics">
                        <div class="text-center w-100">
                            <h3 class="text-center" style="font-size: 22px;">Multi-Biometrics</h3>
                            <span class="text-center">NID, fingerprint, face &amp; iris deduplication</span>
                        </div>
                    </div>
                </div>
                <div class="col-lg-3 col-sm-6 text-center">
                    <div class="counter-stat-card text-center">
                        <img src="assets/img/icon_Cyber_Security.png" alt="PKI Cryptography">
                        <div class="text-center w-100">
                            <h3 class="text-center" style="font-size: 22px;">PKI Cryptography</h3>
                            <span class="text-center">HSM key management &amp; anti-tamper verification</span>
                        </div>
                    </div>
                </div>
                <div class="col-lg-3 col-sm-6 text-center">
                    <div class="counter-stat-card text-center">
                        <img src="assets/img/icon_Business_Security_System.png" alt="SLA Maintenance">
                        <div class="text-center w-100">
                            <h3 class="text-center" style="font-size: 22px;">24/7 SLA Support</h3>
                            <span class="text-center">Nationwide field support across all 64 districts</span>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- SECTION 3: CALL TO ACTION -->
    <div class="container-fluid py-5 cta-banner-section">
        <div class="container text-center py-4 position-relative" style="z-index: 2;">
            <span class="badge px-3 py-2 rounded-pill fw-semibold mb-3" style="background: rgba(242, 101, 34, 0.2); color: #f26522; border: 1px solid rgba(242, 101, 34, 0.4); font-size: 13px;">Deploying National or Enterprise Systems?</span>
            <h2 class="display-6 fw-bold text-white mb-3">Speak Directly With Our Solutions Architects</h2>
            <p class="text-light opacity-75 mx-auto mb-4" style="max-width: 650px; font-size: 16px; line-height: 1.7;">
                From requirements gathering and sovereign data architecture to pilot deployment and nationwide rollout, Spectrum delivers on time and within budget.
            </p>
            <div class="d-flex justify-content-center align-items-center flex-wrap gap-3 pt-2">
                <a href="contact.html" class="cta-primary-btn">
                    <i class="fas fa-paper-plane me-2"></i> Contact Engineering
                </a>
                <a href="tel:+8801615900004" class="cta-secondary-btn">
                    <i class="fas fa-phone-alt me-2 text-warning"></i> +8801615900004
                </a>
            </div>
        </div>
    </div>

{COMMON_FOOTER}
</body>
</html>"""

with open(os.path.join(DIR, 'case-study.html'), 'w', encoding='utf-8') as f:
    f.write(case_study_content)
with open(os.path.join(DIR, 'Case-study.html'), 'w', encoding='utf-8') as f:
    f.write(case_study_content)
print("case-study.html & Case-study.html updated.")

# 5. GENERATE DIGITAL IDENTITY & SECURITY PAGE (FULL SLUG & PADDED CTA)
dis_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
{get_head(
    title="Digital Identity & Security Solutions | Automated ID Verification | Spectrum",
    description="Spectrum's automated ID verification reads Bangla and English NID cards, spots forged IDs, confirms a live person and matches face or fingerprint in seconds. Data stays in Bangladesh.",
    canonical_slug="Digital_Identity_&_Security.html",
    og_image="assets/img/digital-identity/hero-biometric-verify.jpg"
)}
</head>
<body>
{COMMON_TOP_BAR}
{get_navbar('services')}

    <!-- Page Hero Banner -->
    <div class="page-hero-banner">
        <div class="container position-relative text-center">
            <div class="breadcrumb-pill">
                <a href="index.html"><i class="fas fa-home me-1"></i> Home</a>
                <span class="opacity-50">/</span>
                <a href="services.html">Services</a>
                <span class="opacity-50">/</span>
                <span style="color: #f26522; font-weight: 600;">Digital Identity &amp; Security</span>
            </div>
            <h1>Verify a Person in <span>Seconds</span>, Not Minutes</h1>
            <p class="hero-desc">
                Our automated ID verification solution reads a national ID card, checks that it is genuine, and confirms the person holding it is real and matches the card. It all happens in a few seconds, and the data stays in Bangladesh.
            </p>
            <div class="hero-features">
                <span class="hero-feature-item">
                    <i class="fas fa-users" style="color: #4ade80;"></i> 10M+ TCB Family Cards
                </span>
                <span class="hero-feature-item">
                    <i class="fas fa-language" style="color: #fbbf24;"></i> Reads Bangla &amp; English
                </span>
                <span class="hero-feature-item">
                    <i class="fas fa-fingerprint" style="color: #f26522;"></i> Face &amp; Fingerprint Matching
                </span>
                <span class="hero-feature-item">
                    <i class="fas fa-shield-alt" style="color: #38bdf8;"></i> Data Stays in Bangladesh
                </span>
            </div>
        </div>
    </div>

    <!-- INTRO: WHAT THE SOLUTION DOES -->
    <div class="container py-5">
        <div class="row align-items-center g-5 mb-5">
            <div class="col-lg-6">
                <div class="d-inline-flex align-items-center px-3 py-1 rounded-pill mb-3" style="background: rgba(2, 132, 199, 0.1); border: 1px solid rgba(2, 132, 199, 0.25); color: #0284c7; font-size: 13px; font-weight: 700;">
                    <i class="fas fa-shield-virus me-2"></i> AUTOMATED ID VERIFICATION
                </div>
                <h2 class="display-6 fw-bold mb-3" style="color: #2e3760; line-height: 1.25;">
                    Know Exactly Who You Are Dealing With
                </h2>
                <p class="text-muted" style="line-height: 1.8; font-size: 16px;">
                    Manual ID checks are slow, and photocopies are easy to fake. Our solution replaces them with one automated check that runs on a phone, a tablet or a POS terminal at the counter.
                </p>
                <p class="text-muted" style="line-height: 1.8; font-size: 15px;">
                    Banks, telecom operators and government programmes use it to open accounts, register SIM cards and deliver benefits. It stops fake cards, borrowed IDs and photo tricks before they reach your system.
                </p>

                <!-- Key Metrics Grid -->
                <div class="row g-3 pt-2 mb-4">
                    <div class="col-6 col-sm-3">
                        <div class="dis-stat-card">
                            <div class="dis-stat-num text-primary">10M+</div>
                            <small class="text-muted fw-semibold">Families Enrolled</small>
                        </div>
                    </div>
                    <div class="col-6 col-sm-3">
                        <div class="dis-stat-card">
                            <div class="dis-stat-num text-success">0.1s</div>
                            <small class="text-muted fw-semibold">To Read a Card</small>
                        </div>
                    </div>
                    <div class="col-6 col-sm-3">
                        <div class="dis-stat-card">
                            <div class="dis-stat-num" style="color: #f26522;">&lt;2s</div>
                            <small class="text-muted fw-semibold">Full Check</small>
                        </div>
                    </div>
                    <div class="col-6 col-sm-3">
                        <div class="dis-stat-card">
                            <div class="dis-stat-num text-info">100%</div>
                            <small class="text-muted fw-semibold">Stored Locally</small>
                        </div>
                    </div>
                </div>

                <!-- Call to action buttons -->
                <div class="d-flex flex-wrap gap-3">
                    <a href="contact.html" class="btn btn-primary px-4 py-2 fw-semibold rounded-pill shadow-sm" style="background: #2e3760; border-color: #2e3760;">
                        <i class="fas fa-calendar-check me-2"></i> Book a Demo
                    </a>
                    <a href="#how-it-works" class="btn btn-outline-secondary px-4 py-2 fw-semibold rounded-pill">
                        <i class="fas fa-list-ol me-2"></i> See How It Works
                    </a>
                </div>
            </div>

            <!-- Hero Visual Showcase -->
            <div class="col-lg-6">
                <div class="dis-hero-card position-relative">
                    <picture>
                        <source srcset="assets/img/digital-identity/hero-biometric-verify.webp" type="image/webp">
                        <img src="assets/img/digital-identity/hero-biometric-verify.jpg" alt="Customer in a Dhaka bank branch verifies her face on a phone, with a SPECIMEN national ID card on the desk" class="img-fluid w-100" style="object-fit: cover; max-height: 440px;" loading="eager">
                    </picture>
                    <div class="dis-hud-badge">
                        <div class="d-flex align-items-center">
                            <i class="fas fa-check-circle text-success me-2 fa-lg"></i>
                            <div>
                                <div class="fw-bold text-white" style="font-size: 13px;">Face Verified</div>
                                <div class="text-white-50" style="font-size: 11px;">Live person &bull; Matches ID card</div>
                            </div>
                        </div>
                        <span class="badge bg-success px-2 py-1 rounded-pill" style="font-size: 11px;">99.8% Match</span>
                    </div>
                </div>
            </div>
        </div>

        <!-- SECTION: WHAT IT SOLVES -->
        <div class="py-4 my-3 border-top border-bottom">
            <div class="text-center mb-5">
                <span class="badge bg-light text-dark px-3 py-2 rounded-pill fw-bold border text-uppercase" style="letter-spacing: 0.5px;">What It Solves</span>
                <h3 class="fw-bold mt-2" style="color: #2e3760;">Three Questions, Answered Every Time</h3>
                <p class="text-muted mx-auto" style="max-width: 650px;">
                    Most identity fraud comes down to three questions. Our solution answers all three in a single check.
                </p>
            </div>

            <div class="row g-4">
                <div class="col-md-4">
                    <div class="dis-feature-box">
                        <div class="d-inline-flex align-items-center justify-content-center rounded-3 mb-3 p-3" style="background: rgba(2, 132, 199, 0.1); color: #0284c7;">
                            <i class="fas fa-user-shield fa-2x"></i>
                        </div>
                        <h5 class="fw-bold" style="color: #2e3760;">Is This a Real Person?</h5>
                        <p class="text-muted small mb-0" style="line-height: 1.7;">
                            Stops fake profiles, stolen identities and people pretending to be someone else, before any account is opened or payment is made.
                        </p>
                    </div>
                </div>

                <div class="col-md-4">
                    <div class="dis-feature-box">
                        <div class="d-inline-flex align-items-center justify-content-center rounded-3 mb-3 p-3" style="background: rgba(16, 185, 129, 0.1); color: #10b981;">
                            <i class="fas fa-id-card-alt fa-2x"></i>
                        </div>
                        <h5 class="fw-bold" style="color: #2e3760;">Is the ID Genuine?</h5>
                        <p class="text-muted small mb-0" style="line-height: 1.7;">
                            Reads and checks the Smart NID, older NID cards, e-Passports and driving licences automatically. No staff member has to type anything.
                        </p>
                    </div>
                </div>

                <div class="col-md-4">
                    <div class="dis-feature-box">
                        <div class="d-inline-flex align-items-center justify-content-center rounded-3 mb-3 p-3" style="background: rgba(242, 101, 34, 0.1); color: #f26522;">
                            <i class="fas fa-microscope fa-2x"></i>
                        </div>
                        <h5 class="fw-bold" style="color: #2e3760;">Has the Card Been Changed?</h5>
                        <p class="text-muted small mb-0" style="line-height: 1.7;">
                            Spots swapped photos, edited text, copied holograms and colour printouts made to look like real cards.
                        </p>
                    </div>
                </div>
            </div>
        </div>

        <!-- SECTION: HOW IT WORKS (3 STEPS) -->
        <div id="how-it-works" class="py-5">
            <div class="text-center mb-5">
                <span class="badge px-3 py-1 rounded-pill fw-semibold text-uppercase" style="background: #fef3c7; color: #b45309; font-size: 12px;">How It Works</span>
                <h2 class="fw-bold mt-2" style="color: #2e3760;">Three Steps, Under Two Seconds</h2>
                <p class="text-muted mx-auto" style="max-width: 680px;">
                    This is what happens from the moment a customer shows their card to the moment they are approved.
                </p>
            </div>

            <!-- STEP 1: SCAN THE CARD -->
            <div class="dis-step-card p-4 p-md-5">
                <div class="row align-items-center g-4">
                    <div class="col-lg-6 order-2 order-lg-1">
                        <div class="d-flex align-items-center mb-3">
                            <span class="dis-step-num">1</span>
                            <span class="badge bg-primary px-3 py-1 rounded-pill" style="font-size: 12px;">Step 1 &bull; Scan the Card</span>
                        </div>
                        <h3 class="fw-bold mb-3" style="color: #2e3760;">Scan the Card, Skip the Typing</h3>
                        <p class="text-muted" style="line-height: 1.8;">
                            The customer or officer points a phone camera at the card. The app finds the card edges, straightens the image and removes glare by itself.
                        </p>
                        <p class="text-muted" style="line-height: 1.8;">
                            In about <strong>0.1 seconds</strong>, the system reads the card in Bangla and English and fills in the form:
                        </p>
                        <div class="row g-2 mb-3">
                            <div class="col-sm-6">
                                <ul class="list-unstyled small text-muted mb-0">
                                    <li class="mb-1"><i class="fas fa-check text-success me-2"></i> Name in Bangla and English</li>
                                    <li class="mb-1"><i class="fas fa-check text-success me-2"></i> Father's and mother's name</li>
                                    <li class="mb-1"><i class="fas fa-check text-success me-2"></i> Date of birth</li>
                                    <li class="mb-1"><i class="fas fa-check text-success me-2"></i> NID number</li>
                                </ul>
                            </div>
                            <div class="col-sm-6">
                                <ul class="list-unstyled small text-muted mb-0">
                                    <li class="mb-1"><i class="fas fa-check text-success me-2"></i> Gender and nationality</li>
                                    <li class="mb-1"><i class="fas fa-check text-success me-2"></i> Document number and expiry</li>
                                    <li class="mb-1"><i class="fas fa-check text-success me-2"></i> Issuing authority</li>
                                    <li class="mb-1"><i class="fas fa-check text-success me-2"></i> Barcode and passport MRZ data</li>
                                </ul>
                            </div>
                        </div>
                    </div>
                    <div class="col-lg-6 order-1 order-lg-2 text-center">
                        <picture>
                            <source srcset="assets/img/digital-identity/step1-document-scan.webp" type="image/webp">
                            <img src="assets/img/digital-identity/step1-document-scan.jpg" alt="SPECIMEN national ID card on a bank counter next to a phone showing Card scanned in 0.1 s" class="img-fluid rounded-3 shadow-sm" style="max-height: 340px; width: 100%; object-fit: cover;" loading="lazy">
                        </picture>
                    </div>
                </div>
            </div>

            <!-- STEP 2: CHECK THE CARD -->
            <div class="dis-step-card p-4 p-md-5">
                <div class="row align-items-center g-4">
                    <div class="col-lg-6 text-center">
                        <picture>
                            <source srcset="assets/img/digital-identity/step2-forensic-card-analysis.webp" type="image/webp">
                            <img src="assets/img/digital-identity/step2-forensic-card-analysis.jpg" alt="SPECIMEN national ID card under a magnifier lamp, with a checklist for microprint, hologram and chip data" class="img-fluid rounded-3 shadow-sm" style="max-height: 340px; width: 100%; object-fit: cover;" loading="lazy">
                        </picture>
                    </div>
                    <div class="col-lg-6">
                        <div class="d-flex align-items-center mb-3">
                            <span class="dis-step-num" style="background: linear-gradient(135deg, #f26522 0%, #c2410c 100%);">2</span>
                            <span class="badge bg-warning text-dark px-3 py-1 rounded-pill" style="font-size: 12px;">Step 2 &bull; Check the Card</span>
                        </div>
                        <h3 class="fw-bold mb-3" style="color: #2e3760;">Make Sure the Card Is Genuine</h3>
                        <p class="text-muted" style="line-height: 1.8;">
                            A good colour printout on plastic can fool the eye. The system looks closer, at three layers a fake rarely gets right:
                        </p>
                        <div class="d-flex mb-3">
                            <div class="me-3 text-warning"><i class="fas fa-layer-group fa-lg"></i></div>
                            <div>
                                <h6 class="fw-bold mb-1" style="color: #2e3760;">Fine Print and Line Patterns</h6>
                                <p class="text-muted small mb-0">Real cards carry tiny text and fine lines that blur when a card is copied or reprinted.</p>
                            </div>
                        </div>
                        <div class="d-flex mb-3">
                            <div class="me-3 text-warning"><i class="fas fa-gem fa-lg"></i></div>
                            <div>
                                <h6 class="fw-bold mb-1" style="color: #2e3760;">Hologram</h6>
                                <p class="text-muted small mb-0">A real hologram changes colour as the light moves. A flat print does not.</p>
                            </div>
                        </div>
                        <div class="d-flex">
                            <div class="me-3 text-warning"><i class="fas fa-microchip fa-lg"></i></div>
                            <div>
                                <h6 class="fw-bold mb-1" style="color: #2e3760;">Chip and Barcode</h6>
                                <p class="text-muted small mb-0">The data stored in the chip and barcode must match the printed details exactly.</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- STEP 3: CHECK THE PERSON -->
            <div class="dis-step-card p-4 p-md-5">
                <div class="row align-items-center g-4">
                    <div class="col-lg-6 order-2 order-lg-1">
                        <div class="d-flex align-items-center mb-3">
                            <span class="dis-step-num" style="background: linear-gradient(135deg, #10b981 0%, #047857 100%);">3</span>
                            <span class="badge bg-success px-3 py-1 rounded-pill" style="font-size: 12px;">Step 3 &bull; Check the Person</span>
                        </div>
                        <h3 class="fw-bold mb-3" style="color: #2e3760;">Confirm a Real, Live Person</h3>
                        <p class="text-muted" style="line-height: 1.8;">
                            The customer looks at the camera for a moment. They do not need to blink, smile or turn their head. The system checks that the face has real depth, then matches it with the photo on the card.
                        </p>
                        <div class="p-3 rounded mb-3" style="background: #f8fafc; border-left: 4px solid #10b981;">
                            <h6 class="fw-bold text-success mb-1"><i class="fas fa-shield-alt me-1"></i> Blocks Common Tricks</h6>
                            <p class="small text-muted mb-0">Printed photos, videos played on a phone or tablet, masks and AI-generated deepfakes.</p>
                        </div>
                        <div class="d-flex flex-wrap align-items-center gap-2 pt-2">
                            <div class="badge bg-light text-dark border px-3 py-2 mb-1">
                                <i class="fas fa-fingerprint text-success me-1"></i> Fingerprint Matching
                            </div>
                            <div class="badge bg-light text-dark border px-3 py-2 mb-1">
                                <i class="fas fa-eye text-primary me-1"></i> Iris Ready
                            </div>
                            <div class="badge bg-light text-dark border px-3 py-2 mb-1">
                                <i class="fas fa-lock text-warning me-1"></i> Every Check Logged
                            </div>
                        </div>
                    </div>
                    <div class="col-lg-6 order-1 order-lg-2 text-center">
                        <picture>
                            <source srcset="assets/img/digital-identity/step3-biometric-liveness-antispoof.webp" type="image/webp">
                            <img src="assets/img/digital-identity/step3-biometric-liveness-antispoof.jpg" alt="A live person passes the face check, while a printed photo held to the camera is blocked as a spoof" class="img-fluid rounded-3 shadow-sm" style="max-height: 340px; width: 100%; object-fit: cover;" loading="lazy">
                        </picture>
                    </div>
                </div>
            </div>
        </div>

        <!-- SECTION: HOW THE SYSTEM FITS TOGETHER -->
        <div id="architecture" class="py-4">
            <div class="text-center mb-4">
                <span class="badge px-3 py-1 rounded-pill fw-semibold text-uppercase" style="background: #e0f2fe; color: #0369a1; font-size: 12px;">Under the Hood</span>
                <h2 class="fw-bold mt-2" style="color: #2e3760;">How the System Fits Together</h2>
                <p class="text-muted mx-auto" style="max-width: 700px;">
                    Three parts, each with one job. Data is encrypted from the moment it is captured, and it never leaves Bangladesh.
                </p>
            </div>

            <!-- Architecture Diagram Container -->
            <div class="dis-arch-wrapper p-3 p-md-4 mb-4">
                <div class="text-center">
                    <picture>
                        <source srcset="assets/img/digital-identity/architecture-ecosystem.webp" type="image/webp">
                        <img src="assets/img/digital-identity/architecture-ecosystem.jpg" alt="How the ID verification system works: capture devices send encrypted data to the verification engine, which keeps keys and audit logs in a secure vault inside Bangladesh" class="img-fluid rounded-3" style="max-height: 520px; width: 100%; object-fit: contain;" loading="lazy">
                    </picture>
                </div>
                <div class="row g-3 pt-4 text-light">
                    <div class="col-md-4">
                        <div class="p-3 rounded" style="background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.1);">
                            <h6 class="fw-bold text-info mb-1"><i class="fas fa-mobile-alt me-2"></i> 1. Capture</h6>
                            <p class="small text-white-50 mb-0">Phones, tablets, POS terminals, fingerprint scanners and kiosks collect the card image, face and fingerprints.</p>
                        </div>
                    </div>
                    <div class="col-md-4">
                        <div class="p-3 rounded" style="background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.1);">
                            <h6 class="fw-bold text-warning mb-1"><i class="fas fa-brain me-2"></i> 2. Verification Engine</h6>
                            <p class="small text-white-50 mb-0">Runs on your own servers or a local data centre. It reads cards, checks for forgery, tests liveness and matches faces and fingerprints.</p>
                        </div>
                    </div>
                    <div class="col-md-4">
                        <div class="p-3 rounded" style="background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.1);">
                            <h6 class="fw-bold text-success mb-1"><i class="fas fa-database me-2"></i> 3. Secure Vault</h6>
                            <p class="small text-white-50 mb-0">Keeps encryption keys in a hardware security module (HSM) and records every check in an audit log that cannot be altered.</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- SECTION: BENEFITS -->
        <div class="py-5">
            <div class="text-center mb-5">
                <span class="badge px-3 py-1 rounded-pill fw-semibold text-uppercase" style="background: #e0e7ff; color: #4338ca; font-size: 12px;">Benefits</span>
                <h2 class="fw-bold mt-2" style="color: #2e3760;">What Your Organisation Gets</h2>
                <p class="text-muted mx-auto" style="max-width: 650px;">
                    Faster sign-up for customers, less manual work for staff, and fewer losses to fraud.
                </p>
            </div>

            <div class="row g-4">
                <div class="col-md-6 col-lg-3">
                    <div class="dis-feature-box">
                        <div class="mb-3 text-danger"><i class="fas fa-ban fa-2x"></i></div>
                        <h6 class="fw-bold" style="color: #2e3760;">Catch Fake IDs</h6>
                        <p class="text-muted small mb-0">Forged, edited and borrowed cards are flagged before an account is opened.</p>
                    </div>
                </div>

                <div class="col-md-6 col-lg-3">
                    <div class="dis-feature-box">
                        <div class="mb-3 text-primary"><i class="fas fa-file-contract fa-2x"></i></div>
                        <h6 class="fw-bold" style="color: #2e3760;">Meet KYC Rules</h6>
                        <p class="text-muted small mb-0">Supports Bangladesh Bank e-KYC guidelines and AML checks, with records ready for audit.</p>
                    </div>
                </div>

                <div class="col-md-6 col-lg-3">
                    <div class="dis-feature-box">
                        <div class="mb-3 text-success"><i class="fas fa-user-plus fa-2x"></i></div>
                        <h6 class="fw-bold" style="color: #2e3760;">Faster Sign-Up</h6>
                        <p class="text-muted small mb-0">Customers finish verification in seconds, so fewer give up halfway.</p>
                    </div>
                </div>

                <div class="col-md-6 col-lg-3">
                    <div class="dis-feature-box">
                        <div class="mb-3 text-warning"><i class="fas fa-bullseye fa-2x"></i></div>
                        <h6 class="fw-bold" style="color: #2e3760;">Reads Bangla Properly</h6>
                        <p class="text-muted small mb-0">Built for Bangla script, including joined letters and worn, older cards.</p>
                    </div>
                </div>

                <div class="col-md-6 col-lg-3">
                    <div class="dis-feature-box">
                        <div class="mb-3 text-info"><i class="fas fa-cubes fa-2x"></i></div>
                        <h6 class="fw-bold" style="color: #2e3760;">Works on Any Channel</h6>
                        <p class="text-muted small mb-0">Android and iOS SDKs, Flutter, React Native, web camera, REST API and SMS links.</p>
                    </div>
                </div>

                <div class="col-md-6 col-lg-3">
                    <div class="dis-feature-box">
                        <div class="mb-3 text-secondary"><i class="fas fa-cogs fa-2x"></i></div>
                        <h6 class="fw-bold" style="color: #2e3760;">Less Paperwork</h6>
                        <p class="text-muted small mb-0">Staff no longer type card details or file photocopies.</p>
                    </div>
                </div>

                <div class="col-md-6 col-lg-3">
                    <div class="dis-feature-box">
                        <div class="mb-3 text-dark"><i class="fas fa-shield-virus fa-2x"></i></div>
                        <h6 class="fw-bold" style="color: #2e3760;">Stops Spoofing</h6>
                        <p class="text-muted small mb-0">Photos, screen replays, masks and deepfakes are blocked at the camera.</p>
                    </div>
                </div>

                <div class="col-md-6 col-lg-3">
                    <div class="dis-feature-box">
                        <div class="mb-3 text-success"><i class="fas fa-file-invoice fa-2x"></i></div>
                        <h6 class="fw-bold" style="color: #2e3760;">Full Audit Trail</h6>
                        <p class="text-muted small mb-0">Every check is logged and sealed, so the record cannot be changed later.</p>
                    </div>
                </div>
            </div>
        </div>

        <!-- SECTION: PROOF AT NATIONAL SCALE (TCB) -->
        <div class="card mb-5 border-0 shadow-sm" style="border-radius: 16px; background: linear-gradient(135deg, #064e3b 0%, #0f172a 100%); color: white;">
            <div class="card-body p-4 p-md-5">
                <div class="row align-items-center g-4">
                    <div class="col-lg-8">
                        <div class="d-inline-flex align-items-center px-3 py-1 rounded-pill mb-3" style="background: rgba(16, 185, 129, 0.2); border: 1px solid rgba(16, 185, 129, 0.4); color: #34d399; font-size: 13px; font-weight: 700;">
                            <i class="fas fa-landmark me-2"></i> PROVEN AT NATIONAL SCALE
                        </div>
                        <h2 class="text-white fw-bold mb-3">TCB Family Card: 10 Million Families</h2>
                        <p class="text-light opacity-90 mb-4" style="line-height: 1.8; font-size: 16px;">
                            For the <strong>Trading Corporation of Bangladesh (TCB)</strong>, Spectrum enrolled more than <strong>10 million low-income families</strong>, about 50 million people, and issued each family a smart card. Each family is registered only once, so subsidised goods reach the right people.
                        </p>
                        <div class="d-flex flex-wrap gap-3">
                            <a href="case-study.html" class="btn btn-warning px-4 py-2 fw-bold text-dark rounded-pill shadow-sm">
                                <i class="fas fa-file-alt me-2"></i> Read the TCB Case Study
                            </a>
                            <a href="contact.html" class="btn btn-outline-light px-4 py-2 rounded-pill fw-semibold">
                                <i class="fas fa-envelope me-2"></i> Talk to Our Team
                            </a>
                        </div>
                    </div>
                    <div class="col-lg-4 text-center">
                        <div class="p-4 bg-white rounded-3 shadow text-dark">
                            <div class="p-3 rounded-circle d-inline-flex align-items-center justify-content-center mb-3" style="background: rgba(16, 185, 129, 0.1); width: 80px; height: 80px;">
                                <i class="fas fa-hands-helping fa-3x text-success"></i>
                            </div>
                            <h4 class="fw-bold mb-1" style="color: #2e3760;">10,000,000+</h4>
                            <p class="text-muted fw-semibold small mb-2">Families Enrolled</p>
                            <span class="badge bg-success-subtle text-success border border-success-subtle px-3 py-1 rounded-pill" style="font-size: 11px;">One Card per Family</span>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- SECTION: WHO USES IT -->
        <div class="py-4">
            <div class="text-center mb-5">
                <span class="badge px-3 py-1 rounded-pill fw-semibold text-uppercase" style="background: #e2e8f0; color: #334155; font-size: 12px;">Who Uses It</span>
                <h2 class="fw-bold mt-2" style="color: #2e3760;">Built for These Sectors</h2>
                <p class="text-muted mx-auto" style="max-width: 650px;">
                    The same engine, set up for each sector's rules and daily workflow.
                </p>
            </div>

            <div class="row g-4">
                <div class="col-md-6 col-lg-4">
                    <div class="dis-industry-card">
                        <div class="d-flex align-items-center mb-3">
                            <div class="me-3 text-primary"><i class="fas fa-university fa-2x"></i></div>
                            <h5 class="fw-bold mb-0" style="color: #2e3760;">Banks &amp; Mobile Financial Services</h5>
                        </div>
                        <p class="text-muted small mb-0" style="line-height: 1.7;">
                            Open accounts, issue cards and approve loans with e-KYC, in a branch or on the customer's own phone.
                        </p>
                    </div>
                </div>

                <div class="col-md-6 col-lg-4">
                    <div class="dis-industry-card">
                        <div class="d-flex align-items-center mb-3">
                            <div class="me-3 text-info"><i class="fas fa-broadcast-tower fa-2x"></i></div>
                            <h5 class="fw-bold mb-0" style="color: #2e3760;">Telecom</h5>
                        </div>
                        <p class="text-muted small mb-0" style="line-height: 1.7;">
                            Register SIM cards and eSIMs with a fingerprint check at the retail counter, in seconds.
                        </p>
                    </div>
                </div>

                <div class="col-md-6 col-lg-4">
                    <div class="dis-industry-card">
                        <div class="d-flex align-items-center mb-3">
                            <div class="me-3 text-success"><i class="fas fa-landmark fa-2x"></i></div>
                            <h5 class="fw-bold mb-0" style="color: #2e3760;">Government</h5>
                        </div>
                        <p class="text-muted small mb-0" style="line-height: 1.7;">
                            Civil service records, voter lists, civil registration and secure access to government buildings.
                        </p>
                    </div>
                </div>

                <div class="col-md-6 col-lg-4">
                    <div class="dis-industry-card">
                        <div class="d-flex align-items-center mb-3">
                            <div class="me-3 text-danger"><i class="fas fa-shield-alt fa-2x"></i></div>
                            <h5 class="fw-bold mb-0" style="color: #2e3760;">Police &amp; Border Control</h5>
                        </div>
                        <p class="text-muted small mb-0" style="line-height: 1.7;">
                            Fingerprint and face search (AFIS/ABIS), watch-list alerts and identity checks at border points.
                        </p>
                    </div>
                </div>

                <div class="col-md-6 col-lg-4">
                    <div class="dis-industry-card">
                        <div class="d-flex align-items-center mb-3">
                            <div class="me-3 text-warning"><i class="fas fa-hospital-user fa-2x"></i></div>
                            <h5 class="fw-bold mb-0" style="color: #2e3760;">Healthcare &amp; Education</h5>
                        </div>
                        <p class="text-muted small mb-0" style="line-height: 1.7;">
                            One record per patient, faster insurance claim checks, and verified candidates at national exams.
                        </p>
                    </div>
                </div>

                <div class="col-md-6 col-lg-4">
                    <div class="dis-industry-card">
                        <div class="d-flex align-items-center mb-3">
                            <div class="me-3 text-secondary"><i class="fas fa-hand-holding-heart fa-2x"></i></div>
                            <h5 class="fw-bold mb-0" style="color: #2e3760;">NGOs &amp; Social Safety Nets</h5>
                        </div>
                        <p class="text-muted small mb-0" style="line-height: 1.7;">
                            Food aid, relief payments and other benefits reach each person once, with a clear record of who received what.
                        </p>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- SECTION: CALL TO ACTION -->
    <div class="container-fluid py-5 cta-banner-section">
        <div class="container text-center py-4 position-relative" style="z-index: 2;">
            <span class="badge px-3 py-2 rounded-pill fw-semibold mb-3" style="background: rgba(242, 101, 34, 0.2); color: #f26522; border: 1px solid rgba(242, 101, 34, 0.4); font-size: 13px;">Talk to Our Team</span>
            <h2 class="display-6 fw-bold text-white mb-3">See Our ID Verification Check Your Own Cards</h2>
            <p class="text-light opacity-75 mx-auto mb-4" style="max-width: 650px; font-size: 16px; line-height: 1.7;">
                Book a demo. We will run a live check and talk through what you need, whether that is e-KYC, a citizen registry or a system that runs fully on your own site.
            </p>
            <div class="d-flex justify-content-center align-items-center flex-wrap gap-3 pt-2">
                <a href="contact.html" class="cta-primary-btn">
                    <i class="fas fa-paper-plane me-2"></i> Book a Demo
                </a>
                <a href="case-study.html" class="cta-secondary-btn">
                    <i class="fas fa-folder-open me-2"></i> View TCB Case Study
                </a>
            </div>
        </div>
    </div>

{COMMON_FOOTER}
</body>
</html>"""

with open(os.path.join(DIR, 'Digital_Identity_&_Security.html'), 'w', encoding='utf-8') as f:
    f.write(dis_content)
with open(os.path.join(DIR, 'Digital_Identity_ & Security.html'), 'w', encoding='utf-8') as f:
    f.write(dis_content)
with open(os.path.join(DIR, 'dis.html'), 'w', encoding='utf-8') as f:
    f.write(dis_content)
print("Digital_Identity_&_Security.html & aliases updated.")

# 6. GENERATE CONTACT.HTML (MODERNIZED EXECUTIVE DESIGN)
contact_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
{get_head(
    title="Contact Corporate Headquarters | Spectrum IT Solutions Ltd.",
    description="Contact Spectrum IT Solutions Ltd. in Dhaka, Bangladesh for sovereign digital identity, smart card personalization, biometric systems, and enterprise software engineering.",
    canonical_slug="contact.html",
    og_image="assets/img/contact_img.png"
)}
</head>
<body>
{COMMON_TOP_BAR}
{get_navbar('contact')}

    <!-- Page Hero Banner -->
    <div class="page-hero-banner">
        <div class="container position-relative text-center">
            <div class="breadcrumb-pill">
                <a href="index.html"><i class="fas fa-home me-1"></i> Home</a>
                <span class="opacity-50">/</span>
                <span style="color: #f26522; font-weight: 600;">Contact Us</span>
            </div>
            <h1>Get in <span>Touch</span></h1>
            <p class="hero-desc">
                Have an enterprise project in mind, need sovereign digital identity consultation, or want to explore smart card issuance solutions? Reach out directly to our engineering headquarters in Dhaka.
            </p>
            <div class="hero-features">
                <span class="hero-feature-item">
                    <i class="fas fa-map-marker-alt" style="color: #f26522;"></i> Hasan Holdings Ltd., Dhaka
                </span>
                <span class="hero-feature-item">
                    <i class="fas fa-phone-alt" style="color: #4ade80;"></i> +880 1615-900004
                </span>
                <span class="hero-feature-item">
                    <i class="fas fa-envelope" style="color: #38bdf8;"></i> contact@spectrum.com.bd
                </span>
                <span class="hero-feature-item">
                    <i class="fas fa-shield-alt" style="color: #fbbf24;"></i> ISO 9001 &amp; 27001 Certified
                </span>
            </div>
        </div>
    </div>

    <!-- Quick Contact Cards Section -->
    <div class="container py-5">
        <div class="row g-4">
            <div class="col-md-4">
                <div class="quick-contact-card">
                    <div class="icon-box" style="background: rgba(46, 55, 96, 0.08); color: #2e3760;">
                        <i class="fas fa-briefcase"></i>
                    </div>
                    <h5 class="fw-bold mb-2" style="color: #2e3760;">Enterprise Inquiries</h5>
                    <p class="text-muted small mb-3">Sovereign identity, civil registries, smart card systems, and government tender / RFP inquiries.</p>
                    <a href="mailto:contact@spectrum.com.bd" class="text-decoration-none fw-bold" style="color: #f26522; font-size: 14px;">
                        contact@spectrum.com.bd <i class="fas fa-arrow-right ms-1 small"></i>
                    </a>
                </div>
            </div>
            <div class="col-md-4">
                <div class="quick-contact-card">
                    <div class="icon-box" style="background: rgba(242, 101, 34, 0.1); color: #f26522;">
                        <i class="fas fa-headset"></i>
                    </div>
                    <h5 class="fw-bold mb-2" style="color: #2e3760;">Direct Support Desk</h5>
                    <p class="text-muted small mb-3">Dedicated SLA technical assistance, operational maintenance, and deployed system support.</p>
                    <a href="tel:+8801615900004" class="text-decoration-none fw-bold" style="color: #f26522; font-size: 14px;">
                        +880 1615 900 004 <i class="fas fa-arrow-right ms-1 small"></i>
                    </a>
                </div>
            </div>
            <div class="col-md-4">
                <div class="quick-contact-card">
                    <div class="icon-box" style="background: rgba(30, 126, 52, 0.1); color: #1e7e34;">
                        <i class="fas fa-handshake"></i>
                    </div>
                    <h5 class="fw-bold mb-2" style="color: #2e3760;">Strategic Alliances</h5>
                    <p class="text-muted small mb-3">OEM hardware integrations, technological consortiums, and joint digital transformation programs.</p>
                    <a href="#contact-form-section" class="text-decoration-none fw-bold" style="color: #1e7e34; font-size: 14px;">
                        Partner With Us <i class="fas fa-arrow-right ms-1 small"></i>
                    </a>
                </div>
            </div>
        </div>
    </div>

    <!-- Main Contact & Form Section -->
    <div class="container py-3 mb-5" id="contact-form-section">
        <!-- Centered Header -->
        <div class="text-center mb-5">
            <span class="badge px-3 py-2 rounded-pill fw-bold mb-2" style="background: rgba(242, 101, 34, 0.1); color: #f26522; font-size: 13px; text-transform: uppercase; letter-spacing: 0.5px;">Direct Communication</span>
            <h2 class="header_two" style="color: #2e3760; font-size: 32px; font-weight: 700; text-align: center !important;">Start a Conversation with Our Architects</h2>
            <p class="text-muted" style="max-width: 650px; margin: 0 auto;">Whether you are designing a high-assurance citizen registry or upgrading mission-critical IT infrastructure, our solution architects provide clear technical guidance.</p>
        </div>

        <div class="row g-4 align-items-stretch">
            <!-- Left: Headquarters Information Block -->
            <div class="col-lg-5">
                <div class="contact-info-block h-100 d-flex flex-column justify-content-between">
                    <div>
                        <div class="overflow-hidden rounded-3 mb-4 shadow-sm text-center bg-light">
                            <picture><source srcset="assets/img/contact_img.webp" type="image/webp"><img src="assets/img/contact_img.png" alt="Spectrum IT Solutions Headquarters Dhaka" loading="lazy" class="img-fluid w-100" style="height: auto; display: block; object-fit: contain;"></picture>
                        </div>
                        
                        <div class="d-flex align-items-center justify-content-between mb-3">
                            <h4 class="fw-bold mb-0" style="color: #2e3760; font-size: 20px;">Corporate Headquarters</h4>
                            <span class="badge bg-success-subtle text-success border border-success-subtle px-2 py-1 rounded-pill small">
                                <i class="fas fa-check-circle me-1"></i> Verified
                            </span>
                        </div>
                        <p class="text-muted small mb-4">Engineering labs, systems integration center, and sovereign technology operations in Dhaka, Bangladesh.</p>

                        <div class="contact-channel-item">
                            <div class="contact-channel-icon" style="background: #eef2ff; color: #2e3760;">
                                <i class="fas fa-map-marker-alt"></i>
                            </div>
                            <div class="contact-channel-info">
                                <h6>Registered Office Address</h6>
                                <p>52/1, New Eskaton Road (Hasan Holdings Ltd., 12th Floor), Dhaka-1000, Bangladesh</p>
                            </div>
                        </div>

                        <div class="contact-channel-item">
                            <div class="contact-channel-icon" style="background: #fff7ed; color: #f26522;">
                                <i class="fas fa-envelope"></i>
                            </div>
                            <div class="contact-channel-info">
                                <h6>Official Communications</h6>
                                <a href="mailto:contact@spectrum.com.bd">contact@spectrum.com.bd</a>
                            </div>
                        </div>

                        <div class="contact-channel-item">
                            <div class="contact-channel-icon" style="background: #f0fdf4; color: #16a34a;">
                                <i class="fas fa-phone-alt"></i>
                            </div>
                            <div class="contact-channel-info">
                                <h6>Voice &amp; WhatsApp Hotline</h6>
                                <a href="tel:+8801615900004">+880 1615-900004</a>
                            </div>
                        </div>

                        <div class="contact-channel-item">
                            <div class="contact-channel-icon" style="background: #f8fafc; color: #64748b;">
                                <i class="fas fa-clock"></i>
                            </div>
                            <div class="contact-channel-info">
                                <h6>Operational Hours</h6>
                                <p>Sunday &ndash; Thursday: 9:00 AM &ndash; 6:00 PM (BST / UTC+6)</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Right: Modern Form Card -->
            <div class="col-lg-7">
                <div class="contact-form-modern h-100">
                    <div class="d-flex align-items-center justify-content-between mb-3">
                        <div>
                            <span class="text-uppercase fw-bold" style="color: #f26522; font-size: 12px; letter-spacing: 1px;">Direct Inquiry</span>
                            <h3 class="fw-bold mb-1" style="color: #2e3760; font-size: 24px;">Send Us a Message</h3>
                        </div>
                        <span class="badge bg-light text-muted border px-3 py-2 rounded-pill small d-none d-sm-inline-block">
                            <i class="fas fa-bolt text-warning me-1"></i> 24h SLA Response
                        </span>
                    </div>
                    <p class="text-muted small mb-4">Please submit your details below. Our enterprise solutions team will review your specifications and contact you shortly.</p>

                    <!-- Submission Feedback Alert -->
                    <div id="contact-success-alert" class="alert alert-success d-none mb-4" role="alert">
                        <div class="d-flex align-items-center">
                            <i class="fas fa-check-circle fs-3 me-3 text-success"></i>
                            <div>
                                <h6 class="alert-heading fw-bold mb-1">Message Submitted Successfully!</h6>
                                <p class="mb-0 small">Thank you for getting in touch with Spectrum IT Solutions. An enterprise solution architect will respond within 24 business hours.</p>
                            </div>
                        </div>
                    </div>

                    <form id="contact-form" action="#" method="post">
                        <div class="row g-3">
                            <div class="col-md-6">
                                <label for="name" class="form-label">Full Name <span class="text-danger">*</span></label>
                                <input type="text" class="form-control" id="name" name="name" placeholder="Enter your full name" required autocomplete="name">
                            </div>
                            <div class="col-md-6">
                                <label for="sname" class="form-label">Company / Institution <span class="text-danger">*</span></label>
                                <input type="text" class="form-control" id="sname" name="sname" placeholder="Organization / Ministry" required autocomplete="organization">
                            </div>
                            <div class="col-md-6">
                                <label for="email" class="form-label">Email Address <span class="text-danger">*</span></label>
                                <input type="email" class="form-control" id="email" name="email" placeholder="name@organization.com" required autocomplete="email">
                            </div>
                            <div class="col-md-6">
                                <label for="Phone" class="form-label">Phone / Mobile Number <span class="text-danger">*</span></label>
                                <input type="tel" class="form-control" id="Phone" name="Phone" placeholder="+880 1XXXXXXXXX" required autocomplete="tel">
                            </div>
                            <div class="col-md-6">
                                <label for="Country" class="form-label">Country / Region</label>
                                <input type="text" class="form-control" id="Country" name="Country" placeholder="Bangladesh" autocomplete="country-name">
                            </div>
                            <div class="col-md-6">
                                <label for="aboutUs" class="form-label">How Did You Hear About Us?</label>
                                <input type="text" class="form-control" id="aboutUs" name="aboutUs" placeholder="Referral, Exhibition, Web Search, etc.">
                            </div>
                            <div class="col-12">
                                <label for="service_interest" class="form-label">Area of Interest</label>
                                <select class="form-select form-control" id="service_interest" name="service_interest">
                                    <option value="General Consultation" selected>General Consultation &amp; Inquiry</option>
                                    <option value="Digital Identity &amp; Biometrics">Digital Identity &amp; Biometric Systems</option>
                                    <option value="Smart Card Personalization">Smart Card Personalization &amp; Issuance Hardware</option>
                                    <option value="Enterprise Software Engineering">Custom Enterprise Software Engineering</option>
                                    <option value="AI &amp; Computer Vision">Artificial Intelligence &amp; Computer Vision</option>
                                    <option value="Cyber Security &amp; Infrastructure">Cyber Security &amp; Infrastructure Operations</option>
                                </select>
                            </div>
                            <div class="col-12">
                                <label for="subject" class="form-label">Project Details / Message <span class="text-danger">*</span></label>
                                <textarea class="form-control" id="subject" name="message" rows="4" placeholder="Briefly outline your objectives, project scope, technical specifications, or timeline..." required></textarea>
                            </div>
                            <div class="col-12 pt-2 text-center">
                                <button type="submit" class="cta-primary-btn w-100" style="padding: 14px 28px; font-size: 16px; border: none; cursor: pointer; justify-content: center;">
                                    <i class="fas fa-paper-plane me-2"></i> Submit Inquiry
                                </button>
                                <p class="text-muted mt-2 mb-0" style="font-size: 12px;">
                                    <i class="fas fa-lock text-success me-1"></i> Confidentiality Guaranteed. We strictly adhere to ISO 27001 data protection protocols.
                                </p>
                            </div>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    </div>

    <!-- Full-Width Institutional Accreditations Section -->
    <div class="container py-4 mb-5">
        <div class="text-center mb-4">
            <span class="badge px-3 py-2 rounded-pill fw-bold mb-2" style="background: rgba(46, 55, 96, 0.08); color: #2e3760; font-size: 12px; text-transform: uppercase; letter-spacing: 0.5px;">Trust &amp; Governance</span>
            <h3 class="fw-bold mb-1" style="color: #2e3760; font-size: 26px;">Institutional Accreditations</h3>
            <p class="text-muted small mb-0" style="max-width: 600px; margin: 0 auto;">Adhering to international quality assurance benchmarks and verified by Bangladesh&rsquo;s statutory ICT authorities.</p>
        </div>
        <div class="row g-4">
            <div class="col-lg-3 col-sm-6">
                <div class="accreditation-card">
                    <div class="icon-wrap" style="background: rgba(13, 110, 253, 0.1); color: #0d6efd;">
                        <i class="fas fa-shield-alt"></i>
                    </div>
                    <h5 class="fw-bold mb-1" style="color: #2e3760; font-size: 17px;">ISO 9001:2015</h5>
                    <p class="text-muted small mb-0">Quality Management Systems Certified for Sovereign IT Infrastructure</p>
                </div>
            </div>
            <div class="col-lg-3 col-sm-6">
                <div class="accreditation-card">
                    <div class="icon-wrap" style="background: rgba(25, 135, 84, 0.1); color: #198754;">
                        <i class="fas fa-lock"></i>
                    </div>
                    <h5 class="fw-bold mb-1" style="color: #2e3760; font-size: 17px;">ISO 27001:2013</h5>
                    <p class="text-muted small mb-0">Information Security Management &amp; Cryptographic Data Protection</p>
                </div>
            </div>
            <div class="col-lg-3 col-sm-6">
                <div class="accreditation-card">
                    <div class="icon-wrap" style="background: rgba(242, 101, 34, 0.1); color: #f26522;">
                        <i class="fas fa-award"></i>
                    </div>
                    <h5 class="fw-bold mb-1" style="color: #2e3760; font-size: 17px;">BASIS Member</h5>
                    <p class="text-muted small mb-0">Bangladesh Association of Software &amp; Information Services (Member #21-04-024)</p>
                </div>
            </div>
            <div class="col-lg-3 col-sm-6">
                <div class="accreditation-card">
                    <div class="icon-wrap" style="background: rgba(13, 202, 240, 0.15); color: #0891b2;">
                        <i class="fas fa-network-wired"></i>
                    </div>
                    <h5 class="fw-bold mb-1" style="color: #2e3760; font-size: 17px;">BCS Member</h5>
                    <p class="text-muted small mb-0">Bangladesh Computer Samity National ICT Industry Association</p>
                </div>
            </div>
        </div>
    </div>

    <!-- Interactive Google Map Section -->
    <div class="container-fluid px-0">
        <div class="google-map-wrapper">
            <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3652.008074018641!2d90.39395197597223!3d23.747091488902118!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3755b9330fad8b19%3A0x71a6a0b1575c404c!2sHasan%20Holdings%20Limited!5e0!3m2!1sen!2sbd!4v1694437419837!5m2!1sen!2sbd" height="420" style="width: 100%; border: 0; display: block;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade" title="Spectrum IT Solutions Office Location Map"></iframe>
        </div>
    </div>

    <!-- SECTION: CALL TO ACTION -->
    <div class="container-fluid py-5 cta-banner-section">
        <div class="container text-center py-4 position-relative" style="z-index: 2;">
            <span class="badge px-3 py-2 rounded-pill fw-semibold mb-3" style="background: rgba(242, 101, 34, 0.2); color: #f26522; border: 1px solid rgba(242, 101, 34, 0.4); font-size: 13px;">Direct Sovereign Advisory</span>
            <h2 class="display-6 fw-bold text-white mb-3">Ready to Build Resilient Digital Systems?</h2>
            <p class="text-light opacity-75 mx-auto mb-4" style="max-width: 650px; font-size: 16px; line-height: 1.7;">
                Partner with Spectrum IT Solutions for mission-critical digital identity, smart card issuance, and sovereign software engineering.
            </p>
            <div class="d-flex justify-content-center align-items-center flex-wrap gap-3 pt-2">
                <a href="tel:+8801615900004" class="cta-primary-btn">
                    <i class="fas fa-phone-alt me-2"></i> Call Direct: +880 1615-900004
                </a>
                <a href="case-study.html" class="cta-secondary-btn">
                    <i class="fas fa-folder-open me-2"></i> Explore Case Studies
                </a>
            </div>
        </div>
    </div>

    <!-- Contact Form Feedback Script -->
    <script>
    document.addEventListener('DOMContentLoaded', function() {{
        var form = document.getElementById('contact-form');
        var alertBox = document.getElementById('contact-success-alert');
        if (form) {{
            form.addEventListener('submit', function(e) {{
                e.preventDefault();
                alertBox.classList.remove('d-none');
                form.reset();
                alertBox.scrollIntoView({{ behavior: 'smooth', block: 'center' }});
            }});
        }}
    }});
    </script>

{COMMON_FOOTER}
</body>
</html>"""

with open(os.path.join(DIR, 'contact.html'), 'w', encoding='utf-8') as f:
    f.write(contact_content)
with open(os.path.join(DIR, 'Contact.html'), 'w', encoding='utf-8') as f:
    f.write(contact_content)
print("contact.html & Contact.html updated.")

# 7. GENERATE ARTIFICIAL INTELLIGENCE PAGE (FULL SLUG & PADDED CTA)
ai_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
{get_head(
    title="Artificial Intelligence Solutions | Spectrum IT Solutions",
    description="Artificial Intelligence and machine learning engineering by Spectrum IT Solutions: computer vision, automated document parsing, and enterprise cognitive systems.",
    canonical_slug="Artificial_Intelligence.html",
    og_image="assets/img/Artificial_Intelligence.png"
)}
</head>
<body>
{COMMON_TOP_BAR}
{get_navbar('services')}

    <!-- Page Hero Banner -->
    <div class="page-hero-banner">
        <div class="container position-relative text-center">
            <div class="breadcrumb-pill">
                <a href="index.html"><i class="fas fa-home me-1"></i> Home</a>
                <span class="opacity-50">/</span>
                <a href="services.html">Services</a>
                <span class="opacity-50">/</span>
                <span style="color: #f26522; font-weight: 600;">Artificial Intelligence</span>
            </div>
            <h1>Artificial <span>Intelligence</span></h1>
            <p class="hero-desc">
                Transforming industries, enhancing human capabilities, and automating mission-critical tasks with cutting-edge machine learning and computer vision architectures.
            </p>
            <div class="hero-features">
                <span class="hero-feature-item">
                    <i class="fas fa-brain" style="color: #38bdf8;"></i> Cognitive Neural Networks
                </span>
                <span class="hero-feature-item">
                    <i class="fas fa-eye" style="color: #4ade80;"></i> Computer Vision &amp; CCTV
                </span>
                <span class="hero-feature-item">
                    <i class="fas fa-file-alt" style="color: #f26522;"></i> Automated Document OCR/ICR
                </span>
                <span class="hero-feature-item">
                    <i class="fas fa-microchip" style="color: #fbbf24;"></i> Real-Time Edge Inference
                </span>
            </div>
        </div>
    </div>

    <!-- AI Content -->
    <div class="container py-5">
        <div class="row align-items-center mb-5">
            <div class="col-lg-6 mb-4 mb-lg-0">
                <h2 class="fw-bold mb-3" style="color: #2e3760;">Machine Learning &amp; Computer Vision</h2>
                <p class="text-muted" style="line-height: 1.8;">
                    Spectrum harnesses artificial intelligence to solve complex enterprise problems. From automated facial recognition at biometric security checkpoints to automated document recognition for state regulatory bodies, our algorithms deliver unprecedented accuracy and processing velocity.
                </p>
                <div class="pt-3">
                    <ul class="list-unstyled">
                        <li class="mb-3 d-flex align-items-start">
                            <i class="fas fa-check-circle text-success me-3 mt-1 fa-lg"></i>
                            <div><strong>Real-Time Facial Recognition:</strong> Biometric facial matching integrated with CCTV streams and border verification kiosks.</div>
                        </li>
                        <li class="mb-3 d-flex align-items-start">
                            <i class="fas fa-check-circle text-success me-3 mt-1 fa-lg"></i>
                            <div><strong>Cognitive Document Parsing:</strong> Automated extraction of text, stamps, and signatures from scanned legal and citizen documents.</div>
                        </li>
                        <li class="mb-3 d-flex align-items-start">
                            <i class="fas fa-check-circle text-success me-3 mt-1 fa-lg"></i>
                            <div><strong>Automated Decision Engines:</strong> AI-powered algorithms to solve complex data challenges faster and more accurately for national scale.</div>
                        </li>
                    </ul>
                </div>
            </div>
            <div class="col-lg-6 text-center">
                <img src="assets/img/Artificial_Intelligence_2.jpg" alt="Artificial Intelligence Bangladesh" class="img-fluid rounded shadow-sm" style="max-height: 400px;">
            </div>
        </div>

        <!-- Capability Cards -->
        <div class="row pt-2">
            <div class="col-md-4 mb-4">
                <div class="card h-100 p-4 border-0 shadow-sm" style="border-radius: 12px; border: 1px solid #e2e8f0 !important;">
                    <div class="mb-3 text-info"><i class="fas fa-video fa-2x"></i></div>
                    <h5 class="fw-bold" style="color: #2e3760;">Computer Vision &amp; CCTV</h5>
                    <p class="text-muted small">Edge video telemetry for crowd analysis, perimeter boundary breach detection, and automated vehicle license plate recognition (ANPR).</p>
                </div>
            </div>
            <div class="col-md-4 mb-4">
                <div class="card h-100 p-4 border-0 shadow-sm" style="border-radius: 12px; border: 1px solid #e2e8f0 !important;">
                    <div class="mb-3 text-success"><i class="fas fa-file-invoice fa-2x"></i></div>
                    <h5 class="fw-bold" style="color: #2e3760;">Automated Document OCR</h5>
                    <p class="text-muted small">Intelligent character recognition for Bengali and English scripts, extracting structured metadata from citizen applications and court records.</p>
                </div>
            </div>
            <div class="col-md-4 mb-4">
                <div class="card h-100 p-4 border-0 shadow-sm" style="border-radius: 12px; border: 1px solid #e2e8f0 !important;">
                    <div class="mb-3 text-warning"><i class="fas fa-chart-line fa-2x"></i></div>
                    <h5 class="fw-bold" style="color: #2e3760;">Anomaly Detection Engines</h5>
                    <p class="text-muted small">Real-time fraud detection, duplicate subsidy claim auditing, and statistical risk modeling across nationwide registries.</p>
                </div>
            </div>
        </div>
    </div>

    <!-- SECTION: CALL TO ACTION -->
    <div class="container-fluid py-5 cta-banner-section">
        <div class="container text-center py-4 position-relative" style="z-index: 2;">
            <span class="badge px-3 py-2 rounded-pill fw-semibold mb-3" style="background: rgba(242, 101, 34, 0.2); color: #f26522; border: 1px solid rgba(242, 101, 34, 0.4); font-size: 13px;">Applied Machine Intelligence</span>
            <h2 class="display-6 fw-bold text-white mb-3">Accelerate Your Operations with Applied AI</h2>
            <p class="text-light opacity-75 mx-auto mb-4" style="max-width: 650px; font-size: 16px; line-height: 1.7;">
                Consult with Spectrum's machine learning architects to build secure, sovereign cognitive systems tailored to your mission.
            </p>
            <div class="d-flex justify-content-center align-items-center flex-wrap gap-3 pt-2">
                <a href="contact.html" class="cta-primary-btn">
                    <i class="fas fa-paper-plane me-2"></i> Contact AI Engineering
                </a>
                <a href="tel:+8801615900004" class="cta-secondary-btn">
                    <i class="fas fa-phone-alt me-2 text-warning"></i> +8801615900004
                </a>
            </div>
        </div>
    </div>

{COMMON_FOOTER}
</body>
</html>"""

with open(os.path.join(DIR, 'Artificial_Intelligence.html'), 'w', encoding='utf-8') as f:
    f.write(ai_content)
with open(os.path.join(DIR, 'ai.html'), 'w', encoding='utf-8') as f:
    f.write(ai_content)
print("Artificial_Intelligence.html & ai.html updated.")

# 8. GENERATE ABOUT_US.HTML (FULL CHAIRMAN SPEECH ON TOP, MISSION/VISION, PRESERVED ALL DETAILS)
about_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
{get_head(
    title="About Spectrum IT Solutions Ltd., Dhaka | Executive Leadership &amp; History",
    description="Discover Spectrum IT Solutions Ltd. - Over 12+ years delivering sovereign digital transformation, biometric identity, and mission-critical software engineering. Meet our Chairman Kabir Ahmed Bhuiyan.",
    canonical_slug="about_us.html",
    og_image="assets/img/chairman_Sir.png"
)}
</head>
<body>
{COMMON_TOP_BAR}
{get_navbar('about')}

    <!-- Page Hero Banner -->
    <div class="page-hero-banner">
        <div class="container position-relative text-center">
            <div class="breadcrumb-pill">
                <a href="index.html"><i class="fas fa-home me-1"></i> Home</a>
                <span class="opacity-50">/</span>
                <span style="color: #f26522; font-weight: 600;">About Us</span>
            </div>
            <h1>About <span>Spectrum</span></h1>
            <p class="hero-desc">
                Over a decade of leadership in digital transformation, sovereign identity systems, and nation-building enterprise engineering.
            </p>
            <div class="hero-features">
                <span class="hero-feature-item">
                    <i class="fas fa-award" style="color: #f26522;"></i> 12+ Years Proven Delivery
                </span>
                <span class="hero-feature-item">
                    <i class="fas fa-certificate" style="color: #4ade80;"></i> ISO 9001:2015 &amp; ISO 27001:2022
                </span>
                <span class="hero-feature-item">
                    <i class="fas fa-handshake" style="color: #38bdf8;"></i> BASIS Member &amp; National Partner
                </span>
                <span class="hero-feature-item">
                    <i class="fas fa-globe" style="color: #fbbf24;"></i> Dhaka, Bangladesh &amp; Global Delivery
                </span>
            </div>
        </div>
    </div>

    <!-- SECTION 1: MEET OUR CHAIRMAN (FULL SPEECH & BIOGRAPHY ON TOP) -->
    <div class="container py-5" id="chairman">
        <div class="text-center mb-5">
            <span class="badge px-3 py-2 rounded-pill fw-semibold mb-2" style="background: rgba(242, 101, 34, 0.1); color: #f26522; border: 1px solid rgba(242, 101, 34, 0.25); font-size: 13px;">Corporate Leadership</span>
            <h2 class="header_two" style="color: #2e3760; font-size: 38px; font-weight: 700;">Meet Our <span style="color: #f26522;">Chairman</span></h2>
            <h4 class="fw-bold text-dark mt-1" style="font-size: 26px;">Kabir Ahmed Bhuiyan</h4>
            <p class="text-muted mx-auto" style="max-width: 650px;">Visionary Leader in Technology, Humanity, and Global Development</p>
        </div>

        <div class="row align-items-start">
            <!-- Left: Profile & Credentials -->
            <div class="col-lg-4 col-md-5 mb-4 mb-lg-0">
                <div class="chairman-profile-card text-center">
                    <picture><source srcset="assets/img/chairman_Sir.webp" type="image/webp"><img src="assets/img/chairman_Sir.png" alt="Kabir Ahmed Bhuiyan, Chairman" loading="lazy" class="img-fluid mb-3"></picture>
                    <h4 class="fw-bold mb-1" style="color: #2e3760;">Kabir Ahmed Bhuiyan</h4>
                    <p class="text-muted small mb-2">Chairman, Spectrum IT Solutions Ltd.</p>
                    <span class="chairman-badge"><i class="fas fa-globe-americas me-1"></i> International Envoy of Humanity</span>
                    
                    <div class="chairman-social-links my-3">
                        <a href="https://www.facebook.com/kabhuiyanbd" target="_blank" rel="noopener" title="Facebook"><i class="fab fa-facebook-f"></i></a>
                        <a href="https://www.linkedin.com/in/kabir-ahmed-bhuiyan-0a631a108/" target="_blank" rel="noopener" title="LinkedIn"><i class="fab fa-linkedin-in"></i></a>
                        <a href="mailto:chairman@spectrum.com.bd" title="Email"><i class="fas fa-envelope"></i></a>
                    </div>

                    <div class="text-start border-top pt-3 mt-3">
                        <div class="small text-muted mb-2"><strong class="text-dark"><i class="fas fa-building text-warning me-2"></i>Global Leadership:</strong></div>
                        <p class="small text-muted mb-2">Managing Director: Bhuiyan Group UK Limited, Bhuiyan International, Bhuiyan Real Estate UK Limited &amp; Balance.</p>
                        <div class="small text-muted mb-2"><strong class="text-dark"><i class="fas fa-heart text-danger me-2"></i>Philanthropy:</strong></div>
                        <p class="small text-muted mb-0">Bhuiyan Global Foundation supporting nationwide social advancement &amp; healthcare.</p>
                    </div>
                </div>
            </div>

            <!-- Right: Full Speech & Biography -->
            <div class="col-lg-8 col-md-7">
                <!-- Main Intro -->
                <div class="speech-block">
                    <h5><i class="fas fa-quote-left text-warning"></i> A Visionary Leader in Technology &amp; Global Development</h5>
                    <p class="mb-3">
                        <strong>Kabir Ahmed Bhuiyan</strong> is a distinguished and visionary leader in Bangladesh’s technology sector. He is the Chairman of Spectrum IT Solutions Limited, a company that—under his dynamic leadership—has been delivering world-class software solutions, enterprise technology, and digital transformation services to clients across both local and international markets. His leadership philosophy rests on three guiding principles: innovation, strategic foresight, and an unwavering commitment to excellence.
                    </p>
                    <p>
                        Beyond technology, Mr. Bhuiyan has made profound contributions to trade, humanitarian advancement, and socio-economic development in Bangladesh and on the global stage. Widely recognized as the “International Envoy of Humanity,” he is an entrepreneur, philanthropist, and political figure admired for his patriotism, compassion, and multidimensional development initiatives.
                    </p>
                </div>

                <!-- Humanitarian Diplomacy -->
                <div class="speech-block">
                    <h5><i class="fas fa-hand-holding-heart text-danger"></i> Humanitarian Diplomacy</h5>
                    <p>
                        During the global COVID-19 pandemic in 2020, Mr. Bhuiyan spearheaded nationwide humanitarian relief, distributing medical supplies, food, and protective equipment throughout Brahmanbaria district and other regions of Bangladesh. His humanitarian diplomacy extended internationally when Senator Abiola Ajimobi, the Governor of Oyo State in Nigeria, contracted COVID-19. At the request of the Nigerian government, he played a pivotal role in facilitating the supply of a Bangladeshi-produced medicine. With the intervention of Bangladesh’s Foreign Minister, Dr. A. K. Abdul Momen, the medicine and protective equipment were dispatched to Nigeria on a special government-arranged flight. This episode stands as a proud chapter in Bangladesh’s international engagement.
                    </p>
                </div>

                <!-- Championing the Blue Gold Economy -->
                <div class="speech-block">
                    <h5><i class="fas fa-water text-primary"></i> Championing the &ldquo;Blue Gold Economy&rdquo;</h5>
                    <p>
                        Mr. Bhuiyan firmly believes that Bangladesh’s vast freshwater reserves can position the nation as a global hub of the “Blue Gold Economy.” Through policy papers, speeches, and published articles, he has consistently advocated for bottled water exports, water diplomacy, and investments in climate-resilient infrastructure.
                    </p>
                </div>

                <!-- Commitment to Sustainability -->
                <div class="speech-block">
                    <h5><i class="fas fa-leaf text-success"></i> Commitment to Sustainability and Energy Transition</h5>
                    <p>
                        Alongside water resource advocacy, he is deeply engaged in addressing air pollution and climate change. He has advanced forward-looking policy recommendations on sustainable energy use, urban greening, and the expansion of renewable energy. His collaborations with international research institutions and environmental organizations underscore his commitment to sustainable global development.
                    </p>
                </div>

                <!-- Global Partnerships -->
                <div class="speech-block">
                    <h5><i class="fas fa-globe-asia text-info"></i> Global Partnerships and Development Initiatives</h5>
                    <p class="mb-3">
                        With strong ties to political leaders, business communities, and policymakers across Europe, Africa, and beyond, Mr. Bhuiyan actively leverages these relationships to strengthen Bangladesh’s trade and diplomatic partnerships worldwide.
                    </p>
                    <p>
                        Through the Bhuiyan Global Foundation, he supports social development initiatives, while his diversified business ventures span garments, real estate, information technology, and international trade. Additionally, through Gelence, he facilitates cross-border investment and government-focused solution initiatives.
                    </p>
                </div>

                <!-- Multifaceted Leadership -->
                <div class="speech-block">
                    <h5><i class="fas fa-network-wired text-secondary"></i> Multifaceted Leadership</h5>
                    <p>
                        In addition to his business and philanthropic pursuits, Mr. Bhuiyan is actively engaged in advancing education, healthcare, environmental protection, and water resource management in Bangladesh. He also serves as the Managing Director of Bhuiyan Group UK Limited, Bhuiyan International, Bhuiyan Real Estate UK Limited, and Balance. Through these enterprises, he has cultivated long-term collaborations with global investors, business leaders, and policymakers.
                    </p>
                </div>

                <!-- Executive Summary -->
                <div class="speech-summary-card">
                    <p>
                        <i class="fas fa-star text-warning me-2"></i> In summary, <strong>Kabir Ahmed Bhuiyan</strong> is a bridge-builder between technology, humanity, and international trade. His vision and initiatives are not only shaping Bangladesh’s future but also unlocking new opportunities on the global stage.
                    </p>
                </div>
            </div>
        </div>
    </div>

    <!-- SECTION 2: MISSION & VISION (ORIGINAL TEXT & MISSION_BG) -->
    <div class="container-fluid abt_pg_mission py-5 position-relative" style="background-image: url('assets/img/mission_bg.png'); background-size: cover; background-position: center;">
        <div class="container py-4">
            <div class="text-center mb-5">
                <span class="badge px-3 py-2 rounded-pill fw-semibold mb-2" style="background: rgba(255, 255, 255, 0.15); color: #fff; border: 1px solid rgba(255, 255, 255, 0.3); font-size: 13px;">Our Core Philosophy</span>
                <h2 class="display-6 fw-bold text-white">Mission &amp; Vision</h2>
            </div>
            <div class="row g-4 align-items-stretch">
                <!-- Mission -->
                <div class="col-lg-6 reveal-on-scroll">
                    <div class="abt-mission-box">
                        <div class="d-flex align-items-center mb-3">
                            <div class="mission-icon-wrap me-3">
                                <picture>
                                    <source srcset="assets/img/mission.webp" type="image/webp">
                                    <img src="assets/img/mission.png" alt="Our Mission">
                                </picture>
                            </div>
                            <h3 class="mb-0">Our Mission</h3>
                        </div>
                        <p>
                            Our mission at <strong>Spectrum IT Solutions Limited</strong> is to deliver secure, smart, and innovative technology solutions that simplify processes, enhance transparency, and improve service delivery across all sectors. We are dedicated to supporting the national vision of “Digital Bangladesh” by building inclusive digital systems that empower citizens, strengthen institutions, and promote sustainable development. Through continuous innovation, strategic partnerships, and a commitment to excellence, we aim to transform how technology serves people and organizations—making services faster, smarter, and more accessible for everyone.
                        </p>
                    </div>
                </div>

                <!-- Vision -->
                <div class="col-lg-6 reveal-on-scroll">
                    <div class="abt-mission-box">
                        <div class="d-flex align-items-center mb-3">
                            <div class="mission-icon-wrap me-3">
                                <picture>
                                    <source srcset="assets/img/vission.webp" type="image/webp">
                                    <img src="assets/img/vission.png" alt="Our Vision">
                                </picture>
                            </div>
                            <h3 class="mb-0">Our Vision</h3>
                        </div>
                        <p>
                            Our vision at <strong>Spectrum IT Solutions Limited</strong> is to be a leading force in shaping a digitally advanced and inclusive Bangladesh. We aspire to revolutionize the way public and private services are delivered by harnessing the power of secure, intelligent, and user-friendly technology.<br><br>
                            By building sustainable digital ecosystems, we aim to bridge the gap between people and services—ensuring transparency, efficiency, and accessibility for all. We envision a future where innovation drives national development, and every citizen benefits from the opportunities of a truly connected, smart nation.
                        </p>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- SECTION 3: ABOUT US & WHAT WE DO (FULL DETAILS PRESERVED) -->
    <div class="container py-5">
        <!-- About Us Detail -->
        <div class="row align-items-center mb-5 pb-5 border-bottom">
            <div class="col-lg-6 mb-4 mb-lg-0 text-center">
                <img src="assets/img/about_us_3.png" alt="Spectrum Technology Expertise" class="img-fluid rounded-3 shadow-sm" style="max-height: 420px;">
            </div>
            <div class="col-lg-6">
                <span class="badge px-3 py-2 rounded-pill fw-semibold mb-2" style="background: rgba(30, 126, 52, 0.1); color: #1e7e34; border: 1px solid rgba(30, 126, 52, 0.25); font-size: 13px;">Corporate Overview</span>
                <h2 class="header_two" style="color: #2e3760; font-size: 34px; font-weight: 700;">About Us</h2>
                <h5 class="fw-bold mb-3" style="color: #f26522;">Highly Tailored Technology, Development &amp; Support Services</h5>
                <p class="text-muted" style="line-height: 1.8; font-size: 15px;">
                    We are a software development company delivering splendid business IT Solutions and related services to customers at home &amp; abroad. Our development services are led by our dedicated and passionate team to provide the best industry practices combined with technology expertise and business knowledge to drive the digital transformation. Founded in 2012 on a solid foundation of honest family values, we have built lasting relationships that have kept us on the cutting edge of innovation ever since.
                </p>
                <p class="text-muted" style="line-height: 1.8; font-size: 15px;">
                    Our main area of expertise is <strong>Software Development, Biometric Authentication Systems, Digital Identity &amp; Security Systems, Smart Card Personalization &amp; Printing Solutions, Web &amp; Mobile Application Development, Payment Gateway &amp; API Integration, E-commerce, Tracking Systems, Social Media Marketing, Email marketing, SMS marketing</strong>, and nationwide managed services.
                </p>
            </div>
        </div>

        <!-- What We Do Detail -->
        <div class="row align-items-center">
            <div class="col-lg-6 mb-4 mb-lg-0 order-lg-last text-center">
                <picture><source srcset="assets/img/about_us_office.webp" type="image/webp"><img src="assets/img/about_us_office.png" alt="Spectrum Engineering Headquarters" loading="lazy" class="img-fluid rounded-3 shadow-sm" style="max-height: 400px;"></picture>
            </div>
            <div class="col-lg-6">
                <span class="badge px-3 py-2 rounded-pill fw-semibold mb-2" style="background: rgba(242, 101, 34, 0.1); color: #f26522; border: 1px solid rgba(242, 101, 34, 0.25); font-size: 13px;">Operational Capabilities</span>
                <h2 class="header_two" style="color: #2e3760; font-size: 34px; font-weight: 700;">What We Do</h2>
                <h5 class="fw-bold mb-3" style="color: #f26522;">Building Value Through Collaboration, Insight &amp; Expertise</h5>
                <p class="text-muted" style="line-height: 1.8; font-size: 15px;">
                    <strong>Spectrum IT Solutions Limited</strong> is a leading technology firm based in Dhaka, Bangladesh, dedicated to delivering innovative and secure IT solutions across government, non-government, and private sectors. With a strong focus on national development and digital transformation, Spectrum specializes in developing scalable software applications, biometric authentication systems, and smart card-based platforms. Their expertise spans web and mobile app development, ERP systems, IoT integration, secure database management, cloud-based infrastructure, and custom e-Governance platforms.
                </p>
                <p class="text-muted" style="line-height: 1.8; font-size: 15px;">
                    The company has played a key role in building impactful systems such as the <strong>Industrial e-Court System, the TCB Smart Family Card Platform, National Biometric Attendance Services</strong>, and various <strong>e-Licensing portals</strong>. Spectrum also provides consulting, technical training, and long-term system maintenance, ensuring end-to-end service delivery.
                </p>
            </div>
        </div>
    </div>

    <!-- SECTION 4: PROVEN MILESTONES & COUNTERS -->
    <div class="container-fluid py-5" style="background: #f8fafc; border-top: 1px solid #e2e8f0; border-bottom: 1px solid #e2e8f0;">
        <div class="container text-center">
            <div class="row g-4 justify-content-center">
                <div class="col-lg-3 col-sm-6 text-center">
                    <div class="counter-stat-card text-center">
                        <img src="assets/img/icon_1.png" alt="Projects Completed">
                        <div class="text-center w-100">
                            <h3 class="text-center">118</h3>
                            <span class="text-center">Projects Completed</span>
                        </div>
                    </div>
                </div>
                <div class="col-lg-3 col-sm-6 text-center">
                    <div class="counter-stat-card text-center">
                        <img src="assets/img/icon_2.png" alt="Happy Clients">
                        <div class="text-center w-100">
                            <h3 class="text-center">115</h3>
                            <span class="text-center">Happy Clients</span>
                        </div>
                    </div>
                </div>
                <div class="col-lg-3 col-sm-6 text-center">
                    <div class="counter-stat-card text-center">
                        <img src="assets/img/icon_3.png" alt="Business Partners">
                        <div class="text-center w-100">
                            <h3 class="text-center">23</h3>
                            <span class="text-center">Business Partners</span>
                        </div>
                    </div>
                </div>
                <div class="col-lg-3 col-sm-6 text-center">
                    <div class="counter-stat-card text-center">
                        <img src="assets/img/icon_4.png" alt="IT Consultants">
                        <div class="text-center w-100">
                            <h3 class="text-center">21</h3>
                            <span class="text-center">IT Consultants</span>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- SECTION 5: VALUABLE CLIENTS -->
    <div class="container py-5 text-center">
        <span class="badge px-3 py-2 rounded-pill fw-semibold mb-2 d-inline-block text-center" style="background: rgba(30, 126, 52, 0.1); color: #1e7e34; border: 1px solid rgba(30, 126, 52, 0.25); font-size: 13px;">Trusted Partnerships</span>
        <h2 class="header_two mb-4 text-center" style="color: #2e3760; font-size: 34px; font-weight: 700; text-align: center !important;">Our Valuable Clients</h2>
        <div class="row g-4 justify-content-center pt-2">
            <div class="col-lg-4 col-md-4 col-6">
                <div class="client-logo-card">
                    <img src="assets/img/vlc_01.jpg" alt="Valuable Client 1">
                </div>
            </div>
            <div class="col-lg-4 col-md-4 col-6">
                <div class="client-logo-card">
                    <img src="assets/img/vlc_02.jpg" alt="Valuable Client 2">
                </div>
            </div>
            <div class="col-lg-4 col-md-4 col-6">
                <div class="client-logo-card">
                    <img src="assets/img/vlc_03.jpg" alt="Valuable Client 3">
                </div>
            </div>
            <div class="col-lg-4 col-md-4 col-6">
                <div class="client-logo-card">
                    <img src="assets/img/vlc_04.jpg" alt="Valuable Client 4">
                </div>
            </div>
            <div class="col-lg-4 col-md-4 col-6">
                <div class="client-logo-card">
                    <img src="assets/img/vlc_05.jpg" alt="Valuable Client 5">
                </div>
            </div>
            <div class="col-lg-4 col-md-4 col-6">
                <div class="client-logo-card">
                    <img src="assets/img/vlc_06.jpg" alt="Valuable Client 6">
                </div>
            </div>
        </div>
    </div>

    <!-- SECTION: CALL TO ACTION -->
    <div class="container-fluid py-5 cta-banner-section">
        <div class="container text-center py-4 position-relative" style="z-index: 2;">
            <span class="badge px-3 py-2 rounded-pill fw-semibold mb-3" style="background: rgba(242, 101, 34, 0.2); color: #f26522; border: 1px solid rgba(242, 101, 34, 0.4); font-size: 13px;">Over Two Decades of Excellence</span>
            <h2 class="display-6 fw-bold text-white mb-3">Partner with Bangladesh&rsquo;s Sovereign Tech Pioneer</h2>
            <p class="text-light opacity-75 mx-auto mb-4" style="max-width: 650px; font-size: 16px; line-height: 1.7;">
                Delivering high-reliability digital governance, biometric security, and mission-critical software engineering since 2000.
            </p>
            <div class="d-flex justify-content-center align-items-center flex-wrap gap-3 pt-2">
                <a href="contact.html" class="cta-primary-btn">
                    <i class="fas fa-paper-plane me-2"></i> Work with Us
                </a>
                <a href="case-study.html" class="cta-secondary-btn">
                    <i class="fas fa-folder-open me-2"></i> View Case Studies
                </a>
            </div>
        </div>
    </div>

{COMMON_FOOTER}
</body>
</html>"""

with open(os.path.join(DIR, 'about_us.html'), 'w', encoding='utf-8') as f:
    f.write(about_content)
with open(os.path.join(DIR, 'About Us.html'), 'w', encoding='utf-8') as f:
    f.write(about_content)
print("about_us.html & About Us.html updated.")

# 9. GENERATE PRODUCTS.HTML & SCT.HTML
products_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
{get_head(
    title="Enterprise Products | Hardware &amp; Software Solutions | Spectrum IT Solutions Ltd.",
    description="Discover Spectrum IT Solutions enterprise products: Smart Card Printers, Biometric Terminals, Access Control, Kiosks, CCTV, GPS Trackers, ERP, and e-KYC platforms.",
    canonical_slug="products.html",
    og_image="assets/img/sm-card-about.png"
)}
</head>
<body>
{COMMON_TOP_BAR}
{get_navbar('products')}

    <!-- Page Hero Banner -->
    <div class="page-hero-banner">
        <div class="container position-relative text-center">
            <div class="breadcrumb-pill">
                <a href="index.html"><i class="fas fa-home me-1"></i> Home</a>
                <span class="opacity-50">/</span>
                <span style="color: #f26522; font-weight: 600;">Products</span>
            </div>
            <h1>Our <span>Products</span></h1>
            <p class="hero-desc">
                Field-proven hardware systems, high-security smart card personalization printers, certified biometric devices, and mission-critical enterprise software platforms engineered for sovereign reliability.
            </p>
            <div class="hero-features">
                <span class="hero-feature-item">
                    <i class="fas fa-id-card" style="color: #4ade80;"></i> Smart Card &amp; Printers
                </span>
                <span class="hero-feature-item">
                    <i class="fas fa-fingerprint" style="color: #f26522;"></i> Certified Biometrics
                </span>
                <span class="hero-feature-item">
                    <i class="fas fa-tv" style="color: #38bdf8;"></i> Kiosks &amp; Signage
                </span>
                <span class="hero-feature-item">
                    <i class="fas fa-video" style="color: #fbbf24;"></i> Surveillance &amp; Telemetry
                </span>
                <span class="hero-feature-item">
                    <i class="fas fa-cubes" style="color: #a78bfa;"></i> Enterprise Software
                </span>
            </div>
        </div>
    </div>

    <!-- SECTION 1: TURNKEY HARDWARE & SPECIALIZED SYSTEMS (8 CORE PRODUCTS) -->
    <div class="container pt-5 pb-3">
        <div class="text-center mb-4">
            <span class="badge px-3 py-2 rounded-pill fw-semibold mb-2" style="background: rgba(242, 101, 34, 0.1); color: #f26522; border: 1px solid rgba(242, 101, 34, 0.25); font-size: 13px;">Turnkey Hardware Systems</span>
            <h2 class="header_two" style="color: #2e3760; font-size: 36px; font-weight: 700;">Hardware &amp; <span style="color: #f26522;">Specialized Devices</span></h2>
            <p class="text-muted mx-auto mb-4" style="max-width: 680px; font-size: 15px;">Industrial-grade, ruggedized hardware solutions deployed across national governance platforms, financial institutions, and enterprise facilities.</p>

            <!-- Interactive Category Filter Tabs (Single Line Segmented Group) -->
            <div class="filter-nav-wrap">
                <button class="filter-btn active" data-filter="all">
                    <i class="fas fa-layer-group"></i> All <span class="badge-count">12</span>
                </button>
                <button class="filter-btn" data-filter="hardware">
                    <i class="fas fa-microchip"></i> Hardware <span class="badge-count">8</span>
                </button>
                <button class="filter-btn" data-filter="software">
                    <i class="fas fa-code"></i> Software <span class="badge-count">4</span>
                </button>
            </div>
        </div>
    </div>

    <div class="container pb-5 filter-section">
        <div class="row g-4">
            <!-- Product 1: Smart Card & Printer -->
            <div class="col-lg-3 col-md-6 col-sm-6 filter-item reveal-on-scroll" data-category="hardware">
                <div class="product-card-modern">
                    <div>
                        <div class="product-icon-wrap">
                            <img src="assets/img/icon_Smart_Card_Technologies.png" alt="Smart Card &amp; Printer">
                        </div>
                        <div class="text-center">
                            <span class="product-cat">Personalization</span>
                        </div>
                        <h4>Smart Card &amp; Printer</h4>
                        <p>High-definition retransfer and direct-to-card smart card printers, dual-interface chip encoding, and secure holographic lamination.</p>
                        <ul class="product-specs-list">
                            <li><i class="fas fa-check-circle"></i> Retransfer &amp; Direct-to-Card</li>
                            <li><i class="fas fa-check-circle"></i> Contact &amp; Contactless RFID</li>
                            <li><i class="fas fa-check-circle"></i> High-Speed Batch Issuance</li>
                        </ul>
                    </div>
                    <div class="pt-3 text-center">
                        <a href="Smart_Card_Technologies.html" class="button">read more</a>
                    </div>
                </div>
            </div>

            <!-- Product 2: Time Attendance Systems -->
            <div class="col-lg-3 col-md-6 col-sm-6 filter-item reveal-on-scroll" data-category="hardware">
                <div class="product-card-modern">
                    <div>
                        <div class="product-icon-wrap">
                            <img src="assets/img/icon_Time_Attendance.png" alt="Time Attendance Systems">
                        </div>
                        <div class="text-center">
                            <span class="product-cat">Workforce Security</span>
                        </div>
                        <h4>Time Attendance</h4>
                        <p>Optical fingerprint and AI facial recognition terminals featuring standalone operation, battery backup, and encrypted cloud sync.</p>
                        <ul class="product-specs-list">
                            <li><i class="fas fa-check-circle"></i> Face &amp; Fingerprint Auth</li>
                            <li><i class="fas fa-check-circle"></i> Standalone Battery Backup</li>
                            <li><i class="fas fa-check-circle"></i> Real-time Cloud Push SDK</li>
                        </ul>
                    </div>
                    <div class="pt-3 text-center">
                        <a href="contact.html" class="button">read more</a>
                    </div>
                </div>
            </div>

            <!-- Product 3: Access Control Solutions -->
            <div class="col-lg-3 col-md-6 col-sm-6 filter-item reveal-on-scroll" data-category="hardware">
                <div class="product-card-modern">
                    <div>
                        <div class="product-icon-wrap">
                            <img src="assets/img/icon_Smart_Access_Control.png" alt="Access Control Solutions">
                        </div>
                        <div class="text-center">
                            <span class="product-cat">Physical Security</span>
                        </div>
                        <h4>Access Control</h4>
                        <p>Smart turnstiles, optical flap barriers, electromagnetic locks, and multi-factor biometric/RFID facility controllers.</p>
                        <ul class="product-specs-list">
                            <li><i class="fas fa-check-circle"></i> Anti-Tailgating Speed Gates</li>
                            <li><i class="fas fa-check-circle"></i> Multi-Factor Biometric Access</li>
                            <li><i class="fas fa-check-circle"></i> Fire Alarm &amp; Emergency Release</li>
                        </ul>
                    </div>
                    <div class="pt-3 text-center">
                        <a href="contact.html" class="button">read more</a>
                    </div>
                </div>
            </div>

            <!-- Product 4: Digital Signage -->
            <div class="col-lg-3 col-md-6 col-sm-6 filter-item reveal-on-scroll" data-category="hardware">
                <div class="product-card-modern">
                    <div>
                        <div class="product-icon-wrap">
                            <img src="assets/img/icon_eSign_Solutions.png" alt="Digital Signage">
                        </div>
                        <div class="text-center">
                            <span class="product-cat">Display Solutions</span>
                        </div>
                        <h4>Digital Signage</h4>
                        <p>Centralized networked signage systems with ultra-HD commercial displays, remote content scheduling, and multi-zone split playback.</p>
                        <ul class="product-specs-list">
                            <li><i class="fas fa-check-circle"></i> 4K Commercial Grade Displays</li>
                            <li><i class="fas fa-check-circle"></i> Centralized Web CMS</li>
                            <li><i class="fas fa-check-circle"></i> Multi-Zone Layouts &amp; Tickers</li>
                        </ul>
                    </div>
                    <div class="pt-3 text-center">
                        <a href="contact.html" class="button">read more</a>
                    </div>
                </div>
            </div>

            <!-- Product 5: Self-Service Kiosk -->
            <div class="col-lg-3 col-md-6 col-sm-6 filter-item reveal-on-scroll" data-category="hardware">
                <div class="product-card-modern">
                    <div>
                        <div class="product-icon-wrap">
                            <img src="assets/img/icon_Kiosk.png" alt="Self-Service Kiosk">
                        </div>
                        <div class="text-center">
                            <span class="product-cat">Interactive Terminals</span>
                        </div>
                        <h4>Self-Service Kiosk</h4>
                        <p>Rugged interactive touch kiosks equipped with industrial thermal ticket printers, QR scanners, payment readers, and fingerprint sensors.</p>
                        <ul class="product-specs-list">
                            <li><i class="fas fa-check-circle"></i> Capacitive Multi-Touch Screen</li>
                            <li><i class="fas fa-check-circle"></i> Integrated Thermal Printer &amp; QR</li>
                            <li><i class="fas fa-check-circle"></i> Vandal-Proof Steel Enclosure</li>
                        </ul>
                    </div>
                    <div class="pt-3 text-center">
                        <a href="contact.html" class="button">read more</a>
                    </div>
                </div>
            </div>

            <!-- Product 6: Biometric Devices -->
            <div class="col-lg-3 col-md-6 col-sm-6 filter-item reveal-on-scroll" data-category="hardware">
                <div class="product-card-modern">
                    <div>
                        <div class="product-icon-wrap">
                            <img src="assets/img/icon_Biometric_Technologiest.png" alt="Biometric Devices">
                        </div>
                        <div class="text-center">
                            <span class="product-cat">Identity Hardware</span>
                        </div>
                        <h4>Biometric Devices</h4>
                        <p>FBI PIV and STQC certified USB optical &amp; capacitive fingerprint scanners, dual-iris cameras, live-finger detection, and NID readers.</p>
                        <ul class="product-specs-list">
                            <li><i class="fas fa-check-circle"></i> FBI PIV &amp; STQC Certified</li>
                            <li><i class="fas fa-check-circle"></i> Fake Finger &amp; LFD Protection</li>
                            <li><i class="fas fa-check-circle"></i> Multi-OS SDK (Win/Linux/Android)</li>
                        </ul>
                    </div>
                    <div class="pt-3 text-center">
                        <a href="Digital_Identity_&_Security.html" class="button">read more</a>
                    </div>
                </div>
            </div>

            <!-- Product 7: CCTV & Surveillance Cameras -->
            <div class="col-lg-3 col-md-6 col-sm-6 filter-item reveal-on-scroll" data-category="hardware">
                <div class="product-card-modern">
                    <div>
                        <div class="product-icon-wrap">
                            <img src="assets/img/icon_cc_camera.png" alt="CCTV &amp; Surveillance Cameras">
                        </div>
                        <div class="text-center">
                            <span class="product-cat">Perimeter Security</span>
                        </div>
                        <h4>CCTV Camera</h4>
                        <p>High-definition IP surveillance cameras with starlight night vision, motorized optical zoom, vandal-proof IP67 domes, and AI analytics.</p>
                        <ul class="product-specs-list">
                            <li><i class="fas fa-check-circle"></i> 4K UHD Starlight Imaging</li>
                            <li><i class="fas fa-check-circle"></i> 50m Smart IR &amp; IP67 Housing</li>
                            <li><i class="fas fa-check-circle"></i> AI Motion &amp; Perimeter Alert</li>
                        </ul>
                    </div>
                    <div class="pt-3 text-center">
                        <a href="contact.html" class="button">read more</a>
                    </div>
                </div>
            </div>

            <!-- Product 8: GPS & IoT Tracker -->
            <div class="col-lg-3 col-md-6 col-sm-6 filter-item reveal-on-scroll" data-category="hardware">
                <div class="product-card-modern">
                    <div>
                        <div class="product-icon-wrap">
                            <img src="assets/img/icon_Tracking.png" alt="GPS &amp; IoT Tracker">
                        </div>
                        <div class="text-center">
                            <span class="product-cat">Telemetry Hardware</span>
                        </div>
                        <h4>Tracker</h4>
                        <p>Real-time vehicle and mobile asset tracking units featuring GSM/GPS dual-satellite positioning, anti-jamming, and remote engine cut-off.</p>
                        <ul class="product-specs-list">
                            <li><i class="fas fa-check-circle"></i> High-Precision GPS/GLONASS</li>
                            <li><i class="fas fa-check-circle"></i> Remote Engine Immobilization</li>
                            <li><i class="fas fa-check-circle"></i> Fuel Sensor &amp; Geofence Alerts</li>
                        </ul>
                    </div>
                    <div class="pt-3 text-center">
                        <a href="contact.html" class="button">read more</a>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- SECTION 2: ENTERPRISE SOFTWARE SUITES -->
    <div class="container-fluid py-5 filter-section" style="background: #f8fafc; border-top: 1px solid #e2e8f0; border-bottom: 1px solid #e2e8f0;">
        <div class="container">
            <div class="text-center mb-5">
                <span class="badge px-3 py-2 rounded-pill fw-semibold mb-2" style="background: rgba(30, 126, 52, 0.1); color: #1e7e34; border: 1px solid rgba(30, 126, 52, 0.25); font-size: 13px;">Software Platforms</span>
                <h2 class="header_two" style="color: #2e3760; font-size: 36px; font-weight: 700;">Enterprise <span style="color: #f26522;">Software Suites</span></h2>
                <p class="text-muted mx-auto" style="max-width: 680px; font-size: 15px;">Battle-tested digital platforms designed for high-concurrency public service delivery, corporate operations, and national identity ecosystems.</p>
            </div>

            <div class="row g-4">
                <!-- Suite 1: Spectrum Enterprise ERP -->
                <div class="col-lg-3 col-md-6 col-sm-6 filter-item reveal-on-scroll" data-category="software">
                    <div class="product-card-modern">
                        <div>
                            <div class="product-icon-wrap">
                                <img src="assets/img/icon_ERP.png" alt="Enterprise ERP">
                            </div>
                            <div class="text-center">
                                <span class="product-cat">Operations &amp; ERP</span>
                            </div>
                            <h4>Enterprise ERP</h4>
                            <p>Integrated financial accounting, procurement, HR, payroll, supply chain, and asset management suite designed for corporate and institutional scale.</p>
                            <ul class="product-specs-list">
                                <li><i class="fas fa-check-circle"></i> Financials &amp; Double-Entry Audit</li>
                                <li><i class="fas fa-check-circle"></i> Automated Payroll &amp; Tax Engine</li>
                                <li><i class="fas fa-check-circle"></i> Multi-Warehouse Inventory</li>
                            </ul>
                        </div>
                        <div class="pt-3 text-center">
                            <a href="contact.html" class="button">read more</a>
                        </div>
                    </div>
                </div>

                <!-- Suite 2: Spectrum e-KYC Suite -->
                <div class="col-lg-3 col-md-6 col-sm-6 filter-item reveal-on-scroll" data-category="software">
                    <div class="product-card-modern">
                        <div>
                            <div class="product-icon-wrap">
                                <img src="assets/img/icon_Digital_Identity_Security.png" alt="e-KYC Suite">
                            </div>
                            <div class="text-center">
                                <span class="product-cat">Digital Trust</span>
                            </div>
                            <h4>Spectrum e-KYC</h4>
                            <p>Instant citizen verification and NID validation SDK with biometric facial match, passive liveness detection, and Porichoy API interoperability.</p>
                            <ul class="product-specs-list">
                                <li><i class="fas fa-check-circle"></i> Instant National NID Verification</li>
                                <li><i class="fas fa-check-circle"></i> Passive Biometric Liveness Check</li>
                                <li><i class="fas fa-check-circle"></i> Banking Grade AML/CFT Compliance</li>
                            </ul>
                        </div>
                        <div class="pt-3 text-center">
                            <a href="Digital_Identity_&_Security.html" class="button">read more</a>
                        </div>
                    </div>
                </div>

                <!-- Suite 3: Smart City & IoT Platform -->
                <div class="col-lg-3 col-md-6 col-sm-6 filter-item reveal-on-scroll" data-category="software">
                    <div class="product-card-modern">
                        <div>
                            <div class="product-icon-wrap">
                                <img src="assets/img/icon_Smart_City_Solutions.png" alt="Smart City &amp; IoT Platform">
                            </div>
                            <div class="text-center">
                                <span class="product-cat">Urban Infrastructure</span>
                            </div>
                            <h4>Smart City IoT</h4>
                            <p>Centralized municipal command and control platform integrating smart street lighting, traffic telemetry, environmental sensors, and incident dispatching.</p>
                            <ul class="product-specs-list">
                                <li><i class="fas fa-check-circle"></i> GIS Real-Time Sensor Telemetry</li>
                                <li><i class="fas fa-check-circle"></i> Automated Incident Dispatch</li>
                                <li><i class="fas fa-check-circle"></i> Open IoT Protocols (MQTT/CoAP)</li>
                            </ul>
                        </div>
                        <div class="pt-3 text-center">
                            <a href="contact.html" class="button">read more</a>
                        </div>
                    </div>
                </div>

                <!-- Suite 4: AI Computer Vision Suite -->
                <div class="col-lg-3 col-md-6 col-sm-6 filter-item reveal-on-scroll" data-category="software">
                    <div class="product-card-modern">
                        <div>
                            <div class="product-icon-wrap">
                                <img src="assets/img/icon_Artificial_Intelligence.png" alt="AI Computer Vision Suite">
                            </div>
                            <div class="text-center">
                                <span class="product-cat">Applied AI</span>
                            </div>
                            <h4>AI Vision Suite</h4>
                            <p>Deep-learning video analytics engine for real-time crowd density estimation, automated license plate recognition (ALPR), and perimeter breach alerts.</p>
                            <ul class="product-specs-list">
                                <li><i class="fas fa-check-circle"></i> License Plate Recognition (ALPR)</li>
                                <li><i class="fas fa-check-circle"></i> Real-Time Crowd &amp; Queue Analytics</li>
                                <li><i class="fas fa-check-circle"></i> Edge Device &amp; Cloud Inference</li>
                            </ul>
                        </div>
                        <div class="pt-3 text-center">
                            <a href="Artificial_Intelligence.html" class="button">read more</a>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- SECTION 3: ENGINEERING ASSURANCE & COMPLIANCE -->
    <div class="container py-5">
        <div class="row align-items-center">
            <div class="col-lg-5 mb-4 mb-lg-0 text-center text-lg-start">
                <span class="badge px-3 py-2 rounded-pill fw-semibold mb-2" style="background: rgba(46, 55, 96, 0.1); color: #2e3760; border: 1px solid rgba(46, 55, 96, 0.2); font-size: 13px;">Spectrum Assurance</span>
                <h2 class="header_two" style="color: #2e3760; font-size: 34px; font-weight: 700;">Engineered for <span style="color: #f26522;">Mission-Critical</span> Reliability</h2>
                <p class="text-muted" style="line-height: 1.8; font-size: 15px;">
                    Every product delivered by Spectrum IT Solutions complies with stringent international engineering standards. We provide end-to-end integration support, custom firmware development, and locally stationed technical support teams across Bangladesh.
                </p>
                <div class="pt-2 text-center text-lg-start">
                    <a href="contact.html" class="button">Request Product Catalog</a>
                </div>
            </div>
            <div class="col-lg-7">
                <div class="row g-3">
                    <div class="col-sm-6">
                        <div class="p-4 bg-white rounded-3 shadow-sm border h-100">
                            <div class="d-flex align-items-center mb-3">
                                <div class="rounded-circle p-3 me-3 d-flex align-items-center justify-content-center" style="background: rgba(30, 126, 52, 0.1); width: 50px; height: 50px;">
                                    <i class="fas fa-certificate text-success fa-lg"></i>
                                </div>
                                <h5 class="fw-bold mb-0" style="color: #2e3760; font-size: 17px;">Certified Compliance</h5>
                            </div>
                            <p class="text-muted small mb-0">ISO 9001:2015 and ISO 27001:2013 certified processes. Hardware meets CE, FCC, and FBI PIV standards.</p>
                        </div>
                    </div>
                    <div class="col-sm-6">
                        <div class="p-4 bg-white rounded-3 shadow-sm border h-100">
                            <div class="d-flex align-items-center mb-3">
                                <div class="rounded-circle p-3 me-3 d-flex align-items-center justify-content-center" style="background: rgba(242, 101, 34, 0.1); width: 50px; height: 50px;">
                                    <i class="fas fa-tools text-warning fa-lg"></i>
                                </div>
                                <h5 class="fw-bold mb-0" style="color: #2e3760; font-size: 17px;">24/7 SLA Support</h5>
                            </div>
                            <p class="text-muted small mb-0">Dedicated Dhaka technical lab, ready replacement units, and nationwide SLA maintenance engineers.</p>
                        </div>
                    </div>
                    <div class="col-sm-6">
                        <div class="p-4 bg-white rounded-3 shadow-sm border h-100">
                            <div class="d-flex align-items-center mb-3">
                                <div class="rounded-circle p-3 me-3 d-flex align-items-center justify-content-center" style="background: rgba(59, 130, 246, 0.1); width: 50px; height: 50px;">
                                    <i class="fas fa-code text-primary fa-lg"></i>
                                </div>
                                <h5 class="fw-bold mb-0" style="color: #2e3760; font-size: 17px;">SDK &amp; Driver Support</h5>
                            </div>
                            <p class="text-muted small mb-0">Comprehensive SDKs, REST APIs, and native drivers for seamless integration with existing software.</p>
                        </div>
                    </div>
                    <div class="col-sm-6">
                        <div class="p-4 bg-white rounded-3 shadow-sm border h-100">
                            <div class="d-flex align-items-center mb-3">
                                <div class="rounded-circle p-3 me-3 d-flex align-items-center justify-content-center" style="background: rgba(168, 85, 247, 0.1); width: 50px; height: 50px;">
                                    <i class="fas fa-shield-alt text-purple fa-lg" style="color: #8b5cf6;"></i>
                                </div>
                                <h5 class="fw-bold mb-0" style="color: #2e3760; font-size: 17px;">Sovereign Security</h5>
                            </div>
                            <p class="text-muted small mb-0">Air-gapped deployment, local data residency, and zero foreign cloud dependencies for sensitive data.</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- SECTION 4: CALL TO ACTION -->
    <div class="container-fluid py-5 cta-banner-section">
        <div class="container text-center py-4 position-relative" style="z-index: 2;">
            <span class="badge px-3 py-2 rounded-pill fw-semibold mb-3" style="background: rgba(242, 101, 34, 0.2); color: #f26522; border: 1px solid rgba(242, 101, 34, 0.4); font-size: 13px;">Ready to Modernize Your Operations?</span>
            <h2 class="display-6 fw-bold text-white mb-3">Need Custom Specifications or a Volume Quote?</h2>
            <p class="text-light opacity-75 mx-auto mb-4" style="max-width: 650px; font-size: 16px; line-height: 1.7;">
                Our technical solutions team provides free hardware evaluations, RFP compliance matrices, and on-site demonstrations across Bangladesh.
            </p>
            <div class="d-flex justify-content-center align-items-center flex-wrap gap-3 pt-2">
                <a href="contact.html" class="cta-primary-btn">
                    <i class="fas fa-paper-plane me-2"></i> Contact Engineering
                </a>
                <a href="tel:+8801615900004" class="cta-secondary-btn">
                    <i class="fas fa-phone-alt me-2 text-warning"></i> +8801615900004
                </a>
            </div>
        </div>
    </div>

{COMMON_FOOTER}
</body>
</html>"""

with open(os.path.join(DIR, 'products.html'), 'w', encoding='utf-8') as f:
    f.write(products_content)
with open(os.path.join(DIR, 'Products.html'), 'w', encoding='utf-8') as f:
    f.write(products_content)
print("products.html & Products.html updated.")

sct_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
{get_head(
    title="Smart Card Technologies &amp; Personalization | Spectrum IT Solutions",
    description="Turnkey smart card personalization, dual-interface chip encoding, laser engraving, and automated kiosk platforms by Spectrum IT Solutions.",
    canonical_slug="Smart_Card_Technologies.html",
    og_image="assets/img/banner_img_03.jpg"
)}
</head>
<body>
{COMMON_TOP_BAR}
{get_navbar('services')}

    <!-- Page Hero Banner -->
    <div class="page-hero-banner">
        <div class="container position-relative text-center">
            <div class="breadcrumb-pill">
                <a href="index.html"><i class="fas fa-home me-1"></i> Home</a>
                <span class="opacity-50">/</span>
                <a href="services.html">Services</a>
                <span class="opacity-50">/</span>
                <span style="color: #f26522; font-weight: 600;">Smart Card Technologies</span>
            </div>
            <h1>Smart Card <span>Technologies</span></h1>
            <p class="hero-desc">
                State-of-the-art contact &amp; contactless smart card personalization, cryptographic chip encoding, and automated hardware issuance platforms.
            </p>
            <div class="hero-features">
                <span class="hero-feature-item">
                    <i class="fas fa-id-card" style="color: #4ade80;"></i> ISO 7816 &amp; 14443 A/B
                </span>
                <span class="hero-feature-item">
                    <i class="fas fa-microchip" style="color: #38bdf8;"></i> Cryptographic SAM Injection
                </span>
                <span class="hero-feature-item">
                    <i class="fas fa-bolt" style="color: #f26522;"></i> Laser Engraving &amp; Encoding
                </span>
                <span class="hero-feature-item">
                    <i class="fas fa-print" style="color: #fbbf24;"></i> High-Throughput Kiosks
                </span>
            </div>
        </div>
    </div>

    <!-- SCT Content -->
    <div class="container py-5">
        <div class="row align-items-center mb-5">
            <div class="col-lg-6 mb-4 mb-lg-0">
                <h2 class="fw-bold mb-3" style="color: #2e3760;">High-Security Card Personalization</h2>
                <p class="text-muted" style="line-height: 1.8;">
                    Spectrum delivers high-throughput smart card personalization platforms compliant with ISO 7816 and ISO 14443 Type A/B standards. Our systems support laser engraving, magnetic stripe encoding, cryptographic key injection, and secure chip personalization for driving licenses, national identity cards, and transit cards.
                </p>
                <div class="row pt-2">
                    <div class="col-6 mb-3">
                        <div class="p-3 border rounded bg-light text-center">
                            <h4 class="fw-bold text-success mb-1">ISO 7816</h4>
                            <small class="text-muted">Contact Chip Standard</small>
                        </div>
                    </div>
                    <div class="col-6 mb-3">
                        <div class="p-3 border rounded bg-light text-center">
                            <h4 class="fw-bold text-success mb-1">ISO 14443</h4>
                            <small class="text-muted">Contactless RFID/NFC</small>
                        </div>
                    </div>
                </div>
            </div>
            <div class="col-lg-6 text-center">
                <picture><source srcset="assets/img/sm-card-about.webp" type="image/webp"><img src="assets/img/sm-card-about.png" alt="Smart Card Personalization" loading="lazy" class="img-fluid rounded shadow-sm" style="max-height: 380px;"></picture>
            </div>
        </div>

        <!-- Capability Cards -->
        <div class="row pt-2">
            <div class="col-md-4 mb-4">
                <div class="card h-100 p-4 border-0 shadow-sm" style="border-radius: 12px; border: 1px solid #e2e8f0 !important;">
                    <div class="mb-3 text-warning"><i class="fas fa-microchip fa-2x"></i></div>
                    <h5 class="fw-bold" style="color: #2e3760;">Chip Encoding &amp; SAM</h5>
                    <p class="text-muted small">High-speed dual-interface encoding with Hardware Security Module (HSM) integration for cryptographic key generation and PKI signing.</p>
                </div>
            </div>
            <div class="col-md-4 mb-4">
                <div class="card h-100 p-4 border-0 shadow-sm" style="border-radius: 12px; border: 1px solid #e2e8f0 !important;">
                    <div class="mb-3 text-success"><i class="fas fa-award fa-2x"></i></div>
                    <h5 class="fw-bold" style="color: #2e3760;">Laser &amp; Tactile Engraving</h5>
                    <p class="text-muted small">Sub-surface fiber laser marking, tactile relief, and MLI/CLI optical variable devices ensuring physical anti-counterfeiting.</p>
                </div>
            </div>
            <div class="col-md-4 mb-4">
                <div class="card h-100 p-4 border-0 shadow-sm" style="border-radius: 12px; border: 1px solid #e2e8f0 !important;">
                    <div class="mb-3 text-primary"><i class="fas fa-desktop fa-2x"></i></div>
                    <h5 class="fw-bold" style="color: #2e3760;">Automated Issuance Kiosks</h5>
                    <p class="text-muted small">Unattended instant card delivery kiosks with integrated biometrics, document scanners, payment POS, and audit logs.</p>
                </div>
            </div>
        </div>
    </div>

    <!-- SECTION: CALL TO ACTION -->
    <div class="container-fluid py-5 cta-banner-section">
        <div class="container text-center py-4 position-relative" style="z-index: 2;">
            <span class="badge px-3 py-2 rounded-pill fw-semibold mb-3" style="background: rgba(242, 101, 34, 0.2); color: #f26522; border: 1px solid rgba(242, 101, 34, 0.4); font-size: 13px;">Turnkey Hardware &amp; Encoding</span>
            <h2 class="display-6 fw-bold text-white mb-3">Plan Your Smart Card Infrastructure</h2>
            <p class="text-light opacity-75 mx-auto mb-4" style="max-width: 650px; font-size: 16px; line-height: 1.7;">
                Partner with Spectrum IT Solutions for turnkey hardware supply, secure chip operating systems, and nationwide field maintenance.
            </p>
            <div class="d-flex justify-content-center align-items-center flex-wrap gap-3 pt-2">
                <a href="contact.html" class="cta-primary-btn">
                    <i class="fas fa-paper-plane me-2"></i> Request Hardware Quote
                </a>
                <a href="products.html" class="cta-secondary-btn">
                    <i class="fas fa-microchip me-2"></i> Browse Products
                </a>
            </div>
        </div>
    </div>

{COMMON_FOOTER}
</body>
</html>"""

with open(os.path.join(DIR, 'Smart_Card_Technologies.html'), 'w', encoding='utf-8') as f:
    f.write(sct_content)
with open(os.path.join(DIR, 'sct.html'), 'w', encoding='utf-8') as f:
    f.write(sct_content)
print("Smart_Card_Technologies.html & sct.html updated.")


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

# 11. GENERATE SITEMAP.XML & ROBOTS.TXT & LLMS.TXT (Audit #8, #113)
sitemap_content = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url><loc>https://spectrum.com.bd/index.html</loc><priority>1.0</priority></url>
  <url><loc>https://spectrum.com.bd/about_us.html</loc><priority>0.8</priority></url>
  <url><loc>https://spectrum.com.bd/services.html</loc><priority>0.9</priority></url>
  <url><loc>https://spectrum.com.bd/products.html</loc><priority>0.8</priority></url>
  <url><loc>https://spectrum.com.bd/projects.html</loc><priority>0.8</priority></url>
  <url><loc>https://spectrum.com.bd/case-study.html</loc><priority>0.8</priority></url>
  <url><loc>https://spectrum.com.bd/contact.html</loc><priority>0.8</priority></url>
  <url><loc>https://spectrum.com.bd/Digital_Identity_&amp;_Security.html</loc><priority>0.7</priority></url>
  <url><loc>https://spectrum.com.bd/Smart_Card_Technologies.html</loc><priority>0.7</priority></url>
  <url><loc>https://spectrum.com.bd/Artificial_Intelligence.html</loc><priority>0.7</priority></url>
</urlset>"""

with open(os.path.join(DIR, 'sitemap.xml'), 'w', encoding='utf-8') as f:
    f.write(sitemap_content)

robots_content = """User-agent: *
Allow: /
Sitemap: https://spectrum.com.bd/sitemap.xml
"""

with open(os.path.join(DIR, 'robots.txt'), 'w', encoding='utf-8') as f:
    f.write(robots_content)

llms_content = """# Spectrum IT Solutions Ltd.
> Premier Dhaka-based software company providing digital identity, biometric infrastructure, smart card platforms, AI systems, and national-scale software engineering.

## Key pages
- [Home](https://spectrum.com.bd/index.html): Homepage with overview of capabilities
- [About](https://spectrum.com.bd/about_us.html): Company background, 12+ years experience, ISO 9001 & ISO 27001
- [Services](https://spectrum.com.bd/services.html): Digital identity, smart cards, AI, cybersecurity, ERP
- [Digital Identity & Security](https://spectrum.com.bd/Digital_Identity_&_Security.html): National biometric identity and automated ID verification
- [Smart Card Technologies](https://spectrum.com.bd/Smart_Card_Technologies.html): Turnkey smart card personalization, encoding & kiosks
- [Artificial Intelligence](https://spectrum.com.bd/Artificial_Intelligence.html): Computer vision, cognitive OCR, and decision models
- [Products](https://spectrum.com.bd/products.html): Enterprise hardware and software products
- [Projects](https://spectrum.com.bd/projects.html): Delivered government and corporate projects
- [Case Studies](https://spectrum.com.bd/case-study.html): TCB Smart Family Card, Industrial e-Court BD
- [Contact](https://spectrum.com.bd/contact.html): Enquiries and consultations

## Contact
- Email: contact@spectrum.com.bd
- Phone: +8801615900004
- Address: 52/1, New Eskaton Road (Hasan Holdings Ltd., 12th Floor), Dhaka-1000, Bangladesh
"""

with open(os.path.join(DIR, 'llms.txt'), 'w', encoding='utf-8') as f:
    f.write(llms_content)

print("All pages and SEO files successfully generated!")
