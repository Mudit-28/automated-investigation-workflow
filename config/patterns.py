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
    "sentry.io", "bugsnag", "datadog",
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
    "cookiebot", "onetrust", "cookiepro",
    # JavaScript files, debug/analytics, CDN challenge scripts
    "appdebuganalytics", "challenge-platform", "hawkeye",
    ".js", ".min.js", "vendors.js", "client.js", "common.js",
    "homepage.js", "cdn-cgi", "lumberjack", "lumberjack-metrics",
    "frontend-metrics", "linkedin.com", "facebook.net",
    "framerstatic", "smart-assist", "/v1/track",
    "sentry.airtel", "sentrynew",
    "digianalytics", "analytics/pixel"
]

PAYMENT_GATEWAYS = {
    # Indian payment gateways
    "Razorpay":         ["razorpay.com", "api.razorpay", "checkout.razorpay"],
    "Cashfree":         ["cashfree.com", "cashfreepayme"],
    "PayU":             ["payu.in", "payubiz", "payumoney", "secure.payu", "payu.money"],
    "CCAvenue":         ["ccavenue.com"],
    "BillDesk":         ["billdesk.com", "billdesk.net"],
    "JusPay":           ["juspay.in", "juspay.io", "api.juspay"],
    "Easebuzz":         ["easebuzz.in"],
    "Instamojo":        ["instamojo.com"],
    "PayKun":           ["paykun.com"],
    "Zaakpay":          ["zaakpay.com"],
    "Atom":             ["atomtech.in", "paynetz.in"],
    "DirecPay":         ["direcpay.com"],
    "PayGlocal":        ["payglocal.in"],
    "Nimbbl":           ["nimbbl.com"],
    "Open Money":       ["open.money", "openbank.in"],
    "Pay10":            ["pay10.in"],
    "Airpay":           ["airpay.co.in"],
    "SabPaisa":         ["sabpaisa.in"],
    "Plural":           ["pluralonline.com"],
    "HitPay":           ["hitpay.com", "hitpayapp"],
    "PayTabs":          ["paytabs.com"],
    "EBS":              ["ebs.in", "ebspay"],
    "FSS":              ["fssnet.co.in", "fssbillpay"],
    "Paycorp":          ["paycorp.com.au"],
    "TranZact":         ["tranzact.in"],
    "ePaisa":           ["epaisa.in"],
    "Innoviti":         ["innovitipayments.com"],
    "Mosambee":         ["mosambee.com"],
    "Mswipe":           ["mswipe.com"],
    "Sarvatra":         ["sarvatratechnologies.com"],
    "Setu":             ["setu.co"],
    "Digio":            ["digio.in"],
    "Decentro":         ["decentro.tech"],
    "Perfios":          ["perfios.com"],
    "PayNear":          ["paynear.in"],
    "MobiSwipe":        ["mobiswipe.com"],
    "ItzCash":          ["itzcash.com"],
    "Citrus Pay":       ["citruspay.com"],
    "Payu Money":       ["payumoney.com"],

    # Indian bank gateways
    "HDFC":             ["hdfcbank.com", "hdfc.bank", "smartgateway.hdfcbank",
                         "merchant.now.hdfc", "mbrww.hdfcbank", "nextgenhtml.hdfcbank"],
    "ICICI":            ["icicibank.com", "icici.bank", "eazypay.icici",
                         "retailnetbanking.icici", "shopping.icicibank"],
    "Axis Bank":        ["axisbank.com", "axis.bank"],
    "Kotak":            ["kotak.com", "kotakbank.com"],
    "Yes Bank":         ["yesbank.in"],
    "RBL Bank":         ["rblbank.com"],
    "IDFC First":       ["idfcfirstbank.com", "idfcbank.com"],
    "Federal Bank":     ["federalbank.co.in"],
    "Canara Bank":      ["canarabank.in"],
    "PNB":              ["pnbindia.in", "netpnb.com"],
    "Bank of Baroda":   ["bankofbaroda.in", "bobibanking.com"],
    "Indian Bank":      ["indianbank.in"],
    "South Indian Bank":["southindianbank.com"],
    "IDBI":             ["idbi.co.in"],
    "Bandhan Bank":     ["bandhanbank.com"],
    "Union Bank":       ["unionbankofindia.co.in"],
    "IndusInd":         ["indusind.com", "indusindbankpay"],
    "SBI":              ["sbi.co.in", "onlinesbi.com", "sbiepay"],
    "HSBC":             ["hsbc.co.in", "hsbc.com"],
    "DBS":              ["dbs.com"],
    "Citi":             ["citibank.com", "citi.com"],

    # Indian wallets & UPI apps
    "Paytm":            ["paytm.com", "paytmbank.com"],
    "PhonePe":          ["phonepe.com"],
    "BHIM":             ["bhimupi", "bhim.upi"],
    "MobiKwik":         ["mobikwik.com"],
    "Freecharge":       ["freecharge.in"],
    "CRED":             ["cred.club", "credpay"],
    "PayZapp":          ["payzapp.in", "hdfcpay"],
    "Oxigen":           ["oxigenwallet.com"],
    "Airtel Money":     ["airtel.money", "airtelmoney"],
    "JioMoney":         ["jiomoney.com", "jio.money"],
    "Ola Money":        ["olamoney.com"],
    "Pine Labs":        ["pinelabs.com", "plutus.pinelabs"],

    # Global gateways
    "Stripe":           ["stripe.com", "js.stripe.com", "api.stripe"],
    "PayPal":           ["paypal.com", "paypalobjects.com"],
    "Adyen":            ["adyen.com"],
    "Braintree":        ["braintreepayments.com", "braintree-api"],
    "Worldpay":         ["worldpay.com", "wpg.mastercard"],
    "Checkout.com":     ["checkout.com", "cko.com"],
    "Cybersource":      ["cybersource.com"],
    "Authorize.Net":    ["authorize.net", "authorizenet"],
    "Worldline":        ["worldline.com", "ingenico"],
    "BlueSnap":         ["bluesnap.com"],
    "2Checkout":        ["2checkout.com", "2co.com"],
    "PhotonPay":        ["photonpay.com"],
    "Unlimit":          ["unlimint.com"],
    "Fiserv":           ["fiserv.com", "firstdata.com"],
    "FIS":              ["fisglobal.com"],
    "Global Payments":  ["globalpayments.com"],
    "Verifone":         ["verifone.com"],
    "Nuvei":            ["nuvei.com"],
    "Square":           ["squareup.com", "square.com"],
    "Shift4":           ["shift4.com"],
    "Elavon":           ["elavon.com", "convergepay.com"],
    "Moneris":          ["moneris.com"],
    "Mollie":           ["mollie.com"],
    "GoCardless":       ["gocardless.com"],
    "Bambora":          ["bambora.com", "beanstream.com"],
    "Paysafe":          ["paysafe.com", "paysafecard.com"],
    "Spreedly":         ["spreedly.com"],
    "Primer":           ["primer.io"],
    "Airwallex":        ["airwallex.com"],
    "Nium":             ["nium.com"],
    "Rapyd":            ["rapyd.net"],
    "dLocal":           ["dlocal.com"],
    "EBANX":            ["ebanx.com"],
    "Payoneer":         ["payoneer.com"],
    "Skrill":           ["skrill.com", "moneybookers.com"],
    "Wise":             ["wise.com", "transferwise.com"],
    "PPRO":             ["ppro.com"],
    "ACI Worldwide":    ["aciworldwide.com", "acipayonline.com"],
    "Klarna":           ["klarna.com"],
    "Affirm":           ["affirm.com"],
    "Afterpay":         ["afterpay.com", "clearpay.co.uk"],
    "Zip":              ["zip.co", "quadpay.com"],
    "Dwolla":           ["dwolla.com"],
    "Bolt":             ["bolt.com"],
    "Helcim":           ["helcim.com"],
    "Stax":             ["staxpayments.com"],
    "FreedomPay":       ["freedompay.com"],
    "PayJunction":      ["payjunction.com"],
    "Converge":         ["convergepay.com"],
    "CardPointe":       ["cardpointe.com"],
    "TSYS":             ["tsys.com"],
    "Gr4vy":            ["gr4vy.com"],
    "Yuno":             ["y.uno"],
    "Payrails":         ["payrails.com"],
    "Tazapay":          ["tazapay.com"],
    "Payline":          ["paylinedata.com"],
    "eMerchantPay":     ["emerchantpay.com"],
    "DNA Payments":     ["dnapayments.com"],
    "Ecommpay":         ["ecommpay.com"],
    "Advcash":          ["advcash.com"],
    "Recurly":          ["recurly.com"],
    "Chargebee":        ["chargebee.com"],
    "Zuora":            ["zuora.com"],

    # BNPL
    "Mercado Pago":     ["mercadopago.com"],
    "PagSeguro":        ["pagseguro.uol.com.br", "pagseguro.com"],
    "Kushki":           ["kushkipagos.com"],
    "Pagar.me":         ["pagar.me"],

    # Middle East / Africa
    "HyperPay":         ["hyperpay.com"],
    "Telr":             ["telr.com"],
    "Tap Payments":     ["tap.company", "tappayme.com"],
    "PayFort":          ["payfort.com"],
    "DPO":              ["dpogroup.com"],
    "Flutterwave":      ["flutterwave.com"], 
    "Paystack":         ["paystack.com"],
    "Noon Payments":    ["noon.com/payment", "noonpayments"],
    "PayBy":            ["payby.com"],
    "PayGate":          ["paygate.co.za"],
    "Ecentric":         ["ecentric.co.za"],
    "Interswitch":      ["interswitchgroup.com", "webpay.interswitchng"],
    "PayFast":          ["payfast.co.za"],
    "PayHere":          ["payhere.lk"],
    "Network International": ["networkinternational.ae"],

    # Asia Pacific
    "Xendit":           ["xendit.co"],
    "Midtrans":         ["midtrans.com", "snap.midtrans"],
    "DragonPay":        ["dragonpay.ph"],
    "AsiaPay":          ["asiapay.com", "paydollar.com"],
    "eWAY":             ["eway.com.au"],
    "Windcave":         ["windcave.com", "paymentexpress.com"],
    "Opn Payments":     ["opn.ooo", "omise.co"],
    "PayMongo":         ["paymongo.com"],
    "Samsung Pay":      ["samsungpay.com"],
    "Alipay":           ["alipay.com", "alipayhk.com"],
    "WeChat Pay":       ["wechatpay.com", "wx.tenpay.com"],
    "UnionPay":         ["unionpay.com", "unionpayintl.com"],

    # Europe / Global wallets 
    "Vipps":            ["vipps.no"],
    "Swish":            ["swish.nu", "swish.se"],
    "iDEAL":            ["ideal.nl"],
    "Bancontact":       ["bancontact.com"],
    "Giropay":          ["giropay.de"],
    "Przelewy24":       ["przelewy24.pl", "/p24"],
    "PayTR":            ["paytr.com"],
    "Iyzipay":          ["iyzipay.com", "iyzico.com"],
    "YooMoney":         ["yoomoney.ru"],
    "Qiwi":             ["qiwi.com"],
    "Payeer":           ["payeer.com"],
    "WebMoney":         ["webmoney.ru"],
    "WayForPay":        ["wayforpay.com"],
    "Fondy":            ["fondy.eu", "fondy.io"],
    "PayZen":           ["payzen.eu"],
    "Monri":            ["monri.com"],
    "Mercanet":         ["mercanet.bnpparibas"],
    "TrustPay":         ["trustpay.eu"],
    "Trust Payments":   ["trustpayments.com"],
    "Barclays ePDQ":    ["epdq.co.uk", "barclaycard.co.uk"],
    "Bluecode":         ["bluecode.com"],

    # Card scheme gateways 
    "Mastercard Gateway": ["mpgs.com", "mastercard.gateway", "mastercard.com/gateway"],
    "Visa Gateway":       ["visa.com/checkout"],
    "American Express":   ["americanexpress.com", "amex.com"],
    "Apple Pay":          ["apple.com/apple-pay", "applepay"],
    "Google Pay":         ["googlepay.com", "pay.google.com"],
    "Amazon Pay":         ["amazonpay.in", "pay.amazon.com", "amazonpay.com"],

    # Transfer / remittance 
    "Western Union":    ["westernunion.com"],
    "MoneyGram":        ["moneygram.com"],
    "Paysend":          ["paysend.com"],
    "Remitly":          ["remitly.com"],

    # Misc 
    "YAP":              ["yap.co"],
    "NTT DATA":         ["nttdata.com"],
    "AGS Transact":     ["agstransact.com"],
    "Mintoak":          ["mintoak.com"],
    "XPay":             ["xpay.life"],
    "CellPoint":        ["cellpointdigital.com"],
    "Akurateco":        ["akurateco.com"],
    "SecurePay":        ["securepay.com.au"],
    "QuickPay":         ["quickpay.net"],
    "iPay88":           ["ipay88.com"],
    "BR-DGE":           ["br-dge.com"],
    "Trankpay":         ["trankpay.com"],
}

UPI_COLLECT_PATTERNS = [
    "collect", "collectrequest", "upi-collect", "upi/collect",
    "pay-request", "payrequest", "/collect/", "vpa/collect",
    "upi/mandate", "createmandate", "mandate/create",
    "upi/intent", "upiintent", "intent/upi"
]

AGGREGATOR_PATTERNS = {
    "Razorpay Payment Link": ["rzp.io/l/", "rzp.io/pay/"],
    "Cashfree Payment Link": ["payments.cashfree.com/pgbillpay"],
    "Instamojo":             ["instamojo.com/pay"],
    "PayU Hosted":           ["payumoney.com/paybyweb"],
}


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