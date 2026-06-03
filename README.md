# 🔍 Web Payment Investigation Tool

An OSINT automation tool that uses a real browser to detect and extract payment infrastructure from websites — UPI IDs, payment gateways, aggregators, QR codes, and bank account details — and exports findings to a color-coded Excel report.

> Built for investigative and law enforcement use cases targeting illegal online gambling and betting platforms operating in India.

---

## 🚀 Features

- **Live Browser Automation** — Uses Playwright with a real Chromium browser to bypass bot detection
- **Network Interception** — Captures all payment-related API calls in real time
- **UPI Extraction** — Detects UPI IDs from network traffic, JSON response fields, QR codes, and DOM
- **QR Code Decoding** — Automatically decodes QR images from endpoints, base64 HTML, and image links
- **Gateway Detection** — Identifies 20+ payment gateways (Razorpay, PayU, Cashfree, OdeonPay, UKPayCenter, etc.)
- **Aggregator Detection** — Flags aggregator-hosted pages where merchant UPI is hidden
- **UPI Collect Detection** — Alerts when a site initiates a UPI collect/pull request
- **Beneficiary Name Extraction** — Scrapes account holder names from payment modals
- **Bank Account / IFSC Detection** — Extracts NEFT account numbers and IFSC codes
- **Color-Coded Excel Report** — Exports findings with visual highlights per threat type
- **Screenshot & HTML Capture** — Saves full-page screenshots and HTML at every navigation step

---

## 🎨 Excel Report Color Legend

| Color | Meaning |
|-------|---------|
| 🟡 Yellow | UPI ID found in network traffic or DOM |
| 🟠 Orange | QR code / payment initiation endpoint detected |
| 🟢 Green | Known payment gateway detected |
| 🔴 Red | UPI collect request (money pull initiated) |
| 🟣 Purple | Aggregator-hosted page — merchant UPI hidden |

---

## 📁 Project Structure

```
investigation_tool/
├── core/
│   ├── browser.py          # Playwright BrowserManager (async context manager)
│   ├── network_monitor.py  # Intercepts & filters payment-related network requests
│   ├── extractor.py        # UPI, gateway, bank detail extraction logic
│   └── storage.py          # Excel report generation (openpyxl)
├── modules/
│   ├── screenshots.py      # Full-page screenshot capture per navigation
│   ├── html_capture.py     # Full HTML save per navigation
│   ├── page_monitor.py     # DOM mutation observer, popup/tab tracking
│   └── base_capture.py     # Shared file naming utilities
├── config/
│   └── patterns.py         # Regex patterns, gateway lists, noise keywords
├── output/
│   ├── screenshots/        # Auto-created, gitignored
│   ├── html/               # Auto-created, gitignored
│   └── reports/            # Excel reports saved here
├── main.py                 # Entry point
└── requirements.txt
```

---

## ⚙️ Installation

### 1. Clone the repo

```bash
git clone https://github.com/yourusername/investigation-tool.git
cd investigation-tool
```

### 2. Install Python dependencies

```bash
pip install -r requirements.txt
```

### 3. Install Playwright browser

```bash
playwright install chromium
```

> **Note:** `pyzbar` requires the `zbar` system library.
> - **Ubuntu/Debian:** `sudo apt-get install libzbar0`
> - **macOS:** `brew install zbar`
> - **Windows:** Download the DLL from the [zbar project](http://zbar.sourceforge.net/)

---

## 🖥️ Usage

```bash
python main.py <url>
```

**Example:**

```bash
python main.py https://targetsite.com
```

The tool will:
1. Launch a visible Chrome browser and navigate to the URL
2. Monitor all network requests in real time
3. Capture screenshots and HTML at every page change
4. Wait up to **20 minutes** for manual interaction (login, deposit flow, etc.)
5. Save an Excel report to `output/reports/` when the browser is closed

---

## 📊 Output

Each run produces:

| Output | Location | Description |
|--------|----------|-------------|
| Excel Report | `output/reports/<site>_investigation_<timestamp>.xlsx` | Full findings with color highlights |
| Screenshots | `output/screenshots/<site>_<timestamp>/` | PNG captures at each navigation |
| HTML Snapshots | `output/html/<site>_<timestamp>/` | Full page HTML at each navigation |

### Excel Sheets

**Summary Sheet** — One row per investigated site:
- Website URL, Page Title, Total Requests
- Payment API URLs, UPI IDs, Gateways
- Bank IFSC Codes, Account Numbers, Beneficiary Names
- Screenshot Path, Timestamp

**Network Requests Sheet** — One row per captured request:
- Endpoint URL, Method, Status
- Gateways Detected, UPI IDs Found, Beneficiary Names
- Post Data, Response Body, QR Decoded content

---

## 🔬 Detection Logic

### UPI ID Detection (4 layers)
1. **Regex on combined text** — URL + POST data + response body + QR decoded content
2. **JSON field parsing** — Scans known keys: `upiAccount`, `vpa`, `upi_id`, `upiId`, `pa`, `upiAddress`, `paymentAddress`
3. **QR code extraction** — Decodes `pa=` parameter from UPI deep links in QR content
4. **DOM scan** — JavaScript regex injected into the live page at each navigation

### QR Code Decoding (3 strategies)
1. **Image endpoint** — Fetches and decodes image from `/qr/`, `qrcode`, `generateqr` URLs
2. **JSON image link** — Follows `qrImageLink` field in JSON responses
3. **Base64 inline** — Decodes `data:image/...;base64,...` embedded in HTML responses

### Gateway Detection
Matches against a curated list including: Razorpay, PayU, Cashfree, Paytm, PhonePe, BillDesk, CCAvenue, Instamojo, EasyPay, OdeonPay, UKPayCenter, GuardPay, BT3 P2P, and more.

### Noise Filtering
Analytics, CDN, and tracking URLs are filtered out before capture to keep reports clean.

---

## 🛠️ Configuration

All detection patterns are in `config/patterns.py`:

| Variable | Purpose |
|----------|---------|
| `PAYMENT_GATEWAYS` | Dict of gateway name → URL patterns |
| `PAYMENT_KEYWORDS` | URL keywords that flag a request as relevant |
| `NOISE_KEYWORDS` | URL patterns to ignore (analytics, CDNs, etc.) |
| `UPI_PATTERN` | Strict UPI regex |
| `UPI_PATTERN_LOOSE` | Broader UPI regex with post-filtering |
| `UPI_COLLECT_PATTERNS` | Patterns that indicate a collect/pull request |
| `AGGREGATOR_PATTERNS` | Patterns for aggregator-hosted cashier pages |
| `IFSC_PATTERN` | IFSC code regex |
| `BANK_ACCOUNT_PATTERN` | Bank account number regex |

---

## ⚠️ Disclaimer

This tool is intended strictly for **investigative, research, and law enforcement purposes**. Usage against websites without authorization may violate applicable laws. The authors are not responsible for any misuse.

---

## 📦 Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| `playwright` | ≥1.40.0 | Browser automation |
| `openpyxl` | ≥3.1.0 | Excel report generation |
| `httpx` | ≥0.27.0 | Async HTTP (QR fetch, redirect follow) |
| `pyzbar` | ≥0.1.9 | QR code decoding |
| `Pillow` | ≥10.0.0 | Image processing for QR decoder |
