def calculate_result(scores):
    mbti = ""
    mbti += "E" if scores.get('E', 0) >= scores.get('I', 0) else "I"
    mbti += "S" if scores.get('S', 0) >= scores.get('N', 0) else "N"
    mbti += "T" if scores.get('T', 0) >= scores.get('F', 0) else "F"
    mbti += "J" if scores.get('J', 0) >= scores.get('P', 0) else "P"
    #This is a oneline version for if statement
    #If score.get('E', 0=default value if key is missing)>= B, then mbti add "E"
    return mbti

def get_description(mbti_type):
    descriptions = {
#In Telegram we use <b>...</b> for bold instead of \033[1m which only works in terminal

        "ISTJ": """ISTJs are practical, organized, and highly dependable individuals.
They value structure and tradition, preferring clear rules and stability.

<b>Strengths</b>
• Reliable and consistent
• Strong sense of duty
• Excellent attention to detail
• Logical decision-making
• Organized and disciplined

<b>Weaknesses</b>
• Can be stubborn
• Difficulty expressing emotions
• Very judgmental of others
• Often blames themselves

<b>Common Careers</b>
• Accountant
• Military officer
• Auditor
• Police officer
• Operations manager
• Data analyst

<b>Fictional Characters/Famous People</b>
• Hermione Granger (Harry Potter)
• Captain America
• Queen Elizabeth II
• George Washington
• Mike Ehrmantraut (Breaking Bad)

<b>Sources</b>
• Gifts Differing: Understanding Personality Type
• Myers &amp; Briggs Foundation
• 16Personalities
""",

        "ISFJ": """ISFJs are warm, loyal, and caring individuals who prioritize helping others.
They value harmony, stability, and responsibility.

<b>Strengths</b>
• Compassionate
• Loyal and dependable
• Patient and supportive
• Hardworking
• Detail-oriented

<b>Weaknesses</b>
• Sensitive to criticism
• Difficulty setting boundaries
• Can suppress emotions
• Avoids conflict

<b>Common Careers</b>
• Nurse
• Teacher
• Counselor
• Social worker
• HR specialist
• Healthcare administrator

<b>Fictional Characters/Famous People</b>
• Samwise Gamgee
• Mother Teresa
• Pam Beesly
• Kate Middleton
• Steve Rogers

<b>Sources</b>
• Please Understand Me II
• Myers &amp; Briggs Foundation
• 16Personalities
""",

        "INFJ": """INFJs are insightful, idealistic, and deeply thoughtful individuals.
They seek meaning, purpose, and emotional connection.

<b>Strengths</b>
• Empathetic
• Visionary
• Creative
• Determined
• Reflective

<b>Weaknesses</b>
• Perfectionistic
• Emotionally overwhelmed easily
• Very private
• Burns out from helping others

<b>Common Careers</b>
• Psychologist
• Writer
• Counselor
• Professor
• Human rights advocate
• UX researcher

<b>Fictional Characters/Famous People</b>
• Martin Luther King Jr.
• Aragorn
• Lisa Simpson
• Nelson Mandela
• Atticus Finch

<b>Sources</b>
• Gifts Differing: Understanding Personality Type
• Myers &amp; Briggs Foundation
• 16Personalities
""",

        "INTJ": """INTJs are strategic, independent thinkers who enjoy mastering systems.
They are analytical, future-focused, and highly goal-oriented.

<b>Strengths</b>
• Strategic thinking
• Independent
• Analytical
• Innovative
• Goal-focused

<b>Weaknesses</b>
• Can appear arrogant
• Emotionally reserved
• Perfectionistic
• Impatient with incompetence

<b>Common Careers</b>
• Scientist
• Software engineer
• Architect
• Financial analyst
• Researcher
• Strategist

<b>Fictional Characters/Famous People</b>
• Elon Musk
• Gandalf
• Nikola Tesla
• Walter White
• Wednesday Addams

<b>Sources</b>
• Please Understand Me II
• Myers &amp; Briggs Foundation
• 16Personalities
""",

        "ISTP": """ISTPs are adaptable and practical problem-solvers who enjoy understanding how things work.
They are calm under pressure and action-oriented.

<b>Strengths</b>
• Independent
• Practical
• Adaptable
• Calm in emergencies
• Mechanically skilled

<b>Weaknesses</b>
• Emotionally detached
• Easily bored
• Risk-taking tendencies
• Avoids commitment

<b>Common Careers</b>
• Engineer
• Mechanic
• Pilot
• Electrician
• Firefighter
• Forensic technician

<b>Fictional Characters/Famous People</b>
• Bruce Lee
• James Bond
• Black Widow
• Levi Ackerman
• Clint Eastwood

<b>Sources</b>
• Gifts Differing: Understanding Personality Type
• Myers &amp; Briggs Foundation
• 16Personalities
""",

        "ISFP": """ISFPs are artistic, gentle, and emotionally aware individuals.
They value freedom, creativity, and authenticity.

<b>Strengths</b>
• Creative
• Compassionate
• Flexible
• Observant
• Easygoing

<b>Weaknesses</b>
• Sensitive to criticism
• Avoids planning
• Unpredictable
• Dislikes conflict

<b>Common Careers</b>
• Artist
• Musician
• Fashion designer
• Photographer
• Veterinarian
• Graphic designer

<b>Fictional Characters/Famous People</b>
• Harry Potter
• Frodo Baggins
• Zendaya
• Michael Jackson
• Lana Del Rey

<b>Sources</b>
• Please Understand Me II
• Myers &amp; Briggs Foundation
• 16Personalities
""",

        "INFP": """INFPs are imaginative, idealistic, and emotionally deep individuals.
They value authenticity, creativity, and personal meaning.

<b>Strengths</b>
• Creative
• Empathetic
• Open-minded
• Passionate
• Imaginative

<b>Weaknesses</b>
• Overly idealistic
• Sensitive to criticism
• Procrastinates
• Emotionally intense

<b>Common Careers</b>
• Author
• Therapist
• Animator
• Musician
• Screenwriter
• Nonprofit worker

<b>Fictional Characters/Famous People</b>
• Luna Lovegood
• William Shakespeare
• Johnny Depp
• Anne Shirley
• Peter Parker

<b>Sources</b>
• Gifts Differing: Understanding Personality Type
• Myers &amp; Briggs Foundation
• 16Personalities
""",

        "INTP": """INTPs are analytical and curious thinkers who enjoy theories and abstract concepts.
They value logic, innovation, and intellectual exploration.

<b>Strengths</b>
• Logical
• Curious
• Innovative
• Independent-minded
• Open to possibilities

<b>Weaknesses</b>
• Socially detached
• Overthinks
• Neglects practical matters
• Difficulty expressing emotions

<b>Common Careers</b>
• Programmer
• Mathematician
• Philosopher
• Physicist
• Systems analyst
• AI researcher

<b>Fictional Characters/Famous People</b>
• Albert Einstein
• Sherlock Holmes
• Bill Gates
• L (Death Note)
• Neo (The Matrix)

<b>Sources</b>
• Please Understand Me II
• Myers &amp; Briggs Foundation
• 16Personalities
""",

        "ESTP": """ESTPs are energetic and action-oriented individuals who thrive in fast-paced environments.
They enjoy challenge, excitement, and risk-taking.

<b>Strengths</b>
• Bold
• Confident
• Adaptable
• Persuasive
• Practical

<b>Weaknesses</b>
• Impulsive
• Easily bored
• Risk-taking
• Ignores emotional consequences

<b>Common Careers</b>
• Entrepreneur
• Athlete
• Salesperson
• Emergency responder
• Stock trader
• Marketing specialist

<b>Fictional Characters/Famous People</b>
• Tony Stark
• Han Solo
• Madonna
• Eddie Murphy
• Jordan Belfort

<b>Sources</b>
• Gifts Differing: Understanding Personality Type
• Myers &amp; Briggs Foundation
• 16Personalities
""",

        "ESFP": """ESFPs are social, enthusiastic, and spontaneous individuals.
They enjoy entertaining others and living in the moment.

<b>Strengths</b>
• Charismatic
• Optimistic
• Fun-loving
• Expressive
• Sociable

<b>Weaknesses</b>
• Easily distracted
• Dislikes routine
• Impulsive
• Avoids difficult conversations

<b>Common Careers</b>
• Actor
• Performer
• Event planner
• Influencer
• Public relations specialist
• Hospitality manager

<b>Fictional Characters/Famous People</b>
• Elvis Presley
• Miley Cyrus
• Rapunzel
• Joey Tribbiani
• Harley Quinn

<b>Sources</b>
• Please Understand Me II
• Myers &amp; Briggs Foundation
• 16Personalities
""",

        "ENFP": """ENFPs are energetic, imaginative, and people-oriented individuals.
They enjoy exploring possibilities and inspiring others.

<b>Strengths</b>
• Enthusiastic
• Creative
• Charismatic
• Curious
• Emotionally intelligent

<b>Weaknesses</b>
• Difficulty focusing
• Easily overwhelmed
• Overcommits
• Sensitive to criticism

<b>Common Careers</b>
• Journalist
• Entrepreneur
• Counselor
• Actor
• Creative director
• Marketing strategist

<b>Fictional Characters/Famous People</b>
• Robin Williams
• Naruto Uzumaki
• Willy Wonka
• Robert Downey Jr.
• Phil Dunphy

<b>Sources</b>
• Gifts Differing: Understanding Personality Type
• Myers &amp; Briggs Foundation
• 16Personalities
""",

        "ENTP": """ENTPs are inventive and intellectually curious individuals.
They enjoy debating ideas and exploring innovation.

<b>Strengths</b>
• Quick-thinking
• Innovative
• Charismatic
• Adaptable
• Strong problem-solving skills

<b>Weaknesses</b>
• Argumentative
• Easily distracted
• Neglects details
• Dislikes routine

<b>Common Careers</b>
• Lawyer
• Startup founder
• Inventor
• Consultant
• Creative strategist
• Political analyst

<b>Fictional Characters/Famous People</b>
• Tyrion Lannister
• Mark Twain
• Deadpool
• Tony Stark
• The Joker

<b>Sources</b>
• Please Understand Me II
• Myers &amp; Briggs Foundation
• 16Personalities
""",

        "ESTJ": """ESTJs are structured, efficient, and leadership-oriented individuals.
They value order, responsibility, and tradition.

<b>Strengths</b>
• Strong leadership
• Organized
• Decisive
• Responsible
• Efficient

<b>Weaknesses</b>
• Controlling
• Resistant to new ideas
• Harsh communication
• Impatient

<b>Common Careers</b>
• Business manager
• Judge
• Military leader
• Project manager
• Police supervisor
• Administrator

<b>Fictional Characters/Famous People</b>
• Dwight Schrute
• Judge Judy
• Princess Leia
• Franklin D. Roosevelt
• Miranda Priestly

<b>Sources</b>
• Gifts Differing: Understanding Personality Type
• Myers &amp; Briggs Foundation
• 16Personalities
""",

        "ESFJ": """ESFJs are sociable, caring, and community-oriented individuals.
They enjoy helping others and maintaining harmony.

<b>Strengths</b>
• Supportive
• Loyal
• Organized
• Reliable
• Strong interpersonal skills

<b>Weaknesses</b>
• Seeks approval too much
• Sensitive to criticism
• Difficulty adapting to change
• Can become controlling

<b>Common Careers</b>
• Teacher
• Nurse
• Event coordinator
• Human resources specialist
• Customer relations manager
• Community organizer

<b>Fictional Characters/Famous People</b>
• Monica Geller
• Taylor Swift
• Cinderella
• Molly Weasley
• Jennifer Garner

<b>Sources</b>
• Please Understand Me II
• Myers &amp; Briggs Foundation
• 16Personalities
""",

        "ENFJ": """ENFJs are charismatic and empathetic leaders who enjoy helping others grow.
They are inspirational, organized, and emotionally aware.

<b>Strengths</b>
• Inspirational
• Empathetic
• Organized
• Loyal
• Strong communication skills

<b>Weaknesses</b>
• Overextends themselves
• Sensitive to conflict
• Overly idealistic
• Needs validation

<b>Common Careers</b>
• Teacher
• Coach
• Psychologist
• Public speaker
• Politician
• Nonprofit leader

<b>Fictional Characters/Famous People</b>
• Oprah Winfrey
• Barack Obama
• Mufasa
• Ted Lasso
• Daenerys Targaryen

<b>Sources</b>
• Gifts Differing: Understanding Personality Type
• Myers &amp; Briggs Foundation
• 16Personalities
""",

        "ENTJ": """ENTJs are ambitious and strategic individuals who naturally take leadership roles.
They are highly driven and focused on long-term goals.

<b>Strengths</b>
• Strong leadership
• Strategic mindset
• Confident
• Efficient organizer
• Goal-focused

<b>Weaknesses</b>
• Intimidating
• Impatient with emotions
• Workaholic tendencies
• Overly competitive

<b>Common Careers</b>
• CEO
• Attorney
• Entrepreneur
• Executive consultant
• Engineering manager
• Investment banker

<b>Fictional Characters/Famous People</b>
• Steve Jobs
• Gordon Ramsay
• Napoleon Bonaparte
• Light Yagami
• Miranda Bailey

<b>Sources</b>
• Please Understand Me II
• Myers &amp; Briggs Foundation
• 16Personalities
"""
    }
    return descriptions.get(mbti_type, "Unique personality type!")