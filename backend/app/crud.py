import os
from typing import List, Dict, Any

try:
    from openai import OpenAI
except Exception:
    OpenAI = None


class AIStudyService:
    def __init__(self):
        self.api_key = os.getenv("OPENAI_API_KEY")
        self.client = OpenAI(api_key=self.api_key) if self.api_key and OpenAI else None

    def answer_question(self, question: str, context: str = "") -> str:
        if self.client:
            try:
                response = self.client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[
                        {"role": "system", "content": "You are a helpful study tutor. Answer clearly and use examples when helpful."},
                        {"role": "user", "content": f"Context:\n{context}\n\nQuestion:\n{question}"},
                    ],
                    temperature=0.2,
                )
                return response.choices[0].message.content.strip()
            except Exception:
                pass

        if context:
            return f"Based on your notes: {context[:500]}...\n\nAnswer: {question} can be explained by identifying the key concepts, examples, and relationships between them."
        return "A strong answer should define the concept, explain the process step by step, and connect it to real examples or comparisons."

    def summarize(self, text: str) -> str:
        if self.client:
            try:
                response = self.client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[
                        {"role": "system", "content": "Summarize the material clearly and concisely for a student."},
                        {"role": "user", "content": text},
                    ],
                    temperature=0.2,
                )
                return response.choices[0].message.content.strip()
            except Exception:
                pass

        return "Key points: 1) Understand the main idea. 2) Break the topic into components. 3) Review examples and practice recall."

    def generate_flashcards(self, text: str) -> List[Dict[str, str]]:
        if self.client:
            try:
                response = self.client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[
                        {"role": "system", "content": "Create 5 concise study flashcards from the input. Return valid JSON only with an array of objects: [{front, back}]."},
                        {"role": "user", "content": text},
                    ],
                    temperature=0.2,
                )
                content = response.choices[0].message.content.strip()
                import json
                return json.loads(content)
            except Exception:
                pass

        return [
            {"front": "What is the main idea?", "back": "Identify the central concept and explain it in your own words."},
            {"front": "What are the key terms?", "back": "List important vocabulary and define each term briefly."},
            {"front": "How does this connect to prior learning?", "back": "Relate the topic to previous concepts and examples."},
            {"front": "What is one example?", "back": "Use a real or hypothetical scenario to illustrate the concept."},
            {"front": "What should you review next?", "back": "Identify weak points and focus your next study session there."},
        ]

    def generate_quiz(self, text: str) -> List[Dict[str, Any]]:
        if self.client:
            try:
                response = self.client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[
                        {"role": "system", "content": "Generate 5 multiple-choice questions from the input. Return valid JSON only: [{question, options, correct_answer, explanation}]."},
                        {"role": "user", "content": text},
                    ],
                    temperature=0.2,
                )
                content = response.choices[0].message.content.strip()
                import json
                return json.loads(content)
            except Exception:
                pass

        return [
            {
                "question": "Which statement best summarizes the topic?",
                "options": ["A short summary of the concept", "A random guess", "Irrelevant details", "A list of examples without explanation"],
                "correct_answer": "A short summary of the concept",
                "explanation": "A good summary captures the central idea in a concise, relevant way."
            },
            {
                "question": "What is the best way to study this material?",
                "options": ["Memorize without understanding", "Break it into concepts and review examples", "Ignore practice questions", "Skip the summary"],
                "correct_answer": "Break it into concepts and review examples",
                "explanation": "Comprehension improves when you structure your study and actively test yourself."
            },
        ]
