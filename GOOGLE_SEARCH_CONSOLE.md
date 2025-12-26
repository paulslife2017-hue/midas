# Google Search Console 설정 가이드

## 🎯 다국어 SEO 구조 완성!

### ✅ 생성된 언어별 페이지

```
📁 프로젝트 구조:
├── index.html          (한국어 - 기본)
├── en/
│   └── index.html      (영어)
├── ja/
│   └── index.html      (일본어)
├── zh/
│   └── index.html      (중국어)
├── sitemap.xml         (사이트맵)
└── robots.txt          (검색 엔진 크롤링 규칙)
```

### 🌐 URL 구조

- **한국어 (기본)**: https://yonseimidasdental.com/
- **English**: https://yonseimidasdental.com/en/
- **日本語**: https://yonseimidasdental.com/ja/
- **中文**: https://yonseimidasdental.com/zh/

---

## 📋 Google Search Console 설정 단계

### 1. 속성 추가

1. **Google Search Console 접속**
   - https://search.google.com/search-console

2. **속성 추가 클릭**
   - "도메인" 또는 "URL 접두어" 선택
   - 추천: **도메인** (모든 언어 포함)
   - 도메인 입력: `yonseimidasdental.com`

3. **소유권 확인**
   - DNS 레코드 추가 (권장)
   - 또는 HTML 파일 업로드
   - 또는 Google Analytics 연결

---

### 2. 사이트맵 제출

1. **Sitemaps 메뉴 이동**

2. **새 사이트맵 추가**
   ```
   https://yonseimidasdental.com/sitemap.xml
   ```

3. **제출 클릭**

4. **확인**
   - 상태: "성공" 확인
   - 검색된 URL: 4개 (ko, en, ja, zh)

---

### 3. 국제 타겟팅 설정

1. **레거시 도구 및 보고서** 메뉴

2. **국제 타겟팅** 선택

3. **언어 탭**
   - 각 언어별 URL이 올바른 hreflang으로 설정되었는지 확인

4. **국가 탭**
   - 타겟 국가: 대한민국
   - 또는 국제 타겟팅 선택

---

### 4. URL 검사 도구

각 언어별 페이지를 개별 검사:

```
✅ https://yonseimidasdental.com/      (한국어)
✅ https://yonseimidasdental.com/en/   (영어)
✅ https://yonseimidasdental.com/ja/   (일본어)
✅ https://yonseimidasdental.com/zh/   (중국어)
```

**각 페이지에서 확인**:
1. URL 검사 도구 사용
2. "색인 생성 요청" 클릭
3. 1-2일 내 Google 색인 생성

---

## 🔍 SEO 최적화 체크리스트

### ✅ 완료된 항목

- [x] 언어별 별도 URL (/en/, /ja/, /zh/)
- [x] 각 페이지에 고유한 title 태그
- [x] 각 페이지에 고유한 meta description
- [x] hreflang 태그 (양방향 링크)
- [x] canonical 태그
- [x] Open Graph 태그 (언어별)
- [x] Schema.org 구조화 데이터
- [x] XML 사이트맵
- [x] robots.txt
- [x] 모바일 반응형
- [x] 페이지 로딩 속도 최적화
- [x] HTTPS (Vercel 자동 제공)

---

## 📊 Hreflang 구조

모든 페이지에 다음 hreflang 태그 포함:

```html
<link rel="alternate" hreflang="ko" href="https://yonseimidasdental.com/" />
<link rel="alternate" hreflang="en" href="https://yonseimidasdental.com/en/" />
<link rel="alternate" hreflang="ja" href="https://yonseimidasdental.com/ja/" />
<link rel="alternate" hreflang="zh" href="https://yonseimidasdental.com/zh/" />
<link rel="alternate" hreflang="x-default" href="https://yonseimidasdental.com/" />
```

---

## 🌏 타겟 키워드 (언어별)

### 🇰🇷 한국어
- 인천치과, 영종도치과, 인스파이어치과
- 인천임플란트, 인천치아미백
- 영종도임플란트, 운서동치과

### 🇺🇸 영어
- incheon dental clinic, inspire resort dental
- incheon airport dentist, dental tourism korea
- implants incheon, teeth whitening korea

### 🇯🇵 일본어
- 仁川歯科, 永宗島歯科, インスパイアリゾート歯科
- 仁川インプラント, 韓国デンタルツーリズム
- 日本語診療, 韓国審美歯科

### 🇨🇳 중국어
- 仁川牙科, 永宗岛牙科, 韵斯派尔牙科
- 仁川种植牙, 韩国牙科旅游
- 中文诊疗, 韩国美容牙科

---

## 📈 모니터링

### Google Search Console에서 확인할 지표

1. **검색 실적**
   - 클릭 수
   - 노출 수
   - CTR (클릭률)
   - 평균 게재 순위

2. **커버리지**
   - 유효한 페이지: 4개
   - 오류: 0개
   - 경고: 0개

3. **개선 사항**
   - 모바일 사용성
   - 페이지 경험
   - Core Web Vitals

4. **링크**
   - 외부 링크
   - 내부 링크

---

## 🚀 다음 단계

### 1. Google Analytics 연결
```javascript
<!-- Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-XXXXXXXXXX');
</script>
```

### 2. 네이버 웹마스터 도구 등록
- https://searchadvisor.naver.com
- 사이트 추가 및 소유권 확인
- 사이트맵 제출

### 3. 다음/카카오 검색 등록
- https://register.search.daum.net/index.daum

---

## ✅ 완료!

모든 다국어 SEO 설정이 완료되었습니다!

- ✅ 언어별 페이지 생성
- ✅ Hreflang 태그 설정
- ✅ 사이트맵 생성
- ✅ Robots.txt 설정
- ✅ Google Search Console 준비 완료

**이제 배포 후 Google Search Console에 사이트맵을 제출하면 됩니다!**
