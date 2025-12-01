# CP1404 Practical Reflection

Write short but thoughtful answers to each of the following.  
Replace each `...` with your meaningful answer.

## Estimates

Regarding the **estimates** that you did for practical tasks...

### How was your estimate accuracy usually?

My estimate accuracy at the start was not great. I usually underestimated tasks because I assumed things would work on the first attempt. I did not fully account for debugging or clarifying instructions, so my estimates were often too optimistic.

### How did your estimate accuracy improve or change during the course of the subject?

My estimates improved once I started noticing patterns in how long different types of tasks took. I also learned to include time for testing, cleaning up code and handling unexpected issues. This made my estimates more realistic.

### What did you learn from doing these estimates?

I learned that good estimates come from experience and reflection, not guessing. Breaking tasks into smaller parts helped a lot, and I realised how important it is to include buffer time for problems that appear during coding.

## Code Reviews

### What have you learned from being reviewed by other people?

I learned that other people can catch issues that I miss, especially things related to clarity, coding conventions and small mistakes. Reviews helped me see my code from another perspective and understand how important clean structure and naming are.

### What have you learned from doing code reviews of other people?

Doing reviews made me more aware of my own coding habits. When I pointed out things like magic numbers or messy formatting, I noticed I often made similar mistakes. Reviewing others helped me understand how to give clear and constructive feedback.

Provide proper Markdown links (not bare URLs) to two (2) PRs that show you doing good code reviews for any of the past
pracs.  
For each one, write a short explanation of what was good about your review.

### Good Code Review 1

[HongJCU Pull Request #3](https://github.com/HongJCU/cp1404practicals/pull/3)

### Explanation

This was one of my most thorough reviews. I highlighted several areas for improvement, including adding validation loops to prevent crashes from invalid numeric input, handling FileNotFoundError properly when loading projects and replacing hard coded values such as the year 2022 with datetime.now().year to make the code future proof. I also suggested removing unnecessary second docstrings and improving formatting with clearer multi line f strings. I pointed out inconsistencies between the date input format and the parser, clarified how sorting guitars by year works and noted a small CSV formatting issue. The review aimed to improve robustness, readability and maintainability.

### Good Code Review 2

[elijahangJCU Pull Request #2](https://github.com/elijahangJCU/cp1404practicals/pull/2)

### Explanation

I have not been asked to formally review another student’s work besides the first PR, so instead I am reflecting on a good review that another student gave me. AshleyTXH10 gave specific and helpful suggestions. They pointed out magic numbers in guitar.py such as the year 2025 and the threshold 50, advising that they be declared as constants. They suggested adding default values to the __init__ method in programming_language.py and recommended following the GitHub test pattern for used_cars.py. Their feedback was focused, actionable and aimed at improving code structure, maintainability and consistency.

## Practicals

### Regarding the **practical tasks** overall, what would you change if you were in charge of the subject?

I would include short video walkthroughs for the more complex pracs. Sometimes seeing the steps visually makes the instructions easier to follow. I would also add a simple checklist at the end of each prac so students can quickly confirm they have completed all required parts.

### What did you do really well for practicals in this subject?

I improved a lot in writing cleaner and more readable code. I became more consistent with functions, SRP and error handling. I also pushed myself to properly test my programs instead of assuming they were correct immediately. Reusable functions and organised structure made later pracs much easier to manage.