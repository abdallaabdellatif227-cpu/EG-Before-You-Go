import json
from pathlib import Path

import streamlit as st


DATA_FILE = Path(__file__).with_name("data.json")
with DATA_FILE.open(encoding="utf-8") as file:
    SERVICE_DATA = json.load(file)

# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="قبل ما تروح",
    page_icon="🇪🇬",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ============================================================
# SESSION STATE
# ============================================================

if "page" not in st.session_state:
    st.session_state.page = "home"

if "selected_document" not in st.session_state:
    st.session_state.selected_document = None

if "light_mode" not in st.session_state:
    st.session_state.light_mode = False


# ============================================================
# NAVIGATION
# ============================================================

def go(page):
    st.session_state.page = page
    st.rerun()


def home():
    st.session_state.page = "home"
    st.session_state.selected_document = None
    st.rerun()


def back():
    if st.button("← رجوع", key="back_button"):
        home()


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
}

.big-category .stButton > button [data-testid="stMarkdownContainer"] p {
    font-size: 23px !important;
    font-weight: 800 !important;
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
    font-size: 14px !important;
    font-weight: 650 !important;
    line-height: 1.35 !important;
}

[class*="st-key-additional_"] .stButton > button [data-testid="stMarkdownContainer"] p:first-child {
    font-size: 20px !important;
}

[class*="st-key-additional_"] .stButton > button [data-testid="stMarkdownContainer"] p:nth-child(2) {
    font-size: 17px !important;
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
    height: 160px;
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

.back-wrapper .stButton > button {
    width: auto;
    height: 45px;

    min-height: 45px;

    padding: 7px 18px;

    border-radius: 13px;

    font-size: 15px;

    margin-bottom: 10px;
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

if st.session_state.light_mode:
    st.markdown("""
    <style>
    .stApp {
        background:
            radial-gradient(circle at 8% 8%, rgba(83, 171, 166, 0.18), transparent 32%),
            radial-gradient(circle at 92% 18%, rgba(139, 164, 205, 0.20), transparent 36%),
            linear-gradient(135deg, #eef5f3 0%, #e7eef5 52%, #f6f3ed 100%);
        color: #20313a;
    }

    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #e0eceb 0%, #edf2f4 100%);
    }

    .stApp h1,
    .stApp h2,
    .stApp h3,
    .stApp p,
    .stApp label {
        color: #20313a !important;
    }

    .stButton > button {
        color: #20313a;
        border-color: rgba(32, 49, 58, 0.14);
        background: linear-gradient(145deg, rgba(255,255,255,0.82), rgba(222,235,235,0.76));
        box-shadow: 0 10px 26px rgba(51, 77, 84, 0.12);
    }

    .stButton > button:hover {
        background: linear-gradient(145deg, rgba(255,255,255,0.96), rgba(207,230,228,0.88));
        border-color: rgba(42, 137, 132, 0.55);
        box-shadow: 0 16px 34px rgba(51, 77, 84, 0.18);
    }

    div[data-testid="stTextInput"] input {
        color: #20313a;
        background: rgba(255,255,255,0.72);
        border-color: rgba(32, 49, 58, 0.16);
    }

    .footer {
        color: #60737a;
    }
    </style>
    """, unsafe_allow_html=True)


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown("## 🇪🇬 قبل ما تروح")

    st.caption("اعرف كل حاجة قبل ما تتحرك.")

    light_mode = st.toggle(
        "☀️ الوضع الفاتح",
        value=st.session_state.light_mode,
        key="light_mode_toggle"
    )

    if light_mode != st.session_state.light_mode:
        st.session_state.light_mode = light_mode
        st.rerun()

    st.divider()

    if st.button("🏠 الرئيسية", use_container_width=True):
        home()

    if st.button("🔎 البحث", use_container_width=True):
        go("search")

    if st.button("📄 استخراج أوراق", use_container_width=True):
        go("documents")

    if st.button("🏢 معاملات وخدمات", use_container_width=True):
        go("services")

    if st.button("🩺 كشف طبي", use_container_width=True):
        go("medical")

    if st.button("💼 وظائف", use_container_width=True):
        go("jobs")

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

    st.title("🇪🇬 قبل ما تروح")

    st.subheader(
        "اعرف كل حاجة قبل ما تنزل من البيت."
    )

    st.write("")

    # --------------------------------------------------------
    # SEARCH
    # --------------------------------------------------------

    search = st.text_input(
        "بحث",
        placeholder="🔎 ابحث عن خدمة، ورقة، معاملة أو مكان...",
        label_visibility="collapsed"
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

    st.markdown("### ماذا تريد أن تفعل؟")

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
            "📄\n\nاستخراج أوراق\n\n"
            "اعرف المستندات والخطوات والمكان المناسب.",
            key="home_documents"
        ):
            go("documents")

        st.markdown(
            "</div>",
            unsafe_allow_html=True
        )


        st.markdown(
            '<div class="big-category">',
            unsafe_allow_html=True
        )

        if st.button(
            "🩺\n\nكشف طبي\n\n"
            "اعرف الطبيب والمواعيد والمكان قبل ما تروح.",
            key="home_medical"
        ):
            go("medical")

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
            "🏢\n\nمعاملات وخدمات\n\n"
            "اعرف الجهة والمواعيد والأوراق المطلوبة.",
            key="home_services"
        ):
            go("services")

        st.markdown(
            "</div>",
            unsafe_allow_html=True
        )


        st.markdown(
            '<div class="big-category">',
            unsafe_allow_html=True
        )

        if st.button(
            "💼\n\nتقديم لوظيفة\n\n"
            "اعرف مكان التقديم ومواعيد الـHR.",
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

    st.markdown("### خدمات شائعة")

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
            "المستندات والرسوم والمكان والمواعيد.",
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
            "اعرف الأوراق والخطوات والمكان.",
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
            "اعرف المطلوب وطريقة الحصول عليه.",
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

    elif document.startswith("additional:"):

        service_key = document.split(":", 1)[1]
        service = SERVICE_DATA["additional_services"][service_key]

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

    elif document.startswith("medical:"):

        service_key = document.split(":", 1)[1]
        service = SERVICE_DATA["medical_services"][service_key]

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
            st.info(
                "هنضيف الشركات ومواعيد الـHR "
                "والتقديم قريبًا."
            )

        if st.button(
            "🍔 مطعم",
            key="job_restaurant",
            use_container_width=True
        ):
            st.info(
                "هنضيف المطاعم ومواعيد التقديم "
                "والـHR قريبًا."
            )

    with col2:

        if st.button(
            "🏨 فندق",
            key="job_hotel",
            use_container_width=True
        ):
            st.info(
                "هنضيف الفنادق ومواعيد التقديم "
                "والمستندات المطلوبة."
            )

        if st.button(
            "💻 وظيفة أونلاين",
            key="job_online",
            use_container_width=True
        ):
            st.info(
                "هنضيف منصات الوظائف الأونلاين."
            )


# ============================================================
# SEARCH
# ============================================================

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
                "🛂 استخراج جواز سفر",
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