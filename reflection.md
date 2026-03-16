# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").
Answer: While the game is aesthetically pleasing, the first thing I noticed right off the bat is that the range in the game is completely wrong. It says I should input a number 1 to 100, but even when I input 1 it will tell me to go lower. In addition, range wise, I can input numbers outside the range regardless of what is given under the difficulty level. I was expecting to not be able to enter numbers outside the given range, and for the hints to be accurate in terms of whether I have to guess lower or higher. Another major bug that I noticed is that the "New Game" button doesn't work. While I can click it, nothing happens and I have to refresh the page in order to start a new game. I was expecting a new game to start. It was a really confusing game overall, if I'm being honest, and frustrating to play with so many apparent bugs. Another big bug was that the amount of attempts was off. Even if I had one attempt left, it would say game over, which was frustrating. 

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
I used Claude code, as reccomended, and I also chose to experiment with Gemini a little bit. 
An example of an AI suggestion that was correct is fixing the "if new game: " section. So basically, both AI suggested that the original logic behind this section didn't allow a new game to be played once this button was clicked as it assumed the user was still lost, and this glitch is now fixed. 
An example of an AI suggestion that was incorrect was the section: 
if guess > secret: return "Too High", "📈 Go HIGHER!"
else: return "Too Low", "📉 Go LOWER!"
It correctly identified that the guess was higher than the secret number, but then it told the player to "Go HIGHER!" This was a logic failure. 


---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?
To see if the New Game button and the Attempt Limit were actually fixed, I just ran a simple manual test by playing through a full round. First, I played until I used up all my guesses and the game told me I lost. Then, I clicked the "New Game" button and checked two things: I made sure the "Game Over" message disappeared immediately so I could actually type again, and I checked that my attempts reset back to 1 instead of staying stuck at the limit. Before the fix, the button was broken as a new game wasn't starting at all. The AI helped me understand this by explaining that even if you reset the number of attempts, you also have to clear out the "status" variable in the background, otherwise the app still thinks the previous game is happening and the user is still guessing. After I sucessfully fixed this, I was able to restart the game whenever and it would reset my attempt limits. 

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?
In the original app, the secret number kept changing because of the way Streamlit was designed. Every time I interacted with a button or a text box, Streamlit reran the entire script from top to bottom. In the old code, the line that picked the random number was just sitting there in the open, so every single click caused the app to restart and pick a brand-new number, making it impossible to win. If I was explaining it to a friend who has never used it before, I would say it's like a monolithic kernel in a way. If there's one bug, everything shuts down in a monolithic kernel. (I recently learned this in my operating systems class, so I thought it was a good example). Similarly in this case, Streamlit shuts down and reruns the entire script everytime you interact with any of the features of the game. To fix this and get a stable secret number, I used if "secret" not in st.session_state: to check that "battery" first. This tells the app that if a number was already saved, it should skip the random generator and keep using the original one, so the target stays put until the game is over.
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
One habit I’m definitely taking with me is manual logic tracing before I even try to fix the code. I realized during this project that just because the code runs doesn't mean it’s actually working. Sometimes you have to work throught the code and identify errors through testing manually. A code can run sucessfully, but it doesn't mean it is accurate. I think next time, I would like to ask AI more specific questions about how to fix a code and help me walk through it. One thing I learned is that often times, AI generated code is like a rough draft rather than a finished product. I still needs a human to investigate it for mistakes and manually check it, but if used properly, AI agents can be very useful when writing code. 
