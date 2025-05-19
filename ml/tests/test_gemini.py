import os
import google.generativeai as genai

def test_gemini():
    try:
        print("1. Configuring API...")
        genai.configure(api_key='AIzaSyBxpdGmZflrGJOEQSMSL6BqEUg57FCjNoo')
        
        print("2. Creating model...")
        model = genai.GenerativeModel('gemini-2.0-flash-lite')
        
        print("3. Sending test message...")
        response = model.generate_content("Say hello!")
        
        print("4. Response received:")
        print(response.text)
        
        return True
    except Exception as e:
        print(f"Error occurred: {str(e)}")
        if "quota" in str(e).lower():
            print("\nQuota exceeded. Please wait a few minutes before trying again.")
        return False

if __name__ == "__main__":
    print("Starting Gemini API test...")
    success = test_gemini()
    print(f"\nTest {'succeeded' if success else 'failed'}") 