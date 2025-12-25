// 다국어 번역 데이터
const translations = {
    ko: {
        clinic_name: '연세미다스치과',
        nav_home: '치과소개',
        nav_whitening: '치아미백',
        nav_minish: '미니쉬',
        nav_prosthetics: '심미보철',
        nav_implant: '임플란트',
        nav_equipment: '진료장비',
        nav_contact: '오시는 길',
        
        hero_badge: 'Since 2024',
        hero_title: '당신의 소중한 미소를 위한<br><span class="highlight">최고의 선택</span>',
        hero_subtitle: '연세대학교 출신 전문의의 고품격 치과 진료<br>정직과 신뢰를 바탕으로 한 최상의 서비스',
        hero_cta1: '예약 상담',
        hero_cta2: '진료안내',
        stat1: 'Years Experience',
        stat2: 'Happy Patients',
        stat3: 'Satisfaction',
        scroll_down: 'Scroll Down',
        
        about_tag: 'About Us',
        about_title: '연세미다스치과를<br>소개합니다',
        about_subtitle: '정직과 신뢰를 바탕으로 한 진료, 환자 중심의 맞춤형 치료',
        
        feature1_title: '전문성',
        feature1_desc: '연세대학교 치과대학 졸업<br>대한치과교정학회 인정의',
        feature2_title: '정성',
        feature2_desc: '환자 한 분 한 분<br>정성을 다한 진료',
        feature3_title: '최신 시설',
        feature3_desc: '최첨단 장비와<br>청결한 진료 환경',
        
        services_tag: 'Our Services',
        services_title: '진료 안내',
        services_subtitle: '전문적이고 체계적인 치료 프로그램을 제공합니다',
        
        service1_title: '임플란트',
        service1_desc: '정밀한 진단과 안전한 시술로 자연치아와 같은 기능을 회복합니다',
        service1_feat1: '3D 디지털 임플란트',
        service1_feat2: '원데이 임플란트',
        service1_feat3: '뼈이식 임플란트',
        
        service2_title: '치아교정',
        service2_desc: '개인별 맞춤 교정으로 아름답고 건강한 치열을 만듭니다',
        service2_feat1: '투명교정',
        service2_feat2: '설측교정',
        service2_feat3: '부분교정',
        
        service3_title: '심미치료',
        service3_desc: '라미네이트, 올세라믹 등으로 자신감 있는 미소를 선사합니다',
        service3_feat1: '라미네이트',
        service3_feat2: '올세라믹',
        service3_feat3: '치아미백',
        
        service4_title: '일반진료',
        service4_desc: '충치치료, 신경치료, 잇몸치료 등 기본 진료를 제공합니다',
        service4_feat1: '충치치료',
        service4_feat2: '신경치료',
        service4_feat3: '잇몸치료',
        
        // Service Details
        implant_detail_title: '잃어버린 치아를<br>자연치아처럼',
        implant_detail_desc: '임플란트는 상실된 치아를 대체하는 가장 효과적인 방법입니다. 연세미다스치과는 3D CT 촬영을 통한 정밀 진단과 디지털 임플란트 시스템으로 안전하고 정확한 시술을 제공합니다.',
        implant_feat1_title: '3D 디지털 임플란트',
        implant_feat1_desc: '정밀한 CT 분석으로 최적의 식립 위치 결정',
        implant_feat2_title: '원데이 임플란트',
        implant_feat2_desc: '발치와 동시에 임플란트 식립 가능',
        implant_feat3_title: '뼈이식 임플란트',
        implant_feat3_desc: '뼈가 부족한 경우에도 안전한 시술',
        
        ortho_detail_title: '아름답고 건강한<br>미소를 위한 교정',
        ortho_detail_desc: '치아교정은 단순히 치아를 가지런히 하는 것을 넘어 턱관절, 저작 기능, 안면 균형까지 고려한 종합적인 치료입니다. 개인별 맞춤 진단으로 최적의 결과를 제공합니다.',
        ortho_feat1_title: '투명 교정',
        ortho_feat1_desc: '눈에 띄지 않는 투명 장치로 심미적 교정',
        ortho_feat2_title: '설측 교정',
        ortho_feat2_desc: '치아 안쪽에 장치를 부착하여 완전 은폐',
        ortho_feat3_title: '부분 교정',
        ortho_feat3_desc: '앞니만 단기간에 교정 가능',
        
        cosmetic_detail_title: '자신감 넘치는<br>환한 미소',
        cosmetic_detail_desc: '심미치료는 치아의 색상, 모양, 크기를 개선하여 아름다운 미소를 만드는 치료입니다. 자연스러우면서도 돋보이는 미소를 위해 최선을 다합니다.',
        cosmetic_feat1_title: '라미네이트',
        cosmetic_feat1_desc: '앞니의 색상과 모양을 개선하는 얇은 세라믹',
        cosmetic_feat2_title: '올세라믹',
        cosmetic_feat2_desc: '금속 없는 100% 세라믹 크라운',
        cosmetic_feat3_title: '치아 미백',
        cosmetic_feat3_desc: '안전하고 효과적인 전문가 미백',
        
        general_detail_title: '평생 건강한 치아를<br>위한 기본 진료',
        general_detail_desc: '충치, 신경치료, 잇몸질환 등 치아 건강의 기본이 되는 진료를 제공합니다. 정기적인 검진과 예방 치료로 평생 건강한 치아를 유지하세요.',
        general_feat1_title: '충치 치료',
        general_feat1_desc: '초기 충치부터 심한 충치까지 단계별 치료',
        general_feat2_title: '신경 치료',
        general_feat2_desc: '통증 없는 정밀 신경치료',
        general_feat3_title: '잇몸 치료',
        general_feat3_desc: '치주질환의 예방과 치료',
        
        // Why Choose Us
        why_tag: 'Why Choose Us',
        why_title: '연세미다스치과를<br>선택해야 하는 이유',
        why1_title: '전문의 직접 진료',
        why1_desc: '연세대학교 치과대학 출신 전문의가 모든 환자를 직접 진료합니다',
        why2_title: '1:1 맞춤 진료',
        why2_desc: '환자 개개인의 구강 상태에 맞는 맞춤형 치료 계획을 수립합니다',
        why3_title: '최첨단 장비',
        why3_desc: '3D CT, 디지털 스캐너 등 최신 장비로 정밀한 진단과 치료를 제공합니다',
        why4_title: '철저한 멸균 시스템',
        why4_desc: '국제 기준의 멸균 시스템으로 안전하고 위생적인 진료 환경을 유지합니다',
        
        gallery_tag: 'Gallery',
        gallery_title: 'Before & After',
        gallery_subtitle: '환자분들의 아름다운 변화를 확인하세요',
        
        doctor_tag: 'Medical Staff',
        doctor_title: '대표원장 소개',
        doctor_name: '최은영 대표원장',
        doctor_specialty: '치과 전문의 / 교정 인정의',
        credentials_title: '주요 경력',
        
        cred1: '연세대학교 치과대학 졸업',
        cred2: '한국치과교정연구회 연수',
        cred3: '대한치과교정학회 인정의',
        cred4: '카톨릭대학교 임플란트 연수',
        cred5: '"치예원" 임플란트 과정 연수',
        cred6: '미국 로마린다대학교 치주, 임플란트과 연수',
        cred7: '전) 바른치과 원장',
        cred8: '전) 은평 예치과 대표원장',
        cred9: '전) 연세바른치과 대표원장',
        cred10: '현) 연세미다스치과 대표원장',
        
        contact_tag: 'Contact',
        contact_title: '오시는 길',
        contact_subtitle: '연세미다스치과를 찾아오시는 길을 안내해 드립니다',
        contact_address: '주소',
        contact_phone: '전화',
        contact_hours: '진료시간',
        
        hours_weekday: '평일',
        hours_saturday: '토요일',
        hours_lunch: '점심시간',
        hours_closed: '일요일/공휴일 휴진',
        
        map_placeholder: '지도 영역',
        
        footer_desc: '정직과 신뢰를 바탕으로<br>최상의 치과 진료 서비스를 제공합니다',
        footer_nav: '바로가기',
        footer_info: '정보',
        footer_contact: '연락처',
        footer_privacy: '개인정보처리방침',
        footer_terms: '이용약관'
    },
    
    en: {
        clinic_name: 'Yonsei Midas Dental',
        nav_home: 'About',
        nav_whitening: 'Whitening',
        nav_minish: 'Minish',
        nav_prosthetics: 'Prosthetics',
        nav_implant: 'Implant',
        nav_equipment: 'Equipment',
        nav_contact: 'Location',
        
        hero_badge: 'Since 2024',
        hero_title: 'Your Best Choice<br><span class="highlight">for a Precious Smile</span>',
        hero_subtitle: 'Premium Dental Care by Yonsei University Graduate Specialist<br>Integrity and Trust-Based Excellence',
        hero_cta1: 'Book Now',
        hero_cta2: 'Our Services',
        stat1: 'Years Experience',
        stat2: 'Happy Patients',
        stat3: 'Satisfaction',
        scroll_down: 'Scroll Down',
        
        about_tag: 'About Us',
        about_title: 'Welcome to<br>Yonsei Midas Dental',
        about_subtitle: 'Treatment based on honesty and trust, patient-centered customized care',
        
        feature1_title: 'Expertise',
        feature1_desc: 'Yonsei University Graduate<br>Board Certified Orthodontist',
        feature2_title: 'Care',
        feature2_desc: 'Personalized attention<br>for every patient',
        feature3_title: 'Advanced',
        feature3_desc: 'State-of-the-art equipment<br>& clean environment',
        
        services_tag: 'Our Services',
        services_title: 'Our Services',
        services_subtitle: 'Professional and systematic treatment programs',
        
        service1_title: 'Dental Implants',
        service1_desc: 'Precise diagnosis and safe procedures to restore natural tooth function',
        service1_feat1: '3D Digital Implants',
        service1_feat2: 'One-Day Implants',
        service1_feat3: 'Bone Graft Implants',
        
        service2_title: 'Orthodontics',
        service2_desc: 'Customized orthodontic treatment for beautiful and healthy teeth',
        service2_feat1: 'Clear Aligners',
        service2_feat2: 'Lingual Braces',
        service2_feat3: 'Partial Orthodontics',
        
        service3_title: 'Cosmetic',
        service3_desc: 'Confident smile with laminates and all-ceramic treatments',
        service3_feat1: 'Veneers',
        service3_feat2: 'All-Ceramic',
        service3_feat3: 'Teeth Whitening',
        
        service4_title: 'General',
        service4_desc: 'Comprehensive care including cavity, root canal, and gum treatment',
        service4_feat1: 'Cavity Treatment',
        service4_feat2: 'Root Canal',
        service4_feat3: 'Gum Treatment',
        
        // Service Details
        implant_detail_title: 'Natural-Looking<br>Tooth Replacement',
        implant_detail_desc: 'Dental implants are the most effective way to replace missing teeth. Yonsei Midas Dental provides safe and accurate procedures using 3D CT imaging and digital implant systems.',
        implant_feat1_title: '3D Digital Implants',
        implant_feat1_desc: 'Precise CT analysis for optimal placement',
        implant_feat2_title: 'One-Day Implants',
        implant_feat2_desc: 'Implant placement immediately after extraction',
        implant_feat3_title: 'Bone Graft Implants',
        implant_feat3_desc: 'Safe procedures even with insufficient bone',
        
        ortho_detail_title: 'Beautiful & Healthy<br>Smile Through Orthodontics',
        ortho_detail_desc: 'Orthodontics goes beyond straightening teeth - it considers jaw joints, chewing function, and facial balance for comprehensive treatment. Personalized diagnosis for optimal results.',
        ortho_feat1_title: 'Clear Aligners',
        ortho_feat1_desc: 'Invisible transparent devices for aesthetic correction',
        ortho_feat2_title: 'Lingual Braces',
        ortho_feat2_desc: 'Completely hidden with devices on the inside',
        ortho_feat3_title: 'Partial Orthodontics',
        ortho_feat3_desc: 'Quick correction of front teeth only',
        
        cosmetic_detail_title: 'Confident<br>Bright Smile',
        cosmetic_detail_desc: 'Cosmetic dentistry improves the color, shape, and size of teeth to create a beautiful smile. We strive for a natural yet outstanding smile.',
        cosmetic_feat1_title: 'Veneers',
        cosmetic_feat1_desc: 'Thin ceramic to improve front teeth color and shape',
        cosmetic_feat2_title: 'All-Ceramic',
        cosmetic_feat2_desc: '100% ceramic crowns without metal',
        cosmetic_feat3_title: 'Teeth Whitening',
        cosmetic_feat3_desc: 'Safe and effective professional whitening',
        
        general_detail_title: 'Basic Care for<br>Lifelong Healthy Teeth',
        general_detail_desc: 'We provide essential dental care including cavities, root canals, and gum disease treatment. Maintain healthy teeth for life with regular checkups and preventive care.',
        general_feat1_title: 'Cavity Treatment',
        general_feat1_desc: 'Step-by-step treatment from early to severe cavities',
        general_feat2_title: 'Root Canal',
        general_feat2_desc: 'Pain-free precision endodontic treatment',
        general_feat3_title: 'Gum Treatment',
        general_feat3_desc: 'Prevention and treatment of periodontal disease',
        
        // Why Choose Us
        why_tag: 'Why Choose Us',
        why_title: 'Why Choose<br>Yonsei Midas Dental',
        why1_title: 'Specialist Direct Care',
        why1_desc: 'Yonsei University graduate specialists personally treat all patients',
        why2_title: '1:1 Customized Care',
        why2_desc: 'Personalized treatment plans based on individual oral conditions',
        why3_title: 'Advanced Equipment',
        why3_desc: 'Precise diagnosis and treatment with 3D CT and digital scanners',
        why4_title: 'Thorough Sterilization',
        why4_desc: 'Safe and hygienic environment with international sterilization standards',
        
        gallery_tag: 'Gallery',
        gallery_title: 'Before & After',
        gallery_subtitle: 'See the beautiful transformations of our patients',
        
        doctor_tag: 'Medical Staff',
        doctor_title: 'Our Chief Director',
        doctor_name: 'Dr. Eun-young Choi, Chief Director',
        doctor_specialty: 'Dental Specialist / Board Certified Orthodontist',
        credentials_title: 'Credentials & Experience',
        
        cred1: 'Graduated from Yonsei University College of Dentistry',
        cred2: 'Korean Orthodontic Research Association Training',
        cred3: 'Korean Association of Orthodontists Certified',
        cred4: 'Catholic University Implant Training',
        cred5: '"Chiyewon" Implant Course Training',
        cred6: 'Loma Linda University Periodontics & Implantology (USA)',
        cred7: 'Former Director, Bareun Dental Clinic',
        cred8: 'Former Chief Director, Eunpyeong Ye Dental',
        cred9: 'Former Chief Director, Yonsei Bareun Dental',
        cred10: 'Current Chief Director, Yonsei Midas Dental',
        
        contact_tag: 'Contact',
        contact_title: 'Visit Us',
        contact_subtitle: 'Find your way to Yonsei Midas Dental Clinic',
        contact_address: 'Address',
        contact_phone: 'Phone',
        contact_hours: 'Hours',
        
        hours_weekday: 'Weekdays',
        hours_saturday: 'Saturday',
        hours_lunch: 'Lunch',
        hours_closed: 'Closed on Sundays & Holidays',
        
        map_placeholder: 'Map Area',
        
        footer_desc: 'Based on integrity and trust<br>Providing the best dental care services',
        footer_nav: 'Quick Links',
        footer_info: 'Information',
        footer_contact: 'Contact',
        footer_privacy: 'Privacy Policy',
        footer_terms: 'Terms of Service'
    },
    
    ja: {
        clinic_name: '延世ミダス歯科医院',
        nav_home: '歯科紹介',
        nav_whitening: '歯のホワイトニング',
        nav_minish: 'ミニッシュ',
        nav_prosthetics: '審美補綴',
        nav_implant: 'インプラント',
        nav_equipment: '診療設備',
        nav_contact: 'アクセス',
        
        hero_badge: 'Since 2024',
        hero_title: 'あなたの大切な笑顔のための<br><span class="highlight">最高の選択</span>',
        hero_subtitle: '延世大学出身専門医の高品格歯科診療<br>正直と信頼を基盤とした最上のサービス',
        hero_cta1: '予約相談',
        hero_cta2: '診療案内',
        stat1: 'Years Experience',
        stat2: 'Happy Patients',
        stat3: 'Satisfaction',
        scroll_down: 'Scroll Down',
        
        about_tag: 'About Us',
        about_title: '延世ミダス歯科医院<br>のご紹介',
        about_subtitle: '正直と信頼を基盤にした診療、患者中心のカスタマイズ治療',
        
        feature1_title: '専門性',
        feature1_desc: '延世大学歯科大学卒業<br>大韓歯科矯正学会認定医',
        feature2_title: '丁寧さ',
        feature2_desc: '患者様お一人お一人に<br>心を込めた診療',
        feature3_title: '最新設備',
        feature3_desc: '最先端設備と<br>清潔な診療環境',
        
        services_tag: 'Our Services',
        services_title: '診療案内',
        services_subtitle: '専門的かつ体系的な治療プログラムを提供します',
        
        service1_title: 'インプラント',
        service1_desc: '精密な診断と安全な施術で自然歯と同じ機能を回復します',
        service1_feat1: '3Dデジタルインプラント',
        service1_feat2: 'ワンデイインプラント',
        service1_feat3: '骨移植インプラント',
        
        service2_title: '歯列矯正',
        service2_desc: '個別カスタマイズ矯正で美しく健康な歯並びを作ります',
        service2_feat1: '透明矯正',
        service2_feat2: '舌側矯正',
        service2_feat3: '部分矯正',
        
        service3_title: '審美治療',
        service3_desc: 'ラミネート、オールセラミックなどで自信のある笑顔をお届けします',
        service3_feat1: 'ラミネート',
        service3_feat2: 'オールセラミック',
        service3_feat3: 'ホワイトニング',
        
        service4_title: '一般診療',
        service4_desc: '虫歯治療、神経治療、歯茎治療など基本診療を提供します',
        service4_feat1: '虫歯治療',
        service4_feat2: '神経治療',
        service4_feat3: '歯茎治療',
        
        // Service Details
        implant_detail_title: '失った歯を<br>自然歯のように',
        implant_detail_desc: 'インプラントは失った歯を代替する最も効果的な方法です。延世ミダス歯科は3D CT撮影による精密診断とデジタルインプラントシステムで安全で正確な施術を提供します。',
        implant_feat1_title: '3Dデジタルインプラント',
        implant_feat1_desc: '精密なCT分析で最適な埋入位置を決定',
        implant_feat2_title: 'ワンデイインプラント',
        implant_feat2_desc: '抜歯と同時にインプラント埋入可能',
        implant_feat3_title: '骨移植インプラント',
        implant_feat3_desc: '骨が不足している場合も安全な施術',
        
        ortho_detail_title: '美しく健康な<br>笑顔のための矯正',
        ortho_detail_desc: '歯列矯正は単に歯を揃えることを超えて、顎関節、咀嚼機能、顔面バランスまで考慮した総合的な治療です。個別のカスタマイズ診断で最適な結果を提供します。',
        ortho_feat1_title: '透明矯正',
        ortho_feat1_desc: '目立たない透明装置で審美的な矯正',
        ortho_feat2_title: '舌側矯正',
        ortho_feat2_desc: '歯の内側に装置を装着して完全に隠蔽',
        ortho_feat3_title: '部分矯正',
        ortho_feat3_desc: '前歯のみ短期間で矯正可能',
        
        cosmetic_detail_title: '自信に溢れる<br>明るい笑顔',
        cosmetic_detail_desc: '審美治療は歯の色、形、サイズを改善して美しい笑顔を作る治療です。自然でありながら際立つ笑顔のために最善を尽くします。',
        cosmetic_feat1_title: 'ラミネート',
        cosmetic_feat1_desc: '前歯の色と形を改善する薄いセラミック',
        cosmetic_feat2_title: 'オールセラミック',
        cosmetic_feat2_desc: '金属を使わない100%セラミッククラウン',
        cosmetic_feat3_title: 'ホワイトニング',
        cosmetic_feat3_desc: '安全で効果的な専門家ホワイトニング',
        
        general_detail_title: '生涯健康な歯のための<br>基本診療',
        general_detail_desc: '虫歯、神経治療、歯茎疾患など歯の健康の基本となる診療を提供します。定期的な検診と予防治療で生涯健康な歯を維持してください。',
        general_feat1_title: '虫歯治療',
        general_feat1_desc: '初期虫歯から重度虫歯まで段階別治療',
        general_feat2_title: '神経治療',
        general_feat2_desc: '痛みのない精密神経治療',
        general_feat3_title: '歯茎治療',
        general_feat3_desc: '歯周疾患の予防と治療',
        
        // Why Choose Us
        why_tag: 'Why Choose Us',
        why_title: '延世ミダス歯科を<br>選ぶべき理由',
        why1_title: '専門医による直接診療',
        why1_desc: '延世大学歯科大学出身の専門医がすべての患者様を直接診療します',
        why2_title: '1:1カスタマイズ診療',
        why2_desc: '患者様個々の口腔状態に合わせたカスタマイズ治療計画を立案します',
        why3_title: '最先端設備',
        why3_desc: '3D CT、デジタルスキャナーなど最新設備で精密な診断と治療を提供します',
        why4_title: '徹底した滅菌システム',
        why4_desc: '国際基準の滅菌システムで安全で衛生的な診療環境を維持します',
        
        gallery_tag: 'Gallery',
        gallery_title: 'Before & After',
        gallery_subtitle: '患者様の美しい変化をご確認ください',
        
        doctor_tag: 'Medical Staff',
        doctor_title: '代表院長のご紹介',
        doctor_name: 'チェ・ウンヨン 代表院長',
        doctor_specialty: '歯科専門医 / 矯正認定医',
        credentials_title: '主な経歴',
        
        cred1: '延世大学歯科大学卒業',
        cred2: '韓国歯科矯正研究会研修',
        cred3: '大韓歯科矯正学会認定医',
        cred4: 'カトリック大学インプラント研修',
        cred5: '「治予院」インプラント課程研修',
        cred6: '米国ロマリンダ大学歯周、インプラント科研修',
        cred7: '前）バルン歯科院長',
        cred8: '前）恩平イェ歯科代表院長',
        cred9: '前）延世バルン歯科代表院長',
        cred10: '現）延世ミダス歯科代表院長',
        
        contact_tag: 'Contact',
        contact_title: 'アクセス',
        contact_subtitle: '延世ミダス歯科までのアクセスをご案内します',
        contact_address: '住所',
        contact_phone: '電話',
        contact_hours: '診療時間',
        
        hours_weekday: '平日',
        hours_saturday: '土曜日',
        hours_lunch: '昼休み',
        hours_closed: '日曜日・祝日は休診',
        
        map_placeholder: '地図エリア',
        
        footer_desc: '正直と信頼を基盤に<br>最上の歯科診療サービスを提供します',
        footer_nav: 'クイックリンク',
        footer_info: '情報',
        footer_contact: '連絡先',
        footer_privacy: '個人情報取扱方針',
        footer_terms: '利用規約'
    },
    
    zh: {
        clinic_name: '延世弥达斯牙科医院',
        nav_home: '牙科介绍',
        nav_whitening: '牙齿美白',
        nav_minish: '迷你贴面',
        nav_prosthetics: '美学修复',
        nav_implant: '种植牙',
        nav_equipment: '诊疗设备',
        nav_contact: '就诊路线',
        
        hero_badge: 'Since 2024',
        hero_title: '为了您珍贵的微笑<br><span class="highlight">最佳的选择</span>',
        hero_subtitle: '延世大学出身专业医生的高品质牙科诊疗<br>基于诚实与信赖的最优服务',
        hero_cta1: '预约咨询',
        hero_cta2: '诊疗指南',
        stat1: 'Years Experience',
        stat2: 'Happy Patients',
        stat3: 'Satisfaction',
        scroll_down: 'Scroll Down',
        
        about_tag: 'About Us',
        about_title: '欢迎来到<br>延世弥达斯牙科',
        about_subtitle: '基于诚实与信赖的诊疗，以患者为中心的定制化治疗',
        
        feature1_title: '专业性',
        feature1_desc: '延世大学牙科大学毕业<br>大韩牙科矫正学会认证医师',
        feature2_title: '用心',
        feature2_desc: '为每一位患者<br>提供用心的诊疗',
        feature3_title: '最新设施',
        feature3_desc: '最尖端设备和<br>清洁的诊疗环境',
        
        services_tag: 'Our Services',
        services_title: '诊疗指南',
        services_subtitle: '提供专业且系统的治疗方案',
        
        service1_title: '种植牙',
        service1_desc: '通过精密诊断和安全手术恢复如天然牙齿般的功能',
        service1_feat1: '3D数字种植牙',
        service1_feat2: '当天种植牙',
        service1_feat3: '骨移植种植牙',
        
        service2_title: '牙齿矫正',
        service2_desc: '个性化定制矫正，打造美丽健康的牙列',
        service2_feat1: '隐形矫正',
        service2_feat2: '舌侧矫正',
        service2_feat3: '部分矫正',
        
        service3_title: '美容治疗',
        service3_desc: '通过贴面、全瓷等技术呈现自信的笑容',
        service3_feat1: '贴面',
        service3_feat2: '全瓷',
        service3_feat3: '牙齿美白',
        
        service4_title: '一般诊疗',
        service4_desc: '提供蛀牙治疗、神经治疗、牙龈治疗等基本诊疗',
        service4_feat1: '蛀牙治疗',
        service4_feat2: '神经治疗',
        service4_feat3: '牙龈治疗',
        
        // Service Details
        implant_detail_title: '失去的牙齿<br>恢复如自然牙',
        implant_detail_desc: '种植牙是替代缺失牙齿最有效的方法。延世弥达斯牙科通过3D CT扫描进行精密诊断，采用数字种植牙系统提供安全准确的手术。',
        implant_feat1_title: '3D数字种植牙',
        implant_feat1_desc: '通过精密CT分析确定最佳植入位置',
        implant_feat2_title: '当天种植牙',
        implant_feat2_desc: '拔牙的同时即可植入种植体',
        implant_feat3_title: '骨移植种植牙',
        implant_feat3_desc: '骨量不足的情况下也能安全手术',
        
        ortho_detail_title: '美丽健康的<br>微笑矫正',
        ortho_detail_desc: '牙齿矫正不仅仅是排齐牙齿，更要综合考虑颞下颌关节、咀嚼功能、面部平衡等因素。通过个性化诊断提供最佳治疗效果。',
        ortho_feat1_title: '隐形矫正',
        ortho_feat1_desc: '采用不显眼的透明矫正器进行美观矫正',
        ortho_feat2_title: '舌侧矫正',
        ortho_feat2_desc: '将矫正器安装在牙齿内侧，完全隐蔽',
        ortho_feat3_title: '部分矫正',
        ortho_feat3_desc: '仅矫正前牙，短期内完成',
        
        cosmetic_detail_title: '充满自信的<br>灿烂笑容',
        cosmetic_detail_desc: '美容治疗通过改善牙齿的颜色、形状和大小来打造美丽的笑容。我们致力于为您呈现自然而出众的笑容。',
        cosmetic_feat1_title: '贴面',
        cosmetic_feat1_desc: '改善前牙颜色和形状的薄型陶瓷',
        cosmetic_feat2_title: '全瓷',
        cosmetic_feat2_desc: '无金属的100%陶瓷牙冠',
        cosmetic_feat3_title: '牙齿美白',
        cosmetic_feat3_desc: '安全有效的专业美白',
        
        general_detail_title: '终身健康牙齿的<br>基础诊疗',
        general_detail_desc: '提供蛀牙、神经治疗、牙龈疾病等牙齿健康基础诊疗。通过定期检查和预防治疗，保持终身健康的牙齿。',
        general_feat1_title: '蛀牙治疗',
        general_feat1_desc: '从初期到严重蛀牙的分阶段治疗',
        general_feat2_title: '神经治疗',
        general_feat2_desc: '无痛精密神经治疗',
        general_feat3_title: '牙龈治疗',
        general_feat3_desc: '牙周疾病的预防和治疗',
        
        // Why Choose Us
        why_tag: 'Why Choose Us',
        why_title: '选择延世弥达斯<br>牙科的理由',
        why1_title: '专业医师亲自诊疗',
        why1_desc: '延世大学牙科大学毕业的专业医师亲自为所有患者诊疗',
        why2_title: '1:1定制诊疗',
        why2_desc: '根据每位患者的口腔状况制定个性化治疗计划',
        why3_title: '最尖端设备',
        why3_desc: '采用3D CT、数字扫描仪等最新设备提供精密诊断和治疗',
        why4_title: '严格的消毒系统',
        why4_desc: '采用国际标准消毒系统，保持安全卫生的诊疗环境',
        
        gallery_tag: 'Gallery',
        gallery_title: 'Before & After',
        gallery_subtitle: '查看患者们的美丽蜕变',
        
        doctor_tag: 'Medical Staff',
        doctor_title: '代表院长介绍',
        doctor_name: '崔恩英 代表院长',
        doctor_specialty: '牙科专业医师 / 矫正认证医师',
        credentials_title: '主要经历',
        
        cred1: '延世大学牙科大学毕业',
        cred2: '韩国牙科矫正研究会培训',
        cred3: '大韩牙科矫正学会认证医师',
        cred4: '天主教大学种植牙培训',
        cred5: '"齿预院"种植牙课程培训',
        cred6: '美国洛马林达大学牙周、种植科培训',
        cred7: '前）Bareun牙科院长',
        cred8: '前）恩平Ye牙科代表院长',
        cred9: '前）延世Bareun牙科代表院长',
        cred10: '现）延世弥达斯牙科代表院长',
        
        contact_tag: 'Contact',
        contact_title: '就诊地址',
        contact_subtitle: '为您指引前往延世弥达斯牙科的路线',
        contact_address: '地址',
        contact_phone: '电话',
        contact_hours: '诊疗时间',
        
        hours_weekday: '工作日',
        hours_saturday: '星期六',
        hours_lunch: '午休时间',
        hours_closed: '周日及公休日休诊',
        
        map_placeholder: '地图区域',
        
        footer_desc: '基于诚实与信赖<br>提供最优质的牙科诊疗服务',
        footer_nav: '快速链接',
        footer_info: '信息',
        footer_contact: '联系方式',
        footer_privacy: '隐私政策',
        footer_terms: '服务条款'
    }
};

// 언어 변경 함수
function changeLanguage(lang) {
    // 현재 언어 저장
    localStorage.setItem('preferredLanguage', lang);
    
    // HTML lang 속성 변경
    document.documentElement.lang = lang;
    document.body.setAttribute('lang', lang);
    
    // 모든 번역 요소 업데이트
    const elements = document.querySelectorAll('[data-translate]');
    elements.forEach(element => {
        const key = element.getAttribute('data-translate');
        if (translations[lang] && translations[lang][key]) {
            element.innerHTML = translations[lang][key];
        }
    });
    
    // 언어 버튼 활성화 상태 업데이트
    document.querySelectorAll('.lang-btn').forEach(btn => {
        btn.classList.toggle('active', btn.getAttribute('data-lang') === lang);
    });
}

// 페이지 로드시 초기화
document.addEventListener('DOMContentLoaded', () => {
    // URL 파라미터 체크
    const urlParams = new URLSearchParams(window.location.search);
    const urlLang = urlParams.get('lang');
    
    // 브라우저 언어 감지
    const detectBrowserLanguage = () => {
        const browserLang = navigator.language || navigator.userLanguage;
        const langCode = browserLang.toLowerCase().split('-')[0];
        
        // 지원하는 언어 목록
        const supportedLangs = ['ko', 'en', 'ja', 'zh'];
        
        // 브라우저 언어가 지원되면 해당 언어, 아니면 영어
        return supportedLangs.includes(langCode) ? langCode : 'en';
    };
    
    // 저장된 언어 또는 브라우저 언어 설정
    const savedLang = localStorage.getItem('preferredLanguage');
    const browserLang = detectBrowserLanguage();
    const defaultLang = urlLang || savedLang || browserLang;
    
    // 초기 언어 설정
    changeLanguage(defaultLang);
    
    // 언어 버튼 이벤트 리스너
    document.querySelectorAll('.lang-btn').forEach(btn => {
        btn.addEventListener('click', (e) => {
            const lang = e.target.getAttribute('data-lang');
            changeLanguage(lang);
            
            // URL 파라미터 업데이트
            const newUrl = new URL(window.location);
            newUrl.searchParams.set('lang', lang);
            window.history.pushState({}, '', newUrl);
        });
    });
});
