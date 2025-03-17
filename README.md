# wall_paper_slector
# 🌅 Dynamic Wallpaper Selector

This Python script selects an appropriate **wallpaper** based on the current time and the sunrise/sunset times at a given location. The script fetches real-time sunrise and sunset data from an API and determines whether it's **morning, afternoon, evening, or night** to set the correct wallpaper.

---

## 📌 Features

- Fetches **sunrise & sunset** times for any location using an API.
- Gets the **current UTC time** and compares it with sunrise/sunset.
- Selects a **wallpaper** dynamically based on time.
- **Easy to use** with latitude & longitude as inputs.

---

## 🚀 How It Works

1. **User inputs** their location (latitude & longitude).
2. **API fetches** the sunrise & sunset times.
3. **The script determines** the time of day.
4. **Outputs the wallpaper** name to be used.

---

## 🛠️ Installation & Setup

### **Prerequisites**
- Python 3.x
- `requests` library (install if not available)

### **Installation**
1. Clone this repository:
   ```bash
   git clone https://github.com/YOUR_GITHUB_USERNAME/wallpaper-selector.git
   cd wallpaper-selector

