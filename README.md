# 🇵🇱 Job Search Telegram Bot  

A **Telegram bot** that helps users **find job postings in Poland**. The bot allows users to select a city and job category, then fetches **real-time job listings** from **[Pracuj.pl](https://www.pracuj.pl/)** using **Selenium** and **BeautifulSoup**.  

## ✨ Features  

✔ **📌 City and Category Selection** – Users can filter job searches by location and industry.  
✔ **🤖 Automated Parsing** – Uses **Selenium** to scrape job listings dynamically.  
✔ **📩 Real-time Updates** – The bot checks for new job postings and sends them automatically.  
✔ **🔗 Inline Buttons** – Each job listing includes a button with a **direct link** to the offer.  
✔ **⚡ Fast & Lightweight** – Uses **async programming** for optimal performance.  

---

## 🚀 How It Works  

1️⃣ The user starts the bot with `/start`.  
2️⃣ The bot provides an **interactive menu** to select a **city** and **job category**.  
3️⃣ Once selections are made, the user can start the **job search**.  
4️⃣ The parser runs in the background, **scraping Pracuj.pl** for new job listings.  
5️⃣ When new jobs appear, the bot **sends them directly** to the user via Telegram.  

---

## 🛠️ Technologies Used  

| Technology      | Purpose                           |
|---------------|---------------------------------|
| **Python** | Core programming language  |
| **Aiogram** | Telegram bot framework  |
| **Selenium** | Web scraping with a headless browser  |
| **BeautifulSoup4** | HTML parsing for extracting job data  |
| **Aiohttp** | Asynchronous HTTP requests  |
| **JSON** | Storing job listings & user preferences  |

---

## 📦 Installation  

### 🔹 1. Clone the Repository  

```bash
git clone https://github.com/yourusername/job-search-bot.git
cd job-search-bot
```

### 🔹 2. Install Depencies

```bash
pip install -r requirements.txt
```

### 🔹 3. Set Up Your Telegram Bot
1. **Create a bot** via @BotFather on Telegram.
2. Get your **API Token** and add it to the `bot.py` file.

### 🔹 4. Run the Bot
```bash
python bot.py
```

### 🔥 Future Improvements
✔ Add **keyword-based search** for more specific job filtering.

✔ Integrate **multiple job platforms** for a wider job search.

✔ Support **multiple languages** (English, Polish, etc.).

✔ Implement **job alerts** for new listings matching user preferences.

### 🤝 Contributing
💡 If you have any **ideas, improvements, or bug fixes**, feel free to **open an issue** or **submit a pull request!**

📩 You can also reach out to me via **Telegram:** @Bigmaksik

### ⭐ Star the Repo!
If you find this project useful, **please ⭐ star** this repository to support development!
```bash
🚀 Made with Python & ❤️ for Job Seekers in Poland! 🇵🇱
```
