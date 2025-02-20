import os
from crewai.flow.flow import Flow, start, listen
from litellm import completion

# Set API Key
GEMINI_API_KEY = os.getenv("GOOGLE_API_KEY")  # Make sure this is set in your environment

class CityFunFact(Flow):
    
    @start
    def function1(self):
        """Step 1: Take input and search if it exists in a book or knowledge base"""
        input_text = input("📌 Enter a topic to search: ")  # Taking input directly here
        print(f"\n🔍 Step 1: Searching for '{input_text}' in books and knowledge base...")

        search_prompt = f"Find references of '{input_text}' in books or knowledge bases."
        
        response = completion(
            model="gemini-flash",
            messages=[{"role": "user", "content": search_prompt}],
            api_key=GEMINI_API_KEY
        )

        search_result = response["choices"][0]["message"]["content"]
        print("\n🔎 Search Result:\n", search_result)
        return search_result

    @listen(function1)
    def function2(self, search_result):
        """Step 2: Explain the found information using LLM"""
        print("\n📖 Step 2: Elaborating on the search result...")

        explain_prompt = f"Explain the following in simple words: {search_result}"
        
        response = completion(
            model="gemini-flash",
            messages=[{"role": "user", "content": explain_prompt}],
            api_key=GEMINI_API_KEY
        )

        explanation = response["choices"][0]["message"]["content"]
        print("\n📜 Elaborated Explanation:\n", explanation)
        return explanation

    @listen(function2)
    def function3(self, elaboration):
        """Step 3: Save the elaboration to a README file"""
        print("\n💾 Step 3: Writing the elaboration to README.md...")

        with open("README.md", "w", encoding="utf-8") as file:
            file.write("# Fun Fact Explanation\n\n")
            file.write(elaboration)
        
        print("✅ README.md has been updated!")

def kickoff():
    """Start the pipeline"""
    obj = CityFunFact()
    obj.kickoff()  # No need for arguments now

# Run the script directly
if __name__ == "__main__":
    kickoff()
