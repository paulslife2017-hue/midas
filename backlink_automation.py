#!/usr/bin/env python3
"""
🔗 자동 백링크 생성 시스템
연세미다스치과 SEO 백링크 자동화 도구
"""

import json
import csv
import time
from datetime import datetime
from typing import Dict, List, Optional
import webbrowser
import os

class BacklinkAutomation:
    """백링크 자동 생성 및 관리 클래스"""
    
    def __init__(self):
        self.business_info = {
            "name": "Yonsei Midas Dental Clinic",
            "name_kr": "연세미다스치과",
            "address": "127 Gonghang Culture-ro, Jung-gu, Incheon, South Korea",
            "address_kr": "인천광역시 중구 공항문화로 127",
            "phone": "+82-32-722-2879",
            "website": "https://www.yonseimidas.com",
            "email": "info@yonseimidas.com",
            "category_primary": "Dentist / Dental Clinic",
            "category_secondary": ["Cosmetic Dentist", "Orthodontist", "Dental Implants"],
            "hours": {
                "Monday": "9:00 AM - 6:00 PM",
                "Tuesday": "9:00 AM - 6:00 PM",
                "Wednesday": "9:00 AM - 6:00 PM",
                "Thursday": "9:00 AM - 6:00 PM",
                "Friday": "9:00 AM - 6:00 PM",
                "Saturday": "Closed",
                "Sunday": "Closed"
            },
            "services": [
                "Dental Implants",
                "Teeth Whitening",
                "Orthodontics",
                "General Dentistry",
                "Cosmetic Dentistry",
                "Root Canal Treatment",
                "Tooth Extraction",
                "Dental Crowns & Bridges"
            ],
            "languages": ["English", "Korean", "Japanese", "Chinese"],
            "description_en": "English-speaking dentist near Incheon Airport. Premium dental care for international patients. Specializing in dental implants, teeth whitening, and cosmetic dentistry. 10 minutes from Incheon International Airport.",
            "description_kr": "인천공항 10분 거리 연세미다스치과. 외국인 환자 전문 치과. 임플란트, 미백, 교정치료 전문. 영어, 일본어, 중국어 진료 가능.",
            "description_ja": "仁川空港から10分の延世ミダス歯科。外国人患者専門の歯科医院。インプラント、ホワイトニング、矯正治療の専門医。英語・日本語・中国語診療可能。",
            "description_zh": "距离仁川机场10分钟的延世米达斯牙科。专门为外国患者提供服务。专业种植牙、美白、正畸治疗。提供英语、日语、中文诊疗服务。",
            "coordinates": {
                "latitude": "37.4911",
                "longitude": "126.6215"
            }
        }
        
        self.directories = self._load_directories()
        self.progress_file = "backlink_progress.json"
        self.progress = self._load_progress()
    
    def _load_directories(self) -> List[Dict]:
        """백링크 디렉토리 목록 로드"""
        return [
            # 1순위 - Google 생태계
            {
                "name": "Google My Business",
                "url": "https://business.google.com",
                "priority": 1,
                "rating": 5,
                "category": "Google Ecosystem",
                "auto_submit": False,
                "instructions": "Sign in with Google account → Create business profile → Verify location"
            },
            {
                "name": "Google Search Console",
                "url": "https://search.google.com/search-console",
                "priority": 1,
                "rating": 5,
                "category": "Google Ecosystem",
                "auto_submit": True,
                "instructions": "Add property → Verify domain → Submit sitemap"
            },
            
            # 지도/리뷰 플랫폼
            {
                "name": "Naver Map",
                "url": "https://map.naver.com",
                "priority": 1,
                "rating": 5,
                "category": "Maps & Reviews",
                "auto_submit": False,
                "instructions": "네이버 로그인 → 내 비즈니스 등록 → 주소 인증"
            },
            {
                "name": "Kakao Map",
                "url": "https://map.kakao.com",
                "priority": 1,
                "rating": 5,
                "category": "Maps & Reviews",
                "auto_submit": False,
                "instructions": "카카오 로그인 → 장소 등록 → 사업자 인증"
            },
            {
                "name": "Apple Maps",
                "url": "https://mapsconnect.apple.com",
                "priority": 1,
                "rating": 4,
                "category": "Maps & Reviews",
                "auto_submit": False,
                "instructions": "Sign in with Apple ID → Add location → Verify business"
            },
            {
                "name": "Bing Places",
                "url": "https://www.bingplaces.com",
                "priority": 1,
                "rating": 4,
                "category": "Maps & Reviews",
                "auto_submit": False,
                "instructions": "Sign in → Add business → Verify phone"
            },
            
            # 의료 전문 디렉토리 (한국)
            {
                "name": "굿닥 (GoodDoc)",
                "url": "https://www.goodoc.co.kr",
                "priority": 1,
                "rating": 5,
                "category": "Medical Directories",
                "auto_submit": False,
                "instructions": "병원 등록 신청 → 정보 입력 → 승인 대기"
            },
            {
                "name": "병원정보",
                "url": "https://www.hospitalinfo.co.kr",
                "priority": 2,
                "rating": 4,
                "category": "Medical Directories",
                "auto_submit": False,
                "instructions": "회원가입 → 병원 등록 → 정보 입력"
            },
            {
                "name": "114 병원",
                "url": "https://www.114.co.kr",
                "priority": 2,
                "rating": 4,
                "category": "Medical Directories",
                "auto_submit": False,
                "instructions": "114 고객센터 문의 → 병원 등록 신청"
            },
            
            # 국제 의료 디렉토리
            {
                "name": "Medical Departures",
                "url": "https://www.medicaldepartures.com",
                "priority": 1,
                "rating": 5,
                "category": "Medical Tourism",
                "auto_submit": False,
                "instructions": "Sign up → Add clinic → Submit verification documents"
            },
            {
                "name": "Dental Departures",
                "url": "https://www.dentaldepartures.com",
                "priority": 1,
                "rating": 5,
                "category": "Medical Tourism",
                "auto_submit": False,
                "instructions": "Create account → List your clinic → Upload certificates"
            },
            {
                "name": "Whatclinic",
                "url": "https://www.whatclinic.com",
                "priority": 1,
                "rating": 5,
                "category": "Medical Tourism",
                "auto_submit": False,
                "instructions": "Register clinic → Complete profile → Add treatments"
            },
            {
                "name": "Medical Tourism",
                "url": "https://www.medicaltourism.com",
                "priority": 2,
                "rating": 4,
                "category": "Medical Tourism",
                "auto_submit": False,
                "instructions": "Sign up as provider → Submit clinic info"
            },
            {
                "name": "PlacidWay",
                "url": "https://www.placidway.com",
                "priority": 2,
                "rating": 4,
                "category": "Medical Tourism",
                "auto_submit": False,
                "instructions": "Provider signup → Complete verification"
            },
            
            # 여행/리뷰 플랫폼
            {
                "name": "TripAdvisor",
                "url": "https://www.tripadvisor.com",
                "priority": 1,
                "rating": 5,
                "category": "Travel & Reviews",
                "auto_submit": False,
                "instructions": "Sign up → Add your business → Claim listing"
            },
            {
                "name": "Yelp",
                "url": "https://www.yelp.com",
                "priority": 1,
                "rating": 5,
                "category": "Travel & Reviews",
                "auto_submit": False,
                "instructions": "Create account → Add business → Verify ownership"
            },
            {
                "name": "Foursquare",
                "url": "https://foursquare.com",
                "priority": 2,
                "rating": 4,
                "category": "Travel & Reviews",
                "auto_submit": False,
                "instructions": "Sign up → Add venue → Claim business"
            },
            {
                "name": "Yellow Pages",
                "url": "https://www.yellowpages.com",
                "priority": 2,
                "rating": 4,
                "category": "Travel & Reviews",
                "auto_submit": False,
                "instructions": "Add business → Complete profile"
            },
            
            # 비즈니스 디렉토리
            {
                "name": "Manta",
                "url": "https://www.manta.com",
                "priority": 2,
                "rating": 4,
                "category": "Business Directories",
                "auto_submit": False,
                "instructions": "Create account → Add business listing"
            },
            {
                "name": "Hotfrog",
                "url": "https://www.hotfrog.com",
                "priority": 2,
                "rating": 4,
                "category": "Business Directories",
                "auto_submit": False,
                "instructions": "Sign up → Add business → Verify email"
            },
            {
                "name": "Brownbook",
                "url": "https://www.brownbook.net",
                "priority": 2,
                "rating": 4,
                "category": "Business Directories",
                "auto_submit": False,
                "instructions": "Register → Add company → Activate listing"
            },
            {
                "name": "MerchantCircle",
                "url": "https://www.merchantcircle.com",
                "priority": 2,
                "rating": 4,
                "category": "Business Directories",
                "auto_submit": False,
                "instructions": "Sign up → Create listing → Verify business"
            },
            {
                "name": "Alignable",
                "url": "https://www.alignable.com",
                "priority": 2,
                "rating": 4,
                "category": "Business Directories",
                "auto_submit": False,
                "instructions": "Join → Create business profile → Network with local businesses"
            },
            
            # 소셜 미디어
            {
                "name": "Facebook Business Page",
                "url": "https://www.facebook.com/business",
                "priority": 1,
                "rating": 5,
                "category": "Social Media",
                "auto_submit": False,
                "instructions": "Create page → Add business info → Verify page"
            },
            {
                "name": "Instagram Business",
                "url": "https://www.instagram.com",
                "priority": 1,
                "rating": 5,
                "category": "Social Media",
                "auto_submit": False,
                "instructions": "Create account → Switch to business → Add location"
            },
            {
                "name": "LinkedIn Company Page",
                "url": "https://www.linkedin.com",
                "priority": 1,
                "rating": 5,
                "category": "Social Media",
                "auto_submit": False,
                "instructions": "Create company page → Complete profile → Publish updates"
            },
            {
                "name": "YouTube Channel",
                "url": "https://www.youtube.com",
                "priority": 1,
                "rating": 5,
                "category": "Social Media",
                "auto_submit": False,
                "instructions": "Create channel → Add business info → Upload videos"
            },
            {
                "name": "네이버 블로그",
                "url": "https://blog.naver.com",
                "priority": 1,
                "rating": 5,
                "category": "Social Media",
                "auto_submit": False,
                "instructions": "네이버 로그인 → 블로그 개설 → 치과 소개 포스팅"
            },
            {
                "name": "티스토리",
                "url": "https://www.tistory.com",
                "priority": 1,
                "rating": 5,
                "category": "Social Media",
                "auto_submit": False,
                "instructions": "카카오 로그인 → 블로그 개설 → SEO 최적화 글쓰기"
            },
            {
                "name": "Pinterest Business",
                "url": "https://www.pinterest.com/business",
                "priority": 2,
                "rating": 4,
                "category": "Social Media",
                "auto_submit": False,
                "instructions": "Create business account → Add profile → Create pins"
            },
            
            # 전문가 플랫폼
            {
                "name": "Healthgrades",
                "url": "https://www.healthgrades.com",
                "priority": 1,
                "rating": 5,
                "category": "Healthcare Professionals",
                "auto_submit": False,
                "instructions": "Claim profile → Verify credentials → Update info"
            },
            {
                "name": "Vitals",
                "url": "https://www.vitals.com",
                "priority": 2,
                "rating": 4,
                "category": "Healthcare Professionals",
                "auto_submit": False,
                "instructions": "Register → Claim practice → Complete profile"
            },
            {
                "name": "RateMDs",
                "url": "https://www.ratemds.com",
                "priority": 2,
                "rating": 4,
                "category": "Healthcare Professionals",
                "auto_submit": False,
                "instructions": "Find listing → Claim profile → Update information"
            },
            {
                "name": "WebMD Physician Directory",
                "url": "https://doctor.webmd.com",
                "priority": 1,
                "rating": 5,
                "category": "Healthcare Professionals",
                "auto_submit": False,
                "instructions": "Register → Submit credentials → Complete profile"
            },
            {
                "name": "Zocdoc",
                "url": "https://www.zocdoc.com",
                "priority": 1,
                "rating": 5,
                "category": "Healthcare Professionals",
                "auto_submit": False,
                "instructions": "Sign up as provider → Set up schedule → Accept bookings"
            }
        ]
    
    def _load_progress(self) -> Dict:
        """진행 상황 로드"""
        if os.path.exists(self.progress_file):
            with open(self.progress_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {
            "completed": [],
            "in_progress": [],
            "pending": [d["name"] for d in self.directories],
            "last_updated": None
        }
    
    def _save_progress(self):
        """진행 상황 저장"""
        self.progress["last_updated"] = datetime.now().isoformat()
        with open(self.progress_file, 'w', encoding='utf-8') as f:
            json.dump(self.progress, f, indent=2, ensure_ascii=False)
    
    def generate_submission_data(self, directory: Dict) -> Dict:
        """디렉토리별 제출 데이터 생성"""
        data = {
            "business_name": self.business_info["name"],
            "business_name_local": self.business_info["name_kr"],
            "address": self.business_info["address"],
            "address_local": self.business_info["address_kr"],
            "phone": self.business_info["phone"],
            "website": self.business_info["website"],
            "email": self.business_info["email"],
            "category": self.business_info["category_primary"],
            "subcategories": ", ".join(self.business_info["category_secondary"]),
            "description": self.business_info["description_en"],
            "services": ", ".join(self.business_info["services"]),
            "languages": ", ".join(self.business_info["languages"]),
            "hours": self._format_hours(),
            "latitude": self.business_info["coordinates"]["latitude"],
            "longitude": self.business_info["coordinates"]["longitude"]
        }
        return data
    
    def _format_hours(self) -> str:
        """진료 시간 포맷팅"""
        hours_list = []
        for day, hours in self.business_info["hours"].items():
            hours_list.append(f"{day}: {hours}")
        return "\n".join(hours_list)
    
    def export_submission_template(self, filename: str = "backlink_submission_template.csv"):
        """CSV 템플릿 내보내기"""
        fieldnames = [
            "Directory Name",
            "URL",
            "Priority",
            "Rating",
            "Category",
            "Business Name",
            "Business Name (Local)",
            "Address",
            "Address (Local)",
            "Phone",
            "Website",
            "Email",
            "Category",
            "Services",
            "Languages",
            "Description (EN)",
            "Description (KR)",
            "Hours",
            "Latitude",
            "Longitude",
            "Status",
            "Submission Date",
            "Notes"
        ]
        
        with open(filename, 'w', newline='', encoding='utf-8-sig') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            
            for directory in self.directories:
                submission_data = self.generate_submission_data(directory)
                row = {
                    "Directory Name": directory["name"],
                    "URL": directory["url"],
                    "Priority": directory["priority"],
                    "Rating": "⭐" * directory["rating"],
                    "Category": directory["category"],
                    "Business Name": submission_data["business_name"],
                    "Business Name (Local)": submission_data["business_name_local"],
                    "Address": submission_data["address"],
                    "Address (Local)": submission_data["address_local"],
                    "Phone": submission_data["phone"],
                    "Website": submission_data["website"],
                    "Email": submission_data["email"],
                    "Category": submission_data["category"],
                    "Services": submission_data["services"],
                    "Languages": submission_data["languages"],
                    "Description (EN)": self.business_info["description_en"],
                    "Description (KR)": self.business_info["description_kr"],
                    "Hours": submission_data["hours"],
                    "Latitude": submission_data["latitude"],
                    "Longitude": submission_data["longitude"],
                    "Status": "Pending",
                    "Submission Date": "",
                    "Notes": directory.get("instructions", "")
                }
                writer.writerow(row)
        
        print(f"✅ CSV 템플릿 생성 완료: {filename}")
        return filename
    
    def export_json_data(self, filename: str = "backlink_data.json"):
        """JSON 데이터 내보내기"""
        export_data = {
            "business_info": self.business_info,
            "directories": self.directories,
            "progress": self.progress,
            "export_date": datetime.now().isoformat()
        }
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(export_data, f, indent=2, ensure_ascii=False)
        
        print(f"✅ JSON 데이터 생성 완료: {filename}")
        return filename
    
    def generate_html_checklist(self, filename: str = "backlink_checklist.html"):
        """HTML 체크리스트 생성"""
        html_content = f"""<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>백링크 등록 체크리스트 - 연세미다스치과</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        body {{
            font-family: 'Segoe UI', Arial, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 20px;
            min-height: 100vh;
        }}
        .container {{
            max-width: 1200px;
            margin: 0 auto;
            background: white;
            border-radius: 20px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
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
            font-size: 1.2em;
            opacity: 0.9;
        }}
        .stats {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
            padding: 30px;
            background: #f8f9fa;
        }}
        .stat-card {{
            background: white;
            padding: 20px;
            border-radius: 10px;
            text-align: center;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }}
        .stat-number {{
            font-size: 2.5em;
            font-weight: bold;
            color: #667eea;
        }}
        .stat-label {{
            color: #666;
            margin-top: 5px;
        }}
        .content {{
            padding: 40px;
        }}
        .category {{
            margin-bottom: 40px;
        }}
        .category-header {{
            background: #667eea;
            color: white;
            padding: 15px 20px;
            border-radius: 10px;
            margin-bottom: 20px;
            font-size: 1.3em;
            font-weight: bold;
        }}
        .directory-item {{
            background: #f8f9fa;
            padding: 20px;
            margin-bottom: 15px;
            border-radius: 10px;
            border-left: 5px solid #667eea;
            transition: all 0.3s ease;
        }}
        .directory-item:hover {{
            transform: translateX(5px);
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        }}
        .directory-item.completed {{
            border-left-color: #28a745;
            opacity: 0.7;
        }}
        .directory-name {{
            font-size: 1.2em;
            font-weight: bold;
            color: #333;
            margin-bottom: 10px;
        }}
        .directory-info {{
            display: flex;
            gap: 20px;
            margin-bottom: 10px;
            flex-wrap: wrap;
        }}
        .info-badge {{
            background: white;
            padding: 5px 15px;
            border-radius: 20px;
            font-size: 0.9em;
            display: inline-flex;
            align-items: center;
            gap: 5px;
        }}
        .priority-1 {{ color: #dc3545; font-weight: bold; }}
        .priority-2 {{ color: #ffc107; font-weight: bold; }}
        .priority-3 {{ color: #28a745; font-weight: bold; }}
        .directory-url {{
            color: #667eea;
            text-decoration: none;
            font-weight: 500;
        }}
        .directory-url:hover {{
            text-decoration: underline;
        }}
        .instructions {{
            background: white;
            padding: 10px 15px;
            border-radius: 5px;
            margin-top: 10px;
            font-size: 0.9em;
            color: #666;
        }}
        .checkbox {{
            float: right;
            width: 30px;
            height: 30px;
            cursor: pointer;
        }}
        .business-info {{
            background: #e7f3ff;
            padding: 20px;
            border-radius: 10px;
            margin-bottom: 30px;
        }}
        .business-info h3 {{
            color: #667eea;
            margin-bottom: 15px;
        }}
        .business-info p {{
            margin: 5px 0;
            line-height: 1.6;
        }}
        .progress-bar {{
            width: 100%;
            height: 30px;
            background: #e0e0e0;
            border-radius: 15px;
            overflow: hidden;
            margin: 20px 0;
        }}
        .progress-fill {{
            height: 100%;
            background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
            width: 0%;
            transition: width 0.5s ease;
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            font-weight: bold;
        }}
        .action-buttons {{
            display: flex;
            gap: 10px;
            margin-top: 10px;
        }}
        .btn {{
            padding: 8px 16px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-weight: 500;
            text-decoration: none;
            display: inline-block;
        }}
        .btn-primary {{
            background: #667eea;
            color: white;
        }}
        .btn-success {{
            background: #28a745;
            color: white;
        }}
        .btn:hover {{
            opacity: 0.8;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🔗 백링크 등록 체크리스트</h1>
            <p>연세미다스치과 SEO 백링크 자동화</p>
        </div>
        
        <div class="stats">
            <div class="stat-card">
                <div class="stat-number" id="total-count">{len(self.directories)}</div>
                <div class="stat-label">총 디렉토리</div>
            </div>
            <div class="stat-card">
                <div class="stat-number" id="completed-count">0</div>
                <div class="stat-label">완료</div>
            </div>
            <div class="stat-card">
                <div class="stat-number" id="pending-count">{len(self.directories)}</div>
                <div class="stat-label">대기</div>
            </div>
            <div class="stat-card">
                <div class="stat-number" id="completion-rate">0%</div>
                <div class="stat-label">완료율</div>
            </div>
        </div>
        
        <div class="progress-bar">
            <div class="progress-fill" id="progress-fill">0%</div>
        </div>
        
        <div class="content">
            <div class="business-info">
                <h3>📋 비즈니스 정보 (복사하여 사용)</h3>
                <p><strong>Business Name:</strong> {self.business_info['name']}</p>
                <p><strong>비즈니스명 (한글):</strong> {self.business_info['name_kr']}</p>
                <p><strong>Address:</strong> {self.business_info['address']}</p>
                <p><strong>주소 (한글):</strong> {self.business_info['address_kr']}</p>
                <p><strong>Phone:</strong> {self.business_info['phone']}</p>
                <p><strong>Website:</strong> {self.business_info['website']}</p>
                <p><strong>Email:</strong> {self.business_info['email']}</p>
                <p><strong>Services:</strong> {', '.join(self.business_info['services'])}</p>
                <p><strong>Languages:</strong> {', '.join(self.business_info['languages'])}</p>
            </div>
"""
        
        # 카테고리별로 그룹화
        categories = {}
        for directory in self.directories:
            category = directory["category"]
            if category not in categories:
                categories[category] = []
            categories[category].append(directory)
        
        # 각 카테고리별 HTML 생성
        for category, dirs in categories.items():
            html_content += f"""
            <div class="category">
                <div class="category-header">
                    {category} ({len(dirs)}개)
                </div>
"""
            for directory in dirs:
                priority_class = f"priority-{directory['priority']}"
                rating_stars = "⭐" * directory['rating']
                
                html_content += f"""
                <div class="directory-item" data-name="{directory['name']}">
                    <input type="checkbox" class="checkbox" onchange="updateProgress(this)">
                    <div class="directory-name">{directory['name']}</div>
                    <div class="directory-info">
                        <span class="info-badge {priority_class}">우선순위: {directory['priority']}</span>
                        <span class="info-badge">{rating_stars}</span>
                        <a href="{directory['url']}" target="_blank" class="directory-url">{directory['url']}</a>
                    </div>
                    <div class="instructions">
                        📝 {directory.get('instructions', 'No instructions available')}
                    </div>
                    <div class="action-buttons">
                        <a href="{directory['url']}" target="_blank" class="btn btn-primary">등록하기</a>
                        <button class="btn btn-success" onclick="markCompleted(this)">완료 표시</button>
                    </div>
                </div>
"""
            
            html_content += """
            </div>
"""
        
        html_content += """
        </div>
    </div>
    
    <script>
        // 로컬 스토리지에서 진행 상황 로드
        function loadProgress() {
            const saved = localStorage.getItem('backlink_progress');
            if (saved) {
                const completed = JSON.parse(saved);
                completed.forEach(name => {
                    const item = document.querySelector(`[data-name="${name}"]`);
                    if (item) {
                        item.querySelector('.checkbox').checked = true;
                        item.classList.add('completed');
                    }
                });
                updateStats();
            }
        }
        
        // 진행 상황 저장
        function saveProgress() {
            const completed = [];
            document.querySelectorAll('.directory-item.completed').forEach(item => {
                completed.push(item.getAttribute('data-name'));
            });
            localStorage.setItem('backlink_progress', JSON.stringify(completed));
        }
        
        // 통계 업데이트
        function updateStats() {
            const total = document.querySelectorAll('.directory-item').length;
            const completed = document.querySelectorAll('.directory-item.completed').length;
            const pending = total - completed;
            const rate = Math.round((completed / total) * 100);
            
            document.getElementById('completed-count').textContent = completed;
            document.getElementById('pending-count').textContent = pending;
            document.getElementById('completion-rate').textContent = rate + '%';
            
            const progressFill = document.getElementById('progress-fill');
            progressFill.style.width = rate + '%';
            progressFill.textContent = rate + '%';
        }
        
        // 체크박스 변경 시
        function updateProgress(checkbox) {
            const item = checkbox.closest('.directory-item');
            if (checkbox.checked) {
                item.classList.add('completed');
            } else {
                item.classList.remove('completed');
            }
            updateStats();
            saveProgress();
        }
        
        // 완료 표시 버튼
        function markCompleted(button) {
            const item = button.closest('.directory-item');
            const checkbox = item.querySelector('.checkbox');
            checkbox.checked = true;
            item.classList.add('completed');
            updateStats();
            saveProgress();
        }
        
        // 페이지 로드 시 진행 상황 복원
        window.addEventListener('load', loadProgress);
    </script>
</body>
</html>
"""
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        print(f"✅ HTML 체크리스트 생성 완료: {filename}")
        return filename
    
    def open_directories_by_priority(self, priority: int = 1, delay: int = 5):
        """우선순위별로 디렉토리 자동 오픈"""
        priority_dirs = [d for d in self.directories if d["priority"] == priority]
        
        print(f"\n🚀 우선순위 {priority} 디렉토리 자동 오픈 시작...")
        print(f"총 {len(priority_dirs)}개 사이트를 {delay}초 간격으로 엽니다.\n")
        
        for i, directory in enumerate(priority_dirs, 1):
            print(f"[{i}/{len(priority_dirs)}] {directory['name']} 열기...")
            print(f"   URL: {directory['url']}")
            print(f"   지침: {directory.get('instructions', 'N/A')}\n")
            
            try:
                webbrowser.open(directory['url'])
                if i < len(priority_dirs):  # 마지막 항목이 아니면 대기
                    time.sleep(delay)
            except Exception as e:
                print(f"   ❌ 오류 발생: {str(e)}\n")
                continue
        
        print(f"✅ 우선순위 {priority} 디렉토리 오픈 완료!")
    
    def generate_weekly_plan(self, filename: str = "weekly_backlink_plan.md"):
        """주간 백링크 등록 계획 생성"""
        content = f"""# 📅 4주 백링크 등록 계획

## 연세미다스치과 SEO 백링크 구축 로드맵

**생성일**: {datetime.now().strftime('%Y-%m-%d')}  
**총 디렉토리**: {len(self.directories)}개  
**목표**: 4주 내 고품질 백링크 100+ 개 확보

---

## 🗓️ 주차별 실행 계획

### 1주차 (우선순위 1 - Google & 주요 플랫폼)
**목표**: 20개 등록 완료

"""
        
        week1 = [d for d in self.directories if d["priority"] == 1 and d["category"] in ["Google Ecosystem", "Maps & Reviews", "Medical Tourism"]][:20]
        for i, d in enumerate(week1, 1):
            content += f"{i}. **{d['name']}** ({d['rating']}⭐)\n"
            content += f"   - URL: {d['url']}\n"
            content += f"   - 지침: {d.get('instructions', 'N/A')}\n\n"
        
        content += """
### 2주차 (의료 전문 + 여행 플랫폼)
**목표**: 25개 등록 완료

"""
        
        week2 = [d for d in self.directories if d["category"] in ["Medical Directories", "Travel & Reviews"]][:25]
        for i, d in enumerate(week2, 1):
            content += f"{i}. **{d['name']}** ({d['rating']}⭐)\n"
            content += f"   - {d['url']}\n\n"
        
        content += """
### 3주차 (비즈니스 디렉토리 + 소셜 미디어)
**목표**: 25개 등록 완료

"""
        
        week3 = [d for d in self.directories if d["category"] in ["Business Directories", "Social Media"]][:25]
        for i, d in enumerate(week3, 1):
            content += f"{i}. **{d['name']}** ({d['rating']}⭐)\n"
            content += f"   - {d['url']}\n\n"
        
        content += """
### 4주차 (전문가 플랫폼 + 나머지)
**목표**: 나머지 모두 등록 완료

"""
        
        week4 = [d for d in self.directories if d["category"] == "Healthcare Professionals"]
        for i, d in enumerate(week4, 1):
            content += f"{i}. **{d['name']}** ({d['rating']}⭐)\n"
            content += f"   - {d['url']}\n\n"
        
        content += f"""
---

## 📊 예상 성과

### 1개월 후
- ✅ 백링크: 50~80개
- ✅ Domain Authority: +10~15
- ✅ 검색 순위: 상승 시작

### 3개월 후
- ✅ 백링크: 100+ 개
- ✅ Domain Authority: +20~25
- ✅ "Incheon dentist" 1페이지 진입
- ✅ 월간 방문자: 500+ 명

### 6개월 후
- ✅ 백링크: 100+ 개 유지
- ✅ Domain Authority: +30
- ✅ "Incheon dentist" TOP 3
- ✅ 월간 방문자: 1,000~2,000명

---

## ✅ 일일 체크리스트

매일 등록 후 체크:
- [ ] NAP 정보 일관성 확인
- [ ] 웹사이트 URL 정확성 확인
- [ ] 카테고리 적절성 확인
- [ ] 설명문 품질 확인
- [ ] 이미지 업로드 (가능한 경우)
- [ ] 진행 상황 기록

---

**작성 시스템**: 백링크 자동화 도구  
**최종 업데이트**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
"""
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✅ 주간 계획 생성 완료: {filename}")
        return filename
    
    def print_summary(self):
        """백링크 현황 요약 출력"""
        print("\n" + "="*70)
        print("🔗 백링크 자동화 시스템 - 연세미다스치과")
        print("="*70)
        print(f"\n📊 총 디렉토리 수: {len(self.directories)}개\n")
        
        # 카테고리별 집계
        category_count = {}
        priority_count = {1: 0, 2: 0, 3: 0}
        
        for d in self.directories:
            category = d["category"]
            category_count[category] = category_count.get(category, 0) + 1
            priority_count[d["priority"]] += 1
        
        print("📁 카테고리별 분포:")
        for category, count in sorted(category_count.items(), key=lambda x: x[1], reverse=True):
            print(f"   • {category}: {count}개")
        
        print(f"\n🎯 우선순위별 분포:")
        print(f"   • 우선순위 1 (최우선): {priority_count[1]}개")
        print(f"   • 우선순위 2 (중요): {priority_count[2]}개")
        print(f"   • 우선순위 3 (일반): {priority_count.get(3, 0)}개")
        
        print(f"\n✅ 완료: {len(self.progress['completed'])}개")
        print(f"🔄 진행 중: {len(self.progress['in_progress'])}개")
        print(f"⏳ 대기 중: {len(self.progress['pending'])}개")
        
        if self.progress["last_updated"]:
            print(f"\n🕐 마지막 업데이트: {self.progress['last_updated']}")
        
        print("\n" + "="*70 + "\n")


def main():
    """메인 실행 함수"""
    print("""
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║     🔗 백링크 자동화 시스템                                  ║
║     연세미다스치과 SEO 최적화 도구                           ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
    """)
    
    automation = BacklinkAutomation()
    
    while True:
        print("\n📋 메뉴:")
        print("1. 백링크 현황 요약 보기")
        print("2. CSV 템플릿 생성 (Excel용)")
        print("3. JSON 데이터 내보내기")
        print("4. HTML 체크리스트 생성")
        print("5. 우선순위별 사이트 자동 오픈")
        print("6. 주간 등록 계획 생성")
        print("7. 모든 파일 생성 (일괄)")
        print("0. 종료")
        
        choice = input("\n선택 (0-7): ").strip()
        
        if choice == "1":
            automation.print_summary()
        
        elif choice == "2":
            automation.export_submission_template()
            print("\n✅ CSV 파일을 Excel에서 열어 백링크 등록에 활용하세요!")
        
        elif choice == "3":
            automation.export_json_data()
            print("\n✅ JSON 파일을 개발자 도구에서 활용하세요!")
        
        elif choice == "4":
            html_file = automation.generate_html_checklist()
            print(f"\n✅ HTML 체크리스트 생성 완료!")
            print(f"   브라우저에서 열기: {html_file}")
            
            open_browser = input("\n브라우저에서 바로 열까요? (y/n): ").strip().lower()
            if open_browser == 'y':
                webbrowser.open(html_file)
        
        elif choice == "5":
            priority = input("\n우선순위 선택 (1, 2): ").strip()
            if priority in ['1', '2']:
                delay = input("사이트 오픈 간격 (초, 기본 5초): ").strip()
                delay = int(delay) if delay.isdigit() else 5
                
                confirm = input(f"\n⚠️  우선순위 {priority} 사이트들을 {delay}초 간격으로 열까요? (y/n): ").strip().lower()
                if confirm == 'y':
                    automation.open_directories_by_priority(int(priority), delay)
                else:
                    print("취소되었습니다.")
            else:
                print("❌ 올바른 우선순위를 선택하세요.")
        
        elif choice == "6":
            automation.generate_weekly_plan()
            print("\n✅ 4주 등록 계획이 생성되었습니다!")
        
        elif choice == "7":
            print("\n🚀 모든 파일 생성 중...")
            automation.export_submission_template()
            automation.export_json_data()
            automation.generate_html_checklist()
            automation.generate_weekly_plan()
            print("\n✅ 모든 파일이 생성되었습니다!")
            print("\n생성된 파일:")
            print("   • backlink_submission_template.csv")
            print("   • backlink_data.json")
            print("   • backlink_checklist.html")
            print("   • weekly_backlink_plan.md")
        
        elif choice == "0":
            print("\n👋 백링크 자동화 시스템을 종료합니다.")
            print("SEO 성공을 기원합니다! 🚀\n")
            break
        
        else:
            print("❌ 올바른 번호를 선택하세요.")


if __name__ == "__main__":
    main()
