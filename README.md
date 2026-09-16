cd ~/ip-tracker
cat > README.md << 'EOF'
# 🌍 IP TRACKER - By Grazielly

Tool para rastrear qualquer IP com cidade, país, provedor e link do Google Maps.

## 📥 Como baixar e usar no Termux

```bash
pkg update && pkg upgrade -y
pkg install git python -y
pip install requests

git clone https://github.com/graziellycarolini94-gif/ip-tracker.git
cd ip-tracker
python3 ip-tracker.py

