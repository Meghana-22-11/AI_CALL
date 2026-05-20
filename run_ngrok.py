import os
import sys
import re
from dotenv import load_dotenv
from pyngrok import ngrok, conf

def main():
    load_dotenv()
    
    # 1. Get authtoken from env or command line
    authtoken = os.getenv("NGROK_AUTHTOKEN", "").strip()
    if len(sys.argv) > 1:
        authtoken = sys.argv[1].strip()
        
    if not authtoken:
        print("\n" + "=" * 60)
        print("❌ Error: No ngrok authtoken found!")
        print("=" * 60)
        print("Please run the script with your token:")
        print("  python run_ngrok.py <YOUR_NGROK_AUTHTOKEN>")
        print("\nOr add it to your .env file first as:")
        print("  NGROK_AUTHTOKEN=your_token_here")
        print("=" * 60 + "\n")
        return

    # 2. Write/Update NGROK_AUTHTOKEN in .env
    env_path = ".env"
    
    if os.path.exists(env_path):
        with open(env_path, "r") as f:
            env_content = f.read()
    else:
        env_content = ""
        
    if "NGROK_AUTHTOKEN" not in env_content:
        # Append it
        with open(env_path, "a") as f:
            f.write(f"\n# Ngrok authtoken\nNGROK_AUTHTOKEN={authtoken}\n")
        print("✅ Added NGROK_AUTHTOKEN to .env file!")
    else:
        # Update it
        pattern = r"NGROK_AUTHTOKEN\s*=\s*[^\n]*"
        env_content = re.sub(pattern, f"NGROK_AUTHTOKEN={authtoken}", env_content)
        with open(env_path, "w") as f:
            f.write(env_content)
        print("✅ Updated NGROK_AUTHTOKEN in .env file!")

    # 3. Configure pyngrok
    print("\n🔄 Setting up ngrok auth token...")
    ngrok.set_auth_token(authtoken)
    
    # 4. Connect to port 5001
    print("🚀 Starting ngrok tunnel on port 5001...")
    try:
        tunnel = ngrok.connect(5001)
        public_url = tunnel.public_url
        print(f"\n🔥 Ngrok tunnel is active!")
        print(f"🔗 Public URL: {public_url}")
        
        # 5. Update VOICE_WEBHOOK_URL in .env
        voice_url = f"{public_url}/voice"
        print(f"📱 Webhook URL for Twilio: {voice_url}")
        
        with open(env_path, "r") as f:
            content = f.read()
            
        if "VOICE_WEBHOOK_URL" in content:
            pattern = r"VOICE_WEBHOOK_URL\s*=\s*[^\n]*"
            content = re.sub(pattern, f"VOICE_WEBHOOK_URL={voice_url}", content)
        else:
            content += f"\nVOICE_WEBHOOK_URL={voice_url}\n"
            
        with open(env_path, "w") as f:
            f.write(content)
            
        print("✅ Automatically updated VOICE_WEBHOOK_URL in your .env file!")
        print("\n" + "=" * 65)
        print("🎉 You are all set!")
        print("👉 1. Keep this terminal open (keeps the tunnel alive).")
        print("👉 2. Open a new terminal to run your Flask application:")
        print("      python app.py")
        print("👉 3. In the new terminal, trigger the call:")
        print("      python call.py")
        print("=" * 65)
        print("\nPress Ctrl+C to stop the tunnel.\n")
        
        # Wait for user input or keep alive
        import time
        while True:
            time.sleep(1)
            
    except Exception as e:
        print(f"\n❌ Error starting ngrok tunnel: {e}")
        print("Please verify that your auth token is correct.")

if __name__ == "__main__":
    main()
