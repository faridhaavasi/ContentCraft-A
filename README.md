# Intelligent Content Generator Platform

This project is a smart content generation platform powered by OpenAI APIs. It allows users to generate creative content, such as articles, captions, and hashtags, and manage their content efficiently. 

## Features

1. **User Management**
   - User registration and login (JWT-based authentication).
   - Dashboard to manage requests and credits.

2. **AI-Powered Content Generation**
   - Generate article ideas and creative titles.
   - Write complete articles based on user keywords.
   - Create short captions for social media.
   - Translate or rewrite existing texts.

3. **Customizable Options**
   - Set the tone of content (e.g., formal, friendly, humorous).
   - Automatically generate hashtags for posts.

4. **Request Limits and Credits**
   - Free users have daily request limits.
   - Paid users can purchase credits for unlimited access.

5. **Internal API**
   - Expose APIs for developers to use this system in their applications.

## Technologies Used

### Backend
- **Django**: Backend framework.
- **Django REST Framework**: To build RESTful APIs.
- **Celery**: For managing background tasks.
- **Redis**: For caching and task queue management.

### Frontend
- **React.js** (optional): For a dynamic user interface.

### Database
- **PostgreSQL**: To store user data and requests.
- **Redis**: For caching and real-time updates.

### OpenAI APIs
- **ChatGPT API**: For content generation.
- **DALL·E API** (optional): For generating images.

### Others
- **Stripe** or **Zarinpal**: For payment gateway integration.
- **Docker**: To containerize the application.
- **Swagger**: For API documentation.

## Installation

### Prerequisites
- Python 3.10+
- Docker & Docker Compose
- PostgreSQL
- Redis
- OpenAI API Key

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/intelligent-content-generator.git
   cd intelligent-content-generator
###
README - ContentCraft AI
پلتفرم تولید محتوای هوشمند

ContentCraft AI یک پلتفرم تولید محتوای هوشمند است که با استفاده از تکنولوژی‌های پیشرفته OpenAI به شما کمک می‌کند تا محتوای خلاقانه و شخصی‌سازی‌شده تولید کنید. این پلتفرم برای افرادی طراحی شده است که نیاز به تولید سریع و مؤثر محتوای متنی، کپشن‌های شبکه‌های اجتماعی، و مقالات دارند.

ویژگی‌ها:
تولید محتوای شخصی‌سازی‌شده: انتخاب لحن و سبک دلخواه برای محتوای شما.
تولید کپشن و هشتگ: پیشنهاد کپشن‌های جذاب و هشتگ‌های مرتبط برای شبکه‌های اجتماعی.
بازنویسی و ترجمه محتوا: قابلیت بازنویسی متن و ترجمه به زبان‌های مختلف.
مدیریت تاریخچه و درخواست‌ها: مشاهده و مدیریت درخواست‌های قبلی و استفاده از اعتبارهای خریداری‌شده.
امکان خرید اعتبار: کاربران حرفه‌ای می‌توانند اعتبار برای استفاده از امکانات بیشتر خریداری کنند.


