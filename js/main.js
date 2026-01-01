// 페이지 로드시 실행
document.addEventListener('DOMContentLoaded', () => {
    initLanguageSelector();
    initMobileMenu();
    initSmoothScroll();
    initScrollAnimations();
    initNavbarScroll();
    initIntersectionObserver();
    initAOS();
});

// 언어 선택기 초기화
function initLanguageSelector() {
    const langToggle = document.getElementById('langToggle');
    const langDropdown = document.getElementById('langDropdown');
    const langOptions = document.querySelectorAll('.lang-option');
    const currentLangSpan = document.querySelector('.current-lang');
    
    if (!langToggle || !langDropdown) return;
    
    // 자동 언어 감지
    function detectBrowserLanguage() {
        const browserLang = navigator.language || navigator.userLanguage;
        const langCode = browserLang.toLowerCase();
        
        // 브라우저 언어를 사이트 언어로 매핑
        if (langCode.startsWith('ko')) return 'ko';
        if (langCode.startsWith('ja')) return 'ja';
        if (langCode.startsWith('zh')) return 'zh';
        return 'en'; // 기본값 영어
    }
    
    // URL 파라미터에서 언어 가져오기
    function getLanguageFromURL() {
        const params = new URLSearchParams(window.location.search);
        return params.get('lang');
    }
    
    // 저장된 언어 또는 자동 감지
    function getInitialLanguage() {
        // 1순위: URL 파라미터
        const urlLang = getLanguageFromURL();
        if (urlLang && ['ko', 'en', 'ja', 'zh'].includes(urlLang)) {
            return urlLang;
        }
        
        // 2순위: localStorage
        const savedLang = localStorage.getItem('preferredLanguage');
        if (savedLang && ['ko', 'en', 'ja', 'zh'].includes(savedLang)) {
            return savedLang;
        }
        
        // 3순위: 브라우저 자동 감지
        return detectBrowserLanguage();
    }
    
    // 초기 언어 설정
    const initialLang = getInitialLanguage();
    if (initialLang && window.changeLanguage) {
        window.changeLanguage(initialLang);
    }
    
    // 토글 버튼 클릭
    langToggle.addEventListener('click', (e) => {
        e.stopPropagation();
        langToggle.classList.toggle('active');
        langDropdown.classList.toggle('show');
    });
    
    // 언어 옵션 클릭
    langOptions.forEach(option => {
        option.addEventListener('click', (e) => {
            e.stopPropagation();
            const lang = option.dataset.lang;
            
            // 언어 변경
            if (window.changeLanguage) {
                window.changeLanguage(lang);
            }
            
            // localStorage에 저장
            localStorage.setItem('preferredLanguage', lang);
            
            // 활성화 상태 업데이트
            langOptions.forEach(opt => opt.classList.remove('active'));
            option.classList.add('active');
            
            // 현재 언어 표시 업데이트
            const langCode = option.querySelector('.lang-code').textContent;
            currentLangSpan.textContent = langCode;
            
            // 드롭다운 닫기
            langToggle.classList.remove('active');
            langDropdown.classList.remove('show');
        });
    });
    
    // 외부 클릭시 드롭다운 닫기
    document.addEventListener('click', () => {
        langToggle.classList.remove('active');
        langDropdown.classList.remove('show');
    });
    
    // 드롭다운 내부 클릭시 전파 중지
    langDropdown.addEventListener('click', (e) => {
        e.stopPropagation();
    });
}

// 모바일 메뉴 토글
function initMobileMenu() {
    const toggle = document.querySelector('.mobile-menu-toggle');
    const menu = document.querySelector('.nav-menu');
    
    if (!toggle || !menu) return;
    
    toggle.addEventListener('click', () => {
        toggle.classList.toggle('active');
        menu.classList.toggle('active');
        document.body.style.overflow = menu.classList.contains('active') ? 'hidden' : '';
    });
    
    // 메뉴 항목 클릭시 모바일 메뉴 닫기
    document.querySelectorAll('.nav-menu a').forEach(link => {
        link.addEventListener('click', () => {
            if (window.innerWidth <= 968) {
                toggle.classList.remove('active');
                menu.classList.remove('active');
                document.body.style.overflow = '';
            }
        });
    });
}

// 부드러운 스크롤
function initSmoothScroll() {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            const href = this.getAttribute('href');
            
            // 빈 앵커나 #만 있는 경우 제외
            if (!href || href === '#') return;
            
            const target = document.querySelector(href);
            if (!target) return;
            
            e.preventDefault();
            
            const navbarHeight = document.querySelector('.navbar').offsetHeight;
            const targetPosition = target.offsetTop - navbarHeight;
            
            window.scrollTo({
                top: targetPosition,
                behavior: 'smooth'
            });
        });
    });
}

// 스크롤 애니메이션
function initScrollAnimations() {
    const animateOnScroll = () => {
        const elements = document.querySelectorAll('.about-card, .service-card, .doctor-content, .contact-grid');
        
        elements.forEach(element => {
            const elementTop = element.getBoundingClientRect().top;
            const windowHeight = window.innerHeight;
            
            if (elementTop < windowHeight * 0.85) {
                element.style.opacity = '1';
                element.style.transform = 'translateY(0)';
            }
        });
    };
    
    // 초기 스타일 설정
    document.querySelectorAll('.about-card, .service-card, .doctor-content, .contact-grid').forEach(element => {
        element.style.opacity = '0';
        element.style.transform = 'translateY(30px)';
        element.style.transition = 'opacity 0.6s ease-out, transform 0.6s ease-out';
    });
    
    // 스크롤 이벤트
    window.addEventListener('scroll', throttle(animateOnScroll, 100));
    animateOnScroll(); // 초기 실행
}

// 네비게이션 스크롤 효과
function initNavbarScroll() {
    const navbar = document.querySelector('.navbar');
    if (!navbar) return;
    
    let lastScroll = 0;
    
    window.addEventListener('scroll', throttle(() => {
        const currentScroll = window.pageYOffset;
        
        if (currentScroll > 100) {
            navbar.style.padding = '12px 0';
            navbar.style.boxShadow = '0 4px 16px rgba(0, 0, 0, 0.1)';
        } else {
            navbar.style.padding = '16px 0';
            navbar.style.boxShadow = '0 2px 8px rgba(0, 0, 0, 0.08)';
        }
        
        lastScroll = currentScroll;
    }, 100));
}

// Intersection Observer로 섹션 활성화 표시
function initIntersectionObserver() {
    const sections = document.querySelectorAll('section[id]');
    const navLinks = document.querySelectorAll('.nav-menu a[href^="#"]');
    
    const observerOptions = {
        root: null,
        rootMargin: '-50% 0px -50% 0px',
        threshold: 0
    };
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const id = entry.target.getAttribute('id');
                navLinks.forEach(link => {
                    link.classList.remove('active');
                    if (link.getAttribute('href') === `#${id}`) {
                        link.classList.add('active');
                    }
                });
            }
        });
    }, observerOptions);
    
    sections.forEach(section => observer.observe(section));
}

// 성능 최적화를 위한 throttle 함수
function throttle(func, wait) {
    let timeout;
    let lastRan;
    
    return function executedFunction(...args) {
        const context = this;
        
        if (!lastRan) {
            func.apply(context, args);
            lastRan = Date.now();
        } else {
            clearTimeout(timeout);
            timeout = setTimeout(() => {
                if (Date.now() - lastRan >= wait) {
                    func.apply(context, args);
                    lastRan = Date.now();
                }
            }, wait - (Date.now() - lastRan));
        }
    };
}

// 폼 검증 (추후 예약 폼 추가시 사용)
function validateForm(formElement) {
    const inputs = formElement.querySelectorAll('input[required], textarea[required]');
    let isValid = true;
    
    inputs.forEach(input => {
        if (!input.value.trim()) {
            isValid = false;
            input.classList.add('error');
        } else {
            input.classList.remove('error');
        }
    });
    
    return isValid;
}

// 이메일 검증
function isValidEmail(email) {
    const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return re.test(email);
}

// 전화번호 포맷팅 (한국)
function formatPhoneNumber(value) {
    const numbers = value.replace(/\D/g, '');
    
    if (numbers.length <= 3) {
        return numbers;
    } else if (numbers.length <= 7) {
        return numbers.slice(0, 3) + '-' + numbers.slice(3);
    } else if (numbers.length <= 11) {
        return numbers.slice(0, 3) + '-' + numbers.slice(3, 7) + '-' + numbers.slice(7);
    }
    
    return numbers.slice(0, 3) + '-' + numbers.slice(3, 7) + '-' + numbers.slice(7, 11);
}

// 로딩 인디케이터
function showLoading() {
    const loader = document.createElement('div');
    loader.className = 'loading-overlay';
    loader.innerHTML = `
        <div class="loading-spinner">
            <div class="spinner"></div>
        </div>
    `;
    document.body.appendChild(loader);
}

function hideLoading() {
    const loader = document.querySelector('.loading-overlay');
    if (loader) {
        loader.remove();
    }
}

// 토스트 알림
function showToast(message, type = 'info') {
    const toast = document.createElement('div');
    toast.className = `toast toast-${type}`;
    toast.textContent = message;
    
    document.body.appendChild(toast);
    
    setTimeout(() => {
        toast.classList.add('show');
    }, 100);
    
    setTimeout(() => {
        toast.classList.remove('show');
        setTimeout(() => toast.remove(), 300);
    }, 3000);
}

// 페이지 진입 애니메이션
window.addEventListener('load', () => {
    document.body.classList.add('loaded');
});

// 리사이즈 이벤트 최적화
let resizeTimer;
window.addEventListener('resize', () => {
    clearTimeout(resizeTimer);
    resizeTimer = setTimeout(() => {
        // 리사이즈 완료 후 실행할 코드
        const menu = document.querySelector('.nav-menu');
        if (window.innerWidth > 968 && menu) {
            menu.classList.remove('active');
            document.body.style.overflow = '';
        }
    }, 250);
});

// 외부 링크 새 탭으로 열기
document.querySelectorAll('a[href^="http"]').forEach(link => {
    if (!link.href.includes(window.location.hostname)) {
        link.setAttribute('target', '_blank');
        link.setAttribute('rel', 'noopener noreferrer');
    }
});

// 접근성: 키보드 네비게이션
document.addEventListener('keydown', (e) => {
    // ESC 키로 모바일 메뉴 닫기
    if (e.key === 'Escape') {
        const toggle = document.querySelector('.mobile-menu-toggle');
        const menu = document.querySelector('.nav-menu');
        if (menu && menu.classList.contains('active')) {
            toggle.classList.remove('active');
            menu.classList.remove('active');
            document.body.style.overflow = '';
        }
    }
});

// Google Analytics (필요시 활성화)
/*
window.dataLayer = window.dataLayer || [];
function gtag(){dataLayer.push(arguments);}
gtag('js', new Date());
gtag('config', 'GA_MEASUREMENT_ID');
*/

// 이미지 레이지 로딩 폴백 (최신 브라우저는 loading="lazy" 지원)
if ('loading' in HTMLImageElement.prototype === false) {
    document.querySelectorAll('img[loading="lazy"]').forEach(img => {
        img.src = img.src;
    });
}

// AOS (Animate On Scroll) 초기화
function initAOS() {
    const observerOptions = {
        root: null,
        rootMargin: '0px',
        threshold: 0.1
    };
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('aos-animate');
                // 한번 애니메이션 후 관찰 중지
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);
    
    document.querySelectorAll('[data-aos]').forEach(element => {
        observer.observe(element);
    });
}

// 다국어 SEO 메타 태그 동적 업데이트
function updateMetaTags(lang) {
    if (!translations[lang]) return;
    
    // Use translation data for meta tags
    const title = translations[lang].meta_title || translations.ko.meta_title;
    const description = translations[lang].meta_description || translations.ko.meta_description;
    const keywords = translations[lang].meta_keywords || translations.ko.meta_keywords;
    
    // Update document title
    document.title = title;
    
    // Update meta description
    const metaDescElement = document.querySelector('meta[name="description"]');
    if (metaDescElement) {
        metaDescElement.setAttribute('content', description);
    }
    
    // Update meta keywords
    const metaKeywordsElement = document.querySelector('meta[name="keywords"]');
    if (metaKeywordsElement) {
        metaKeywordsElement.setAttribute('content', keywords);
    }
    
    // Update OG title
    const ogTitleElement = document.querySelector('meta[property="og:title"]');
    if (ogTitleElement) {
        ogTitleElement.setAttribute('content', title);
    }
    
    // Update OG description
    const ogDesc = document.querySelector('meta[property="og:description"]');
    if (ogDesc) {
        ogDesc.setAttribute('content', description);
    }
    
    // Update html lang attribute
    document.documentElement.setAttribute('lang', lang);
}

// Export for use in translations.js
window.updateMetaTags = updateMetaTags;
