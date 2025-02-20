from crewai.flow.flow import Flow, start, listen
from litellm import completion

API_KEY = 'AIzaSyD9Bhd5WZvNa5iWUM9trpS_qrn6ALBMTjc'

class CityFunFact(Flow):
    def __init__(self):
        super().__init__()

    @start()
    def ask(self):
        search = input("Write the text: ")
        result = completion(
            model='gemini/gemini-1.5-flash',
            api_key=API_KEY,
            messages=[{"content": f"i am in the 7th class in pakistan urdu medium,  so reply me in urdu {search}", "role": "user"}]
        )
        
        things = result["choices"][0]["message"]["content"]
        print(things)
        return things  # Returning value for the next function

    @listen(ask)
    def write_to_readme(self, content):
        with open("README.md", "w", encoding="utf-8") as file:
            file.write(f"# Generated Content\n\n{content}\n")
        print("Content written to README.md successfully!")

def kickoff():
    obj = CityFunFact()
    obj.kickoff()

# Start process
kickoff()
