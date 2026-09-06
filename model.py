from openai import OpenAI
import ai_back
import Data


class AI:

    def __init__(self):
       self.url = "https://integrate.api.nvidia.com/v1"
       
    def AI_model(self):

        self.api_key = None
        with open("API_KEY.txt","r") as file:
            self.api_key = file.read().strip()
            
        if self.api_key == "none":
            print("No API key found. Please set your API key.")
            api_again = input("Enter your API KEY for keep using AI model (NVIDIA_MODELS/Meta/llama-3.1-8b-instruct):  ")
            self.api_key = api_again

            with open("API_KEY.txt","w") as file:
                file.write(self.api_key)
                
        print(ai_back.logo)
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
                model="meta/llama-3.1-8b-instruct",
                messages=[{"role":"user","content": "Say me bye!."}],
                temperature=0.2,
                top_p=0.7,
                max_tokens=20,
                stream=True
                )
                for chunk in completion:
                    if chunk.choices and chunk.choices[0].delta.content is not None:
                        print(chunk.choices[0].delta.content, end="")
            else:
                system_prompt = """You are Pacify, an advanced AI model expert in coding and data analysis for the Pacify project.

                CRITICAL INSTRUCTION - Follow these rules EXACTLY:
                1. If the user's prompt ENDS with "from pacify data" or "pd" (case-insensitive), respond with ONLY the two characters: 'DX' only.
                2. Do NOT add anything else - no spaces, no punctuation, no explanation
                3. Only 'DX' - nothing more

                If the prompt does NOT end with "from pacify data":
                - Provide helpful responses about coding and data analysis
                - Output should be plain text or ASCII (no markdown)
                - Keep responses concise

                Remember: ONLY respond with 'DX' when the prompt ends with "from pacify data", nothing else."""

                completion = client.chat.completions.create(
                    model="meta/llama-3.1-8b-instruct",
                    messages=[
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": prompt}
                    ],
                    temperature=0.6,
                    top_p=0.7,
                    max_tokens=450,
                    stream=True
                )

                for chunk in completion:
                    if chunk.choices and chunk.choices[0].delta.content is not None:
                         a = chunk.choices[0].delta.content

                         if a == 'DX':
                            print("Data mode: -")
                            completion = client.chat.completions.create(
                                 model="meta/llama-3.1-8b-instruct",
                                 messages=[
                                     {"role": "system", "content": (
                                         "You are an advanced AI your name is Pacify, model that is very expert in coding and in data analysis. "
                                         "You are chosen to manage data in the project named Pacify. "
                                         "Output should be without any markdown and should be simple text or ASCII."
                                         f"You have also info about people data of pacify if people asks question about data tell from this, you must give answer only only form this data {Data.User_data_1} and whenever you give info from this data tell them that this data is collected form pacify data."
                                     )},
                                     {"role": "user", "content": prompt}
                                 ],
                                 temperature=0.6,
                                 top_p=0.7,
                                 max_tokens=450,
                                 stream=True
                             )

                            for chunk1 in completion:
                                if chunk1.choices and chunk1.choices[0].delta.content is not None:
                                    a = chunk1.choices[0].delta.content
                                    print(a, end="")
                         else:
                             print(a, end="")



            
            