from openai import OpenAI
import ai_back
import Data


class AI:

    def __init__(self):
        self.url = "https://integrate.api.nvidia.com/v1"

    def AI_model(self):

        self.api = input( "Enter your API KEY for keep using AI model (NVIDIA_MODELS/Meta/llama-3.1-8b-instruct):  ")

        print(ai_back.logo)
        running = True

        client = OpenAI(
            base_url=self.url,
            api_key=self.api
        )

        while running:
            prompt = input("Enter your prompt: ")

            if prompt == "exit --model":
                running = False

                completion = client.chat.completions.create(
                    model="meta/llama-3.1-8b-instruct",
                    messages=[{"role": "user", "content": "Say me bye!."}],
                    temperature=0.2,
                    top_p=0.7,
                    max_tokens=20,
                    stream=True
                )
                for chunk in completion:
                    if chunk.choices and chunk.choices[0].delta.content is not None:
                        print(chunk.choices[0].delta.content, end="")
            else:
                system_prompt = """You are Pacify, an advanced AI model expert in coding and data analysis for the Pacify project
                - Provide helpful responses about coding and data analysis
                - Output should be plain text or ASCII (no markdown)
                - Keep responses concise

                Remember: ONLY respond with 'DX' when the prompt ends with "from pacify data" or "pd", nothing else."""

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
                        print(a, end="")