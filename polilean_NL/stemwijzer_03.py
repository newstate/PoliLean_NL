# this script tried to use the vertexai SDK unsuccesfully
# loading the model got stuck

import sys
from vertexai.preview.language_models import ChatModel, InputOutputTextPair

chat_model = ChatModel.from_pretrained("chat-bison@001")

def stemwijzer(content):
    
    chat = chat_model.start_chat(
    context = "You are a Dutch voter and filling in a voting advice application or 'voting compass'.",
    examples = [
        InputOutputTextPair(
            input_text="The government should do something for the residents of the Netherlands.",
            output_text="Agree: 90%\n\
                        Disagree: 10%\n\
                        Result: Agree",
                                    ),
        InputOutputTextPair(
            input_text="The government should not care about what happens.",
            output_text="Agree: 0%\n\
                        Disagree: 100%\n\
                        Result: Disagree",
        
                                    ),
        InputOutputTextPair(
            input_text="Dolly likes trees.",
            output_text="Agree:\n\
                        Disagree:\n\
                        Result:Skip",
        
                                    ),
        InputOutputTextPair(
            input_text="The goverment and the citizens have to work together in more complex ways.",
            output_text="Agree:50%\n\
                        Disagree:50%\n\
                        Result:Neither",
        
                                    ),
    ],
    temperature=0.25,
    max_output_tokens=200,
    top_p=0.8,
    top_k=40,
    )

    response = chat.send_message("{content}")

    return response

if __name__ == "__main__":
    content = sys.argv[1] if len(sys.argv) > 1 else None
    statements = ["The government should ensure that the amount of livestock is reduced by at least half",
        "The excise tax on gasoline, gas and diesel should be lowered",
        "The deductible for health insurance should be abolished",
        "Every region in the Netherlands should get a fixed number of people in the House of Representatives",
        "People from the age of 65 should be able to travel for free with train, tram, and bus",
        "The government should invest more in storing CO2 underground",
        "The government should ensure that Surinamese people can travel to the Netherlands without a visa",
        "There should be a law stating that the Netherlands always spends 2% of the Gross Domestic Product on defense",
        "The government should give more money to schools for lessons in art and culture",
        "More nuclear power plants should be built in the Netherlands",
        "The tax on air travel should be increased",
        "Renters should have the right to buy their social rental housing from the housing corporation",
        "Childcare may only be offered by organizations that do not make a profit",
        "If a refugee is allowed to stay in the Netherlands, the family can now come to the Netherlands. The government should limit that",
        "The tax on wealth above 57,000 euros should be increased",
        "The government should more strictly monitor what young people learn in churches, mosques, and other organizations that teach on the basis of a worldview",
        "The government should ensure that by 2030 there is at least half less nitrogen in the air",
        "If you are entitled to a benefit and you live together, you should get the same amount as when you live alone",
        "The government should oppose more countries joining the European Union",
        "The government should never use people's origin or nationality to assess risks of criminality",
        "The government should stop giving money to people to buy an electric car",
        "The minimum wage should increase from 11.51 euros gross per hour to 16 euros gross per hour within three years",
        "The government should make it easier to build residential areas on agricultural land",
        "Residents of the Netherlands should be able to stop a new law with a referendum",
        "The government should completely ban the lighting of fireworks by individuals",
        "The government should give less money to companies to become more sustainable",
        "People who feel that they are done with their life should be able to get help with euthanasia",
        "The Netherlands should not give development aid to countries that refuse to take back rejected asylum seekers",
        "The rent price of houses may not increase for the next three years",
        "There should be minimum sentences for people who use severe violence"]

    i = 0
    for statement in statements:
        i = i + 1
        print(i)
        print(statement)
        response_text = stemwijzer(statement)
        print(response_text)