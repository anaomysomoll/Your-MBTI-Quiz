#We import telegram bot library
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
# InlineKeyboardButton is a single clickable button inside a message
#InlineKeyboardMarkup is a layout that holds buttons as row/columns
#Update: The incoming event object
from telegram.ext import CallbackQueryHandler, CommandHandler, ContextTypes
#
from bot.states import init_user, reset_user, user_data, next_question, update_score
# init_user, and reset_user is functions from our states.py
from logic.questions import QUESTIONS
from logic.results import calculate_result, get_description

def start_keyboard():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("Start Quiz", callback_data="start_quiz")]
    ])
#Returns a keyboard with one button "Start Quiz", it will send "start_quiz" as callback_data

#Nested Lists
def answer_keyboard():
    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton("✅ Strongly Agree", callback_data="Strongly Agree"),
            InlineKeyboardButton("🙂 Agree",          callback_data="Agree"),
            InlineKeyboardButton("😐 Neutral",        callback_data="Neutral"),
        ],
        [
            InlineKeyboardButton("🙁 Disagree",          callback_data="Disagree"),
            InlineKeyboardButton("❌ Strongly Disagree", callback_data="Strongly Disagree"),
        ]
    ])

#Dictionary/Map: converts a button click into a number for our calculation
SCORE_MAP = {
    "Strongly Agree": 2,
    "Agree": 1,
    "Neutral": 0,
    "Disagree": -1,
    "Strongly Disagree": -2,
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id #Gets the telegram user's unique ID number
    init_user(user_id) #Creates a new entry state for this user in states.py
    context.user_data['last_message'] = None

    await update.message.reply_text(
        "🙂‍↔️ Welcome to the <b>MBTI Quiz!</b>\n\nPress Start when you're ready.",
        parse_mode="HTML", #Allow us to use HTML syntax for bold statement
        reply_markup=start_keyboard(),
    ) #attaches the Start Quiz button to the message


async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query #Gets the button click event object
    user_id = query.from_user.id #Gets user

    try:
        await query.answer() #Tells Telegram the click was recieved
    except Exception:
        pass  # query expired (>10s timeout), that's fine — still process the button

    if user_id not in user_data: #Uhh kinda like safety
        await query.message.reply_text(
            "⚠️ Session expired or not started.\nPlease type /start to begin!"
        )
        return

    # ── Start quiz ─────────────────────────────────────────────────────────────
    if query.data == "start_quiz": #Checks which button was clicked by reading callback_data
        try:
            await query.message.edit_reply_markup(reply_markup=None)
        except Exception:
            pass  # buttons already removed (e.g. double tap), that's fine
#Removes the Start button after clicking
        question_index = user_data[user_id]['question_index'] #Reads current question number from states.py
        question = QUESTIONS[question_index]['text'] #From questions.py
        user_data[user_id]['current_state'] = 'QUESTION_LOOP' #Updates state - tracks where the suer is in the quiz

        msg = await query.message.reply_text(
            f"❓ <b>Question {question_index + 1}/{len(QUESTIONS)}</b>\n\n{question}", #f-string
            parse_mode="HTML",
            reply_markup=answer_keyboard(),
        )
        context.user_data['last_message'] = msg

    # Answering a question
    elif query.data in SCORE_MAP: #Checks if the click was one of the 6 answer buttons
        question_index = user_data[user_id]['question_index']
        dimension = QUESTIONS[question_index]['dimension'] #Gets MBTI dimension
        update_score(user_id, dimension, SCORE_MAP[query.data])
        #Converts the button click to score number before adding it to its dimension
        try:
            await query.message.edit_reply_markup(reply_markup=None)
        except Exception:
            pass  # buttons already removed (e.g. double tap), that's fine

        next_question(user_id) #increments question_index by 1 in state
        question_index = user_data[user_id]['question_index']

        if question_index < len(QUESTIONS): #If no more question, then show results)
            question = QUESTIONS[question_index]['text']

            msg = await query.message.reply_text(
                f"❓ <b>Question {question_index + 1}/{len(QUESTIONS)}</b>\n\n{question}",
                parse_mode="HTML",
                reply_markup=answer_keyboard(),
            )
            context.user_data['last_message'] = msg

        else:
            scores = user_data[user_id]['scores']
            mbti_type = calculate_result(scores)
            description = get_description(mbti_type)

            # FIX: parse_mode="HTML" — safe against * and _ in description text
            await query.message.reply_text(
                f"🎉 <b>Quiz Complete!</b>\n\n"
                f"Your MBTI type is: <b>{mbti_type}</b>\n\n"
                f"{description}",
                parse_mode="HTML",
                reply_markup=InlineKeyboardMarkup([
                    [InlineKeyboardButton("🔄 Restart Quiz", callback_data="restart")]
                ]),
            )
            user_data[user_id]['current_state'] = 'RESULT'

    # Restart quiz
    elif query.data == "restart":
        reset_user(user_id)
        context.user_data['last_message'] = None

        await query.message.edit_text(
            "🔄 Quiz restarted! Press <b>Start Quiz</b> to go again.",
            parse_mode="HTML",
            reply_markup=start_keyboard(),
        )