import os

questions_data = [
    ("Is the United Nations headquartered in New York City?", True),
    ("Is the European Union comprised of exactly 20 member states?", False),
    ("Did the Cold War officially end with the dissolution of the Soviet Union?", True),
    ("Is India currently the most populous country in the world over China?", True),
    ("Is the capital of Australia Sydney?", False),
    ("Does the United Kingdom have a written constitution codified in a single document?", False),
    ("Is the World Trade Organization (WTO) headquartered in Geneva, Switzerland?", True),
    ("Is Brazil a member of the BRICS economic group?", True),
    ("Did the Berlin Wall fall in 1989?", True),
    ("Is NATO an economic alliance rather than a military alliance?", False),
    ("Is the currency of Japan the Won?", False),
    ("Does the United States hold veto power in the UN Security Council?", True),
    ("Is Vatican City the smallest internationally recognized independent state in the world by both area and population?", True),
    ("Are there exactly 50 member states in the African Union?", False),
    ("Is the headquarters of the African Union located in Addis Ababa, Ethiopia?", True),
    ("Is Canada divided into 50 states?", False),
    ("Did South Sudan gain its independence in 2011?", True),
    ("Is the capital of Canada Ottawa?", True),
    ("Is the G7 a group of the world's seven largest emerging economies?", False),
    ("Is Taiwan a member of the United Nations?", False),
    ("Does the Schengen Agreement allow border-free travel across all member states of the European Union without exception?", False),
    ("Is the Geneva Convention a set of treaties on the humanitarian treatment in war?", True),
    ("Is Russia the largest country in the world by land area?", True),
    ("Does Antarctica have an official, internationally recognized sovereign government?", False),
    ("Did the Brexit transition period officially end on December 31, 2020?", True),
    ("Is the currency of the European Union exclusively the Euro for all member states?", False),
    ("Is Jerusalem recognized as the undivided capital of Israel by the United Nations?", False),
    ("Are the permanent members of the UN Security Council known as the P5?", True),
    ("Is the headquarters of the International Monetary Fund (IMF) located in Washington, D.C.?", True),
    ("Is Greenland an independent sovereign nation?", False),
    ("Does North Korea share a land border with Russia?", True),
    ("Has the United States ever had a female President?", False),
    ("Is Kyoto the current capital city of Japan?", False),
    ("Does Switzerland belong to the European Union?", False),
    ("Did the apartheid regime in South Africa end in the 1990s?", True),
    ("Is the Mercosur a South American trade bloc?", True),
    ("Are there 193 member states in the United Nations?", True),
    ("Is the Organization of Petroleum Exporting Countries (OPEC) headquartered in the Middle East?", False),
    ("Does the equator pass through the continent of South America?", True),
    ("Is India a member of the UN Security Council as a permanent member?", False),
    ("Did the League of Nations successfully prevent World War II?", False),
    ("Is the capital of Turkey Istanbul?", False),
    ("Is Singapore an island city-state?", True),
    ("Is the official language of Brazil Spanish?", False),
    ("Did the Korean War end with a signed peace treaty?", False),
    ("Is the World Health Organization (WHO) a specialized agency of the United Nations?", True),
    ("Is the president of France elected for a 5-year term?", True),
    ("Is the Falkland Islands a British Overseas Territory?", True),
    ("Is the Association of Southeast Asian Nations (ASEAN) headquartered in Jakarta, Indonesia?", True),
    ("Is the official currency of the United Kingdom the Euro?", False),
]

questions = [{"q": f"{i+1}. {q[0]}", "is_yes_correct": q[1]} for i, q in enumerate(questions_data)]

html_template = """<!DOCTYPE html>
<html>
<head>
    <title>Quiz Question {question_num}</title>
</head>
<body>
    <h1>{question_text}</h1>
    <a href="{yes_link}">Yes</a>
    <br><br>
    <a href="{no_link}">No</a>
    <br><br>
    <p>Current Score: {score}</p>
</body>
</html>
"""

result_template = """<!DOCTYPE html>
<html>
<head>
    <title>Quiz Result</title>
</head>
<body>
    <h1>Quiz Complete!</h1>
    <p>You scored {score} out of {total}</p>
    <a href="index.html">Play Again</a>
</body>
</html>
"""

def generate():
    os.chdir('/Users/ubbe/Documents/Quiz')
    
    # Generate question files
    for q_idx, q in enumerate(questions):
        question_num = q_idx + 1
        is_last = (q_idx == len(questions) - 1)
        
        for score in range(q_idx + 1):
            file_name = f"q{question_num}_score{score}.html"
            
            yes_score = score + 1 if q["is_yes_correct"] else score
            no_score = score + 1 if not q["is_yes_correct"] else score
            
            if is_last:
                yes_link = f"result_score{yes_score}.html"
                no_link = f"result_score{no_score}.html"
            else:
                yes_link = f"q{question_num + 1}_score{yes_score}.html"
                no_link = f"q{question_num + 1}_score{no_score}.html"
            
            content = html_template.format(
                question_num=question_num,
                question_text=q["q"],
                yes_link=yes_link,
                no_link=no_link,
                score=score
            )
            
            with open(file_name, 'w', encoding='utf-8') as f:
                f.write(content)
                
    # Generate result files
    total_q = len(questions)
    for score in range(total_q + 1):
        file_name = f"result_score{score}.html"
        
        content = result_template.format(
            score=score,
            total=total_q
        )
        
        with open(file_name, 'w', encoding='utf-8') as f:
            f.write(content)

if __name__ == "__main__":
    generate()
