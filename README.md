# 🌌 How to run the website:

1. open the terminal
2. choose cmd in terminal
3. type: "python manage.py runserver"
4. follow the link or copy the link to edge or any server you wanna open the website
5. another option: "Go Live"
6. or visit the official website.

--Jazak Allah

# 🌌 WeatherOS - Premium Atmospheric Intelligence Dashboard

WeatherOS is a premium, enterprise-grade weather monitoring web application. Built on top of a robust **Django full-stack infrastructure**, it utilizes high-fidelity live weather data streams paired with an interactive, dynamic client-side **JavaScript Engine** to present real-time meteorological metrics seamlessly.



## 🚀 Key Features

- **Real-Time Data Streams:** Instant access to localized temperatures, barometric pressure, wind speeds, humidity, and UV indexes.
- **Dynamic Adaptive Vectors:** Auto-mapping interactive icons (Sun, Clouds, Rain, Thunderstorms) that adapt based on regional weather headlines using high-quality asset delivery.
- **Advanced Metrics Panels:** Includes a fully functional 24-Hour Timeline Slider, Regional Climate Alerts, Weather Analytics Reports, and User Configuration Panels.
- **Premium Dual-Theme Integration:** Smooth, persistent toggle transitions between **☀️ Light Mode** and **🌙 Dark Mode** synced with browser local storage.
- **Responsive Layout:** Clean, fluid dashboard optimized with enterprise sidebar configurations and analytical components.



## 🛠️ Tech Stack

- **Backend:** Python / Django (Full-stack framework)
- **Frontend:** Vanilla HTML5, CSS3 Variables (Custom Grid & Flexbox), Modern ES6 JavaScript
- **API Integration:** Live Meteorological APIs (WeatherAPI / OpenWeatherMap)
- **Deployment Ready:** Configured explicitly for instant serverless cloud deployment via Vercel.



## 🔧 Installation & Local Setup

Follow these steps to get a local copy of WeatherOS up and running on your machine:

1. **Clone the Repository:**

git clone [https://github.com/NwalTahir/WeatherOS.git](https://github.com/NwalTahir/WeatherOS.git)
cd WeatherOS

2. **Set Up a Virtual Environment:**

python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

3. Install Dependencies:

Bash


pip install -r requirements.txt

4. **Run DataBase Migrations:**

python manage.py migrate

5. **Start the Development Server:**

python manage.py runserver

Open http://127.0.0.1:8000/ in your browser to explore the dashboard.

🌐 **Serverless Cloud Deployment (Vercel):**

This project contains native configuration routing via vercel.json for rapid deployment:

1. Push your repository code to GitHub.

2. Link your GitHub account on Vercel.

3. Import the WeatherOS repository and click Deploy.

📄 **License:**

This project is licensed under the MIT License - see the LICENSE file for details.

👩‍💻 **Designer & Developer:**

Developed with 💻 by Nawal Tahir, Contact: nawaltahir94@gmail.com
