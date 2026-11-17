/**
 * Spectrum IT Solutions Ltd. - Reusable Web Components
 * Zero-dependency Custom Elements for <site-header> and <site-footer>.
 */

class SiteHeader extends HTMLElement {
    connectedCallback() {
        this.innerHTML = `
    <header>
    <!-- Start Top bar -->
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
    <!-- Close Top bar -->
    <!-- Header -->
    <nav class="navbar navbar-expand-lg navbar-light shadow sticky-top pt-3 pb-3">
        <div class="container d-flex align-items-center justify-content-between">
            <div class="d-flex align-items-center">
                <div class="logo">
                    <a class="navbar-brand text-success align-self-center m-0 p-0" href="./">
                        <img src="assets/img/logo.png" width="165" height="60" alt="Spectrum IT Solutions Logo">
                    </a>
                </div>
                <div class="iso d-none d-lg-flex align-items-center ms-3">
                    <img src="assets/img/ISO_9001.png" width="70" height="75" alt="ISO 9001:2015" class="me-1">
                    <img src="assets/img/ISO_27001.png" width="70" height="75" alt="ISO 27001:2022">
                </div>
            </div>

            <button class="navbar-toggler d-lg-none border-0 ms-auto collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#main_nav" aria-controls="main_nav" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>

            <div class="collapse navbar-collapse flex-fill d-lg-flex justify-content-lg-between" id="main_nav">
                <div class="flex-fill">
                    <ul class="nav navbar-nav d-flex menu_list justify-content-center">
                        <li class="nav-item">
                            <a class="nav-link" href="about-us.html">About Us</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="services.html">Services</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="products.html">Products</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="projects.html">Projects</a>
                        </li>
                        <li class="nav-item dropdown">
                            <a class="nav-link dropdown-toggle" href="case-study.html" id="caseStudyDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                                Case Study
                            </a>
                            <ul class="dropdown-menu shadow-sm" aria-labelledby="caseStudyDropdown">
                                <li><a class="dropdown-item" href="case-study.html"><i class="fas fa-layer-group me-2 text-warning"></i> All Case Studies</a></li>
                                <li><hr class="dropdown-divider my-1"></li>
                                <li><a class="dropdown-item" href="case-study-tcb.html"><i class="fas fa-id-card me-2 text-success"></i> TCB Smart Card</a></li>
                                <li class="d-none"><!-- Hidden while ecourt.gov.bd is offline (not deleted). Remove "d-none" to show it again. --><a class="dropdown-item" href="case-study-e-court.html"><i class="fas fa-gavel me-2 text-primary"></i> Industrial e-Court</a></li>
                                <li><a class="dropdown-item" href="case-study-e-licensing.html"><i class="fas fa-file-contract me-2 text-info"></i> National e-Licensing</a></li>
                                <li><a class="dropdown-item" href="case-study-smart-card.html"><i class="fas fa-print me-2 text-warning"></i> Smart Card Issuance</a></li>
                                <li><a class="dropdown-item" href="case-study-ocd.html"><i class="fas fa-calendar-check me-2 text-info"></i> Officers’ Club Dhaka</a></li>
                                <li><a class="dropdown-item" href="case-study-tcb-contact-center.html"><i class="fas fa-headset me-2 text-success"></i> TCB AI Contact Center</a></li>
                                <li><a class="dropdown-item" href="case-study-novotheatre.html"><i class="fas fa-ticket-alt me-2 text-warning"></i> Novotheatre eTicket</a></li>
                                <li><a class="dropdown-item" href="case-study-gcc.html"><i class="fas fa-landmark me-2 text-success"></i> Gazipur City Corporation</a></li>
                                <li><a class="dropdown-item" href="case-study-apfs.html"><i class="fas fa-user-clock me-2 text-primary"></i> Automated Presence &amp; Feedback</a></li>
                            </ul>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="contact.html">Contact</a>
                        </li>
                    </ul>
                </div>
                
                <div class="ms-lg-3">
                    <div class="free_con d-flex align-items-center">
                        <i class="fa fa-phone-alt mx-2 text-warning"></i>
                        <div>
                            <span>Free Consultation</span><br>
                            <a href="tel:+8801615900004" style="color: inherit; text-decoration: none;"><strong>+880 1615-900004</strong></a>
                        </div>
                    </div>
                </div>

                <div class="d-lg-none text-center pt-3 pb-2 border-top mt-3">
                    <img width="26" height="28" src="assets/img/ISO_9001.png" alt="ISO 9001:2015" class="me-2" style="height: 28px;" loading="lazy">
                    <img width="26" height="28" src="assets/img/ISO_27001.png" alt="ISO 27001:2022" style="height: 28px;" loading="lazy">
                </div>
            </div>
        </div>
    </nav>
    </header>`;

        const servicePages = new Set([
            'services.html',
            'ai-contact-center.html',
            'anti-counterfeit.html',
            'artificial-intelligence.html',
            'blockchain-technology.html',
            'brand-protection.html',
            'business-automation.html',
            'digital-identity-security.html',
            'mobile-apps.html',
            'smart-card-technologies.html',
            'upokari.html'
        ]);

        const currentFile = window.location.pathname.split('/').pop() || 'index.html';
        let activeHref = this.getAttribute('active');

        if (!activeHref) {
            if (servicePages.has(currentFile)) {
                activeHref = 'services.html';
            } else if (currentFile.startsWith('case-study')) {
                activeHref = 'case-study.html';
            } else if (currentFile !== 'index.html' && currentFile !== '404.html') {
                activeHref = currentFile;
            }
        }

        if (activeHref) {
            const navLink = this.querySelector(`.nav-link[href="${activeHref}"]`);
            if (navLink) {
                navLink.classList.add('active');
            }
        }
    }
}

class SiteFooter extends HTMLElement {
    connectedCallback() {
        this.innerHTML = `
    <footer>
    <div class="footer-wrapper">
        <div class="container">
            <div class="row">
                <div class="col-lg-3 col-sm-6 mb-4 footer-col-about">
                    <div class="footer-about">
                        <a href="./"><img src="assets/img/logo.png" width="165" height="60" class="img-fluid mb-3" alt="Spectrum IT Solutions Logo" loading="lazy"></a>
                        <p>A Dhaka software company building secure digital services for government and business since 2012.</p>
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
                        <li class="mb-2 d-none"><!-- Hidden while ecourt.gov.bd is offline (not deleted). Remove "d-none" to show it again. --><a href="http://www.ecourt.gov.bd/" target="_blank" rel="noopener" class="text-light text-decoration-none"><i class="fas fa-angle-right me-1 text-warning"></i> www.ecourt.gov.bd</a></li>
                        <li class="mb-2"><a href="https://novo.spectrum.com.bd/" target="_blank" rel="noopener" class="text-light text-decoration-none"><i class="fas fa-angle-right me-1 text-warning"></i> www.sobticket.com</a></li>
                    </ul>
                </div>

                <div class="col-lg-3 col-sm-6 mb-4 footer-col-links">
                    <h3 class="text-white mb-3" style="font-size: 1.25rem;">Quick Link</h3>
                    <ul class="list-unstyled">
                        <li class="mb-2"><a href="artificial-intelligence.html" class="text-light text-decoration-none"><i class="fas fa-angle-right me-1 text-warning"></i> Artificial Intelligence</a></li>
                        <li class="mb-2"><a href="digital-identity-security.html" class="text-light text-decoration-none"><i class="fas fa-angle-right me-1 text-warning"></i> Digital Identity &amp; Security</a></li>
                        <li class="mb-2"><a href="smart-card-technologies.html" class="text-light text-decoration-none"><i class="fas fa-angle-right me-1 text-warning"></i> Smart Card Technologies</a></li>
                        <li class="mb-2"><a href="blockchain-technology.html" class="text-light text-decoration-none"><i class="fas fa-angle-right me-1 text-warning"></i> Blockchain Technology</a></li>
                        <li class="mb-2"><a href="about-us.html" class="text-light text-decoration-none"><i class="fas fa-angle-right me-1 text-warning"></i> About Us</a></li>
                        <li class="mb-2"><a href="services.html" class="text-light text-decoration-none"><i class="fas fa-angle-right me-1 text-warning"></i> Our Services</a></li>
                        <li class="mb-2"><a href="products.html" class="text-light text-decoration-none"><i class="fas fa-angle-right me-1 text-warning"></i> Our Products</a></li>
                        <li class="mb-2"><a href="contact.html" class="text-light text-decoration-none"><i class="fas fa-angle-right me-1 text-warning"></i> Contact Us</a></li>
                    </ul>
                </div>

                <div class="col-lg-3 col-sm-6 mb-4 footer-col-contact">
                    <h3 class="text-white mb-3" style="font-size: 1.25rem;">Contact Us</h3>
                    <p class="text-light mb-2"><i class="fas fa-map-marker-alt me-2 text-warning"></i> 52/1, New Eskaton Road (Hasan Holdings Ltd., 12th Floor), Dhaka-1000, Bangladesh</p>
                    <p class="text-light mb-2"><i class="fas fa-envelope me-2 text-warning"></i> <a href="mailto:contact@spectrum.com.bd" class="text-light text-decoration-none">contact@spectrum.com.bd</a></p>
                    <p class="text-light mb-2"><i class="fas fa-phone-alt me-2 text-warning"></i> <a href="tel:+8801615900004" class="text-light text-decoration-none">+880 1615-900004</a></p>
                </div>
            </div>

            <!-- Copyright section with same background inside footer-wrapper -->
            <div class="footer-copyright">
                <p class="mb-0">Copyright &copy; 2026 <a href="./" style="color: #f26522; text-decoration: none;"><strong>Spectrum IT Solutions Ltd.</strong></a> All Rights Reserved.</p>
                <p class="mb-0 footer-legal"><a href="privacy-policy.html">Privacy Policy</a><span aria-hidden="true">&middot;</span><a href="terms.html">Terms of Use</a></p>
            </div>
        </div>
    </div>
    </footer>`;
    }
}

customElements.define('site-header', SiteHeader);
customElements.define('site-footer', SiteFooter);
