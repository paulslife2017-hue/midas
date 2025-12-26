# 🔧 도메인 불일치 오류 해결

## 📌 발견된 문제

Google Search Console에서 **오류 1개** 발생:
- **원인**: 도메인 불일치
- **기대 도메인**: `incheondentist.com`
- **잘못된 도메인**: `yonseimidasdental.com`

---

## 🎯 문제 분석

### 오류 진행 상황
```
초기: 오류 4개 (리다이렉트 오류)
1차 수정 후: 오류 1개 (도메인 불일치) ← 현재
목표: 성공 (오류 0개)
```

### 도메인 불일치 상세
sitemap.xml과 모든 HTML 파일에서 잘못된 도메인 사용:
- ❌ `https://yonseimidasdental.com/`
- ✅ `https://incheondentist.com/`

Google Search Console은 `incheondentist.com`에서 sitemap을 크롤링했지만, sitemap 내부의 URL은 `yonseimidasdental.com`을 가리켜 오류 발생.

---

## ✅ 수정 완료

### 변경된 파일 (7개)

#### 1. **sitemap.xml**
```xml
<!-- Before -->
<loc>https://yonseimidasdental.com/</loc>

<!-- After -->
<loc>https://incheondentist.com/</loc>
```

#### 2. **robots.txt**
```
# Before
Sitemap: https://yonseimidasdental.com/sitemap.xml

# After
Sitemap: https://incheondentist.com/sitemap.xml
```

#### 3. **index.html** (메인 페이지)
모든 URL 참조 변경:
- Hreflang 링크
- Canonical URL
- Open Graph URL
- Schema.org URL
- Twitter Card URL

#### 4. **en/index.html** (영어 페이지)
모든 URL 참조를 `incheondentist.com`으로 변경

#### 5. **ja/index.html** (일본어 페이지)
모든 URL 참조를 `incheondentist.com`으로 변경

#### 6. **zh/index.html** (중국어 페이지)
모든 URL 참조를 `incheondentist.com`으로 변경

#### 7. **package.json**
```json
{
  "homepage": "https://incheondentist.com"
}
```

---

## 🌍 수정된 Sitemap 최종 구조

```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" 
        xmlns:xhtml="http://www.w3.org/1999/xhtml">
  <url>
    <loc>https://incheondentist.com/</loc>
    <xhtml:link rel="alternate" hreflang="ko" href="https://incheondentist.com/"/>
    <xhtml:link rel="alternate" hreflang="en" href="https://incheondentist.com/en/"/>
    <xhtml:link rel="alternate" hreflang="ja" href="https://incheondentist.com/ja/"/>
    <xhtml:link rel="alternate" hreflang="zh" href="https://incheondentist.com/zh/"/>
    <xhtml:link rel="alternate" hreflang="x-default" href="https://incheondentist.com/"/>
    <lastmod>2025-12-26</lastmod>
    <changefreq>weekly</changefreq>
    <priority>1.0</priority>
  </url>
</urlset>
```

**특징**:
- ✅ 올바른 도메인 사용 (`incheondentist.com`)
- ✅ 1개 URL + 5개 언어 변형 (ko, en, ja, zh, x-default)
- ✅ 서버측 리다이렉트와 연동 (/en/, /ja/, /zh/ → 메인 페이지)

---

## 🚀 배포 및 확인

### 1단계: 배포 완료
```bash
git commit -m "fix(seo): Update domain to incheondentist.com"
git push origin main
```

**Commit**: `c4222f6`  
**Status**: ✅ 배포 완료

### 2단계: 확인 절차 (5-10분 후)

#### A. Sitemap 접근 테스트
```
https://incheondentist.com/sitemap.xml
```

**확인 사항**:
- ✅ 모든 URL이 `incheondentist.com`으로 표시
- ✅ XML 형식 정상
- ✅ 1개 `<url>` 엔트리 + 5개 hreflang

#### B. Robots.txt 확인
```
https://incheondentist.com/robots.txt
```

**확인 사항**:
- ✅ Sitemap URL이 `https://incheondentist.com/sitemap.xml`

#### C. 메인 페이지 메타데이터 확인
```
https://incheondentist.com/
```

브라우저에서 소스 보기 (Ctrl+U) 또는 개발자 도구로 확인:
```html
<!-- 확인할 태그들 -->
<link rel="canonical" href="https://incheondentist.com/" />
<link rel="alternate" hreflang="ko" href="https://incheondentist.com/" />
<link rel="alternate" hreflang="en" href="https://incheondentist.com/en/" />
<meta property="og:url" content="https://incheondentist.com/">
```

### 3단계: Google Search Console 재제출

#### 방법 1: Sitemap 재제출
1. Google Search Console 접속
2. **Sitemaps** 메뉴
3. 기존 sitemap.xml 삭제 (선택사항)
4. 새로 제출: `sitemap.xml`

#### 방법 2: URL 검사 도구
1. **URL 검사** 선택
2. URL 입력: `https://incheondentist.com/`
3. **색인 생성 요청** 클릭

---

## 📊 예상 결과

### 현재 상태
```
Sitemap: /sitemap.xml
상태: 오류 1개 (도메인 불일치)
발견된 페이지: 1
```

### 수정 후 예상 (24-48시간)
```
Sitemap: /sitemap.xml
상태: ✅ 성공
발견된 페이지: 1
마지막으로 읽은 날짜: 2025-12-27 또는 최신 날짜
```

---

## ⏱️ 타임라인

| 시간 | 예상 상태 | 액션 |
|------|----------|------|
| **즉시** | 배포 시작 | Vercel 대시보드 확인 |
| **1-2분** | 배포 완료 | ✅ |
| **5-10분** | CDN 캐시 갱신 | sitemap.xml 접근 테스트 |
| **1-24시간** | Google 재크롤링 | 대기 |
| **24-48시간** | Search Console 반영 | 오류 → 성공 확인 |

---

## 🎯 최종 예상 결과

### Google Search Console
```
제출된 사이트맵

Sitemap          유형      제출         마지막으로 읽은 날짜    상태      발견된 페이지
/sitemap.xml    Sitemap   2025.12.26   2025.12.27           ✅ 성공    1
```

### 커버리지 리포트
- ✅ 유효한 페이지: 1
- ✅ 오류: 0
- ✅ 경고: 0
- ✅ 제외됨: 필요에 따라

---

## 🔍 문제 해결 가이드

### Q1: 24시간 후에도 오류가 남아있는 경우

**증상**: "오류 1개" 여전히 표시

**해결 단계**:
1. **마지막으로 읽은 날짜** 확인
   - 날짜가 업데이트되지 않음 → URL 검사 도구로 수동 크롤링 요청
   - 날짜가 업데이트됨 → 48시간까지 추가 대기

2. **Sitemap 세부 정보** 확인
   - Google Search Console → Sitemaps → /sitemap.xml 클릭
   - 구체적인 오류 메시지 확인
   - 오류 세부 정보에서 URL 확인

3. **Cache 강제 갱신**
   - 브라우저 캐시 삭제
   - Vercel 캐시 Purge (필요시)
   - Google Search Console에서 sitemap 삭제 후 재제출

### Q2: 여전히 잘못된 도메인이 표시되는 경우

**확인**:
```bash
# 로컬에서 확인
curl https://incheondentist.com/sitemap.xml | grep -o "https://[^/]*"

# 기대 결과: incheondentist.com만 표시
# 만약 yonseimidasdental.com이 나오면 CDN 캐시 문제
```

**해결**:
1. Vercel 대시보드에서 최신 배포 확인
2. 5-10분 추가 대기 (CDN propagation)
3. 시크릿 모드에서 테스트

### Q3: 다른 오류가 표시되는 경우

**가능한 새로운 오류**:
- **리다이렉트 오류**: `/en/`, `/ja/`, `/zh/`가 404 반환
  - 확인: Vercel redirects 설정 (`vercel.json`)
  - 해결: 리다이렉트 규칙이 올바른지 확인
  
- **접근 거부**: robots.txt가 sitemap을 차단
  - 확인: `https://incheondentist.com/robots.txt`
  - 해결: `Allow: /` 및 `Sitemap:` 지시문 확인

- **형식 오류**: XML 파싱 에러
  - 확인: https://www.xml-sitemaps.com/validate-xml-sitemap.html
  - 해결: sitemap.xml 형식 검증

---

## 📈 SEO 영향

### 긍정적 영향
- ✅ 도메인 일관성 확보
- ✅ 크롤링 효율성 향상
- ✅ 중복 도메인 문제 해결
- ✅ 브랜드 일관성 (incheondentist.com)

### 주의사항
만약 `yonseimidasdental.com`도 사용 중이라면:
- 301 리다이렉트 설정 필요
- DNS/도메인 설정에서 메인 도메인 지정
- Google Search Console에 두 도메인 모두 등록 고려

---

## 📚 관련 문서

- `SITEMAP_FIX.md` - 1차 수정 (HTTP 헤더)
- `SITEMAP_REDIRECT_FIX.md` - 2차 수정 (리다이렉트)
- `GOOGLE_SEARCH_CONSOLE_FINAL.md` - 종합 가이드
- `DOMAIN_FIX.md` - 이 문서 (3차 수정 - 도메인)

---

## 🎉 완료 체크리스트

### 즉시 확인
- [x] sitemap.xml 도메인 변경
- [x] robots.txt 도메인 변경
- [x] 모든 HTML 파일 도메인 변경
- [x] package.json 도메인 변경
- [x] Git 커밋 및 푸시
- [x] Vercel 배포 완료

### 5-10분 후 확인
- [ ] `https://incheondentist.com/sitemap.xml` 접근 가능
- [ ] sitemap 내 모든 URL이 `incheondentist.com`
- [ ] robots.txt 확인
- [ ] 메인 페이지 메타데이터 확인

### 24-48시간 후 확인
- [ ] Google Search Console 상태: **성공**
- [ ] 오류 개수: **0**
- [ ] 발견된 페이지: **1**
- [ ] 마지막으로 읽은 날짜 업데이트

---

## 🎯 최종 요약

**문제**: 도메인 불일치 (`yonseimidasdental.com` vs `incheondentist.com`)  
**해결**: 모든 파일에서 도메인을 `incheondentist.com`으로 통일  
**파일**: sitemap.xml, robots.txt, index.html, en/ja/zh/index.html, package.json  
**커밋**: `c4222f6`  
**상태**: ✅ 배포 완료

**예상 결과**: 24-48시간 내 Google Search Console에서 **성공** 상태로 변경

---

**배포 날짜**: 2025-12-26  
**Repository**: https://github.com/paulslife2017-hue/midas.git  
**도메인**: https://incheondentist.com
