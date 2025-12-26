# 🪞 AI Smart Mirror & Command Center

![Project Status](https://img.shields.io/badge/status-active-brightgreen)
![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

> A futuristic, gesture-free smart mirror dashboard that identifies users via facial recognition and serves personalized schedules, tasks, and environmental data in real-time.

## 📸 Screenshots
![screenshots](https://github.com/dy546/Magic-Mirror-Project/blob/f0ae68e0b033a002338ae9375925fd01ed559295/screenshot.png)

## 📖 About
This project transforms a standard webcam and monitor into an intelligent "Magic Mirror." Unlike traditional smart mirrors that show static information, this system uses **Computer Vision** to detect who is looking at it.

When a user is recognized, the dashboard dynamically updates to show:
* **Personalized To-Do Lists:** Assigned by an administrator.
* **Real-time Environmental Data:** UV Index, Humidity, Rain Forecast, and Wind Speed.
* **Urgent Notifications:** Global alerts or private messages.
* **Attendance Logging:** Automatically logs entry times to a CSV file.

## ✨ Key Features
* **Face Recognition Authentication:** Secure, hands-free user identification using `dlib` and `face_recognition`.
* **Dynamic HUD Interface:** Custom-drawn UI using Pillow (PIL) with progress bars and sci-fi aesthetic.
* **Admin Command Panel:** A dedicated CLI tool (`admin.py`) for managers to assign tasks and broadcast alerts remotely.
* **Live Weather Integration:** Fetches granular weather data (UV, Rain %, Wind) via API.
* **Data Persistence:** Uses JSON-based local storage for task management, requiring no external database setup.

---

## 🛠️ Installation

### 1. Prerequisites
* Python 3.8 or higher
* A webcam
* **Visual Studio C++ Build Tools** (Required for installing `dlib` on Windows)

### 2. Clone the Repository
```bash
git clone https://github.com/dy546/Magic-Mirror-Project.git

```

### 3. Install Dependencies

```bash
pip install -r requirements.txt

```

### 4. Configuration

1. **Environment Variables:**
* Duplicate `.env.example` and rename it to `.env`.
* Add your WeatherAPI key (get one for free at [weatherapi.com](https://www.weatherapi.com/)):


```ini
WEATHER_API_KEY=your_api_key_here

```


2. **User Setup:**
* Navigate to the `known_faces/` directory.
* Add clear photos of authorized users.
* **Naming Convention:** The filename becomes the user ID (e.g., `elon_musk.jpg` -> User `ELON_MUSK`).



---

## 🚀 Usage

### Starting the Mirror

Run the main application script. This will launch the camera feed and dashboard.

```bash
python main.py

```

*Press `q` to quit the application.*

### Using the Admin Panel

Open a separate terminal to manage the system. This allows you to send data to the mirror without stopping it.

```bash
python admin.py

```

**Options:**

1. **Global Announcement:** Displays a red alert banner for all users.
2. **Assign Task:** Adds a checklist item to a specific user's dashboard.
3. **Clear Data:** Wipes tasks/alerts for a user.

---

## 📂 Project Structure

```text
Magic Mirror/
├── known_faces/           # Folder for user reference images
├── admin.py               # CLI tool for managing tasks/alerts
├── main.py                # Core application (CV + Dashboard logic)
├── company_data.json      # Local database for tasks (Auto-generated)
├── attendance.csv         # Login logs (Auto-generated)
├── JetBrainsMono-Regular.ttf # Font file for UI
├── requirements.txt       # Python dependencies
└── .env                   # API Keys (Not committed to repo)

```

## 🧩 Technologies Used

* **OpenCV:** Video capture and image processing.
* **Face Recognition:** Dlib-based facial encodings.
* **Pillow (PIL):** drawing the high-resolution HUD overlay.
* **NumPy:** Matrix operations for image stitching.
* **WeatherAPI:** External data provider.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/dy546/Magic-Mirror-Project/issues).

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/dy546/Magic-Mirror-Project/blob/33aaff9f3f963a3a7e9484d1dc39cbdbb5316eb9/LICENSE) file for details.