#!/usr/bin/env python3
"""
자동 백링크 생성기
다양한 플랫폼에 자동으로 백링크를 생성합니다.
"""

import json
import time
from datetime import datetime
from typing import List, Dict
import random

class BacklinkGenerator:
    def __init__(self):
        self.target_url = "https://incheondentist.org"
        self.target_keywords = [
            "인천 치과",
            "인천 임플란트",
            "인천 치아미백",
            "인천 응급 치과",
            "Incheon Dentist",
            "Incheon Dental Clinic"
        ]
        
        # 백링크 플랫폼 목록
        self.platforms = {
            "web2.0": [
                {
                    "name": "WordPress.com",
                    "url": "https://wordpress.com",
                    "type": "블로그",
                    "da": 94,
                    "instructions": "무료 블로그 생성 후 포스팅"
                },
                {
                    "name": "Blogger",
                    "url": "https://www.blogger.com",
                    "type": "블로그",
                    "da": 100,
                    "instructions": "구글 계정으로 블로그 생성"
                },
                {
                    "name": "Medium",
                    "url": "https://medium.com",
                    "type": "블로그",
                    "da": 96,
                    "instructions": "기사 작성 및 게시"
                },
                {
                    "name": "Tumblr",
                    "url": "https://www.tumblr.com",
                    "type": "블로그",
                    "da": 99,
                    "instructions": "블로그 포스트 작성"
                },
                {
                    "name": "Wix",
                    "url": "https://www.wix.com",
                    "type": "웹사이트 빌더",
                    "da": 93,
                    "instructions": "무료 사이트 생성"
                }
            ],
            "social_bookmarks": [
                {
                    "name": "Reddit",
                    "url": "https://www.reddit.com",
                    "da": 91,
                    "instructions": "관련 서브레딧에 포스팅"
                },
                {
                    "name": "Mix (formerly StumbleUpon)",
                    "url": "https://mix.com",
                    "da": 92,
                    "instructions": "컨텐츠 공유"
                },
                {
                    "name": "Folkd",
                    "url": "https://www.folkd.com",
                    "da": 52,
                    "instructions": "소셜 북마크 추가"
                },
                {
                    "name": "Diigo",
                    "url": "https://www.diigo.com",
                    "da": 92,
                    "instructions": "북마크 및 주석 추가"
                },
                {
                    "name": "Scoop.it",
                    "url": "https://www.scoop.it",
                    "da": 93,
                    "instructions": "큐레이션 생성"
                }
            ],
            "directories": [
                {
                    "name": "Google My Business",
                    "url": "https://business.google.com",
                    "da": 100,
                    "priority": "최우선",
                    "instructions": "비즈니스 프로필 생성"
                },
                {
                    "name": "Bing Places",
                    "url": "https://www.bingplaces.com",
                    "da": 95,
                    "priority": "높음",
                    "instructions": "비즈니스 등록"
                },
                {
                    "name": "Yelp",
                    "url": "https://www.yelp.com/biz/add",
                    "da": 95,
                    "priority": "높음",
                    "instructions": "비즈니스 리스팅 추가"
                },
                {
                    "name": "Yellow Pages",
                    "url": "https://www.yellowpages.com",
                    "da": 92,
                    "priority": "중간",
                    "instructions": "디렉토리 등록"
                },
                {
                    "name": "Foursquare",
                    "url": "https://foursquare.com/business",
                    "da": 93,
                    "priority": "중간",
                    "instructions": "장소 등록"
                }
            ],
            "korean_platforms": [
                {
                    "name": "네이버 블로그",
                    "url": "https://blog.naver.com",
                    "da": 98,
                    "priority": "최우선",
                    "instructions": "네이버 계정으로 블로그 생성 및 포스팅"
                },
                {
                    "name": "티스토리",
                    "url": "https://www.tistory.com",
                    "da": 90,
                    "priority": "최우선",
                    "instructions": "카카오 계정으로 블로그 생성"
                },
                {
                    "name": "네이버 카페",
                    "url": "https://section.cafe.naver.com",
                    "da": 98,
                    "priority": "높음",
                    "instructions": "관련 카페에 게시글 작성"
                },
                {
                    "name": "다음 카페",
                    "url": "https://cafe.daum.net",
                    "da": 92,
                    "priority": "높음",
                    "instructions": "카페 게시글 작성"
                },
                {
                    "name": "네이버 플레이스",
                    "url": "https://new.place.naver.com",
                    "da": 100,
                    "priority": "최우선",
                    "instructions": "비즈니스 등록"
                }
            ],
            "japanese_platforms": [
                {
                    "name": "Ameba Blog",
                    "url": "https://ameblo.jp",
                    "da": 88,
                    "priority": "높음",
                    "instructions": "아메바 블로그 작성"
                },
                {
                    "name": "FC2 Blog",
                    "url": "https://blog.fc2.com",
                    "da": 85,
                    "priority": "중간",
                    "instructions": "FC2 블로그 포스팅"
                },
                {
                    "name": "Hatena Blog",
                    "url": "https://hatenablog.com",
                    "da": 82,
                    "priority": "중간",
                    "instructions": "하테나 블로그 작성"
                },
                {
                    "name": "Google My Business (Japan)",
                    "url": "https://business.google.com",
                    "da": 100,
                    "priority": "최우선",
                    "instructions": "일본어 비즈니스 프로필"
                }
            ]
        }
        
        self.content_templates = {
            "korean": {
                "title_templates": [
                    "인천에서 믿을 수 있는 치과를 찾으시나요?",
                    "인천 치과 추천 - 외국인 환자 전문",
                    "인천공항 근처 치과 - 빠르고 편리한 치료",
                    "인천 임플란트 전문 치과 소개",
                    "인천 치아미백 - 합리적인 가격으로"
                ],
                "content_templates": [
                    """
인천에서 치과를 찾고 계신가요? {url}에서 외국인 환자를 위한 전문 치과 서비스를 제공합니다.

✅ 주요 서비스:
- 치아 임플란트
- 치아 미백
- 응급 치과 진료
- 외국인 환자 지원

📍 위치: 인천공항 근처 편리한 접근성
🌐 웹사이트: {url}
💰 합리적인 가격과 투명한 진료

지금 방문하여 더 많은 정보를 확인하세요!
                    """,
                    """
인천 치과를 찾는 외국인 여행객들을 위한 완벽한 가이드!

{url}에서는:
🦷 최신 장비를 이용한 정밀 진료
👨‍⚕️ 경험 많은 치과 전문의
🌏 다국어 지원 (한국어, 영어, 일본어, 중국어)
✈️ 공항 근처 편리한 위치

자세한 내용은 {url}에서 확인하세요!
                    """
                ]
            },
            "english": {
                "title_templates": [
                    "Best Dental Clinic in Incheon for International Patients",
                    "Incheon Dentist - Professional Dental Care Near Airport",
                    "Affordable Dental Implants in Incheon, Korea",
                    "Emergency Dental Services in Incheon",
                    "Teeth Whitening in Incheon - Quality Service"
                ],
                "content_templates": [
                    """
Looking for a reliable dentist in Incheon? Visit {url} for professional dental care!

✅ Services:
- Dental Implants
- Teeth Whitening
- Emergency Dental Care
- International Patient Support

📍 Location: Near Incheon International Airport
🌐 Website: {url}
💬 Languages: Korean, English, Japanese, Chinese

Book your appointment today!
                    """,
                    """
Welcome to Incheon's premier dental clinic for international patients!

At {url}, we offer:
🦷 State-of-the-art equipment
👨‍⚕️ Experienced dental professionals
🌏 Multilingual support
✈️ Convenient location near the airport

Learn more at {url}!
                    """
                ]
            },
            "japanese": {
                "title_templates": [
                    "仁川で信頼できる歯科医院をお探しですか？",
                    "仁川歯科 - 外国人患者専門",
                    "仁川空港近くの歯科 - 便利でプロフェッショナル",
                    "仁川でのインプラント治療",
                    "仁川ホワイトニング - お手頃価格"
                ],
                "content_templates": [
                    """
仁川で歯科医院をお探しですか？{url}で外国人患者向けの専門的な歯科サービスを提供しています。

✅ 主なサービス:
- 歯科インプラント
- ホワイトニング
- 緊急歯科診療
- 外国人患者サポート

📍 場所: 仁川空港近く
🌐 ウェブサイト: {url}
💰 手頃な価格と透明な診療

今すぐ訪問して詳細をご確認ください！
                    """
                ]
            }
        }
    
    def generate_content(self, language="korean"):
        """컨텐츠 생성"""
        templates = self.content_templates.get(language, self.content_templates["english"])
        title = random.choice(templates["title_templates"])
        content = random.choice(templates["content_templates"]).format(url=self.target_url)
        
        return {
            "title": title,
            "content": content,
            "url": self.target_url,
            "keywords": ", ".join(self.target_keywords)
        }
    
    def generate_backlink_plan(self):
        """백링크 생성 계획 작성"""
        plan = {
            "timestamp": datetime.now().isoformat(),
            "target_url": self.target_url,
            "target_keywords": self.target_keywords,
            "platforms": self.platforms,
            "total_platforms": sum(len(platforms) for platforms in self.platforms.values()),
            "estimated_backlinks": 0
        }
        
        # 예상 백링크 수 계산
        for category, platforms in self.platforms.items():
            plan["estimated_backlinks"] += len(platforms)
        
        return plan
    
    def create_submission_checklist(self):
        """제출 체크리스트 생성"""
        checklist = []
        
        for category, platforms in self.platforms.items():
            for platform in platforms:
                checklist.append({
                    "category": category,
                    "platform": platform["name"],
                    "url": platform["url"],
                    "da": platform.get("da", "N/A"),
                    "priority": platform.get("priority", "중간"),
                    "instructions": platform["instructions"],
                    "status": "대기중",
                    "submitted_date": None,
                    "backlink_url": None
                })
        
        return checklist
    
    def save_plan_to_file(self, filename="backlink_plan.json"):
        """계획을 파일로 저장"""
        plan = self.generate_backlink_plan()
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(plan, f, ensure_ascii=False, indent=2)
        return filename
    
    def save_checklist_to_file(self, filename="backlink_checklist.json"):
        """체크리스트를 파일로 저장"""
        checklist = self.create_submission_checklist()
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(checklist, f, ensure_ascii=False, indent=2)
        return filename
    
    def generate_html_report(self, filename="backlink_report.html"):
        """HTML 리포트 생성"""
        plan = self.generate_backlink_plan()
        checklist = self.create_submission_checklist()
        
        html_content = f"""
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>자동 백링크 생성 계획</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            color: #333;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 20px;
        }}
        .container {{
            max-width: 1200px;
            margin: 0 auto;
            background: white;
            border-radius: 15px;
            box-shadow: 0 10px 40px rgba(0,0,0,0.2);
            overflow: hidden;
        }}
        .header {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 40px;
            text-align: center;
        }}
        .header h1 {{
            font-size: 2.5em;
            margin-bottom: 10px;
        }}
        .header p {{
            font-size: 1.1em;
            opacity: 0.9;
        }}
        .summary {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
            padding: 40px;
            background: #f8f9fa;
        }}
        .summary-card {{
            background: white;
            padding: 25px;
            border-radius: 10px;
            box-shadow: 0 3px 10px rgba(0,0,0,0.1);
            text-align: center;
            transition: transform 0.3s;
        }}
        .summary-card:hover {{
            transform: translateY(-5px);
        }}
        .summary-card .number {{
            font-size: 2.5em;
            font-weight: bold;
            color: #667eea;
            margin-bottom: 10px;
        }}
        .summary-card .label {{
            font-size: 0.9em;
            color: #666;
            text-transform: uppercase;
            letter-spacing: 1px;
        }}
        .content {{
            padding: 40px;
        }}
        .section {{
            margin-bottom: 40px;
        }}
        .section h2 {{
            font-size: 1.8em;
            color: #667eea;
            margin-bottom: 20px;
            padding-bottom: 10px;
            border-bottom: 3px solid #667eea;
        }}
        .platform-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 20px;
            margin-top: 20px;
        }}
        .platform-card {{
            background: white;
            border: 2px solid #e0e0e0;
            border-radius: 10px;
            padding: 20px;
            transition: all 0.3s;
        }}
        .platform-card:hover {{
            border-color: #667eea;
            box-shadow: 0 5px 20px rgba(102, 126, 234, 0.2);
            transform: translateY(-3px);
        }}
        .platform-card .platform-name {{
            font-size: 1.3em;
            font-weight: bold;
            color: #333;
            margin-bottom: 10px;
        }}
        .platform-card .platform-url {{
            color: #667eea;
            text-decoration: none;
            font-size: 0.9em;
            word-break: break-all;
            display: block;
            margin-bottom: 10px;
        }}
        .platform-card .platform-url:hover {{
            text-decoration: underline;
        }}
        .badge {{
            display: inline-block;
            padding: 5px 12px;
            border-radius: 20px;
            font-size: 0.8em;
            font-weight: bold;
            margin: 5px 5px 5px 0;
        }}
        .badge-priority-최우선 {{
            background: #ff4757;
            color: white;
        }}
        .badge-priority-높음 {{
            background: #ffa502;
            color: white;
        }}
        .badge-priority-중간 {{
            background: #57606f;
            color: white;
        }}
        .badge-da {{
            background: #2ed573;
            color: white;
        }}
        .badge-type {{
            background: #667eea;
            color: white;
        }}
        .instructions {{
            margin-top: 10px;
            padding: 10px;
            background: #f8f9fa;
            border-radius: 5px;
            font-size: 0.9em;
            color: #666;
        }}
        .checklist {{
            margin-top: 20px;
        }}
        .checklist-item {{
            background: white;
            border: 1px solid #e0e0e0;
            border-radius: 5px;
            padding: 15px;
            margin-bottom: 10px;
            display: flex;
            align-items: center;
            gap: 15px;
        }}
        .checklist-item input[type="checkbox"] {{
            width: 20px;
            height: 20px;
            cursor: pointer;
        }}
        .checklist-item .item-content {{
            flex: 1;
        }}
        .status-badge {{
            padding: 5px 15px;
            border-radius: 15px;
            font-size: 0.85em;
            font-weight: bold;
        }}
        .status-대기중 {{
            background: #ffeaa7;
            color: #fdcb6e;
        }}
        .status-완료 {{
            background: #55efc4;
            color: #00b894;
        }}
        .footer {{
            background: #f8f9fa;
            padding: 30px;
            text-align: center;
            color: #666;
        }}
        .btn {{
            display: inline-block;
            padding: 12px 30px;
            background: #667eea;
            color: white;
            text-decoration: none;
            border-radius: 25px;
            font-weight: bold;
            transition: all 0.3s;
            border: none;
            cursor: pointer;
            margin: 5px;
        }}
        .btn:hover {{
            background: #764ba2;
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(102, 126, 234, 0.3);
        }}
        .content-sample {{
            background: #f8f9fa;
            padding: 20px;
            border-radius: 10px;
            margin-top: 20px;
            border-left: 4px solid #667eea;
        }}
        .content-sample h3 {{
            color: #667eea;
            margin-bottom: 10px;
        }}
        .content-sample pre {{
            background: white;
            padding: 15px;
            border-radius: 5px;
            overflow-x: auto;
            white-space: pre-wrap;
            word-wrap: break-word;
        }}
        @media (max-width: 768px) {{
            .platform-grid {{
                grid-template-columns: 1fr;
            }}
            .summary {{
                grid-template-columns: 1fr;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🚀 자동 백링크 생성 계획</h1>
            <p>Incheon Dentist 웹사이트를 위한 종합 백링크 전략</p>
            <p style="font-size: 0.9em; margin-top: 10px;">생성일: {plan['timestamp']}</p>
        </div>
        
        <div class="summary">
            <div class="summary-card">
                <div class="number">{len(self.platforms)}</div>
                <div class="label">플랫폼 카테고리</div>
            </div>
            <div class="summary-card">
                <div class="number">{plan['total_platforms']}</div>
                <div class="label">총 플랫폼 수</div>
            </div>
            <div class="summary-card">
                <div class="number">{plan['estimated_backlinks']}</div>
                <div class="label">예상 백링크</div>
            </div>
            <div class="summary-card">
                <div class="number">{len(self.target_keywords)}</div>
                <div class="label">타겟 키워드</div>
            </div>
        </div>
        
        <div class="content">
            <div class="section">
                <h2>📊 타겟 정보</h2>
                <p><strong>타겟 URL:</strong> <a href="{self.target_url}" target="_blank">{self.target_url}</a></p>
                <p><strong>타겟 키워드:</strong> {', '.join(self.target_keywords)}</p>
            </div>
"""
        
        # 각 카테고리별 플랫폼 추가
        category_names = {
            "korean_platforms": "🇰🇷 한국 플랫폼 (최우선)",
            "directories": "📁 디렉토리 및 비즈니스 리스팅",
            "web2.0": "🌐 Web 2.0 플랫폼",
            "social_bookmarks": "🔖 소셜 북마크",
            "japanese_platforms": "🇯🇵 일본 플랫폼"
        }
        
        for category, name in category_names.items():
            if category in self.platforms:
                platforms = self.platforms[category]
                html_content += f"""
            <div class="section">
                <h2>{name}</h2>
                <div class="platform-grid">
"""
                for platform in platforms:
                    priority_class = f"badge-priority-{platform.get('priority', '중간')}"
                    html_content += f"""
                    <div class="platform-card">
                        <div class="platform-name">{platform['name']}</div>
                        <a href="{platform['url']}" target="_blank" class="platform-url">{platform['url']}</a>
                        <div>
                            <span class="badge badge-da">DA: {platform.get('da', 'N/A')}</span>
                            <span class="badge {priority_class}">{platform.get('priority', '중간')}</span>
                            {f'<span class="badge badge-type">{platform.get("type", "")}</span>' if 'type' in platform else ''}
                        </div>
                        <div class="instructions">
                            📝 {platform['instructions']}
                        </div>
                    </div>
"""
                html_content += """
                </div>
            </div>
"""
        
        # 컨텐츠 샘플 추가
        korean_content = self.generate_content("korean")
        english_content = self.generate_content("english")
        japanese_content = self.generate_content("japanese")
        
        html_content += f"""
            <div class="section">
                <h2>📝 컨텐츠 샘플</h2>
                
                <div class="content-sample">
                    <h3>🇰🇷 한국어 컨텐츠</h3>
                    <p><strong>제목:</strong> {korean_content['title']}</p>
                    <pre>{korean_content['content']}</pre>
                </div>
                
                <div class="content-sample">
                    <h3>🇺🇸 영어 컨텐츠</h3>
                    <p><strong>제목:</strong> {english_content['title']}</p>
                    <pre>{english_content['content']}</pre>
                </div>
                
                <div class="content-sample">
                    <h3>🇯🇵 일본어 컨텐츠</h3>
                    <p><strong>제목:</strong> {japanese_content['title']}</p>
                    <pre>{japanese_content['content']}</pre>
                </div>
            </div>
            
            <div class="section">
                <h2>✅ 실행 체크리스트</h2>
                <div class="checklist">
"""
        
        for item in checklist:
            html_content += f"""
                    <div class="checklist-item">
                        <input type="checkbox" id="check-{checklist.index(item)}">
                        <div class="item-content">
                            <strong>{item['platform']}</strong> ({item['category']})
                            <br>
                            <small>{item['instructions']}</small>
                        </div>
                        <span class="badge badge-da">DA: {item['da']}</span>
                        <span class="status-badge status-{item['status']}">{item['status']}</span>
                    </div>
"""
        
        html_content += """
                </div>
            </div>
            
            <div class="section">
                <h2>🎯 실행 가이드</h2>
                <ol style="line-height: 2;">
                    <li><strong>우선순위 설정:</strong> "최우선" 표시된 플랫폼부터 시작</li>
                    <li><strong>계정 생성:</strong> 각 플랫폼에 계정 생성 (실제 이메일 사용)</li>
                    <li><strong>컨텐츠 작성:</strong> 위의 샘플을 참고하여 자연스러운 컨텐츠 작성</li>
                    <li><strong>링크 삽입:</strong> 컨텐츠 내에 자연스럽게 백링크 삽입</li>
                    <li><strong>다양화:</strong> 각 플랫폼마다 조금씩 다른 컨텐츠 사용</li>
                    <li><strong>정기적 업데이트:</strong> 주 2-3회 새로운 컨텐츠 추가</li>
                    <li><strong>추적:</strong> 생성된 백링크 URL 기록</li>
                </ol>
            </div>
            
            <div class="section">
                <h2>⚠️ 주의사항</h2>
                <ul style="line-height: 2;">
                    <li>스팸으로 보이지 않도록 자연스러운 컨텐츠 작성</li>
                    <li>각 플랫폼의 이용 약관 준수</li>
                    <li>과도한 키워드 반복 피하기</li>
                    <li>다양한 앵커 텍스트 사용</li>
                    <li>점진적으로 백링크 생성 (하루에 5-10개 이내)</li>
                    <li>품질 > 수량 (고품질 백링크에 집중)</li>
                </ul>
            </div>
        </div>
        
        <div class="footer">
            <p><strong>자동 백링크 생성기</strong></p>
            <p>이 도구로 생성된 계획은 수동으로 실행해야 합니다.</p>
            <p>© 2024 Incheon Dentist SEO Project</p>
            <div style="margin-top: 20px;">
                <button class="btn" onclick="window.print()">📄 인쇄하기</button>
                <a href="backlink_plan.json" class="btn" download>💾 JSON 다운로드</a>
            </div>
        </div>
    </div>
    
    <script>
        // 체크박스 상태 저장
        document.querySelectorAll('input[type="checkbox"]').forEach(checkbox => {{
            checkbox.addEventListener('change', function() {{
                const item = this.closest('.checklist-item');
                const statusBadge = item.querySelector('.status-badge');
                if (this.checked) {{
                    statusBadge.textContent = '완료';
                    statusBadge.className = 'status-badge status-완료';
                    item.style.opacity = '0.6';
                }} else {{
                    statusBadge.textContent = '대기중';
                    statusBadge.className = 'status-badge status-대기중';
                    item.style.opacity = '1';
                }}
            }});
        }});
    </script>
</body>
</html>
"""
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        return filename


def main():
    """메인 함수"""
    print("=" * 60)
    print("🚀 자동 백링크 생성기")
    print("=" * 60)
    print()
    
    generator = BacklinkGenerator()
    
    print("📊 백링크 계획 생성 중...")
    json_file = generator.save_plan_to_file()
    print(f"✅ 계획 저장 완료: {json_file}")
    
    print("\n📋 체크리스트 생성 중...")
    checklist_file = generator.save_checklist_to_file()
    print(f"✅ 체크리스트 저장 완료: {checklist_file}")
    
    print("\n📄 HTML 리포트 생성 중...")
    html_file = generator.generate_html_report()
    print(f"✅ HTML 리포트 저장 완료: {html_file}")
    
    print("\n" + "=" * 60)
    print("🎉 모든 파일 생성 완료!")
    print("=" * 60)
    print(f"\n생성된 파일:")
    print(f"  1. {json_file} - 백링크 계획 (JSON)")
    print(f"  2. {checklist_file} - 실행 체크리스트 (JSON)")
    print(f"  3. {html_file} - 시각적 리포트 (HTML)")
    print(f"\n💡 {html_file}을 브라우저에서 열어 확인하세요!")
    
    # 요약 통계
    plan = generator.generate_backlink_plan()
    print(f"\n📈 통계:")
    print(f"  • 총 플랫폼 카테고리: {len(generator.platforms)}")
    print(f"  • 총 플랫폼 수: {plan['total_platforms']}")
    print(f"  • 예상 백링크: {plan['estimated_backlinks']}")
    print(f"  • 타겟 키워드: {len(generator.target_keywords)}")


if __name__ == "__main__":
    main()
