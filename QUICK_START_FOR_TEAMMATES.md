# ⚡ Quick Start Guide for New Team Members

## 🚀 Setup in 5 Minutes

### 1️⃣ Clone & Install (2 minutes)
```bash
git clone <your-repo-url>
cd modularecg-main
python3 -m venv .venv
source .venv/bin/activate  # macOS/Linux
pip install -r requirements.txt
```

### 2️⃣ Configure Cloud (2 minutes)
```bash
# Copy the template
cp env_template.txt .env

# Edit and add your AWS credentials (get from Divyansh)
nano .env
```

**Fill in:**
```env
CLOUD_SERVICE=s3
AWS_ACCESS_KEY_ID=<ask_divyansh>
AWS_SECRET_ACCESS_KEY=<ask_divyansh>
AWS_S3_BUCKET=<ask_divyansh>
AWS_S3_REGION=us-east-1
```

### 3️⃣ Test Connection (1 minute)
```bash
python3 test_cloud_connection.py
```

**Expected:** `🎉 SUCCESS! Cloud upload is properly configured!`

### 4️⃣ Run the App
```bash
python src/main.py
```

---

## 📋 Checklist

- [ ] Repository cloned
- [ ] Virtual environment activated
- [ ] Dependencies installed
- [ ] `.env` created with AWS credentials
- [ ] Test script passed
- [ ] App runs successfully

---

## 🆘 Common Issues

| Issue | Solution |
|-------|----------|
| `.env file not found` | Run: `cp env_template.txt .env` |
| `Cloud Not Configured` | Check `.env` is in project root |
| `Access Denied` | Verify credentials with Divyansh |
| `boto3 not installed` | Run: `pip install boto3` |

---

## 📚 Full Documentation

- **Complete Setup:** See `CLOUD_SETUP_GUIDE.md`
- **Dependencies:** See `DEPENDENCIES_SUMMARY.md`
- **Technical Docs:** See `TECHNICAL_DOCUMENTATION.md`

---

## 👥 Team Contacts

- **Team Lead:** Divyansh (backend, AWS setup)
- **Frontend:** Indresh, PTR
- **Android:** (Android dev name)

---

**Ready to code? Run:** `python src/main.py` 🎉

