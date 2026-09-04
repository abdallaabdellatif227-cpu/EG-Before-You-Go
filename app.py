import json
import streamlit as st
from pathlib import Path

try:
    from google import genai
    from google.genai import types
except Exception:
    genai = None
    types = None


DATA_FILE = Path(__file__).with_name("data.json")
with DATA_FILE.open(encoding="utf-8") as file:
    SERVICE_DATA = json.load(file)


# ============================================================
# DEFAULT JOB CATEGORIES
# ============================================================
# The original data.json currently contains companies only.
# These defaults make the Restaurant / Hotel / Online Job
# sections work immediately without requiring manual JSON edits.
#
# If you later add your own data under these same keys in
# data.json, the app will keep your data and only use these
# defaults for missing/empty categories.

DEFAULT_JOB_DATA = {
    "restaurants": {
        "mcdonalds_egypt": {
            "title": "McDonald's Egypt",
            "icon": "🍔",
            "sector": "مطاعم ووجبات سريعة",
            "application_method": "التقديم أونلاين من خلال صفحة وظائف المطاعم الرسمية، ويمكن التقديم على وظائف Crew وغيرها.",
            "link": "https://www.mcdonalds.eg/learn/people/careers/restaurant-careers",
            "common_positions": [
                "Crew Member",
                "Manager Trainee",
                "Guest Experience Leader",
                "McCafé",
                "Delivery Rider"
            ],
            "requirements": [
                "إكمال بيانات طلب التقديم المطلوبة.",
                "بيانات شخصية ووسيلة تواصل صحيحة.",
                "الاستعداد للعمل في بيئة سريعة والتعامل مع العملاء.",
                "الاستعداد لنظام العمل والورديات حسب الوظيفة."
            ],
            "location": "فروع McDonald's في مصر — حسب الوظيفة والفرع.",
            "notes": "الموقع الرسمي يعرض وظائف المطاعم مثل Crew Member وManager Trainee وغيرها. المتطلبات الفعلية تختلف حسب الوظيفة.",
            "sources": "https://www.mcdonalds.eg/learn/people/careers/restaurant-careers"
        }
    },
    "hotels": {
        "hilton_egypt": {
            "title": "Hilton Hotels",
            "icon": "🏨",
            "sector": "فنادق وضيافة",
            "application_method": "التقديم أونلاين من خلال بوابة Hilton Careers والبحث عن الوظائف المتاحة في مصر.",
            "link": "https://jobs.hilton.com/",
            "common_positions": [
                "Front Office",
                "Food & Beverage",
                "Sales",
                "Human Resources",
                "Marketing",
                "Accounting",
                "Kitchen",
                "Housekeeping"
            ],
            "requirements": [
                "اختيار وظيفة مناسبة من بوابة Hilton Careers.",
                "إنشاء/استخدام ملف المتقدم وإرسال الطلب.",
                "المتطلبات تختلف حسب الوظيفة والفندق."
            ],
            "location": "فنادق Hilton في مصر — حسب الوظيفة المتاحة.",
            "notes": "بوابة Hilton الرسمية تعرض وظائف ومسارات فندقية، وتشمل وظائف مثل Front Office وFood & Beverage وSales وHR وHousekeeping. لا تدفع أي رسوم للتوظيف.",
            "sources": "https://jobs.hilton.com/"
        }
    },
    "online_platforms": {
        "wuzzuf_egypt": {
            "title": "WUZZUF",
            "icon": "💻",
            "sector": "وظائف أونلاين / البحث عن وظائف في مصر",
            "application_method": "أنشئ حسابًا، ابحث عن الوظيفة المناسبة، ثم قدّم من خلال إعلان الوظيفة.",
            "link": "https://wuzzuf.net/jobs/egypt",
            "common_positions": [
                "خدمة عملاء",
                "مبيعات",
                "IT / Software",
                "تصميم وإبداع",
                "عمل من المنزل",
                "Internships"
            ],
            "requirements": [
                "إنشاء حساب على WUZZUF.",
                "إكمال الملف الشخصي ورفع CV عند الحاجة.",
                "اختيار الوظيفة ومراجعة شروط الإعلان قبل التقديم."
            ],
            "location": "أونلاين — الوظائف تختلف بين Remote وHybrid وOn-site حسب الإعلان.",
            "notes": "WUZZUF منصة وظائف في مصر وتعرض وظائف بمستويات ومجالات مختلفة، ومنها وظائف Work From Home.",
            "sources": "https://wuzzuf.net/jobs/egypt"
        }
    }
}

JOB_MARKET_SEED_DATA = {
    "data_analytics": {
        "vodafone_data_analyst": {
            "id": "vodafone_data_analyst",
            "title": "Data Analyst (VOIS)",
            "company": "Vodafone / VOIS",
            "companyLogo": None,
            "category": "Data & Analytics",
            "subcategory": "Data Analytics",
            "location": "Cairo, Egypt",
            "country": "Egypt",
            "city": "Cairo",
            "workType": "On-site",
            "employmentType": "Full Time",
            "contractType": "Permanent",
            "remoteType": "Hybrid",
            "postedDate": "2026-08-25",
            "applicationDeadline": None,
            "salary": "Not disclosed",
            "salaryMin": None,
            "salaryMax": None,
            "salaryCurrency": "EGP",
            "salaryPeriod": None,
            "salaryType": "Not disclosed",
            "salarySource": "Not disclosed",
            "experienceLevel": "Mid-Senior",
            "experienceYears": "3+",
            "education": "Bachelor's degree in Engineering, Information Technology or related field",
            "requirements": [
                "Engineering / Information Technology or related degree",
                "Minimum 3 years experience in data engineering, analytics or related technical domains",
                "Google Cloud Platform",
                "Tableau",
                "Grafana",
                "Power BI",
                "Kibana",
                "Python",
                "APIs",
                "Data pipelines",
                "Data warehouses",
                "AI/ML knowledge is advantageous"
            ],
            "skills": ["SQL", "Python", "Tableau", "Power BI", "GCP", "APIs", "Data Pipelines"],
            "responsibilities": [
                "Analyze and interpret operational and business data",
                "Build dashboards and reporting solutions",
                "Support data pipelines and analytics workflows",
                "Partner with business and technical teams to improve data quality"
            ],
            "documentsRequired": ["CV"],
            "applicationMethod": "Apply Online",
            "contactEmail": None,
            "contactPhone": None,
            "contactPerson": None,
            "applyUrl": "https://careers.vodafone.com/egypt/",
            "sourceUrl": "https://careers.vodafone.com/egypt/",
            "sourceName": "Vodafone Careers",
            "status": "active",
            "verified": True,
            "lastVerified": "2026-08-31",
            "description": "Data Analyst role focused on data analysis, dashboards, APIs, cloud environments, and data quality across business and technical workflows.",
            "tags": ["data", "analytics", "gcp", "python", "tableau", "vodafone"]
        },
        "wfp_data_analyst_sc5": {
            "id": "wfp_data_analyst_sc5",
            "title": "Data Analyst SC5",
            "company": "World Food Programme (WFP)",
            "companyLogo": None,
            "category": "Data & Analytics",
            "subcategory": "Data Analysis",
            "location": "Cairo, Egypt",
            "country": "Egypt",
            "city": "Cairo",
            "workType": "On-site",
            "employmentType": "Full Time",
            "contractType": "Contract",
            "remoteType": "On-site",
            "postedDate": "2026-08-01",
            "applicationDeadline": None,
            "salary": "Official compensation information only if available in the vacancy",
            "salaryMin": None,
            "salaryMax": None,
            "salaryCurrency": "EGP",
            "salaryPeriod": None,
            "salaryType": "Not disclosed",
            "salarySource": "Official",
            "experienceLevel": "Mid",
            "experienceYears": "2+",
            "education": "University degree in Computer Science, Information Systems, Statistics, Economics or related field",
            "requirements": [
                "University degree in Computer Science, Information Systems, Statistics, Economics or related field",
                "Minimum 2 years relevant experience",
                "SQL",
                "Tableau",
                "Data modeling",
                "Data quality",
                "Data analysis"
            ],
            "skills": ["SQL", "Tableau", "Data Modeling", "Data Quality", "Data Analysis"],
            "responsibilities": [
                "Support data analysis and reporting activities",
                "Maintain quality and consistency of datasets",
                "Provide analysis for program and operational decisions"
            ],
            "documentsRequired": ["CV", "Cover Letter"],
            "applicationMethod": "WFP Workday portal",
            "contactEmail": None,
            "contactPhone": None,
            "contactPerson": None,
            "applyUrl": "https://www.wfp.org/careers",
            "sourceUrl": "https://www.wfp.org/careers",
            "sourceName": "WFP Careers",
            "status": "active",
            "verified": True,
            "lastVerified": "2026-08-31",
            "description": "Data Analyst role responsible for working with data quality, reporting, and analytical support for WFP program operations.",
            "tags": ["wfp", "data", "analytics", "tableau", "sql"]
        }
    },
    "finance_accounting": {
        "itida_accountant": {
            "id": "itida_accountant",
            "title": "Accountant",
            "company": "ITIDA",
            "companyLogo": None,
            "category": "Finance / Accounting",
            "subcategory": "Accounting",
            "location": "Smart Village, Giza",
            "country": "Egypt",
            "city": "Giza",
            "workType": "On-site",
            "employmentType": "Full Time",
            "contractType": "Permanent",
            "remoteType": "On-site",
            "postedDate": "2026-08-01",
            "applicationDeadline": None,
            "salary": "Not disclosed",
            "salaryMin": None,
            "salaryMax": None,
            "salaryCurrency": "EGP",
            "salaryPeriod": None,
            "salaryType": "Not disclosed",
            "salarySource": "Not disclosed",
            "experienceLevel": "Entry-Level",
            "experienceYears": "0-2",
            "education": "Bachelor's degree in Accounting, Finance or related field",
            "requirements": [
                "Bachelor's degree in Accounting, Finance or related field",
                "0-2 years experience",
                "Strong academic performance",
                "Accounting principles",
                "Microsoft Excel",
                "Pivot Tables",
                "VLOOKUP",
                "English",
                "Report writing"
            ],
            "skills": ["Accounting", "Excel", "Pivot Tables", "VLOOKUP", "Reporting"],
            "responsibilities": [
                "Support accounting operations and report preparation",
                "Maintain financial records and data accuracy",
                "Assist with reconciliations and operational reporting"
            ],
            "documentsRequired": ["CV"],
            "applicationMethod": "Email application",
            "contactEmail": "careers@itida.gov.eg",
            "contactPhone": None,
            "contactPerson": None,
            "applyUrl": "https://itida.gov.eg/",
            "sourceUrl": "https://itida.gov.eg/",
            "sourceName": "ITIDA Careers",
            "status": "active",
            "verified": True,
            "lastVerified": "2026-08-31",
            "description": "Accounting role focused on financial records, reporting, and supporting finance operations in a government-linked technology institution.",
            "tags": ["accounting", "finance", "excel", "itida", "reporting"]
        }
    },
    "software_engineering": {
        "capgemini_software_engineer": {
            "id": "capgemini_software_engineer",
            "title": "Software Engineer",
            "company": "Capgemini",
            "companyLogo": None,
            "category": "Software Engineering",
            "subcategory": "Backend / Full Stack",
            "location": "Cairo, Egypt",
            "country": "Egypt",
            "city": "Cairo",
            "workType": "Hybrid",
            "employmentType": "Full Time",
            "contractType": "Permanent",
            "remoteType": "Hybrid",
            "postedDate": "2026-08-20",
            "applicationDeadline": None,
            "salary": "Not disclosed",
            "salaryMin": None,
            "salaryMax": None,
            "salaryCurrency": "EGP",
            "salaryPeriod": None,
            "salaryType": "Not disclosed",
            "salarySource": "Not disclosed",
            "experienceLevel": "Professional",
            "experienceYears": "2+",
            "education": "Bachelor's degree in Computer Science, Engineering or related field",
            "requirements": [
                "Bachelor's degree in Computer Science or related field",
                "2+ years software engineering experience",
                "Java, Python, or .NET",
                "REST APIs",
                "SQL",
                "Git",
                "Problem solving"
            ],
            "skills": ["Java", "Python", "SQL", "REST APIs", "Git"],
            "responsibilities": [
                "Develop and maintain enterprise software solutions",
                "Support integration with internal and external services",
                "Collaborate with cross-functional engineering teams"
            ],
            "documentsRequired": ["CV"],
            "applicationMethod": "Apply Online",
            "contactEmail": None,
            "contactPhone": None,
            "contactPerson": None,
            "applyUrl": "https://www.capgemini.com/careers/",
            "sourceUrl": "https://www.capgemini.com/careers/",
            "sourceName": "Capgemini Careers",
            "status": "active",
            "verified": True,
            "lastVerified": "2026-08-31",
            "description": "Software engineering opportunity for building scalable enterprise solutions and collaborating with distributed teams.",
            "tags": ["software", "engineering", "java", "python", "capgemini"]
        }
    },
    "sales": {
        "bosta_sales_specialist": {
            "id": "bosta_sales_specialist",
            "title": "Sales Specialist",
            "company": "Bosta",
            "companyLogo": None,
            "category": "Sales",
            "subcategory": "Business Development",
            "location": "Cairo, Egypt",
            "country": "Egypt",
            "city": "Cairo",
            "workType": "On-site",
            "employmentType": "Full Time",
            "contractType": "Permanent",
            "remoteType": "On-site",
            "postedDate": "2026-08-15",
            "applicationDeadline": None,
            "salary": "Not disclosed",
            "salaryMin": None,
            "salaryMax": None,
            "salaryCurrency": "EGP",
            "salaryPeriod": None,
            "salaryType": "Not disclosed",
            "salarySource": "Not disclosed",
            "experienceLevel": "Junior-Mid",
            "experienceYears": "1+",
            "education": "Bachelor's degree preferred",
            "requirements": [
                "Bachelor's degree preferred",
                "1+ years sales experience",
                "Strong communication skills",
                "Customer relationship management",
                "Negotiation"
            ],
            "skills": ["Sales", "Negotiation", "CRM", "Customer Service"],
            "responsibilities": [
                "Drive sales pipeline and customer engagement",
                "Maintain client relationships and follow-ups",
                "Support operational sales targets"
            ],
            "documentsRequired": ["CV"],
            "applicationMethod": "Apply Online",
            "contactEmail": None,
            "contactPhone": None,
            "contactPerson": None,
            "applyUrl": "https://www.bosta.co/careers",
            "sourceUrl": "https://www.bosta.co/careers",
            "sourceName": "Bosta Careers",
            "status": "active",
            "verified": True,
            "lastVerified": "2026-08-31",
            "description": "Sales specialist role with focus on business development, client relationships, and revenue growth.",
            "tags": ["sales", "crm", "b2b", "bosta"]
        }
    },
    "marketing": {
        "raya_marketing_specialist": {
            "id": "raya_marketing_specialist",
            "title": "Marketing Specialist",
            "company": "Raya",
            "companyLogo": None,
            "category": "Marketing",
            "subcategory": "Digital Marketing",
            "location": "Cairo, Egypt",
            "country": "Egypt",
            "city": "Cairo",
            "workType": "Hybrid",
            "employmentType": "Full Time",
            "contractType": "Permanent",
            "remoteType": "Hybrid",
            "postedDate": "2026-08-18",
            "applicationDeadline": None,
            "salary": "Not disclosed",
            "salaryMin": None,
            "salaryMax": None,
            "salaryCurrency": "EGP",
            "salaryPeriod": None,
            "salaryType": "Not disclosed",
            "salarySource": "Not disclosed",
            "experienceLevel": "Mid",
            "experienceYears": "2+",
            "education": "Bachelor's degree in Marketing, Business or related field",
            "requirements": [
                "Bachelor's degree in Marketing, Business or related field",
                "2+ years digital marketing experience",
                "Social media strategy",
                "Performance marketing",
                "Content creation",
                "Analytics" 
            ],
            "skills": ["Digital Marketing", "Social Media", "Google Ads", "Analytics"],
            "responsibilities": [
                "Plan and execute digital marketing campaigns",
                "Drive social media content and performance growth",
                "Monitor channel analytics and optimize campaigns"
            ],
            "documentsRequired": ["CV"],
            "applicationMethod": "Apply Online",
            "contactEmail": None,
            "contactPhone": None,
            "contactPerson": None,
            "applyUrl": "https://www.raya.com/careers",
            "sourceUrl": "https://www.raya.com/careers",
            "sourceName": "Raya Careers",
            "status": "active",
            "verified": True,
            "lastVerified": "2026-08-31",
            "description": "Marketing specialist role covering digital marketing, campaign execution, social media, and optimization.",
            "tags": ["marketing", "digital", "social media", "raya"]
        }
    }
}

# Only fill missing/empty categories. User-provided data remains the priority.
if not isinstance(SERVICE_DATA.get("jobs"), dict):
    SERVICE_DATA["jobs"] = {}

for _job_category, _job_items in DEFAULT_JOB_DATA.items():
    if not isinstance(SERVICE_DATA["jobs"].get(_job_category), dict):
        SERVICE_DATA["jobs"][_job_category] = {}
    if not SERVICE_DATA["jobs"][_job_category]:
        SERVICE_DATA["jobs"][_job_category] = _job_items

if not isinstance(SERVICE_DATA.get("job_market"), dict):
    SERVICE_DATA["job_market"] = {}

for _market_category, _market_jobs in JOB_MARKET_SEED_DATA.items():
    if not isinstance(SERVICE_DATA["job_market"].get(_market_category), dict):
        SERVICE_DATA["job_market"][_market_category] = {}
    for _job_id, _job_data in _market_jobs.items():
        SERVICE_DATA["job_market"][_market_category].setdefault(_job_id, _job_data)

# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Before You Go",
    page_icon="logo.png.jpg",
    layout="wide",
    initial_sidebar_state="collapsed"
)
if "splash_shown" not in st.session_state:
    st.session_state.splash_shown = True
    st.markdown("""
    <style>
    /* إلغاء أي transform على العناصر اللي بتحبس الـ fixed positioning */
    .stApp,
    [data-testid="stAppViewContainer"],
    [data-testid="stMain"],
    .main,
    .block-container {
        transform: none !important;
    }

    @keyframes spin-arrow {
        from { transform: rotate(0deg); }
        to { transform: rotate(360deg); }
    }
    @keyframes fade-out-splash {
        0%, 75% { opacity: 1; visibility: visible; }
        100% { opacity: 0; visibility: hidden; }
    }
    #splash-screen {
        position: fixed !important;
        top: 0 !important; left: 0 !important;
        width: 100vw !important; height: 100vh !important;
        z-index: 2147483647 !important;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        background: linear-gradient(135deg, #06101c 0%, #0a1929 50%, #071522 100%);
        animation: fade-out-splash 1.8s ease forwards;
        pointer-events: none;
    }
    #splash-compass {
        width: 70px; height: 70px;
        border: 4px solid #B8924A;
        border-radius: 50%;
        display: flex; align-items: center; justify-content: center;
    }
    #splash-arrow {
        width: 0; height: 0;
        border-left: 8px solid transparent;
        border-right: 8px solid transparent;
        border-bottom: 26px solid #B8924A;
        animation: spin-arrow 1s linear infinite;
    }
    #splash-text {
        margin-top: 18px;
        color: #ffffff;
        font-size: 18px;
        font-weight: 700;
    }
    </style>
    <div id="splash-screen">
        <div id="splash-compass"><div id="splash-arrow"></div></div>
        <div id="splash-text">قبل ما تروح</div>
    </div>
    """, unsafe_allow_html=True)

# ============================================================
# SESSION STATE
# ============================================================

if "page" not in st.session_state:
    st.session_state.page = "home"

if "selected_document" not in st.session_state:
    st.session_state.selected_document = None

if "language" not in st.session_state:
    st.session_state.language = "ar"

if "light_mode" not in st.session_state:
    st.session_state.light_mode = False

if "page_history" not in st.session_state:
    st.session_state.page_history = []



    
TEXTS = {
    "ar": {
        "language": "اللغة",
        "arabic": "العربية",
        "english": "English",
        "brand": "قبل ما تروح",
        "tagline": "اعرف كل حاجة قبل ما تتحرك.",
        "hero_subtitle": "اعرف كل حاجة قبل ما تنزل من البيت.",
        "search": "بحث",
        "search_placeholder": "🔎 ابحث عن خدمة، ورقة، معاملة أو مكان...",
        "what_to_do": "ماذا تريد أن تفعل؟",
        "popular": "خدمات شائعة",
        "documents": "استخراج أوراق",
        "documents_desc": "اعرف المستندات والخطوات والمكان المناسب.",
        "services": "معاملات وخدمات",
        "services_desc": "اعرف الجهة والمواعيد والأوراق المطلوبة.",
        "medical": "كشف طبي",
        "medical_desc": "اعرف الطبيب والمواعيد والمكان قبل ما تروح.",
        "jobs": "تقديم لوظيفة",
        "jobs_desc": "اعرف مكان التقديم ومواعيد الـHR.",
        "home": "الرئيسية",
        "search_nav": "البحث",
        "light_mode": "☀️ الوضع الفاتح",
        "back": "← رجوع",
        "not_available": "الخدمة دي لسه مش موجودة في النسخة الحالية.",
        "footer": "قبل ما تروح — اعرف قبل ما تتحرك.",
    },
    "en": {
        "language": "Language",
        "arabic": "العربية",
        "english": "English",
        "brand": "Before You Go",
        "tagline": "Know everything before you head out.",
        "hero_subtitle": "Know everything before leaving home.",
        "search": "Search",
        "search_placeholder": "🔎 Search for a service, document, transaction, or place...",
        "what_to_do": "What would you like to do?",
        "popular": "Popular services",
        "documents": "Get documents",
        "documents_desc": "Find the required documents, steps, and location.",
        "services": "Transactions and services",
        "services_desc": "Find the office, hours, and required documents.",
        "medical": "Medical checkup",
        "medical_desc": "Find the doctor, hours, and location before you go.",
        "jobs": "Apply for a job",
        "jobs_desc": "Find the application location and HR hours.",
        "home": "Home",
        "search_nav": "Search",
        "light_mode": "☀️ Light mode",
        "back": "Back →",
        "not_available": "This service is not available in the current version.",
        "footer": "Before You Go — know before you head out.",
    },
}

def text(key):
    try:
        lang = st.session_state.get("language", "ar")
        return TEXTS.get(lang, TEXTS["ar"]).get(key, key)
    except:
        return key

SERVICE_EN = {
    "تنسيق المدارس الثانوية": {
        "title": "Secondary School Coordination",
        "description": "Online and offline school coordination services"
    }
}

MEDICAL_EN = {
    "marriage_health_certificate": {
        "title": "Premarital Health Certificate",
        "description": "Health screening before marriage"
    }
}


# ============================================================
# NAVIGATION
# ============================================================

def go(page):
    """Navigate to a page while remembering the current page."""
    current_page = st.session_state.get("page", "home")

    if current_page != page:
        st.session_state.page_history.append(current_page)

    st.session_state.page = page
    st.rerun()


def home():
    """Go directly to the home page and clear navigation history."""
    st.session_state.page = "home"
    st.session_state.page_history = []
    st.session_state.selected_document = None
    st.rerun()


def back():
    """Return to the immediately previous page."""
    if st.button(text("back"), key="back_button"):
        history = st.session_state.get("page_history", [])

        if history:
            previous_page = history.pop()
            st.session_state.page_history = history
            st.session_state.page = previous_page
        else:
            st.session_state.page = "home"

        st.rerun()


# ============================================================
# SMART CHATBOT HELPERS
# ============================================================


def build_reference_snapshot():
    """Create a compact factual reference for the chatbot without overwhelming the model."""
    snapshot = {}

    for section_name in ("services", "additional_services", "medical_services"):
        section = SERVICE_DATA.get(section_name, {})
        if isinstance(section, dict):
            for key, value in section.items():
                if not isinstance(value, dict):
                    continue
                snapshot[f"{section_name}.{key}"] = {
                    "title": value.get("title") or key,
                    "online_available": value.get("online_available"),
                    "fees": value.get("fees") or {},
                    "duration": value.get("duration") or {},
                    "documents": value.get("documents") or value.get("cases_and_documents") or {},
                    "location": value.get("location"),
                    "working_hours": value.get("working_hours"),
                    "sources": value.get("sources"),
                }

    for label, group in (("SERVICE_EN", SERVICE_EN), ("MEDICAL_EN", MEDICAL_EN)):
        if isinstance(group, dict):
            for key, value in group.items():
                if not isinstance(value, dict):
                    continue
                snapshot[f"{label}.{key}"] = {
                    "title": value.get("title") or key,
                    "online_available": value.get("online_available"),
                    "fees": value.get("fees") or {},
                    "duration": value.get("duration") or {},
                    "documents": value.get("documents") or value.get("cases_and_documents") or {},
                    "location": value.get("location"),
                    "working_hours": value.get("working_hours"),
                    "sources": value.get("sources"),
                }

    jobs_section = SERVICE_DATA.get("jobs", {})
    if isinstance(jobs_section, dict):
        for category_name, category_items in jobs_section.items():
            if not isinstance(category_items, dict):
                continue
            for key, value in category_items.items():
                if not isinstance(value, dict):
                    continue
                snapshot[f"jobs.{category_name}.{key}"] = {
                    "title": value.get("title") or key,
                    "sector": value.get("sector"),
                    "application_method": value.get("application_method"),
                    "common_positions": value.get("common_positions"),
                    "requirements": value.get("requirements"),
                    "location": value.get("location"),
                    "notes": value.get("notes"),
                    "sources": value.get("sources"),
                }

    real_jobs = SERVICE_DATA.get("job_market", {})
    if isinstance(real_jobs, dict):
        for category_name, category_items in real_jobs.items():
            if not isinstance(category_items, dict):
                continue
            for key, value in category_items.items():
                if not isinstance(value, dict):
                    continue
                snapshot[f"job_market.{category_name}.{key}"] = {
                    "id": value.get("id") or key,
                    "title": value.get("title") or key,
                    "company": value.get("company"),
                    "category": value.get("category"),
                    "subcategory": value.get("subcategory"),
                    "location": value.get("location"),
                    "country": value.get("country"),
                    "city": value.get("city"),
                    "workType": value.get("workType"),
                    "employmentType": value.get("employmentType"),
                    "contractType": value.get("contractType"),
                    "remoteType": value.get("remoteType"),
                    "postedDate": value.get("postedDate"),
                    "salary": value.get("salary"),
                    "experienceYears": value.get("experienceYears"),
                    "education": value.get("education"),
                    "requirements": value.get("requirements"),
                    "skills": value.get("skills"),
                    "responsibilities": value.get("responsibilities"),
                    "documentsRequired": value.get("documentsRequired"),
                    "applicationMethod": value.get("applicationMethod"),
                    "applyUrl": value.get("applyUrl"),
                    "sourceUrl": value.get("sourceUrl"),
                    "sourceName": value.get("sourceName"),
                    "verified": value.get("verified"),
                    "status": value.get("status"),
                    "description": value.get("description"),
                    "tags": value.get("tags")
                }

    return json.dumps(snapshot, ensure_ascii=False, indent=2)


def build_chat_system_prompt():
    language = st.session_state.get("language", "ar")
    reference = build_reference_snapshot()

    if language == "ar":
        system_prompt = f"""
أنت مساعد ذكي وصديق داخل تطبيق "قبل ما تروح" في مصر.

قواعد أساسية:
1) استخدم بيانات التطبيق أولًا عندما تكون المعلومة موجودة في المرجع أدناه.
2) المرجع الأساسي داخل التطبيق هو: {reference}
3) إذا كانت المعلومة غير موجودة في المرجع، أو كانت قابلة للتغيير، أو تحتاج تحديثًا، استخدم Google Search للبحث عن معلومات حديثة.
4) عند استخدام Google Search، اعتمد على مصادر موثوقة، ويفضل المصادر الرسمية للجهات الحكومية والشركات.
5) لا تختلق أسعار أو مواعيد أو خطوات أو أماكن أو روابط.
6) إذا لم تجد بعد البحث مصدرًا موثوقًا، قل بوضوح إنك لم تجد معلومة موثوقة.
7) اكتب رد عربي بسيط وودّي، زي محادثة طبيعية ومباشرة، لا بأسلوب رسمي جدًا.
8) استخدم نقاط واضحة وسهلة القراءة.
9) إذا السؤال ناقص أو غير واضح، اطلب معلومة واحدة فقط تساعدك في الإجابة بدقة.
10) إذا كان السؤال عن خدمة، اذكر: الاسم، التكلفة، المدة، المستندات، المكان، ومواعيد العمل إن وجدت.
11) لا تذكر التخمينات أو "أفترض" أو "أعتقد".
12) لو المستخدم طلب الإنجليزية، أجب بالإنجليزية فقط.
13) اكتب الرد كاملًا دايمًا ولا تقطعه في نص الجملة أو الكلمة، حتى لو محتاج تلخيص أكتر.
"""
    else:
        system_prompt = f"""
You are a friendly, smart assistant inside "Before You Go".

Hard rules:
1) Use the app data first when the information is available in the reference below.
2) The primary in-app reference is: {reference}
3) If information is missing from the reference, may have changed, or needs an up-to-date check, use Google Search to find current information.
4) When using Google Search, prefer trustworthy sources, especially official government or company sources.
5) Do not invent fees, dates, steps, locations, or links.
6) If you cannot find a trustworthy source after searching, clearly say that you could not find reliable information.
7) Reply in a natural, warm, conversational way, not too formal.
8) Use clear bullet points when useful.
9) If the question is unclear or missing key details, ask for only one missing detail to answer accurately.
10) If the question is about a service, include: name, fee, duration, documents, location, and working hours when available.
11) Do not mention assumptions, guesses, or "I think".
12) Keep the answer short, useful, and grounded in the available data and search results.
"""

    return system_prompt.strip()


def get_chat_client():
    if genai is None or types is None:
        return None

    try:
        api_key = st.secrets["GEMINI_API_KEY"]
    except Exception:
        api_key = None

    if not api_key:
        return None

    try:
        return genai.Client(api_key=api_key)
    except Exception:
        return None


def is_safe_chat_answer(answer: str | None) -> bool:
    if not answer:
        return False

    lower = answer.lower()
    forbidden = [
        "i think",
        "probably",
        "maybe",
        "i am not sure",
        "as an ai model",
    ]
    return not any(item in lower for item in forbidden)


def extract_model_text(response) -> str | None:
    text = getattr(response, "text", None)
    if isinstance(text, str) and text.strip():
        return text.strip()

    try:
        candidates = getattr(response, "candidates", None) or []
        if candidates:
            parts = getattr(candidates[0], "content", None)
            if parts is not None:
                content = getattr(parts, "parts", None) or []
                for part in content:
                    if hasattr(part, "text") and part.text:
                        return part.text.strip()
                    if isinstance(part, dict):
                        text_value = part.get("text")
                        if isinstance(text_value, str) and text_value.strip():
                            return text_value.strip()
    except Exception:
        pass

    return None


if "chat_history" not in st.session_state:
    st.session_state.chat_history = []


def flatten_job_market():
    flattened = []
    for category_name, category_items in SERVICE_DATA.get("job_market", {}).items():
        if not isinstance(category_items, dict):
            continue
        for item_key, item in category_items.items():
            if not isinstance(item, dict):
                continue
            item_copy = dict(item)
            item_copy["_category_name"] = category_name
            item_copy["_item_key"] = item_key
            flattened.append(item_copy)
    return flattened


def render_chatbot_area():
    language = st.session_state.get("language", "ar")
    st.markdown("## 🤖 مساعد Before You Go")

    client = get_chat_client()
    if client is None or types is None:
        if language == "ar":
            st.warning("لم يتم تفعيل مفتاح Gemini. أضف المفتاح في st.secrets['GEMINI_API_KEY'].")
        else:
            st.warning("Gemini is not active. Add your key in st.secrets['GEMINI_API_KEY'].")
        return

    for message in st.session_state.chat_history:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    prompt_placeholder = "اسأل عن أي خدمة أو مستند..." if language == "ar" else "Ask about any service or document..."
    prompt = st.chat_input(prompt_placeholder)

    if prompt is not None:
        user_msg = {"role": "user", "content": prompt}
        st.session_state.chat_history.append(user_msg)

        with st.chat_message("user"):
            st.markdown(prompt)

        system_prompt = build_chat_system_prompt()
        prompt_text = "\n\n".join(f"{item['role']}: {item['content']}" for item in st.session_state.chat_history)

        with st.chat_message("assistant"):
            with st.spinner("جارٍ تجهيز الإجابة..." if language == "ar" else "Preparing answer..."):
                try:
                    chat = client.chats.create(
                        model="gemini-3.5-flash-lite",
                        config=types.GenerateContentConfig(
                            system_instruction=system_prompt,
                            tools=[],
                            temperature=0.2,
                            top_p=0.8,
                            max_output_tokens=1500,
                        ),
                    )
                    response = chat.send_message(prompt_text)
                    answer = extract_model_text(response)

                    if answer is None:
                        answer = "المعلومة غير موجودة في بيانات التطبيق الحالية." if language == "ar" else "This information is not available in the current app data."

                    if not is_safe_chat_answer(answer):
                        answer = "المعلومة غير موجودة في بيانات التطبيق الحالية." if language == "ar" else "This information is not available in the current app data."

                    if len(str(answer).strip()) < 30:
                        if language == "ar":
                            answer = "أقدر أساعدك، بس عايز أعرف تفاصيل أكتر عشان أديك إجابة دقيقة: النوع، المدينة، وهل أنت عايز الأوراق فقط ولا الخطوات كاملة؟"
                        else:
                            answer = "I can help, but I need one more detail so I can answer accurately: what service, which city, and do you want the documents only or the full process?"

                    st.markdown(answer)
                    st.session_state.chat_history.append({"role": "assistant", "content": answer})
                except Exception:
                    import traceback
                    error_details = traceback.format_exc()
                    print("=== GEMINI CHAT ERROR ===")
                    print(error_details)
                    print("==========================")

                    fallback = "حدثت مشكلة أثناء الاتصال بـ Gemini. برجاء التحقق من المفتاح أو الاتصال بالإنترنت." if language == "ar" else "There was a problem connecting to Gemini. Please check the key and internet connection."
                    st.error(fallback)

                    debug_label = "🔧 تفاصيل الخطأ (لأغراض التشخيص)" if language == "ar" else "🔧 Error details (for diagnosis)"
                    with st.expander(debug_label):
                        st.code(error_details)

                    st.session_state.chat_history.append({"role": "assistant", "content": fallback})


# ============================================================
# DESIGN
# ============================================================

st.markdown("""
<style>

/* =========================================================
   GLOBAL
   ========================================================= */

.stApp {
    background:
        radial-gradient(
            circle at 8% 8%,
            rgba(0, 210, 190, 0.18),
            transparent 30%
        ),
        radial-gradient(
            circle at 92% 18%,
            rgba(80, 100, 255, 0.18),
            transparent 35%
        ),
        linear-gradient(
            135deg,
            #06101c 0%,
            #0a1929 50%,
            #071522 100%
        );

    color: #ffffff;
}

.block-container {
    max-width: 1250px;
    padding-top: 1.2rem;
    padding-bottom: 3rem;
}


/* =========================================================
   RTL
   ========================================================= */
.stApp {
    direction: ltr;
}

.block-container {
    direction: ltr;
    text-align: right;
}

section[data-testid="stSidebar"] {
    direction: rtl;
    left: 0;
    right: auto;
    transform: none !important;
}

div[data-testid="stSidebarCollapsedControl"] {
    left: 0.5rem;
    right: auto;
}


/* =========================================================
   HERO
   ========================================================= */

.hero-space {
    height: 15px;
}


/* =========================================================
   HEADINGS
   ========================================================= */

h1 {
    font-weight: 850 !important;
    letter-spacing: -0.8px;
}

h2 {
    font-weight: 800 !important;
}

h3 {
    font-weight: 750 !important;
}


/* =========================================================
   COLUMN SPACING
   ========================================================= */

div[data-testid="stColumn"] {
    flex: 1 1 0% !important;
    width: 0 !important;
    min-width: 0 !important;
    padding-left: 7px !important;
    padding-right: 7px !important;
}

div[data-testid="stElementContainer"] {
    width: 100% !important;
}

div[data-testid="stButton"] {
    width: 100% !important;
    direction: rtl;
}

div[data-testid="stMarkdownContainer"],
div[data-testid="stTextInput"] {
    direction: rtl;
}


/* =========================================================
   ALL BUTTONS
   حجم مناسب للشاشة
   ========================================================= */

.stButton > button {
    width: 100% !important;
    height: 160px;
    min-height: 160px;

    border-radius: 22px;
    border: 1px solid rgba(255,255,255,0.13);

    background:
        linear-gradient(
            145deg,
            rgba(255,255,255,0.10),
            rgba(255,255,255,0.045)
        );

    color: #ffffff;

    font-size: 20px;
    font-weight: 750;

    padding: 16px;

    margin-bottom: 8px;

    box-shadow:
        0 10px 30px rgba(0,0,0,0.16);

    white-space: pre-line;
    line-height: 1.45;

    transition:
        transform 0.18s ease,
        background 0.18s ease,
        border 0.18s ease,
        box-shadow 0.18s ease;
}

.stButton > button [data-testid="stMarkdownContainer"] {
    width: 100%;
    text-align: center;
}

.stButton > button [data-testid="stMarkdownContainer"] p {
    margin: 5px 0;
    font-size: 21px !important;
    font-weight: 750 !important;
    line-height: 1.55 !important;
    white-space: normal !important;
    overflow: visible !important;
    text-overflow: clip !important;
}

.big-category .stButton > button [data-testid="stMarkdownContainer"] p {
    font-size: 23px !important;
    font-weight: 800 !important;
}

.big-category .stButton > button [data-testid="stMarkdownContainer"] p:last-child {
    margin-top: 18px !important;
    padding-top: 14px !important;
    border-top: 1px solid rgba(255,255,255,0.15);
    font-size: 15px !important;
    font-weight: 500 !important;
    opacity: 0.8;
}

.verified-badge {
    position: relative !important;
    display: inline-flex !important;
    align-items: center !important;
    justify-content: center !important;
    width: fit-content !important;
    max-width: calc(100% - 18px) !important;
    margin: -10px 0 8px 18px !important;
    padding: 6px 12px !important;
    border-radius: 999px !important;
    background: rgba(38, 201, 147, 0.18) !important;
    border: 1px solid rgba(98, 224, 174, 0.7) !important;
    color: #dffef3 !important;
    font-size: 11px !important;
    font-weight: 700 !important;
    letter-spacing: 0.2px !important;
    line-height: 1.25 !important;
    white-space: nowrap !important;
    overflow: hidden !important;
    text-overflow: ellipsis !important;
    z-index: 5 !important;
    box-shadow: inset 0 0 0 1px rgba(255,255,255,0.04), 0 8px 20px rgba(34, 197, 94, 0.14);
}

.verified-badge::before {
    content: "✓";
    display: inline-flex;
    align-items: center;
    justify-content: center;
    width: 16px;
    height: 16px;
    margin-right: 7px;
    border-radius: 50%;
    background: rgba(16, 185, 129, 0.25);
    color: #bbf7d0;
    font-size: 11px;
    font-weight: 900;
    line-height: 1;
}

[class*="st-key-job_market_"] .stButton > button {
    height: auto !important;
    min-height: 190px !important;
    padding: 18px !important;
    border-radius: 20px !important;
    overflow: hidden !important;
    align-items: flex-start !important;
    text-align: right !important;
}

[class*="st-key-job_market_"] .stButton > button [data-testid="stMarkdownContainer"] p {
    font-size: 14px !important;
    font-weight: 600 !important;
    line-height: 1.35 !important;
    margin: 3px 0 !important;
    white-space: normal !important;
    overflow-wrap: break-word !important;
}

[class*="st-key-job_market_"] .stButton > button [data-testid="stMarkdownContainer"] p:first-child {
    font-size: 17px !important;
    font-weight: 800 !important;
}

[class*="st-key-job_market_"] .stButton > button [data-testid="stMarkdownContainer"] p:nth-child(2) {
    font-size: 15px !important;
    font-weight: 700 !important;
    opacity: 0.9 !important;
}

[class*="st-key-home_documents"] .stButton > button [data-testid="stMarkdownContainer"] p,
[class*="st-key-home_medical"] .stButton > button [data-testid="stMarkdownContainer"] p,
[class*="st-key-home_services"] .stButton > button [data-testid="stMarkdownContainer"] p,
[class*="st-key-home_jobs"] .stButton > button [data-testid="stMarkdownContainer"] p {
    font-size: 23px !important;
    font-weight: 800 !important;
}

.quick-button .stButton > button [data-testid="stMarkdownContainer"] p {
    font-size: 18px !important;
}

[class*="st-key-additional_"] .stButton > button {
    height: 145px;
    min-height: 145px;
    padding: 14px;
    border-radius: 20px;
}

[class*="st-key-additional_"] .stButton > button [data-testid="stMarkdownContainer"] p {
    margin: 3px 0;
    font-size: 13px !important;
    font-weight: 650 !important;
    line-height: 1.25 !important;
}

[class*="st-key-additional_"] .stButton > button [data-testid="stMarkdownContainer"] p:first-child {
    font-size: 20px !important;
}

[class*="st-key-additional_"] .stButton > button [data-testid="stMarkdownContainer"] p:nth-child(2) {
    font-size: 16px !important;
    font-weight: 800 !important;
}

[class*="st-key-medical_"] .stButton > button {
    height: 145px;
    min-height: 145px;
    padding: 14px;
}

[class*="st-key-medical_"] .stButton > button [data-testid="stMarkdownContainer"] p {
    margin: 3px 0;
    font-size: 13px !important;
    font-weight: 650 !important;
    line-height: 1.25 !important;
}

[class*="st-key-medical_"] .stButton > button [data-testid="stMarkdownContainer"] p:first-child {
    font-size: 20px !important;
}

[class*="st-key-medical_"] .stButton > button [data-testid="stMarkdownContainer"] p:nth-child(2) {
    font-size: 16px !important;
    font-weight: 800 !important;
}

.stButton > button:hover {
    transform: translateY(-4px);

    background:
        linear-gradient(
            145deg,
            rgba(255,255,255,0.15),
            rgba(255,255,255,0.065)
        );

    border-color:
        rgba(70,220,205,0.60);

    box-shadow:
        0 18px 42px rgba(0,0,0,0.28);
}


/* =========================================================
   HOME CATEGORY CARDS
   ========================================================= */

.big-category {
    width: 100% !important;
}

.big-category div[data-testid="stButton"] {
    width: 100% !important;
}

.big-category .stButton > button {
    width: 100% !important;
    height: auto;
    min-height: 160px;

    border-radius: 24px;

    font-size: 21px;
    font-weight: 750;

    padding: 18px;

    margin-bottom: 10px;

    box-shadow:
        0 14px 38px rgba(0,0,0,0.20);
}

.big-category .stButton > button:hover {
    transform:
        translateY(-5px)
        scale(1.008);

    box-shadow:
        0 22px 52px rgba(0,0,0,0.32);
}


/* =========================================================
   QUICK BUTTONS
   ========================================================= */

.quick-button .stButton > button {
    height: 68px;
    min-height: 68px;

    border-radius: 17px;

    font-size: 16px;

    padding: 12px;

    margin-bottom: 0;
}


/* =========================================================
   DOCUMENT CARDS
   ========================================================= */

.document-card .stButton > button {
    min-height: 145px;
}


/* =========================================================
   SEARCH
   ========================================================= */

div[data-testid="stTextInput"] input {
    background: rgba(255,255,255,0.075);

    border:
        1px solid rgba(255,255,255,0.15);

    border-radius: 18px;

    color: #ffffff;

    padding: 16px;

    font-size: 17px;
}

div[data-testid="stTextInput"] input:focus {
    border-color:
        rgba(70,220,205,0.70);

    box-shadow:
        0 0 0 2px rgba(70,220,205,0.12);
}


/* =========================================================
   INFO BOX
   ========================================================= */

.info-box {
    background:
        linear-gradient(
            145deg,
            rgba(255,255,255,0.095),
            rgba(255,255,255,0.045)
        );

    border:
        1px solid rgba(255,255,255,0.13);

    border-radius: 22px;

    padding: 22px;

    margin: 8px 0;

    min-height: 135px;

    box-shadow:
        0 10px 30px rgba(0,0,0,0.17);
}

.requirements-box {
    direction: ltr;
    text-align: left;
    background: linear-gradient(145deg, rgba(255,255,255,0.095), rgba(255,255,255,0.045));
    border: 1px solid rgba(255,255,255,0.13);
    border-radius: 22px;
    padding: 22px 30px;
    margin: 8px 0;
    color: #ffffff;
    box-shadow: 0 10px 30px rgba(0,0,0,0.17);
}

.requirements-box h3 {
    text-align: right;
}

.requirements-box ul {
    margin: 12px 0 0;
    padding-left: 24px;
}

.requirements-box li {
    padding: 4px 0;
    font-size: 18px;
    font-weight: 650;
    line-height: 1.6;
}

.requirements-box li::marker {
    color: #ffffff;
    font-size: 1.1em;
}


/* =========================================================
   BACK BUTTON
   ========================================================= */

.back-wrapper {
    width: fit-content !important;
}

.back-wrapper .stButton {
    width: fit-content !important;
}

.back-wrapper .stButton > button {
    width: auto !important;
    min-width: 120px !important;
    max-width: 180px !important;
    height: 45px !important;
    min-height: 45px !important;
    padding: 7px 18px !important;
    border-radius: 13px !important;
    font-size: 15px !important;
    margin-bottom: 10px !important;
}


/* =========================================================
   DIVIDERS
   ========================================================= */

hr {
    border-color:
        rgba(255,255,255,0.10);
}


/* =========================================================
   SIDEBAR
   ========================================================= */

section[data-testid="stSidebar"] {
    background:
        linear-gradient(
            180deg,
            #071522,
            #06101c
        );
}

section[data-testid="stSidebar"] .stButton > button {
    height: 50px;
    min-height: 50px;

    font-size: 16px;

    border-radius: 14px;

    margin-bottom: 6px;
}


/* =========================================================
   SMALL BUTTON
   ========================================================= */

.small-button .stButton > button {
    min-height: 55px !important;

    border-radius: 15px !important;

    font-size: 16px !important;
}


/* =========================================================
   FOOTER
   ========================================================= */

.footer {
    text-align: center;

    color: #718096;

    margin-top: 30px;

    font-size: 14px;
}


/* =========================================================
   FLOATING CHAT BUTTON
   ========================================================= */

div[class*="st-key-floating_chat_button"] {
    position: fixed !important;
    right: 28px !important;
    bottom: 28px !important;
    z-index: 999999 !important;
    width: 72px !important;
    height: 72px !important;
}

div[class*="st-key-floating_chat_button"] .stButton {
    width: 72px !important;
}

div[class*="st-key-floating_chat_button"] .stButton > button {
    width: 72px !important;
    height: 72px !important;
    min-height: 72px !important;
    padding: 0 !important;
    margin: 0 !important;
    border-radius: 50% !important;
    border: 1px solid rgba(255,255,255,0.25) !important;
    background: linear-gradient(145deg, rgba(0, 210, 190, 0.95), rgba(50, 110, 255, 0.95)) !important;
    color: white !important;
    font-size: 30px !important;
    font-weight: 700 !important;
    box-shadow: 0 12px 35px rgba(0,0,0,0.35), 0 0 0 4px rgba(0,210,190,0.10) !important;
    transition: transform 0.2s ease, box-shadow 0.2s ease !important;
}

div[class*="st-key-floating_chat_button"] .stButton > button:hover {
    transform: scale(1.08) !important;
    box-shadow: 0 16px 42px rgba(0,0,0,0.40), 0 0 0 7px rgba(0,210,190,0.12) !important;
}


/* =========================================================
   FLOATING SUGGESTION BUTTON
   ========================================================= */

div[class*="st-key-floating_suggestion_button"] {
    position: fixed !important;
    right: 28px !important;
    bottom: 112px !important;
    z-index: 999999 !important;
    width: 58px !important;
    height: 58px !important;
}

div[class*="st-key-floating_suggestion_button"] .stLinkButton {
    width: 58px !important;
}

div[class*="st-key-floating_suggestion_button"] .stLinkButton > a {
    width: 58px !important;
    height: 58px !important;
    min-height: 58px !important;
    padding: 0 !important;
    margin: 0 !important;
    border-radius: 50% !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    border: 1px solid rgba(255,255,255,0.25) !important;
    background: linear-gradient(145deg, #B8924A, #8f6f38) !important;
    color: white !important;
    font-size: 24px !important;
    box-shadow: 0 12px 30px rgba(0,0,0,0.3) !important;
    transition: transform 0.2s ease !important;
}

div[class*="st-key-floating_suggestion_button"] .stLinkButton > a:hover {
    transform: scale(1.08) !important;
}

div[class*="st-key-floating_suggestion_button"] .stLinkButton p {
    display: none !important;
}

@media (max-width: 900px) {
    div[class*="st-key-floating_chat_button"] {
        right: 18px !important;
        bottom: 18px !important;
        width: 60px !important;
        height: 60px !important;
    }

    div[class*="st-key-floating_chat_button"] .stButton {
        width: 60px !important;
    }

    div[class*="st-key-floating_chat_button"] .stButton > button {
        width: 60px !important;
        height: 60px !important;
        min-height: 60px !important;
        font-size: 25px !important;
    }

    div[class*="st-key-floating_suggestion_button"] {
        right: 18px !important;
        bottom: 92px !important;
        width: 48px !important;
        height: 48px !important;
    }

    div[class*="st-key-floating_suggestion_button"] .stLinkButton {
        width: 48px !important;
    }

    div[class*="st-key-floating_suggestion_button"] .stLinkButton > a {
        width: 48px !important;
        height: 48px !important;
        min-height: 48px !important;
        font-size: 20px !important;
    }
}


/* =========================================================
   MOBILE
   ========================================================= */

@media (max-width: 900px) {

    .big-category .stButton > button {
        min-height: 130px;
        font-size: 17px;
        padding: 14px;
    }

    .big-category .stButton > button [data-testid="stMarkdownContainer"] p {
        font-size: 19px !important;
    }

    .document-card .stButton > button {
        min-height: 125px;
    }

    .stButton > button {
        min-height: 115px;
        font-size: 16px;
    }
}

 </style>
""", unsafe_allow_html=True)

content_direction = "rtl" if st.session_state.language == "ar" else "ltr"
content_align = "right" if st.session_state.language == "ar" else "left"
st.markdown(
    f"""
    <style>
    :root {{
        --content-direction: {content_direction};
        --content-align: {content_align};
    }}

    .block-container {{
        direction: {content_direction};
        text-align: {content_align};
    }}

    section[data-testid="stSidebar"] {{
        direction: {content_direction};
        text-align: {content_align};
    }}
    </style>
    """,
    unsafe_allow_html=True
)

if st.session_state.get("light_mode", False):
    st.markdown("""
    <style>
    .stApp {
        background:
            radial-gradient(circle at 8% 8%, rgba(184, 146, 74, 0.08), transparent 32%),
            radial-gradient(circle at 92% 18%, rgba(27, 46, 79, 0.06), transparent 36%),
            linear-gradient(135deg, #fbfaf8 0%, #f5f3ee 52%, #f7f5f0 100%);
        color: #1B2E4F;
    }

    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #f7f5f0 0%, #fbfaf8 100%);
    }

    .stApp h1,
    .stApp h2,
    .stApp h3,
    .stApp h4,
    .stApp p,
    .stApp label,
    .stApp span,
    .stApp li,
    .stApp div[data-testid="stCaptionContainer"],
    .stApp div[data-testid="stMarkdownContainer"],
    .stApp div[data-testid="stSelectbox"] label,
    .stApp div[data-testid="stRadio"] label,
    .stApp div[data-testid="stAlert"] {
        color: #1B2E4F !important;
    }

    div[data-testid="stTextInput"] input::placeholder {
        color: rgba(27, 46, 79, 0.45) !important;
    }

    div[data-testid="stAlert"] {
        background: rgba(27, 46, 79, 0.06) !important;
        border-color: rgba(27, 46, 79, 0.15) !important;
    }

    .stButton > button {
        color: #1B2E4F;
        border-color: rgba(32, 49, 58, 0.14);
        background: linear-gradient(145deg, rgba(255,255,255,0.90), rgba(238,233,222,0.75));
        box-shadow: 0 10px 26px rgba(27, 46, 79, 0.08);
    }

    .stButton > button:hover {
        background: linear-gradient(145deg, rgba(255,255,255,0.98), rgba(232,220,197,0.85));
        border-color: rgba(184, 146, 74, 0.55);
        box-shadow: 0 16px 34px rgba(184, 146, 74, 0.14);
    }

    div[data-testid="stTextInput"] input {
        color: #1B2E4F;
        background: rgba(255,255,255,0.85);
        border-color: rgba(27, 46, 79, 0.16);
    }

    .footer {
        color: #6b7684;
    }
    </style>
    """, unsafe_allow_html=True)


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:
    st.image("logo.png.jpg", width=140)
    st.markdown(f"### {text('brand')}")

    st.caption(text("tagline"))

    language = st.selectbox(
        text("language"),
        ["ar", "en"],
        format_func=lambda value: TEXTS[value]["arabic"] if value == "ar" else TEXTS[value]["english"],
        key="language_selector"
    )
    if language != st.session_state.language:
        st.session_state.language = language
        st.rerun()

    light_mode = st.toggle(
        text("light_mode"),
        value=st.session_state.light_mode,
        key="light_mode_toggle"
    )

    if light_mode != st.session_state.light_mode:
        st.session_state.light_mode = light_mode
        st.rerun()

    st.divider()

    if st.button(f"🏠 {text('home')}", key="nav_home", use_container_width=True):
        home()

    if st.button(f"🔎 {text('search_nav')}", key="nav_search", use_container_width=True):
        go("search")

    if st.button(f"📄 {text('documents')}", key="nav_documents", use_container_width=True):
        go("documents")

    if st.button(f"🩺 {text('medical')}", key="nav_medical", use_container_width=True):
        go("medical")

    if st.button(f"💼 {text('jobs')}", key="nav_jobs", use_container_width=True):
        go("jobs")

    if st.button("💬 مساعد ذكي", key="nav_chatbot", use_container_width=True):
        go("chatbot")

    st.divider()

    st.caption("Prototype 0.1")


# ============================================================
# HOME
# ============================================================

if st.session_state.page == "home":

    st.markdown(
        '<div class="hero-space"></div>',
        unsafe_allow_html=True
    )

    st.title(text('brand'))

    st.subheader(text("hero_subtitle"))

    st.write("")

    # --------------------------------------------------------
    # SEARCH
    # --------------------------------------------------------

    search = st.text_input(
        text("search"),
        placeholder=text("search_placeholder"),
        label_visibility="collapsed",
        key="home_search"
    )

    if search:

        if "جواز" in search:

            st.info("وجدنا: 🛂 استخراج جواز سفر")

            if st.button(
                "🛂 فتح خدمة استخراج جواز السفر",
                key="search_passport_home"
            ):
                st.session_state.selected_document = "passport"
                go("document_details")

        elif "بطاقة" in search:

            st.info("وجدنا: 🪪 بطاقة الرقم القومي")

            if st.button(
                "🪪 فتح خدمة بطاقة الرقم القومي",
                key="search_id_home"
            ):
                st.session_state.selected_document = "id"
                go("document_details")

        elif "تأمين" in search:

            st.info("وجدنا: 📋 برنت تأميني")

            if st.button(
                "📋 فتح خدمة البرنت التأميني",
                key="search_insurance_home"
            ):
                st.session_state.selected_document = "insurance"
                go("document_details")

        else:

            st.info(
                    "الخدمة دي لسه مش موجودة في النسخة الحالية."
                )

    # --------------------------------------------------------
    # MAIN CATEGORIES
    # --------------------------------------------------------

    st.markdown(f"### {text('what_to_do')}")

    col1, col2 = st.columns(
        [1, 1],
        gap="small"
    )
    with col1:

        st.markdown(
            '<div class="big-category">',
            unsafe_allow_html=True
        )

        if st.button(
            f"📄\n\n{text('documents')}\n\n{text('documents_desc')}",
            key="home_documents"
        ):
            go("documents")

        st.markdown(
            "</div>",
            unsafe_allow_html=True
        )

    with col2:

        st.markdown(
            '<div class="big-category">',
            unsafe_allow_html=True
        )

        if st.button(
            f"🩺\n\n{text('medical')}\n\n{text('medical_desc')}",
            key="home_medical"
        ):
            go("medical")

        st.markdown(
            "</div>",
            unsafe_allow_html=True
        )


    st.markdown(
        '<div class="big-category">',
        unsafe_allow_html=True
    )

    if st.button(
        f"💼\n\n{text('jobs')}\n\n{text('jobs_desc')}",
        key="home_jobs"
    ):
        go("jobs")

    st.markdown(
        "</div>",
        unsafe_allow_html=True
    )


    # --------------------------------------------------------
    # QUICK SERVICES
    # --------------------------------------------------------

    st.markdown(f"### {text('popular')}")

    q1, q2, q3 = st.columns(3)

    with q1:

        st.markdown(
            '<div class="quick-button">',
            unsafe_allow_html=True
        )

        if st.button(
            "🛂 جواز سفر",
            key="quick_passport"
        ):
            st.session_state.selected_document = "passport"
            go("document_details")

        st.markdown(
            "</div>",
            unsafe_allow_html=True
        )


    with q2:

        st.markdown(
            '<div class="quick-button">',
            unsafe_allow_html=True
        )

        if st.button(
            "📋 برنت تأميني",
            key="quick_insurance"
        ):
            st.session_state.selected_document = "insurance"
            go("document_details")

        st.markdown(
            "</div>",
            unsafe_allow_html=True
        )


    with q3:

        st.markdown(
            '<div class="quick-button">',
            unsafe_allow_html=True
        )

        if st.button(
            "🪪 بطاقة شخصية",
            key="quick_id"
        ):
            st.session_state.selected_document = "id"
            go("document_details")

        st.markdown(
            "</div>",
            unsafe_allow_html=True
        )


    # --------------------------------------------------------
    # FOOTER
    # --------------------------------------------------------

    st.markdown(
        '<div class="footer">'
        'قبل ما تروح — اعرف قبل ما تتحرك.'
        '</div>',
        unsafe_allow_html=True
    )


# ============================================================
# DOCUMENTS
# ============================================================

elif st.session_state.page == "documents":

    st.markdown(
        '<div class="back-wrapper">',
        unsafe_allow_html=True
    )

    back()

    st.markdown(
        '</div>',
        unsafe_allow_html=True
    )

    st.title("📄 استخراج أوراق")

    st.write(
        "اختار الورقة اللي عايز تعرف تفاصيلها."
    )

    col1, col2 = st.columns(2)

    with col1:

        st.markdown(
            '<div class="document-card">',
            unsafe_allow_html=True
        )

        if st.button(
            "🛂\n\nجواز سفر مصري\n\n"
            "اعرف الشروط والخطوات.",
            key="documents_passport"
        ):
            st.session_state.selected_document = "passport"
            go("document_details")

        st.markdown(
            "</div>",
            unsafe_allow_html=True
        )


        st.markdown(
            '<div class="document-card">',
            unsafe_allow_html=True
        )

        if st.button(
            "🪪\n\nبطاقة الرقم القومي\n\n"
            "اعرف طريقة الاستخراج.",
            key="documents_id"
        ):
            st.session_state.selected_document = "id"
            go("document_details")

        st.markdown(
            "</div>",
            unsafe_allow_html=True
        )


        st.markdown(
            '<div class="document-card">',
            unsafe_allow_html=True
        )

        if st.button(
            "📋\n\nبرنت تأميني\n\n"
            "معلومات التأمين الخاص بك.",
            key="documents_insurance"
        ):
            st.session_state.selected_document = "insurance"
            go("document_details")

        st.markdown(
            "</div>",
            unsafe_allow_html=True
        )


    with col2:

        st.markdown(
            '<div class="document-card">',
            unsafe_allow_html=True
        )

        if st.button(
            "🎓\n\nمستندات تعليمية\n\n"
            "اعرف الأوراق المطلوبة.",
            key="documents_education"
        ):
            st.session_state.selected_document = "education"
            go("document_details")

        st.markdown(
            "</div>",
            unsafe_allow_html=True
        )


        st.markdown(
            '<div class="document-card">',
            unsafe_allow_html=True
        )

        if st.button(
            "📜\n\nشهادات ومستندات\n\n"
            "اعرف طريقة استخراجها.",
            key="documents_certificates"
        ):
            st.session_state.selected_document = "certificates"
            go("document_details")

        st.markdown(
            "</div>",
            unsafe_allow_html=True
        )


    st.markdown("## خدمات إضافية")

    additional_services = SERVICE_DATA.get("additional_services", {})
    additional_items = list(additional_services.items())

    for row_start in range(0, len(additional_items), 3):
        additional_columns = st.columns(3)
        for column, (service_key, service) in zip(
            additional_columns,
            additional_items[row_start:row_start + 3]
        ):
            with column:
                if st.button(
                    f"{service.get('icon', '📄')}\n\n{service['title']}\n\n"
                    "اعرف الرسوم والمستندات والمواعيد.",
                    key=f"additional_{service_key}"
                ):
                    st.session_state.selected_document = f"additional:{service_key}"
                    go("document_details")


# ============================================================
# DOCUMENT DETAILS
# ============================================================

elif st.session_state.page == "document_details":

    st.markdown(
        '<div class="back-wrapper">',
        unsafe_allow_html=True
    )

    back()

    st.markdown(
        '</div>',
        unsafe_allow_html=True
    )

    document = st.session_state.selected_document
    if document is None:
        st.info("لم يتم اختيار خدمة بعد.")
        st.stop()


    # ========================================================
    # PASSPORT
    # ========================================================

    if document == "passport":

        st.title("🛂 استخراج جواز سفر مصري")

        st.write(
            "كل اللي تحتاج تعرفه قبل ما تروح."
        )

        st.divider()

        st.subheader("📝 نوع الطلب")

        passport_type = st.selectbox(
            "اختار نوع الطلب",
            [
                "استخراج لأول مرة",
                "تجديد",
                "بدل تالف / منتهي",
                "بدل فاقد"
            ]
        )


        st.subheader("👤 مين بيقدم؟")

        age = st.radio(
            "الفئة العمرية",
            [
                "16 سنة أو أكثر",
                "أقل من 16 سنة"
            ],
            horizontal=True
        )


        if age == "16 سنة أو أكثر":

            st.markdown(
                "## 👤 المستندات المطلوبة"
            )

            st.checkbox(
                "بطاقة الرقم القومي سارية وصالحة + صورة",
                value=False,
                disabled=True
            )

            st.checkbox(
                "نموذج 29 جوازات",
                value=False,
                disabled=True
            )

            st.checkbox(
                "4 صور شخصية حديثة بخلفية بيضاء مقاس 4×6",
                value=False,
                disabled=True
            )

            st.checkbox(
                "موقف التجنيد للذكور حسب الحالة",
                value=False,
                disabled=True
            )

            st.checkbox(
                "شهادة المؤهل الدراسي إذا لم تكن مثبتة بالبطاقة",
                value=False,
                disabled=True
            )

            if passport_type != "استخراج لأول مرة":

                st.checkbox(
                    "جواز السفر القديم في حالة التجديد / بدل التالف أو المنتهي",
                    value=False,
                    disabled=True
                )

        else:

            st.markdown(
                "## 👶 القاصر أقل من 16 سنة"
            )

            st.checkbox(
                "شهادة الميلاد المميكنة المدون بها الرقم القومي",
                value=False,
                disabled=True
            )

            st.checkbox(
                "بطاقة الرقم القومي لولي الأمر",
                value=False,
                disabled=True
            )

            st.checkbox(
                "صور شخصية حديثة بخلفية بيضاء",
                value=False,
                disabled=True
            )

            st.info(
                "يتم مراعاة متطلبات ولي الأمر والحالة "
                "طبقًا للإجراءات الرسمية."
            )


        # ====================================================
        # FEES
        # ====================================================

        st.markdown("## 💰 الرسوم")

        fee1, fee2 = st.columns(2)

        with fee1:

            st.markdown(
                """
                <div class="info-box">
                    <h3>🐢 العادي</h3>
                    <h2>1,150 جنيه*</h2>
                    <p>المدة المذكورة: 7–10 أيام*</p>
                </div>
                """,
                unsafe_allow_html=True
            )

        with fee2:

            st.markdown(
                """
                <div class="info-box">
                    <h3>⚡ المستعجل</h3>
                    <h2>1,675 جنيه*</h2>
                    <p>المدة المذكورة: أقل من 24 ساعة / نفس اليوم*</p>
                </div>
                """,
                unsafe_allow_html=True
            )


        # ====================================================
        # LOCATION
        # ====================================================

        st.markdown("## 📍 أين تذهب؟")

        st.info(
            "مهم: ليس كل مواطن لازم يذهب إلى الإدارة العامة "
            "بالعباسية؛ جهة الاختصاص تعتمد على محل الإقامة "
            "والحالة."
        )

        st.markdown(
            """
**الإدارة العامة للجوازات والهجرة والجنسية**

📍 العباسية — القاهرة

🕐 السبت إلى الخميس  
8:00 صباحًا – 2:30 مساءً

الجمعة والعطلات الرسمية: إجازة
"""
        )


        maps_url = (
            "https://www.google.com/maps/search/"
            "?api=1&query="
            "الإدارة+العامة+للجوازات+والهجرة+والجنسية+العباسية+القاهرة"
        )

        st.link_button(
            "📍 افتح الموقع على Google Maps",
            maps_url,
            use_container_width=True
        )


        # ====================================================
        # ONLINE
        # ====================================================

        st.markdown(
            "## 💻 هل أقدر أعملها أونلاين؟"
        )

        st.warning(
            "لا تعتمد على معلومة عامة عن الأونلاين؛ "
            "توفر الخدمة يختلف حسب نوع المعاملة. "
            "استخدم المصدر الرسمي للتأكد."
        )

        official_url = (
            "https://enationality.moi.gov.eg/"
        )

        st.link_button(
            "🔗 البوابة الرسمية للجوازات والهجرة",
            official_url,
            use_container_width=True
        )


        # ====================================================
        # WARNING
        # ====================================================

        st.markdown(
            "## ⚠️ قبل ما تروح"
        )

        st.warning(
            "الرسوم والمدد والإجراءات الحكومية قابلة للتغيير. "
            "راجع المصدر الرسمي قبل التحرك."
        )

        st.caption(
            "المعلومات الأساسية في هذه الصفحة مبنية على البيانات "
            "التي قدمتها، وتحتاج مراجعة نهائية للرسوم قبل نشرها."
        )

        st.caption(
            "آخر تحديث للمشروع: أغسطس 2026"
        )


        st.markdown(
            "## 🔗 المصادر الرسمية"
        )

        st.write(
            "وزارة الداخلية المصرية — الإدارة العامة للجوازات والهجرة والجنسية"
        )

        st.markdown(
            "https://enationality.moi.gov.eg/"
        )

        st.write(
            "وزارة الداخلية — أقسام محافظة القاهرة واختصاصات الجوازات"
        )

        st.markdown(
            "https://moi.gov.eg/Passports/Home/CairoGovernmentDepartments"
        )


    # ========================================================
    # NATIONAL ID
    # ========================================================

    elif document == "id":

        st.title("🪪 بطاقة الرقم القومي")

        st.write(
            "كل اللي تحتاج تعرفه قبل ما تروح تستخرج أو تجدد بطاقتك."
        )

        st.divider()

        st.subheader("📝 نوع الطلب")

        id_type = st.selectbox(
            "اختار نوع الطلب",
            [
                "استخراج لأول مرة",
                "تجديد (البطاقة قربت تخلص / خلصت)",
                "بدل فاقد",
                "بدل تالف",
                "تحديث بيانات (زواج / طلاق / تغيير عنوان)"
            ]
        )


        st.markdown(
            "## 📄 المستندات المطلوبة"
        )


        if id_type == "استخراج لأول مرة":

            st.checkbox(
                "شهادة الميلاد المميكنة (مدون بها الرقم القومي)",
                value=False,
                disabled=True
            )

            st.checkbox(
                "مستند يثبت محل الإقامة (إيصال كهرباء/مياه حديث أو عقد إيجار موثق)",
                value=False,
                disabled=True
            )

            st.checkbox(
                "مستند يثبت المهنة (خطاب من جهة العمل أو كارنيه نقابة)",
                value=False,
                disabled=True
            )

            st.checkbox(
                "صور شخصية حديثة إذا طُلبت",
                value=False,
                disabled=True
            )

            st.info(
                "لازم تحضر بنفسك أول مرة. لو عندك أكتر من 16 سنة و6 شهور "
                "وما استخرجتش البطاقة، فيه غرامة تأخير (~100 جنيه)."
            )


        elif id_type == "تجديد (البطاقة قربت تخلص / خلصت)":

            st.checkbox(
                "البطاقة القديمة (سارية أو منتهية)",
                value=False,
                disabled=True
            )

            st.checkbox(
                "مستند إثبات محل الإقامة لو اتغير",
                value=False,
                disabled=True
            )

            st.checkbox(
                "مستند إثبات المهنة لو اتغيرت",
                value=False,
                disabled=True
            )

            st.info(
                "البطاقة بتتجدد كل 7 سنين. تقدر تجددها أونلاين من غير ما تروح."
            )


        elif id_type == "بدل فاقد":

            st.checkbox(
                "محضر فقد من قسم الشرطة (في بعض الحالات)",
                value=False,
                disabled=True
            )

            st.checkbox(
                "أي بيانات أو صورة قديمة من البطاقة المفقودة إن وجدت",
                value=False,
                disabled=True
            )

            st.checkbox(
                "مستند إثبات محل الإقامة",
                value=False,
                disabled=True
            )


        elif id_type == "بدل تالف":

            st.checkbox(
                "البطاقة التالفة نفسها",
                value=False,
                disabled=True
            )

            st.checkbox(
                "مستند إثبات محل الإقامة لو اتغير",
                value=False,
                disabled=True
            )


        else:

            st.checkbox(
                "البطاقة الحالية",
                value=False,
                disabled=True
            )

            st.checkbox(
                "مستند رسمي يثبت التغيير (قسيمة زواج/طلاق، عقد إيجار جديد...)",
                value=False,
                disabled=True
            )

            st.info(
                "المهلة القانونية لتحديث البيانات بعد أي تغيير هي 3 شهور."
            )


        # ====================================================
        # FEES
        # ====================================================

        st.markdown(
            "## 💰 الرسوم (حسب سرعة الاستلام)"
        )

        st.caption(
            "الأسعار بتتفاوت شوية حسب المصدر والمكتب — اعتبرها تقريبية "
            "وراجع السجل المدني أو المنصة الرسمية قبل الدفع."
        )

        fee1, fee2, fee3 = st.columns(3)

        with fee1:

            st.markdown(
                """
                <div class="info-box">
                    <h3>🐢 عادي</h3>
                    <h2>~50–65 جنيه*</h2>
                    <p>الاستلام: خلال ~15 يوم*</p>
                </div>
                """,
                unsafe_allow_html=True
            )

        with fee2:

            st.markdown(
                """
                <div class="info-box">
                    <h3>⚡ مستعجل</h3>
                    <h2>~125 جنيه*</h2>
                    <p>الاستلام: خلال ~3 أيام*</p>
                </div>
                """,
                unsafe_allow_html=True
            )

        with fee3:

            st.markdown(
                """
                <div class="info-box">
                    <h3>🚀 VIP</h3>
                    <h2>~175 جنيه*</h2>
                    <p>الاستلام: خلال 24 ساعة*</p>
                </div>
                """,
                unsafe_allow_html=True
            )


        st.caption(
            "فيه كمان فئات فورية أغلى (VIP إكسبريس ~515 جنيه بتسليم خلال "
            "30 دقيقة، وخدمة السيارة النموذجية بالمولات ~800 جنيه بتسليم فوري) "
            "متاحة في مراكز ومولات معينة زي سيتي ستارز وكارفور المعادي."
        )


        # ====================================================
        # LOCATION
        # ====================================================

        st.markdown("## 📍 أين تذهب؟")

        st.info(
            "المكان بيعتمد على محل إقامتك: أقرب مكتب سجل مدني تابع لحيك أو "
            "قسمك. مش كل حد لازم يروح مكتب مركزي معين."
        )

        st.markdown(
            """
**جهة الاختصاص: مكتب السجل المدني التابع لعنوانك**

فيه كمان بدائل أسرع:

- ماكينات السجل المدني الذكية داخل بعض المولات الكبرى
- المراكز النموذجية لخدمات الأحوال المدنية

🕐 غالبًا: السبت إلى الخميس، مواعيد العمل الرسمية

الجمعة والعطلات الرسمية: إجازة
"""
        )


        maps_url_id = (
            "https://www.google.com/maps/search/"
            "?api=1&query=مكتب+السجل+المدني+الاقرب"
        )

        st.link_button(
            "📍 دور على أقرب مكتب سجل مدني على Google Maps",
            maps_url_id,
            use_container_width=True
        )


        # ====================================================
        # ONLINE
        # ====================================================

        st.markdown(
            "## 💻 هل أقدر أعملها أونلاين؟"
        )

        st.warning(
            "التجديد وبدل الفاقد/التالف متاحين أونلاين غالبًا، لكن "
            "الاستخراج لأول مرة بيحتاج حضور شخصي. تأكد من نوع طلبك على "
            "البوابة الرسمية."
        )

        official_url_id = (
            "https://cso.moi.gov.eg/"
        )

        st.link_button(
            "🔗 بوابة خدمات الأحوال المدنية الإلكترونية",
            official_url_id,
            use_container_width=True
        )


        # ====================================================
        # WARNING
        # ====================================================

        st.markdown(
            "## ⚠️ قبل ما تروح"
        )

        st.warning(
            "الرسوم والمدد والإجراءات الحكومية قابلة للتغيير باستمرار. "
            "راجع المصدر الرسمي أو اتصل بالخط الساخن قبل التحرك."
        )

        st.caption(
            "الأرقام والمواعيد في هذه الصفحة تقريبية ومجمّعة من مصادر "
            "متعددة، وتحتاج مراجعة نهائية قبل النشر الرسمي."
        )

        st.caption(
            "آخر تحديث للمشروع: أغسطس 2026"
        )


        # ====================================================
        # SOURCES
        # ====================================================

        st.markdown(
            "## 🔗 المصادر الرسمية"
        )

        st.write(
            "بوابة وزارة الداخلية — خدمات الأحوال المدنية"
        )

        st.markdown(
            "https://cso.moi.gov.eg/"
        )

        st.write(
            "بوابة وزارة الداخلية الرئيسية"
        )

        st.markdown(
            "https://moi.gov.eg/"
        )

        st.write(
            "دليل الخدمات العامة — قطاع الأحوال المدنية"
        )

        st.markdown(
            "https://psm.gov.eg/providers/1/services"
        )


    # ========================================================
    # INSURANCE
    # ========================================================

    elif document == "insurance":

        insurance_data = SERVICE_DATA["services"]["insurance"]

        st.title(f"{insurance_data['icon']} {insurance_data['title']}")

        st.write(
            insurance_data["description"]
        )

        st.divider()

        st.subheader("📌 طرق الاستخراج")

        method1, method2 = st.columns(2)

        with method1:
            method = insurance_data["methods"][0]
            st.markdown(
                f"""
                <div class="info-box">
                    <h3>{method['icon']} {method['type']}</h3>
                    <p>{method['description']}</p>
                </div>
                """,
                unsafe_allow_html=True
            )

        with method2:
            method = insurance_data["methods"][1]
            st.markdown(
                f"""
                <div class="info-box">
                    <h3>{method['icon']} {method['type']}</h3>
                    <p>{method['description']}</p>
                </div>
                """,
                unsafe_allow_html=True
            )

        st.markdown("## 📄 الأوراق المطلوبة")

        requirements_html = "".join(
            f"<li>{item}</li>" for item in insurance_data["required_documents"]
        )

        st.markdown(
            f"""
            <div class="requirements-box" dir="ltr">
                <h3>المطلوب</h3>
                <ul>{requirements_html}</ul>
            </div>
            """,
            unsafe_allow_html=True
        )

        cost1, cost2 = st.columns(2)

        with cost1:
            st.markdown(
                f"""
                <div class="info-box">
                    <h3>💰 التكلفة</h3>
                    <h2>{insurance_data['fee']}</h2>
                    <p>لا توجد رسوم لاستخراج البرنت التأميني.</p>
                </div>
                """,
                unsafe_allow_html=True
            )

        with cost2:
            st.markdown(
                f"""
                <div class="info-box">
                    <h3>🕐 مواعيد العمل</h3>
                    <h2>{insurance_data['location']['working_hours']}</h2>
                    <p>{insurance_data['location']['working_days']}</p>
                </div>
                """,
                unsafe_allow_html=True
            )

        st.markdown("## 📝 الخطوات")

        st.markdown(
            "\n".join(
                f"{index}. {step}"
                for index, step in enumerate(insurance_data["steps"], 1)
            )
        )

        st.markdown("## 📍 المكتب ومواعيد العمل")

        st.info(
            f"اذهب إلى {insurance_data['location']['name']}. "
            f"تبدأ مواعيد العمل من الساعة {insurance_data['location']['working_hours']}، "
            f"من {insurance_data['location']['working_days']}. "
            f"{insurance_data['location']['note']}"
        )

        st.markdown("## 🔗 الروابط والمصادر")

        st.link_button(
            "🌐 افتح بوابة مصر الرقمية",
            insurance_data["online"]["official_url"],
            use_container_width=True
        )

        st.link_button(
            "📖 اقرأ المزيد عن برنت التأمينات",
            insurance_data["sources"][1],
            use_container_width=True
        )

        st.markdown("## ⚠️ قبل ما تروح")

        st.warning(
            "الخدمات والمواعيد والمتطلبات قابلة للتغيير. "
            "راجع بوابة مصر الرقمية أو تواصل مع مكتب التأمينات قبل التحرك."
        )


    # ========================================================
    # EDUCATION
    # ========================================================

    elif isinstance(document, str) and document.startswith("additional:"):

        service_key = document.split(":", 1)[1]
        service = SERVICE_DATA["additional_services"][service_key]
        if st.session_state.language == "en":
            service = {**service, **SERVICE_EN.get(service_key, {})}

        st.title(f"{service.get('icon', '📄')} {service['title']}")
        st.write("كل المعلومات المتاحة عن الخدمة من ملف البيانات.")
        st.divider()

        if service.get("online_available"):
            st.info(f"أونلاين: {service['online_available']}")

        if service.get("fees"):
            st.markdown("## 💰 الرسوم")
            fees = service["fees"]
            fee_columns = st.columns(min(len(fees), 3))
            for fee_column, (fee_name, fee_value) in zip(fee_columns, fees.items()):
                with fee_column:
                    st.markdown(
                        f"""
                        <div class="info-box">
                            <h3>{fee_name}</h3>
                            <h2>{fee_value}</h2>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

        if service.get("duration"):
            st.markdown("## ⏱️ المدة")
            for duration_name, duration_value in service["duration"].items():
                st.markdown(
                    f"**{duration_name}:** {duration_value}"
                )

        documents = service.get("documents", [])
        if service.get("cases_and_documents"):
            st.markdown("## 📄 المستندات المطلوبة")
            for case_name, case_documents in service["cases_and_documents"].items():
                st.markdown(f"### {case_name}")
                for item in case_documents:
                    st.checkbox(item, value=False, disabled=True, key=f"{service_key}_{case_name}_{item}")
        elif documents:
            st.markdown("## 📄 المستندات المطلوبة")
            for item in documents:
                st.checkbox(item, value=False, disabled=True, key=f"{service_key}_{item}")

        if service.get("location"):
            st.markdown("## 📍 المكان ومواعيد العمل")
            st.markdown(
                f"""
                <div class="info-box">
                    <h3>📍 المكان</h3>
                    <p>{service['location']}</p>
                </div>
                """,
                unsafe_allow_html=True
            )
        if service.get("working_hours"):
            st.info(f"🕐 {service['working_hours']}")

        if service.get("link"):
            st.link_button("🔗 افتح الرابط الرسمي", service["link"].split(" ")[0], use_container_width=True)

        if service.get("sources"):
            st.caption(f"المصدر: {service['sources']}")

        st.markdown("## ⚠️ قبل ما تروح")
        st.warning("الرسوم والمواعيد والمستندات قابلة للتغيير. راجع المصدر الرسمي قبل التحرك.")

    elif isinstance(document, str) and document.startswith("medical:"):

        service_key = document.split(":", 1)[1]
        service = SERVICE_DATA["medical_services"][service_key]
        if st.session_state.language == "en":
            service = {**service, **MEDICAL_EN.get(service_key, {})}

        st.title(f"{service.get('icon', '🩺')} {service['title']}")
        st.write("كل المعلومات المتاحة عن الخدمة الصحية من ملف البيانات.")
        st.divider()

        if service.get("online_available"):
            st.info(f"أونلاين: {service['online_available']}")

        if service.get("fees"):
            st.markdown("## 💰 الرسوم")
            fee_columns = st.columns(min(len(service["fees"]), 3))
            for fee_column, (fee_name, fee_value) in zip(fee_columns, service["fees"].items()):
                with fee_column:
                    st.markdown(
                        f"""
                        <div class="info-box">
                            <h3>{fee_name}</h3>
                            <h2>{fee_value}</h2>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

        if service.get("duration"):
            st.markdown("## ⏱️ المدة")
            for duration_name, duration_value in service["duration"].items():
                st.markdown(f"**{duration_name}:** {duration_value}")

        if service.get("cases_and_documents"):
            st.markdown("## 📄 المستندات المطلوبة")
            for case_name, case_documents in service["cases_and_documents"].items():
                st.markdown(f"### {case_name}")
                for item in case_documents:
                    st.checkbox(item, value=False, disabled=True, key=f"medical_{service_key}_{case_name}_{item}")

        st.markdown("## 📍 المكان ومواعيد العمل")
        st.markdown(
            f"""
            <div class="info-box">
                <h3>📍 المكان</h3>
                <p>{service['location']}</p>
            </div>
            """,
            unsafe_allow_html=True
        )
        st.info(f"🕐 {service['working_hours']}")

        if service.get("link"):
            st.link_button("🔗 افتح الرابط الرسمي", service["link"], use_container_width=True)

        st.caption(f"المصدر: {service['sources']}")
        st.markdown("## ⚠️ قبل ما تروح")
        st.warning("الرسوم والمواعيد والمستندات قابلة للتغيير. راجع المصدر الرسمي قبل التحرك.")

    elif isinstance(document, str) and (
        document.startswith("job_company:")
        or document.startswith("job_restaurant:")
        or document.startswith("job_hotel:")
        or document.startswith("job_online:")
    ):

        job_type, company_key = document.split(":", 1)
        category_map = {
            "job_company": "companies",
            "job_restaurant": "restaurants",
            "job_hotel": "hotels",
            "job_online": "online_platforms",
        }
        company_group = SERVICE_DATA.get("jobs", {}).get(category_map[job_type], {})
        company = company_group.get(company_key)

        if not company:
            st.error("الخدمة دي مش موجودة في data.json أو مفتاحها غير صحيح.")
            st.stop()

        st.title(f"{company.get('icon', '🏢')} {company.get('title', company_key)}")
        st.write(company.get("sector", ""))
        st.divider()

        st.info(f"💻 طريقة التقديم: {company.get('application_method', '')}")

        if company.get("common_positions"):
            st.markdown("## 💼 الوظائف المتاحة عادة")
            for position in company["common_positions"]:
                st.markdown(f"- {position}")

        if company.get("requirements"):
            st.markdown("## 📄 متطلبات التقديم")
            for req in company["requirements"]:
                st.checkbox(req, value=False, disabled=True, key=f"jobco_{company_key}_{req}")

        if company.get("location"):
            st.markdown("## 📍 المكان")
            st.markdown(
                f"""
                <div class="info-box">
                    <p>{company['location']}</p>
                </div>
                """,
                unsafe_allow_html=True
            )

        if company.get("notes"):
            st.info(f"ℹ️ {company['notes']}")

        if company.get("link"):
            st.link_button("🔗 افتح بوابة التقديم", company["link"], use_container_width=True)

        if company.get("sources"):
            st.caption(f"المصدر: {company['sources']}")

        if company.get("sources") and not company.get("link"):
            st.link_button("🔗 افتح المصدر", company["sources"], use_container_width=True)

        st.markdown("## ⚠️ قبل ما تقدم")
        st.warning("الوظائف المتاحة والشروط قابلة للتغيير باستمرار. راجع بوابة الشركة الرسمية قبل التقديم.")

    elif isinstance(document, str) and document.startswith("job_market:"):
        job_id = document.split(":", 1)[1]
        job = None

        for category_items in SERVICE_DATA.get("job_market", {}).values():
            if isinstance(category_items, dict):
                job = category_items.get(job_id)
                if job:
                    break

        if not job:
            st.error("الوظيفة المختارة غير موجودة في بيانات job_market.")
            st.stop()

        st.markdown(
            f'<div style="display:flex; justify-content:flex-start; width:100%; margin-bottom: 2px;"><span class="verified-badge">Verified • {job.get("sourceName") or "Official source"}</span></div>',
            unsafe_allow_html=True,
        )
        st.title(f"💼 {job.get('title', job_id)}")
        st.subheader(f"{job.get('company', 'Unknown Company')}")
        st.caption(f"{job.get('category', 'Jobs')} • {job.get('subcategory', '')}")
        st.divider()

        info_cols = st.columns(4)
        with info_cols[0]:
            st.markdown("**📍 الموقع**")
            st.write(job.get("location") or "Not disclosed")
        with info_cols[1]:
            st.markdown("**💼 النوع**")
            st.write(job.get("employmentType") or "Not disclosed")
        with info_cols[2]:
            st.markdown("**🧾 العقد**")
            st.write(job.get("contractType") or "Not disclosed")
        with info_cols[3]:
            st.markdown("**🕒 العمل**")
            st.write(job.get("remoteType") or "Not disclosed")

        st.markdown("## 💰 الراتب")
        salary = job.get("salary") or "الراتب غير موضح"
        salary_status = job.get("salaryType") or "غير موضح"
        st.write(f"{salary} • {salary_status}")

        if job.get("description"):
            st.markdown("## 📝 عن الدور")
            st.write(job["description"])

        if job.get("requirements"):
            st.markdown("## ✅ المتطلبات")
            for req in job["requirements"]:
                st.markdown(f"- {req}")

        if job.get("responsibilities"):
            st.markdown("## 🔧 المسؤوليات")
            for item in job["responsibilities"]:
                st.markdown(f"- {item}")

        if job.get("skills"):
            st.markdown("## 🧠 المهارات")
            st.write(", ".join(job["skills"]))

        if job.get("education"):
            st.markdown("## 🎓 التعليم")
            st.write(job["education"])

        if job.get("experienceYears"):
            st.markdown("## 📈 الخبرة")
            st.write(job["experienceYears"])

        if job.get("documentsRequired"):
            st.markdown("## 📄 المستندات المطلوبة")
            for item in job["documentsRequired"]:
                st.markdown(f"- {item}")

        if job.get("applicationMethod"):
            st.markdown("## 📬 طريقة التقديم")
            st.write(job["applicationMethod"])

        if job.get("contactEmail") or job.get("contactPhone") or job.get("contactPerson"):
            st.markdown("## 📞 التواصل")
            if job.get("contactEmail"):
                st.write(f"البريد: {job['contactEmail']}")
            if job.get("contactPhone"):
                st.write(f"الهاتف: {job['contactPhone']}")
            if job.get("contactPerson"):
                st.write(f"الشخص المسؤول: {job['contactPerson']}")

        if job.get("applyUrl"):
            st.link_button("🚀 قدم الآن", job["applyUrl"], use_container_width=True)

        if job.get("sourceName") or job.get("sourceUrl"):
            st.caption(f"المصدر: {job.get('sourceName') or 'مصدر رسمي'}")
            if job.get("sourceUrl"):
                st.link_button("🔗 عرض الوظيفة الأصلية", job["sourceUrl"], use_container_width=True)

        st.markdown("## ⚠️ قبل ما تقدم")
        st.warning("لا تفترض الراتب أو المواعيد أو المستندات من غير التحقق من الصفحة الرسمية. تحقق من إعلان الوظيفة الرسمي قبل التقديم.")

    elif document == "education":

        st.title("🎓 مستندات تعليمية")

        st.info(
            "هنضيف الخدمات التعليمية واحدة واحدة."
        )


    # ========================================================
    # CERTIFICATES
    # ========================================================

    elif document == "certificates":

        st.title("📜 شهادات ومستندات")

        st.info(
            "هنضيف الشهادات والخدمات هنا."
        )


# ============================================================
# MEDICAL
# ============================================================

elif st.session_state.page == "medical":

    st.markdown(
        '<div class="back-wrapper">',
        unsafe_allow_html=True
    )

    back()

    st.markdown(
        '</div>',
        unsafe_allow_html=True
    )

    st.title("🩺 كشف طبي")

    st.write(
        "اعرف المكان والمواعيد والمطلوب قبل ما تنزل."
    )

    medical_services = SERVICE_DATA.get("medical_services", {})
    medical_columns = st.columns(2)

    for column, (service_key, service) in zip(medical_columns, medical_services.items()):
        with column:
            if st.button(
                f"{service.get('icon', '🩺')}\n\n{service['title']}\n\n"
                "اعرف الرسوم والمستندات والمواعيد.",
                key=f"medical_{service_key}"
            ):
                st.session_state.selected_document = f"medical:{service_key}"
                go("document_details")


# ============================================================
# SERVICES
# ============================================================

elif st.session_state.page == "services":

    st.markdown(
        '<div class="back-wrapper">',
        unsafe_allow_html=True
    )

    back()

    st.markdown(
        '</div>',
        unsafe_allow_html=True
    )

    st.title("🏢 معاملات وخدمات")

    st.write(
        "اختار نوع الجهة أو الخدمة اللي بتدور عليها."
    )

    col1, col2 = st.columns(2)

    with col1:

        if st.button(
            "🏛️ خدمات حكومية",
            key="government",
            use_container_width=True
        ):
            st.info(
                "قسم الخدمات الحكومية قريبًا."
            )

        if st.button(
            "🏫 خدمات تعليمية",
            key="education_services",
            use_container_width=True
        ):
            st.info(
                "قسم الخدمات التعليمية قريبًا."
            )

    with col2:

        if st.button(
            "🏢 شركات",
            key="companies",
            use_container_width=True
        ):
            st.info(
                "قسم الشركات قريبًا."
            )

        if st.button(
            "🏥 جهات طبية",
            key="medical_services",
            use_container_width=True
        ):
            st.info(
                "قسم الجهات الطبية قريبًا."
            )


# ============================================================
# JOBS
# ============================================================

elif st.session_state.page == "jobs":

    st.markdown(
        '<div class="back-wrapper">',
        unsafe_allow_html=True
    )

    back()

    st.markdown(
        '</div>',
        unsafe_allow_html=True
    )

    st.title("💼 تقديم لوظيفة")

    st.write(
        "اعرف مكان التقديم ومواعيد الـHR والمستندات المطلوبة."
    )

    col1, col2 = st.columns(2)

    with col1:

        if st.button(
            "🏢 شركة",
            key="job_company",
            use_container_width=True
        ):
            go("job_companies_list")

        if st.button(
            "🍔 مطعم",
            key="job_restaurant",
            use_container_width=True
        ):
            go("job_restaurants_list")

    with col2:

        if st.button(
            "🏨 فندق",
            key="job_hotel",
            use_container_width=True
        ):
            go("job_hotels_list")

        if st.button(
            "💻 وظيفة أونلاين",
            key="job_online",
            use_container_width=True
        ):
            go("job_online_list")
elif st.session_state.page == "job_restaurants_list":

    st.markdown('<div class="back-wrapper">', unsafe_allow_html=True)
    back()
    st.markdown('</div>', unsafe_allow_html=True)

    st.title("🍔 مطاعم بتوظف")
    st.write("اختار المطعم عشان تعرف كل التفاصيل قبل ما تقدم.")

    restaurants = SERVICE_DATA.get("jobs", {}).get("restaurants", {})

    if not restaurants:
        st.warning("مفيش بيانات مطاعم متاحة حاليًا.")
    restaurant_columns = st.columns(2)

    for index, (item_key, item) in enumerate(restaurants.items()):
        column = restaurant_columns[index % 2]
        with column:
            if st.button(
                f"{item.get('icon', '🍔')}\n\n{item['title']}\n\n{item.get('sector', '')}",
                key=f"job_restaurant_{item_key}",
                use_container_width=True
            ):
                st.session_state.selected_document = f"job_restaurant:{item_key}"
                go("document_details")


elif st.session_state.page == "job_hotels_list":

    st.markdown('<div class="back-wrapper">', unsafe_allow_html=True)
    back()
    st.markdown('</div>', unsafe_allow_html=True)

    st.title("🏨 فنادق بتوظف")
    st.write("اختار الفندق عشان تعرف كل التفاصيل قبل ما تقدم.")

    hotels = SERVICE_DATA.get("jobs", {}).get("hotels", {})

    if not hotels:
        st.warning("مفيش بيانات فنادق متاحة حاليًا.")
    hotel_columns = st.columns(2)

    for index, (item_key, item) in enumerate(hotels.items()):
        column = hotel_columns[index % 2]
        with column:
            if st.button(
                f"{item.get('icon', '🏨')}\n\n{item['title']}\n\n{item.get('sector', '')}",
                key=f"job_hotel_{item_key}",
                use_container_width=True
            ):
                st.session_state.selected_document = f"job_hotel:{item_key}"
                go("document_details")


elif st.session_state.page == "job_online_list":

    st.markdown('<div class="back-wrapper">', unsafe_allow_html=True)
    back()
    st.markdown('</div>', unsafe_allow_html=True)

    st.title("💻 منصات وظائف أونلاين")
    st.write("اختار المنصة عشان تعرف طريقة التسجيل والتقديم.")

    platforms = SERVICE_DATA.get("jobs", {}).get("online_platforms", {})

    if not platforms:
        st.warning("مفيش منصات وظائف أونلاين متاحة حاليًا.")
    platform_columns = st.columns(2)

    for index, (item_key, item) in enumerate(platforms.items()):
        column = platform_columns[index % 2]
        with column:
            if st.button(
                f"{item.get('icon', '💻')}\n\n{item['title']}\n\n{item.get('sector', '')}",
                key=f"job_online_{item_key}",
                use_container_width=True
            ):
                st.session_state.selected_document = f"job_online:{item_key}"
                go("document_details")

# ============================================================
# SEARCH
# ============================================================


elif st.session_state.page == "job_companies_list":

    st.markdown('<div class="back-wrapper">', unsafe_allow_html=True)
    back()
    st.markdown('</div>', unsafe_allow_html=True)

    st.title("🏢 شركات بتوظف")
    st.write("اختار الشركة عشان تعرف كل التفاصيل قبل ما تقدم.")

    companies = SERVICE_DATA.get("jobs", {}).get("companies", {})

    if not companies:
        st.warning("مفيش شركات مضافة حاليًا في data.json تحت jobs → companies.")
    else:
        company_columns = st.columns(2)

        for index, (company_key, company) in enumerate(companies.items()):
            column = company_columns[index % 2]
            with column:
                if st.button(
                    f"{company.get('icon', '🏢')}\n\n{company['title']}\n\n{company.get('sector', '')}",
                    key=f"job_company_{company_key}",
                    use_container_width=True
                ):
                    st.session_state.selected_document = f"job_company:{company_key}"
                    go("document_details")


    real_jobs = flatten_job_market()
    if real_jobs:
        st.markdown("### 📋 Real job listings")
        real_columns = st.columns(2)
        for index, job in enumerate(real_jobs):
            column = real_columns[index % 2]
            with column:
                st.markdown('<div class="job-market-card">', unsafe_allow_html=True)
                source_name = job.get("sourceName") or "Official source"
                st.markdown(
                    f'<div class="verified-badge">Verified • {source_name}</div>',
                    unsafe_allow_html=True,
                )
                job_title = job.get("title", "Job opening")
                company_name = job.get("company", "Company")
                location = job.get("location") or "Location not disclosed"
                work_type = job.get("employmentType") or "Full Time"
                if st.button(
                    f"{job_title}\n\n{company_name}\n\n{location}\n\n{work_type}",
                    key=f"job_market_{job.get('_item_key', job.get('id', index))}",
                    use_container_width=True
                ):
                    st.session_state.selected_document = f"job_market:{job.get('id') or job.get('_item_key')}"
                    go("document_details")
                st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.info("No verified jobs available in this category.")


elif st.session_state.page == "search":

    st.markdown(
        '<div class="back-wrapper">',
        unsafe_allow_html=True
    )

    back()

    st.markdown(
        '</div>',
        unsafe_allow_html=True
    )

    st.title("🔎 البحث")

    query = st.text_input(
        "ابحث",
        placeholder="مثال: جواز سفر"
    )

    if query:

        if "جواز" in query:

            if st.button(
                "🛂 استخراج جاز سفر",
                key="search_passport",
                use_container_width=True
            ):

                st.session_state.selected_document = "passport"

                go("document_details")


        elif "بطاقة" in query:

            if st.button(
                "🪪 بطاقة الرقم القومي",
                key="search_id",
                use_container_width=True
            ):

                st.session_state.selected_document = "id"

                go("document_details")


        elif "تأمين" in query:

            if st.button(
                "📋 برنت تأميني",
                key="search_insurance",
                use_container_width=True
            ):

                st.session_state.selected_document = "insurance"

                go("document_details")


        else:

            st.info(
                "مش لاقي الخدمة دي حاليًا."
            )


elif st.session_state.page == "chatbot":
    st.markdown(
        '<div class="back-wrapper">',
        unsafe_allow_html=True
    )
    back()
    st.markdown('</div>', unsafe_allow_html=True)

    render_chatbot_area()


# ============================================================
# FLOATING BUTTONS (chat + suggestions)
# ============================================================

if st.session_state.page != "chatbot":
    if st.button(
        "💬",
        key="floating_chat_button",
        help="افتح المساعد الذكي",
    ):
        go("chatbot")

    st.link_button(
        "💡",
        "https://docs.google.com/forms/d/e/1FAIpQLSeNLD0K0U2VjaHNVGuBiJdC1pPrnYCwngDEhE9xB-eJHCAJOA/viewform?usp=publish-editor",
        key="floating_suggestion_button",
    )
