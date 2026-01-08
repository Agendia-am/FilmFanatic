# 🎬 Letterboxd Analyzer - Web Application

A modern web application for analyzing Letterboxd profiles with ML-powered movie recommendations.

## Architecture

**Backend (Flask)**
- RESTful API server
- Scrapes Letterboxd profiles
- Generates ML recommendations
- Processes visualization data

**Frontend (HTML/CSS/JS)**
- Clean, responsive UI
- Real-time dashboard updates
- Interactive charts with Chart.js
- Letterboxd-themed design

## Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Start the Server

```bash
python server.py
```

The server will start on `http://localhost:5000`

### 3. Open in Browser

Visit `http://localhost:5000` in your web browser

## Usage

1. **Enter Username**: Type a Letterboxd username in the input field
2. **Analyze**: Click "Analyze Profile" to start scraping
3. **View Dashboard**: See stats, charts, and recommendations
4. **Refresh**: Generate new recommendations with the refresh button

## API Endpoints

### `POST /api/scrape`
Scrape a Letterboxd profile

**Request:**
```json
{
  "username": "rjbritton08",
  "max_pages": null,
  "parallel_workers": 5
}
```

**Response:**
```json
{
  "success": true,
  "username": "rjbritton08",
  "total_films": 123,
  "films": [...],
  "stats": {...}
}
```

### `POST /api/recommendations`
Generate ML recommendations

**Request:**
```json
{
  "username": "rjbritton08",
  "top_n": 10
}
```

**Response:**
```json
{
  "success": true,
  "count": 10,
  "recommendations": [...]
}
```

### `GET /health`
Health check

**Response:**
```json
{
  "status": "ok",
  "version": "1.0.0",
  "features": {...}
}
```

## Project Structure

```
LetterboxdNew/
├── server.py              # Flask backend API
├── LetterboxdNew.py       # Core scraping logic
├── movie_recommender.py   # ML recommendation engine
├── viz_report.py          # Visualization utilities
├── frontend/
│   ├── index.html         # Main frontend page
│   ├── style.css          # Styles
│   └── app.js             # Frontend JavaScript
├── data/                  # Scraped data storage
└── requirements.txt       # Python dependencies
```

## Features

### Dashboard
- **Stats Cards**: Total films, average rating, watch time
- **Recommendations**: ML-powered personalized suggestions
- **Charts**: Rating distribution, films by year, genres, runtime
- **Top Lists**: Top genres and directors

### Recommendations
- Uses scikit-learn ML algorithms
- TF-IDF content similarity
- Hybrid scoring (40% content, 20% rating, 20% genre, 15% director, 5% actor)
- Randomized within score ranges for variety

### Caching
- Popular films cached for 7 days
- Instant recommendations after first run
- Automatic cache refresh

## Technology Stack

**Backend:**
- Flask (Web framework)
- BeautifulSoup (HTML parsing)
- Playwright (Browser automation)
- scikit-learn (ML algorithms)
- pandas/numpy (Data processing)

**Frontend:**
- Vanilla JavaScript (No frameworks)
- Chart.js (Data visualization)
- Modern CSS (Grid, Flexbox)

## Configuration

Edit `server.py` to change:
- Port (default: 5000)
- Data directory
- Parallel workers
- Cache settings

## Development

### Enable Debug Mode
```python
app.run(debug=True, host='0.0.0.0', port=5000)
```

### Add CORS for External Frontend
Already enabled with `flask-cors`

### Run Tests
```bash
python test_recommender.py
```

## Deployment

### Production Server
Use Gunicorn for production:

```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 server:app
```

### Environment Variables
```bash
export FLASK_ENV=production
export PORT=5000
```

## Troubleshooting

**Import Errors**: Install all dependencies
```bash
pip install -r requirements.txt
```

**Port Already in Use**: Change port in server.py
```python
app.run(port=5001)
```

**Playwright Browser**: Install browser
```bash
playwright install chromium
```

## Future Enhancements

- [ ] User authentication
- [ ] Save multiple profiles
- [ ] Export data as CSV/PDF
- [ ] Social features (compare profiles)
- [ ] Advanced filters
- [ ] Watchlist integration

## License

MIT

## Credits

- Letterboxd for the amazing platform
- Chart.js for beautiful charts
- Flask for simple backend
