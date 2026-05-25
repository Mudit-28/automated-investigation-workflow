PAYMENT_KEYWORDS = [
    # Core payment words
    "payment", "paid", "pay", "paying", "payout",
    "payin", "transaction", "txn", "transfer", "transferred",
    "credited", "debited", "credit", "debit", "withdrawal",
    "deposit", "refund", "refunded", "charge", "charged",
    "bill", "billing", "invoice", "receipt", "checkout",
    "purchase", "order", "merchant", "settlement", "amount",
    # Banking
    "bank", "account", "saving account", "current account", "balance",
    "statement", "utr", "rrn", "reference number", "bank transfer",
    "neft", "rtgs", "imps", "swift", "wire transfer",
    "beneficiary", "remittance", "banking", "bank txn", "a/c",
    # UPI / India
    "upi", "upi id", "vpa", "virtual payment address", "collect request",
    "payment request", "scan qr", "qr code", "qr payment", "paytm",
    "phonepe", "gpay", "google pay", "bhim", "amazon pay",
    "mobikwik", "cred", "freecharge", "payzapp", "airtel money",
    "jiomoney", "wallet", "wallet balance", "merchant payment", "payment link",
    # Cards
    "credit card", "debit card", "visa", "mastercard", "rupay",
    "american express", "amex", "cvv", "expiry", "card payment",
    "tap to pay", "contactless", "pos", "terminal", "swipe",
    "chip", "pin", "card ending", "card txn", "last four digits",
    # Banking channels
    "netbanking", "internet banking", "mobile banking", "bank login", "bank payment",
    "standing instruction", "autopay", "mandate", "standing mandate", "recurring payment",
    # EMI / Loans / BNPL
    "emi", "loan", "pay later", "bnpl", "installment",
    "monthly payment", "no cost emi", "simpl", "lazypay", "zestmoney",
    # Transaction states
    "success", "successful", "completed", "processed", "pending",
    "failed", "declined", "cancelled", "initiated", "reversed",
    "processing", "approved", "authorized", "settled", "captured",
    # Invoice language
    "invoice number", "bill payment", "amount due", "payment due", "payment received",
    "receipt number", "invoice amount", "total due", "subtotal", "tax amount",
    # Currency indicators
    "₹", "rs", "rs.", "inr", "usd",
    "$", "eur", "€", "gbp", "aed",
    # SMS transaction phrases
    "spent", "received", "credited to", "debited from", "available balance",
    "avl bal", "txn id", "utr no", "rrn no", "ref no",
    "payment successful", "payment failed", "txn successful", "txn failed", "credited by",
    "debited by", "merchant ref", "payment id", "reference id", "txn ref",
    # Checkout wording
    "buy now", "pay now", "confirm payment", "continue to payment", "place order",
    "cash on delivery", "cod", "checkout session", "confirm purchase", "payment page",
    # Authentication
    "otp", "authentication", "3d secure", "verified by visa", "securecode",
    "authorize", "authorize payment", "payment verification", "verification code", "secure payment",
    # International transfers
    "swift code", "iban", "bic", "international transfer", "cross border",
    # Crypto payments
    "crypto", "bitcoin", "ethereum", "usdt", "wallet address",
    # Merchant/payment infra
    "processor", "payment processor", "authorization", "capture", "capture payment",
    "settlement", "merchant txn", "merchant id", "order amount", "payment intent",
    # Banking abbreviations
    "acct", "account no", "txn#", "txn ref", "bank ref",
    "merchant ref", "reference no", "transaction id", "payment reference", "order id",
    # OCR/payment page indicators
    "pay securely", "proceed to pay", "secure checkout", "payment details", "payment mode",
    "choose payment", "select payment", "payment option", "pay via", "upi collect",
    # Additional detection terms
    "wallet txn", "bank debit", "bank credit", "payment initiated", "transaction complete",
    "payment complete", "money transfer", "fund transfer", "send money", "receive money"
    ]

NOISE_KEYWORDS = [
    # Analytics & tracking
    "google-analytics", "googletagmanager", "gtm",
    "hotjar", "mixpanel", "amplitude", "segment",
    "clarity", "logrocket", "fbevents", "doubleclick",
    # Social & ads
    "facebook.com", "instagram.com", "twitter.com",
    "snapchat.com", "pinterest.com",
    # Static assets by extension
    ".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp",
    ".css", ".woff", ".woff2", ".ttf", ".ico", ".mp4",
    # CDN & infrastructure
    "cdn.", "fonts.googleapis", "fontawesome",
    "jsdelivr", "cloudflare", "unpkg.com",
    # Live chat & support tools
    "zendesk", "intercom", "freshchat", "tawk",
    "crisp", "livechat",
    # Error monitoring
    "sentry.io", "bugsnag", "datadog"
    # A/B testing tools
    "optimizely", "vwo.com", "abtasty",
    # Marketing automation  
    "hubspot", "mailchimp", "klaviyo", "marketo",
    # Video/media CDNs
    "youtube.com", "vimeo.com", "jwplayer",
    "brightcove", "dailymotion",
    # Performance monitoring
    "newrelic", "dynatrace", "pingdom",
    # Push notifications
    "onesignal", "pushwoosh", "firebase-messaging",
    # Cookie consent tools
    "cookiebot", "onetrust", "cookiepro"
    # javacript files, bebug/analytics, CDN challenge scripts
    "appdebuganalytics", "challenge-platform", "hawkeye", 
    ".js", ".min.js", "vendors.js", "client.js", "common.js",
    "homepage.js", "cdn-cgi", "lumberjack", "lumberjack-metrics", 
    "frontend-metrics", "linkedin.com", "facebook.net", 
    "framerstatic", "smart-assist","/v1/track",
    "sentry.io", "sentry.airtel", "sentrynew"
    ]

PAYMENT_GATEWAYS = [
    "Razorpay", "Cashfree", "PayU", "CCAvenue", "BillDesk",
    "Juspay", "Easebuzz", "Instamojo", "PayKun", "Zaakpay",
    "Atom", "DirecPay", "PayGlocal", "Nimbbl", "Open Money",
    "Pay10", "Airpay", "SabPaisa", "Plural", "HitPay",
    "PayTabs", "EBS", "FSS", "Paycorp", "TranZact",
    "ePaisa", "Innoviti", "Mosambee", "Mswipe", "Worldline",
    "Sarvatra", "Setu", "Digio", "Decentro", "Perfios",
    "YAP", "NTT DATA", "AGS Transact", "Mintoak", "HyperPay",
    "XPay", "CellPoint", "Network International", "Cybersource", "Fiserv",
    "FIS", "Global Payments", "BlueSnap", "Checkout.com", "Stripe",
    "PayPal", "Adyen", "Braintree", "Worldpay", "2Checkout",
    "PhotonPay", "Unlimit", "Authorize.Net", "Amazon Pay", "Google Pay",
    "Apple Pay", "Pine Labs", "SBIePay", "HDFC SmartGateway", "ICICI Eazypay",
    "Axis Gateway", "Kotak Gateway", "Yes Bank Gateway", "RBL Gateway", "IDFC Gateway",
    "Federal Gateway", "Canara Gateway", "PNB Gateway", "BOB Gateway", "Indian Bank Gateway",
    "South Indian Bank Gateway", "IDBI Gateway", "Bandhan Gateway", "Union Bank Gateway", "IndusInd Gateway",
    "HSBC Gateway", "DBS Gateway", "Citi Gateway", "American Express Gateway", "TrustPay",
    "SecurePay", "QuickPay", "iPay", "Akurateco", "Telr",
    "Tap Payments", "PayFort", "DPO", "Flutterwave", "Paystack",
    "Rapyd", "dLocal", "EBANX", "Payoneer", "Skrill",
    "Wise", "PPRO", "ACI Worldwide", "Verifone", "Nuvei",
    "Paytm", "PhonePe", "BHIM", "MobiKwik", "Freecharge",
    "CRED Pay", "PayZapp", "Oxigen", "Airtel Money", "JioMoney",
    "Ola Money", "Samsung Pay", "Alipay", "WeChat Pay", "UnionPay",
    "Klarna", "Affirm", "Afterpay", "Zip", "Paysafe",
    "Trust Payments", "Bambora", "Elavon", "Moneris", "Mollie",
    "Mercado Pago", "Vipps", "Swish", "iDEAL", "Bancontact",
    "Giropay", "Przelewy24", "PayTR", "Iyzipay", "Midtrans",
    "Xendit", "DragonPay", "AsiaPay", "eWAY", "Windcave",
    "PayFast", "PayHere", "Interswitch", "MPGS", "Mastercard Gateway",
    "Visa Gateway", "Barclays ePDQ", "Tazapay", "Airwallex", "Nium",
    "PayMongo", "Opn Payments", "Primer", "Spreedly", "Gr4vy",
    "Yuno", "BR-DGE", "Payrails", "Converge", "CardPointe",
    "TSYS", "Ecentric", "PaysafeCard", "Payu Money", "Citrus Pay",
    "Noon Payments", "PayBy", "Chargebee Payments", "Zuora Payments", "Recurly",
    "PayNear", "MobiSwipe", "ItzCash", "PayGate", "CyberSource",
    "Mastercard Payment Gateway Services", "Visa Cybersource", "BlueSnap Payments", "Payline", "eMerchantPay",
    "Nuvei Payments", "Shift4", "Checkout Fintech", "DNA Payments", "Ecommpay",
    "Kushki", "PagSeguro", "Stone Payments", "Pagar.me", "Mercury Payments",
    "FreedomPay", "ACI Payments", "PayJunction", "Dwolla", "Bolt Payments",
    "Square", "Helcim", "Stax", "Advcash", "GoCardless",
    "Paysend", "Remitly", "Western Union Business", "MoneyGram Business", "Bluecode",
    "Monri", "PayZen", "WayForPay", "Fondy", "YooMoney",
    "Qiwi", "Payeer", "WebMoney", "Mercanet", "Trankpay"
    ]

import re
UPI_PATTERN = re.compile(
    r'[a-zA-Z0-9.\-_]{3,256}'
    r'@'
    r'(paytm|okicici|okhdfcbank|okaxis|oksbi|ybl|ibl|axl|'
    r'upi|apl|pingpay|waicici|mahb|idbi|dbs|'
    r'freecharge|ikwik|indus|rbl|'
    r'paytmbank|phonepe|gpay|bhim|airtel)',
    re.IGNORECASE
)
UPI_PATTERN_LOOSE = re.compile(
    r'[a-zA-Z0-9.\-_]{4,256}@[a-zA-Z]{4,20}'
)
