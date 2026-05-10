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
#In string, when want to use bold can use \033[1m...
        "ISTJ": """ISTJs are practical, organized, and highly dependable individuals.
    They value structure and tradition, preferring clear rules and stability.

    \033[1mStrengths\033[0m
    • Reliable and consistent
    • Strong sense of duty
    • Excellent attention to detail
    • Logical decision-making
    • Organized and disciplined

    \033[1mWeaknesses\033[0m
    • Can be stubborn
    • Difficulty expressing emotions
    • Very judgmental of others
    • Often blames themselves

    \033[1mCommon Careers\033[0m
    • Accountant
    • Military officer
    • Auditor
    • Police officer
    • Operations manager
    • Data analyst

    \033[1mFictional Characters/Famous People\033[0m
    • Hermione Granger (Harry Potter)
    • Captain America
    • Queen Elizabeth II
    • George Washington
    • Mike Ehrmantraut (Breaking Bad)

    \033[1mSources\033[0m
    • Gifts Differing: Understanding Personality Type
    • Myers & Briggs Foundation
    • 16Personalities
    """,

        "ISFJ": """ISFJs are warm, loyal, and caring individuals who prioritize helping others.
    They value harmony, stability, and responsibility.

    \033[1mStrengths\033[0m
    • Compassionate
    • Loyal and dependable
    • Patient and supportive
    • Hardworking
    • Detail-oriented

    \033[1mWeaknesses\033[0m
    • Sensitive to criticism
    • Difficulty setting boundaries
    • Can suppress emotions
    • Avoids conflict

    \033[1mCommon Careers\033[0m
    • Nurse
    • Teacher
    • Counselor
    • Social worker
    • HR specialist
    • Healthcare administrator

    \033[1mFictional Characters/Famous People\033[0m
    • Samwise Gamgee
    • Mother Teresa
    • Pam Beesly
    • Kate Middleton
    • Steve Rogers

    \033[1mSources\033[0m
    • Please Understand Me II
    • Myers & Briggs Foundation
    • 16Personalities
    """,

        "INFJ": """INFJs are insightful, idealistic, and deeply thoughtful individuals.
    They seek meaning, purpose, and emotional connection.

    \033[1mStrengths\033[0m
    • Empathetic
    • Visionary
    • Creative
    • Determined
    • Reflective

    \033[1mWeaknesses\033[0m
    • Perfectionistic
    • Emotionally overwhelmed easily
    • Very private
    • Burns out from helping others

    \033[1mCommon Careers\033[0m
    • Psychologist
    • Writer
    • Counselor
    • Professor
    • Human rights advocate
    • UX researcher

    \033[1mFictional Characters/Famous People\033[0m
    • Martin Luther King Jr.
    • Aragorn
    • Lisa Simpson
    • Nelson Mandela
    • Atticus Finch

    \033[1mSources\033[0m
    • Gifts Differing: Understanding Personality Type
    • Myers & Briggs Foundation
    • 16Personalities
    """,

        "INTJ": """INTJs are strategic, independent thinkers who enjoy mastering systems.
    They are analytical, future-focused, and highly goal-oriented.

    \033[1mStrengths\033[0m
    • Strategic thinking
    • Independent
    • Analytical
    • Innovative
    • Goal-focused

    \033[1mWeaknesses\033[0m
    • Can appear arrogant
    • Emotionally reserved
    • Perfectionistic
    • Impatient with incompetence

    \033[1mCommon Careers\033[0m
    • Scientist
    • Software engineer
    • Architect
    • Financial analyst
    • Researcher
    • Strategist

    \033[1mFictional Characters/Famous People\033[0m
    • Elon Musk
    • Gandalf
    • Nikola Tesla
    • Walter White
    • Wednesday Addams

    \033[1mSources\033[0m
    • Please Understand Me II
    • Myers & Briggs Foundation
    • 16Personalities
    """,

        "ISTP": """ISTPs are adaptable and practical problem-solvers who enjoy understanding how things work.
    They are calm under pressure and action-oriented.

    \033[1mStrengths\033[0m
    • Independent
    • Practical
    • Adaptable
    • Calm in emergencies
    • Mechanically skilled

    \033[1mWeaknesses\033[0m
    • Emotionally detached
    • Easily bored
    • Risk-taking tendencies
    • Avoids commitment

    \033[1mCommon Careers\033[0m
    • Engineer
    • Mechanic
    • Pilot
    • Electrician
    • Firefighter
    • Forensic technician

    \033[1mFictional Characters/Famous People\033[0m
    • Bruce Lee
    • James Bond
    • Black Widow
    • Levi Ackerman
    • Clint Eastwood

    \033[1mSources\033[0m
    • Gifts Differing: Understanding Personality Type
    • Myers & Briggs Foundation
    • 16Personalities
    """,

        "ISFP": """ISFPs are artistic, gentle, and emotionally aware individuals.
    They value freedom, creativity, and authenticity.

    \033[1mStrengths\033[0m
    • Creative
    • Compassionate
    • Flexible
    • Observant
    • Easygoing

    \033[1mWeaknesses\033[0m
    • Sensitive to criticism
    • Avoids planning
    • Unpredictable
    • Dislikes conflict

    \033[1mCommon Careers\033[0m
    • Artist
    • Musician
    • Fashion designer
    • Photographer
    • Veterinarian
    • Graphic designer

    \033[1mFictional Characters/Famous People\033[0m
    • Harry Potter
    • Frodo Baggins
    • Zendaya
    • Michael Jackson
    • Lana Del Rey

    \033[1mSources\033[0m
    • Please Understand Me II
    • Myers & Briggs Foundation
    • 16Personalities
    """,

        "INFP": """INFPs are imaginative, idealistic, and emotionally deep individuals.
    They value authenticity, creativity, and personal meaning.

    \033[1mStrengths\033[0m
    • Creative
    • Empathetic
    • Open-minded
    • Passionate
    • Imaginative

    \033[1mWeaknesses\033[0m
    • Overly idealistic
    • Sensitive to criticism
    • Procrastinates
    • Emotionally intense

    \033[1mCommon Careers\033[0m
    • Author
    • Therapist
    • Animator
    • Musician
    • Screenwriter
    • Nonprofit worker

    \033[1mFictional Characters/Famous People\033[0m
    • Luna Lovegood
    • William Shakespeare
    • Johnny Depp
    • Anne Shirley
    • Peter Parker

    \033[1mSources\033[0m
    • Gifts Differing: Understanding Personality Type
    • Myers & Briggs Foundation
    • 16Personalities
    """,

        "INTP": """INTPs are analytical and curious thinkers who enjoy theories and abstract concepts.
    They value logic, innovation, and intellectual exploration.

    \033[1mStrengths\033[0m
    • Logical
    • Curious
    • Innovative
    • Independent-minded
    • Open to possibilities

    \033[1mWeaknesses\033[0m
    • Socially detached
    • Overthinks
    • Neglects practical matters
    • Difficulty expressing emotions

    \033[1mCommon Careers\033[0m
    • Programmer
    • Mathematician
    • Philosopher
    • Physicist
    • Systems analyst
    • AI researcher

    \033[1mFictional Characters/Famous People\033[0m
    • Albert Einstein
    • Sherlock Holmes
    • Bill Gates
    • L (Death Note)
    • Neo (The Matrix)

    \033[1mSources\033[0m
    • Please Understand Me II
    • Myers & Briggs Foundation
    • 16Personalities
    """,

        "ESTP": """ESTPs are energetic and action-oriented individuals who thrive in fast-paced environments.
    They enjoy challenge, excitement, and risk-taking.

    \033[1mStrengths\033[0m
    • Bold
    • Confident
    • Adaptable
    • Persuasive
    • Practical

    \033[1mWeaknesses\033[0m
    • Impulsive
    • Easily bored
    • Risk-taking
    • Ignores emotional consequences

    \033[1mCommon Careers\033[0m
    • Entrepreneur
    • Athlete
    • Salesperson
    • Emergency responder
    • Stock trader
    • Marketing specialist

    \033[1mFictional Characters/Famous People\033[0m
    • Tony Stark
    • Han Solo
    • Madonna
    • Eddie Murphy
    • Jordan Belfort

    \033[1mSources\033[0m
    • Gifts Differing: Understanding Personality Type
    • Myers & Briggs Foundation
    • 16Personalities
    """,

        "ESFP": """ESFPs are social, enthusiastic, and spontaneous individuals.
    They enjoy entertaining others and living in the moment.

    \033[1mStrengths\033[0m
    • Charismatic
    • Optimistic
    • Fun-loving
    • Expressive
    • Sociable

    \033[1mWeaknesses\033[0m
    • Easily distracted
    • Dislikes routine
    • Impulsive
    • Avoids difficult conversations

    \033[1mCommon Careers\033[0m
    • Actor
    • Performer
    • Event planner
    • Influencer
    • Public relations specialist
    • Hospitality manager

    \033[1mFictional Characters/Famous People\033[0m
    • Elvis Presley
    • Miley Cyrus
    • Rapunzel
    • Joey Tribbiani
    • Harley Quinn

    \033[1mSources\033[0m
    • Please Understand Me II
    • Myers & Briggs Foundation
    • 16Personalities
    """,

        "ENFP": """ENFPs are energetic, imaginative, and people-oriented individuals.
    They enjoy exploring possibilities and inspiring others.

    \033[1mStrengths\033[0m
    • Enthusiastic
    • Creative
    • Charismatic
    • Curious
    • Emotionally intelligent

    \033[1mWeaknesses\033[0m
    • Difficulty focusing
    • Easily overwhelmed
    • Overcommits
    • Sensitive to criticism

    \033[1mCommon Careers\033[0m
    • Journalist
    • Entrepreneur
    • Counselor
    • Actor
    • Creative director
    • Marketing strategist

    \033[1mFictional Characters/Famous People\033[0m
    • Robin Williams
    • Naruto Uzumaki
    • Willy Wonka
    • Robert Downey Jr.
    • Phil Dunphy

    \033[1mSources\033[0m
    • Gifts Differing: Understanding Personality Type
    • Myers & Briggs Foundation
    • 16Personalities
    """,

        "ENTP": """ENTPs are inventive and intellectually curious individuals.
    They enjoy debating ideas and exploring innovation.

    \033[1mStrengths\033[0m
    • Quick-thinking
    • Innovative
    • Charismatic
    • Adaptable
    • Strong problem-solving skills

    \033[1mWeaknesses\033[0m
    • Argumentative
    • Easily distracted
    • Neglects details
    • Dislikes routine

    \033[1mCommon Careers\033[0m
    • Lawyer
    • Startup founder
    • Inventor
    • Consultant
    • Creative strategist
    • Political analyst

    \033[1mFictional Characters/Famous People\033[0m
    • Tyrion Lannister
    • Mark Twain
    • Deadpool
    • Tony Stark
    • The Joker

    \033[1mSources\033[0m
    • Please Understand Me II
    • Myers & Briggs Foundation
    • 16Personalities
    """,

        "ESTJ": """ESTJs are structured, efficient, and leadership-oriented individuals.
    They value order, responsibility, and tradition.

    \033[1mStrengths\033[0m
    • Strong leadership
    • Organized
    • Decisive
    • Responsible
    • Efficient

    \033[1mWeaknesses\033[0m
    • Controlling
    • Resistant to new ideas
    • Harsh communication
    • Impatient

    \033[1mCommon Careers\033[0m
    • Business manager
    • Judge
    • Military leader
    • Project manager
    • Police supervisor
    • Administrator

    \033[1mFictional Characters/Famous People\033[0m
    • Dwight Schrute
    • Judge Judy
    • Princess Leia
    • Franklin D. Roosevelt
    • Miranda Priestly

    \033[1mSources\033[0m
    • Gifts Differing: Understanding Personality Type
    • Myers & Briggs Foundation
    • 16Personalities
    """,

        "ESFJ": """ESFJs are sociable, caring, and community-oriented individuals.
    They enjoy helping others and maintaining harmony.

    \033[1mStrengths\033[0m
    • Supportive
    • Loyal
    • Organized
    • Reliable
    • Strong interpersonal skills

    \033[1mWeaknesses\033[0m
    • Seeks approval too much
    • Sensitive to criticism
    • Difficulty adapting to change
    • Can become controlling

    \033[1mCommon Careers\033[0m
    • Teacher
    • Nurse
    • Event coordinator
    • Human resources specialist
    • Customer relations manager
    • Community organizer

    \033[1mFictional Characters/Famous People\033[0m
    • Monica Geller
    • Taylor Swift
    • Cinderella
    • Molly Weasley
    • Jennifer Garner

    \033[1mSources\033[0m
    • Please Understand Me II
    • Myers & Briggs Foundation
    • 16Personalities
    """,

        "ENFJ": """ENFJs are charismatic and empathetic leaders who enjoy helping others grow.
    They are inspirational, organized, and emotionally aware.

    \033[1mStrengths\033[0m
    • Inspirational
    • Empathetic
    • Organized
    • Loyal
    • Strong communication skills

    \033[1mWeaknesses\033[0m
    • Overextends themselves
    • Sensitive to conflict
    • Overly idealistic
    • Needs validation

    \033[1mCommon Careers\033[0m
    • Teacher
    • Coach
    • Psychologist
    • Public speaker
    • Politician
    • Nonprofit leader

    \033[1mFictional Characters/Famous People\033[0m
    • Oprah Winfrey
    • Barack Obama
    • Mufasa
    • Ted Lasso
    • Daenerys Targaryen

    \033[1mSources\033[0m
    • Gifts Differing: Understanding Personality Type
    • Myers & Briggs Foundation
    • 16Personalities
    """,

        "ENTJ": """ENTJs are ambitious and strategic individuals who naturally take leadership roles.
    They are highly driven and focused on long-term goals.

    \033[1mStrengths\033[0m
    • Strong leadership
    • Strategic mindset
    • Confident
    • Efficient organizer
    • Goal-focused

    \033[1mWeaknesses\033[0m
    • Intimidating
    • Impatient with emotions
    • Workaholic tendencies
    • Overly competitive

    \033[1mCommon Careers\033[0m
    • CEO
    • Attorney
    • Entrepreneur
    • Executive consultant
    • Engineering manager
    • Investment banker

    \033[1mFictional Characters/Famous People\033[0m
    • Steve Jobs
    • Gordon Ramsay
    • Napoleon Bonaparte
    • Light Yagami
    • Miranda Bailey

    \033[1mSources\033[0m
    • Please Understand Me II
    • Myers & Briggs Foundation
    • 16Personalities
    """
    }
    return descriptions.get(mbti_type, "Unique personality type!")
