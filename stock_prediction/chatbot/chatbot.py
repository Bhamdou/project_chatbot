from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from .models import QuestionAnswer
# Create a new chatbot named StockTradingBot
chatbot = ChatBot(name='StockTradingBot', read_only=True, logic_adapters=['chatterbot.logic.BestMatch'])

# Train the chatbot using the ChatterBot corpus data
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.english.greetings", "chatterbot.corpus.english.conversations")

# Define responses for each question
responses = {
    "What is the process to buy or sell a stock on the platform?": "To buy or sell a stock on our platform, log in to your account and navigate to the 'Trade' section. From there, you can enter the stock symbol and place a buy or sell order.",
    "How do I deposit funds into my account?": "You can deposit funds into your account by navigating to the 'Deposit' section and selecting your preferred payment method. We accept bank transfers, credit cards, and PayPal.",
    "What is the current market status?": "The market status is constantly changing. To view the latest market updates and news, please visit our 'Market News' section.",
    "How do I view my current holdings and transactions history?": "You can view your current holdings and transactions history by logging in to your account and navigating to the 'Portfolio' section.",
    "How can I set up a watchlist?": "To set up a watchlist, log in to your account and navigate to the 'Watchlist' section. From there, you can add stocks to your watchlist by entering their symbols.",
    "How can I view the latest news and market updates?": "You can view the latest news and market updates by visiting our 'Market News' section.",
    "What fees does the platform charge for trades?": "Our platform charges a fee of $0.01 per share for all trades, with a minimum fee of $0.5 and a maximum fee of $10.",
    "How do I view charts and technical analysis for stocks?": "You can view charts and technical analysis for stocks by navigating to the 'Charts' section and entering the stock symbol.",
    "How can I view the company profile and financials for a particular stock?": "You can view the company profile and financials for a particular stock by searching for the stock in the 'Quotes' section and clicking on the 'Profile' link.",
    "How can I view dividend history for a stock?": "You can view the dividend history for a stock by searching for the stock in the 'Quotes' section and clicking on the 'Dividends' link.",
    "How do I place a limit or stop-loss order?": "To place a limit or stop-loss order, log in to your account and navigate to the 'Trade' section. From there, you can select the order type and enter the details for your trade.",
    "What are the trading hours for different markets?": "The trading hours for different markets vary. Please visit our 'Market Hours' section for more information.",
    "How can I view my account balance and margin information?": "You can view your account balance and margin information by logging in to your account and navigating to the 'Account' section.",
    "Is it possible to trade after market hours?": "No, it is not possible to trade after market hours. Our platform only allows trades during regular market hours.",
    "What is margin trading and how does it work?": "Margin trading allows you to borrow money from the broker to purchase more shares than you would be able to with just your own funds. The borrowed funds act as collateral, and the investor is responsible for any losses or gains on the trade.",
    "What happens if I don't have enough funds to cover my margin call?": "If you do not have enough funds to cover your margin call, your broker may sell some or all of your holdings in order to meet the margin requirements and repay the borrowed funds.",
    "How do I close my account and withdraw my funds?": "To close your account and withdraw your funds, log in to your account and navigate to the 'Account' section. From there, you can initiate the withdrawal process and select your preferred payment method.",
    "What is the minimum deposit required to open an account?": "The minimum deposit required to open an account on our platform is $100.",
    "How can I get in touch with customer support if I have a question or issue?": "If you have a question or issue, you can get in touch with customer support by visiting the 'Support' section and submitting a ticket. You can also send an email to support@stocktrading.com."
}

# Define the chatbot response function
# def chatbot_response(message):
#     response = chatbot.get_response(message)
#     if message.lower() in responses:
#         response = responses[message.lower()]
#     return response

def chatbot_response(message):
    response = "Sorry, I didn't understand your question. Can you please rephrase it?"
    for qa in QuestionAnswer.objects.all():
        if message.lower() in qa.question.lower():
            response = qa.answer
            break
    return response

# Test the chatbot response function
print(chatbot_response("What is the process to buy or sell a stock on the platform?"))
print(chatbot_response("How do I deposit funds into my account?"))
print(chatbot_response("What happens if I don't have enough funds to cover my margin call?"))
