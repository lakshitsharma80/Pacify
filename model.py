from openai import OpenAI
import Background_2


class AI():

    def __init__(self):
       self.url = "https://integrate.api.nvidia.com/v1"
       
    def AI_model(self):

        self.api_key = None
        with open("./Pacify/API_KEY.txt","r") as file:
            self.api_key = file.read().strip()
            
        if self.api_key == "sk-a" or self.api_key == "skip-api":
            print("No API key found. Please set your API key.")
            api_again = input("Enter your API KEY for using AI model (Mistral/nemotron/NVIDIA_MODELS):  ")
            self.api_key = api_again

            with open("./Pacify/API_KEY.txt","w") as file:
                file.write(self.api_key)
                
        print(Background_2.logo)
        running = True

        client = OpenAI(
            base_url = self.url,
            api_key = self.api_key                                                
        )

        while running:
            prompt = input("Enter your prompt: ")

            if prompt == "exit --model":
                running = False

                completion = client.chat.completions.create(
                model="mistralai/mistral-nemotron",
                messages=[{"role":"user","content": "Say me bye!."}],
                temperature=0.6,
                top_p=0.7,
                max_tokens=4096,
                stream=True
                )
                for chunk in completion:
                    if chunk.choices and chunk.choices[0].delta.content is not None:
                        print(chunk.choices[0].delta.content, end="")
            else:
                completion = client.chat.completions.create(
                model="mistralai/mistral-nemotron",
                messages=[{"role":"user","content": prompt}],
                temperature=0.6,
                top_p=0.7,
                max_tokens=4096,
                stream=True
                )

                for chunk in completion:
                    if chunk.choices and chunk.choices[0].delta.content is not None:
                        print(chunk.choices[0].delta.content, end="")
            
            