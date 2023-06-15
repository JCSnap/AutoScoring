AUTOSCORING_INSTRUCTION = """
You are a teacher. You will be given a question, a model answer, and a student's answer. 
You are tasked to grade your student's answer out of 100 based on its accuracy when compared to the model answer and question. 
1. Allow some leeway for correct answers, even if it does not follow the model answer word for word.
2. Do not provide explanation, just give the score.
3. Even if the student's answer contains words from the model answer, it does not mean that it is correct.
"""

QUESTION_SCIENTIFIC_METHOD = {
    "question": "What are some key principles of the scientific method?",
    "model_answer": "The scientific method includes making observations, formulating a hypothesis, conducting experiments, analyzing data, and drawing conclusions. Results should be reproducible and subject to peer review.",
    "student_answer": "Experiments and stuff"
}

QUESTION = [
    {
        "question": "How does fiscal policy influence economic growth and how might it impact inflation?",
        "model_answer": "Fiscal policy, which involves government decisions about taxation and spending, can significantly influence economic growth. When a government increases spending (expansionary fiscal policy), it injects more money into the economy, which can stimulate economic activity and lead to growth. This occurs as government spending increases demand for goods and services, prompting businesses to increase production and potentially hire more workers. However, expansionary fiscal policy can also lead to inflation. As demand for goods and services increases, prices can rise due to heightened competition among consumers for the available supply of goods and services. This is demand-pull inflation. On the other hand, contractionary fiscal policy, which involves reducing spending or increasing taxes, can slow economic growth by reducing the amount of money in circulation. This policy can be used to control inflation but, if implemented during a weak economy, it could potentially exacerbate economic downturns. Therefore, while fiscal policy is a powerful tool for managing economic growth and inflation, it needs to be used judiciously to balance these two often conflicting economic objectives.",
        "student_answer": "Fiscal policy, including government decisions about taxes and spending, can influence economic growth. When the government decreases taxes, it directly leads to economic growth because people will have more money to spend. This extra money allows consumers to buy more goods and services, which causes businesses to increase production. Inflation, on the other hand, is not influenced by fiscal policy but is more related to the actions of the central bank and its management of the money supply."
    }
]
QUESTIONS = [
    {
        "question": "What is the greenhouse effect and how does it contribute to global warming?",
        "model_answer": "The greenhouse effect is the natural process of gases in Earth's atmosphere trapping heat, maintaining the planet's temperature. Human activities like burning fossil fuels have increased these gases, enhancing the effect and causing global warming.",
        "student_answer": "The greenhouse effect is when Earth gets hotter due to gases in the air. Things like cars and factories cause more gases, which leads to global warming."
    },

    {
        "question": "Describe the process of mitosis in cell division.",
        "model_answer": "Mitosis is a process of cell division, resulting in two identical cells from one parent cell. It involves stages - Prophase, Metaphase, Anaphase, Telophase, and then Cytokinesis, where the cell divides.",
        "student_answer": "Mitosis is how a cell divides to make more cells. It has steps like Prophase, Metaphase, Anaphase, Telophase, and then the cell splits into two."
    },

    {
        "question": "How did the Industrial Revolution impact society and economy in the 19th century?",
        "model_answer": "The Industrial Revolution shifted economy from agrarian to industry-based, causing urbanization and emergence of a working class. Economically, it led to growth and wealth generation, but also economic disparity and social issues.",
        "student_answer": "The Industrial Revolution made people move to cities for factory jobs. It made some people very rich but also led to problems like child labor."
    },

    {
        "question": "What are some key principles of the scientific method?",
        "model_answer": "The scientific method includes making observations, formulating a hypothesis, conducting experiments, analyzing data, and drawing conclusions. Results should be reproducible and subject to peer review.",
        "student_answer": "The scientific method is about observing, guessing, doing experiments, checking data, and deciding if you're right. Other people should also be able to do the same experiment and get the same result."
    },

    {
        "question": "How does photosynthesis work in plants?",
        "model_answer": "Photosynthesis is the process where plants use sunlight to convert carbon dioxide and water into glucose and oxygen. This process is vital for the plant's growth and releasing oxygen into the atmosphere.",
        "student_answer": "Photosynthesis is how plants make food and oxygen. They use sunlight, air, and water to do it."
    },

    {
        "question": "What were the causes and effects of the American Civil War?",
        "model_answer": "The American Civil War was caused by disputes over slavery and states' rights. Its effects included the abolition of slavery, significant loss of life, economic change, and laying the groundwork for modern America.",
        "student_answer": "The American Civil War happened because of fights over slavery. It ended slavery, caused many deaths, changed the economy, and helped shape America."
    },
]

QUESTIONS2 = [
    {
        "question": "How does gravity work?",
        "model_answer": "Gravity is the force that attracts two objects toward each other. The greater the mass of an object, the stronger its gravitational pull. This is why Earth, being much more massive than us, pulls us towards its center, keeping us grounded.",
        "student_answer": "Gravity is like a force that pulls things together. It's why we don't float off the ground, because Earth's gravity is pulling us down."
    },
    {
        "question": "What is the function of the heart in the human body?",
        "model_answer": "The heart's main function is to pump blood throughout the body, delivering oxygen and nutrients to the tissues and removing carbon dioxide and other wastes.",
        "student_answer": "The heart is like a pump for the body. It sends blood all around to give oxygen and food to our body parts and take away the bad stuff."
    },
    {
        "question": "What was the Enlightenment, and how did it change society?",
        "model_answer": "The Enlightenment was an intellectual and philosophical movement in 18th-century Europe. It promoted reason, science, and individual rights, influencing the development of democratic institutions and sparking societal and political changes.",
        "student_answer": "The Enlightenment was when people in Europe started thinking more about science and reason. It made society more focused on individuals and led to changes in government."
    },
    {
        "question": "What is natural selection and how does it contribute to evolution?",
        "model_answer": "Natural selection is a process where individuals with advantageous traits are more likely to survive and reproduce, passing these traits to the next generation. Over time, this can lead to significant changes in species, a process known as evolution.",
        "student_answer": "Natural selection is when animals with better skills survive and have babies. Over a long time, this can change the whole species, which is called evolution."
    },
    {
        "question": "What are renewable energy sources and why are they important?",
        "model_answer": "Renewable energy sources are those that can be replenished naturally in a short time, like solar, wind, and hydro energy. They are important because they are sustainable, reduce dependence on fossil fuels, and help mitigate climate change.",
        "student_answer": "Renewable energy comes from things that don't run out, like sun, wind, and water. They're good because they won't finish, don't need fossil fuels, and don't harm the environment."
    },
    {
        "question": "How did World War II impact the world politically and socially?",
        "model_answer": "World War II led to significant political changes, including the emergence of the United States and the Soviet Union as superpowers. Socially, it fostered movements for decolonization and civil rights, but also caused devastating loss of life and displacement.",
        "student_answer": "After World War II, the USA and the Soviet Union became superpowers. It also made people fight for their rights and freedom, but many people died or lost their homes."
    },
    {
        "question": "What are plate tectonics and how do they contribute to earthquakes and volcanic activity?",
        "model_answer": "Plate tectonics is the theory that Earth's crust is made of large pieces that move over time. Their movement can cause earthquakes when they grind against each other, or volcanic activity when one plate is forced under another and melts.",
        "student_answer": "Plate tectonics is about Earth's crust being like puzzle pieces moving around. When they hit or slide past each other, it can cause earthquakes. Volcanoes can happen when one piece goes under another and melts."
    },
    {
        "question": "What is artificial intelligence and how is it used in everyday life?",
        "model_answer": "Artificial intelligence (AI) is a field of computer science focused on creating systems that perform tasks that usually require human intelligence. In everyday life, AI is used in various ways, from voice assistants like Siri or Alexa to recommendation systems on streaming platforms.",
        "student_answer": "Artificial intelligence is like when computers can do things like humans. We use it in our daily life like when we talk to Siri or Alexa, or when Netflix suggests a movie we might like."
    },
    {
        "question": "How did the French Revolution impact France and Europe?",
        "model_answer": "The French Revolution marked the end of absolute monarchy in France and introduced democratic principles. It also sparked a wave of revolutions across Europe, leading to political and social change.",
        "student_answer": "The French Revolution made France a democracy and ended the king's rule. It also led to other revolutions in Europe and changed society and government."
    },
    {
        "question": "What is the theory of relativity and who proposed it?",
        "model_answer": "The theory of relativity, proposed by Albert Einstein, includes two parts: special relativity and general relativity. Special relativity states that the laws of physics are the same for all non-accelerating observers and that the speed of light is the same for all observers. General relativity is a theory of gravitation where gravity is not a force but a curvature in space-time caused by mass and energy.",
        "student_answer": "Relativity is a big idea from Einstein. It says stuff about how light speed is always the same and gravity is like a bend in space. Or something like that."
    },
    {
        "question": "What are human rights and why are they important?",
        "model_answer": "Human rights are the basic rights and freedoms to which all individuals are entitled, such as the right to life, liberty, free speech, and privacy. They are important because they ensure dignity, equality, and respect for all people, regardless of nationality, sex, ethnicity, religion, or other status.",
        "student_answer": "Human rights are like, the rules that say everyone should be treated fairly and can do things like talk freely, live safely, and have privacy. They're important because they make sure everyone is respected."
    },
    {
        "question": "What is quantum physics and how does it challenge our understanding of the physical world?",
        "model_answer": "Quantum physics, or quantum mechanics, is a branch of physics that deals with phenomena on a very small scale, such as molecules, atoms, and subatomic particles. It challenges our understanding of the physical world because it includes principles that seem counterintuitive, such as superposition (particles can be in multiple places at once) and entanglement (particles can be instantly connected regardless of distance).",
        "student_answer": "Quantum physics is about really tiny stuff like atoms and even smaller things. It's weird and tricky because it says stuff can be in more than one place at the same time and particles can talk to each other instantly even if they're far away."
    },
    {
        "question": "What is a black hole and how is it formed?",
        "model_answer": "A black hole is a region of space where gravity is so strong that nothing, not even light, can escape from it. They are formed when a large star collapses under its own gravity after depleting its nuclear fuel.",
        "student_answer": "Black holes are like these big space things that suck everything in, even light can't escape. They happen when a star, like, explodes or something and then falls in on itself."
    },
    {
        "question": "What is photosynthesis and why is it important to life on Earth?",
        "model_answer": "Photosynthesis is a process used by plants, algae, and some bacteria to convert light energy, usually from the Sun, into chemical energy in the form of glucose. It's crucial for life on Earth as it produces oxygen and serves as the base of the food chain.",
        "student_answer": "Photosynthesis is what plants do to make food using sunlight. It's important because it makes oxygen, which we need to breathe, and it also feeds the plants, and then the animals eat the plants, and we eat the plants and animals."
    }
]

QUESTIONS_WRONG = [
    {
        "question": "What is the structure of an atom?",
        "model_answer": "An atom consists of a central nucleus, which contains protons and neutrons, surrounded by a cloud of electrons that move in orbital shells.",
        "student_answer": "An atom is like a solar system, with the sun in the middle and planets going around it."
    },
    {
        "question": "Why is the ozone layer important?",
        "model_answer": "The ozone layer absorbs most of the Sun's harmful ultraviolet (UV) radiation, which can cause skin cancer and cataracts in humans and harm ecosystems.",
        "student_answer": "The ozone layer is important because it gives us air to breathe."
    },
    {
        "question": "What is the difference between a democracy and a dictatorship?",
        "model_answer": "In a democracy, power is held by the people who elect leaders and have the right to participate in decision-making. In a dictatorship, power is concentrated in the hands of a single leader or a small group, and citizens have limited freedom and political participation.",
        "student_answer": "Democracy and dictatorship are types of money systems. In democracy, money is divided equally, and in dictatorship, one person has all the money."
    },
    {
        "question": "What causes the seasons to change?",
        "model_answer": "Seasonal changes are caused by the tilt of Earth's axis as it orbits the Sun. This tilt means that different parts of Earth receive different amounts of sunlight at different times of the year.",
        "student_answer": "Seasons change because the distance between Earth and Sun changes. When Earth is close to the Sun, it's summer, and when it's far, it's winter."
    },
    {
        "question": "What is the function of the kidneys in the human body?",
        "model_answer": "The kidneys filter the blood to remove waste products and excess substances, which are excreted as urine. They also help regulate blood pressure, electrolyte balance, and red blood cell production.",
        "student_answer": "The kidneys are like storage units in the body where extra food and nutrients are stored for when we need them."
    }
]

QUESTIONS_WRONG2 = [
    {
        "question": "What are greenhouse gases and how do they affect the Earth's climate?",
        "model_answer": "Greenhouse gases, like carbon dioxide and methane, trap heat in Earth's atmosphere, creating a 'greenhouse effect.' This effect is essential for life by keeping the planet warm, but an excess of these gases can cause global warming and climate change.",
        "student_answer": "Greenhouse gases are toxic gases that plants give off. They harm the Earth's climate by causing acid rain."
    },
    {
        "question": "What is DNA and what role does it play in our bodies?",
        "model_answer": "DNA, or deoxyribonucleic acid, is the molecule that carries the genetic instructions for growth, development, functioning, and reproduction of all known living organisms. It determines our physical characteristics and influences our health.",
        "student_answer": "DNA is like a battery that powers our bodies. Without DNA, we wouldn't have any energy."
    },
    {
        "question": "What are the primary colors and how can they be used to make other colors?",
        "model_answer": "The primary colors are red, blue, and yellow. By mixing these primary colors, we can create secondary colors: red and blue make purple, blue and yellow make green, and red and yellow make orange.",
        "student_answer": "The primary colors are red, white, and blue. They make all other colors, like red and white make pink, and blue and white make light blue."
    },
    {
        "question": "What is the process of evaporation in the water cycle?",
        "model_answer": "Evaporation is the process where water changes from a liquid state to a gas or vapor, typically under the heat of the sun. This process is a key part of the water cycle, allowing water to travel from Earth's surface to the atmosphere, where it can condense and fall back to the surface as precipitation.",
        "student_answer": "Evaporation is when water disappears. Like, if you leave a glass of water outside, after a few days, there's less water. It just vanishes."
    },
    {
        "question": "How does photosynthesis work and why is it important?",
        "model_answer": "Photosynthesis is a process used by plants and certain other organisms to convert light energy, usually from the Sun, into chemical energy in the form of glucose, which provides nutrients to the organisms. It also produces oxygen, which is vital for most life forms on Earth.",
        "student_answer": "Photosynthesis is when plants eat sunlight and turn it into color. That's why plants are green. It's important because it makes the plants look nice."
    }
]

QUESTIONS_CORRECT_BUT_LAYMAN = [
    {
        "question": "What is the law of supply and demand?",
        "model_answer": "The law of supply and demand is an economic theory that explains how a market balances price and the quantity of goods sold. When demand increases and supply remains the same, the price goes up. Conversely, if supply increases and demand remains the same, the price goes down.",
        "student_answer": "It's kind of like a see-saw. If more people want something and there's not enough, the price goes up. But if there's a lot of something and people don't want it, the price goes down."
    },
    {
        "question": "What is photosynthesis?",
        "model_answer": "Photosynthesis is a process used by plants and certain other organisms to convert light energy, typically from the Sun, into chemical energy in the form of glucose, which provides nutrients to the organisms.",
        "student_answer": "It's like how plants eat sunlight and make it into their food."
    },
    {
        "question": "What is a constitutional monarchy?",
        "model_answer": "A constitutional monarchy is a form of government in which a monarch acts as head of state within the parameters of a written or unwritten constitution. The monarch's roles are largely ceremonial with the real power lying with other political leaders.",
        "student_answer": "It's when a country has a king or queen, but they're more like a figurehead. The real decisions are made by other leaders."
    },
    {
        "question": "What is the theory of evolution by natural selection?",
        "model_answer": "The theory of evolution by natural selection, proposed by Charles Darwin, suggests that traits that enhance survival and reproduction become more common over generations in a population, leading to changes over time and potentially new species.",
        "student_answer": "It's like survival of the fittest. The animals with the best traits for survival have more babies and over time, the population changes."
    },
    {
        "question": "What is the principle of conservation of energy?",
        "model_answer": "The principle of conservation of energy states that energy can neither be created nor destroyed; instead, it can only be transferred or changed from one form to another.",
        "student_answer": "It's like saying energy just changes its outfit but never disappears or magically appears from nowhere."
    }
]

QUESTIONS_CORRECT_BUT_GRAMMAR_BAD = [
    {
        "question": "What is photosynthesis?",
        "model_answer": "Photosynthesis is a process used by plants and other organisms to convert light energy, typically from the Sun, into chemical energy in the form of glucose, which fuels their activities.",
        "student_answer": "Photosynthesis be like plants taking sun light and making it into food for themselves."
    },
    {
        "question": "How does gravity work?",
        "model_answer": "Gravity is a force that attracts two objects towards each other. The more massive an object is, the stronger its gravitational pull. It's why we stay on the ground instead of floating off into space.",
        "student_answer": "Gravity is like magnet, but for all things. Big stuff have more gravity. It why we don't fly off Earth."
    },
    {
        "question": "What is the water cycle?",
        "model_answer": "The water cycle describes how water evaporates from the surface of the earth, rises into the atmosphere, cools and condenses into clouds, and falls back to the surface as precipitation.",
        "student_answer": "Water cycle is when water go up into sky, turn into cloud, then fall back down as rain or snow."
    },
    {
        "question": "What is democracy?",
        "model_answer": "Democracy is a system of government where citizens exercise power by voting. In a direct democracy, the citizens as a whole form a governing body. In a representative democracy, citizens vote for representatives to handle legislation and governing.",
        "student_answer": "Democracy where people vote and decide things. Sometimes all people decide, sometime they pick other people for decide."
    },
    {
        "question": "What is a food chain?",
        "model_answer": "A food chain is a linear sequence of organisms where each one is eaten by the next member in the sequence. It begins with producer organisms, like plants, and ends with apex predators, followed by decomposers.",
        "student_answer": "Food chain is like line of eating. Plant get eaten by small animals, them get eaten by big animals, then big animals die and get eaten by tiny bugs and stuff."
    }
]

QUESTIONS_CORRECT_BUT_KEYWORD_PHRASING_DIFFERENT = [
    {
        "question": "What is the theory of plate tectonics?",
        "model_answer": "The theory of plate tectonics postulates that the Earth's crust is made up of large pieces, or plates, that move around due to convection currents in the underlying mantle. These movements cause earthquakes, volcanic activity, and the creation of mountain ranges.",
        "student_answer": "Earth's surface isn't one solid piece. It's like a giant jigsaw puzzle with big chunks that move about. These chunks bumping into each other or pulling apart, that's what makes volcanoes, mountains, and shakes."
    },
    {
        "question": "What is photosynthesis?",
        "model_answer": "Photosynthesis is a process used by plants and other organisms to convert light energy, typically from the Sun, into chemical energy in the form of glucose, which fuels their activities.",
        "student_answer": "Plants have this cool trick where they take sunlight and whip it up into their food, sort of like cooking up a meal!"
    },
    {
        "question": "What is democracy?",
        "model_answer": "Democracy is a system of government where citizens exercise power by voting. In a direct democracy, the citizens as a whole form a governing body. In a representative democracy, citizens vote for representatives to handle legislation and governing.",
        "student_answer": "Democracy is like having a say in how things are run. You get a vote to choose who makes the rules. Sometimes it's everyone deciding together, other times we pick some folks to do the decision making for us."
    },
    {
        "question": "What is the water cycle?",
        "model_answer": "The water cycle describes how water evaporates from the surface of the earth, rises into the atmosphere, cools and condenses into clouds, and falls back to the surface as precipitation.",
        "student_answer": "Water doesn't just stay still, it goes on a journey! It can turn into vapor and go up into the sky, then cools down and comes back down as rain or snow."
    },
    {
        "question": "What is a food chain?",
        "model_answer": "A food chain is a linear sequence of organisms where each one is eaten by the next member in the sequence. It begins with producer organisms, like plants, and ends with apex predators, followed by decomposers.",
        "student_answer": "Food chain? That's just the order of who eats who in nature. It starts with plants and ends with the big, scary predators. Once they're gone, the leftovers are handled by those cleanup bugs and organisms."
    }
]

QUESTIONS_PARTIALLY_CORRECT = [
    {
        "question": "What is photosynthesis?",
        "model_answer": "Photosynthesis is a process used by plants and other organisms to convert light energy, typically from the Sun, into chemical energy in the form of glucose, which fuels their activities.",
        "student_answer": "Photosynthesis is when plants make their food using sunlight."
    },
    {
        "question": "What is the theory of evolution by natural selection?",
        "model_answer": "The theory of evolution by natural selection, proposed by Charles Darwin, suggests that traits that enhance survival and reproduction become more common over generations in a population, leading to changes over time and potentially new species.",
        "student_answer": "Evolution by natural selection is about how animals change over time."
    },
    {
        "question": "What is a constitutional monarchy?",
        "model_answer": "A constitutional monarchy is a form of government in which a monarch acts as head of state within the parameters of a written or unwritten constitution. The monarch's roles are largely ceremonial with the real power lying with other political leaders.",
        "student_answer": "A constitutional monarchy is when a country has a king or queen."
    },
    {
        "question": "What is the principle of conservation of energy?",
        "model_answer": "The principle of conservation of energy states that energy can neither be created nor destroyed; instead, it can only be transferred or changed from one form to another.",
        "student_answer": "Conservation of energy means that energy doesn't disappear."
    },
    {
        "question": "What is the water cycle?",
        "model_answer": "The water cycle describes how water evaporates from the surface of the earth, rises into the atmosphere, cools and condenses into clouds, and falls back to the surface as precipitation.",
        "student_answer": "The water cycle is about how water moves from the ground to the sky and back."
    }
]

QUESTIONS_CORRECT_BUT_INCORRECT_TERMS = [
    {
        "question": "What is photosynthesis?",
        "model_answer": "Photosynthesis is a process used by plants and other organisms to convert light energy, typically from the Sun, into chemical energy in the form of glucose, which fuels their activities.",
        "student_answer": "Photosynthesis is when plants sunbake and make their own food-energy stuff."
    },
    {
        "question": "What is a constitutional monarchy?",
        "model_answer": "A constitutional monarchy is a form of government in which a monarch acts as head of state within the parameters of a written or unwritten constitution. The monarch's roles are largely ceremonial with the real power lying with other political leaders.",
        "student_answer": "A constitutional monarchy is where the king or queen is just for show, and the real boss work is done by the leader dudes."
    },
    {
        "question": "What is the principle of conservation of energy?",
        "model_answer": "The principle of conservation of energy states that energy can neither be created nor destroyed; instead, it can only be transferred or changed from one form to another.",
        "student_answer": "Conservation of energy means energy can't poof into or out of existence, it just changes its disguise."
    },
    {
        "question": "What is the theory of evolution by natural selection?",
        "model_answer": "The theory of evolution by natural selection, proposed by Charles Darwin, suggests that traits that enhance survival and reproduction become more common over generations in a population, leading to changes over time and potentially new species.",
        "student_answer": "Evolution by natural selection is like the survival game where the best fit creatures pass on their winning traits to their babies, causing creature change over a long, long time."
    },
    {
        "question": "What is the water cycle?",
        "model_answer": "The water cycle describes how water evaporates from the surface of the earth, rises into the atmosphere, cools and condenses into clouds, and falls back to the surface as precipitation.",
        "student_answer": "The water cycle is how water goes on its vacation - evaporating and becoming sky water, then falling back as rain or snow."
    }
]

QUESTIONS_MISUNDERSTOOD_CONCEPTS = [
    {
        "question": "What is photosynthesis?",
        "model_answer": "Photosynthesis is a process used by plants and other organisms to convert light energy, typically from the Sun, into chemical energy in the form of glucose, which fuels their activities.",
        "student_answer": "Photosynthesis is how plants grow by absorbing water from the sun."
    },
    {
        "question": "What is a constitutional monarchy?",
        "model_answer": "A constitutional monarchy is a form of government in which a monarch acts as head of state within the parameters of a written or unwritten constitution. The monarch's roles are largely ceremonial with the real power lying with other political leaders.",
        "student_answer": "A constitutional monarchy is a government where the king or queen makes the laws according to the constitution."
    },
    {
        "question": "What is the principle of conservation of energy?",
        "model_answer": "The principle of conservation of energy states that energy can neither be created nor destroyed; instead, it can only be transferred or changed from one form to another.",
        "student_answer": "Conservation of energy means that you always have to save energy, like turning off lights when you leave a room."
    },
    {
        "question": "What is the theory of evolution by natural selection?",
        "model_answer": "The theory of evolution by natural selection, proposed by Charles Darwin, suggests that traits that enhance survival and reproduction become more common over generations in a population, leading to changes over time and potentially new species.",
        "student_answer": "Evolution by natural selection means that the strongest animals always survive and the weak ones die."
    },
    {
        "question": "What is the water cycle?",
        "model_answer": "The water cycle describes how water evaporates from the surface of the earth, rises into the atmosphere, cools and condenses into clouds, and falls back to the surface as precipitation.",
        "student_answer": "The water cycle is when water goes down the drain, gets cleaned, and then we can drink it again."
    }
]

QUESTIONS_WRONG_BUT_CORRECT_TERMS = [
    {
        "question": "What is photosynthesis?",
        "model_answer": "Photosynthesis is a process used by plants and other organisms to convert light energy, typically from the Sun, into chemical energy in the form of glucose, which fuels their activities.",
        "student_answer": "Photosynthesis is when sunlight turns into glucose which then makes plants grow bigger."
    },
    {
        "question": "What is a constitutional monarchy?",
        "model_answer": "A constitutional monarchy is a form of government in which a monarch acts as head of state within the parameters of a written or unwritten constitution. The monarch's roles are largely ceremonial with the real power lying with other political leaders.",
        "student_answer": "A constitutional monarchy is when the monarch writes the constitution and decides the laws of the state."
    },
    {
        "question": "What is the principle of conservation of energy?",
        "model_answer": "The principle of conservation of energy states that energy can neither be created nor destroyed; instead, it can only be transferred or changed from one form to another.",
        "student_answer": "Conservation of energy means that energy always stays the same, it never changes."
    },
    {
        "question": "What is the theory of evolution by natural selection?",
        "model_answer": "The theory of evolution by natural selection, proposed by Charles Darwin, suggests that traits that enhance survival and reproduction become more common over generations in a population, leading to changes over time and potentially new species.",
        "student_answer": "Evolution by natural selection is about how the smartest animals survive and the dumb ones die out."
    },
    {
        "question": "What is the water cycle?",
        "model_answer": "The water cycle describes how water evaporates from the surface of the earth, rises into the atmosphere, cools and condenses into clouds, and falls back to the surface as precipitation.",
        "student_answer": "The water cycle is when water turns into vapor, then it cools down in the fridge and we can drink it."
    }
]

QUESTIONS_CORRECT_BUT_WRONG_REASONING = [
    {
        "question": "What is photosynthesis?",
        "model_answer": "Photosynthesis is a process used by plants and other organisms to convert light energy, typically from the Sun, into chemical energy in the form of glucose, which fuels their activities.",
        "student_answer": "Photosynthesis is when plants eat sunlight and then they sweat out glucose."
    },
    {
        "question": "What is a constitutional monarchy?",
        "model_answer": "A constitutional monarchy is a form of government in which a monarch acts as head of state within the parameters of a written or unwritten constitution. The monarch's roles are largely ceremonial with the real power lying with other political leaders.",
        "student_answer": "A constitutional monarchy is when the king or queen have to follow the constitution or else they lose their crown."
    },
    {
        "question": "What is the principle of conservation of energy?",
        "model_answer": "The principle of conservation of energy states that energy can neither be created nor destroyed; instead, it can only be transferred or changed from one form to another.",
        "student_answer": "Conservation of energy is when energy can't be destroyed or created, it just has to stay in a room."
    },
    {
        "question": "What is the theory of evolution by natural selection?",
        "model_answer": "The theory of evolution by natural selection, proposed by Charles Darwin, suggests that traits that enhance survival and reproduction become more common over generations in a population, leading to changes over time and potentially new species.",
        "student_answer": "Evolution by natural selection is when the biggest and toughest animals survive because they can fight off all the other animals."
    },
    {
        "question": "What is the water cycle?",
        "model_answer": "The water cycle describes how water evaporates from the surface of the earth, rises into the atmosphere, cools and condenses into clouds, and falls back to the surface as precipitation.",
        "student_answer": "The water cycle is when water from the ocean flies up to the sky, freezes into clouds, and then the clouds explode and the water comes back down."
    }
]

QUESTIONS_UNRELATED_IRRELEVANT = [
    {
        "question": "What is photosynthesis?",
        "model_answer": "Photosynthesis is a process used by plants and other organisms to convert light energy, typically from the Sun, into chemical energy in the form of glucose, which fuels their activities.",
        "student_answer": "Plants are really important because they give us oxygen so we can breathe."
    },
    {
        "question": "What is a constitutional monarchy?",
        "model_answer": "A constitutional monarchy is a form of government in which a monarch acts as head of state within the parameters of a written or unwritten constitution. The monarch's roles are largely ceremonial with the real power lying with other political leaders.",
        "student_answer": "Monarchs are like butterflies and bees. They are very important for pollinating flowers."
    },
    {
        "question": "What is the principle of conservation of energy?",
        "model_answer": "The principle of conservation of energy states that energy can neither be created nor destroyed; instead, it can only be transferred or changed from one form to another.",
        "student_answer": "Energy drinks can help you stay awake, but they're not good for you."
    },
    {
        "question": "What is the theory of evolution by natural selection?",
        "model_answer": "The theory of evolution by natural selection, proposed by Charles Darwin, suggests that traits that enhance survival and reproduction become more common over generations in a population, leading to changes over time and potentially new species.",
        "student_answer": "Darwin is a city in Australia. It's named after Charles Darwin who visited there on the HMS Beagle."
    },
    {
        "question": "What is the water cycle?",
        "model_answer": "The water cycle describes how water evaporates from the surface of the earth, rises into the atmosphere, cools and condenses into clouds, and falls back to the surface as precipitation.",
        "student_answer": "Water is very important. You should drink eight glasses a day to stay healthy."
    }
]

QUESTIONS_WRONG_COMPLETELY = [
    {
        "question": "What is photosynthesis?",
        "model_answer": "Photosynthesis is a process used by plants and other organisms to convert light energy, typically from the Sun, into chemical energy in the form of glucose, which fuels their activities.",
        "student_answer": "Photosynthesis is when plants take in carbon dioxide and release oxygen to help people breathe."
    },
    {
        "question": "What is a constitutional monarchy?",
        "model_answer": "A constitutional monarchy is a form of government in which a monarch acts as head of state within the parameters of a written or unwritten constitution. The monarch's roles are largely ceremonial with the real power lying with other political leaders.",
        "student_answer": "A constitutional monarchy is where the monarch has absolute power and controls everything."
    },
    {
        "question": "What is the principle of conservation of energy?",
        "model_answer": "The principle of conservation of energy states that energy can neither be created nor destroyed; instead, it can only be transferred or changed from one form to another.",
        "student_answer": "Conservation of energy means that we should use less energy to save the planet."
    },
    {
        "question": "What is the theory of evolution by natural selection?",
        "model_answer": "The theory of evolution by natural selection, proposed by Charles Darwin, suggests that traits that enhance survival and reproduction become more common over generations in a population, leading to changes over time and potentially new species.",
        "student_answer": "Evolution by natural selection is when an animal changes in its lifetime to survive better, and then passes these changes on to its offspring."
    },
    {
        "question": "What is the water cycle?",
        "model_answer": "The water cycle describes how water evaporates from the surface of the earth, rises into the atmosphere, cools and condenses into clouds, and falls back to the surface as precipitation.",
        "student_answer": "The water cycle is when water from the sea goes to the factories to be cleaned and then sent to our homes through pipes."
    }
]

QUESTIONS_NEGATIONS_AND_EXCEPTIONS = [
    {
        "question": "Is it accurate to say that all birds can fly?",
        "model_answer": "No, it is not accurate to say that all birds can fly. While many bird species have the ability to fly, there are some exceptions such as penguins, ostriches, and kiwis that are flightless.",
        "student_answer": "Yeah, all birds can fly, that's what makes them birds."
    },
    {
        "question": "Do all plants produce flowers?",
        "model_answer": "No, not all plants produce flowers. Many plants, like ferns and mosses, reproduce through spores rather than producing flowers.",
        "student_answer": "Yes, all plants make flowers because they need to produce seeds."
    },
    {
        "question": "Is it correct to say that all mammals lay eggs?",
        "model_answer": "No, it is not correct to say that all mammals lay eggs. Most mammals give birth to live young. However, there are exceptions, such as the platypus and the echidna, which are mammals that do lay eggs.",
        "student_answer": "Yes, mammals lay eggs. That's how they have babies."
    },
    {
        "question": "Are all chemical reactions fast?",
        "model_answer": "No, not all chemical reactions are fast. While some reactions, like explosions, occur nearly instantaneously, others, such as rusting, can take years.",
        "student_answer": "Yes, all chemical reactions are fast. That's why they are called reactions."
    },
    {
        "question": "Does heat always flow from colder to hotter objects?",
        "model_answer": "No, heat does not flow from colder to hotter objects. It flows from hotter to colder objects in order to equalize the temperature between the two.",
        "student_answer": "Yes, heat flows from colder to hotter objects. That's how things get warmed up."
    }
]

QUESTIONS_CORRECT_BUT_DIFFERENT_CONTEXT = [
    {
        "question": "What is the theory of relativity?",
        "model_answer": "The theory of relativity, developed by Albert Einstein, fundamentally changed our understanding of physics, introducing concepts like space-time and energy-mass equivalence. It consists of two parts: special relativity and general relativity.",
        "student_answer": "Relativity is when you look at something from different points of view. Like, if I say a car is moving fast, it's relative to whether I'm standing still or moving in the same direction."
    },
    {
        "question": "What is the role of mitochondria in a cell?",
        "model_answer": "Mitochondria are often referred to as the 'powerhouse of the cell' because they generate most of the cell's supply of adenosine triphosphate (ATP), used as a source of chemical energy.",
        "student_answer": "Mitochondria are important in our bodies because they provide us with energy. It's like eating food for our cells."
    },
    {
        "question": "What is the Industrial Revolution?",
        "model_answer": "The Industrial Revolution was a period of major industrialization and innovation that took place during the late 1700s and early 1800s. It marked a significant shift in history, influencing nearly every aspect of daily life.",
        "student_answer": "The Industrial Revolution is when people started to use machines to do work. Like, instead of making clothes by hand, they used sewing machines."
    },
    {
        "question": "What is the greenhouse effect?",
        "model_answer": "The greenhouse effect is a natural process where certain gases in Earth's atmosphere trap heat, preventing it from escaping into space and thereby keeping the planet warm enough to sustain life.",
        "student_answer": "Greenhouse effect is when you keep plants in a greenhouse so they can grow better. It's warmer inside and they get lots of sunlight."
    },
    {
        "question": "What is the Pythagorean theorem?",
        "model_answer": "The Pythagorean theorem is a fundamental principle in geometry, stating that in a right-angled triangle, the square of the length of the hypotenuse is equal to the sum of the squares of the other two sides.",
        "student_answer": "The Pythagorean theorem is like when you have a ladder leaning against a wall and you want to know how tall the ladder is or how far it is from the wall. It helps with that."
    }
]

QUESTIONS_GIBBERISH = [
    {
        "question": "What is the process of photosynthesis?",
        "model_answer": "Photosynthesis is the process by which green plants and some other organisms use sunlight to synthesize foods with the help of chlorophyll pigments. Essentially, they convert light energy into chemical energy, producing glucose and releasing oxygen as a byproduct.",
        "student_answer": "Flurple grunk photosmash chlorofill sun muncher."
    },
    {
        "question": "What is the significance of Shakespeare's work in English literature?",
        "model_answer": "Shakespeare's work is seminal in English literature due to his profound impact on language, storytelling, and theatrical practices. His plays and sonnets explore universal human themes and continue to influence modern literature and drama.",
        "student_answer": "Shakyspears big word tumbler story write funny hat guy."
    },
    {
        "question": "Explain the concept of gravitational force.",
        "model_answer": "Gravitational force is a force of attraction that exists between any two masses, any two bodies, any two particles. It is mathematically described by Newton's law of universal gravitation.",
        "student_answer": "Gravity umbo jumbo pull-push whoosh round round."
    },
    {
        "question": "How does the respiratory system function?",
        "model_answer": "The respiratory system's primary function is to supply the blood with oxygen so that the blood can deliver oxygen to all parts of the body. This process happens through breathing: inhaling oxygen-rich air and exhaling air filled with carbon dioxide, which is a waste product.",
        "student_answer": "Breath in out huff puff lung balloon air bag whoosh."
    },
    {
        "question": "What is the French Revolution?",
        "model_answer": "The French Revolution was a period of radical political and societal change in France that lasted from 1789 until 1799, leading to the end of monarchy and the rise of radical political forces.",
        "student_answer": "France spin topsy-turvy king no king baguette riot."
    }
]

QUESTIONS_SYNONYM = [
    {
        "question": "What is the process of photosynthesis?",
        "model_answer": "Photosynthesis is the process by which green plants and some other organisms use sunlight to synthesize foods with the help of chlorophyll pigments. Essentially, they convert light energy into chemical energy, producing glucose and releasing oxygen as a byproduct.",
        "student_answer": "Photosynthesis is how plants cook up their own food using sunshine and the green stuff in their leaves. They take light and turn it into food energy, and also let out oxygen."
    },
    {
        "question": "What is the significance of Shakespeare's work in English literature?",
        "model_answer": "Shakespeare's work is seminal in English literature due to his profound impact on language, storytelling, and theatrical practices. His plays and sonnets explore universal human themes and continue to influence modern literature and drama.",
        "student_answer": "Shakespeare's writings are super important in English literature because he really changed how we use words, tell stories, and put on plays. He wrote about things that everyone can relate to, and people are still influenced by his stuff today."
    },
    {
        "question": "Explain the concept of gravitational force.",
        "model_answer": "Gravitational force is a force of attraction that exists between any two masses, any two bodies, any two particles. It is mathematically described by Newton's law of universal gravitation.",
        "student_answer": "Gravitational force is like a magnetic pull that happens between any two things that have mass. It's what Newton was talking about when he said everything in the universe pulls on everything else."
    },
    {
        "question": "How does the respiratory system function?",
        "model_answer": "The respiratory system's primary function is to supply the blood with oxygen so that the blood can deliver oxygen to all parts of the body. This process happens through breathing: inhaling oxygen-rich air and exhaling air filled with carbon dioxide, which is a waste product.",
        "student_answer": "The job of the respiratory system is to get oxygen into the blood so the blood can take it to all parts of the body. This happens when we breathe: we suck in air that's full of oxygen and blow out air that's full of carbon dioxide, which is like the body's trash."
    },
    {
        "question": "What is the French Revolution?",
        "model_answer": "The French Revolution was a period of radical political and societal change in France that lasted from 1789 until 1799, leading to the end of monarchy and the rise of radical political forces.",
        "student_answer": "The French Revolution was when everything got turned upside down in France from 1789 to 1799. They kicked out the king and it was all about radical politics after that."
    }
]

QUESTIONS_COMPLEX_STRCUTURES = [
    {
        "question": "What is the process of photosynthesis?",
        "model_answer": "Photosynthesis is the process by which green plants and some other organisms use sunlight to synthesize foods with the help of chlorophyll pigments. Essentially, they convert light energy into chemical energy, producing glucose and releasing oxygen as a byproduct.",
        "student_answer": "The mechanism by which organisms, like green plants, leverage the energy of the sun to create food substances is referred to as photosynthesis. The conversion of light energy into chemical energy happens here, resulting in the production of glucose and the expulsion of oxygen."
    },
    {
        "question": "What is the significance of Shakespeare's work in English literature?",
        "model_answer": "Shakespeare's work is seminal in English literature due to his profound impact on language, storytelling, and theatrical practices. His plays and sonnets explore universal human themes and continue to influence modern literature and drama.",
        "student_answer": "The body of work created by Shakespeare is regarded as a cornerstone in English literature, and this can be attributed to the transformative effect he had on language use, narrative techniques, and theater customs. His ability to address themes relatable to humanity is exhibited in his plays and sonnets, a practice that is still influential in contemporary literature and drama."
    },
    {
        "question": "Explain the concept of gravitational force.",
        "model_answer": "Gravitational force is a force of attraction that exists between any two masses, any two bodies, any two particles. It is mathematically described by Newton's law of universal gravitation.",
        "student_answer": "Gravitational force, as understood through the lens of Newton's law of universal gravitation, is described as an attractive force that manifests between any two entities that possess mass."
    },
    {
        "question": "How does the respiratory system function?",
        "model_answer": "The respiratory system's primary function is to supply the blood with oxygen so that the blood can deliver oxygen to all parts of the body. This process happens through breathing: inhaling oxygen-rich air and exhaling air filled with carbon dioxide, which is a waste product.",
        "student_answer": "The chief duty of the respiratory system is the provision of oxygen to the blood, which then transports this oxygen to various body parts. Oxygen-rich air is inhaled and carbon dioxide-filled air, a waste product, is exhaled in the act of breathing, which facilitates this process."
    },
    {
        "question": "What is the French Revolution?",
        "model_answer": "The French Revolution was a period of radical political and societal change in France that lasted from 1789 until 1799, leading to the end of monarchy and the rise of radical political forces.",
        "student_answer": "A transformative period in French history, spanning from 1789 to 1799, the French Revolution was characterized by dramatic shifts in political and social structures, most notably the demise of monarchy and the emergence of radical political factions."
    }
]


def format_answer(question, model_answer, student_answer):
    template = """
        Question: {}
        Model answer: {}
        Student answer: <> {} <>

        Format:
        Justification: [your justification]
        Score: [score]
    """.format(question, model_answer, student_answer)

    return template
